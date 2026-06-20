# UAA Execution Specification

## 1. Purpose

This specification defines the minimum execution-prevention mechanism required to demonstrate UAA execution admissibility reconstruction.

## 2. State Model

The system recognizes the following states:

- Intent
- Evaluation
- Authorization
- Reconciliation
- Execution Admissibility
- Execution Outcome

## 3. Core Invariant

Authorization State ? Execution-Admissibility State

## 4. Required Transition Path

Intent
? Evaluation
? Authorization
? Reconciliation
? Execution Admissibility
? Execution Outcome

## 5. Forbidden Transitions

The following transitions are invalid:

- Capability ? Execution
- Authorization ? Execution
- Prior Admissibility ? Current Execution
- Prior Execution ? Future Execution

## 6. Reconciliation Rule

Before execution, the system SHALL evaluate current reality state against the authorized intent.

## 7. Admissibility Rule

Execution admissibility SHALL evaluate TRUE only if all required current-state conditions remain satisfied.

## 8. Decline Rule

If admissibility evaluates FALSE, execution outcome SHALL be DECLINED.

## 9. Fail-Closed Rule

If admissibility cannot be determined, execution outcome SHALL be DECLINED.

## 10. EP-001 Required Demonstration

EP-001 SHALL demonstrate the following:

1. A purchase request is authorized.
2. Vendor status changes after authorization.
3. Execution is attempted.
4. Reconciliation detects the changed vendor state.
5. Admissibility evaluates FALSE.
6. Execution is declined.
7. The report records a prevented invalid execution event.
