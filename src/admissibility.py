from models import ExecutionCase
from reconciliation import (
    vendor_state_changed,
    intent_drift_detected,
    authorization_expired,
    counterparty_risk_state_changed,
    delegation_revoked,
)

ADMISSIBILITY_RULES = [
    ("vendor_state_changed", vendor_state_changed),
    ("intent_drift_detected", intent_drift_detected),
    ("authorization_expired", authorization_expired),
    ("counterparty_risk_state_changed", counterparty_risk_state_changed),
    ("delegation_revoked", delegation_revoked),
]


def collect_violations(case: ExecutionCase) -> list[str]:
    violations = []

    for rule_name, rule in ADMISSIBILITY_RULES:
        if rule(case):
            violations.append(rule_name)

    return violations


def evaluate_admissibility(case: ExecutionCase) -> bool:
    """
    UAA-D-002
    Authorization does not imply admissibility.

    UAA-D-003
    Admissibility is reconstructed.
    """

    return len(collect_violations(case)) == 0