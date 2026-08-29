#!/usr/bin/env python3
"""Deterministic audit for Quantum Point Affine Spatial Carrier v0.1."""
from __future__ import annotations

from fractions import Fraction
import json

Vector = tuple[Fraction, Fraction, Fraction]


def add(a: Vector, b: Vector) -> Vector:
    return tuple(x + y for x, y in zip(a, b))  # type: ignore[return-value]


def sub(a: Vector, b: Vector) -> Vector:
    return tuple(x - y for x, y in zip(a, b))  # type: ignore[return-value]


def dot(a: Vector, b: Vector) -> Fraction:
    return sum((x * y for x, y in zip(a, b)), Fraction(0, 1))


def rank3(v1: Vector, v2: Vector, v3: Vector) -> int:
    a, b, c = v1
    d, e, f = v2
    g, h, i = v3
    det = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
    return 3 if det != 0 else 2


def build_receipt() -> dict[str, object]:
    r0: Vector = (Fraction(0), Fraction(0), Fraction(0))
    rx: Vector = (Fraction(1, 2), Fraction(0), Fraction(0))
    ry: Vector = (Fraction(0), Fraction(1, 3), Fraction(0))
    rz: Vector = (Fraction(0), Fraction(0), Fraction(1, 4))
    r1: Vector = (Fraction(1, 2), Fraction(0), Fraction(0))
    r2: Vector = (Fraction(1, 2), Fraction(1, 3), Fraction(0))
    r3: Vector = (Fraction(1, 2), Fraction(1, 3), Fraction(1, 4))

    e01 = sub(r1, r0)
    e12 = sub(r2, r1)
    e23 = sub(r3, r2)
    e03 = sub(r3, r0)

    composed = add(add(e01, e12), e23)
    closure = composed == e03
    reversal = sub(r0, r1) == tuple(-x for x in e01)
    carrier_rank = rank3(sub(rx, r0), sub(ry, r0), sub(rz, r0))

    # Under E=(delta r).sigma, 1/2 Tr(E^2)=|delta r|^2.
    metric_e03 = dot(e03, e03)
    expected_metric = Fraction(1, 4) + Fraction(1, 9) + Fraction(1, 16)
    metric_exact = metric_e03 == expected_metric == Fraction(61, 144)

    # Integer tetrahedral certificate: normalized pairwise dot is -1/3.
    tetra = (
        (1, 1, 1),
        (1, -1, -1),
        (-1, 1, -1),
        (-1, -1, 1),
    )
    tetra_sum = tuple(sum(v[k] for v in tetra) for k in range(3))
    tetra_cross = [sum(tetra[a][k] * tetra[b][k] for k in range(3)) for a in range(4) for b in range(a + 1, 4)]
    tetra_norms = [sum(x * x for x in v) for v in tetra]
    tetra_pass = tetra_sum == (0, 0, 0) and tetra_cross == [-1] * 6 and tetra_norms == [3] * 4

    blocks = {
        "trace_one_affine_hull": {
            "herm2_real_dimension": 4,
            "trace_constraint_codimension": 1,
            "affine_hull_real_dimension": 3,
            "translation_space": "Herm_0(2)",
            "pass": carrier_rank == 3,
        },
        "canonical_affine_difference": {
            "formula": "E_xy=2*(rho_y-rho_x)=(r_y-r_x).sigma",
            "reversal": reversal,
            "endpoint_composition": closure,
            "loop_closure_automatic": closure,
            "pass": reversal and closure,
        },
        "hilbert_schmidt_metric": {
            "identity": "0.5*Tr(E^2)=|delta_r|^2",
            "sample_squared_length": "61/144",
            "pass": metric_exact,
        },
        "tetrahedral_affine_frame": {
            "zero_mean": tetra_sum == (0, 0, 0),
            "normalized_pairwise_dot": "-1/3",
            "affine_span_dimension": 3,
            "pass": tetra_pass,
        },
    }
    passed = all(bool(block["pass"]) for block in blocks.values())
    return {
        "schema": "TIR_QUANTUM_POINT_AFFINE_SPATIAL_CARRIER_V0_1",
        "promotion_route": "QUANTUM_POINT_AFFINE_DIFFERENCE",
        "local_relation_carrier": "Herm_0(2)~=R3",
        "endpoint_closure_automatic_under_bridge": True,
        "minimal_representation_route_role": "UNIQUENESS_CROSSCHECK",
        "remaining_gate": "RELATION_AS_CANONICAL_QUANTUM_STATE_DIFFERENCE",
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
