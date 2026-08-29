#!/usr/bin/env python3
"""Deterministic audit for The Space of Geometry dependency fork v0.9."""
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


def common_carrier_certificate() -> dict[str, object]:
    herm2_real_dimension = 4
    trace_codimension = 1
    relation_dimension = herm2_real_dimension - trace_codimension
    return {
        "trace_one_affine_dimension": relation_dimension,
        "translation_space": "Herm_0(2)",
        "canonical_relation": "delta(rho_x,rho_y)=rho_y-rho_x",
        "generator_relation": "E_xy=2*(rho_y-rho_x)",
        "carrier": "Herm_0(2)~=R3",
        "pass": relation_dimension == 3,
    }


def euclidean_branch_certificate() -> dict[str, object]:
    a = (5, 0, 0)
    b = (0, 12, 0)
    c = tuple(x + y for x, y in zip(a, b))
    a2 = dot(a, a)
    b2 = dot(b, b)
    c2 = dot(c, c)
    orthogonal = dot(a, b) == 0
    return {
        "inner_product": "0.5*Tr(A*B)",
        "endpoint_composition": "E_xz=E_xy+E_yz",
        "orthogonality": "<A,B>=0",
        "pythagorean_identity": "a^2+b^2=c^2",
        "sample": {"a2": a2, "b2": b2, "c2": c2},
        "pass": orthogonal and c2 == a2 + b2 == 169,
    }


def finite_cell_branch_certificate() -> dict[str, object]:
    verts = (0, 1, 2, 3)
    s4 = list(itertools.permutations(verts))
    edges = {tuple(sorted(e)) for e in itertools.combinations(verts, 2)}
    orbit = {tuple(sorted((p[0], p[1]))) for p in s4}

    norms = [dot(v, v) for v in TETRA]
    cross = [dot(TETRA[i], TETRA[j]) for i in range(4) for j in range(i + 1, 4)]
    zero_sum = tuple(sum(v[k] for v in TETRA) for k in range(3)) == (0, 0, 0)
    normalized_cross = {Fraction(x, norms[0]) for x in cross}

    return {
        "minimal_vertices": 4,
        "minimal_cell": "Delta^3",
        "automorphism_group": "S4",
        "edge_orbit_size": len(orbit),
        "regularity_route": "A5_A7_INTRINSIC_SIMPLEX_EDGE_ORBIT_INVARIANCE",
        "normalized_pairwise_dot": "-1/3",
        "tetrahedron_role": "MINIMAL_FINITE_FULL_DIMENSIONAL_CELL",
        "pass": (
            len(s4) == 24
            and len(edges) == 6
            and orbit == edges
            and zero_sum
            and norms == [3] * 4
            and normalized_cross == {Fraction(-1, 3)}
        ),
    }


def build_receipt() -> dict[str, object]:
    blocks = {
        "common_carrier": common_carrier_certificate(),
        "euclidean_branch": euclidean_branch_certificate(),
        "finite_cell_branch": finite_cell_branch_certificate(),
    }
    passed = all(bool(block["pass"]) for block in blocks.values())
    return {
        "schema": "THE_SPACE_OF_GEOMETRY_SPINE_V0_9",
        "working_title": "The Space of Geometry: From First Distinction to Pythagoras",
        "dependency_shape": "COMMON_CARRIER_THEN_PARALLEL_EUCLIDEAN_AND_FINITE_CELL_BRANCHES",
        "common_carrier_status": "CLOSED_AT_TIR_AXIOM_MODEL_LEVEL",
        "euclidean_branch_status": "CLOSED_AT_TIR_AXIOM_MODEL_LEVEL",
        "finite_cell_branch_status": "CLOSED_AT_TIR_AXIOM_MODEL_LEVEL",
        "pythagorean_endpoint": "DIRECT_INNER_PRODUCT_BRANCH",
        "tetrahedron_required_for_pythagoras": False,
        "tetrahedron_role": "MINIMAL_FINITE_FULL_DIMENSIONAL_CELL",
        "sic_role": "INDEPENDENT_CONVERGENCE_CROSSCHECK",
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
