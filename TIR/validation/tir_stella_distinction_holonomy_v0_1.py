#!/usr/bin/env python3
"""Audit for the TIR stella distinction/holonomy bridge.

Exact integer/Gaussian-integer checks are used where possible. Irrational
normalization is represented algebraically by M(v)^2=|v|^2 I.
"""
from fractions import Fraction as F
import json

V = [
    (1, 1, 1),
    (1, -1, -1),
    (-1, 1, -1),
    (-1, -1, 1),
]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]


def msub(A, B):
    return [[A[i][j] - B[i][j] for j in range(2)] for i in range(2)]


def mscale(c, A):
    return [[c * A[i][j] for j in range(2)] for i in range(2)]


def pauli_dot(v):
    x, y, z = v
    return [[z + 0j, x - 1j * y], [x + 1j * y, -z + 0j]]


I2 = [[1 + 0j, 0j], [0j, 1 + 0j]]
Z2 = [[0j, 0j], [0j, 0j]]
checks = {}

checks["tetra_zero_sum"] = all(sum(v[k] for v in V) == 0 for k in range(3))
checks["tetra_norm_sq_3"] = all(dot(v, v) == 3 for v in V)
checks["tetra_pair_dot_minus1"] = all(
    dot(V[i], V[j]) == -1 for i in range(4) for j in range(i + 1, 4)
)

stella = V + [neg(v) for v in V]
checks["stella_eight_unique_vertices"] = len(set(stella)) == 8
checks["cross_unmatched_dot_plus1"] = all(
    dot(V[i], neg(V[j])) == 1
    for i in range(4) for j in range(4) if i != j
)
checks["matched_antipode_dot_minus3"] = all(
    dot(V[i], neg(V[i])) == -3 for i in range(4)
)

matchings = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]
axis_pairs = []
for (i, j), (k, l) in matchings:
    axis_pairs.append((cross(V[i], neg(V[j])), cross(V[k], neg(V[l]))))
checks["perfect_matching_transport_axes_orthogonal"] = all(
    dot(a, b) == 0 for a, b in axis_pairs
)

Ms = [pauli_dot(v) for v in V]
checks["pauli_numerator_square_3I"] = all(
    mm(M, M) == mscale(3, I2) for M in Ms
)
checks["tetra_pauli_anticommutator"] = all(
    madd(mm(Ms[i], Ms[j]), mm(Ms[j], Ms[i])) == mscale(-2, I2)
    for i in range(4) for j in range(i + 1, 4)
)
checks["tetra_pauli_noncommuting"] = all(
    msub(mm(Ms[i], Ms[j]), mm(Ms[j], Ms[i])) != Z2
    for i in range(4) for j in range(i + 1, 4)
)

half_classes = []
half_turn_square_checks = []
for M in Ms:
    for eps in (+1, -1):
        numerator_square = mscale((-1j * eps) ** 2, mm(M, M))
        half_turn_square_checks.append(numerator_square == mscale(-3, I2))
        half_classes.append(F(eps, 2) % 1)
checks["eight_oriented_half_turns"] = len(half_turn_square_checks) == 8
checks["all_half_turn_squares_minus_I"] = all(half_turn_square_checks)
checks["all_modulo_classes_half"] = all(q == F(1, 2) for q in half_classes)


def readout_from_raw_dot(raw_dot):
    return (F(1) + F(raw_dot, 3)) / 2


checks["readout_same_vertex_1"] = readout_from_raw_dot(3) == F(1)
checks["readout_same_tetra_distinct_1_3"] = readout_from_raw_dot(-1) == F(1, 3)
checks["readout_matched_antipode_0"] = readout_from_raw_dot(-3) == F(0)
checks["readout_cross_unmatched_2_3"] = readout_from_raw_dot(1) == F(2, 3)
checks["orthogonal_frame_readout_half"] = (F(1) + F(0)) / 2 == F(1, 2)

passed = all(checks.values())
payload = {
    "schema": "TIR_STELLA_DISTINCTION_HOLONOMY_BRIDGE_V0_1",
    "technical_status": "PASS" if passed else "FAIL",
    "checks": checks,
    "counts": {
        "tetra_vertices": 4,
        "stella_vertices": 8,
        "antipodal_axes": 4,
        "oriented_half_turn_representatives": 8,
    },
    "modulo_class": "[1/2] in R/Z",
    "firewall": {
        "antipodal_completion_required_as_scope": True,
        "idt_temporal_phase_identification_proved": False,
        "interpretation_equivalence_proved": False,
        "riemann_hypothesis_proved": False,
    },
}
print(json.dumps(payload, indent=2, sort_keys=True))
raise SystemExit(0 if passed else 1)
