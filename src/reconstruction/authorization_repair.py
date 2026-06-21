def repair_authorization(state, violations):

    return {
        "status": "RESTORED" if "delegation_revoked" in violations else "UNCHANGED",
        "authority_chain": [
            "root_authority",
            "governance_layer",
            "execution_agent"
        ]
    }