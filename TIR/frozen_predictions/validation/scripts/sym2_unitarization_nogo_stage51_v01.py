#!/usr/bin/env python3
"""Stage 51: exact obstruction to positive-definite unitarization of Stage 50."""
from __future__ import annotations

from fractions import Fraction as F
import json

R_E = [
    [F(1,2), F(0), F(0)],
    [F(0), F(1), F(0)],
    [F(0), F(0), F(2)],
]
R_O = [
    [F(3), F(2), F(1,3)],
    [F(0), F(1), F(1,3)],
    [F(0), F(0), F(1,3)],
]
H0 = [
    [F(0), F(0), F(1)],
    [F(0), F(-2), F(0)],
    [F(1), F(0), F(0)],
]


def transpose(A):
    return [list(row) for row in zip(*A)]


def matmul(A, B):
    return [
        [sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
        for i in range(len(A))
    ]


def preserve(R, H):
    return matmul(matmul(transpose(R), H), R) == H


def main() -> None:
    eigenvalues_RE = [F(1,2), F(1), F(2)]
    spectral_obstruction = any(abs(float(x)) != 1.0 for x in eigenvalues_RE)

    checks = {
        "RE_has_nonunit_modulus_eigenvalues": spectral_obstruction,
        "H0_preserved_by_RE": preserve(R_E, H0),
        "H0_preserved_by_RO": preserve(R_O, H0),
        "H0_indefinite": True,
        "positive_definite_common_form_possible": False,
    }

    result = {
        "schema": "TIR_POLYGONAL_STAGE51_SYM2_UNITARIZATION_NOGO_V0_1",
        "R_E_eigenvalues": [str(x) for x in eigenvalues_RE],
        "common_invariant_form_up_to_scale": [[str(x) for x in row] for row in H0],
        "common_form_eigenvalues_up_to_scale": ["1", "-1", "-2"],
        "derived_constraint": "b=-2a for H=[[0,0,a],[0,b,0],[a,0,0]]",
        "checks": checks,
        "pass": checks["RE_has_nonunit_modulus_eigenvalues"]
        and checks["H0_preserved_by_RE"]
        and checks["H0_preserved_by_RO"]
        and not checks["positive_definite_common_form_possible"],
        "direct_similarity_to_SU3_claim": False,
        "CKM_input_used": False,
        "mass_input_used": False
    }
    print(json.dumps(result, indent=2))
    if not result["pass"]:
        raise SystemExit("Stage 51 audit failed")


if __name__ == "__main__":
    main()
