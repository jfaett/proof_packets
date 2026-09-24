# system_of_record_update

Writes a normalized workflow checkpoint to a system of record. Simulation writes a local JSON fixture; live mode uses an HTTPS API contract.

## Inputs

- demo_mode
- sor_endpoint
- sor_token
- sor_method
- sor_payload
- sor_evidence_directory

## Output

system_of_record_update_result with mode and status.

## Failure

Retry only according to the API and customer policy. Do not falsely mark a service accepted when the authoritative record was not updated. Queue or escalate if the workflow may continue without the record.

## Security

Inject tokens from AAP credentials, keep no_log enabled, validate TLS, scope the service account, and never store credentials in repository variables.

Official reference: [ansible.builtin.uri](https://docs.ansible.com/projects/ansible/latest/collections/ansible/builtin/uri_module.html).
