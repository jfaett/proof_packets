# Catalog model

The repository has three related catalogs.

~~~mermaid
flowchart TB
  UC[Use case / complete Proof Pack]
  PR[Practices / ways of working]
  CP[Capabilities / reusable contracts]
  EV[Evidence / measured observations]
  OW[Owners / maintenance commitments]

  PR --> UC
  CP --> UC
  UC --> EV
  OW --> UC
  OW --> CP
  EV --> DEC[Proof and expansion decision]
~~~

## Use cases

A use case is a customer-facing outcome and the end-to-end proof path. It owns orchestration and acceptance, but it should consume shared capabilities.

## Capabilities

A capability is a reusable contract such as a precheck, controlled reboot, or evidence checkpoint. A capability may have several implementations. Shared status means that an owner accepts maintenance responsibility; it does not imply product certification.

## Practices

A practice is a reusable facilitation or analysis method. Practices create the discovery, process, baseline, or proof artifacts used by many packs.

## Promotion rule

A building block begins inside a use case. Promote it to the shared catalog when:

- a second consumer exists or is imminent;
- inputs, outputs, failure semantics, and evidence can be described independently;
- a maintenance owner accepts the contract;
- contract tests exist.

This is the repository expression of ReCommoning: improvement returns to the shared commons through an explicit ownership negotiation.
