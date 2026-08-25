#!/usr/bin/env python3
"""Stage 39 — frozen two-operator family candidate.

No CKM/PDG values are read.  The candidate uses only previously frozen
polygonal/McKay invariants:
  D = diag(c3,c4,c5)
  C = F3 D F3^dagger
  a = 2/7
  b = 2/9
and the lowest-order Hermitian family H(alpha)=D+alpha C.

Both sector assignments (a,b) and (b,a) are retained.  This script freezes
outputs before any numerical target comparison.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results"
OUT.mkdir(parents=True, exist_ok=True)


def jarlskog(V: np.ndarray) -> float:
    return float(np.imag(V[0, 0] * V[1, 1] * np.conj(V[0, 1]) * np.conj(V[1, 0])))


def su3_representative(V: np.ndarray) -> np.ndarray:
    return V * np.exp(-1j * np.angle(np.linalg.det(V)) / 3.0)


def solve(D: np.ndarray, alpha_u: float, alpha_d: float):
    omega = np.exp(2j * math.pi / 3.0)
    F3 = np.array(
        [[1.0, 1.0, 1.0], [1.0, omega, omega**2], [1.0, omega**2, omega]],
        dtype=complex,
    ) / math.sqrt(3.0)
    C = F3 @ D @ F3.conj().T
    H_u = D + alpha_u * C
    H_d = D + alpha_d * C
    eval_u, U_u = np.linalg.eigh(H_u)
    eval_d, U_d = np.linalg.eigh(H_d)
    V = su3_representative(U_u.conj().T @ U_d)
    comm = H_u @ H_d - H_d @ H_u
    return {
        "alpha_u": alpha_u,
        "alpha_d": alpha_d,
        "eigenvalues_u": [float(x) for x in eval_u],
        "eigenvalues_d": [float(x) for x in eval_d],
        "commutator_max_abs": float(np.max(np.abs(comm))),
        "unitarity_residual": float(np.max(np.abs(V.conj().T @ V - np.eye(3)))),
        "determinant_residual": float(abs(np.linalg.det(V) - 1.0)),
        "J_family": jarlskog(V),
        "abs_relative_matrix": np.abs(V).tolist(),
    }


def main() -> None:
    a = 2.0 / 7.0
    b = 2.0 / 9.0

    axes = {
        "primary_cN": np.diag([-1.0 / 3.0, 0.0, 1.0 / math.sqrt(5.0)]),
        "control_polygon_N": np.diag([3.0, 4.0, 5.0]),
        "control_ADE_node_count": np.diag([7.0, 8.0, 9.0]),
    }

    outputs = {}
    for name, D in axes.items():
        outputs[name] = {
            "u=a_d=b": solve(D, a, b),
            "u=b_d=a": solve(D, b, a),
        }

    primary = outputs["primary_cN"]["u=a_d=b"]
    passed = all(
        [
            primary["commutator_max_abs"] > 1e-9,
            primary["unitarity_residual"] < 1e-12,
            primary["determinant_residual"] < 1e-12,
            abs(primary["J_family"]) > 1e-9,
        ]
    )

    receipt = {
        "schema": "TIR_POLYGONAL_STAGE39_TWO_OPERATOR_FAMILY_CANDIDATE_V0_1",
        "status": "STAGE_39_STRUCTURAL_CANDIDATE_FROZEN" if passed else "STAGE_39_CANDIDATE_EXECUTION_FAIL",
        "candidate": "H(alpha)=D+alpha*F3*D*F3^dagger",
        "primary_axis": "D=diag(c3,c4,c5)",
        "c_values": [-1.0 / 3.0, 0.0, 1.0 / math.sqrt(5.0)],
        "endpoint_ratios": {"a": a, "b": b},
        "both_sector_assignments_retained": True,
        "target_data_loaded": False,
        "uses_observed_CKM": False,
        "uses_observed_masses": False,
        "uses_fitted_coefficients": False,
        "outputs": outputs,
        "candidate_execution_pass": passed,
        "predictive_status": "FROZEN_STRUCTURAL_CANDIDATE_POSTDICTION_CONTEXT",
    }
    path = OUT / "TIR_POLYGONAL_STAGE39_TWO_OPERATOR_FAMILY_CANDIDATE_RECEIPT_V0_1.json"
    path.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    print(json.dumps(receipt, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
