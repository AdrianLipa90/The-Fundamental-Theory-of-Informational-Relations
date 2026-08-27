#!/usr/bin/env python3
"""Stage 18: shared Z3 seam between the E7 and E8 exceptional branches.

Checks the explicit U(1)->SU(3) embedding and the trivial action of the SU(3)
center on CP2 projective coordinates.
"""
import cmath
import json

TOL = 1e-12


def matmul3(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def dagger3(A):
    return [[A[j][i].conjugate() for j in range(3)] for i in range(3)]


def outer_projector(v):
    n = sum(abs(x)**2 for x in v)
    return [[v[i]*v[j].conjugate()/n for j in range(3)] for i in range(3)]


def maxdiff(A, B):
    return max(abs(A[i][j]-B[i][j]) for i in range(3) for j in range(3))


def run():
    theta = 2.0*cmath.pi/3.0
    a = cmath.exp(1j*theta)
    U = [[a,0,0],[0,a,0],[0,0,cmath.exp(-2j*theta)]]
    omega = cmath.exp(2j*cmath.pi/3.0)
    Z = [[omega if i == j else 0 for j in range(3)] for i in range(3)]

    detU = U[0][0]*U[1][1]*U[2][2]
    unit = matmul3(dagger3(U), U)
    I = [[1 if i == j else 0 for j in range(3)] for i in range(3)]

    v = [1+2j, -3+0.5j, 2-1j]
    zv = [omega*x for x in v]
    P = outer_projector(v)
    Pz = outer_projector(zv)

    checks = {
        "embedding_element_in_SU3": abs(detU-1) < TOL and maxdiff(unit, I) < TOL,
        "third_turn_hits_SU3_center": maxdiff(U, Z) < TOL,
        "center_has_order_3": abs(omega**3-1) < TOL,
        "Z3_trivial_on_CP2_projector": maxdiff(P, Pz) < TOL,
    }

    return {
        "schema": "TIR-E7-E8-Z3-SEAM/0.1",
        "stage": 18,
        "embedding": "exp(i theta) -> diag(exp(i theta), exp(i theta), exp(-2 i theta))",
        "theta_test": "2*pi/3",
        "determinant_residual": abs(detU-1),
        "center_match_residual": maxdiff(U, Z),
        "center_order3_residual": abs(omega**3-1),
        "CP2_projective_center_residual": maxdiff(P, Pz),
        "checks": checks,
        "verdict": "PASS" if all(checks.values()) else "FAIL"
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
