#!/usr/bin/env python3
"""Stage 52: spin-1 Sym^2(SU(2)) Lie-algebra embedding into su(3)."""
from __future__ import annotations

import cmath
import json
import math

SQ2 = math.sqrt(2.0)

JX = [
    [0j, 1/SQ2, 0j],
    [1/SQ2, 0j, 1/SQ2],
    [0j, 1/SQ2, 0j],
]
JY = [
    [0j, -1j/SQ2, 0j],
    [1j/SQ2, 0j, -1j/SQ2],
    [0j, 1j/SQ2, 0j],
]
JZ = [
    [1+0j, 0j, 0j],
    [0j, 0j, 0j],
    [0j, 0j, -1+0j],
]


def mm(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def sub(A, B):
    return [[A[i][j]-B[i][j] for j in range(3)] for i in range(3)]


def scale(s, A):
    return [[s*A[i][j] for j in range(3)] for i in range(3)]


def dag(A):
    return [[A[j][i].conjugate() for j in range(3)] for i in range(3)]


def comm(A, B):
    return sub(mm(A, B), mm(B, A))


def maxabs(A):
    return max(abs(x) for row in A for x in row)


def trace(A):
    return sum(A[i][i] for i in range(3))


def main() -> None:
    hermitian = all(maxabs(sub(J, dag(J))) < 1e-12 for J in (JX, JY, JZ))
    traceless = all(abs(trace(J)) < 1e-12 for J in (JX, JY, JZ))

    r_xy = maxabs(sub(comm(JX, JY), scale(1j, JZ)))
    r_yz = maxabs(sub(comm(JY, JZ), scale(1j, JX)))
    r_zx = maxabs(sub(comm(JZ, JX), scale(1j, JY)))

    antihermitian_T = all(
        maxabs(sub(scale(-1j, J), scale(-1, dag(scale(-1j, J))))) < 1e-12
        for J in (JX, JY, JZ)
    )

    checks = {
        "J_generators_hermitian": hermitian,
        "J_generators_traceless": traceless,
        "su2_commutator_xy": r_xy < 1e-12,
        "su2_commutator_yz": r_yz < 1e-12,
        "su2_commutator_zx": r_zx < 1e-12,
        "minus_i_J_in_su3_lie_algebra": antihermitian_T and traceless,
    }

    result = {
        "schema": "TIR_POLYGONAL_STAGE52_COMPACT_REAL_FORM_SYM2_V0_1",
        "commutator_residuals": {"xy": r_xy, "yz": r_yz, "zx": r_zx},
        "checks": checks,
        "pass": all(checks.values()),
        "representation_dimension": 3,
        "embedding": "Sym^2(SU(2)) subset SU(3)",
        "compact_real_form_dynamically_selected": False,
        "CKM_input_used": False,
        "mass_input_used": False
    }
    print(json.dumps(result, indent=2))
    if not result["pass"]:
        raise SystemExit("Stage 52 audit failed")


if __name__ == "__main__":
    main()
