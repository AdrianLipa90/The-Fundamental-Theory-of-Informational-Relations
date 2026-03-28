"""Toy simulation for object-state energy normalization."""

from __future__ import annotations

import csv
from pathlib import Path

from src.ciel_foundations.solvers.object_state_energy_solver import (
    amplitudes_from_normalized_energy,
    local_states,
    normalize_energies,
    phase_from_seed_text,
)


def write_csv(path: str | Path) -> None:
    ids = ["obj_1", "obj_2", "obj_3"]
    raw = [2.0, 3.0, 5.0]
    norm = normalize_energies(raw)
    amps = amplitudes_from_normalized_energy(norm)
    phases = [phase_from_seed_text(f"toy-seed-{k}") for k in range(1, 4)]
    psi = local_states(amps, phases)
    rows = []
    for i, obj_id in enumerate(ids):
        rows.append({
            "id": obj_id,
            "raw_energy": raw[i],
            "norm_energy": float(norm[i]),
            "amplitude": float(amps[i]),
            "phase": float(phases[i]),
            "state_re": float(psi[i].real),
            "state_im": float(psi[i].imag),
        })
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "raw_energy", "norm_energy", "amplitude", "phase", "state_re", "state_im"])
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    output = Path("Simulations/results/ART-0009-object-state-energy-demo.csv")
    output.parent.mkdir(parents=True, exist_ok=True)
    write_csv(output)
