# Measurement and proof plan

## Decision

**CUSTOMER INPUT REQUIRED:** After a bounded pilot and agreed observation window, decide to proceed, adapt, or stop the governed RHEL patch workflow and whether an adjacent expansion is justified.

## Primary hypothesis

> **HYPOTHESIS:** Coordinating approval context, readiness, service protection, execution, verification, and evidence in one governed workflow will reduce avoidable manual coordination and elapsed waiting while maintaining or improving service acceptance and evidence quality.

## Measures

| Metric | Operational definition | Baseline | Proof observation | Source | Owner |
|---|---|---|---|---|---|
| Request-to-acceptance time | Approved request timestamp to accepted service timestamp | CUSTOMER INPUT REQUIRED | Same boundary | ITSM + AAP | |
| Manual touch time | Person-minutes actively coordinating, operating, investigating, or assembling evidence | CUSTOMER INPUT REQUIRED | Time sample or activity log | Operator study | |
| Manual handoffs | Transfers requiring a person to carry or re-enter context | CUSTOMER INPUT REQUIRED | Workflow/event review | ITSM + interviews | |
| Change success rate | Accepted without unplanned recovery divided by attempted hosts or batches | CUSTOMER INPUT REQUIRED | Same denominator | AAP + service record | |
| Recovery time | Failure detection to restored service or accepted exception | CUSTOMER INPUT REQUIRED | Same event boundary | AAP + incident/change | |
| Evidence completeness | Required fields with source and version reference divided by required fields | CUSTOMER INPUT REQUIRED | Evidence checklist | Evidence store | |
| Operator experience | Short structured rating of clarity and effort | CUSTOMER INPUT REQUIRED | Same questions | Survey/interview | |

## Guardrails

- no expansion of unapproved host scope;
- no decrease in service acceptance rate;
- no unresolved critical security or change-control finding;
- no evidence record containing secrets;
- no batch proceeds after a defined stop condition;
- maintenance effort is included in the result.

## Study design

1. Select one service with an owner, repeatable history, and recovery path.
2. Baseline at least three comparable recent windows when available.
3. Document host count, criticality, application, batch size, content type, and exclusions.
4. Run the safe demo and failure scenario before the customer pilot.
5. Execute a bounded pilot and then only the approved batches.
6. Capture the same measures at the same boundaries.
7. Review exceptions and adverse outcomes, not only averages.
8. Include build, integration, operation, and maintenance effort.
9. Hold an acceptance review with the sponsor and practitioners.

## Analysis

- Report median and range for elapsed and touch time.
- Report counts and denominator for success, exceptions, and evidence completeness.
- Identify process changes or incidents that make a window non-comparable.
- Do not extrapolate a single pilot to the estate without stating assumptions.
- Treat recovered time as capacity until the customer identifies how it is redeployed.

## Evidence package

- baseline worksheet and source references;
- approved scope and content reference;
- AAP workflow/job IDs and repository commit;
- per-stage checkpoints;
- package, kernel, reboot, and health observations;
- acceptance or exception decision;
- implementation and run effort;
- after-action review and expansion decision.
