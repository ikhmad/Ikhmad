# Evacuation Overview

IKHMAD's evacuation layer is intended to evaluate more than shortest-path distance.

At a high level, future versions may consider:
- current incident/hazard information;
- predicted changes in hazard conditions;
- travel time;
- road accessibility;
- safe-zone availability;
- operational closures;
- uncertainty in source information;
- changing conditions during evacuation.

## Public abstraction

```text
Hazard Information
        |
        v
Route / Destination Evaluation
        |
        v
Candidate Safe Route
        |
        v
Continuous Reassessment
```

The detailed predictive algorithm, confidence propagation, road-safety scoring, safe-zone scoring and rerouting thresholds are confidential / proprietary and are not disclosed here.
