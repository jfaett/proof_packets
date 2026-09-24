# evidence_checkpoint

Writes a structured, redacted JSON checkpoint on the controller so workflow stages can be correlated with request, host, pack, and content version.

## Inputs

- evidence_stage
- evidence_payload
- evidence_directory
- evidence_pack_version
- evidence_change_reference

## Outputs

- evidence_checkpoint_result
- one JSON file per host and stage

## Failure

Treat inability to produce required evidence according to policy. For regulated or contractual controls, the workflow should fail closed.

## Data handling

Do not put secrets, full command output, personal data, or unapproved host facts into the payload. The customer owns retention, redaction, access, and export policy.
