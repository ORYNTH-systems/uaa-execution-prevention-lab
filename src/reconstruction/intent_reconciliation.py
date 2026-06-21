def reconcile_intent(state, violations):

    if "intent_drift_detected" in violations:
        return {
            "intent_state": "ALIGNED",
            "effective_intent": state.get("authorized_intent")
        }

    return {
        "intent_state": "UNCHANGED",
        "effective_intent": state.get("authorized_intent")
    }