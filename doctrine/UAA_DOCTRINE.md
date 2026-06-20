# Unified Agency Architecture Doctrine Registry

## UAA-D-001 — Semantic State Separation

Capability, authority, admissibility, and execution are distinct states. No state may be treated as equivalent to another.

**Operational consequence:** A system may not infer execution permission from capability, identity, role, credential, or prior authorization.

---

## UAA-D-002 — Authority Non-Implication

Authorization does not imply execution admissibility.

**Operational consequence:** An authorized action must still pass execution-time admissibility evaluation.

---

## UAA-D-003 — Admissibility Reconstruction

Execution admissibility is reconstructed from current reality state.

**Operational consequence:** Execution eligibility is not stored as a durable permission.

---

## UAA-D-004 — Temporal Non-Inheritance

A prior valid state does not automatically persist into a future execution state.

**Operational consequence:** Time passage, state change, revocation, expiry, drift, or dependency failure may invalidate execution.

---

## UAA-D-005 — Reconciliation Precondition

Execution requires reconciliation between authorized intent and current reality state.

**Operational consequence:** Execution cannot proceed directly from authorization.

---

## UAA-D-006 — Boundary Contemporaneity

Execution boundaries must be evaluated at the time of attempted execution.

**Operational consequence:** Stale boundaries cannot authorize current execution.

---

## UAA-D-007 — Execution Non-Effectuation

A system may determine that execution is inadmissible without producing execution.

**Operational consequence:** Declined execution is a valid system outcome.

---

## UAA-D-008 — Fail-Closed Execution

If admissibility cannot be established, execution must be declined.

**Operational consequence:** Uncertainty does not authorize execution.

---

## Core Doctrine

Execution authority is not inherited.

Execution authority is reconstructed from current admissibility conditions.
