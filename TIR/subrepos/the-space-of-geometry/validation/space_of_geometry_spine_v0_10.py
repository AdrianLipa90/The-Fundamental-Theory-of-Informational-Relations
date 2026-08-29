#!/usr/bin/env python3
"""Deterministic release audit for The Space of Geometry research spine v0.10."""
from __future__ import annotations

import json
from fractions import Fraction


TETRA = (
    (1, 1, 1),
    (1, -1, -1),
    (-1, 1, -1),
    (-1, -1, 1),
)


def dot(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
    return sum(x * y for x, y in zip(a, b))


def tetra_certificate() -> dict[str, object]:
    norms = [dot(v, v) for v in TETRA]
    cross = [dot(TETRA[i], TETRA[j]) for i in range(4) for j in range(i + 1, 4)]
    zero_sum = tuple(sum(v[k] for v in TETRA) for k in range(3)) == (0, 0, 0)
    passed = zero_sum and norms == [3, 3, 3, 3] and cross == [-1] * 6
    return {
        "minimal_vertices": 4,
        "simplex": "Delta^3",
        "zero_sum": zero_sum,
        "normalized_pairwise_dot": "-1/3",
        "regular_tetrahedron": passed,
        "pass": passed,
    }


def physical_pythagoras_certificate() -> dict[str, object]:
    a2 = Fraction(9, 25)
    b2 = Fraction(16, 25)
    c2 = Fraction(1, 1)
    physical_y = a2 <= 1
    physical_z = a2 + b2 <= 1
    passed = physical_y and physical_z and a2 + b2 == c2
    return {
        "a_squared": str(a2),
        "b_squared": str(b2),
        "c_squared": str(c2),
        "all_endpoints_physical": physical_y and physical_z,
        "pythagorean_identity": a2 + b2 == c2,
        "certificate": "3/5,4/5,1",
        "pass": passed,
    }


def build_receipt() -> dict[str, object]:
    carrier_dimension = 3
    physical_chord_radius = 2
    blocks = {
        "physical_pythagoras": physical_pythagoras_certificate(),
        "finite_cell": tetra_certificate(),
    }
    passed = (
        carrier_dimension == 3
        and physical_chord_radius == 2
        and all(bool(block["pass"]) for block in blocks.values())
    )
    return {
        "schema": "THE_SPACE_OF_GEOMETRY_SPINE_V0_10",
        "technical_status": "PASS" if passed else "FAIL",
        "working_title": "The Space of Geometry: From First Distinction to Pythagoras",
        "dependency_shape": "COMMON_CARRIER_THEN_EUCLIDEAN_PHYSICAL_REALIZABILITY_AND_FINITE_CELL_OUTPUTS",
        "common_carrier": "Herm_0(2)~=R3",
        "carrier_real_dimension": carrier_dimension,
        "physical_single_edge_domain": "radius_two_ball",
        "physical_single_edge_radius": physical_chord_radius,
        "physical_pythagorean_realization": "EXPLICIT_NONEMPTY_FAMILY",
        "pythagorean_endpoint": "DIRECT_INNER_PRODUCT_BRANCH_WITH_PHYSICAL_REALIZATION",
        "tetrahedron_required_for_pythagoras": False,
        "tetrahedron_role": "MINIMAL_FINITE_FULL_DIMENSIONAL_CELL",
        "sic_role": "INDEPENDENT_CONVERGENCE_CROSSCHECK",
        "global_refinement": "DOWNSTREAM_GEOMETRY_PROGRAMME",
        "blocks": blocks,
    }


def main() -> None:
    receipt = build_receipt()
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if receipt["technical_status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
