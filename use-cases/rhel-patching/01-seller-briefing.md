# Seller briefing

## One-sentence story

Coordinate the RHEL patch window as a governed service workflow: keep approved content in the customer's designated source, use AAP to connect approval, readiness, execution, service verification, and evidence, then prove the improvement locally.

## The customer problem

**HYPOTHESIS:** Technical patch execution may already be automated, while people still carry context between ITSM, inventory, content, application, and evidence systems. That can create waiting, repeat coordination, inconsistent stop decisions, and manual evidence assembly.

Validate this. Do not assume the handoffs exist.

## Desired outcome

**CUSTOMER INPUT REQUIRED:** Define the mission or service result. A useful outcome statement names the service, measure, baseline, target direction, and decision.

Example:

> **ILLUSTRATIVE:** Reduce patch-window coordination and evidence effort for a selected RHEL service while maintaining or improving change success and application acceptance.

## Qualify in ten minutes

Ask:

1. Which business or mission service is affected by RHEL patching?
2. Who owns patch execution and who accepts the service afterward?
3. What patch content source is authoritative?
4. Where do approvals, target lists, health results, and evidence live?
5. Which parts are automated now?
6. Where are the manual launches, waits, rekeying, and handoffs?
7. How is a failed precheck or application test handled?
8. What baseline data exists for the last three comparable windows?
9. Is there a bounded pilot with an application owner and recovery plan?
10. What measured result would justify another service or platform?

## Strong qualification signals

- named service and accountable owner;
- repeatable patch windows with accessible historical data;
- existing automation that is fragmented across teams or tools;
- manual coordination or evidence burden acknowledged by practitioners;
- application health and failure handling can be defined;
- sponsor will decide based on agreed evidence;
- pilot scope and recovery path are available.

## Caution signals

- the conversation is only “show us Ansible”;
- no service owner or acceptance authority;
- no approved content or target source;
- production demo expected without recovery planning;
- success means only “job completed”;
- universal savings target requested without baseline;
- desire to replace native tools without evidence.

## Positioning

| Existing owner | Keeps ownership of | AAP contributes |
|---|---|---|
| ITSM / change | Request, authorization, process record | Launch context, status, references |
| Satellite or approved source | Content lifecycle and approved repositories | Coordinated use of approved content |
| RHEL platform team | Host standards and execution policy | Repeatable job templates and batching |
| Application or cluster owner | Quiesce, restore, acceptance | Sequenced calls and evidence |
| CMDB / evidence owner | Authoritative state and retention | Verified update and job correlation |

## What not to promise

- a percentage saving before baseline;
- zero downtime;
- automatic rollback of every package update;
- universal health checks;
- that a reference playbook is certified or production supported;
- that recovered capacity becomes cash savings;
- that AAP should replace the customer's designated patch platform.

## Recommended next step

Run a 60-90 minute discovery and MBPM session with the patch operator, application owner, service owner, change/evidence stakeholder, and AAP owner. Leave with a validated boundary, fact/assumption register, baseline data request, and pilot decision.
