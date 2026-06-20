from models import ExecutionCase


def reconciliation_required(case: ExecutionCase) -> bool:
    """
    UAA-D-005
    Reconciliation is required before execution.
    """
    return True


def vendor_state_changed(case: ExecutionCase) -> bool:
    """
    EP-001:
    Detect whether vendor state changed between
    authorization and execution.
    """
    if not case.initial_vendor_status:
        return False

    return (
        case.initial_vendor_status
        != case.current_vendor_status
    )


def intent_drift_detected(case: ExecutionCase) -> bool:
    """
    EP-002:
    Detect whether the current agent action differs
    from the originally authorized intent.
    """
    if not case.authorized_intent:
        return False

    if not case.current_action:
        return False

    return case.authorized_intent != case.current_action


def authorization_expired(case: ExecutionCase) -> bool:
    """
    EP-003:
    Detect whether authorization expired before execution.
    """
    if case.current_authorization_status == "EXPIRED":
        return True

    if not case.authorization_expiration or not case.current_date:
        return False

    return case.current_date > case.authorization_expiration


def counterparty_risk_state_changed(case: ExecutionCase) -> bool:
    """
    EP-004:
    Detect whether counterparty risk state changed before settlement execution.
    """
    if case.risk_flag:
        return True

    if not case.initial_counterparty_status:
        return False

    return (
        case.initial_counterparty_status
        != case.current_counterparty_status
    )


def delegation_revoked(case: ExecutionCase) -> bool:
    """
    EP-006:
    Detect whether delegated authority was revoked before execution.
    """
    if not case.initial_delegation_status:
        return False

    return case.current_delegation_status == "REVOKED"


def identity_continuity_failed(case: ExecutionCase) -> bool:
    """
    EP-007:
    Detect whether execution is being attempted by a
    different actor than the actor originally authorized.
    """
    if not case.authorized_actor:
        return False

    if not case.current_actor:
        return False

    return case.authorized_actor != case.current_actor


def resource_constraint_violated(case: ExecutionCase) -> bool:
    """
    EP-008:
    Detect whether required execution resources exceed
    the authorized or available resource limit.
    """
    if not case.resource_limit:
        return False

    if not case.resource_required:
        return False

    return case.resource_required > case.resource_limit