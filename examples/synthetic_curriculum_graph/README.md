# Synthetic Curriculum Graph Example

This example illustrates the general logic of curriculum graph representation used
in AlphaPath. It uses a small synthetic curriculum with 9 nodes and 8 edges.

This example is intentionally simplified. It does not reproduce the private AlphaPath
core pipeline, institutional data, or domain-specific PCU ontology.

---

## Files

| File | Description |
|---|---|
| `synthetic_curriculum_edges.csv` | Synthetic directed edges (source → target) |
| `toy_graph_demo.py` | Script to load and analyse the graph |

---

## Requirements

```
networkx>=3.0
```

Install with:

```bash
pip install networkx
```

---

## Usage

```bash
python toy_graph_demo.py
```

Expected output:

```
Nodes: 9
Edges: 8
Is DAG: True
Topological order:
['Mathematics I', 'Physics I', 'Mathematics II', 'Mechanics', 'Structures',
 'Hydraulics', 'Water Resources', 'Capstone Project']
```

---

## Notes

The synthetic graph represents a simplified curriculum with two early foundational
subjects feeding into a convergent capstone. It illustrates the directed acyclic graph
(DAG) structure used in AlphaPath but does not model the complexity of a real
curriculum or the full AlphaPath metric suite.
