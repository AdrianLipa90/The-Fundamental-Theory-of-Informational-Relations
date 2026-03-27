"""Toy simulation for tau-from-coupling via a Laplacian generator."""

from __future__ import annotations

import csv
from pathlib import Path

from src.ciel_foundations.solvers.tau_from_coupling_solver import log_tau_from_coupling, strength_vector, tau_from_coupling


def write_csv(path: str | Path) -> None:
    A = [
        [0.0, 1.0, 0.2],
        [1.0, 0.0, 0.5],
        [0.2, 0.5, 0.0],
    ]
    d = strength_vector(A)
    dbar = sum(d) / len(d)
    xi = log_tau_from_coupling(A)
    taus = tau_from_coupling(A)
    rows = [
        {"i": i, "d_i": d[i], "d_bar": dbar, "xi_i": xi[i], "tau_i": taus[i]}
        for i in range(len(d))
    ]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["i", "d_i", "d_bar", "xi_i", "tau_i"])
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    output = Path("Simulations/results/ART-0004-tau-from-coupling-demo.csv")
    output.parent.mkdir(parents=True, exist_ok=True)
    write_csv(output)
