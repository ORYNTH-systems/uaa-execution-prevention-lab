import json

from models import ExecutionCase, EvaluationResult
from reconciliation import (
    reconciliation_required,
    intent_drift_detected,
    authorization_expired,
    counterparty_risk_state_changed,
    delegation_revoked,
    identity_continuity_failed,
)
from admissibility import evaluate_admissibility, collect_violations
from metrics import generate_metrics


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
        initial_counterparty_status=initial_state.get("counterparty_status", ""),
        current_counterparty_status=state_change.get("counterparty_status", ""),
        risk_flag=state_change.get("risk_flag", False),
        initial_delegation_status=initial_state.get("delegation_status", ""),
        current_delegation_status=state_change.get("delegation_status", ""),
        authorized_actor=initial_state.get("authorized_actor", ""),
        current_actor=state_change.get("current_actor", ""),
    )


def evaluate_case(case: ExecutionCase) -> EvaluationResult:
    authorization_valid = case.authorization == "VALID"
    reconciliation = reconciliation_required(case)
    violations = collect_violations(case)
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
        violations=violations,
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

    if case.initial_counterparty_status:
        print(f"Initial Counterparty Status: {case.initial_counterparty_status}")
        print(f"Current Counterparty Status: {case.current_counterparty_status}")
        print(f"Risk Flag: {case.risk_flag}")
        print(f"Counterparty Risk State Changed: {counterparty_risk_state_changed(case)}")

    if case.initial_delegation_status:
        print(f"Initial Delegation Status: {case.initial_delegation_status}")
        print(f"Current Delegation Status: {case.current_delegation_status}")
        print(f"Delegation Revoked: {delegation_revoked(case)}")

    if case.authorized_actor:
        print(f"Authorized Actor: {case.authorized_actor}")
        print(f"Current Actor: {case.current_actor}")
        print(f"Identity Continuity Failed: {identity_continuity_failed(case)}")

    print(f"Violations: {result.violations}")
    print(f"Admissibility: {result.admissibility}")
    print(f"Execution Result: {result.execution_result}")
    print(f"Failure Prevented: {result.failure_prevented}")


def print_metrics(results: list[EvaluationResult]) -> None:
    metrics = generate_metrics(results)

    print("=== METRICS ===")
    print(f"Total Demonstrations: {metrics['total_demonstrations']}")
    print(f"Total Prevented Failures: {metrics['total_prevented_failures']}")

    prevention_rate = (
        metrics["total_prevented_failures"]
        / metrics["total_demonstrations"]
        * 100
    )

    print(f"Prevention Rate: {prevention_rate:.0f}%")
    print()
    print("Rule Hits:")

    for rule_name, count in metrics["rule_hits"].items():
        print(f"- {rule_name}: {count}")

    print()
    print("Category Hits:")

    for category_name, count in metrics["category_hits"].items():
        print(f"- {category_name}: {count}")


def main() -> None:
    cases = [
        "cases/EP-001_VENDOR_BLACKLIST.json",
        "cases/EP-002_AGENT_ACTION_DRIFT.json",
        "cases/EP-003_HEALTHCARE_AUTHORIZATION_EXPIRY.json",
        "cases/EP-004_FINANCIAL_SETTLEMENT_STATE_CHANGE.json",
        "cases/EP-005_COMPOUND_FAILURE.json",
        "cases/EP-006_DELEGATION_REVOCATION.json",
        "cases/EP-007_IDENTITY_CONTINUITY_FAILURE.json",
    ]

    results = []

    for index, case_path in enumerate(cases):
        case = load_case(case_path)
        result = evaluate_case(case)
        results.append(result)
        print_result(case, result)

        if index < len(cases) - 1:
            print()

    print()
    print_metrics(results)


if __name__ == "__main__":
    main()