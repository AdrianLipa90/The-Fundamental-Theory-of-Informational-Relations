#!/usr/bin/env python3
"""Stage 34 audit: CKM-form family transformation is in SU(3)_F and commutes with SU(3)_C."""
import cmath
import json
import math

KAPPA = math.log(2.0) / (24.0 * math.pi)
A = 2.0 / 7.0
B = 2.0 / 9.0
C = 2.0 / 5.0

lam = B + A * KAPPA
v_cb = A * A / 2.0
v_ub = A * A * B * C / 2.0
theta12 = math.asin(lam)
theta23 = math.asin(v_cb)
theta13 = math.asin(v_ub)
delta = math.acos(C)

def mm(x, y):
    return [[sum(x[i][k] * y[k][j] for k in range(len(y)))
             for j in range(len(y[0]))] for i in range(len(x))]

def dagger(x):
    return [[x[j][i].conjugate() for j in range(len(x))]
            for i in range(len(x[0]))]

def eye(n):
    return [[1.0 + 0j if i == j else 0j for j in range(n)] for i in range(n)]

def det3(x):
    a,b,c = x[0]
    d,e,f = x[1]
    g,h,i = x[2]
    return a*(e*i-f*h) - b*(d*i-f*g) + c*(d*h-e*g)

def maxdiff(x, y):
    return max(abs(x[i][j] - y[i][j])
               for i in range(len(x)) for j in range(len(x[0])))

def kron(x, y):
    return [[x[i][j] * y[p][q]
             for j in range(len(x[0])) for q in range(len(y[0]))]
            for i in range(len(x)) for p in range(len(y))]

s12, c12 = math.sin(theta12), math.cos(theta12)
s23, c23 = math.sin(theta23), math.cos(theta23)
s13, c13 = math.sin(theta13), math.cos(theta13)

r12 = [[c12, s12, 0], [-s12, c12, 0], [0, 0, 1]]
r13 = [
    [c13, 0, s13 * cmath.exp(-1j * delta)],
    [0, 1, 0],
    [-s13 * cmath.exp(1j * delta), 0, c13],
]
r23 = [[1, 0, 0], [0, c23, s23], [0, -s23, c23]]
v_family = mm(mm(r23, r13), r12)

unitarity_residual = maxdiff(mm(v_family, dagger(v_family)), eye(3))
determinant_residual = abs(det3(v_family) - 1.0)

p3_color = [[0,0,1],[1,0,0],[0,1,0]]
gc = kron(p3_color, eye(3))
vf = kron(eye(3), v_family)
comm = [[a-b for a,b in zip(r1,r2)] for r1,r2 in zip(mm(gc, vf), mm(vf, gc))]
color_family_commutator_residual = max(abs(z) for row in comm for z in row)

tol = 1e-12
status = "PASS" if (
    unitarity_residual < tol
    and determinant_residual < tol
    and color_family_commutator_residual < tol
) else "FAIL"

out = {
    "schema": "TIR_POLYGONAL_STAGE34_CKM_SU3F_AUDIT_V0_1",
    "status": status,
    "inputs": {
        "kappa": KAPPA,
        "a": A,
        "b": B,
        "c": C,
        "lambda": lam,
        "V_cb": v_cb,
        "V_ub": v_ub,
        "delta_deg": delta * 180.0 / math.pi,
    },
    "checks": {
        "unitarity_residual_max_abs": unitarity_residual,
        "determinant_minus_one_abs": determinant_residual,
        "color_family_commutator_residual_max_abs": color_family_commutator_residual,
    },
    "epistemic_boundary": "group-representation audit only; Stage 32 governs predictive status of numerical CKM formulas",
}
print(json.dumps(out, indent=2, sort_keys=True))
raise SystemExit(0 if status == "PASS" else 1)
