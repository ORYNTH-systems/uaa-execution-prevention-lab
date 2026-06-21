from reconstruction.state_reconstruction import reconstruct_state
from reconstruction.authorization_repair import repair_authorization
from reconstruction.policy_rebinding import rebind_policy
from reconstruction.intent_reconciliation import reconcile_intent


class ReconstructionEngine:

    def reconstruct(self, result):

        violations = getattr(result, "violations", []) or []

        state = getattr(result, "state_snapshot", None) or getattr(result, "raw_state", None) or {}

        return {
            "reconstructed_state": reconstruct_state(state, violations),
            "authorization_repair": repair_authorization(state, violations),
            "policy_rebinding": rebind_policy(state, violations),
            "intent_reconciliation": reconcile_intent(state, violations),
            "source_violations": violations
        }
