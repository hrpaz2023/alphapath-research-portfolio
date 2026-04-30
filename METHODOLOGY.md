# Methodology

AlphaPath evaluates curriculum architectures through a staged logic. This document
describes the methodological principles. The full implementation is maintained in the
private AlphaPath core repository.

---

## 1. Structural Representation

Curricula are represented as progression architectures, typically as directed acyclic
graphs where nodes correspond to Professional Competence Units (PCUs) and edges represent
formal prerequisite dependencies.

This representation makes structural properties of the curriculum explicit and measurable:
bottlenecks, redundancy, frontier openness, downstream blockage, and terminal closure
fragility.

---

## 2. Candidate Generation

Candidate architectures can be generated or modified under explicit constraints. These
candidates are not assumed viable merely because they are structurally plausible.

Generation respects domain-level constraints derived from the institutional context,
including load limits, simultaneity rules, and sequencing policies.

---

## 3. Structural Screening

Candidates are first evaluated through graph-level metrics that assess:

- progression fragility;
- bottleneck concentration;
- downstream blockage;
- path redundancy;
- frontier openness;
- terminal closure risk.

Only candidates that pass structural screening proceed to subsequent evaluation stages.

---

## 4. Institutional Translation

A structurally plausible candidate must survive translation into an institutionally
deliverable form. This includes:

- subject packaging and wrapper coherence;
- simultaneity and coordination constraints;
- translation distortion and reintroduced bottleneck risk;
- operational granularity cost.

Institutional translation is treated as a hard feasibility filter, not a preference.

---

## 5. Packaging-Aware Evaluation

Candidates that survive translation are evaluated for:

- synchronisation burden;
- cross-cluster coordination cost;
- packaging distortion relative to the PCU graph;
- assessment observability under institutional form.

---

## 6. Simulation- and Uncertainty-Aware Evaluation

Surviving candidates are compared using uncertainty-aware evaluation metrics that account
for the variability of outcomes across student populations and institutional parameters.

Key metrics include:

- transition support coverage;
- confidence-adjusted return;
- winner stability under perturbation.

---

## 7. Claim Discipline

AlphaPath distinguishes between apparent ranking leadership and robust evaluative
superiority.

A candidate may lead under one metric or in one scenario without supporting an overstrong
claim of dominance. The framework enforces explicit claim categorisation at the point of
reporting, requiring alignment between evidence strength and claim strength.

---

## Synthetic Example

A minimal synthetic illustration of the curriculum graph representation and toy scoring
pipeline is available in [examples/](examples/).

This illustration is intentionally simplified. It does not reproduce the private
AlphaPath core pipeline.
