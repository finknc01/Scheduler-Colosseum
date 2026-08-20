# Round 00 — Weigh-In: Bare Process Baseline

## Briefing
Before the contenders fight, the judges need to know what the workload looks like without orchestration.

## Objective
Create a small repeatable CPU/GPU workload and establish its direct execution behavior.

## Tasks
Define inputs, runtime command, logs, exit code, resource needs, output artifact, and success condition. Measure startup time, runtime, CPU/RAM, and GPU utilization where available.

## Twist
Kill the process once and observe what does—and does not—restart automatically.

## Evidence
- workload source/config
- baseline measurements
- process tree and logs
- manual recovery notes

## Victory condition
You know exactly what each execution platform will be asked to run and have a neutral baseline to compare against.
