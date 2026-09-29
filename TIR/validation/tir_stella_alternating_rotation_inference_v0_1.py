#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations, product

Matrix = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]
Vec = tuple[int, int, int]

I3: Matrix = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
TETRA: tuple[Vec, ...] = (
    (1, 1, 1),
    (1, -1, -1),
    (-1, 1, -1),
    (-1, -1, 1),
)
R_PLUS: Matrix = ((0, -1, 0), (1, 0, 0), (0, 0, 1))
R_MINUS: Matrix = ((1, 0, 0), (0, 0, -1), (0, 1, 0))


def matmul(A: Matrix, B: Matrix) -> Matrix:
    return tuple(
        tuple(sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )  # type: ignore[return-value]


def matvec(A: Matrix, v: Vec) -> Vec:
    return tuple(sum(A[i][k] * v[k] for k in range(3)) for i in range(3))  # type: ignore[return-value]


def det(A: Matrix) -> int:
    return (
        A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
        - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
        + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0])
    )


def tetrahedral_rotations() -> tuple[Matrix, ...]:
    out: list[Matrix] = []
    target = set(TETRA)
    for p in permutations(range(3)):
        for s in product((1, -1), repeat=3):
            A: Matrix = tuple(
                tuple(s[i] if p[i] == j else 0 for j in range(3))
                for i in range(3)
            )  # type: ignore[assignment]
            if det(A) == 1 and {matvec(A, v) for v in TETRA} == target:
                out.append(A)
    if len(out) != 12:
        raise AssertionError(f"expected 12 tetrahedral rotations, got {len(out)}")
    return tuple(out)


A4 = tetrahedral_rotations()


def cross_overlap_signature(A: Matrix, B: Matrix) -> tuple[Fraction, ...]:
    vals: list[Fraction] = []
    for vi in TETRA:
        p = matvec(A, vi)
        for vj in TETRA:
            q = matvec(B, vj)
            vals.append(Fraction(-sum(p[k] * q[k] for k in range(3)), 3))
    return tuple(sorted(vals))


@dataclass(frozen=True)
class AlternatingStellaState:
    coarse: int
    sector: int
    plus: Matrix = I3
    minus: Matrix = I3

    def __post_init__(self) -> None:
        if self.coarse < 0 or self.sector not in (0, 1):
            raise ValueError("state must lie in N_0 x Z_2 with two orientation lifts")


def half_step(x: AlternatingStellaState) -> AlternatingStellaState:
    if x.sector == 0:
        return AlternatingStellaState(
            x.coarse, 1, matmul(R_PLUS, x.plus), x.minus
        )
    return AlternatingStellaState(
        x.coarse + 1, 0, x.plus, matmul(R_MINUS, x.minus)
    )


def full_successor(x: AlternatingStellaState) -> AlternatingStellaState:
    return AlternatingStellaState(
        x.coarse + 1,
        x.sector,
        matmul(R_PLUS, x.plus),
        matmul(R_MINUS, x.minus),
    )


def validate() -> dict[str, object]:
    for sector in (0, 1):
        x = AlternatingStellaState(0, sector)
        assert half_step(half_step(x)) == full_successor(x)

    x0 = AlternatingStellaState(0, 0)
    sig0 = cross_overlap_signature(x0.plus, x0.minus)
    x1 = half_step(x0)
    sig1 = cross_overlap_signature(x1.plus, x1.minus)

    # Concrete witness that a non-tetrahedral quarter-turn changes the
    # relational signature, without promoting this witness to a universal law.
    assert sig1 != sig0

    # Independent tetrahedral relabelings only permute rows/columns and
    # therefore preserve the unordered overlap signature.
    for a in A4:
        for b in A4:
            assert (
                cross_overlap_signature(
                    matmul(x1.plus, a),
                    matmul(x1.minus, b),
                )
                == sig1
            )

    return {
        "schema": "TIR_STELLA_ALTERNATING_ROTATION_INFERENCE_V0_1",
        "status": "PASS",
        "tetrahedral_rotation_group_order": len(A4),
        "half_step_square_equals_decorated_successor": True,
        "label_gauge_signature_invariant": True,
        "alternating_transform_changes_relational_signature_in_witness": True,
        "physical_time_assumed": False,
        "physical_space_assumed": False,
        "canon_allowed": False,
    }


if __name__ == "__main__":
    import json

    print(json.dumps(validate(), sort_keys=True))
