"""
Toy evaluation pipeline demo.

This script illustrates the idea of staged scoring using synthetic values.
It is not the AlphaPath core evaluation engine.
"""

import json
from pathlib import Path


def toy_composite(item: dict) -> float:
    return round(
        0.4 * item["structural_score"]
        + 0.3 * item["packaging_score"]
        + 0.3 * item["uncertainty_score"],
        4,
    )


def main():
    path = Path(__file__).with_name("synthetic_candidates.json")
    candidates = json.loads(path.read_text(encoding="utf-8"))

    for item in candidates:
        item["toy_composite_score"] = toy_composite(item)

    ranked = sorted(
        candidates,
        key=lambda x: x["toy_composite_score"],
        reverse=True,
    )

    print("Toy ranking (composite = 0.4*structural + 0.3*packaging + 0.3*uncertainty):")
    print()
    for rank, item in enumerate(ranked, start=1):
        print(
            f"  {rank}. {item['candidate']:<22}"
            f"  composite={item['toy_composite_score']:.4f}"
            f"  (str={item['structural_score']:.2f},"
            f" pkg={item['packaging_score']:.2f},"
            f" unc={item['uncertainty_score']:.2f})"
        )

    print()
    print("Note: this composite is illustrative only.")
    print("AlphaPath uses a staged evaluation pipeline, not a single weighted sum.")


if __name__ == "__main__":
    main()
