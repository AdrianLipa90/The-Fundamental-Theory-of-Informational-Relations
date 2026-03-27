"""Minimal CP1/Bloch Berry-spin demo simulation."""

from __future__ import annotations

import csv
import math
from pathlib import Path

from src.ciel_foundations.holonomy.berry import berry_connection_phi, berry_phase_latitude


def generate_rows(num_steps: int = 16):
    theta = math.pi / 2.0
    for k in range(num_steps + 1):
        phi = 2.0 * math.pi * k / num_steps
        a_phi = berry_connection_phi(theta)
        berry_phase = a_phi * phi
        yield {
            "step": k,
            "phi": phi,
            "theta": theta,
            "A_phi": a_phi,
            "berry_phase": berry_phase,
            "spinor_re": math.cos(berry_phase),
            "spinor_im": math.sin(berry_phase),
            "closure_abs_pair_0_phase": abs(1.0 + complex(math.cos(berry_phase), math.sin(berry_phase))),
        }


def write_csv(path: str | Path) -> None:
    rows = list(generate_rows())
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    output = Path("Simulations/results/ART-0001-cp1-berry-spin-demo.csv")
    output.parent.mkdir(parents=True, exist_ok=True)
    write_csv(output)
