# Relation to STRUCTURA

STRUCTURA is a complementary diagnostic framework focused on early-stage structural
constraint analysis within curriculum architectures.

---

## Conceptual Relationship

STRUCTURA provides the foundational blockage analysis that motivates the AlphaPath
search-based redesign approach.

| STRUCTURA | AlphaPath |
|---|---|
| Diagnoses structural constraint in an existing curriculum | Searches for architectures that escape that constraint |
| Identifies where and why blockage occurs | Evaluates whether candidate redesigns resolve it |
| Produces forensic analysis of a specific curriculum | Produces comparative evaluation across candidates |
| Answers: what is wrong? | Answers: can it be fixed, and how? |

---

## The Forensic Floor

A key contribution of the STRUCTURA analysis is the concept of the **forensic floor**:
the minimum structural constraint that the existing curriculum imposes, below which
no redesign can reach without architectural-level intervention.

The forensic floor concept is developed in the manuscript series and illustrated in
[Fig. 1](../figures/manuscript_figures/Fig_1_Forensic_Floor.png).

---

## Sequence

In the AlphaPath research programme, STRUCTURA analysis precedes AlphaPath evaluation:

1. STRUCTURA diagnoses the structural constraint in the 2005 curriculum.
2. AlphaPath searches for candidate architectures that might resolve or reduce it.
3. The campaign series evaluates whether and to what extent viable alternatives exist.

---

## Public Status

The STRUCTURA analysis is described in:

- Paz, H. R. (2026). *AlphaPath. Toward a Search-Based Architecture for Professional
  Knowledge Navigation (v1.0.0).* Zenodo.
  https://doi.org/10.5281/zenodo.19552912

The full STRUCTURA implementation is maintained in the private AlphaPath core repository.
