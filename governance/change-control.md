# Change control

## Change classes

| Class | Example | Review |
|---|---|---|
| Editorial | Typo or clearer explanation | Repository maintainer |
| Compatible | New optional metric or adapter | Content owner plus affected consumers |
| Operational | Changed task, permission, failure behavior, or dependency | Content, platform, security/change owners |
| Breaking | Removed input, changed evidence contract, renamed deep link | Major version and migration plan |

## Required sequence

1. Describe the reason and affected consumers.
2. Update contract and tests together.
3. Run automated and scenario validation.
4. Review security, recovery, and evidence impact.
5. Record version and changelog.
6. Promote the approved version.
7. Communicate migration and retirement dates.
