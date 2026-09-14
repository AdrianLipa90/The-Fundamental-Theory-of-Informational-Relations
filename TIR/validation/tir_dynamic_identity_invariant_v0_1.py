#!/usr/bin/env python3
"""Deterministic validator for the TIR Dynamic Identity Invariant v0.1.

This is a numerical regression witness for exact algebraic statements documented
in the repository. It does not promote physical interpretations.
"""
from math import acos, pi, sqrt
import json

TOL = 1e-12

I2 = [[1+0j, 0j], [0j, 1+0j]]

V = [
    (1/sqrt(3), 1/sqrt(3), 1/sqrt(3)),
    (1/sqrt(3), -1/sqrt(3), -1/sqrt(3)),
    (-1/sqrt(3), 1/sqrt(3), -1/sqrt(3)),
    (-1/sqrt(3), -1/sqrt(3), 1/sqrt(3)),
]


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def mm(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
            for i in range(len(A))]


def madd(A, B):
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def msub(A, B):
    return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mscale(c, A):
    return [[c*A[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def dagger(A):
    return [[A[j][i].conjugate() for j in range(len(A))] for i in range(len(A[0]))]


def maxabs(A):
    return max(abs(x) for row in A for x in row)


def close(A, B, tol=TOL):
    return maxabs(msub(A, B)) <= tol


def sigma(n):
    x, y, z = n
    return [[z+0j, x-1j*y], [x+1j*y, -z+0j]]


S = [sigma(v) for v in V]


def edge_transport(i, j):
    d = dot(V[i], V[j])
    denom = sqrt(2*(1+d))
    return mscale(1/denom, madd(I2, mm(S[i], S[j])))


def block_set(A, bi, bj, B):
    r0, c0 = 2*bi, 2*bj
    for i in range(2):
        for j in range(2):
            A[r0+i][c0+j] = B[i][j]


def commutator(A, B):
    return msub(mm(A, B), mm(B, A))


checks = {}
checks["tetra_pair_dot_minus_one_third"] = all(
    abs(dot(V[i], V[j]) + 1/3) <= TOL
    for i in range(4) for j in range(i+1, 4)
)
checks["sigma_involutions"] = all(close(mm(s, s), I2) for s in S)

for i in range(4):
    for j in range(4):
        if i == j:
            continue
        U = edge_transport(i, j)
        checks[f"unitary_{i}{j}"] = close(mm(U, dagger(U)), I2)
        checks[f"intertwine_{i}{j}"] = close(mm(mm(U, S[j]), dagger(U)), S[i])

W012 = mm(mm(edge_transport(0, 1), edge_transport(1, 2)), edge_transport(2, 0))
W021 = mm(mm(edge_transport(0, 2), edge_transport(2, 1)), edge_transport(1, 0))
checks["face_holonomy_positive"] = close(W012, mscale(1j, S[0]))
checks["face_holonomy_negative"] = close(W021, mscale(-1j, S[0]))
checks["holonomy_square_minus_identity"] = close(mm(W012, W012), mscale(-1, I2))
checks["holonomy_fourth_identity"] = close(mm(mm(W012, W012), mm(W012, W012)), I2)
checks["closed_loop_preserves_local_sector"] = maxabs(commutator(W012, S[0])) <= TOL

c = -1/3
cos_A = c/(1+c)
A = acos(cos_A)
Omega = 3*A - pi
checks["tetra_spherical_face_angle_two_pi_over_three"] = abs(A - 2*pi/3) <= TOL
checks["tetra_spherical_excess_pi"] = abs(Omega - pi) <= TOL

N = 3
Sig = [[0j]*(2*N) for _ in range(2*N)]
H = [[0j]*(2*N) for _ in range(2*N)]
for a in range(N):
    block_set(Sig, a, a, S[a])
    block_set(H, a, a, mscale(0.17*(a+1), S[a]))

for a, b, t in [(0, 1, 0.31), (1, 2, 0.23), (2, 0, 0.19)]:
    Uab = edge_transport(a, b)
    Uba = dagger(Uab)
    block_set(H, a, b, mscale(-t, Uab))
    block_set(H, b, a, mscale(-t, Uba))

checks["global_hamiltonian_hermitian"] = close(H, dagger(H))
checks["global_dynamic_identity_commutator_zero"] = maxabs(commutator(H, Sig)) <= 2e-12

H_bad = [row[:] for row in H]
block_set(H_bad, 0, 1, mscale(-0.31, I2))
block_set(H_bad, 1, 0, mscale(-0.31, I2))
checks["negative_control_breaks_invariant"] = maxabs(commutator(H_bad, Sig)) > 1e-6

passed = all(checks.values())
payload = {
    "schema": "TIR_DYNAMIC_IDENTITY_INVARIANT_V0_1",
    "technical_status": "PASS" if passed else "FAIL",
    "claim_scope": {
        "local_tetrahedral_transport": "EXACT_ALGEBRAIC_STATEMENT",
        "face_holonomy": "EXACT_ALGEBRAIC_STATEMENT",
        "global_static_invariant_under_compatible_transport": "EXACT_ALGEBRAIC_STATEMENT",
        "time_dependent_extension": "STANDARD_INVARIANT_EQUATION",
        "periodic_n_simplex_extension": "CONDITIONAL_ON_CHOSEN_CLIFFORD_AND_GLUE_DATA",
        "physical_identity_binding": "NOT_CLAIMED",
    },
    "checks": checks,
    "max_commutator_good": maxabs(commutator(H, Sig)),
    "max_commutator_bad": maxabs(commutator(H_bad, Sig)),
    "spherical_excess": Omega,
}
print(json.dumps(payload, indent=2, sort_keys=True))
raise SystemExit(0 if passed else 1)
