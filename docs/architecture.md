# AlphaPath Architecture

AlphaPath is organised around a separation between distinct architectural layers.
The full implementation is maintained in the private AlphaPath core repository.
This document describes the conceptual architecture.

---

## Layer 1 — Domain Representation

The domain layer encodes:

- a Professional Competence Unit (PCU) ontology;
- inter-PCU prerequisite relations;
- cluster and terminal profile assignments;
- institutional translation policy.

Domain representation is the source of truth for all downstream analysis. It is
maintained as structured YAML assets in the private core.

---

## Layer 2 — Curriculum Graph Structure

The graph layer builds a directed acyclic graph (DAG) from the PCU ontology and
relation set. This graph is the primary object of structural analysis.

Key graph properties analysed include:

- topological ordering;
- in-degree and out-degree distributions;
- reachability and downstream footprints;
- critical path identification;
- bottleneck and gateway detection.

---

## Layer 3 — Candidate Architecture Generation

The generation layer produces candidate architectures by modifying the PCU graph
under explicit structural and institutional constraints.

Generation strategies include:

- baseline-anchored perturbation;
- essentiality-driven simplification;
- ontology variant exploration.

---

## Layer 4 — Packaging and Institutional Translation

The translation layer converts structurally valid PCU graphs into institutionally
deliverable curriculum forms.

This involves:

- subject packaging (grouping PCUs into deliverable units);
- simultaneity and coordination constraint application;
- translation distortion assessment.

Institutional translation is a hard feasibility filter: structurally valid candidates
that cannot survive translation are eliminated from further evaluation.

---

## Layer 5 — Evaluation Metrics

The metrics layer computes multi-family evaluation metrics across structural, packaging,
and uncertainty-aware dimensions.

See [metrics.md](metrics.md) for public metric descriptions.

---

## Layer 6 — Uncertainty-Aware Comparison

The comparison layer applies confidence-adjusted ranking and winner stability analysis
to surviving candidates.

This layer enforces claim discipline: the strength of comparative claims must be
supported by the strength of available evidence.

---

## Layer 7 — Manuscript-Level Reporting

The reporting layer produces structured outputs with explicit traceability:

- run ID → experiment → campaign → metric → figure → manuscript claim.

All canonical run IDs are pinned in private registries maintained in the core
repository.
