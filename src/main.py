import argparse
import json
from pathlib import Path

from models import ExecutionCase, EvaluationResult
from admissibility import evaluate_admissibility, collect_violations
from metrics import generate_metrics
from reconstruction.engine import ReconstructionEngine


CASE_PATHS = sorted(str(path) for path in Path("cases").rglob("*.json"))


def load_case(path: str) -> ExecutionCase:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    initial_state = data.get("initial_state", {})
    state_change = data.get("state_change", {})
    execution_attempt = data.get("execution_attempt", {})

    return ExecutionCase(
        case_id=data.get("case_id", ""),
        title=data.get("title", ""),
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
        resource_limit=initial_state.get("resource_limit", 0),
        resource_required=state_change.get("resource_required", 0),
        policy_version=initial_state.get("policy_version", ""),
        current_policy_version=state_change.get("policy_version", ""),
    )


def resolve_case_id(case_id: str) -> str:
    for path in CASE_PATHS:
        if case_id in path:
            return path

    raise ValueError(f"Unknown case id: {case_id}")


def build_state_snapshot(case: ExecutionCase) -> dict:
    return {
        "vendor_status": case.initial_vendor_status,
        "authorization": case.authorization,
        "counterparty_status": case.initial_counterparty_status,
        "delegation_status": case.initial_delegation_status,
        "authorized_intent": case.authorized_intent,
        "current_action": case.current_action,
        "policy_version": case.policy_version,
        "resource_limit": case.resource_limit,
        "resource_required": case.resource_required,
    }


def evaluate_case(case: ExecutionCase) -> EvaluationResult:
    violations = collect_violations(case)
    admissibility = evaluate_admissibility(case)

    return EvaluationResult(
        case_id=case.case_id,
        authorization_valid=case.authorization == "VALID",
        reconciliation_required=True,
        admissibility=admissibility,
        execution_result="DECLINED" if not admissibility else "EXECUTED",
        failure_prevented=not admissibility,
        violations=violations,
        state_snapshot=build_state_snapshot(case),
    )


def print_case_output(case: ExecutionCase, result: EvaluationResult, reconstruction: dict) -> None:
    print(f"\nCase: {case.case_id} - {case.title}")
    print(f"Admissibility: {result.admissibility}")
    print(f"Execution Result: {result.execution_result}")
    print(f"Violations: {result.violations}")

    print("\n=== RECONSTRUCTION OUTPUT ===")
    print(reconstruction)

    before_state = result.state_snapshot
    after_state = reconstruction.get("reconstructed_state", {})

    delta = {
        k: {
            "before": before_state.get(k),
            "after": after_state.get(k),
        }
        for k in set(before_state) | set(after_state)
        if before_state.get(k) != after_state.get(k)
    }

    print("\n=== STATE DELTA ===")
    print(delta)


def print_aggregate_metrics(results: list[EvaluationResult]) -> None:
    metrics = generate_metrics(results)

    print("\n=== AGGREGATE METRICS ===")
    print(f"Total Demonstrations: {metrics['total_demonstrations']}")
    print(f"Total Prevented Failures: {metrics['total_prevented_failures']}")

    prevention_rate = (
        metrics["total_prevented_failures"]
        / metrics["total_demonstrations"]
        * 100
        if metrics["total_demonstrations"]
        else 0
    )

    print(f"Prevention Rate: {prevention_rate:.0f}%")
    print(f"Rule Hits: {metrics['rule_hits']}")
    print(f"Category Hits: {metrics['category_hits']}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--case", type=str, default=None)
    args = parser.parse_args()

    reconstructor = ReconstructionEngine()

    if args.case:
        case_paths = [resolve_case_id(args.case)]
    else:
        case_paths = CASE_PATHS

    results = []
    for case_path in case_paths:
        case = load_case(case_path)
        result = evaluate_case(case)
        reconstruction = reconstructor.reconstruct(result)

        print_case_output(case, result, reconstruction)
        results.append(result)

    print_aggregate_metrics(results)

    return results


if __name__ == "__main__":
    main()



