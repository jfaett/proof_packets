# Process maps

## ILLUSTRATIVE current state

~~~mermaid
flowchart LR
  A[Change approved] --> B[Operator reconciles target list]
  B --> C[Operator launches prechecks]
  C --> D{Checks pass?}
  D -- no --> X[Investigate and update ticket]
  D -- yes --> E[Coordinate app drain and backup]
  E --> F[Launch patch action]
  F --> G[Review results]
  G --> H[Reboot where needed]
  H --> I[Ask app owner to test]
  I --> J{Accepted?}
  J -- no --> Y[Recover and assemble exception evidence]
  J -- yes --> K[Update ITSM and CMDB]
  K --> L[Accept or start next batch]
~~~

Likely measurement points are the waits before scope reconciliation, application coordination, next-batch acceptance, and record completion. **CUSTOMER INPUT REQUIRED:** Observe rather than assume where the actual constraint exists.

## ILLUSTRATIVE future state

~~~mermaid
flowchart LR
  A[Approved request and scope] --> B[AAP validates policy and context]
  B --> C[Automated normalized prechecks]
  C --> D{Pass?}
  D -- no --> X[Stop, record, assign recovery]
  D -- yes --> E[Call approved quiesce and recovery controls]
  E --> F[Apply approved content]
  F --> G[Bounded reboot and readiness]
  G --> H[Automated service checks]
  H --> I{Owner acceptance required?}
  I -- yes --> J[Approval / acceptance node]
  I -- no --> K[Record verified state]
  J --> K
  K --> L[Next approved batch]
~~~

The future state removes avoidable coordination while retaining accountable decisions. Native tools continue to own their domain.
