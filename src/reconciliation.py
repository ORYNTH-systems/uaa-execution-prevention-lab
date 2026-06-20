from models import ExecutionCase


def reconciliation_required(case: ExecutionCase) -> bool:
    """
    UAA-D-005
    Reconciliation is required before execution.
    """
    return True


def vendor_state_changed(case: ExecutionCase) -> bool:
    if not case.initial_vendor_status:
        return False

    if not case.current_vendor_status:
        return False

    return case.initial_vendor_status != case.current_vendor_status


def intent_drift_detected(case: ExecutionCase) -> bool:
    if not case.authorized_intent:
        return False

    if not case.current_action:
        return False

    return case.authorized_intent != case.current_action


def authorization_expired(case: ExecutionCase) -> bool:
    if case.current_authorization_status == "EXPIRED":
        return True

    if not case.authorization_expiration:
        return False

    if not case.current_date:
        return False

    return case.current_date > case.authorization_expiration


def counterparty_risk_state_changed(case: ExecutionCase) -> bool:
    if case.risk_flag:
        return True

    if not case.initial_counterparty_status:
        return False

    if not case.current_counterparty_status:
        return False

    return case.initial_counterparty_status != case.current_counterparty_status


def delegation_revoked(case: ExecutionCase) -> bool:
    if not case.initial_delegation_status:
        return False

    if not case.current_delegation_status:
        return False

    return case.current_delegation_status == "REVOKED"


def identity_continuity_failed(case: ExecutionCase) -> bool:
    if not case.authorized_actor:
        return False

    if not case.current_actor:
        return False

    return case.authorized_actor != case.current_actor


def resource_constraint_violated(case: ExecutionCase) -> bool:
    if not case.resource_limit:
        return False

    if not case.resource_required:
        return False

    return case.resource_required > case.resource_limit


def policy_change_detected(case: ExecutionCase) -> bool:
    if not case.policy_version:
        return False

    if not case.current_policy_version:
        return False

    return case.policy_version != case.current_policy_version