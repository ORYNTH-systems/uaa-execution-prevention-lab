import json

from models import ExecutionCase, EvaluationResult
from reconciliation import reconciliation_required
from admissibility import evaluate_admissibility


def load_case(path: str) -> ExecutionCase:
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return ExecutionCase(
        case_id=data["case_id"],
        title=data["title"],
        authorization=data["initial_state"]["authorization"],
        initial_vendor_status=data["initial_state"]["vendor_status"],
        current_vendor_status=data["state_change"]["vendor_status"],
        execution_requested=data["execution_attempt"]["requested"],
    )


def evaluate_case(case: ExecutionCase) -> EvaluationResult:
    authorization_valid = case.authorization == "VALID"
    reconciliation = reconciliation_required(case)
    admissibility = evaluate_admissibility(case)

    execution_result = (
        "EXECUTED"
        if authorization_valid and reconciliation and admissibility
        else "DECLINED"
    )

    failure_prevented = (
        authorization_valid
        and case.execution_requested
        and not admissibility
        and execution_result == "DECLINED"
    )

    return EvaluationResult(
        case_id=case.case_id,
        authorization_valid=authorization_valid,
        reconciliation_required=reconciliation,
        admissibility=admissibility,
        execution_result=execution_result,
        failure_prevented=failure_prevented,
    )


def main() -> None:
    case = load_case("cases/EP-001_VENDOR_BLACKLIST.json")
    result = evaluate_case(case)

    print(f"Case: {case.case_id} - {case.title}")
    print(f"Authorization Valid: {result.authorization_valid}")
    print(f"Reconciliation Required: {result.reconciliation_required}")
    print(f"Admissibility: {result.admissibility}")
    print(f"Execution Result: {result.execution_result}")
    print(f"Failure Prevented: {result.failure_prevented}")


if __name__ == "__main__":
    main()