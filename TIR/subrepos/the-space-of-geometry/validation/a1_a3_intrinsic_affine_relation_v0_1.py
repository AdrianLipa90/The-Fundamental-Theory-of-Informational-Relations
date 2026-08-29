#!/usr/bin/env python3
"""Deterministic audit for the A1+A3 intrinsic affine relation candidate."""
from __future__ import annotations

import json
from fractions import Fraction as F

Vec = tuple[F, F, F]
Mat = tuple[Vec, Vec, Vec]


def add(a: Vec, b: Vec) -> Vec:
    return tuple(x + y for x, y in zip(a, b))  # type: ignore[return-value]


def sub(a: Vec, b: Vec) -> Vec:
    return tuple(x - y for x, y in zip(a, b))  # type: ignore[return-value]


def scale(c: F, v: Vec) -> Vec:
    return tuple(c * x for x in v)  # type: ignore[return-value]


def mv(m: Mat, v: Vec) -> Vec:
    return tuple(sum((row[j] * v[j] for j in range(3)), F(0)) for row in m)  # type: ignore[return-value]


def relation(x: Vec, y: Vec, c: F) -> Vec:
    return scale(c, sub(y, x))


def main() -> None:
    x: Vec = (F(1, 3), F(-1, 5), F(2, 7))
    y: Vec = (F(-2, 9), F(3, 8), F(1, 6))
    a: Vec = (F(5, 11), F(-4, 13), F(7, 17))
    c = F(7, 5)

    # Invertible integer frame change with determinant 1.
    L: Mat = (
        (F(1), F(1), F(0)),
        (F(0), F(1), F(1)),
        (F(0), F(0), F(1)),
    )

    translation_naturality = relation(add(x, a), add(y, a), c) == relation(x, y, c)
    linear_naturality = relation(mv(L, x), mv(L, y), c) == mv(L, relation(x, y, c))
    reversal = relation(y, x, c) == scale(F(-1), relation(x, y, c))

    z: Vec = (F(4, 15), F(-1, 9), F(5, 12))
    endpoint = add(relation(x, y, c), relation(y, z, c)) == relation(x, z, c)
    distinction_preserved = c != 0 and relation(x, y, c) != (F(0), F(0), F(0))

    passed = all([translation_naturality, linear_naturality, reversal, endpoint, distinction_preserved])
    receipt = {
        "schema": "TIR_A1_A3_INTRINSIC_AFFINE_RELATION_V0_1",
        "technical_status": "PASS" if passed else "FAIL",
        "exact_family": "R(x,y)=c*(y-x)",
        "translation_naturality": translation_naturality,
        "GL_frame_naturality_sample": linear_naturality,
        "reversal": reversal,
        "endpoint_composition": endpoint,
        "distinction_preservation": distinction_preserved,
        "uniqueness_status": "EXACT_UNDER_CONTINUOUS_INTRINSIC_AFFINE_NATURALITY",
        "remaining_tir_gate": "A1_A3_SELECT_INTRINSIC_AFFINE_NATURALITY",
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
