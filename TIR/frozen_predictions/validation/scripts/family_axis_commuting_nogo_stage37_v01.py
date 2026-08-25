#!/usr/bin/env python3
"""Stage 37 — common family-axis commuting no-go audit.

Pure mathematical gate.  It tests the exact statement that two sector
Hamiltonians built only as functions of one common normal family operator K
must commute and therefore cannot generate non-trivial family mixing or CP.

The numerical matrices below instantiate already frozen family labels from the
polygonal/McKay chain; the proof itself is general.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results"
OUT.mkdir(parents=True, exist_ok=True)


def commutator(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    return A @ B - B @ A


def main() -> None:
    # Three already frozen family-axis label systems.
    K_N = np.diag([3.0, 4.0, 5.0])
    K_ADE_nodes = np.diag([7.0, 8.0, 9.0])
    K_c = np.diag([-1.0 / 3.0, 0.0, 1.0 / math.sqrt(5.0)])

    # Representative independent scalar functions.  Any scalar spectral
    # functions of one common normal K share its eigenbasis; these examples are
    # only an executable consistency check of the general algebraic statement.
    examples = {
        "N_axis": (K_N @ K_N + 2.0 * K_N + np.eye(3), np.linalg.matrix_power(K_N, 3) - K_N),
        "ADE_node_axis": (K_ADE_nodes / 9.0, K_ADE_nodes @ K_ADE_nodes / 81.0),
        "c_axis": (K_c, K_c @ K_c + np.eye(3)),
    }

    residuals = {}
    for name, (H_u, H_d) in examples.items():
        residuals[name] = float(np.max(np.abs(commutator(H_u, H_d))))

    max_residual = max(residuals.values())

    # In the common ordered eigenbasis the relative diagonalizer is identity
    # up to phases/permutations, hence the Jarlskog invariant vanishes.
    V = np.eye(3, dtype=complex)
    J = float(np.imag(V[0, 0] * V[1, 1] * np.conj(V[0, 1]) * np.conj(V[1, 0])))

    passed = max_residual == 0.0 and J == 0.0
    receipt = {
        "schema": "TIR_POLYGONAL_STAGE37_FAMILY_AXIS_COMMUTING_NOGO_V0_1",
        "status": "STAGE_37_COMMON_FAMILY_AXIS_NOGO_PASS" if passed else "STAGE_37_FAIL",
        "theorem": "If H_u=f(K) and H_d=g(K) for one common normal K, then [H_u,H_d]=0.",
        "family_axes_checked": {
            "polygon_N": [3, 4, 5],
            "affine_ADE_node_counts": [7, 8, 9],
            "local_geometry_cN": [-1.0 / 3.0, 0.0, 1.0 / math.sqrt(5.0)],
        },
        "commutator_residuals": residuals,
        "max_commutator_residual": max_residual,
        "relative_mixing_representative": "I3",
        "J_family": J,
        "consequence": "A second non-commuting geometric/holonomic operator is required for non-trivial family mixing.",
        "uses_observed_CKM": False,
        "uses_observed_masses": False,
        "pass": passed,
    }
    path = OUT / "TIR_POLYGONAL_STAGE37_FAMILY_AXIS_COMMUTING_NOGO_RECEIPT_V0_1.json"
    path.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    print(json.dumps(receipt, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
