#!/usr/bin/env python3
"""Deterministic audit for The Space of Geometry research spine v0.1."""
from __future__ import annotations

import json


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
        "zero_mean": zero_sum,
        "norm_squared": norms,
        "cross_dots": cross,
        "normalized_pairwise_dot": "-1/3",
        "regular_tetrahedron": passed,
        "pass": passed,
    }


def dimension_certificate() -> dict[str, object]:
    # Herm_0(2) is the real span of the three Pauli matrices.
    herm0_real_dimension = 3
    simplex_vertices = herm0_real_dimension + 1
    return {
        "herm0_2_real_dimension": herm0_real_dimension,
        "minimal_full_dimensional_simplex_vertices": simplex_vertices,
        "simplex": "Delta^3",
        "pass": simplex_vertices == 4,
    }


def pythagoras_certificate() -> dict[str, object]:
    # Exact integer orthogonal control in R^3.
    a = (3, 0, 0)
    b = (0, 4, 0)
    c = tuple(x + y for x, y in zip(a, b))
    aa = dot(a, a)
    bb = dot(b, b)
    cc = dot(c, c)
    orthogonal = dot(a, b) == 0
    passed = orthogonal and cc == aa + bb and (aa, bb, cc) == (9, 16, 25)
    return {
        "orthogonal": orthogonal,
        "a_squared": aa,
        "b_squared": bb,
        "c_squared": cc,
        "pythagorean_identity": cc == aa + bb,
        "pass": passed,
    }


def build_receipt() -> dict[str, object]:
    blocks = {
        "dimension_to_simplex": dimension_certificate(),
        "regular_tetrahedral_cell": tetra_certificate(),
        "pythagorean_closure": pythagoras_certificate(),
    }
    passed = all(bool(block["pass"]) for block in blocks.values())
    return {
        "schema": "THE_SPACE_OF_GEOMETRY_SPINE_V0_1",
        "subrepo": "TIR/subrepos/the-space-of-geometry",
        "working_title": "The Space of Geometry: From First Distinction to Pythagoras",
        "endpoint": "PYTHAGOREAN_CLOSURE",
        "spatial_promotion_derived": False,
        "continuum_refinement_derived": False,
        "tetrahedral_information_space_identification_derived": False,
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
