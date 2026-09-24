# MBPM baseline worksheet

Use this worksheet with the people who perform and receive the work. Record observed ranges and evidence; do not force false precision.

## Blank customer worksheet

**CUSTOMER INPUT REQUIRED**

| Step | Actor | System | Process time | Wait time | People | Complete and accurate | Rework frequency/time | Evidence source | Notes |
|---|---|---|---:|---:|---:|---:|---|---|---|
| Confirm request and scope | | | | | | | | | |
| Run prechecks | | | | | | | | | |
| Prepare service | | | | | | | | | |
| Apply updates | | | | | | | | | |
| Reboot and restore | | | | | | | | | |
| Verify and accept | | | | | | | | | |
| Update evidence and records | | | | | | | | | |

## Illustrative worked example

> **ILLUSTRATIVE ONLY:** The values below are invented to demonstrate the math. They are not targets, benchmarks, or customer results.

| Step | Actor | Process time | Wait time | People | Complete and accurate |
|---|---|---:|---:|---:|---:|
| Confirm request and scope | Change coordinator | 15 min | 240 min | 1 | 92% |
| Run prechecks | RHEL operator | 20 min | 60 min | 1 | 90% |
| Prepare service | App + RHEL | 25 min | 120 min | 2 | 95% |
| Apply updates | RHEL operator | 15 min | 0 min | 1 | 98% |
| Reboot and restore | RHEL + app | 15 min | 20 min | 2 | 96% |
| Verify and accept | App owner | 20 min | 90 min | 1 | 90% |
| Update records | Change coordinator | 15 min | 30 min | 1 | 95% |
| **Total** | | **125 min** | **560 min** | | **approximately 62% rolled** |

Illustrative lead time represented by the table is 685 minutes. Illustrative flow efficiency is 125 divided by 685, or about 18%. The point is to expose where work waits and where incomplete inputs create rework, not to compare customers to this example.

## Window-level measures

| Measure | Definition | Baseline window | Evidence owner |
|---|---|---|---|
| Request-to-acceptance time | Approved request timestamp to accepted service timestamp | CUSTOMER INPUT REQUIRED | |
| Manual touch time | Sum of person-minutes actively coordinating or operating | CUSTOMER INPUT REQUIRED | |
| Manual handoffs | Count of person-to-person or tool-to-person transfers | CUSTOMER INPUT REQUIRED | |
| Change success | Accepted without unplanned recovery divided by attempted | CUSTOMER INPUT REQUIRED | |
| Recovery time | Failure detected to service recovered or accepted exception | CUSTOMER INPUT REQUIRED | |
| Evidence completeness | Required evidence fields present and traceable divided by required fields | CUSTOMER INPUT REQUIRED | |
| Window overrun | Actual completion after approved window end | CUSTOMER INPUT REQUIRED | |

## Data request

Collect at least three comparable recent windows when available. Record sample size, exclusions, service mix, host count, criticality, and any major process change that limits comparison.
