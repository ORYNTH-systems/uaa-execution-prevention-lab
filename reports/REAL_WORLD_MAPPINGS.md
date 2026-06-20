\# UAA Execution Prevention Lab — Real World Mappings



\## Purpose



This document maps execution-prevention demonstrations to real-world failure scenarios.



The goal is to show why execution admissibility must be reconstructed immediately before execution.



\---



\## EP-001 — Vendor Status Revocation



Scenario:



A vendor is approved during authorization.



Before payment execution, vendor status changes.



Risk:



Payment may be issued to a vendor that no longer satisfies eligibility requirements.



Result:



Execution declined.



\---



\## EP-002 — Agent Action Drift



Scenario:



An AI agent is authorized for one task.



Before execution, the agent attempts a different action.



Risk:



Execution occurs outside authorized intent.



Result:



Execution declined.



\---



\## EP-003 — Healthcare Authorization Expiry



Scenario:



Medical authorization exists when approved.



Authorization expires before procedure execution.



Risk:



Services may be delivered without valid authorization.



Result:



Execution declined.



\---



\## EP-004 — Financial Settlement Risk Change



Scenario:



Settlement is authorized.



Counterparty becomes high-risk before execution.



Risk:



Settlement proceeds despite updated risk state.



Result:



Execution declined.



\---



\## EP-005 — Compound Failure



Scenario:



Multiple admissibility failures occur simultaneously.



Risk:



Execution proceeds despite multiple invalidating conditions.



Result:



Execution declined.



\---



\## EP-006 — Delegation Revocation



Scenario:



Authority is delegated.



Delegation is revoked before execution.



Risk:



Execution proceeds using invalid authority.



Result:



Execution declined.



\---



\## EP-007 — Identity Continuity Failure



Scenario:



Authorization belongs to one actor.



Execution attempt originates from another.



Risk:



Unauthorized execution under identity substitution.



Result:



Execution declined.



\---



\## EP-008 — Resource Constraint Violation



Scenario:



Execution exceeds approved resource limits.



Risk:



Resource exhaustion or unauthorized consumption.



Result:



Execution declined.



\---



\## EP-009 — Policy Change



Scenario:



Authorization occurs under one policy version.



Execution occurs after policy revision.



Risk:



Execution proceeds under outdated governance conditions.



Result:



Execution declined.



\---



\## EP-010 — Multi-Actor Authority Conflict



Scenario:



One actor authorizes an action.



A different actor modifies execution parameters.



Risk:



Authority continuity and intent continuity are broken.



Result:



Execution declined.



\---



\## Demonstrated Principle



Across all demonstrations:



Authorization existed.



Execution admissibility failed.



Execution was declined.



Failure was prevented.



The evidence corpus demonstrates that execution decisions should depend on current admissibility rather than historical authorization.



