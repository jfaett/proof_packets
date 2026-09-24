# Reusable capability catalog

Capabilities are bounded, testable contracts used by multiple outcome workflows.

| Capability | Purpose | Current consumer |
|---|---|---|
| [approval_gate](approval_gate/README.md) | Refuse progression without approved context | RHEL patching |
| [patch_precheck](patch_precheck/README.md) | Validate readiness inputs before change | RHEL patching |
| [workload_quiesce](workload_quiesce/README.md) | Pause and later restore selected services | RHEL patching |
| [apply_updates](apply_updates/README.md) | Apply approved RHEL package updates | RHEL patching |
| [controlled_reboot](controlled_reboot/README.md) | Reboot only when required and wait for readiness | RHEL patching |
| [service_health_check](service_health_check/README.md) | Verify service and endpoint state | RHEL patching |
| [evidence_checkpoint](evidence_checkpoint/README.md) | Emit versioned workflow evidence | RHEL patching |
| [system_of_record_update](system_of_record_update/README.md) | Write progress or acceptance to an external record | RHEL patching |

These reference implementations use simulation mode by default. Shared catalog status means the repository owner accepts the documented contract; it does not mean the content is Red Hat certified.

## Capability contract

Every capability declares inputs, outputs, failure semantics, evidence, supported targets, owner role, version, and consumers. Implementations must be idempotent where practical and must never broaden privilege or scope silently.
