#!/usr/bin/env python3
from __future__ import annotations
import json

X2 = ((0, 1), (1, 0))
I2 = ((1, 0), (0, 1))

def mm(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))

J_chi = X2
C_E = X2
F = I2
F_swapped = X2

checks = {
    "tir_involution": mm(J_chi, J_chi) == I2,
    "exceptional_involution": mm(C_E, C_E) == I2,
    "convention_fixed_intertwiner": mm(F, J_chi) == mm(C_E, F),
    "swapped_orientation_also_intertwines": mm(F_swapped, J_chi) == mm(C_E, F_swapped),
}

report = {
    "schema": "tir.polygonal.stage23.chirality-intertwiner/v0.1",
    "status": "PASS" if all(checks.values()) else "FAIL",
    "checks": checks,
    "intertwiner_residual_exact": 0 if checks["convention_fixed_intertwiner"] else 1,
    "orientation_convention": "TIR left-handed Weyl matter carrier -> 27 label",
    "scope": "Z2 label-representation equivalence",
}
print(json.dumps(report, indent=2, sort_keys=True))
raise SystemExit(0 if report["status"] == "PASS" else 1)
