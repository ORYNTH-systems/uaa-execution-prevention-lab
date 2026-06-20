from models import ExecutionCase
from reconciliation import (
    vendor_state_changed,
    intent_drift_detected,
)


def evaluate_admissibility(case: ExecutionCase) -> bool:
    """
    UAA-D-002
    Authorization does not imply admissibility.

    UAA-D-003
    Admissibility is reconstructed.
    """

    if vendor_state_changed(case):
        return False

    if intent_drift_detected(case):
        return False

    return True
