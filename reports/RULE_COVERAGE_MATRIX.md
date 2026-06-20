# UAA Execution Prevention Lab — Rule Coverage Matrix

## Purpose

This matrix shows which admissibility rules are triggered by each execution-prevention demonstration.

| Rule | EP-001 | EP-002 | EP-003 | EP-004 | EP-005 | EP-006 | EP-007 | EP-008 | EP-009 | EP-010 |
|---|---|---|---|---|---|---|---|---|---|---|
| vendor_state_changed | X |  |  |  |  |  |  |  |  |  |
| intent_drift_detected |  | X |  |  | X |  |  |  |  | X |
| authorization_expired |  |  | X |  | X |  |  |  |  |  |
| counterparty_risk_state_changed |  |  |  | X | X |  |  |  |  |  |
| delegation_revoked |  |  |  |  |  | X |  |  |  |  |
| identity_continuity_failed |  |  |  |  |  |  | X |  |  | X |
| resource_constraint_violated |  |  |  |  |  |  |  | X |  |  |
| policy_change_detected |  |  |  |  |  |  |  |  | X |  |

## Summary

The corpus covers:

- State drift
- Intent drift
- Temporal expiry
- Risk-state drift
- Authority revocation
- Identity continuity failure
- Resource constraint violation
- Policy change
- Multi-actor authority conflict
- Compound admissibility failure
