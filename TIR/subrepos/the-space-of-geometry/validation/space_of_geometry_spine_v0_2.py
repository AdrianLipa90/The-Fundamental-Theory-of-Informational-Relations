#!/usr/bin/env python3
"""Deterministic audit for The Space of Geometry research spine v0.2."""
from __future__ import annotations

import json

TETRA = (
    (1, 1, 1),
    (1, -1, -1),
    (-1, 1, -1),
    (-1, -1, 1),
)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def rank3_tetra_certificate() -> dict[str, object]:
    norms = [dot(v, v) for v in TETRA]
    cross = [dot(TETRA[i], TETRA[j]) for i in range(4) for j in range(i + 1, 4)]
    zero_sum = tuple(sum(v[k] for v in TETRA) for k in range(3)) == (0, 0, 0)
    passed = zero_sum and norms == [3] * 4 and cross == [-1] * 6
    return {
        "carrier_dimension": 3,
        "minimal_simplex_vertices": 4,
        "simplex": "Delta^3",
        "tetrahedral_zero_sum": zero_sum,
        "normalized_pairwise_dot": "-1/3",
        "pass": passed,
    }


def pythagorean_certificate() -> dict[str, object]:
    a = (5, 0, 0)
    b = (0, 12, 0)
    c = tuple(x + y for x, y in zip(a, b))
    a2, b2, c2 = dot(a, a), dot(b, b), dot(c, c)
    passed = dot(a, b) == 0 and c2 == a2 + b2 == 169
    return {
        "orthogonal_inner_product": dot(a, b),
        "a_squared": a2,
        "b_squared": b2,
        "c_squared": c2,
        "pass": passed,
    }


def build_receipt() -> dict[str, object]:
    blocks = {
        "minimal_tetrahedral_geometry": rank3_tetra_certificate(),
        "pythagorean_endpoint": pythagorean_certificate(),
    }
    passed = all(bool(block["pass"]) for block in blocks.values())
    return {
        "schema": "THE_SPACE_OF_GEOMETRY_SPINE_V0_2",
        "working_title": "The Space of Geometry: From First Distinction to Pythagoras",
        "endpoint": "PYTHAGOREAN_CLOSURE",
        "promotion_theorem_status": "CONDITIONAL_UNIQUENESS_UP_TO_ORTHOGONAL_EQUIVALENCE_AND_SCALE",
        "core_open_gate": "DERIVE_SPATIAL_REALIZATION_CRITERION_FROM_TIR_AXIOMS",
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
