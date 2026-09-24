# Contributing

Contributions are welcome when they improve reuse, evidence, or usability without presenting illustrative content as customer fact.

## Before opening a change

1. Choose the contribution type: practice, capability, Proof Pack, or governance.
2. Name an accountable owner and reviewer.
3. Open or link an issue that states the outcome and expected consumers.
4. For a capability, show at least one consumer; promotion to shared status normally requires two.
5. For a Proof Pack, copy the v1.0 template and complete every required artifact.

## Authoring rules

- Use **ILLUSTRATIVE** for invented examples, sample metrics, mock architectures, and demo data.
- Use **CUSTOMER INPUT REQUIRED** for facts that must be discovered.
- Do not include customer names, credentials, private endpoints, proprietary data, or source decks.
- Prefer stable relative links and headings because slides may deep-link into the repository.
- Reference shared capabilities instead of duplicating them.
- State support and ownership boundaries honestly. Validated examples are not automatically certified or supported product content.
- Use fully qualified Ansible collection names in automation.

## Change flow

~~~text
propose -> review contract -> implement -> test -> evidence -> approve -> release
~~~

Run:

~~~bash
make validate
make test
make syntax
~~~

If ansible-playbook is unavailable, syntax validation reports a documented skip locally; CI installs the development requirements and runs it.

## Pull request expectations

- Explain the customer or contributor problem.
- List changed contracts and consumers.
- Include test results.
- State whether deep links, maturity, or ownership changed.
- Add a changelog entry for externally visible changes.
- Obtain the approvals named in CODEOWNERS and the relevant OWNERS file.

See [governance](governance/README.md), especially [definition of done](governance/definition-of-done.md) and [ReCommoning](governance/recommoning.md).
