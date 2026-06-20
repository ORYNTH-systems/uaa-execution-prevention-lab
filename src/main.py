import json

from models import ExecutionCase, EvaluationResult
from reconciliation import (
    reconciliation_required,
    intent_drift_detected,
    authorization_expired,
)
from admissibility import evaluate_admissibility


def load_case(path: str) -> ExecutionCase:
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    initial_state = data.get("initial_state", {})
    state_change = data.get("state_change", {})
    execution_attempt = data.get("execution_attempt", {})

    return ExecutionCase(
        case_id=data["case_id"],
        title=data["title"],
        authorization=initial_state.get("authorization", ""),
        initial_vendor_status=initial_state.get("vendor_status", ""),
        current_vendor_status=state_change.get("vendor_status", ""),
        execution_requested=execution_attempt.get("requested", False),
        authorized_intent=initial_state.get("authorized_intent", ""),
        current_action=state_change.get("current_agent_action", ""),
        authorization_expiration=initial_state.get("authorization_expiration", ""),
        current_date=state_change.get("current_date", ""),
        current_authorization_status=state_change.get("authorization_status", ""),
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


def print_result(case: ExecutionCase, result: EvaluationResult) -> None:
    print(f"Case: {case.case_id} - {case.title}")
    print(f"Authorization Valid: {result.authorization_valid}")
    print(f"Reconciliation Required: {result.reconciliation_required}")

    if case.authorized_intent:
        print(f"Authorized Intent: {case.authorized_intent}")
        print(f"Current Action: {case.current_action}")
        print(f"Intent Drift Detected: {intent_drift_detected(case)}")

    if case.authorization_expiration:
        print(f"Authorization Expiration: {case.authorization_expiration}")
        print(f"Current Date: {case.current_date}")
        print(f"Authorization Expired: {authorization_expired(case)}")

    print(f"Admissibility: {result.admissibility}")
    print(f"Execution Result: {result.execution_result}")
    print(f"Failure Prevented: {result.failure_prevented}")


def main() -> None:
    cases = [
        "cases/EP-001_VENDOR_BLACKLIST.json",
        "cases/EP-002_AGENT_ACTION_DRIFT.json",
        "cases/EP-003_HEALTHCARE_AUTHORIZATION_EXPIRY.json",
    ]

    for index, case_path in enumerate(cases):
        case = load_case(case_path)
        result = evaluate_case(case)
        print_result(case, result)

        if index < len(cases) - 1:
            print()


if __name__ == "__main__":
    main()
