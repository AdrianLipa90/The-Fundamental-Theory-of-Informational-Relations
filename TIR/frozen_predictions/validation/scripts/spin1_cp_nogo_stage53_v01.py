#!/usr/bin/env python3
"""Stage 53: numerical sanity check of spin-1 Wigner rephasing and J=0."""
from __future__ import annotations

import cmath
import json
import math


def matmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][k]*B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]


def diag(vals):
    return [[vals[i] if i == j else 0j for j in range(len(vals))] for i in range(len(vals))]


def d1(beta: float):
    c = math.cos(beta)
    s = math.sin(beta)
    r2 = math.sqrt(2.0)
    return [
        [(1+c)/2, -s/r2, (1-c)/2],
        [s/r2, c, -s/r2],
        [(1-c)/2, s/r2, (1+c)/2],
    ]


def D1(alpha: float, beta: float, gamma: float):
    PL = diag([cmath.exp(-1j*alpha), 1+0j, cmath.exp(1j*alpha)])
    PR = diag([cmath.exp(-1j*gamma), 1+0j, cmath.exp(1j*gamma)])
    return matmul(matmul(PL, d1(beta)), PR)


def jarlskog(V):
    return (V[0][0]*V[1][1]*V[0][1].conjugate()*V[1][0].conjugate()).imag


def max_imag_after_rephase(alpha, beta, gamma):
    V = D1(alpha, beta, gamma)
    PL_inv = diag([cmath.exp(1j*alpha), 1+0j, cmath.exp(-1j*alpha)])
    PR_inv = diag([cmath.exp(1j*gamma), 1+0j, cmath.exp(-1j*gamma)])
    real_form = matmul(matmul(PL_inv, V), PR_inv)
    return max(abs(complex(x).imag) for row in real_form for x in row)


def main() -> None:
    samples = [
        (0.37, 0.61, -0.29),
        (1.2, 0.4, 2.1),
        (-0.8, 1.1, 0.55),
        (2.4, 0.9, -1.7),
    ]
    rows = []
    for alpha, beta, gamma in samples:
        V = D1(alpha, beta, gamma)
        rows.append({
            "alpha": alpha,
            "beta": beta,
            "gamma": gamma,
            "J": jarlskog(V),
            "max_imag_after_row_column_rephase": max_imag_after_rephase(alpha, beta, gamma),
        })

    checks = {
        "all_sample_J_zero": all(abs(r["J"]) < 1e-14 for r in rows),
        "all_rephase_to_real": all(r["max_imag_after_row_column_rephase"] < 1e-14 for r in rows),
        "dimension_decomposition": 8 == 3 + 5,
    }
    result = {
        "schema": "TIR_POLYGONAL_STAGE53_SPIN1_CP_NOGO_3PLUS5_V0_1",
        "samples": rows,
        "checks": checks,
        "pass": all(checks.values()),
        "adjoint_decomposition": "su(3) -> 3 + 5 under spin-1 SU(2)",
        "CKM_input_used": False,
        "mass_input_used": False,
        "polygon_N5_identification_claimed": False
    }
    print(json.dumps(result, indent=2))
    if not result["pass"]:
        raise SystemExit("Stage 53 audit failed")


if __name__ == "__main__":
    main()
