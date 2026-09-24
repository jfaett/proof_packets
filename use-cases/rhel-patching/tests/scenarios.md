# Scenario tests

## 1. Happy-path simulation

Given approved context and passing normalized checks, both pilot and batch simulations complete, evidence checkpoints exist, and the simulated system-of-record record shows accepted state.

## 2. Approval denial

Set approval_status to denied. The workflow must stop before precheck or change work.

## 3. Precheck failure

Set precheck_repo_reachable to false. The workflow must stop before quiesce or update and must identify the failed contract.

## 4. Service verification failure

Set simulated_health_passed to false. The workflow must stop after the simulated change, must not write accepted state, and must route discussion to recovery.

## 5. Live execution gate

Set demo_mode to false and patch_execute_confirmed to false. The workflow must refuse package execution.

## 6. Evidence contract

For a successful simulation, every checkpoint includes stage, change reference, host, pack version, and UTC timestamp. No token or credential may appear.

## 7. Scope control

Inventory must include only explicit pilot and batch aliases. An unintended host must not be selected by a wildcard outside rhel_patch_targets.
