"""
Toy curriculum graph demo.

This script is intentionally simple and synthetic.
It does not reproduce the private AlphaPath core pipeline.
"""

from pathlib import Path
import csv
import networkx as nx


def load_edges(path: Path):
    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [(row["source"], row["target"]) for row in reader]


def downstream_footprint(graph: nx.DiGraph, node: str) -> int:
    return len(nx.descendants(graph, node))


def main():
    path = Path(__file__).with_name("synthetic_curriculum_edges.csv")
    edges = load_edges(path)

    graph = nx.DiGraph()
    graph.add_edges_from(edges)

    print("Nodes:", graph.number_of_nodes())
    print("Edges:", graph.number_of_edges())
    print("Is DAG:", nx.is_directed_acyclic_graph(graph))
    print()
    print("Topological order:")
    print(list(nx.topological_sort(graph)))
    print()
    print("Downstream footprint per node (descendants reachable):")
    for node in nx.topological_sort(graph):
        print(f"  {node}: {downstream_footprint(graph, node)}")


if __name__ == "__main__":
    main()
