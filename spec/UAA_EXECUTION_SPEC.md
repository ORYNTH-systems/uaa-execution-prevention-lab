\# UAA Execution Specification



\## State Model



Intent

↓

Evaluation

↓

Authorization

↓

Reconciliation

↓

Execution Admissibility

↓

Execution



\---



\## Core Invariant



Authorization State ≠ Execution-Admissibility State



\---



\## Allowed Transitions



Intent → Evaluation



Evaluation → Authorization



Authorization → Reconciliation



Reconciliation → Execution Admissibility



Execution Admissibility → Execution



\---



\## Forbidden Transitions



Capability → Execution



Authorization → Execution



Prior Execution → Future Execution



\---



\## Execution Rule



Execution SHALL NOT occur unless execution admissibility evaluates TRUE at execution time.



\---



\## Reconciliation Rule



Current reality state SHALL be evaluated prior to execution.



\---



\## Failure Rule



If admissibility evaluates FALSE:



Execution Result = DECLINED

