# Neutral Workload

This directory defines the one workload used throughout Scheduler-Colosseum.

## Rule
Keep the workload behavior and `config.yaml` constant across:
1. bare process;
2. Docker;
3. Kubernetes;
4. Slurm.

Platform-specific files such as a Dockerfile, Kubernetes manifests, GPU resource configuration, and Slurm submission scripts should be created during their missions, not supplied here as answers.

## Baseline run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r workload/requirements.txt
COLOSSEUM_CONTESTANT=bare COLOSSEUM_RUN_ID=bare-001 \
  python workload/workload.py --config workload/config.yaml \
  --output artifacts/bare-001.json
```

The script performs deterministic CPU work and, when a compatible PyTorch/CUDA environment already exists, an optional GPU matrix workload. GPU support is supplementary; do not alter the base CPU workload just because one platform lacks GPU access.

## What to record
- platform / contender;
- run ID;
- workload/config version;
- wall time;
- CPU time reported by the workload;
- GPU use/availability where applicable;
- scheduler/startup delay measured externally;
- failure/retry behavior;
- resource requests/limits;
- notes about anything that changed.
