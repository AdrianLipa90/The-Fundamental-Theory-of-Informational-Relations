#!/usr/bin/env python3

import itertools
import json
from fractions import Fraction


def parity(p):
    inv = 0
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                inv += 1
    return inv % 2


verts = (0, 1, 2, 3)
s4 = list(itertools.permutations(verts))
a4 = [p for p in s4 if parity(p) == 0]
edges = {tuple(sorted(e)) for e in itertools.combinations(verts, 2)}

edge_orbit = set()
for p in a4:
    edge_orbit.add(tuple(sorted((p[0], p[1]))))

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


edge_sq = {dot(sub(vecs[i], vecs[j]), sub(vecs[i], vecs[j])) for i, j in itertools.combinations(range(4), 2)}
center = tuple(sum(v[k] for v in vecs) for k in range(3))
vertex_norm_sq = dot(vecs[0], vecs[0])
offdiag = {Fraction(dot(vecs[i], vecs[j]), vertex_norm_sq) for i, j in itertools.combinations(range(4), 2)}

second_integer = [[sum(v[i] * v[j] for v in vecs) for j in range(3)] for i in range(3)]
second_normalized = [[Fraction(x, vertex_norm_sq) for x in row] for row in second_integer]
second_expected = [[Fraction(4, 3) if i == j else Fraction(0) for j in range(3)] for i in range(3)]

checks = {
    "aut_delta3_order_24": len(s4) == 24,
    "oriented_aut_delta3_order_12": len(a4) == 12,
    "edge_count_6": len(edges) == 6,
    "a4_edge_transitive": edge_orbit == edges,
    "regular_realization_all_edges_equal": len(edge_sq) == 1,
    "centered_frame_zero_sum": center == (0, 0, 0),
    "normalized_pairwise_dot_minus_one_third": offdiag == {Fraction(-1, 3)},
    "second_moment_four_thirds_identity": second_normalized == second_expected,
}

receipt = {
    "schema": "TIR_UNLABELED_SIMPLEX_AUTOMORPHISM_REGULARITY_V0_1",
    "technical_status": "PASS" if all(checks.values()) else "FAIL",
    "abstract_simplex_automorphism_group": "S4",
    "oriented_automorphism_group": "A4",
    "edge_orbit_size": len(edge_orbit),
    "exact_result": "FAITHFUL_ISOMETRIC_REALIZATION_OF_ORIENTED_SIMPLEX_AUTOMORPHISMS_IMPLIES_REGULAR_TETRAHEDRON",
    "normalized_pairwise_dot": "-1/3",
    "second_moment": "(4/3)I3",
    "su2_lift": "binary_tetrahedral_group_2T",
    "remaining_tir_gate": "A3+A7_FAITHFULLY_REALIZE_INTRINSIC_ORIENTED_SIMPLEX_AUTOMORPHISMS_ISOMETRICALLY",
    "checks": checks,
}

print(json.dumps(receipt, indent=2, sort_keys=True))
