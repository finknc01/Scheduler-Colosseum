#!/usr/bin/env python3
"""Neutral Scheduler-Colosseum workload.

Keep this workload functionally the same across bare process, Docker,
Kubernetes, and Slurm runs. Platform-specific wrappers should change; this
program should not silently change between contenders.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import socket
import sys
import time
from pathlib import Path

import yaml


def cpu_work(iterations: int, payload_kb: int) -> str:
    payload = ("scheduler-colosseum" * 4096).encode()[: payload_kb * 1024]
    digest = b"seed"
    for i in range(iterations):
        digest = hashlib.sha256(digest + payload + str(i).encode()).digest()
    return digest.hex()


def optional_gpu_work(matrix_size: int, iterations: int) -> dict:
    try:
        import torch  # optional; do not add to base requirements solely for this lab
    except ImportError:
        return {"available": False, "used": False, "reason": "torch-not-installed"}

    available = bool(torch.cuda.is_available())
    if not available:
        return {"available": False, "used": False, "reason": "cuda-unavailable"}

    device = torch.device("cuda")
    torch.manual_seed(42)
    a = torch.randn((matrix_size, matrix_size), device=device)
    b = torch.randn((matrix_size, matrix_size), device=device)
    torch.cuda.synchronize()
    start = time.perf_counter()
    result = None
    for _ in range(iterations):
        result = a @ b
    torch.cuda.synchronize()
    elapsed = time.perf_counter() - start
    checksum = float(result[0, 0].item()) if result is not None else None
    return {
        "available": True,
        "used": True,
        "device": torch.cuda.get_device_name(0),
        "elapsed_seconds": elapsed,
        "checksum": checksum,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="workload/config.yaml")
    parser.add_argument("--output", default="artifacts/result.json")
    parser.add_argument("--gpu", choices=["auto", "off"], default="auto")
    args = parser.parse_args()

    with open(args.config, "r", encoding="utf-8") as handle:
        config = yaml.safe_load(handle)

    cpu_cfg = config.get("cpu", {})
    gpu_cfg = config.get("gpu", {})

    started = time.time()
    cpu_start = time.perf_counter()
    digest = cpu_work(
        int(cpu_cfg.get("iterations", 10000)),
        int(cpu_cfg.get("payload_kb", 32)),
    )
    cpu_elapsed = time.perf_counter() - cpu_start

    gpu_result = {"available": None, "used": False, "reason": "disabled"}
    if args.gpu == "auto" and bool(gpu_cfg.get("enabled_if_available", True)):
        gpu_result = optional_gpu_work(
            int(gpu_cfg.get("matrix_size", 1024)),
            int(gpu_cfg.get("iterations", 10)),
        )

    ended = time.time()
    result = {
        "workload_version": config.get("workload_version", 1),
        "hostname": socket.gethostname(),
        "platform": platform.platform(),
        "python": sys.version.split()[0],
        "pid": os.getpid(),
        "started_epoch": started,
        "ended_epoch": ended,
        "wall_seconds": ended - started,
        "cpu": {
            "elapsed_seconds": cpu_elapsed,
            "iterations": int(cpu_cfg.get("iterations", 10000)),
            "payload_kb": int(cpu_cfg.get("payload_kb", 32)),
            "digest": digest,
        },
        "gpu": gpu_result,
        "environment": {
            "contestant": os.getenv("COLOSSEUM_CONTESTANT", "unspecified"),
            "run_id": os.getenv("COLOSSEUM_RUN_ID", "unspecified"),
        },
    }

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
