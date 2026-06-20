from models import ExecutionCase
from reconciliation import vendor_state_changed


def evaluate_admissibility(case: ExecutionCase) -> bool:
    """
    UAA-D-002
    Authorization does not imply admissibility.

    UAA-D-003
    Admissibility is reconstructed.
    """

    if vendor_state_changed(case):
        return False

    return True