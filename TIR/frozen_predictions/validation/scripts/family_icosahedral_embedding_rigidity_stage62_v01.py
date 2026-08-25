#!/usr/bin/env python3
"""Stage 62 — rigidity of the C3-compatible family/icosahedral embedding.

Checks that preserving the frozen P3 cycle and the D0 diagonal sector reduces
SO(3) orientation freedom to {I,P3,P3^2}, and that preserving the exact labelled
A_seed channel leaves only the identity.
"""
from __future__ import annotations

import itertools
import json
import math
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results"
OUT.mkdir(parents=True, exist_ok=True)
TOL = 1e-10


def main() -> None:
    P3 = np.array(
        [
            [0.0, 0.0, 1.0],
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
        ]
    )
    n = np.array([1.0, 1.0, 1.0]) / math.sqrt(3.0)

    D = np.diag([-1.0 / 3.0, 0.0, 1.0 / math.sqrt(5.0)])
    D0 = D - np.trace(D) / 3.0 * np.eye(3)
    eigenvalues = np.linalg.eigvalsh(D0)
    minimum_eigenvalue_gap = min(
        abs(float(eigenvalues[i] - eigenvalues[j]))
        for i in range(3)
        for j in range(i + 1, 3)
    )

    solutions: list[np.ndarray] = []
    for perm in itertools.permutations(range(3)):
        P = np.zeros((3, 3))
        for column, row in enumerate(perm):
            P[row, column] = 1.0
        for signs in itertools.product((-1.0, 1.0), repeat=3):
            R = P @ np.diag(signs)
            if abs(float(np.linalg.det(R)) - 1.0) > TOL:
                continue
            if np.max(np.abs(R @ n - n)) > TOL:
                continue
            solutions.append(R)

    expected = [np.eye(3), P3, np.linalg.matrix_power(P3, 2)]

    def matrix_in_set(M: np.ndarray, collection: list[np.ndarray]) -> bool:
        return any(np.max(np.abs(M - X)) < TOL for X in collection)

    solution_set_matches = (
        len(solutions) == 3
        and all(matrix_in_set(M, expected) for M in solutions)
        and all(matrix_in_set(M, solutions) for M in expected)
    )

    # All three discrete solutions keep D0 inside the diagonal sector.
    diagonal_residuals = []
    for R in expected:
        transformed = R.T @ D0 @ R
        offdiag = transformed - np.diag(np.diag(transformed))
        diagonal_residuals.append(float(np.max(np.abs(offdiag))))

    E12 = np.zeros((3, 3))
    E12[0, 1] = E12[1, 0] = 1.0
    Aseed = 0.5 * E12
    Aseed_residuals = []
    for R in expected:
        Aseed_residuals.append(float(np.max(np.abs(R @ Aseed @ R.T - Aseed))))

    exact_label_preservers = sum(residual < TOL for residual in Aseed_residuals)

    # Verify the three solutions commute with P3 and fix the cycle axis.
    commutator_residual = max(
        float(np.max(np.abs(R @ P3 - P3 @ R))) for R in expected
    )
    axis_residual = max(float(np.max(np.abs(R @ n - n))) for R in expected)

    passed = (
        minimum_eigenvalue_gap > 1e-6
        and solution_set_matches
        and max(diagonal_residuals) < TOL
        and exact_label_preservers == 1
        and Aseed_residuals[0] < TOL
        and Aseed_residuals[1] > 0.1
        and Aseed_residuals[2] > 0.1
        and commutator_residual < TOL
        and axis_residual < TOL
    )

    receipt = {
        "schema": "TIR_POLYGONAL_STAGE62_FAMILY_ICOSAHEDRAL_EMBEDDING_RIGIDITY_RECEIPT_V0_1",
        "status": (
            "STAGE_62_FAMILY_ICOSAHEDRAL_EMBEDDING_RIGIDITY_PASS"
            if passed
            else "STAGE_62_FAIL"
        ),
        "D0_eigenvalues": [float(x) for x in eigenvalues],
        "D0_minimum_eigenvalue_gap": minimum_eigenvalue_gap,
        "orientation_preserving_signed_permutations_fixing_cycle_axis": len(solutions),
        "solution_set": ["I", "P3", "P3^2"] if solution_set_matches else "unexpected",
        "max_solution_P3_commutator_residual": commutator_residual,
        "max_solution_cycle_axis_residual": axis_residual,
        "D0_diagonal_sector_residuals": diagonal_residuals,
        "Aseed_exact_label_residuals_for_I_P3_P3sq": Aseed_residuals,
        "exact_Aseed_label_preserver_count": exact_label_preservers,
        "result": "Preserving P3 and the D0 diagonal sector removes the continuous SO(3) orientation freedom down to C3={I,P3,P3^2}; holding the fixed Stage41 A_seed label removes the residual cyclic relabelling.",
        "uses_observed_CKM": False,
        "uses_observed_masses": False,
        "uses_fitted_coefficients": False,
        "pass": passed,
    }

    path = OUT / "TIR_POLYGONAL_STAGE62_FAMILY_ICOSAHEDRAL_EMBEDDING_RIGIDITY_RECEIPT_V0_1.json"
    path.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    print(json.dumps(receipt, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
