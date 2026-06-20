from collections import Counter


def generate_metrics(results):
    metrics = {
        "total_demonstrations": len(results),
        "total_prevented_failures": 0,
        "rule_hits": Counter(),
    }

    for result in results:
        if result.failure_prevented:
            metrics["total_prevented_failures"] += 1

        for violation in result.violations:
            metrics["rule_hits"][violation] += 1

    return metrics