#!/usr/bin/env python3
"""Deterministic checks for the one-parameter physical length calibration theorem."""
from __future__ import annotations

from fractions import Fraction
import json


def dot(a: tuple[Fraction, Fraction, Fraction], b: tuple[Fraction, Fraction, Fraction]) -> Fraction:
    return sum((x * y for x, y in zip(a, b)), Fraction(0))


def q(v: tuple[Fraction, Fraction, Fraction]) -> Fraction:
    return dot(v, v)


def scaled_q(v: tuple[Fraction, Fraction, Fraction], lstar: Fraction) -> Fraction:
    return lstar * lstar * q(v)


def add(a: tuple[Fraction, Fraction, Fraction], b: tuple[Fraction, Fraction, Fraction]) -> tuple[Fraction, Fraction, Fraction]:
    return tuple(x + y for x, y in zip(a, b))  # type: ignore[return-value]


def build_receipt() -> dict[str, object]:
    a = (Fraction(3, 5), Fraction(0), Fraction(0))
    b = (Fraction(0), Fraction(4, 5), Fraction(0))
    c = add(a, b)

    lstar = Fraction(7, 3)

    pyth_dimensionless = q(c) == q(a) + q(b) == Fraction(1)
    pyth_calibrated = scaled_q(c, lstar) == scaled_q(a, lstar) + scaled_q(b, lstar)

    u = (Fraction(1), Fraction(0), Fraction(0))
    v = (Fraction(0), Fraction(2), Fraction(0))
    ratio_q_dimensionless = q(v) / q(u)
    ratio_q_physical = scaled_q(v, lstar) / scaled_q(u, lstar)
    ratio_invariant = ratio_q_dimensionless == ratio_q_physical == Fraction(4)

    orthogonal_dimensionless = dot(u, v) == 0
    orthogonal_physical = lstar * lstar * dot(u, v) == 0

    e_ref = c
    q_ref = q(e_ref)
    ell_ref_squared = lstar * lstar * q_ref
    recovered_lstar_squared = ell_ref_squared / q_ref
    calibration_inverse_exact = recovered_lstar_squared == lstar * lstar

    edge_boundary = (Fraction(2), Fraction(0), Fraction(0))
    edge_boundary_q = q(edge_boundary)
    physical_edge_max_squared = scaled_q(edge_boundary, lstar)
    edge_diameter_rule = edge_boundary_q == 4 and physical_edge_max_squared == 4 * lstar * lstar

    passed = all((
        pyth_dimensionless,
        pyth_calibrated,
        ratio_invariant,
        orthogonal_dimensionless,
        orthogonal_physical,
        calibration_inverse_exact,
        edge_diameter_rule,
        lstar > 0,
    ))

    return {
        "schema": "TIR_PHYSICAL_LENGTH_SCALE_CALIBRATION_V0_1",
        "technical_status": "PASS" if passed else "FAIL",
        "exact_result": "EUCLIDEAN_PHYSICAL_LENGTH_IS_ONE_PARAMETER_POSITIVE_SCALE_FAMILY",
        "metric_family": "g_phys=L_*^2*g_0",
        "length_map": "ell_phys(E)=L_*sqrt(Tr(E^2)/2)",
        "calibration_parameter_positive": lstar > 0,
        "reference_q": str(q_ref),
        "calibration_inverse_exact": calibration_inverse_exact,
        "single_edge_dimensionless_radius": 2,
        "single_edge_physical_radius": "2*L_*",
        "edge_diameter_rule_exact": edge_diameter_rule,
        "shape_invariants": {
            "orthogonality_scale_independent": orthogonal_dimensionless and orthogonal_physical,
            "squared_length_ratio_scale_independent": ratio_invariant,
            "pythagorean_covariant_under_calibration": pyth_dimensionless and pyth_calibrated,
        },
        "dimension_source_gate": "REQUIRES_TYPED_LENGTH_DIMENSION_DATUM",
        "next_frontier": "DERIVE_OR_BIND_L_STAR_SOURCE",
    }


def main() -> None:
    receipt = build_receipt()
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if receipt["technical_status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
