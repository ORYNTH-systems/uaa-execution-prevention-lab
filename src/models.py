class ExecutionCase:
    def __init__(self, **data):
        self._data = data

    def __getattr__(self, name):
        return self._data.get(name, "")

    def get(self, name, default=None):
        return self._data.get(name, default)


class EvaluationResult:
    def __init__(
        self,
        case_id,
        authorization_valid,
        reconciliation_required,
        admissibility,
        execution_result,
        failure_prevented,
        violations,
        state_snapshot=None
    ):
        self.case_id = case_id
        self.authorization_valid = authorization_valid
        self.reconciliation_required = reconciliation_required
        self.admissibility = admissibility
        self.execution_result = execution_result
        self.failure_prevented = failure_prevented
        self.violations = violations
        self.state_snapshot = state_snapshot or {}
