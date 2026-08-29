#!/usr/bin/env python3
"""Exact deterministic audit for physical relation chord realizability v0.1."""
from __future__ import annotations

import json
from fractions import Fraction


Vec = tuple[Fraction, Fraction, Fraction]


def v(*xs: int | Fraction) -> Vec:
    return tuple(Fraction(x) for x in xs)  # type: ignore[return-value]


def add(a: Vec, b: Vec) -> Vec:
    return tuple(x + y for x, y in zip(a, b))  # type: ignore[return-value]


def sub(a: Vec, b: Vec) -> Vec:
    return tuple(x - y for x, y in zip(a, b))  # type: ignore[return-value]


def scale(c: Fraction, a: Vec) -> Vec:
    return tuple(c * x for x in a)  # type: ignore[return-value]


def dot(a: Vec, b: Vec) -> Fraction:
    return sum((x * y for x, y in zip(a, b)), Fraction(0))


def norm2(a: Vec) -> Fraction:
    return dot(a, a)


def physical(a: Vec) -> bool:
    return norm2(a) <= 1


def boundary_chord_certificate() -> dict[str, object]:
    d = v(2, 0, 0)
    rx = scale(Fraction(-1, 2), d)
    ry = scale(Fraction(1, 2), d)
    recovered = sub(ry, rx)
    passed = physical(rx) and physical(ry) and recovered == d and norm2(d) == 4
    return {
        "target_chord": [str(x) for x in d],
        "endpoint_x": [str(x) for x in rx],
        "endpoint_y": [str(x) for x in ry],
        "endpoint_x_physical": physical(rx),
        "endpoint_y_physical": physical(ry),
        "chord_norm_squared": str(norm2(d)),
        "radius_two_boundary_realized": passed,
        "pass": passed,
    }


def right_triangle_certificate() -> dict[str, object]:
    a = Fraction(3, 5)
    b = Fraction(4, 5)
    rx = v(0, 0, 0)
    ry = v(a, 0, 0)
    rz = v(a, b, 0)

    exy = sub(ry, rx)
    eyz = sub(rz, ry)
    exz = sub(rz, rx)

    endpoint_addition = add(exy, eyz) == exz
    orthogonal = dot(exy, eyz) == 0
    pyth = norm2(exz) == norm2(exy) + norm2(eyz)
    expected = (
        norm2(exy) == Fraction(9, 25)
        and norm2(eyz) == Fraction(16, 25)
        and norm2(exz) == 1
    )
    endpoints_physical = all(physical(r) for r in (rx, ry, rz))
    passed = endpoints_physical and endpoint_addition and orthogonal and pyth and expected

    return {
        "a_squared": str(norm2(exy)),
        "b_squared": str(norm2(eyz)),
        "c_squared": str(norm2(exz)),
        "all_endpoints_physical": endpoints_physical,
        "endpoint_addition": endpoint_addition,
        "orthogonal": orthogonal,
        "pythagorean_identity": pyth,
        "normalized_3_4_5_certificate": expected,
        "pass": passed,
    }


def local_span_certificate() -> dict[str, object]:
    half = Fraction(1, 2)
    basis_chords = (v(half, 0, 0), v(0, half, 0), v(0, 0, half))
    each_reachable = all(norm2(d) <= 4 for d in basis_chords)
    independent = (
        basis_chords[0][0] != 0
        and basis_chords[1][1] != 0
        and basis_chords[2][2] != 0
    )
    passed = each_reachable and independent
    return {
        "three_independent_local_chords": independent,
        "all_inside_radius_two_domain": each_reachable,
        "spans_three_real_directions": passed,
        "pass": passed,
    }


def build_receipt() -> dict[str, object]:
    blocks = {
        "radius_two_boundary": boundary_chord_certificate(),
        "physical_right_triangle": right_triangle_certificate(),
        "local_three_direction_span": local_span_certificate(),
    }
    passed = all(bool(block["pass"]) for block in blocks.values())
    return {
        "schema": "PHYSICAL_RELATION_CHORD_REALIZABILITY_V0_1",
        "exact_theorem": "PHYSICAL_RELATION_CHORD_SET_IS_RADIUS_TWO_BALL",
        "relation_formula": "E_xy=(r_y-r_x).sigma",
        "reachable_coefficient_domain": "|d|<=2",
        "converse_realization": "r_x=-d/2,r_y=+d/2",
        "physical_pythagorean_family": "a>=0,b>=0,a^2+b^2<=1",
        "normalized_certificate": "3/5,4/5,1",
        "carrier_span": "Herm_0(2)~=R3",
        "global_extent_status": "DOWNSTREAM_LOCAL_CARRIER_GLUING",
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
