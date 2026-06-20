## Additional Reviewer Resources

This repository includes supplemental artifacts designed for independent verification, reproducibility, and audit clarity.

---

## Evidence Library

A complete catalog of all execution-prevention demonstrations, including:

- Case identifiers
- Violations triggered
- Rule hit counts
- Category-level aggregation
- Outcome metrics
- Prevention rate summary

---

## Real-World Mappings

Maps each execution-prevention case to a representative real-world failure scenario to contextualize system behavior.

Each mapping links:

- Abstract failure class
- System-level condition
- Equivalent real-world risk pattern

---

## Structured JSON Evidence

Each execution case produces a machine-readable artifact containing:

- case_id
- admissibility result
- execution result
- failure_prevented flag
- triggered violations

These outputs enable deterministic validation and external reproducibility.

---

## Replay Support

All demonstrations can be re-executed deterministically.

### Run full corpus

```powershell
python src\main.py --all