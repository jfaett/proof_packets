# service_health_check

Verifies selected system services and HTTP endpoints after maintenance. Simulation is the default.

## Inputs

- demo_mode
- health_services
- health_endpoints
- simulated_health_passed

## Output

service_health_check_result with the checked services, endpoints, and pass state.

## Failure

Do not accept the host or advance the next batch. Restore the service if safe or invoke the application recovery and escalation plan.

## Boundary

Host availability is not business-service acceptance. Customer application owners must define representative positive, negative, access, and dependency checks.
