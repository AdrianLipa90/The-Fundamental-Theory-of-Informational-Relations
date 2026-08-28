#!/usr/bin/env python3
"""Deterministic audit for TIR Rank-3 Isotropy Stabilization v0.1."""
from __future__ import annotations

import json

Matrix = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]
Vector = tuple[int, int, int]

I3: Matrix = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
RX90: Matrix = ((1, 0, 0), (0, 0, -1), (0, 1, 0))
RY90: Matrix = ((0, 0, 1), (0, 1, 0), (-1, 0, 0))
RZ90: Matrix = ((0, -1, 0), (1, 0, 0), (0, 0, 1))


def matmul(a: Matrix, b: Matrix) -> Matrix:
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )  # type: ignore[return-value]


def transpose(a: Matrix) -> Matrix:
    return tuple(tuple(a[j][i] for j in range(3)) for i in range(3))  # type: ignore[return-value]


def det3(a: Matrix) -> int:
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def apply(a: Matrix, v: Vector) -> Vector:
    return tuple(sum(a[i][j] * v[j] for j in range(3)) for i in range(3))  # type: ignore[return-value]


def rank3(v1: Vector, v2: Vector, v3: Vector) -> int:
    m: Matrix = (
        (v1[0], v2[0], v3[0]),
        (v1[1], v2[1], v3[1]),
        (v1[2], v2[2], v3[2]),
    )
    if det3(m) != 0:
        return 3
    nonzero = [v for v in (v1, v2, v3) if v != (0, 0, 0)]
    if not nonzero:
        return 0
    a = nonzero[0]
    for b in nonzero[1:]:
        cross = (
            a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0],
        )
        if cross != (0, 0, 0):
            return 2
    return 1


def rotation_certificate() -> dict[str, object]:
    rows = []
    passed = True
    for name, r in (("Rx90", RX90), ("Ry90", RY90), ("Rz90", RZ90)):
        ortho = matmul(transpose(r), r) == I3
        det_one = det3(r) == 1
        row_pass = ortho and det_one
        passed &= row_pass
        rows.append({"rotation": name, "orthogonal": ortho, "determinant": det3(r), "pass": row_pass})
    return {"rows": rows, "pass": passed}


def full_orbit_rank_certificate() -> dict[str, object]:
    seeds = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 2, 3))
    rows = []
    passed = True
    for seed in seeds:
        orbit = (seed, apply(RX90, seed), apply(RY90, seed), apply(RZ90, seed))
        best = 0
        triples = (
            (orbit[0], orbit[1], orbit[2]),
            (orbit[0], orbit[1], orbit[3]),
            (orbit[0], orbit[2], orbit[3]),
            (orbit[1], orbit[2], orbit[3]),
        )
        for tri in triples:
            best = max(best, rank3(*tri))
        row_pass = best == 3
        passed &= row_pass
        rows.append({"seed": seed, "generated_span_rank": best, "pass": row_pass})
    return {"rows": rows, "pass": passed}


def proper_coordinate_subspace_breaking_certificate() -> dict[str, object]:
    # Axis <e1> is broken by Rz90; plane <e1,e2> is broken by Ry90 because e1 -> -e3.
    axis_image = apply(RZ90, (1, 0, 0))
    plane_image = apply(RY90, (1, 0, 0))
    axis_broken = axis_image not in ((1, 0, 0), (-1, 0, 0), (0, 0, 0))
    plane_broken = plane_image[2] != 0
    return {
        "axis_image": axis_image,
        "plane_image": plane_image,
        "rank1_full_isotropy_broken": axis_broken,
        "rank2_full_isotropy_broken": plane_broken,
        "pass": axis_broken and plane_broken,
    }


def build_receipt() -> dict[str, object]:
    blocks = {
        "so3_rotation_generators": rotation_certificate(),
        "nonzero_seed_orbits_generate_rank3_samples": full_orbit_rank_certificate(),
        "proper_coordinate_subspaces_fail_full_isotropy": proper_coordinate_subspace_breaking_certificate(),
    }
    passed = all(bool(block["pass"]) for block in blocks.values())
    return {
        "schema": "TIR_RANK3_ISOTROPY_STABILIZATION_V0_1",
        "scope": "TIR_CONDITIONAL_SO3_IRREDUCIBILITY_AUDIT",
        "theorem_dependency": "standard irreducibility of defining real SO(3) representation",
        "conditional_result": "NONZERO_FULL_SO3_INVARIANT_LOCAL_EDGE_SPAN_HAS_RANK_3",
        "primitive_law_gate": "UNBROKEN_FULL_LOCAL_ADJOINT_SO3_ISOTROPY",
        "unconditional_spatial_rank_derived": False,
        "rank3_under_declared_isotropy": passed,
        "next_gate": "RELATIONAL_ENDPOINT_CLOSURE_TO_TORSION_FREE_LIMIT",
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
