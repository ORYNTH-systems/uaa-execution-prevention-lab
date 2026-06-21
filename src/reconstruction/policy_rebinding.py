def rebind_policy(state, violations):

    if "policy_change_detected" in violations:
        return {
            "policy_state": "REBOUND",
            "active_version": state.get("policy_version")
        }

    return {
        "policy_state": "UNCHANGED",
        "active_version": state.get("policy_version")
    }