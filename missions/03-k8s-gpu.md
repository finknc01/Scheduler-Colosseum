# Round 03 — The GPU Operator Trial

## Briefing
Kubernetes can schedule CPU workloads, but the arena now demands accelerators.

## Objective
Understand GPU discovery, device plugins/operators, resource advertisement, GPU requests, and sharing/MIG concepts.

## Build
Where your hardware/environment supports it, expose the laptop GPU to Kubernetes using the appropriate NVIDIA components. If the local cluster cannot safely support GPU passthrough, keep the cluster CPU-based and perform the GPU control-path portion as a clearly labeled architecture exercise.

## Deliberate failure
Create a pod that requests an unavailable GPU resource or deliberately omit a required GPU integration component in the lab. Diagnose why it remains pending or lacks device visibility.

## Evidence
- GPU resource path diagram
- node capacity/allocatable output
- pod scheduling events
- real-vs-modeled limitation note

## Victory condition
You can explain how a physical GPU becomes a schedulable Kubernetes resource.
