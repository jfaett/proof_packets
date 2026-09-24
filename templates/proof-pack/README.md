# Proof Pack v1.0

Proof Pack v1.0 is the authoring and review contract for a seller/SA use case.

## Required artifacts

| Artifact | Purpose |
|---|---|
| README.md | Navigable front door and deep-link anchor |
| use-case.yaml | Machine-readable identity, outcomes, actors, metrics, capabilities, ownership, maturity |
| 01-seller-briefing.md | Conversation framing, qualification, positioning, non-goals |
| 02-discovery-guide.md | Questions, participants, fact and assumption capture |
| 03-current-state.md | Illustrative SOP, map, and blank baseline worksheet or links to them |
| 04-decomposition.md | Human, existing, automatable, reusable, orchestration, and gap model |
| 05-solution-pattern.md | Product roles, architecture, workflow, integrations, security boundary |
| demo/ | Safe runnable or realistically scaffolded assets, setup, talk track, expected results, reset |
| 06-measurement-and-proof.md | Baseline, hypothesis, metrics, sources, observation, analysis |
| 07-pov-success-criteria.md | Acceptance and decision rules |
| 08-failure-and-recovery.md | Failure semantics, stop conditions, rollback or recovery |
| 09-expansion-paths.md | Qualified adjacent outcomes and triggers |
| 10-evidence-and-sources.md | Provenance, citations, evidence inventory |
| OWNERS.md | Service, content, platform, reviewer, and maintenance responsibility |
| CHANGELOG.md | Version history |
| tests/ | Content, contract, and scenario tests |

## Required labels

Use **ILLUSTRATIVE** on invented examples and **CUSTOMER INPUT REQUIRED** on unknown environment facts. Do not combine them in a way that makes a sample look discovered.

## Machine-readable minimum

The manifest must include:

- schema and pack version;
- ID, title, summary, status, and maturity;
- outcome and decision;
- actors and systems;
- prerequisites and exclusions;
- metric definitions;
- capability references;
- evidence types;
- owner roles;
- validation and last-reviewed state;
- deep-link slug;
- related use cases.

See [use-case.schema.json](use-case.schema.json) and [use-case.yaml](use-case.yaml).

## Definition of ready

A pack may enter build when the outcome, sponsor decision, scope, initial users, owner, discovery plan, and safety classification are known.

## Definition of done

A pack is reference-ready when all required artifacts pass repository checks, another SA can run the demo, evidence can be traced to versions, failure paths are exercised, and named owners accept maintenance.

## Maturity

- **draft** — incomplete and not seller-ready;
- **demonstrable** — safe repeatable demo, incomplete local proof;
- **reference** — complete reusable pack with contract tests;
- **proven-local** — customer-specific evidence exists outside this public template;
- **retired** — preserved for history with successor guidance.
