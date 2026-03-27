"""Toy simulation for a nonlocal holonomic vortex around a local attractor."""

from __future__ import annotations

import csv
from pathlib import Path

from src.ciel_foundations.solvers.nonlocal_holonomic_vortex_solver import coriolis_term, spacetime_circulation


def rows():
    displacements = [
        (0.0, 1.0, 0.0, 0.0),
        (1.0, 0.0, 0.0, 0.0),
        (0.0, -1.0, 0.0, 0.0),
        (-1.0, 0.0, 0.0, 0.0),
    ]
    u_forms = [
        (0.0, 1.0, 0.0, 0.0),
        (1.0, 0.0, 0.0, 0.0),
        (0.0, -1.0, 0.0, 0.0),
        (-1.0, 0.0, 0.0, 0.0),
    ]
    omega = (0.0, 0.0, 1.0)
    velocity = (1.0, 0.0, 0.0)
    cx, cy, cz = coriolis_term(omega, velocity)
    total = 0.0
    for k, (dx, u) in enumerate(zip(displacements, u_forms)):
        contrib = sum(a * b for a, b in zip(dx, u))
        total += contrib
        yield {
            "segment": k,
            "dt": dx[0],
            "dx": dx[1],
            "dy": dx[2],
            "dz": dx[3],
            "u_t": u[0],
            "u_x": u[1],
            "u_y": u[2],
            "u_z": u[3],
            "segment_contribution": contrib,
            "cumulative_circulation": total,
            "omega_x": omega[0],
            "omega_y": omega[1],
            "omega_z": omega[2],
            "coriolis_x": cx,
            "coriolis_y": cy,
            "coriolis_z": cz,
        }


def write_csv(path: str | Path) -> None:
    rs = list(rows())
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rs[0].keys()))
        writer.writeheader()
        writer.writerows(rs)


if __name__ == "__main__":
    output = Path("Simulations/results/ART-0002-nonlocal-holonomic-vortex-demo.csv")
    output.parent.mkdir(parents=True, exist_ok=True)
    write_csv(output)
