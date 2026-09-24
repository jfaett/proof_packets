# approval_gate

Refuses workflow progression unless the supplied approval state is allowed.

In an AAP production workflow, prefer a controller Approval node for an actual human pause and authorization boundary. This role validates that downstream automation received approved context; it does not create independent authorization.

## Inputs

- approval_status
- approval_reference
- approval_allowed_statuses

## Output

approval_gate_result with status, reference, and passed.

## Failure

Terminal for the current path. Route denial or timeout to the workflow failure branch and record it.

## Security boundary

The caller is responsible for authenticating the approver and protecting the approval record. Do not accept an untrusted survey value as authoritative approval.

Official reference: [AAP approval nodes](https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6/develop-ref_controller_approval_nodes).
