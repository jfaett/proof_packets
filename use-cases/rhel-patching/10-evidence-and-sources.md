# Evidence and sources

## Proof evidence inventory

| Evidence | Minimum fields | Authoritative system | Sensitivity | Owner |
|---|---|---|---|---|
| Request and approval | change ID, state, approver role, scope, window | ITSM | Internal | Change owner |
| Target manifest | host ID, owner, service, batch, exclusions | Inventory/CMDB | Internal/restricted | Service owner |
| Content reference | source, version/view, repository, approval | Satellite/content system | Internal | RHEL/content owner |
| Precheck | normalized check, result, timestamp, host | AAP/evidence store | Internal | RHEL/app owner |
| Execution | workflow/job ID, project revision, execution environment, result | AAP | Internal | Platform owner |
| Verification | package/kernel observation, host readiness, app tests | AAP/monitoring | Internal | RHEL/app owner |
| Acceptance | accepting role, time, result, exception | ITSM | Internal | Service owner |
| Measurement | definition, sample, baseline, result, exclusions | Approved analysis store | Internal | Evidence owner |

## Source context

This pack adapts ideas from:

- **AAP Cross-Platform Lifecycle Master v28**, especially pages 1-3, 7, and 20-21: follow the work from request through evidence; RHEL patch stages; local proof; content governance; ownership and retirement.
- **Enterprise Automation Denver.2.21.24**, especially pages 5, 9-10, and 28: innovation capacity, change, accessibility, data, and a repeatable organizational automation process.
- **Say Hello to the Platform Operating Model**, especially pages 5, 8, 12, 17, 21, 24, and 32: flow, reusable services/components, platform product thinking, ReCommoning, adoption, and community stewardship.
- **Open Practice Library Metrics-Based Process Mapping**: actors, process time, lead/wait time, resources, and complete-and-accurate measures.
- Official Red Hat and Ansible documentation linked in the architecture and capability files.

Source decks are not included. Respect their original confidentiality and ownership.

## Evidence handling

- Record repository commit, pack version, and capability versions.
- Store production evidence in approved customer systems, not in this reference repository.
- Redact secrets, personal data, internal endpoints, and unnecessary host facts.
- Use immutable or access-controlled records where policy requires.
- Do not update CMDB with an intended state; record verified state and source.

## External evidence boundary

External research or vendor material may help form a hypothesis. It is not a customer baseline and must not be used as proof of local outcomes.
