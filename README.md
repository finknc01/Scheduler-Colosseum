# Scheduler-Colosseum

> **Three execution models enter the arena. One workload exposes what each is actually good at.**

## Project status

| Field | Current state |
|---|---|
| **Status** | **Planned — scheduled across the container, Kubernetes, and Slurm blocks** |
| **Current stage** | Campaign authored; no tournament round or platform comparison is claimed complete |
| **Lab environment** | Laptop-scale Docker/Kubernetes/Slurm labs; one physical GPU where practical; unsupported multi-node/multi-GPU behavior is modeled |
| **Evidence rule** | Comparisons use the same workload, explicit assumptions, and measured/observed evidence rather than preference |
| **Last plan sync** | 2026-08-19 |

## Purpose

Scheduler-Colosseum is a comparative execution and orchestration lab. A fictional organization is deciding how to run accelerated workloads, and three teams advocate different operating models:

- direct/containerized execution with Docker,
- Kubernetes orchestration,
- Slurm batch/HPC scheduling.

Docker is **not** treated as a scheduler. The experiment compares execution models and operational responsibilities, while also examining the scheduler behavior that Kubernetes and Slurm introduce.

The central question is:

> **Which execution model is the best fit for which workload, team, and operational problem?**

## Skills developed

- Linux process/container boundaries
- Docker and NVIDIA container-runtime concepts
- Kubernetes architecture, reconciliation, scheduling, and accelerator resource exposure
- NVIDIA device-plugin / GPU Operator concepts
- Slurm controller/node/partition/job/GRES concepts
- workload placement, failure behavior, reproducibility, and operations
- fair comparative experiment design

## Arena campaign

The files in [`missions/`](missions/) are authoritative.

| Round | Trial | Primary outcome |
|---|---|---|
| [00 — Bare Process Baseline](missions/00-weigh-in.md) | Define one neutral workload before adding orchestration | repeatable baseline + measurements |
| [01 — Docker](missions/01-docker.md) | Run the same workload as a container | container boundary + reproducibility evidence |
| [02 — Kubernetes](missions/02-kubernetes.md) | Run the same workload through Kubernetes | control-plane/scheduling behavior |
| [03 — Kubernetes GPU](missions/03-k8s-gpu.md) | Explain/test how GPUs become schedulable resources | device-resource path + real-vs-modeled note |
| [04 — Slurm](missions/04-slurm.md) | Submit the same workload through Slurm | batch-scheduling evidence |
| [05 — Comparison](missions/05-comparison.md) | Compare the contenders under the same rules | tradeoff matrix |
| [06 — Sabotage](missions/06-sabotage.md) | Introduce controlled failures and compare recovery/visibility | failure-behavior evidence |
| [Final — Architecture Verdict](missions/final-verdict.md) | Recommend different platforms for different fictional organizations | decision framework grounded in evidence |

## GPU support rule

Where the selected Linux/Kubernetes environment can safely expose the real NVIDIA GPU, use it. If local GPU passthrough or supported Operator deployment is impractical, keep the cluster CPU-based and model the accelerator control path explicitly.

Whole-GPU allocation can be hands-on where supported. **MIG must remain modeled/reference-only unless the selected GPU actually supports MIG.** Full GPU Operator deployment is an optional supported-hardware/cloud extension; understanding the control path is the core objective.

## Experimental-control rule

Keep one workload definition, one measurement sheet, and one assumptions list across all contenders. Do not silently change the workload to make a platform look better.

Useful comparison dimensions include:

- startup/submission path
- reproducibility
- resource declaration/allocation
- logs and operational visibility
- failure/retry semantics
- multi-user/queue behavior
- configuration burden
- GPU exposure where supported

## Completion condition

Scheduler-Colosseum is complete when you can explain, with evidence, why Docker, Kubernetes, and Slurm solve different operational problems and recommend an execution model without pretending there is one universal winner.
