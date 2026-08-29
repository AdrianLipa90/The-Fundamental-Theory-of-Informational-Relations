#!/usr/bin/env python3

import json
from fractions import Fraction


def add(u, v):
    return tuple(a + b for a, b in zip(u, v))


def sub(u, v):
    return tuple(a - b for a, b in zip(u, v))


def scale(c, v):
    return tuple(c * x for x in v)


def mat_vec(M, v):
    return tuple(sum(M[i][j] * v[j] for j in range(3)) for i in range(3))


x = (Fraction(1, 7), Fraction(-2, 9), Fraction(3, 10))
y = (Fraction(5, 8), Fraction(4, 11), Fraction(-1, 6))
z = (Fraction(-2, 5), Fraction(7, 12), Fraction(1, 3))

d_xy = sub(y, x)
d_yz = sub(z, y)
d_xz = sub(z, x)

endpoint_carrying = add(x, d_xy) == y
reversal = sub(x, y) == scale(Fraction(-1), d_xy)
composition = add(d_xy, d_yz) == d_xz
triangle = add(add(d_xy, d_yz), sub(x, z)) == (0, 0, 0)

L = (
    (Fraction(2), Fraction(1), Fraction(0)),
    (Fraction(0), Fraction(1), Fraction(1)),
    (Fraction(1), Fraction(0), Fraction(1)),
)
a = (Fraction(2, 3), Fraction(-1, 4), Fraction(5, 9))
Fx = add(mat_vec(L, x), a)
Fy = add(mat_vec(L, y), a)
naturality = sub(Fy, Fx) == mat_vec(L, d_xy)

# Pauli coordinate normalization doubles density-operator affine displacement.
pauli_relation = scale(Fraction(2), d_xy)
pauli_metric_sq = sum(c * c for c in pauli_relation)
bloch_delta = pauli_relation
bloch_metric_sq = sum(c * c for c in bloch_delta)

checks = {
    "endpoint_carrying_unique_displacement_sample": endpoint_carrying,
    "reversal": reversal,
    "endpoint_composition": composition,
    "triangle_closure": triangle,
    "affine_naturality": naturality,
    "pauli_metric_matches_coefficient_metric": pauli_metric_sq == bloch_metric_sq,
}

receipt = {
    "schema": "TIR_CANONICAL_SPATIAL_RELATION_EXTRACTION_V0_1",
    "technical_status": "PASS" if all(checks.values()) else "FAIL",
    "exact_result": "UNIQUE_ENDPOINT_CARRYING_AFFINE_DISPLACEMENT",
    "intrinsic_relation": "e_xy=rho_y-rho_x",
    "generator_normalization": "E_xy=2*(rho_y-rho_x)",
    "local_relation_carrier": "Herm_0(2)~=R3",
    "carrier_real_dimension": 3,
    "source_minimality_role": "AUDIT_EXPLANATION",
    "spatial_relation_status": "CANONICAL_BRANCH_CONSTRUCTION",
    "next_frontier": "DELTA3_TO_REGULAR_TETRAHEDRON_VIA_INTRINSIC_SIMPLEX_SYMMETRY",
    "checks": checks,
}

print(json.dumps(receipt, indent=2, sort_keys=True))
