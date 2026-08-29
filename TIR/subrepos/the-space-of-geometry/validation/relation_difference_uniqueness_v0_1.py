#!/usr/bin/env python3
"""Exact deterministic audit for relation-difference uniqueness v0.1."""
from __future__ import annotations

from fractions import Fraction
import json


Matrix = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]

RZ90: Matrix = (
    (0, -1, 0),
    (1, 0, 0),
    (0, 0, 1),
)
RX90: Matrix = (
    (1, 0, 0),
    (0, 0, -1),
    (0, 1, 0),
)


def commutator_constraint_rows(r: Matrix) -> list[list[Fraction]]:
    """Linear equations for M R - R M = 0, unknowns M_ij in row-major order."""
    rows: list[list[Fraction]] = []
    for i in range(3):
        for j in range(3):
            row = [Fraction(0) for _ in range(9)]
            # (M R)_ij = sum_k M_ik R_kj
            for k in range(3):
                row[3 * i + k] += Fraction(r[k][j])
            # (R M)_ij = sum_k R_ik M_kj
            for k in range(3):
                row[3 * k + j] -= Fraction(r[i][k])
            rows.append(row)
    return rows


def rank_q(rows: list[list[Fraction]]) -> int:
    a = [row[:] for row in rows]
    if not a:
        return 0
    m, n = len(a), len(a[0])
    rank = 0
    col = 0
    while rank < m and col < n:
        pivot = next((r for r in range(rank, m) if a[r][col] != 0), None)
        if pivot is None:
            col += 1
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        p = a[rank][col]
        a[rank] = [x / p for x in a[rank]]
        for r in range(m):
            if r == rank:
                continue
            f = a[r][col]
            if f != 0:
                a[r] = [x - f * y for x, y in zip(a[r], a[rank])]
        rank += 1
        col += 1
    return rank


def sub(a: tuple[int, int, int], b: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(x - y for x, y in zip(a, b))  # type: ignore[return-value]


def add(a: tuple[int, int, int], b: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(x + y for x, y in zip(a, b))  # type: ignore[return-value]


def scale(c: int, a: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(c * x for x in a)  # type: ignore[return-value]


def dot(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
    return sum(x * y for x, y in zip(a, b))


def build_receipt() -> dict[str, object]:
    constraints = commutator_constraint_rows(RZ90) + commutator_constraint_rows(RX90)
    rank = rank_q(constraints)
    nullity = 9 - rank

    # Exact affine-difference control in integer Bloch-coordinate units.
    rx = (1, 2, -1)
    ry = (3, -1, 2)
    rz = (-2, 4, 5)
    c = 2
    exy = scale(c, sub(ry, rx))
    eyz = scale(c, sub(rz, ry))
    exz = scale(c, sub(rz, rx))

    additive = add(exy, eyz) == exz
    reversal = scale(-1, exy) == scale(c, sub(rx, ry))
    nondegenerate = exy != (0, 0, 0)
    hs_bloch_norm_control = dot(exy, exy) == 4 * dot(sub(ry, rx), sub(ry, rx))

    # Two independent 90-degree rotations generate enough constraints here to leave
    # a one-dimensional commutant, i.e. scalar multiples of I_3.
    commutant_scalar_only = nullity == 1

    passed = all((additive, reversal, nondegenerate, hs_bloch_norm_control, commutant_scalar_only))

    return {
        "schema": "TIR_RELATION_DIFFERENCE_UNIQUENESS_V0_1",
        "technical_status": "PASS" if passed else "FAIL",
        "relation_space": "Herm_0(2)~=R3",
        "structural_form": "R(rho_x,rho_y)=c*(rho_y-rho_x)",
        "normalization": "c=2_FOR_BLOCH_COORDINATE_GENERATOR",
        "commutant_constraint_rank": rank,
        "commutant_dimension": nullity,
        "commutant_scalar_only": commutant_scalar_only,
        "endpoint_composition_exact": additive,
        "reversal_exact": reversal,
        "nondegenerate_control": nondegenerate,
        "hs_bloch_norm_control": hs_bloch_norm_control,
        "remaining_foundational_bundle": "SOURCE_CLOSED_COMPOSITIONAL_COVARIANT_PRIMITIVE_RELATION",
        "promotion_status": "UNIQUE_UP_TO_SCALE_IF_BRIDGE_PROPERTIES_ADMITTED",
    }


def main() -> None:
    receipt = build_receipt()
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if receipt["technical_status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
