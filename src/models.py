from dataclasses import dataclass


@dataclass(frozen=True)
class ExecutionCase:
    case_id: str
    title: str
    authorization: str
    initial_vendor_status: str
    current_vendor_status: str
    execution_requested: bool
    authorized_intent: str = ""
    current_action: str = ""
    authorization_expiration: str = ""
    current_date: str = ""
    current_authorization_status: str = ""


@dataclass(frozen=True)
class EvaluationResult:
    case_id: str
    authorization_valid: bool
    reconciliation_required: bool
    admissibility: bool
    execution_result: str
    failure_prevented: bool
