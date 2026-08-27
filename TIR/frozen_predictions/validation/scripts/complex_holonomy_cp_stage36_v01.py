#!/usr/bin/env python3
"""Stage 36 — complex open-holonomy family CP mechanism audit.

Uses the archived v3.5 pre-CKM structural records only.  No observed CKM
entries, masses, PMNS entries, or fitted White-Thread values enter the
construction.

The pre-existing v3.5 record supplies, for each up/down family pair,
- oriented_open_holonomy_overlap = a_ij
- phase_gap_rad = phi_ij

The minimal complex lift is
    W_ij = a_ij * exp(i phi_ij)
with no additional coefficient.

Then
    H_u = W W^dagger
    H_d = W^dagger W
and the relative eigenbasis transformation is audited for unitarity,
non-commutation, non-removable plaquette phase, and non-zero Jarlskog-type
invariant.  Source quarantine is propagated separately from the mechanism
result.
"""
from __future__ import annotations

import csv
import json
import math
from itertools import combinations
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT.parents[2] / "archive" / "v7.9" / "full"
PAIRS = (
    ARCHIVE
    / "33_debt10_white_thread_open_holonomy_preckm_v3_5"
    / "results"
    / "white_thread_open_holonomy_pairs_v3_5.csv"
)
CHANNELS = (
    ARCHIVE
    / "32_debt9_projection_orientation_sector_basis_v3_4"
    / "results"
    / "sector_basis_orientation_channels_v3_4.csv"
)
OUT = ROOT / "results"
OUT.mkdir(parents=True, exist_ok=True)

UP = ("u", "c", "t")
DOWN = ("d", "s", "b")
TOL = 1e-12


def read_csv(path: Path):
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def jarlskog_like(V: np.ndarray) -> float:
    return float(np.imag(V[0, 0] * V[1, 1] * np.conj(V[0, 1]) * np.conj(V[1, 0])))


def main() -> None:
    pairs = read_csv(PAIRS)
    channels = read_csv(CHANNELS)
    by_pair = {(r["up_particle"], r["down_particle"]): r for r in pairs}

    W = np.zeros((3, 3), dtype=complex)
    provenance_ok = True
    for i, u in enumerate(UP):
        for j, d in enumerate(DOWN):
            row = by_pair[(u, d)]
            provenance_ok = provenance_ok and all(
                row[key] == "False"
                for key in (
                    "uses_observed_mass",
                    "uses_observed_CKM",
                    "uses_observed_PMNS",
                    "uses_old_tau",
                    "uses_fitted_white_thread_values",
                )
            )
            a = float(row["oriented_open_holonomy_overlap"])
            phi = float(row["phase_gap_rad"])
            W[i, j] = a * np.exp(1j * phi)

    H_u = W @ W.conj().T
    H_d = W.conj().T @ W
    herm_u = float(np.max(np.abs(H_u - H_u.conj().T)))
    herm_d = float(np.max(np.abs(H_d - H_d.conj().T)))
    comm = H_u @ H_d - H_d @ H_u
    comm_max = float(np.max(np.abs(comm)))

    eval_u, U_u = np.linalg.eigh(H_u)
    eval_d, U_d = np.linalg.eigh(H_d)
    V = U_u.conj().T @ U_d

    # Remove only the physically irrelevant global determinant phase so the
    # representative lies in SU(3); this does not alter |V_ij| or J.
    det_phase = float(np.angle(np.linalg.det(V)))
    V_su3 = V * np.exp(-1j * det_phase / 3.0)
    unitary_residual = float(np.max(np.abs(V_su3.conj().T @ V_su3 - np.eye(3))))
    determinant_residual = float(abs(np.linalg.det(V_su3) - 1.0))
    J = jarlskog_like(V_su3)

    plaquette_phases = []
    for i, j in combinations(range(3), 2):
        for k, l in combinations(range(3), 2):
            q = W[i, k] * W[j, l] * np.conj(W[i, l]) * np.conj(W[j, k])
            plaquette_phases.append(float(np.angle(q)))
    max_abs_plaquette_phase = max(abs(x) for x in plaquette_phases)

    source_status = {
        r["particle"]: r["source_status"]
        for r in channels
        if r["particle"] in set(UP + DOWN)
    }
    quarantined_sources = sorted(
        p for p, status in source_status.items() if "quarantined" in status
    )

    mechanism_pass = all(
        [
            provenance_ok,
            herm_u < TOL,
            herm_d < TOL,
            comm_max > 1e-9,
            unitary_residual < TOL,
            determinant_residual < TOL,
            abs(J) > 1e-9,
            max_abs_plaquette_phase > 1e-9,
        ]
    )

    receipt = {
        "schema": "TIR_POLYGONAL_STAGE36_COMPLEX_HOLONOMY_CP_V0_1",
        "status": (
            "STAGE_36_COMPLEX_HOLONOMY_CP_MECHANISM_PASS__SOURCE_PROMOTION_QUARANTINED"
            if mechanism_pass and quarantined_sources
            else "STAGE_36_COMPLEX_HOLONOMY_CP_MECHANISM_PASS"
            if mechanism_pass
            else "STAGE_36_FAIL"
        ),
        "construction": "W_ij = oriented_open_holonomy_overlap_ij * exp(i * phase_gap_rad_ij)",
        "uses_observed_CKM": False,
        "uses_observed_masses": False,
        "uses_observed_PMNS": False,
        "uses_fitted_white_thread_values": False,
        "hermiticity_residual_Hu": herm_u,
        "hermiticity_residual_Hd": herm_d,
        "commutator_max_abs": comm_max,
        "eigenvalues_Hu": [float(x) for x in eval_u],
        "eigenvalues_Hd": [float(x) for x in eval_d],
        "relative_unitarity_residual": unitary_residual,
        "relative_determinant_residual": determinant_residual,
        "J_family": J,
        "abs_relative_matrix": np.abs(V_su3).tolist(),
        "plaquette_phases_rad": plaquette_phases,
        "max_abs_plaquette_phase_rad": max_abs_plaquette_phase,
        "source_status": source_status,
        "quarantined_source_particles": quarantined_sources,
        "physical_promotion_allowed": len(quarantined_sources) == 0,
        "mechanism_pass": mechanism_pass,
    }

    path = OUT / "TIR_POLYGONAL_STAGE36_COMPLEX_HOLONOMY_CP_RECEIPT_V0_1.json"
    path.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    print(json.dumps(receipt, indent=2))
    if not mechanism_pass:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
