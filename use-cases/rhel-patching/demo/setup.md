# Demo setup

## Safety statement

The default inventory uses local aliases and demo_mode=true. It does not install packages, stop services, reboot, or call an external API. It writes only JSON files under use-cases/rhel-patching/demo/evidence.

## Prerequisites

- Python 3.10 or newer;
- ansible-core in the supported development range;
- a disposable working copy of this repository.

## Install and validate

From the repository root:

~~~bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-dev.txt
make validate
make syntax
~~~

## Run the happy path

~~~bash
make demo
~~~

Expected: one pilot and two batch aliases complete; precheck and accepted JSON checkpoints plus simulated system-of-record records appear under demo/evidence.

## Exercise a verification failure

~~~bash
ansible-playbook \
  -i use-cases/rhel-patching/demo/inventory/hosts.yml \
  use-cases/rhel-patching/demo/playbooks/rhel_patch_window.yml \
  -e '{"simulated_health_passed": false}'
~~~

Expected: service verification fails, a failed checkpoint is written, acceptance is not written for the failing host, and the workflow stops.

## Reset

Follow [reset-demo.md](reset-demo.md).

## Live adaptation gate

Do not enable live mode from this reference without all of the following:

- customer-approved inventory and pilot;
- authoritative approval integration;
- approved Satellite/content reference and repository policy;
- environment-specific readiness adapters;
- application/cluster quiesce, restore, health, and recovery contracts;
- least-privilege AAP credentials and approved network path;
- bounded batch and reboot policy;
- system-of-record schema, retention, and redaction review;
- scenario tests in a non-production environment;
- named operational owners.

Only after those reviews do the explicit variables customer_adaptation_complete, approval_authoritative, and patch_execute_confirmed become true in an approved, protected runtime source. Never commit credentials or production approvals.
