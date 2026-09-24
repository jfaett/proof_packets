# Five-minute walkthrough

## 1. See the system

Start at [README.md](README.md). The library connects use cases, shared capabilities, and reusable practices through the eight-stage methodology.

## 2. See the authoring standard

Open [Proof Pack v1.0](templates/proof-pack/README.md). It defines the required seller, discovery, process, architecture, demo, proof, ownership, and evidence artifacts plus maturity and readiness rules.

## 3. Follow one use case

Open [RHEL Patching](use-cases/rhel-patching/README.md). Move from seller briefing to discovery, illustrative current state, MBPM baseline, decomposition, future-state architecture, demo, proof, failure, and expansion.

The most important distinction appears throughout:

- **ILLUSTRATIVE** means teaching example.
- **CUSTOMER INPUT REQUIRED** means discover and validate locally.

## 4. Inspect reuse

Open [capabilities](capabilities/README.md). The RHEL workflow composes eight contracts rather than hiding one large playbook. Each capability declares inputs, outputs, failures, evidence, consumers, owner role, support boundary, and tests.

## 5. Run safely

Follow [demo setup](use-cases/rhel-patching/demo/setup.md). The default run is local and non-destructive. It emits structured evidence and includes a failure injection that stops the workflow before acceptance.

## 6. See how it lasts

Read [governance](governance/README.md). Semantic versions, CODEOWNERS placeholders, CI, definitions of ready/done, maturity, change control, retirement, and ReCommoning turn an example into a maintainable organizational asset.

## Build assumptions

The complete assumption set is in [docs/assumptions.md](docs/assumptions.md). The most important are:

1. this is a new repository and does not modify Denver21.02.24;
2. source decks are references and are not redistributed;
3. the short-link host, real GitHub owners, and customer integrations are intentionally left for deployment;
4. Satellite or another approved source owns patch content, while AAP coordinates the workflow;
5. local proof—not vendor or illustrative data—drives the expansion decision.

## Verification performed

- repository contract and link validation;
- unit tests for catalog references and safe defaults;
- Ansible syntax check with ansible-core;
- successful three-host-alias simulation;
- failed-health scenario that recorded failure and stopped before acceptance.
