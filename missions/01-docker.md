# Round 01 — Docker Enters the Arena

## Briefing
The application team says containers solve deployment and therefore no scheduler is necessary.

## Objective
Understand images, containers, mounts, environment, process isolation, resource limits, and GPU exposure.

## Build
Package the baseline workload into a container. Run it with explicit inputs/outputs and, where supported, expose the NVIDIA GPU through the container runtime.

## Deliberate failure
Run once without a required mount/env value or without GPU exposure. Diagnose from inside and outside the container.

## Evidence
- Dockerfile/container definition
- image size/build notes
- direct vs container runtime comparison
- failure/recovery log

## Victory condition
You can explain what Docker gives you and what it does not provide for multi-user queueing, placement, or cluster recovery.
