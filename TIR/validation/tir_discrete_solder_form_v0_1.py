#!/usr/bin/env python3
"""Deterministic audit for TIR Discrete Relational Solder Form v0.1."""
from __future__ import annotations

import json
import math

Matrix = tuple[tuple[complex, complex], tuple[complex, complex]]

I: Matrix = ((1 + 0j, 0j), (0j, 1 + 0j))
SX: Matrix = ((0j, 1 + 0j), (1 + 0j, 0j))
SY: Matrix = ((0j, -1j), (1j, 0j))
SZ: Matrix = ((1 + 0j, 0j), (0j, -1 + 0j))


def add(a: Matrix, b: Matrix) -> Matrix:
    return tuple(tuple(a[i][j] + b[i][j] for j in range(2)) for i in range(2))  # type: ignore[return-value]


def scale(c: complex, a: Matrix) -> Matrix:
    return tuple(tuple(c * a[i][j] for j in range(2)) for i in range(2))  # type: ignore[return-value]


def matmul(a: Matrix, b: Matrix) -> Matrix:
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)) for i in range(2))  # type: ignore[return-value]


def dagger(a: Matrix) -> Matrix:
    return ((a[0][0].conjugate(), a[1][0].conjugate()), (a[0][1].conjugate(), a[1][1].conjugate()))


def trace(a: Matrix) -> complex:
    return a[0][0] + a[1][1]


def mateq(a: Matrix, b: Matrix, tol: float = 1e-12) -> bool:
    return all(abs(a[i][j] - b[i][j]) <= tol for i in range(2) for j in range(2))


def edge_generator(v: tuple[float, float, float]) -> Matrix:
    x, y, z = v
    return add(add(scale(x, SX), scale(y, SY)), scale(z, SZ))


def edge_norm_sq(e: Matrix) -> float:
    value = 0.5 * trace(matmul(e, e))
    return float(value.real)


def conjugate(u: Matrix, a: Matrix) -> Matrix:
    return matmul(matmul(u, a), dagger(u))


def matrix_rank(vectors: list[list[float]], tol: float = 1e-12) -> int:
    m = [row[:] for row in vectors]
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
        p = m[rank][col]
        m[rank] = [value / p for value in m[rank]]
        for r in range(rows):
            if r == rank:
                continue
            f = m[r][col]
            m[r] = [m[r][c] - f * m[rank][c] for c in range(cols)]
        rank += 1
        col += 1
    return rank


def norm_certificate() -> dict[str, object]:
    rows = []
    passed = True
    for v in ((1.0, 0.0, 0.0), (0.0, 2.0, 0.0), (1.0, 2.0, 2.0)):
        e = edge_generator(v)
        lhs = edge_norm_sq(e)
        rhs = sum(x * x for x in v)
        ok = abs(lhs - rhs) <= 1e-12
        passed &= ok
        rows.append({"vector": list(v), "generator_norm_sq": lhs, "euclidean_norm_sq": rhs, "pass": ok})
    return {"rows": rows, "pass": passed}


def frame_covariance_certificate() -> dict[str, object]:
    theta = math.pi / 3
    c = math.cos(theta / 2)
    s = math.sin(theta / 2)
    u: Matrix = ((c - 1j * s, 0j), (0j, c + 1j * s))
    e = edge_generator((1.0, 2.0, 3.0))
    transformed = conjugate(u, e)
    return {
        "norm_before": edge_norm_sq(e),
        "norm_after": edge_norm_sq(transformed),
        "pass": abs(edge_norm_sq(e) - edge_norm_sq(transformed)) <= 1e-12,
    }


def reverse_edge_certificate() -> dict[str, object]:
    e_xy = edge_generator((1.0, -2.0, 0.5))
    e_yx = scale(-1, e_xy)
    expected_zero = ((0j, 0j), (0j, 0j))
    return {"pass": mateq(add(e_xy, e_yx), expected_zero)}


def triangle_closure_certificate() -> dict[str, object]:
    # Flat triangle: x=(0,0,0), y=(1,0,0), z=(1,1,0), trivial transport.
    e_xy = edge_generator((1.0, 0.0, 0.0))
    e_yz = edge_generator((0.0, 1.0, 0.0))
    e_zx = edge_generator((-1.0, -1.0, 0.0))
    closure = add(add(e_xy, e_yz), e_zx)
    zero = ((0j, 0j), (0j, 0j))
    holonomy = matmul(matmul(I, I), I)
    return {
        "closure_zero": mateq(closure, zero),
        "flat_holonomy_identity": mateq(holonomy, I),
        "pass": mateq(closure, zero) and mateq(holonomy, I),
    }


def local_rank_certificate() -> dict[str, object]:
    outgoing = [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
    rank = matrix_rank(outgoing)
    planar = matrix_rank([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [1.0, 1.0, 0.0]])
    return {"full_local_rank": rank, "planar_control_rank": planar, "pass": rank == 3 and planar == 2}


def build_receipt() -> dict[str, object]:
    blocks = {
        "edge_generator_norm": norm_certificate(),
        "su2_frame_covariance": frame_covariance_certificate(),
        "reverse_edge_orientation": reverse_edge_certificate(),
        "flat_triangle_torsion_holonomy": triangle_closure_certificate(),
        "local_generator_rank": local_rank_certificate(),
    }
    passed = all(block["pass"] for block in blocks.values())
    return {
        "schema": "TIR_DISCRETE_SOLDER_FORM_V0_1",
        "scope": "TIR_RELATIONAL_EDGE_TO_COFRAME_PRECURSOR_AUDIT",
        "internal_generator_space": "Herm_0(2)",
        "max_local_rank": 3,
        "continuum_limit_open": True,
        "torsion_free_selection_open": True,
        "next_gate": "DERIVE_RANK3_AND_TORSION_FREE_STABILITY_LAW",
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
