# Discovery guide

## Session objective

Understand one real RHEL patch service from accepted request to accepted service, identify measurable friction and risk, and decide whether a bounded proof is warranted.

## Participants

**CUSTOMER INPUT REQUIRED**

- service or outcome owner;
- patch operator;
- RHEL and Satellite/content owner;
- application or cluster owner;
- ITSM/change owner;
- CMDB/evidence owner;
- AAP platform owner;
- security representative where needed.

## Prework

Request redacted examples from two or three recent comparable windows:

- request and approval record;
- target/batch list and ownership;
- execution and exception records;
- application validation;
- close/acceptance evidence;
- elapsed times and operator effort, if available.

Do not copy restricted artifacts into this repository.

## Questions by stage

### Outcome and scope

1. Which service is the customer trying to protect or improve?
2. Why is this important now?
3. Where does the process start, and who can declare it accepted?
4. Which hosts, environments, applications, clusters, and exclusions apply?
5. What decision will the proof enable?

### Request and approval

6. What creates the request and authoritative scope?
7. Who approves content, window, targets, and risk?
8. Can scope change after approval? How is that reconciled?
9. What information is rekeyed between ITSM, inventory, or automation?

### Existing automation

10. Which tools own content, package execution, snapshots, drain, reboot, monitoring, and records?
11. Which playbooks or scripts already work reliably?
12. Where are people manually launching the next tool or translating output?
13. Which interfaces are supported APIs versus console-only steps?

### Precheck and preparation

14. What makes a host and service eligible?
15. How are disk, repository, package, application, dependency, and cluster states checked?
16. Who decides whether a failed check is remediated, excluded, or accepted?
17. What backup, snapshot, drain, or quiesce is required?

### Execution and reboot

18. How is approved content identified and pinned?
19. How are pilots and batches selected?
20. What determines whether a reboot is required?
21. What timeout, retry, and out-of-band access are available?

### Verification and evidence

22. Which host facts are necessary but insufficient for service acceptance?
23. What positive, negative, access, dependency, and cluster tests matter?
24. Who accepts the batch and next-batch progression?
25. What must ITSM and CMDB record, and which system is authoritative?
26. How is workflow/content version linked to execution?

### Failure and recovery

27. What should stop one host, a batch, or the entire window?
28. Which failures are safe to retry?
29. What does recovery mean for package, host, application, and service?
30. Who owns escalation at each boundary?

### Baseline and proof

31. How many comparable windows and hosts are available?
32. Can request-to-acceptance, touch time, handoffs, rework, success, recovery, and evidence completeness be measured?
33. What guardrail must not worsen?
34. What result means proceed, adapt, or stop?
35. What implementation and maintenance effort will be counted?

## Fact and assumption register

| Statement | Label | Source | Confidence | Validation action | Owner |
|---|---|---|---|---|---|
| Approved content comes from Satellite | CUSTOMER INPUT REQUIRED | | | | |
| Application can be drained by API | CUSTOMER INPUT REQUIRED | | | | |
| Manual evidence effort is material | HYPOTHESIS | | | Measure recent windows | |
| Reference demo values | ILLUSTRATIVE | This pack | Not customer evidence | Replace | SA |

## Exit criteria

- a named outcome and decision;
- validated process boundary;
- identified system owners;
- baseline data request with owners and dates;
- pilot candidate and recovery owner;
- documented gaps that could stop the proof.
