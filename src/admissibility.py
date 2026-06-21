from rules import ADMISSIBILITY_RULES
from models import ExecutionCase


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
