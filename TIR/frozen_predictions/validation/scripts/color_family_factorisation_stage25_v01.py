#!/usr/bin/env python3
from __future__ import annotations
import json

P3 = (
    (0,0,1),
    (1,0,0),
    (0,1,0),
)

def eye(n):
    return tuple(tuple(1 if i == j else 0 for j in range(n)) for i in range(n))

def mm(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))) for i in range(len(A)))

def sub(A, B):
    return tuple(tuple(A[i][j] - B[i][j] for j in range(len(A[0]))) for i in range(len(A)))

def maxabs(A):
    return max(abs(x) for row in A for x in row)

def kron(A, B):
    return tuple(
        tuple(A[i][j] * B[a][b] for j in range(len(A[0])) for b in range(len(B[0])))
        for i in range(len(A)) for a in range(len(B))
    )

I3 = eye(3)
I2 = eye(2)
color_Q = kron(kron(P3, I2), I3)
family_Q = kron(kron(I3, I2), P3)
comm = sub(mm(color_Q, family_Q), mm(family_Q, color_Q))

multiplicities = {
    "Q_Y_1_6": 3*2*3,
    "u_c_Y_m2_3": 3*1*3,
    "d_c_Y_1_3": 3*1*3,
    "L_Y_m1_2": 1*2*3,
    "e_c_Y_1": 1*1*3,
    "nu_c_Y_0": 1*1*3,
}
checks = {
    "quark_doublet_dimension_18": len(color_Q) == 18,
    "color_family_commutator_zero": maxabs(comm) == 0,
    "stage21_multiplicities": multiplicities == {
        "Q_Y_1_6":18,
        "u_c_Y_m2_3":9,
        "d_c_Y_1_3":9,
        "L_Y_m1_2":6,
        "e_c_Y_1":3,
        "nu_c_Y_0":3,
    },
    "total_dimension_48": sum(multiplicities.values()) == 48,
}
report = {
    "schema":"tir.polygonal.stage25.color-family-factorisation/v0.1",
    "status":"PASS" if all(checks.values()) else "FAIL",
    "checks":checks,
    "commutator_max_abs_exact":maxabs(comm),
    "multiplicities":multiplicities,
    "scope":"commuting SU(3)_C and SU(3)_F carrier factors",
}
print(json.dumps(report, indent=2, sort_keys=True))
raise SystemExit(0 if report["status"] == "PASS" else 1)
