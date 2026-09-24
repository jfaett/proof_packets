# Illustrative current-state SOP

> **ILLUSTRATIVE:** This is a plausible teaching example, not a customer's process and not a production runbook. Validate every step, owner, system, control, and exception.

## Purpose

Patch an approved group of RHEL hosts during a maintenance window, restore service, verify acceptance, and close the change record.

## Start and end

- Start: approved change, target list, content reference, owner, and window are available.
- End: in-scope hosts have an accepted outcome or documented exception; required service checks and records are complete.

## Roles

- change coordinator;
- RHEL operator;
- Satellite/content administrator;
- application or cluster owner;
- service desk/evidence owner.

## Procedure

### 1. Confirm request and scope

1. Open the approved change.
2. Compare target hosts with the authoritative inventory.
3. Confirm owner, window, exclusions, pilot, and approved content.
4. Resolve mismatches before execution.

Exception: unowned or out-of-window targets are excluded and recorded.

### 2. Run readiness checks

1. Confirm connectivity and credentials.
2. Check disk capacity and repository access.
3. Confirm packages/content are available.
4. Check application, dependency, and cluster health.
5. Record pass/fail per host.

Exception: failed checks stop that host and may stop the batch according to policy.

### 3. Prepare the service

1. Drain traffic or quiesce workload if required.
2. Take backup or snapshot according to policy.
3. Confirm recovery owner and method.
4. Record the pre-change checkpoint.

Exception: partial drain or failed backup stops execution and triggers restoration.

### 4. Apply approved updates

1. Launch the approved package action.
2. Monitor host and batch results.
3. Record package transaction status.
4. Stop progression on a terminal error.

Exception: do not assume package rollback. Follow the approved recovery plan.

### 5. Reboot and restore

1. Determine whether reboot is required.
2. Reboot within the bounded timeout.
3. Wait for host readiness.
4. Restore workload or cluster membership.

Exception: a host that does not return is escalated through out-of-band and recovery procedures.

### 6. Verify and accept

1. Verify expected package and kernel state.
2. Run host, application, access, dependency, and cluster checks.
3. Ask the application or service owner to accept the result where required.
4. Permit the next batch only after the agreed gate.

Exception: failed service checks stop the next batch and invoke application recovery.

### 7. Update evidence and records

1. Link request, host, batch, workflow job, and content version.
2. Update ITSM progress and outcome.
3. Update CMDB or evidence store only with verified state.
4. Record exceptions, recovery, and owner acceptance.
5. Close or hold the change according to policy.

## Known discovery gaps

- authoritative target and owner source;
- content view and repository policy;
- application-specific quiesce and acceptance;
- cluster-aware batch logic;
- backup and recovery contract;
- evidence retention and redaction;
- package/kernel verification commands;
- approval segregation of duties.
