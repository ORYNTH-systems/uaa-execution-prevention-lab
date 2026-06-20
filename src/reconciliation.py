from models import ExecutionCase


def reconciliation_required(case: ExecutionCase) -> bool:
    """
    UAA-D-005
    Reconciliation is required before execution.
    """
    return True


def vendor_state_changed(case: ExecutionCase) -> bool:
    """
    Detect whether vendor state changed between
    authorization and execution.
    """
    return (
        case.initial_vendor_status
        != case.current_vendor_status
    )