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
Toy ranking:
1 cluster_first 0.7520
2 low_fragmentation 0.7260
3 baseline 0.5870
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
