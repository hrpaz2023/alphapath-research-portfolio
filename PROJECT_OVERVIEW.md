# Project Overview

AlphaPath is a research programme and computational framework for analysing and evaluating
curriculum architectures.

The project begins from a central premise: professional curricula should not be treated only
as administrative sequences of subjects. They can also be studied as structured architectures
that distribute progression, constraint, opportunity, and institutional friction.

AlphaPath combines:

- curriculum graph analysis;
- Professional Competence Unit (PCU) modelling;
- search-based architecture exploration;
- institutional packaging analysis;
- simulation-aware evaluation;
- uncertainty-aware ranking;
- manuscript-level traceability.

---

## Empirical Context

The framework was developed in the context of Civil Engineering education, with the 2005
Civil Engineering curriculum at FACET-UNT (Faculty of Exact Sciences and Technology,
National University of Tucumán, Argentina) as an initial empirical anchor.

Its longer-term goal is broader: to support the analysis and redesign of professional
curricula across domains.

---

## Key Concepts

### Professional Competence Units (PCUs)

PCUs are the atomic representational units of AlphaPath. Rather than treating a curriculum
as a list of subjects, AlphaPath decomposes it into competence-centred building blocks that
can be structured, sequenced, and evaluated as an architectural system.

### Curriculum Architecture

A curriculum architecture is a structured arrangement of PCUs with explicit progression
dependencies, institutional constraints, and evaluation criteria. AlphaPath treats the
space of valid architectures as a searchable design space.

### The Evaluation Stack

AlphaPath does not evaluate curriculum candidates through a single metric. It applies a
staged evaluation logic that filters candidates through structural, institutional,
packaging, and uncertainty-aware criteria in sequence.

---

## Research Programme Structure

The AlphaPath research programme has produced:

- a framework paper introducing the search-based architecture concept;
- a domain-specific paper applying the framework to Civil Engineering in the AI era;
- a series of structural diagnosis papers analysing the 2005 Civil Engineering curriculum;
- a series of campaign-based evaluation papers comparing candidate architectures.

See [MANUSCRIPT_MAP.md](MANUSCRIPT_MAP.md) for the full map.

---

## Relation to CAPIRE

CAPIRE is the student trajectory simulation system that operates alongside AlphaPath.

Where AlphaPath evaluates curriculum architectures from a structural and institutional
perspective, CAPIRE models how student populations traverse those architectures over time,
introducing agent-based dynamics into the evaluation.

See [docs/relation_to_capire.md](docs/relation_to_capire.md) for a full description.

---

## Relation to STRUCTURA

STRUCTURA is a complementary diagnostic framework focused on early-stage structural
constraint analysis. It provides the foundational blockage analysis that motivates the
AlphaPath search-based redesign approach.

See [docs/relation_to_structura.md](docs/relation_to_structura.md) for a full description.
