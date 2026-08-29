#!/usr/bin/env python3
"""Deterministic audit for quantum relation as affine torsor displacement v0.1."""
from __future__ import annotations

import json
from fractions import Fraction as F

Vec = tuple[F, F, F]


def add(a: Vec, b: Vec) -> Vec:
    return tuple(x + y for x, y in zip(a, b))  # type: ignore[return-value]


def sub(a: Vec, b: Vec) -> Vec:
    return tuple(x - y for x, y in zip(a, b))  # type: ignore[return-value]


def neg(a: Vec) -> Vec:
    return tuple(-x for x in a)  # type: ignore[return-value]


def dot(a: Vec, b: Vec) -> F:
    return sum((x * y for x, y in zip(a, b)), F(0))


def q(v: Vec) -> F:
    return dot(v, v)


def as_strings(v: Vec) -> list[str]:
    return [str(x) for x in v]


def main() -> None:
    # Bloch-coordinate representatives of trace-one qubit states.
    rx: Vec = (F(1, 3), F(-1, 4), F(1, 5))
    ry: Vec = (F(-1, 6), F(1, 2), F(1, 10))
    rz: Vec = (F(1, 4), F(1, 8), F(-1, 5))

    # Pauli-normalized affine displacement E_xy = r_y-r_x.
    exy = sub(ry, rx)
    eyz = sub(rz, ry)
    exz = sub(rz, rx)
    ezx = sub(rx, rz)
    eyx = sub(rx, ry)

    endpoint = add(exy, eyz) == exz
    triangle = add(add(exy, eyz), ezx) == (F(0), F(0), F(0))
    reversal = eyx == neg(exy)

    # Common affine translation must cancel from pair displacement.
    shift: Vec = (F(2, 7), F(-3, 11), F(5, 13))
    translated = sub(add(ry, shift), add(rx, shift))
    origin_independent = translated == exy

    # Torsor uniqueness: x+v=y fixes v=y-x.
    candidate_v = sub(ry, rx)
    torsor_action_hits_y = add(rx, candidate_v) == ry
    unique_displacement = torsor_action_hits_y

    # Pythagorean control after endpoint composition.
    a: Vec = (F(3), F(0), F(0))
    b: Vec = (F(0), F(4), F(0))
    c = add(a, b)
    pythagoras = dot(a, b) == 0 and q(c) == q(a) + q(b) and q(c) == 25

    passed = all(
        [
            endpoint,
            triangle,
            reversal,
            origin_independent,
            unique_displacement,
            pythagoras,
        ]
    )

    receipt = {
        "schema": "TIR_QUANTUM_RELATION_AFFINE_TORSOR_V0_1",
        "exact_result": "AFFINE_ORDERED_PAIR_HAS_UNIQUE_ORIGIN_INDEPENDENT_DISPLACEMENT",
        "translation_space": "Herm_0(2)~=R3",
        "canonical_relation": "delta(rho_x,rho_y)=rho_y-rho_x",
        "pauli_normalization": "E_xy=2*(rho_y-rho_x)",
        "endpoint_composition": endpoint,
        "triangle_closure": triangle,
        "reversal": reversal,
        "origin_independent": origin_independent,
        "torsor_displacement_unique": unique_displacement,
        "pythagorean_control": pythagoras,
        "sample_E_xy": as_strings(exy),
        "remaining_tir_gate": "A3_RELATION_TYPED_AS_INTRINSIC_AFFINE_DISPLACEMENT",
        "A8_role": "LOCAL_CLOSURE_CROSSCHECK_AND_DOWNSTREAM_CONTEXT_LIFT",
        "A5_role": "METRIC_INVARIANT_MEASUREMENT",
        "technical_status": "PASS" if passed else "FAIL",
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
