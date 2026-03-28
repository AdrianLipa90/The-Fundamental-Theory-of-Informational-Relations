"""Toy simulation for semantic action measurement operators."""

from __future__ import annotations

import csv
from pathlib import Path

from src.ciel_foundations.solvers.semantic_action_measurement_solver import (
    closure_defect_cost,
    phase_cost_discrete,
    semantic_action_full,
    semantic_action_online,
    semantic_length_discrete,
    truth_audit_cost,
    truth_structural_cost,
)


def write_csv(path: str | Path) -> None:
    L = semantic_length_discrete([1.0, 0.5, 0.8], [1.0, 1.5, 0.7])
    P = phase_cost_discrete([0.0, 0.3, 0.1, 0.4])
    D = closure_defect_cost([[0.0, 0.0], [0.0, 2.09439510239, 4.18879020479]])
    T_struct = truth_structural_cost([0.9, 0.8, 0.95])
    T_audit = truth_audit_cost(1, 0, 1, 0, 1, 20)
    online = semantic_action_online(L, P, D, T_struct, alpha=1.0, beta=1.0, kappa=1.0, mu=1.0)
    full = semantic_action_full(online, T_audit, nu=1.0)
    rows = [
        {"component": "L", "value": L},
        {"component": "Delta_phi", "value": P},
        {"component": "D_rel", "value": D},
        {"component": "Pi_truth_struct", "value": T_struct},
        {"component": "Pi_truth_audit", "value": T_audit},
        {"component": "S_online", "value": online},
        {"component": "S_full", "value": full},
    ]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["component", "value"])
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    output = Path("Simulations/results/ART-0007-semantic-action-measurement-demo.csv")
    output.parent.mkdir(parents=True, exist_ok=True)
    write_csv(output)
