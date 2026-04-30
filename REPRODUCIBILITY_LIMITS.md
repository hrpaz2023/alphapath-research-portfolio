# Reproducibility Limits

This public repository supports manuscript-level and conceptual reproducibility, not
full computational reproduction of the private AlphaPath core system.

---

## Publicly Available

- conceptual documentation;
- synthetic examples;
- selected non-sensitive figures;
- manuscript-to-campaign mappings;
- high-level metric descriptions;
- public references and citations.

---

## Not Publicly Released

- full source code;
- institutional datasets;
- student-level records;
- internal experiment configurations;
- full experiment bundles;
- unpublished manuscript drafts;
- sensitive outputs;
- private research notes.

---

## Rationale

The full system depends on institutional data, internal experimental pipelines, and
ongoing research assets that cannot be publicly released due to confidentiality,
intellectual property, and research-continuity constraints.

The public repository therefore provides a curated research portfolio rather than a
full executable reproduction package.

---

## Partial Reproducibility

The synthetic examples in [examples/](examples/) demonstrate the general logic of
curriculum graph representation and simplified staged evaluation. These examples use
only synthetic, non-sensitive data and do not depend on the private core pipeline.

To run them:

```bash
python -m venv .venv
# Windows:
.\.venv\Scripts\Activate.ps1
# Linux/macOS:
source .venv/bin/activate

pip install networkx

python examples/synthetic_curriculum_graph/toy_graph_demo.py
python examples/toy_evaluation_pipeline/toy_scoring_demo.py
```

---

## Public Research Outputs

Two preprints are publicly available and provide extensive methodological documentation:

- Paz, H. R. (2026). *AlphaPath. Toward a Search-Based Architecture for Professional
  Knowledge Navigation (v1.0.0).* Zenodo.
  https://doi.org/10.5281/zenodo.19552912

- Paz, H. R. (2026). *Toward a New Curricular Architecture for Civil Engineering in the
  Age of Artificial Intelligence.* Zenodo.
  https://doi.org/10.5281/zenodo.19591967
