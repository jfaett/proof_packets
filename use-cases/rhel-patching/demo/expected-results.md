# Expected results

## Happy path

- approval validation passes for the illustrative change reference;
- readiness checks pass for all three local aliases;
- quiesce, package update, reboot, restore, and service health are visibly marked simulation;
- pilot completes before batch play begins;
- each host receives precheck and accepted checkpoints;
- each host receives a simulated system-of-record record;
- no package, service, or reboot change occurs.

Example evidence file names:

~~~text
ILLUSTRATIVE-CHG-0001-demo-pilot-01-precheck.json
ILLUSTRATIVE-CHG-0001-demo-pilot-01-accepted.json
sor-demo-pilot-01.json
~~~

## Verification failure

- health assertion fails;
- rescue writes a failed checkpoint;
- accepted checkpoint and accepted system-of-record update do not occur after failure;
- workflow exits unsuccessfully;
- the operator is directed to the recovery plan.

## What the result proves

- the reference capability contracts compose;
- safety gates are visible;
- failure stops progression;
- evidence structure is reproducible.

## What it does not prove

- compatibility with a customer RHEL estate;
- Satellite, ITSM, CMDB, backup, cluster, or application integration;
- production scaling, duration, success rate, or savings;
- operational support or product certification.
