\# UAA Doctrine to Rule Mapping



\## Purpose



This document establishes traceability between UAA doctrine and executable admissibility rules.



\---



\## UAA-D-002



Authorization does not imply admissibility.



Mapped Rules:



\* vendor\_state\_changed

\* intent\_drift\_detected

\* authorization\_expired

\* counterparty\_risk\_state\_changed

\* delegation\_revoked

\* identity\_continuity\_failed

\* resource\_constraint\_violated

\* policy\_change\_detected



\---



\## UAA-D-003



Admissibility is reconstructed from current reality.



Mapped Components:



\* collect\_violations()

\* evaluate\_admissibility()



\---



\## UAA-D-005



Reconciliation is required before execution.



Mapped Components:



\* reconciliation\_required()



\---



\## UAA-D-008



Execution must be declined when admissibility fails.



Mapped Components:



\* execution\_result = DECLINED

\* failure\_prevented = True



\---



\## Rule Registry



\### vendor\_state\_changed



Doctrine:



\* UAA-D-002

\* UAA-D-003



Category:



\* State



Cases:



\* EP-001



\---



\### intent\_drift\_detected



Doctrine:



\* UAA-D-002

\* UAA-D-003



Category:



\* Intent



Cases:



\* EP-002

\* EP-005

\* EP-010



\---



\### authorization\_expired



Doctrine:



\* UAA-D-002

\* UAA-D-003



Category:



\* Temporal



Cases:



\* EP-003

\* EP-005



\---



\### counterparty\_risk\_state\_changed



Doctrine:



\* UAA-D-002

\* UAA-D-003



Category:



\* Risk



Cases:



\* EP-004

\* EP-005



\---



\### delegation\_revoked



Doctrine:



\* UAA-D-002

\* UAA-D-003



Category:



\* Authority



Cases:



\* EP-006



\---



\### identity\_continuity\_failed



Doctrine:



\* UAA-D-002

\* UAA-D-003



Category:



\* Identity



Cases:



\* EP-007

\* EP-010



\---



\### resource\_constraint\_violated



Doctrine:



\* UAA-D-002

\* UAA-D-003



Category:



\* Resource



Cases:



\* EP-008



\---



\### policy\_change\_detected



Doctrine:



\* UAA-D-002

\* UAA-D-003



Category:



\* Policy



Cases:



\* EP-009



\---



\## Traceability Chain



Doctrine

↓

Rule

↓

Case

↓

Evaluation

↓

Evidence

↓

Metrics



