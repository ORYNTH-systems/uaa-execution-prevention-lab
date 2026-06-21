from models import ExecutionCase


def vendor_state_changed(case: ExecutionCase) -> bool:
    return (
        case.initial_vendor_status
        and case.current_vendor_status
        and case.initial_vendor_status != case.current_vendor_status
    )


def intent_drift_detected(case: ExecutionCase) -> bool:
    return (
        case.authorized_intent
        and case.current_action
        and case.authorized_intent != case.current_action
    )


def authorization_expired(case: ExecutionCase) -> bool:
    return (
        case.authorization_expiration
        and case.current_date
        and case.current_date > case.authorization_expiration
    )


def counterparty_risk_state_changed(case: ExecutionCase) -> bool:
    return (
        case.initial_counterparty_status
        and case.current_counterparty_status
        and case.initial_counterparty_status != case.current_counterparty_status
    ) or bool(case.risk_flag)


def delegation_revoked(case: ExecutionCase) -> bool:
    return (
        case.initial_delegation_status
        and case.current_delegation_status
        and case.initial_delegation_status != case.current_delegation_status
    )


def identity_continuity_failed(case: ExecutionCase) -> bool:
    return (
        case.authorized_actor
        and case.current_actor
        and case.authorized_actor != case.current_actor
    )


def resource_constraint_violated(case: ExecutionCase) -> bool:
    return (
        case.resource_limit
        and case.resource_required
        and case.resource_required > case.resource_limit
    )


def policy_change_detected(case: ExecutionCase) -> bool:
    return (
        case.policy_version
        and case.current_policy_version
        and case.policy_version != case.current_policy_version
    )


ADMISSIBILITY_RULES = [
    ("vendor_state_changed", vendor_state_changed),
    ("intent_drift_detected", intent_drift_detected),
    ("authorization_expired", authorization_expired),
    ("counterparty_risk_state_changed", counterparty_risk_state_changed),
    ("delegation_revoked", delegation_revoked),
    ("identity_continuity_failed", identity_continuity_failed),
    ("resource_constraint_violated", resource_constraint_violated),
    ("policy_change_detected", policy_change_detected),
]


def collect_violations(case: ExecutionCase) -> list[str]:
    if isinstance(case, list):
        raise TypeError("collect_violations received list instead of ExecutionCase")

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
