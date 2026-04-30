# Evaluation Stack

AlphaPath evaluates curriculum candidates through a staged evaluation stack.
Each stage applies progressively more demanding criteria.
A candidate that fails any stage does not proceed to subsequent stages.

---

## Stage 1 — Structural Screening

**Question:** Is this candidate structurally plausible?

Evaluates graph-level properties:

- progression fragility;
- downstream blockage concentration;
- redundancy and alternative path availability;
- frontier openness;
- early lock-in burden;
- terminal closure fragility.

A candidate passes structural screening if it clears minimum thresholds on these metrics.
Candidates with critical structural defects are eliminated.

---

## Stage 2 — Institutional Translation

**Question:** Can this candidate be delivered in an institutional context?

Tests whether the candidate PCU graph can be translated into a valid institutional
curriculum form under:

- subject packaging constraints;
- simultaneity rules;
- coordination and dependency constraints;
- operational granularity limits.

Institutional translation is a hard feasibility filter. A structurally excellent
candidate that cannot be delivered institutionally is not viable.

---

## Stage 3 — Packaging-Aware Evaluation

**Question:** How much does institutional translation distort the structural design?

Assesses:

- synchronisation burden;
- cross-cluster coordination cost;
- translation distortion (structural intent preserved vs. lost in packaging);
- reintroduced bottleneck risk;
- assessment observability.

---

## Stage 4 — Simulation- and Uncertainty-Aware Evaluation

**Question:** How does this candidate perform under uncertainty?

Evaluates:

- transition support coverage (breadth of student paths supported);
- extrapolation risk (confidence in out-of-sample claims);
- confidence-adjusted return;
- winner stability under perturbation.

---

## Stage 5 — Claim Discipline

**Question:** What can we actually claim about this candidate?

Distinguishes:

- conditional leadership (leads under specific conditions);
- robust superiority (leads consistently across conditions);
- inconclusive comparison (insufficient evidence for strong claims).

AlphaPath enforces explicit claim categorisation at the point of reporting.
The claim strength must match the evidence strength.

---

## Design Principle

The stack is deliberately conservative. It is easier to construct a candidate that
looks good structurally than one that survives the full evaluation pipeline. The
stack is designed to surface the difficulty of genuine curriculum redesign, not to
produce optimistic rankings from incomplete analysis.
