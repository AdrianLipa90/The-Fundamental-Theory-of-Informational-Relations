"""Toy simulation for the White-Thread U(1) holonomy primitive."""

from __future__ import annotations

import csv
from pathlib import Path

from src.ciel_foundations.solvers.white_thread_primitive_solver import u1_holonomy_phase, white_thread_matrix_element


def write_csv(path: str | Path) -> None:
    psi_i = [1.0 + 0j, 0.0 + 0j]
    psi_j = [0.6 + 0j, 0.8 + 0j]
    phase = u1_holonomy_phase([0.2, 0.3, -0.1])
    W = white_thread_matrix_element(psi_i, psi_j, phase)
    rows = [{"phase": phase, "W_re": W.real, "W_im": W.imag, "W_abs": abs(W)}]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["phase", "W_re", "W_im", "W_abs"])
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    output = Path("Simulations/results/ART-0005-white-thread-primitive-demo.csv")
    output.parent.mkdir(parents=True, exist_ok=True)
    write_csv(output)
