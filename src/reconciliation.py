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

    return case.authorized_intent != case.current_action