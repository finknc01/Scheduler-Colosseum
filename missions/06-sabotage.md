# Round 06 — Sabotage Round

## Briefing
A contender only looks good when everything works. The judges now permit controlled sabotage.

## Objective
Compare failure semantics.

## Fault deck
Choose at least four across the systems: kill workload process, delete container/pod, remove worker, exhaust requested resource, bad image, bad command, unavailable GPU request, scheduler/controller outage, or lost output path.

## Rules
Introduce equivalent faults where meaningful. Record who notices the failure, what state is persisted, whether work retries, what the user sees, and what an operator must do.

## Evidence
- fault matrix
- timestamps/events/logs
- recovery action and time
- surprising differences

## Victory condition
You understand each system better from how it fails than from how it launches a happy-path job.
