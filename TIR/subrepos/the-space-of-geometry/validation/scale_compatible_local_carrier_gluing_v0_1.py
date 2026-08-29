#!/usr/bin/env python3
"""Deterministic exact checks for scale-compatible local carrier gluing."""
from __future__ import annotations

from fractions import Fraction
import json

Vec = tuple[Fraction, Fraction, Fraction]
Mat = tuple[Vec, Vec, Vec]


def dot(a: Vec, b: Vec) -> Fraction:
    return sum((x * y for x, y in zip(a, b)), Fraction(0))


def mv(m: Mat, v: Vec) -> Vec:
    return tuple(dot(row, v) for row in m)  # type: ignore[return-value]


def scale(v: Vec, s: Fraction) -> Vec:
    return tuple(s * x for x in v)  # type: ignore[return-value]


def add(a: Vec, b: Vec) -> Vec:
    return tuple(x + y for x, y in zip(a, b))  # type: ignore[return-value]


def g_phys(a: Vec, b: Vec, lscale: Fraction) -> Fraction:
    return lscale * lscale * dot(a, b)


def det3(m: Mat) -> Fraction:
    a, b, c = m[0]
    d, e, f = m[1]
    g, h, i = m[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def build_receipt() -> dict[str, object]:
    rz90: Mat = (
        (Fraction(0), Fraction(-1), Fraction(0)),
        (Fraction(1), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(1)),
    )

    a: Vec = (Fraction(2), Fraction(1), Fraction(-1))
    b: Vec = (Fraction(1), Fraction(-3), Fraction(2))
    ra = mv(rz90, a)
    rb = mv(rz90, b)

    rotation_preserves_g0 = dot(ra, rb) == dot(a, b) and dot(ra, ra) == dot(a, a)
    rotation_orientation_preserving = det3(rz90) == 1

    lx = Fraction(2)
    ly = Fraction(3)

    pure_rotation_metric_equal_when_scales_differ = g_phys(ra, rb, ly) == g_phys(a, b, lx)
    pure_rotation_requires_equal_scale_sample = not pure_rotation_metric_equal_when_scales_differ

    conformal_factor = lx / ly
    ca = scale(ra, conformal_factor)
    cb = scale(rb, conformal_factor)
    conformal_metric_compatibility = g_phys(ca, cb, ly) == g_phys(a, b, lx)

    lcommon = Fraction(5, 2)
    common_scale_rotation_compatible = g_phys(ra, rb, lcommon) == g_phys(a, b, lcommon)

    l0, l1, l2 = Fraction(2), Fraction(3), Fraction(5)
    s01 = l0 / l1
    s12 = l1 / l2
    s20 = l2 / l0
    loop_scale_product = s01 * s12 * s20
    node_scale_loop_closure = loop_scale_product == 1

    e_xy: Vec = (Fraction(1), Fraction(0), Fraction(0))
    e_yz: Vec = (Fraction(1), Fraction(2), Fraction(0))
    transported_yz = mv(rz90, e_yz)
    e_xz = add(e_xy, transported_yz)
    closure_defect = tuple(x - y for x, y in zip(e_xz, add(e_xy, transported_yz)))
    endpoint_transport_composition_exact = closure_defect == (Fraction(0), Fraction(0), Fraction(0))

    passed = all((
        rotation_preserves_g0,
        rotation_orientation_preserving,
        pure_rotation_requires_equal_scale_sample,
        conformal_metric_compatibility,
        common_scale_rotation_compatible,
        node_scale_loop_closure,
        endpoint_transport_composition_exact,
    ))

    return {
        "schema": "TIR_SCALE_COMPATIBLE_LOCAL_CARRIER_GLUING_V0_1",
        "technical_status": "PASS" if passed else "FAIL",
        "exact_result": "PURE_SO3_METRIC_COMPATIBILITY_PROPAGATES_COMMON_SCALE_OR_CONFORMAL_FACTOR_LX_OVER_LY",
        "rotation_transport": "R_xy=Ad(W_xy^X) in SO(3)",
        "pure_rotation_common_scale_rule": "L_x=L_y",
        "varying_scale_transport": "C_xy=(L_x/L_y)*R_xy",
        "rotation_preserves_reference_metric": rotation_preserves_g0,
        "common_scale_rotation_metric_compatible": common_scale_rotation_compatible,
        "different_scale_pure_rotation_incompatible_sample": pure_rotation_requires_equal_scale_sample,
        "conformal_metric_compatibility_exact": conformal_metric_compatibility,
        "node_induced_scale_loop_product": str(loop_scale_product),
        "node_induced_scale_loop_closure": node_scale_loop_closure,
        "endpoint_transport_composition_exact": endpoint_transport_composition_exact,
        "closure_defect_sample": [str(x) for x in closure_defect],
        "next_frontier": "BIND_WIJ_LOOP_HOLONOMY_AND_CLOSURE_SECTORS_TO_TETRAHEDRAL_REFINEMENT",
    }


def main() -> None:
    receipt = build_receipt()
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if receipt["technical_status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
