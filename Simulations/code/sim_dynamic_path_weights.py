"""Toy simulation for dynamic path weights from semantic action."""

from __future__ import annotations

import csv
from pathlib import Path

from src.ciel_foundations.solvers.dynamic_path_weights_solver import effective_white_thread_from_actions, path_action, softmax_weights


def write_csv(path: str | Path) -> None:
    actions = [
        path_action(1.0, 0.1, 0.2, 0.3),
        path_action(1.4, 0.4, 0.5, 0.6),
        path_action(0.8, 0.6, 0.4, 0.2),
    ]
    weights = softmax_weights(actions, sigma=1.5)
    primitives = [1.0 + 0.0j, 0.2 + 0.6j, 0.5 + 0.2j]
    weff = effective_white_thread_from_actions(primitives, actions, sigma=1.5)
    rows = [
        {"path": i, "action": actions[i], "weight": weights[i], "primitive_re": primitives[i].real, "primitive_im": primitives[i].imag}
        for i in range(len(actions))
    ]
    rows.append({"path": -1, "action": -1.0, "weight": -1.0, "primitive_re": weff.real, "primitive_im": weff.imag})
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["path", "action", "weight", "primitive_re", "primitive_im"])
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    output = Path("Simulations/results/ART-0006-dynamic-path-weights-demo.csv")
    output.parent.mkdir(parents=True, exist_ok=True)
    write_csv(output)
