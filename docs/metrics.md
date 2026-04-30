# Metrics

AlphaPath uses multiple metric families distributed across the evaluation stack.
This document provides public-facing descriptions. The full implementation is maintained
in the private AlphaPath core repository.

---

## Structural Metrics

Computed from the PCU dependency graph.

| Metric | Description |
|---|---|
| Progression fragility | Sensitivity of the curriculum to bottleneck nodes |
| Downstream blockage | Fraction of the curriculum reachable through critical gateways |
| Path redundancy | Availability of alternative progression paths between stages |
| Frontier openness | Number of unlockable units at each stage of progression |
| Early lock-in burden | Degree to which early stages over-constrain later progression |
| Terminal closure fragility | Risk of late-stage blockage near terminal qualification |

---

## Packaging Metrics

Computed after institutional translation.

| Metric | Description |
|---|---|
| Synchronisation burden | Coordination cost imposed by packaging on co-requisite units |
| Translation distortion | Divergence between PCU graph structure and packaged form |
| Reintroduced bottleneck index | Bottlenecks created or amplified by the packaging process |
| Operational granularity cost | Institutional cost of fine-grained PCU delivery |
| Assessment observability | Degree to which outcomes remain observable after packaging |

---

## Uncertainty-Aware Metrics

Computed during simulation- and uncertainty-aware evaluation.

| Metric | Description |
|---|---|
| Transition support coverage | Fraction of student trajectory types with adequate structural support |
| Extrapolation risk | Confidence level on claims beyond the evaluated candidate distribution |
| Confidence-adjusted return | Expected metric value weighted by estimation confidence |
| Winner stability | Robustness of the top-ranked candidate across perturbation scenarios |

---

## Notes

- All metrics are computed relative to the canonical domain representation (PCU ontology
  and relations) for the relevant experiment.
- Baseline metrics are computed for the 2005 Civil Engineering curriculum and used as a
  reference throughout the campaign series.
- Metric specifications are documented in detail in the private core repository
  (AlphaPath Evaluation Stack v2 Technical Notes).
