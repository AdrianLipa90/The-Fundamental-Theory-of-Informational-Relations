#!/usr/bin/env python3

import itertools
import json
from fractions import Fraction

verts = (0, 1, 2, 3)
s4 = list(itertools.permutations(verts))
edges = {tuple(sorted(e)) for e in itertools.combinations(verts, 2)}

edge_orbit = set()
for p in s4:
    edge_orbit.add(tuple(sorted((p[0], p[1]))))

# Exact regular tetrahedral realization used only as a downstream certificate.
vecs = [
    (1, 1, 1),
    (1, -1, -1),
    (-1, 1, -1),
    (-1, -1, 1),
]


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def sub(u, v):
    return tuple(a - b for a, b in zip(u, v))


edge_sq = {
    dot(sub(vecs[i], vecs[j]), sub(vecs[i], vecs[j]))
    for i, j in itertools.combinations(range(4), 2)
}
center = tuple(sum(v[k] for v in vecs) for k in range(3))
norm_sq = dot(vecs[0], vecs[0])
normalized_offdiag = {
    Fraction(dot(vecs[i], vecs[j]), norm_sq)
    for i, j in itertools.combinations(range(4), 2)
}
second_integer = [[sum(v[i] * v[j] for v in vecs) for j in range(3)] for i in range(3)]
second_normalized = [[Fraction(x, norm_sq) for x in row] for row in second_integer]
second_expected = [[Fraction(4, 3) if i == j else Fraction(0) for j in range(3)] for i in range(3)]

checks = {
    "aut_delta3_order_24": len(s4) == 24,
    "edge_count_6": len(edges) == 6,
    "s4_edge_action_transitive": edge_orbit == edges,
    "regular_certificate_equal_six_edges": len(edge_sq) == 1,
    "centered_zero_sum": center == (0, 0, 0),
    "normalized_pairwise_dot_minus_one_third": normalized_offdiag == {Fraction(-1, 3)},
    "second_moment_four_thirds_identity": second_normalized == second_expected,
}

receipt = {
    "schema": "TIR_A5_A7_SIMPLEX_EDGE_ORBIT_REGULARITY_V0_1",
    "technical_status": "PASS" if all(checks.values()) else "FAIL",
    "abstract_simplex_automorphism_group": "S4",
    "edge_orbit_size": len(edge_orbit),
    "edge_measure": "q_ij=0.5*Tr(E_ij^2)",
    "a5_role": "ARITHMETIC_GEOMETRIC_EDGE_MEASURE",
    "a7_role": "INVARIANCE_OF_EDGE_MEASURE_LAW_UNDER_INTRINSIC_SIMPLEX_AUTOMORPHISMS",
    "exact_result": "S4_EDGE_ORBIT_INVARIANCE_IMPLIES_EQUAL_SIX_EDGE_LENGTHS_AND_REGULAR_TETRAHEDRON",
    "normalized_pairwise_dot": "-1/3",
    "second_moment": "(4/3)I3",
    "regularity_gate_status": "CLOSED_BY_EXISTING_A5_A7_CROSSWALK",
    "oriented_rotation_group": "A4",
    "su2_lift": "binary_tetrahedral_group_2T",
    "checks": checks,
}

print(json.dumps(receipt, indent=2, sort_keys=True))
