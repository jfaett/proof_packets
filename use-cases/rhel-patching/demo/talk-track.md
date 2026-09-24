# Demo talk track

## 0:00 — Start with the outcome

“This is not a patch command demo. We are following an approved service from request through verified acceptance and evidence.”

Show the [Proof Pack front door](../README.md) and the Baseline-to-Proof decision.

## 1:00 — Show what is already owned

Point to the [architecture](../05-solution-pattern.md):

- approved content remains with Satellite or the designated source;
- ITSM owns approval and process;
- application owners define health and recovery;
- AAP coordinates the workflow and evidence.

## 2:00 — Expose the current work

Show the [illustrative process map](../current-state/process-map.md). Ask the audience which waits and handoffs actually occur for them. Explicitly label the map illustrative.

## 3:00 — Show the contract, not magic

Open the shared capability catalog. Highlight approval, normalized prechecks, quiesce, approved updates, controlled reboot, service health, and evidence.

“Every block has inputs, outputs, failure behavior, evidence, and an owner.”

## 4:00 — Run the safe workflow

Run make demo. Narrate:

1. approved context is validated;
2. readiness facts gate progression;
3. the workload is protected;
4. approved updates and reboot are simulated;
5. service health gates acceptance;
6. evidence and the system-of-record checkpoint are written.

## 7:00 — Show evidence

Open one precheck and one accepted JSON file. Point out change reference, host, stage, pack version, and timestamp. Explain that production evidence belongs in approved customer systems.

## 8:00 — Demonstrate failure

Explain or run simulated_health_passed=false.

“A job failure is not hidden. The next batch stops, a failure checkpoint is created, and ownership moves to the agreed recovery path.”

## 9:00 — Return to proof

Show the [measurement plan](../06-measurement-and-proof.md).

“The demo proves the workflow can be experienced. The POV tests whether it improves your baseline without violating guardrails.”

Close with: “Which local result would justify expanding this pattern?”
