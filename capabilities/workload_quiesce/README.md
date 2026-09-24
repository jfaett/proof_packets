# workload_quiesce

Pauses selected application services before maintenance and publishes what changed. Simulation is the default.

## Inputs

- demo_mode
- workload_services
- workload_action, either quiesce or restore

## Outputs

workload_quiesce_result with action and services.

## Failure

Stop the host or batch. If a partial quiesce occurred, restore only the services changed by this workflow or invoke the agreed application recovery plan.

## Adaptation

Many applications require load-balancer drain, cluster-aware sequencing, database coordination, or an application API rather than a system service stop. Replace this reference implementation with a tested adapter.
