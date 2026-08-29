#!/usr/bin/env python3
"""Deterministic audit for Local Euclidean and Pythagorean Closure v0.1."""
from __future__ import annotations

import json
import math


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def norm2(a):
    return dot(a, a)


def build_receipt() -> dict[str, object]:
    # Exact 3-4-5 orthogonal sample in the coefficient realization of Herm_0(2).
    a = (3, 0, 0)
    b = (0, 4, 0)
    c = add(a, b)
    orthogonal = dot(a, b) == 0
    pythagorean = norm2(c) == norm2(a) + norm2(b) == 25

    # General inner-product identity sample with non-orthogonal vectors.
    u = (1, 2, 3)
    v = (-2, 1, 4)
    cosine_identity = norm2(add(u, v)) == norm2(u) + norm2(v) + 2 * dot(u, v)

    # Regular tetrahedron edge-angle firewall.
    theta = math.acos(1.0 / 3.0)
    deficit_at_five = 5.0 * theta < 2.0 * math.pi
    excess_at_six = 6.0 * theta > 2.0 * math.pi

    blocks = {
        "orthogonal_sample": {
            "dot": dot(a, b),
            "a2": norm2(a),
            "b2": norm2(b),
            "c2": norm2(c),
            "orthogonal": orthogonal,
            "pythagorean": pythagorean,
            "pass": orthogonal and pythagorean,
        },
        "inner_product_identity": {
            "lhs": norm2(add(u, v)),
            "rhs": norm2(u) + norm2(v) + 2 * dot(u, v),
            "pass": cosine_identity,
        },
        "regular_tetrahedron_edge_angle": {
            "cos_dihedral": "1/3",
            "five_cells_leave_positive_deficit": deficit_at_five,
            "six_cells_produce_excess": excess_at_six,
            "status": "DEFICIT_AT_5_EXCESS_AT_6",
            "pass": deficit_at_five and excess_at_six,
        },
    }

    passed = all(bool(block["pass"]) for block in blocks.values())
    return {
        "schema": "TIR_SPACE_OF_GEOMETRY_LOCAL_EUCLIDEAN_PYTHAGOREAN_CLOSURE_V0_1",
        "endpoint": "PYTHAGOREAN_CLOSURE",
        "local_euclidean_closure": "EXACT_AFTER_SPATIAL_PROMOTION_AND_ADDITIVE_ENDPOINT_COMPOSITION",
        "regular_tetrahedron_role": "MINIMAL_LOCAL_ISOTROPIC_CELL",
        "global_regular_tetrahedron_gluing_status": "SEPARATE_DOWNSTREAM_REFINEMENT_PROBLEM",
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
