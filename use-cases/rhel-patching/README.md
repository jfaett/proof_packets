# Coordinate the RHEL patch window

**Proof Pack v1.0 · version 1.0.0 · maturity: reference**

Coordinate an approved RHEL patch window from scoped request through readiness, service protection, approved updates, bounded reboot, verification, acceptance, and evidence.

> **ILLUSTRATIVE REFERENCE:** The workflow, sample SOP, demo data, timings, and thresholds in this pack are examples. They are not facts about a customer.
>
> **CUSTOMER INPUT REQUIRED:** Approved content source, host ownership, maintenance policy, application behavior, cluster sequencing, recovery plan, credentials, evidence retention, baseline, and success thresholds must be discovered and approved locally.

## Why this exists

Many teams already have patch tools or playbooks. The remaining work is often carried by people: validate scope, move context across systems, wait for approvals, protect services, decide whether to reboot, verify the application, update records, and assemble evidence.

The pattern keeps approved content ownership with the designated source, such as Red Hat Satellite, while AAP coordinates the cross-tool service workflow.

## Choose your path

| Need | Deep link |
|---|---|
| Prepare a customer conversation | [Seller briefing](01-seller-briefing.md) |
| Run discovery | [Discovery guide](02-discovery-guide.md) |
| Show the illustrative current state | [SOP](current-state/illustrative-sop.md) and [process map](current-state/process-map.md) |
| Establish a baseline | [MBPM worksheet](current-state/baseline-worksheet.md) |
| Explain what stays human and what becomes reusable | [Decomposition](04-decomposition.md) |
| Explain AAP's role | [Solution pattern and architecture](05-solution-pattern.md) |
| Run the demo | [Setup](demo/setup.md) and [talk track](demo/talk-track.md) |
| Design a POV | [Measurement plan](06-measurement-and-proof.md) and [success criteria](07-pov-success-criteria.md) |
| Discuss risk | [Failure and recovery](08-failure-and-recovery.md) |
| Qualify what comes next | [Expansion paths](09-expansion-paths.md) |
| Review provenance | [Evidence and sources](10-evidence-and-sources.md) |

Suggested slide short link: **/go/rhel-patching**

Audience routes: **/discover**, **/demo**, **/prove**

## Outcome chain

~~~mermaid
flowchart LR
  R[Approved request] --> S[Scope and owner]
  S --> C[Readiness checks]
  C --> P[Protect service]
  P --> U[Apply approved updates]
  U --> B[Bounded reboot]
  B --> V[Verify service]
  V --> A[Owner acceptance]
  A --> E[Evidence and record]
  C -- failed --> X[Stop, assign, recover]
  V -- failed --> X
~~~

## Customer conversation

1. How does a patch request become an accepted service today?
2. Where do people carry context or wait between existing tools?
3. What local baseline can be measured?
4. Which decisions must remain human?
5. What can be demonstrated safely?
6. What result would justify expanding to another service?

## AAP role

AAP coordinates sequence, context, approval state, failure routing, verification, and evidence. It does not automatically replace:

- Satellite or another approved content source;
- application or cluster-native lifecycle controls;
- the ITSM approval policy;
- CMDB ownership;
- application owner acceptance;
- customer backup, rollback, or recovery standards.

## Demonstration contract

The supplied demo:

- runs against local inventory aliases;
- simulates patching, reboot, health, and external updates;
- creates redacted JSON evidence;
- exercises the same capability boundaries expected in a live adaptation;
- refuses live package changes unless an explicit confirmation gate is set.

It does not prove customer compatibility or production readiness.

## Proof decision

The pack is successful when the customer can make an evidence-based decision to **proceed**, **adapt**, or **stop**. A successful automation job alone is not proof; service verification, evidence completeness, operational effort, and agreed outcomes are part of acceptance.
