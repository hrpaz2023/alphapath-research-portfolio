# Toy Evaluation Pipeline Example

This example illustrates the general logic of staged curriculum evaluation used in
AlphaPath. It uses synthetic candidate scores across three evaluation dimensions.

This example is intentionally simplified. It does not reproduce the private AlphaPath
core evaluation engine, institutional data, or full metric suite.

---

## Files

| File | Description |
|---|---|
| `synthetic_candidates.json` | Synthetic candidate scores (structural, packaging, uncertainty) |
| `toy_scoring_demo.py` | Script to compute toy composite scores and rank candidates |

---

## Requirements

No external dependencies beyond the Python standard library.

---

## Usage

```bash
python toy_scoring_demo.py
```

Expected output:

```text
Toy ranking (composite = 0.4*structural + 0.3*packaging + 0.3*uncertainty):

 1. cluster_first          composite=0.7520 (str=0.74, pkg=0.70, unc=0.82)
 2. low_fragmentation      composite=0.7260 (str=0.78, pkg=0.72, unc=0.66)
 3. baseline               composite=0.5870 (str=0.62, pkg=0.58, unc=0.55)

Note: this composite is illustrative only.
AlphaPath uses a staged evaluation pipeline, not a single weighted sum.
```

---

## Notes

The three synthetic candidates — `baseline`, `low_fragmentation`, and `cluster_first` —
illustrate different trade-off profiles:

- `baseline`: moderate scores across all dimensions;
- `low_fragmentation`: strong structural and packaging scores, moderate uncertainty;
- `cluster_first`: moderate structural and packaging, strong uncertainty performance.

In AlphaPath, these trade-offs are resolved through the full evaluation stack, not a
simple weighted composite. The toy composite used here is illustrative only.
