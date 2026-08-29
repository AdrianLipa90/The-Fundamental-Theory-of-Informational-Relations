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


vertices = (0, 1, 2, 3)
a4 = [p for p in itertools.permutations(vertices) if parity(p) == 0]
edges = {tuple(sorted(e)) for e in itertools.combinations(vertices, 2)}

edge_orbit = set()
seed = (0, 1)
for p in a4:
    edge_orbit.add(tuple(sorted((p[seed[0]], p[seed[1]]))))

# Exact regular tetrahedral integer realization.
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


pairwise_sq = {dot(sub(vecs[i], vecs[j]), sub(vecs[i], vecs[j])) for i, j in itertools.combinations(range(4), 2)}
center_sum = tuple(sum(v[k] for v in vecs) for k in range(3))
diag = {dot(v, v) for v in vecs}
offdiag = {dot(vecs[i], vecs[j]) for i, j in itertools.combinations(range(4), 2)}
normalized_offdiag = Fraction(next(iter(offdiag)), next(iter(diag)))

# Second moment of normalized directions: integer realization gives sum vv^T = 4 I,
# while |v|^2=3, hence normalized moment is (4/3) I.
second_moment_integer = [[sum(v[i] * v[j] for v in vecs) for j in range(3)] for i in range(3)]
second_moment_normalized = [[Fraction(x, 3) for x in row] for row in second_moment_integer]
expected_second_moment = [[Fraction(4, 3) if i == j else Fraction(0) for j in range(3)] for i in range(3)]

checks = {
    "a4_order_is_12": len(a4) == 12,
    "edge_set_size_is_6": len(edges) == 6,
    "a4_edge_action_transitive": edge_orbit == edges,
    "regular_realization_all_six_edges_equal": len(pairwise_sq) == 1,
    "barycenter_zero": center_sum == (0, 0, 0),
    "equal_vertex_norms": len(diag) == 1,
    "equal_offdiagonal_inner_products": len(offdiag) == 1,
    "normalized_pairwise_dot_is_minus_one_third": normalized_offdiag == Fraction(-1, 3),
    "normalized_second_moment_is_four_thirds_identity": second_moment_normalized == expected_second_moment,
}

technical_status = "PASS" if all(checks.values()) else "FAIL"

receipt = {
    "schema": "TIR_MINIMAL_SIMPLEX_MAXIMAL_SYMMETRY_V0_1",
    "technical_status": technical_status,
    "minimal_full_dimensional_vertex_count": 4,
    "minimal_cell": "Delta^3",
    "max_orientation_preserving_symmetry_order": 12,
    "max_symmetry_group": "A4",
    "edge_action_transitive": True,
    "regularity_result": "MAXIMAL_ORIENTATION_PRESERVING_TETRAHEDRAL_SYMMETRY_IMPLIES_REGULAR_TETRAHEDRON",
    "normalized_pairwise_dot": "-1/3",
    "second_moment": "(4/3)I3",
    "finite_stabilizer_in_SO3": "A4",
    "su2_lift": "binary_tetrahedral_group_2T",
    "remaining_tir_gate": "A7_PRIMITIVE_MINIMAL_CELL_SELECTS_MAXIMAL_AVAILABLE_ORIENTATION_PRESERVING_SYMMETRY",
    "checks": checks,
}

print(json.dumps(receipt, indent=2, sort_keys=True))
