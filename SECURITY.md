# Security policy

This repository is a reference and demonstration system. It is not a credential store and must not receive production secrets, customer data, internal tokens, private endpoints, or exported job artifacts containing sensitive facts.

## Supported versions

Security corrections are applied to the current major version. Older examples should be retired or clearly marked unsupported.

## Reporting

Report a suspected vulnerability privately to the repository maintainers through the approved organizational security channel. Do not open a public issue containing exploit details, credentials, or customer information.

## Demo safety

- Simulation mode is the default.
- Live patching requires an explicit execution confirmation variable.
- Credentials are injected at runtime through the platform credential system.
- TLS verification remains enabled.
- Evidence examples redact secrets and minimize host data.
- Production use requires threat modeling, least-privilege review, recovery testing, and customer change approval.
