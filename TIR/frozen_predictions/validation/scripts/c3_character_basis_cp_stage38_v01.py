#!/usr/bin/env python3
"""Stage 38 — C3 character-basis family CP audit.

Pure mathematical gate using only the previously frozen ordered three-family
cycle and a nondegenerate family-axis operator.  The unitary discrete Fourier
matrix F3 is the character basis that diagonalizes the C3 permutation cycle.
No CKM angles, observed masses, or fitted coefficients are used.
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


def main() -> None:
    omega = np.exp(2j * math.pi / 3.0)
    P3 = np.array(
        [
            [0.0, 0.0, 1.0],
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
        ],
        dtype=complex,
    )
    F3 = np.array(
        [
            [1.0, 1.0, 1.0],
            [1.0, omega, omega**2],
            [1.0, omega**2, omega],
        ],
        dtype=complex,
    ) / math.sqrt(3.0)

    # Character-basis diagonalization of the frozen C3 label cycle.
    D_cycle = F3.conj().T @ P3 @ F3
    expected_cycle_eigs = np.diag([1.0, omega**2, omega])
    cycle_diag_residual = float(np.max(np.abs(D_cycle - expected_cycle_eigs)))

    # A nondegenerate frozen family-axis representative.  Only the ordering and
    # nondegeneracy matter for the relative basis transformation.
    K = np.diag([3.0, 4.0, 5.0])
    H_ordered = K
    H_character = F3 @ K @ F3.conj().T
    hermitian_residual = float(np.max(np.abs(H_character - H_character.conj().T)))
    commutator = H_ordered @ H_character - H_character @ H_ordered
    commutator_max = float(np.max(np.abs(commutator)))

    unitary_residual = float(np.max(np.abs(F3.conj().T @ F3 - np.eye(3))))
    determinant_modulus_residual = float(abs(abs(np.linalg.det(F3)) - 1.0))
    J = jarlskog(F3)
    J_exact = 1.0 / (6.0 * math.sqrt(3.0))
    J_exact_residual = float(abs(J - J_exact))

    # Rephasing-invariant quartet phases for the relative unitary.
    quartet = F3[0, 0] * F3[1, 1] * np.conj(F3[0, 1]) * np.conj(F3[1, 0])
    quartet_phase = float(np.angle(quartet))

    passed = all(
        [
            cycle_diag_residual < 1e-12,
            hermitian_residual < 1e-12,
            commutator_max > 1e-9,
            unitary_residual < 1e-12,
            determinant_modulus_residual < 1e-12,
            abs(J) > 1e-9,
            J_exact_residual < 1e-12,
            abs(quartet_phase) > 1e-9,
        ]
    )

    receipt = {
        "schema": "TIR_POLYGONAL_STAGE38_C3_CHARACTER_BASIS_CP_V0_1",
        "status": "STAGE_38_C3_CHARACTER_BASIS_CP_MATH_PASS" if passed else "STAGE_38_FAIL",
        "cycle_diagonalization_residual": cycle_diag_residual,
        "hermiticity_residual": hermitian_residual,
        "commutator_max_abs": commutator_max,
        "unitarity_residual_F3": unitary_residual,
        "determinant_modulus_residual_F3": determinant_modulus_residual,
        "J_F3": J,
        "J_exact": J_exact,
        "J_exact_residual": J_exact_residual,
        "quartet_phase_rad": quartet_phase,
        "abs_F3": np.abs(F3).tolist(),
        "uses_observed_CKM": False,
        "uses_observed_masses": False,
        "uses_fitted_coefficients": False,
        "physical_sector_assignment_status": "OPEN",
        "pass": passed,
    }

    path = OUT / "TIR_POLYGONAL_STAGE38_C3_CHARACTER_BASIS_CP_RECEIPT_V0_1.json"
    path.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    print(json.dumps(receipt, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
