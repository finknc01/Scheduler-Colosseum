# Round 05 — Same Workload, Same Rules

## Briefing
The arguments are over. The judges want evidence.

## Objective
Run the same workload through direct execution, Docker, Kubernetes, and Slurm using a fixed comparison rubric.

## Measure
- setup complexity
- submission/startup path
- resource declaration
- log/output handling
- restart/retry behavior
- multi-user/queueing model
- GPU allocation model
- observability
- failure recovery
- operational surface area

Do not over-interpret laptop timing differences as production benchmarks. The important result is architectural behavior.

## Evidence
- one comparison matrix
- diagrams showing each control path
- concise “best fit / poor fit” statement for each contender

## Victory condition
You can answer “Kubernetes or Slurm?” with conditions and tradeoffs rather than loyalty.
