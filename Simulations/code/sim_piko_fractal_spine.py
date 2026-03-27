"""Toy simulation for the consolidated piko-scale fractal foundations spine."""

from __future__ import annotations

import csv
from pathlib import Path

from src.ciel_foundations.solvers.piko_fractal_spine_solver import build_spine_snapshot, spine_consistency_score


def write_csv(path: str | Path) -> None:
    snap = build_spine_snapshot()
    score = spine_consistency_score(snap)
    rows = [
        {"component": "berry_phase", "value": snap["berry_phase"]},
        {"component": "closure_magnitude", "value": snap["closure_magnitude"]},
        {"component": "tetra_relative_phase_1", "value": snap["tetra_relative_phases"][0]},
        {"component": "tetra_relative_phase_2", "value": snap["tetra_relative_phases"][1]},
        {"component": "tetra_relative_phase_3", "value": snap["tetra_relative_phases"][2]},
        {"component": "local_order_parameter_re", "value": snap["local_order_parameter"][0]},
        {"component": "local_order_parameter_im", "value": snap["local_order_parameter"][1]},
        {"component": "nonlocal_vortex", "value": int(snap["nonlocal_vortex"])},
        {"component": "spine_consistency_score", "value": score},
    ]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["component", "value"])
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    output = Path("Simulations/results/ART-0003-piko-fractal-spine-demo.csv")
    output.parent.mkdir(parents=True, exist_ok=True)
    write_csv(output)
