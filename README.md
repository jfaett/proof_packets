# Red Hat Sales Proof Library

A GitHub-ready system for turning an outcome-oriented sales conversation into a measurable, governed proof.

This repository connects three catalogs:

- **Use cases** tell the complete customer outcome story.
- **Capabilities** provide reusable automation building blocks.
- **Practices** provide reusable ways of discovering, mapping, measuring, and proving value.

The first complete reference pack is [RHEL Patching](use-cases/rhel-patching/README.md).

> **Important boundary:** This is a sales proof system and reference pattern, not a production implementation runbook. Every invented example is labeled **ILLUSTRATIVE**. Every production decision is labeled **CUSTOMER INPUT REQUIRED**. Adaptation, security review, change approval, testing, and support ownership remain mandatory.

## The method

~~~mermaid
flowchart LR
  D[Discover] --> U[Understand / Map]
  U --> B[Baseline]
  B --> X[Decompose]
  X --> P[Position]
  P --> M[Demonstrate]
  M --> V[Prove]
  V --> E[Expand]
  E -. learning .-> D
~~~

The sequence deliberately starts with the work and its outcome, not with product features. It combines the Denver 2024 pattern of process to SOP to decomposition to automation with the deck's **Baseline to Proof to Qualified Expansion** motion and a platform operating model built around reusable, owned services.

Read the full [methodology](docs/methodology.md) and [Proof Pack v1.0 standard](templates/proof-pack/README.md).

## Start here

| If you are... | Start with... |
|---|---|
| Seller | [RHEL seller briefing](use-cases/rhel-patching/01-seller-briefing.md) |
| Solution architect | [RHEL discovery guide](use-cases/rhel-patching/02-discovery-guide.md) |
| Demo owner | [Demo setup](use-cases/rhel-patching/demo/setup.md) |
| POV lead | [Measurement and proof plan](use-cases/rhel-patching/06-measurement-and-proof.md) |
| Contributor | [Contribution guide](CONTRIBUTING.md) |
| Capability owner | [Capability catalog](capabilities/README.md) |
| Reviewer | [Definition of done](governance/definition-of-done.md) |
| New reader | [Five-minute walkthrough](WALKTHROUGH.md) |

## Repository map

~~~text
.
├── docs/                 Method, catalog model, provenance, and deep-link design
├── practices/            Discovery and measurement practices
├── templates/            Proof Pack v1.0 authoring contract
├── governance/           Ownership, maturity, releases, and ReCommoning
├── capabilities/         Reusable automation contracts and implementations
├── use-cases/            Complete, outcome-oriented Proof Packs
├── scripts/              Repository validation and short-link export
└── tests/                Repository-level acceptance tests
~~~

## Run the safe demonstration

The default demo is intentionally non-destructive. It simulates approvals, patching, reboot, health checks, and system-of-record updates while producing evidence files.

~~~bash
make validate
make demo
~~~

The demo requires ansible-core. See [demo setup](use-cases/rhel-patching/demo/setup.md). Live execution is disabled unless a customer adapts the integration contracts and explicitly sets the execution gate described there.

## What “ready” means

A Proof Pack is ready only when:

1. outcome, actors, scope, and unknowns are explicit;
2. a current-state map and measurable baseline exist;
3. human judgment is separated from deterministic automation;
4. reusable capabilities have owners and contracts;
5. the demo is reproducible and safe by default;
6. proof criteria name evidence, source, owner, and decision rule;
7. failure and recovery paths are tested;
8. ownership, version, maturity, and maintenance commitments are visible.

## Version

Proof Pack specification: **1.0**

Repository release: see [VERSION](VERSION) and the [release policy](governance/release-and-versioning.md).

## Source and trademark note

The library is informed by source material listed in [Sources and provenance](docs/sources-and-provenance.md). Source decks are not redistributed here. “Red Hat,” “Ansible,” and product names are trademarks of their respective owners. This repository is a reference asset and does not itself grant product support or certification.

## License

Apache License 2.0. See [LICENSE](LICENSE). Source material referenced but not included retains its original ownership and access restrictions.
