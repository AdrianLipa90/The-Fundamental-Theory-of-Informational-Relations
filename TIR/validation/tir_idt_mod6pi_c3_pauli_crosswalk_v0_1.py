#!/usr/bin/env python3
"""TIR/IDT representation crosswalk for the periodic 6pi triad.

This validator is deliberately representation-level only.  It checks that the
C3 shift obtained from the periodic three-frame quotient admits both:

1. the F3 character basis already used by the TIR family-space branch; and
2. an SU(2)-adjoint realization that cyclically permutes the Pauli basis of
   Herm_0(2).

No physical identification of temporal, spatial, or flavour sectors is made.
"""
from __future__ import annotations

import json
import math

import numpy as np


TOL = 1.0e-12


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

    sx = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    sy = np.array([[0.0, -1j], [1j, 0.0]], dtype=complex)
    sz = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
    pauli = (sx, sy, sz)

    n_sigma = (sx + sy + sz) / math.sqrt(3.0)
    U3 = (
        math.cos(math.pi / 3.0) * np.eye(2, dtype=complex)
        - 1j * math.sin(math.pi / 3.0) * n_sigma
    )

    gram = np.array(
        [[0.5 * np.trace(a @ b) for b in pauli] for a in pauli],
        dtype=complex,
    )
    f3_diag = F3.conj().T @ P3 @ F3
    target_diag = np.diag([1.0, omega**2, omega])

    cycle_residual = max(
        float(np.max(np.abs(U3 @ pauli[j] @ U3.conj().T - pauli[(j + 1) % 3])))
        for j in range(3)
    )

    checks = {
        "c3_shift_order_three": bool(
            np.allclose(np.linalg.matrix_power(P3, 3), np.eye(3), atol=TOL)
        ),
        "f3_unitary": bool(np.allclose(F3.conj().T @ F3, np.eye(3), atol=TOL)),
        "f3_character_diagonalization": bool(
            np.allclose(f3_diag, target_diag, atol=TOL)
        ),
        "pauli_hs_orthonormal": bool(
            np.allclose(gram, np.eye(3), atol=TOL)
        ),
        "u3_special_unitary": bool(
            np.allclose(U3.conj().T @ U3, np.eye(2), atol=TOL)
            and abs(np.linalg.det(U3) - 1.0) < TOL
        ),
        "pauli_c3_equivariance": cycle_residual < TOL,
        "spinorial_cube_minus_identity": bool(
            np.allclose(np.linalg.matrix_power(U3, 3), -np.eye(2), atol=TOL)
        ),
        "spinorial_sixth_power_identity": bool(
            np.allclose(np.linalg.matrix_power(U3, 6), np.eye(2), atol=TOL)
        ),
    }

    passed = all(checks.values())
    payload = {
        "schema": "TIR_IDT_MOD6PI_C3_PAULI_CROSSWALK_V0_1",
        "technical_status": "PASS" if passed else "FAIL",
        "representation_status": (
            "C3_CHARACTER_AND_PAULI_EQUIVARIANT_CROSSWALK_CLOSED"
            if passed
            else "CROSSWALK_FAILED"
        ),
        "physical_sector_binding": "OPEN",
        "idt_parent": "02JN periodic P4 endpoint quotient at N=3",
        "tir_pauli_parent": "TIR_RELATIONAL_GENERATOR_SPACE_V0_1",
        "tir_c3_parent": "TIR_POLYGONAL_STAGE38_C3_CHARACTER_BASIS_CP_V0_1",
        "checks": checks,
        "cycle_residual": cycle_residual,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
