# Round 04 — Slurm Answers the Bell

## Briefing
The HPC team says AI training is batch computing and wants queues, partitions, fair-share concepts, and explicit resource allocation.

## Objective
Understand Slurm controller/daemon roles, nodes, partitions, jobs, queues, and GRES GPU concepts.

## Build
Create a laptop-scale Slurm lab using lightweight VMs/containers or a small local setup. Submit the same baseline workload through `sbatch`/`srun` and observe job lifecycle.

## Deliberate failure
Request an unavailable resource, drain a worker, or stop a lab daemon. Use Slurm state and logs to explain the queued/failed behavior.

## Evidence
- Slurm component diagram
- job script
- queue/node state
- failure timeline

## Victory condition
You can explain why a batch scheduler feels different from Kubernetes even when both eventually start a process on a node.
