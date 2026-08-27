#!/usr/bin/env python3
"""Stage 32 audit: reproduce CKM unitary construction while preserving postdictive provenance status."""
import cmath
import json
import math

KAPPA = math.log(2.0) / (24.0 * math.pi)
L3, L4, L5 = 7.0, 2.0, 5.0
V_CB = (L4 / L3) ** 2 / 2.0
V_UB = (L4 / L3) ** 2 * L4 / (L3 + L4) / L5
J_CP = KAPPA ** 2 * (L4 / L5) * (1.0 - (L4 / L5) ** 2 / 2.0)

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

def build(lam):
    theta12 = math.asin(lam)
    theta23 = math.asin(V_CB)
    theta13 = math.asin(V_UB)
    s12, s23, s13 = lam, V_CB, V_UB
    c12, c23, c13 = math.cos(theta12), math.cos(theta23), math.cos(theta13)
    denom = s12*s23*s13*c12*c23*c13
    sin_delta = max(-1.0, min(1.0, J_CP / denom))
    delta = math.asin(sin_delta)
    r12 = [[c12,s12,0],[-s12,c12,0],[0,0,1]]
    r13 = [
        [c13,0,s13*cmath.exp(-1j*delta)],
        [0,1,0],
        [-s13*cmath.exp(1j*delta),0,c13],
    ]
    r23 = [[1,0,0],[0,c23,s23],[0,-s23,c23]]
    v = mm(mm(r23,r13),r12)
    return {
        "lambda": lam,
        "delta_from_jarlskog_deg": delta*180.0/math.pi,
        "unitarity_residual_max_abs": maxdiff(mm(v,dagger(v)),eye(3)),
        "determinant_minus_one_abs": abs(det3(v)-1.0),
    }

base = build(L4/(L3+L4))
refined = build(L4/(L3+L4) + (L4/L3)*KAPPA)
tol = 1e-12
math_pass = all(
    row["unitarity_residual_max_abs"] < tol and row["determinant_minus_one_abs"] < tol
    for row in (base, refined)
)

out = {
    "schema": "TIR_POLYGONAL_STAGE32_CKM_PROVENANCE_AUDIT_V0_1",
    "status": "PASS" if math_pass else "FAIL",
    "mathematical_construction": {
        "base_v7_9": base,
        "refined_v7_9r1": refined,
    },
    "provenance_classification": {
        "structural_formula_candidate": "RETAIN",
        "prospective_prediction_status": "POSTDICTIVE",
        "reason": [
            "v7.9 provenance records structural PASS but not formal freeze",
            "PDG comparison was present in the development record",
            "r1 changes lambda after the earlier comparison",
            "the later CP chapter changes the phase formula after analysis of the earlier result",
        ],
    },
    "guard": "No PDG values are used in this executable; postdictive status is a provenance classification, not a numerical-fit calculation.",
}
print(json.dumps(out, indent=2, sort_keys=True))
raise SystemExit(0 if math_pass else 1)
