# apply_updates

Applies approved package updates on RHEL when live execution is explicitly authorized. Simulation is the default.

## Inputs

- demo_mode
- patch_execute_confirmed
- patch_security_only

## Output

apply_updates_result with simulation state and change result.

## Failure

Stop the host and next batch. Package rollback is not assumed. Follow the customer recovery plan, which may use snapshots, application recovery, package downgrade, rebuild, or vendor guidance.

## Safety

Live mode requires patch_execute_confirmed=true. The role uses ansible.builtin.dnf with update_only and GPG checking enabled. Approved repository and content-view selection remains a customer platform responsibility.

Official reference: [ansible.builtin.dnf](https://docs.ansible.com/projects/ansible/latest/collections/ansible/builtin/dnf_module.html).
