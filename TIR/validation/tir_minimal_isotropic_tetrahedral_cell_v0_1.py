#!/usr/bin/env python3
"""Deterministic audit for TIR Minimal Isotropic Tetrahedral Cell v0.1."""
from __future__ import annotations

import json

Vector = tuple[int, int, int]

TETRA: tuple[Vector, ...] = (
    (1, 1, 1),
    (1, -1, -1),
    (-1, 1, -1),
    (-1, -1, 1),
)

ORTHO_TRIAD: tuple[Vector, ...] = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
)

PLANAR_ZERO_SUM: tuple[Vector, ...] = (
    (1, 0, 0),
    (0, 1, 0),
    (-1, -1, 0),
)


def dot(a: Vector, b: Vector) -> int:
    return sum(x * y for x, y in zip(a, b))


def vecsum(vs: tuple[Vector, ...]) -> Vector:
    return tuple(sum(v[i] for v in vs) for i in range(3))  # type: ignore[return-value]


def second_moment(vs: tuple[Vector, ...]) -> tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]:
    return tuple(
        tuple(sum(v[i] * v[j] for v in vs) for j in range(3))
        for i in range(3)
    )  # type: ignore[return-value]


def det3_from_columns(a: Vector, b: Vector, c: Vector) -> int:
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - b[0] * (a[1] * c[2] - a[2] * c[1])
        + c[0] * (a[1] * b[2] - a[2] * b[1])
    )


def span_rank(vs: tuple[Vector, ...]) -> int:
    nonzero = tuple(v for v in vs if v != (0, 0, 0))
    if not nonzero:
        return 0
    n = len(nonzero)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if det3_from_columns(nonzero[i], nonzero[j], nonzero[k]) != 0:
                    return 3
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


def tetrahedral_certificate() -> dict[str, object]:
    norms = [dot(v, v) for v in TETRA]
    off_diag = [dot(TETRA[i], TETRA[j]) for i in range(4) for j in range(i + 1, 4)]
    moment = second_moment(TETRA)
    zero_mean = vecsum(TETRA) == (0, 0, 0)
    equal_norm = norms == [3, 3, 3, 3]
    regular_angles = off_diag == [-1] * 6
    isotropic_second_moment = moment == ((4, 0, 0), (0, 4, 0), (0, 0, 4))
    rank = span_rank(TETRA)
    passed = zero_mean and equal_norm and regular_angles and isotropic_second_moment and rank == 3
    return {
        "sum": vecsum(TETRA),
        "norm_squared": norms,
        "off_diagonal_dots": off_diag,
        "second_moment": moment,
        "span_rank": rank,
        "pass": passed,
    }


def three_relation_obstruction_certificate() -> dict[str, object]:
    # Any three vectors whose sum is zero satisfy v3=-(v1+v2), so their span has rank <=2.
    sample_rank = span_rank(PLANAR_ZERO_SUM)
    logical_identity = vecsum(PLANAR_ZERO_SUM) == (0, 0, 0)
    passed = logical_identity and sample_rank == 2
    return {
        "sample": PLANAR_ZERO_SUM,
        "sample_sum": vecsum(PLANAR_ZERO_SUM),
        "sample_rank": sample_rank,
        "general_reason": "v1+v2+v3=0 implies v3 is in span(v1,v2), hence rank<=2",
        "pass": passed,
    }


def moment_condition_independence_certificate() -> dict[str, object]:
    # Orthogonal triad has isotropic second moment I but nonzero first moment.
    ortho_moment = second_moment(ORTHO_TRIAD)
    ortho_sum = vecsum(ORTHO_TRIAD)
    # Planar zero-sum sample has vanishing first moment but rank-deficient anisotropic second moment.
    planar_moment = second_moment(PLANAR_ZERO_SUM)
    planar_sum = vecsum(PLANAR_ZERO_SUM)
    passed = (
        ortho_moment == ((1, 0, 0), (0, 1, 0), (0, 0, 1))
        and ortho_sum != (0, 0, 0)
        and planar_sum == (0, 0, 0)
        and span_rank(PLANAR_ZERO_SUM) == 2
        and planar_moment != ((2, 0, 0), (0, 2, 0), (0, 0, 2))
    )
    return {
        "orthogonal_triad_sum": ortho_sum,
        "orthogonal_triad_second_moment": ortho_moment,
        "planar_zero_sum": planar_sum,
        "planar_second_moment": planar_moment,
        "pass": passed,
    }


def gram_certificate() -> dict[str, object]:
    gram = [[dot(a, b) for b in TETRA] for a in TETRA]
    target = [[3 if i == j else -1 for j in range(4)] for i in range(4)]
    passed = gram == target
    return {
        "unnormalized_gram": gram,
        "normalized_diagonal": "1",
        "normalized_off_diagonal": "-1/3",
        "pass": passed,
    }


def build_receipt() -> dict[str, object]:
    blocks = {
        "exact_tetrahedral_realization": tetrahedral_certificate(),
        "three_relation_zero_mean_rank_obstruction": three_relation_obstruction_certificate(),
        "first_and_second_moment_conditions_are_independent": moment_condition_independence_certificate(),
        "regular_tetrahedral_gram_matrix": gram_certificate(),
    }
    passed = all(bool(block["pass"]) for block in blocks.values())
    return {
        "schema": "TIR_MINIMAL_ISOTROPIC_TETRAHEDRAL_CELL_V0_1",
        "scope": "TIR_EQUAL_WEIGHT_LOCAL_ISOTROPY_AUDIT",
        "conditional_result": "MINIMAL_ZERO_MEAN_FULL_SECOND_MOMENT_ISOTROPY_CELL_IS_TETRAHEDRAL",
        "minimal_valence": 4,
        "local_rank": 3,
        "normalized_pairwise_dot": "-1/3",
        "stability_functional_status": "DIAGNOSTIC_CANDIDATE_NOT_FUNDAMENTAL_ACTION",
        "continuum_gluing_derived": False,
        "next_gate": "AXIOMATIC_SELECTION_OF_ZERO_DEFECT_ISOTROPY_CLOSURE_SECTOR",
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
