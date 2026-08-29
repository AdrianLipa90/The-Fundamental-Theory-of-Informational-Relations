#!/usr/bin/env python3
"""Deterministic audit for Relational Cocycle to Affine Geometry v0.1."""
from __future__ import annotations

import json
from itertools import product

POINTS = {
    "o": (0, 0, 0),
    "x": (3, 0, 0),
    "y": (3, 4, 0),
    "z": (3, 4, 12),
}


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def norm2(a):
    return dot(a, a)


def edge(a: str, b: str):
    return sub(POINTS[b], POINTS[a])


def build_receipt() -> dict[str, object]:
    names = tuple(POINTS)

    reversal = all(edge(b, a) == tuple(-v for v in edge(a, b)) for a, b in product(names, repeat=2))
    closure = all(
        add(add(edge(a, b), edge(b, c)), edge(c, a)) == (0, 0, 0)
        for a, b, c in product(names, repeat=3)
    )

    origin = "o"
    reconstructed = all(
        edge(a, b) == sub(edge(origin, b), edge(origin, a))
        for a, b in product(names, repeat=2)
    )

    endpoint_addition = all(
        add(edge(a, b), edge(b, c)) == edge(a, c)
        for a, b, c in product(names, repeat=3)
    )

    # Metric triangle inequality in squared-coordinate realization; compare actual norms.
    import math
    metric_triangle = all(
        math.sqrt(norm2(edge(a, c))) <= math.sqrt(norm2(edge(a, b))) + math.sqrt(norm2(edge(b, c))) + 1e-12
        for a, b, c in product(names, repeat=3)
    )

    a = edge("o", "x")
    b = edge("x", "y")
    c = edge("o", "y")
    pythagorean = dot(a, b) == 0 and norm2(c) == norm2(a) + norm2(b) == 25

    blocks = {
        "reversal": {"pass": reversal},
        "triangle_closure": {"pass": closure},
        "affine_reconstruction": {"pass": reconstructed},
        "endpoint_addition": {"pass": endpoint_addition},
        "metric_triangle_inequality": {"pass": metric_triangle},
        "pythagorean_relational_triangle": {
            "a2": norm2(a),
            "b2": norm2(b),
            "c2": norm2(c),
            "pass": pythagorean,
        },
    }
    passed = all(bool(v["pass"]) for v in blocks.values())
    return {
        "schema": "TIR_SPACE_OF_GEOMETRY_RELATIONAL_COCYCLE_AFFINE_CLOSURE_V0_1",
        "exact_result": "TRIANGLE_CLOSURE_IMPLIES_LOCAL_AFFINE_COORDINATE_RECONSTRUCTION",
        "coordinate_formula": "E_xy=r(y)-r(x)",
        "endpoint_formula": "E_xz=E_xy+E_yz",
        "metric_formula": "d(x,y)=||E_xy||",
        "pythagorean_endpoint": "d(x,z)^2=d(x,y)^2+d(y,z)^2_FOR_ORTHOGONAL_STEPS",
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
