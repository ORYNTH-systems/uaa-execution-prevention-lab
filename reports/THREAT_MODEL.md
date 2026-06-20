# UAA Doctrine Registry

## Purpose

This registry identifies the doctrine statements currently represented in the UAA Execution Prevention Lab.

| Doctrine ID | Doctrine Statement | Repository Representation |
|---|---|---|
| UAA-D-002 | Authorization does not imply admissibility. | admissibility evaluation and violation collection |
| UAA-D-003 | Admissibility is reconstructed from current reality. | collect_violations() and evaluate_admissibility() |
| UAA-D-005 | Reconciliation is required before execution. | reconciliation_required() |
| UAA-D-008 | Execution must be declined when admissibility fails. | execution_result = DECLINED |

## Canonical Principle

```text
Authorization State != Execution-Admissibility State
@'
# UAA Execution Prevention Lab — Threat Model

## Purpose

This document identifies the failure classes represented by the UAA Execution Prevention Lab and clarifies the system assumptions.

## Threats Represented

| Threat | Demonstrated By |
|---|---|
| State changes after authorization | EP-001 |
| Agent action drift | EP-002 |
| Authorization expiry | EP-003 |
| Counterparty risk escalation | EP-004 |
| Compound admissibility failure | EP-005 |
| Delegation revocation | EP-006 |
| Actor identity substitution | EP-007 |
| Resource overrun | EP-008 |
| Policy change before execution | EP-009 |
| Multi-actor authority conflict | EP-010 |

## Core Risk

The primary risk modeled by this repository is execution based on stale or incomplete authorization state.

## Security Objective

Prevent execution when current reality state invalidates execution admissibility.

## System Assumptions

- Case input data is available before execution.
- Reconciliation occurs before execution.
- Admissibility rules are evaluated deterministically.
- Failed admissibility results cause fail-closed execution behavior.

## Out of Scope

This repository does not currently model:

- Distributed consensus
- Cryptographic signing
- Network adversaries
- Identity-provider compromise
- External policy-engine integration
- Production runtime deployment
