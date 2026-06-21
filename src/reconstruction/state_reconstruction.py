def reconstruct_state(state, violations):

    corrected = dict(state)

    if "vendor_state_changed" in violations:
        corrected["vendor_status"] = "APPROVED"

    if "authorization_expired" in violations:
        corrected["authorization"] = "REVALIDATED"

    if "counterparty_risk_state_changed" in violations:
        corrected["counterparty_status"] = "LOW_RISK"

    if "resource_constraint_violated" in violations:
        corrected["resource_required"] = corrected.get("resource_limit")

    if "policy_change_detected" in violations:
        corrected["policy_version"] = "RECONCILED"

    if "delegation_revoked" in violations:
        corrected["delegation_status"] = "RESTORED"

    if "identity_continuity_failed" in violations:
        corrected["authorized_actor"] = "SYSTEM_REBOUND"

    if "intent_drift_detected" in violations:
        corrected["current_action"] = corrected.get("authorized_intent")

    return corrected
