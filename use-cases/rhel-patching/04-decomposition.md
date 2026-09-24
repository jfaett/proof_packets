# Decomposition

## Step classification

| Workflow step | Human judgment to preserve | Existing automation to integrate | Automatable work | Shared capability | Use-case orchestration | Gap to discover |
|---|---|---|---|---|---|---|
| Scope and approve | Risk acceptance, window, exception | ITSM approval, inventory query | Validate approved fields and target reconciliation | approval_gate, system_of_record_update | Select pilot and batches | Authoritative owner/target source |
| Precheck | Accept or exclude a failed target | Existing scripts, monitoring, Satellite query | Normalize and gate readiness facts | patch_precheck, evidence_checkpoint | Batch stop policy | Application and cluster health |
| Prepare | Approve backup/recovery sufficiency | Snapshot, load balancer, cluster commands | Call deterministic quiesce and backup interfaces | workload_quiesce | Order by service dependency | Customer recovery contract |
| Apply updates | Exception decision | Satellite/content and patch playbooks | Launch approved package action | apply_updates | Correlate content to request and batch | Content pinning and exclusions |
| Reboot and restore | Escalation on timeout | Existing reboot and cluster procedures | Conditional reboot, wait, restore | controlled_reboot, workload_quiesce | Batch concurrency | Out-of-band recovery |
| Verify and accept | Service owner acceptance | Monitoring and test suites | Run deterministic host/app checks | service_health_check | Gate next batch | Business-service test |
| Evidence and close | Exception closure and audit judgment | ITSM/CMDB APIs | Record verified state and version links | evidence_checkpoint, system_of_record_update | Assemble pack-level result | Retention and data classification |

## Human work is not waste by definition

Preserve accountable decisions where ambiguity, policy, or risk exists. Improve the decision by presenting consistent context, deadline, and evidence. An AAP Approval node is an appropriate human boundary; a survey value is not a substitute for authorization.

## Existing automation is an asset

Do not rewrite a working Satellite, application, network, backup, or monitoring action merely to put it in Ansible. Wrap supported interfaces, normalize results, and coordinate progression.

## Capability contracts

Each referenced shared capability defines:

- validated inputs;
- observable output;
- terminal and retryable failures;
- evidence emitted;
- support boundary;
- owner and version.

The use case retains the unique sequence, batch policy, product roles, and final acceptance.

## Gaps that can stop a POV

- no authoritative scope or owner;
- no approved pilot window;
- no application health or recovery definition;
- unsupported interface to a required native tool;
- inability to obtain baseline evidence;
- no owner for exceptions or ongoing content;
- request to use production credentials or data in the repository.
