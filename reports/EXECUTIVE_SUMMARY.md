## Additional Reviewer Resources

The repository includes supplemental materials to support independent review and reproducibility.

### Evidence Library

Provides a complete catalog of all demonstrations, metrics, rule hits, category hits, and evidence coverage.

### Real World Mappings

Maps each execution-prevention demonstration to a representative real-world failure scenario.

### Structured JSON Evidence

Each demonstration generates a machine-readable evidence artifact containing:

* Case identifier
* Admissibility result
* Execution result
* Failure-prevention status
* Triggered violations

### Replay Support

Reviewers can reproduce results using:

```powershell
python src\main.py --all
```

or execute individual demonstrations:

```powershell
python src\main.py --case EP-004
```

### Technical Summary

Provides a concise overview of doctrine, implementation, evidence generation, and demonstrated outcomes.
