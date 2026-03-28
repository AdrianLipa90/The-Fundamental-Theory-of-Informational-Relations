"""Toy simulation for spectral tau from effective White-Thread transport."""

from __future__ import annotations

import csv
from pathlib import Path

from src.ciel_foundations.solvers.spectral_tau_from_white_thread_solver import (
    build_symmetric_coupling_matrix,
    characteristic_coefficients_3x3_zero_diag,
    hermitian_projection_entry,
    spectral_tau_modes,
)


def write_csv(path: str | Path) -> None:
    w_eff = 0.74224129 + 0.12412309j
    a12 = hermitian_projection_entry(w_eff)
    a13 = 0.5
    a23 = 0.3
    A = build_symmetric_coupling_matrix(a12, a13, a23)
    s2, s3 = characteristic_coefficients_3x3_zero_diag(a12, a13, a23)
    tau = spectral_tau_modes(A)
    rows = [
        {"object": "A12", "value": a12},
        {"object": "A13", "value": a13},
        {"object": "A23", "value": a23},
        {"object": "poly_lambda", "value": s2},
        {"object": "poly_const", "value": s3},
        {"object": "tau_1", "value": tau[0]},
        {"object": "tau_2", "value": tau[1]},
        {"object": "tau_3", "value": tau[2]},
    ]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["object", "value"])
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    output = Path("Simulations/results/ART-0008-spectral-tau-from-white-thread-demo.csv")
    output.parent.mkdir(parents=True, exist_ok=True)
    write_csv(output)
