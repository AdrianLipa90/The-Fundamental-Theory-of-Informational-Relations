#!/usr/bin/env python3
"""Stage 50: exact symmetric-square three-dimensional polynomial lift."""
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

J = [
    [F(0), F(0), F(1,2)],
    [F(0), F(-1), F(0)],
    [F(1,2), F(0), F(0)],
]


def transpose(A):
    return [list(row) for row in zip(*A)]


def matmul(A, B):
    return [
        [sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
        for i in range(len(A))
    ]


def det3(A):
    return (
        A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
        - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
        + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0])
    )


def preserve(R):
    return matmul(matmul(transpose(R), J), R) == J


def encode(A):
    return [[str(x) for x in row] for row in A]


def main() -> None:
    checks = {
        "det_RE_one": det3(R_E) == 1,
        "det_RO_one": det3(R_O) == 1,
        "RE_preserves_J": preserve(R_E),
        "RO_preserves_J": preserve(R_O),
    }
    result = {
        "schema": "TIR_POLYGONAL_STAGE50_SYM2_POLYNOMIAL_THREE_CARRIER_V0_1",
        "R_E": encode(R_E),
        "R_O": encode(R_O),
        "J": encode(J),
        "checks": checks,
        "pass": all(checks.values()),
        "carrier_dimension": 3,
        "preserved_quadratic_form": "xz-y^2",
        "signature": "indefinite (1,2) up to overall sign convention",
        "SU3_family_identification_claimed": False,
        "CKM_input_used": False,
        "mass_input_used": False
    }
    print(json.dumps(result, indent=2))
    if not result["pass"]:
        raise SystemExit("Stage 50 audit failed")


if __name__ == "__main__":
    main()
