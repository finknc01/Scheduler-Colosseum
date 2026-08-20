# Round 02 — Kubernetes Takes the Gate

## Briefing
The platform team wants desired state, services, health checks, and automatic rescheduling.

## Objective
Understand control plane, worker nodes, pods, deployments/jobs, requests/limits, scheduling, and reconciliation.

## Build
Use a laptop-appropriate Kubernetes environment. Run the workload as a Job first. Inspect the request path from manifest → API → scheduler → kubelet → container runtime.

## Deliberate failure
Delete a pod or make a worker unavailable in a multi-node simulation. Observe which controller reacts and what state is recreated.

## Evidence
- component/request-path diagram
- manifest
- scheduler/event output
- recovery timeline

## Victory condition
You can distinguish containerization from orchestration and explain Kubernetes reconciliation from evidence.
