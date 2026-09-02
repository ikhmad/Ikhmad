# Incident Lifecycle

A public example lifecycle:

```text
REPORTED
   |
   v
UNDER_REVIEW
   |
   +----> REJECTED
   |
   v
PROBABLE
   |
   v
CONFIRMED
   |
   v
ACTIVE
   |
   v
CONTROLLED
   |
   v
CLOSED
```

The exact confidence thresholds and transition rules are proprietary and are not defined in this public repository.

## Design goals

- maintain traceable state changes;
- distinguish observations from validated incidents;
- preserve source provenance;
- support auditability;
- allow professional overrides where operationally authorized.
