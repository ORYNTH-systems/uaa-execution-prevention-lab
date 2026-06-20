from models import ExecutionCase
from reconciliation import (
    vendor_state_changed,
    intent_drift_detected,
    authorization_expired,
    counterparty_risk_state_changed,
)

ADMISSIBILITY_RULES = [
    vendor_state_changed,
    intent_drift_detected,
    authorization_expired,
    counterparty_risk_state_changed,
]


def evaluate_admissibility(case: ExecutionCase) -> bool:
    """
    UAA-D-002
    Authorization does not imply admissibility.

    UAA-D-003
    Admissibility is reconstructed.
    """

    for rule in ADMISSIBILITY_RULES:
        if rule(case):
            return False

    return True
