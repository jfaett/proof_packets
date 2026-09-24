# patch_precheck

Validates normalized readiness facts before patching. Environment-specific adapters should gather disk, repository, application, and cluster facts, then pass them to this contract.

## Inputs

- precheck_disk_free_mb
- precheck_min_free_mb
- precheck_repo_reachable
- precheck_package_ready
- precheck_service_healthy

## Output

patch_precheck_result with normalized checks and passed state.

## Failure

Terminal for the host or batch. Do not progress to quiesce or update. Record the failed check and assign remediation.

## Why normalized inputs

Repository access, cluster health, and package readiness differ by customer. Keeping collection adapters outside the shared gate avoids pretending one probe fits every environment.
