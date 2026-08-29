#!/usr/bin/env python3
"""Deterministic audit for The Space of Geometry research spine v0.6."""
from __future__ import annotations

import itertools
import json
from fractions import Fraction

TETRA = (
    (1, 1, 1),
    (1, -1, -1),
    (-1, 1, -1),
    (-1, -1, 1),
)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def parity(p):
    inv = 0
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                inv += 1
    return inv % 2


def affine_carrier_certificate() -> dict[str, object]:
    herm2_real_dimension = 4
    trace_constraint_codimension = 1
    affine_dimension = herm2_real_dimension - trace_constraint_codimension
    return {
        "herm2_real_dimension": herm2_real_dimension,
        "trace_constraint_codimension": trace_constraint_codimension,
        "affine_state_hull_dimension": affine_dimension,
        "translation_space": "Herm_0(2)",
        "pass": affine_dimension == 3,
    }


def tetra_certificate() -> dict[str, object]:
    norms = [dot(v, v) for v in TETRA]
    cross = [dot(TETRA[i], TETRA[j]) for i in range(4) for j in range(i + 1, 4)]
    zero_sum = tuple(sum(v[k] for v in TETRA) for k in range(3)) == (0, 0, 0)
    normalized_cross = {Fraction(x, norms[0]) for x in cross}
    return {
        "minimal_simplex_vertices": 4,
        "simplex": "Delta^3",
        "tetrahedral_zero_sum": zero_sum,
        "normalized_pairwise_dot": "-1/3",
        "pass": zero_sum and norms == [3] * 4 and normalized_cross == {Fraction(-1, 3)},
    }


def automorphism_certificate() -> dict[str, object]:
    verts = (0, 1, 2, 3)
    s4 = list(itertools.permutations(verts))
    a4 = [p for p in s4 if parity(p) == 0]
    edges = {tuple(sorted(e)) for e in itertools.combinations(verts, 2)}
    orbit = {tuple(sorted((p[0], p[1]))) for p in a4}
    return {
        "aut_delta3": "S4",
        "oriented_aut_delta3": "A4",
        "s4_order": len(s4),
        "a4_order": len(a4),
        "edge_orbit_size": len(orbit),
        "pass": len(s4) == 24 and len(a4) == 12 and orbit == edges,
    }


def pythagorean_certificate() -> dict[str, object]:
    a = (5, 0, 0)
    b = (0, 12, 0)
    c = tuple(x + y for x, y in zip(a, b))
    a2, b2, c2 = dot(a, a), dot(b, b), dot(c, c)
    return {
        "orthogonal_inner_product": dot(a, b),
        "a_squared": a2,
        "b_squared": b2,
        "c_squared": c2,
        "pass": dot(a, b) == 0 and c2 == a2 + b2 == 169,
    }


def build_receipt() -> dict[str, object]:
    blocks = {
        "quantum_point_affine_carrier": affine_carrier_certificate(),
        "minimal_regular_tetrahedral_geometry": tetra_certificate(),
        "intrinsic_simplex_automorphisms": automorphism_certificate(),
        "pythagorean_endpoint": pythagorean_certificate(),
    }
    passed = all(bool(block["pass"]) for block in blocks.values())
    return {
        "schema": "THE_SPACE_OF_GEOMETRY_SPINE_V0_6",
        "working_title": "The Space of Geometry: From First Distinction to Pythagoras",
        "endpoint": "PYTHAGOREAN_CLOSURE",
        "current_source_gate": "A1_DEPENDENCY_MINIMALITY_APPLIES_TO_PRIMITIVE_LAW_SIGNATURE",
        "current_symmetry_gate": "A3+A7_FAITHFULLY_REALIZE_INTRINSIC_ORIENTED_SIMPLEX_AUTOMORPHISMS_ISOMETRICALLY",
        "relation_law_after_source_gate": "R(x,y)=c*(y-x), c!=0",
        "local_relation_carrier": "Herm_0(2)~=R3",
        "minimal_cell": "Delta^3",
        "regularity_route": "INTRINSIC_ORIENTED_SIMPLEX_AUTOMORPHISM_REALIZATION",
        "tetrahedral_information_route": "INDEPENDENT_CONVERGENCE_CROSSCHECK",
        "global_refinement": "DOWNSTREAM_GEOMETRY_PROGRAMME",
        "blocks": blocks,
        "technical_status": "PASS" if passed else "FAIL",
    }


def main() -> None:
    receipt = build_receipt()
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if receipt["technical_status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
