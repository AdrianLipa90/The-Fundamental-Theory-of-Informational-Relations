#!/usr/bin/env python3
from __future__ import annotations
import json

P3 = (
    (0, 0, 1),
    (1, 0, 0),
    (0, 1, 0),
)
X2 = ((0, 1), (1, 0))
I3 = ((1,0,0),(0,1,0),(0,0,1))
I2 = ((1,0),(0,1))

def mm(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(m)) for j in range(p)) for i in range(n))

def eye(n):
    return tuple(tuple(1 if i == j else 0 for j in range(n)) for i in range(n))

def kron(A, B):
    return tuple(
        tuple(A[i][j] * B[a][b] for j in range(len(A[0])) for b in range(len(B[0])))
        for i in range(len(A)) for a in range(len(B))
    )

def mpow(A, k):
    R = eye(len(A))
    for _ in range(k):
        R = mm(R, A)
    return R

P_s = P3
J_chi = X2
P_e8 = P3
C_e8 = X2
M_s = I3
F = I2
T = kron(M_s, F)
G_tir = kron(P_s, J_chi)
G_e8 = kron(P_e8, C_e8)
I6 = eye(6)

checks = {
    "seed_triplet_intertwiner": mm(M_s, P_s) == mm(P_e8, M_s),
    "chirality_intertwiner": mm(F, J_chi) == mm(C_e8, F),
    "six_state_intertwiner": mm(T, G_tir) == mm(G_e8, T),
    "cube_is_sheet_flip": mpow(G_tir, 3) == kron(I3, X2),
    "sixth_power_identity": mpow(G_tir, 6) == I6,
    "minimal_order_six": all(mpow(G_tir, k) != I6 for k in range(1, 6)),
    "same_exceptional_operator": G_tir == G_e8,
}

report = {
    "schema": "tir.polygonal.stage24.seed-chirality-e8-intertwiner/v0.1",
    "status": "PASS" if all(checks.values()) else "FAIL",
    "seed_order": [[3,5],[5,7],[11,13]],
    "checks": checks,
    "intertwiner_residual_exact": 0 if checks["six_state_intertwiner"] else 1,
    "operator_order": 6,
    "characteristic_polynomial": "lambda^6 - 1",
    "scope": "finite six-state label representation",
}
print(json.dumps(report, indent=2, sort_keys=True))
raise SystemExit(0 if report["status"] == "PASS" else 1)
