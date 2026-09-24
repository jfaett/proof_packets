# Failure and recovery

Failed checks stop the affected progression. Recovery is owned by the relevant service domain, not improvised by a generic patch playbook.

## Failure matrix

| Failure | Detection | Stop boundary | Retry rule | Recovery | Owner | Evidence |
|---|---|---|---|---|---|---|
| Approval denied or timed out | Workflow node state | Entire request | New approval only | Correct request or reschedule | Change owner | Approval reference/state |
| Target or owner mismatch | Reconciliation | Affected target or request | After authoritative correction | Remove or correct scope | Service owner | Before/after target manifest |
| Disk/repository/package readiness fails | Precheck | Host; batch if policy says | After remediation and fresh check | Remediate or exclude | RHEL owner | Failed check and assignment |
| Application or cluster unhealthy before change | Precheck | Batch | After app owner accepts healthy state | Restore baseline health | App owner | Health observations |
| Quiesce or backup fails | Adapter result | Host or service batch | Only if idempotent and owner approves | Restore partially changed state | App/backup owner | Action results |
| Package transaction fails | dnf/job result | Host and next batch | Customer policy only | Snapshot, rebuild, downgrade, or vendor path | RHEL owner | Transaction and content refs |
| Host does not return | Reboot timeout | Host and next batch | Bounded retry policy | Out-of-band platform recovery | RHEL owner | Timeout and recovery timeline |
| Service health fails after patch | Test result | Host/batch; do not accept | After documented recovery action | Restore service, fail over, rebuild, or escalate | App owner | Tests and decision |
| ITSM/CMDB update fails | API result | Policy-dependent | Bounded, idempotent retry | Queue or manual controlled update | Record owner | Request/response reference |
| Evidence write fails | Checkpoint result | Fail closed when required | After sink recovery | Alternate approved evidence path | Evidence owner | Failure and final record |

## Compensation principles

- Compensate only changes made by this workflow.
- Never claim rollback when the platform cannot guarantee it.
- Keep failed hosts out of subsequent batches.
- Preserve job output and redacted evidence before recovery changes context.
- Require application owner acceptance after recovery.
- Reconcile ITSM and CMDB only with verified final state.

## Demo failure exercise

Run the simulation with simulated_health_passed=false. Expected result:

1. the service health capability fails;
2. acceptance evidence is not written;
3. the batch play ends;
4. the operator explains the recovery owner and evidence that would be required.

See [demo setup](demo/setup.md).
