# controlled_reboot

Reboots a host only when required and waits for it to return within a bounded timeout. Simulation is the default.

## Inputs

- demo_mode
- reboot_required
- reboot_timeout_seconds
- reboot_test_command

## Output

controlled_reboot_result with required, performed, simulated, and ready state.

## Failure

Stop the host and next batch. Preserve out-of-band access and escalate through the agreed platform and application recovery plan.

Official reference: [ansible.builtin.reboot](https://docs.ansible.com/projects/ansible/latest/collections/ansible/builtin/reboot_module.html).
