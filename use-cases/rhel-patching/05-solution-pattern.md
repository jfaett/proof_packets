# AAP solution pattern and architecture

## Positioning

Use AAP as the governed coordinator of an approved service workflow. Keep platform-native ownership where it belongs.

~~~mermaid
flowchart TB
  REQ[ITSM request and approval]
  INV[Authoritative inventory / CMDB]
  AAP[AAP workflow, RBAC, credentials, jobs]
  SAT[Approved content source / Satellite]
  APP[Application, cluster, load balancer, backup]
  RHEL[RHEL pilot and batches]
  OBS[Monitoring and service tests]
  EVD[ITSM, CMDB, evidence store]

  REQ -->|approved context| AAP
  INV -->|targets and owners| AAP
  AAP -->|approved content reference| SAT
  AAP -->|quiesce / restore contract| APP
  AAP -->|precheck, update, reboot| RHEL
  RHEL -->|host result| AAP
  AAP -->|verification request| OBS
  OBS -->|service result| AAP
  AAP -->|progress, verified state, version refs| EVD
~~~

## Logical workflow

~~~mermaid
flowchart LR
  A[Validate request] --> B[Approval node]
  B --> C[Pilot precheck]
  C --> D[Pilot prepare]
  D --> E[Pilot update]
  E --> F[Pilot reboot / restore]
  F --> G[Pilot service verify]
  G --> H{Accept next batch?}
  H -- yes --> I[Batch workflow]
  I --> J[Final evidence and acceptance]
  B -- denied / timeout --> X[Record and stop]
  C -- failed --> X
  G -- failed --> Y[Recover or escalate]
  Y --> X
~~~

## AAP objects

| Object | Purpose | Owner |
|---|---|---|
| Project | Versioned Proof Pack and customer adaptation | Automation content team |
| Inventory | Approved targets and groups; not the source of truth unless designed as one | Platform team |
| Credentials | Least-privilege machine, API, and vault credentials | Platform/security |
| Execution environment | Pinned runtime and collections | Platform team |
| Job templates | Precheck, prepare, patch, verify, evidence adapters | Content owners |
| Workflow template | Sequence, approval, success/failure edges, pilot/batch gates | Service owner + content owner |
| Approval nodes | Human authorization or acceptance with timeout and failure path | Service/change owner |
| Notifications | Actionable progress and exception routing | Service owner |

## Workflow node scaffold

See [workflow-nodes.yml](demo/controller/workflow-nodes.yml). It is a design contract, not an importable universal controller configuration, because credential, inventory, and organization IDs are customer-specific.

## Trust boundaries

**CUSTOMER INPUT REQUIRED**

- Identity: map controller users, service accounts, and approvers.
- Authorization: separate launch, approve, administer, and credential-use permissions.
- Credentials: inject through AAP; never put tokens in variables or Git.
- Network: use approved execution paths and customer security boundaries.
- Content: pin project revision, execution environment, collection versions, and content reference.
- Data: minimize and classify host/evidence fields.
- Evidence: link request, job, inventory snapshot, workflow version, content version, and acceptance.
- Recovery: preserve out-of-band access and application-specific ownership.

## Supported reference modules

The safe scaffold uses fully qualified ansible.builtin modules. The live reference paths rely on dnf, reboot, service_facts, uri, assert, copy, and file. Validate module and platform support against the customer's approved AAP execution environment.

## Non-goals

- replace Satellite content lifecycle;
- infer approval from untrusted input;
- create a generic application recovery algorithm;
- guarantee package rollback;
- update unverified CMDB state;
- define production batching without customer service topology.
