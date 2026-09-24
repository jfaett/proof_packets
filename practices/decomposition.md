# Decomposition

## Purpose

Separate a service workflow into the things people must decide, the automation that already exists, reusable deterministic actions, use-case orchestration, and unresolved gaps.

## Classification

| Class | Test | Typical treatment |
|---|---|---|
| Human judgment | Requires accountability, risk acceptance, or ambiguous interpretation | Preserve as approval or decision with context |
| Existing automation | Already performs a bounded action reliably | Integrate; do not rewrite without evidence |
| Automatable | Deterministic inputs, action, result, and failure semantics | Implement or adapt |
| Reusable capability | Useful across multiple services with a stable contract | Promote to shared catalog |
| Use-case orchestration | Ordering and policy unique to the outcome | Keep in the Proof Pack |
| Gap | Unknown, unsupported, unowned, or unavailable | Resolve, constrain scope, or stop |

## Contract prompts

- What are the inputs and who may supply them?
- What observable result permits the next step?
- What failures are retryable, recoverable, or terminal?
- What evidence is emitted?
- Is the action idempotent?
- Who supports it and which targets are supported?
- Which second consumer justifies shared ownership?
