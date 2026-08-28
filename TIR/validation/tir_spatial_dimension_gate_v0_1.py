#!/usr/bin/env python3
"""Deterministic audit for TIR Spatial Dimension Gate v0.1.

This audit checks the exact conditional dimension arithmetic and an operational
Gram-rank dimension certificate on finite Euclidean metric samples. It does not
promote either open bridge Xi or rho_x to an established TIR theorem.
"""
from __future__ import annotations

import json
from typing import Sequence


def squared_distance(a: Sequence[float], b: Sequence[float]) -> float:
    return sum((x - y) ** 2 for x, y in zip(a, b))


def squared_distance_matrix(points: Sequence[Sequence[float]]) -> list[list[float]]:
    return [[squared_distance(a, b) for b in points] for a in points]


def matmul(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    rows = len(a)
    inner = len(b)
    cols = len(b[0])
    return [
        [sum(a[i][k] * b[k][j] for k in range(inner)) for j in range(cols)]
        for i in range(rows)
    ]


def centered_gram(delta: list[list[float]]) -> list[list[float]]:
    m = len(delta)
    j = [
        [(1.0 if r == c else 0.0) - 1.0 / m for c in range(m)]
        for r in range(m)
    ]
    jd = matmul(j, delta)
    jdj = matmul(jd, j)
    return [[-0.5 * value for value in row] for row in jdj]


def matrix_rank(a: list[list[float]], tol: float = 1e-10) -> int:
    m = [row[:] for row in a]
    rows = len(m)
    cols = len(m[0]) if rows else 0
    rank = 0
    col = 0
    while rank < rows and col < cols:
        pivot = max(range(rank, rows), key=lambda r: abs(m[r][col]))
        if abs(m[pivot][col]) <= tol:
            col += 1
            continue
        m[rank], m[pivot] = m[pivot], m[rank]
        pivot_value = m[rank][col]
        m[rank] = [value / pivot_value for value in m[rank]]
        for r in range(rows):
            if r == rank:
                continue
            factor = m[r][col]
            if abs(factor) <= tol:
                continue
            m[r] = [m[r][c] - factor * m[rank][c] for c in range(cols)]
        rank += 1
        col += 1
    return rank


def gram_rank(points: Sequence[Sequence[float]]) -> int:
    return matrix_rank(centered_gram(squared_distance_matrix(points)))


def build_receipt() -> dict[str, object]:
    bloch_boundary_dimension = 2
    boundary_route_bulk_dimension = bloch_boundary_dimension + 1
    so3_defining_real_rep_dimension = 3

    tetrahedral_local_sample = (
        (0.0, 0.0, 0.0),
        (1.0, 0.0, 0.0),
        (0.0, 1.0, 0.0),
        (0.0, 0.0, 1.0),
    )
    planar_control = (
        (0.0, 0.0, 0.0),
        (1.0, 0.0, 0.0),
        (0.0, 1.0, 0.0),
        (1.0, 1.0, 0.0),
    )

    rank_3 = gram_rank(tetrahedral_local_sample)
    rank_2 = gram_rank(planar_control)

    route_a_pass = boundary_route_bulk_dimension == 3
    route_b_pass = so3_defining_real_rep_dimension == 3
    routes_converge = boundary_route_bulk_dimension == so3_defining_real_rep_dimension == 3
    rank_pass = rank_3 == 3 and rank_2 == 2

    passed = route_a_pass and route_b_pass and routes_converge and rank_pass

    return {
        "schema": "TIR_SPATIAL_DIMENSION_GATE_V0_1",
        "scope": "TIR_CONDITIONAL_SPATIAL_DIMENSION_AUDIT",
        "boundary_route": {
            "bloch_sphere_dimension": bloch_boundary_dimension,
            "boundary_rule": "dim(boundary(B^n))=n-1",
            "conditional_bulk_dimension": boundary_route_bulk_dimension,
            "bridge_required": "Xi:S2_Bloch->S^(n-1)_space homeomorphism",
            "pass": route_a_pass,
        },
        "symmetry_route": {
            "standard_projective_symmetry": "PSU(2)~=SO(3)",
            "defining_real_representation_dimension": so3_defining_real_rep_dimension,
            "conditional_spatial_dimension": so3_defining_real_rep_dimension,
            "bridge_required": "rho_x:projective symmetry->defining tangent isotropy",
            "pass": route_b_pass,
        },
        "relational_metric_dimension_audit": {
            "generic_tetrahedral_sample_gram_rank": rank_3,
            "planar_control_gram_rank": rank_2,
            "pass": rank_pass,
        },
        "conditional_dimension": 3,
        "routes_converge": routes_converge,
        "unconditional_dimension_derived": False,
        "open_bridges": ["Xi", "rho_x"],
        "next_gate": "DERIVE_SPATIAL_STATE_GEOMETRY_BRIDGE",
        "technical_status": "PASS" if passed else "FAIL",
    }


def main() -> None:
    receipt = build_receipt()
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if receipt["technical_status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
