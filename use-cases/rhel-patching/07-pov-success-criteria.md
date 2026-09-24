# POV success criteria

Agree on all criteria before live execution.

## Mandatory technical acceptance

| Criterion | Pass condition | Evidence |
|---|---|---|
| Scope control | Only approved pilot and batch targets are addressed | Request, inventory snapshot, AAP job scope |
| Approval control | Denied, missing, or timed-out approval cannot reach change execution | Workflow path test |
| Precheck gate | A deliberately failed readiness input stops the host or batch | Failure scenario job |
| Approved content | Execution references the approved content source/version | Content reference + job |
| Reboot control | Reboot occurs only when required and is bounded | Reboot decision + readiness |
| Service verification | Agreed host and application checks run before acceptance | Check results |
| Evidence traceability | Request, target, job, content, result, and version correlate | Evidence checklist |
| Failure route | At least one representative failure reaches the named recovery/escalation path | Scenario evidence |
| Secret handling | No credential appears in repository, job output, or evidence sample | Review |

## Outcome acceptance

**CUSTOMER INPUT REQUIRED:** Set thresholds from the local baseline and sponsor decision.

Illustrative decision shape:

- proceed when manual coordination and/or elapsed waiting measurably improve, guardrails hold, and maintenance effort is acceptable;
- adapt when the workflow is technically credible but an integration, health, batching, or evidence contract needs revision;
- stop when ownership, safety, recovery, data access, or measurable value cannot be established.

Do not copy the following as customer thresholds:

> **ILLUSTRATIVE:** 100% required evidence fields present; zero out-of-scope hosts; all defined failure gates stop correctly; no decrease in service acceptance; a locally agreed reduction in touch time.

## Acceptance record

| Decision | CUSTOMER INPUT REQUIRED |
|---|---|
| Sponsor | |
| Practitioner representatives | |
| Observation window and sample | |
| Result against each criterion | |
| Exceptions and adverse effects | |
| Maintenance owner and estimate | |
| Proceed / adapt / stop | |
| Qualified expansion, if any | |
