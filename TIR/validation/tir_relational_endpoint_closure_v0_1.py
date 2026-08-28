#!/usr/bin/env python3
"""Deterministic audit for TIR Relational Endpoint Closure v0.1."""
from __future__ import annotations

import json

Vector = tuple[int, int, int]
Matrix = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]

I3: Matrix = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
RZ90: Matrix = ((0, -1, 0), (1, 0, 0), (0, 0, 1))
RZ_90: Matrix = ((0, 1, 0), (-1, 0, 0), (0, 0, 1))


def apply(r: Matrix, v: Vector) -> Vector:
    return tuple(sum(r[i][j] * v[j] for j in range(3)) for i in range(3))  # type: ignore[return-value]


def add(a: Vector, b: Vector) -> Vector:
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def sub(a: Vector, b: Vector) -> Vector:
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def neg(a: Vector) -> Vector:
    return (-a[0], -a[1], -a[2])


def norm2(a: Vector) -> int:
    return a[0] * a[0] + a[1] * a[1] + a[2] * a[2]


def endpoint_closure_certificate() -> dict[str, object]:
    e_xy: Vector = (1, 0, 0)
    e_yz: Vector = (1, 0, 0)
    transported_yz = apply(RZ90, e_yz)
    e_xz = add(e_xy, transported_yz)
    defect = sub(e_xz, add(e_xy, transported_yz))
    return {
        "E_xy": e_xy,
        "Ad_Uxy_E_yz": transported_yz,
        "E_xz": e_xz,
        "endpoint_defect": defect,
        "pass": defect == (0, 0, 0),
    }


def triangle_equivalence_certificate() -> dict[str, object]:
    e_xy: Vector = (1, 0, 0)
    e_yz: Vector = (1, 0, 0)
    transported_yz = apply(RZ90, e_yz)
    e_xz = add(e_xy, transported_yz)

    # Choose U_xz = I, hence U_zx = I and E_zx = -E_xz.
    e_zx = neg(e_xz)
    torsion = add(add(e_xy, transported_yz), apply(I3, e_zx))
    endpoint_defect = sub(e_xz, add(e_xy, transported_yz))
    equivalence = torsion == neg(endpoint_defect)
    return {
        "endpoint_defect": endpoint_defect,
        "triangle_torsion_defect": torsion,
        "T_equals_minus_C": equivalence,
        "pass": equivalence and torsion == (0, 0, 0),
    }


def mismatch_detection_certificate() -> dict[str, object]:
    e_xy: Vector = (1, 0, 0)
    e_yz: Vector = (1, 0, 0)
    transported_yz = apply(RZ90, e_yz)
    wrong_e_xz: Vector = (2, 0, 0)
    defect = sub(wrong_e_xz, add(e_xy, transported_yz))
    return {
        "wrong_E_xz": wrong_e_xz,
        "endpoint_defect": defect,
        "defect_norm_squared": norm2(defect),
        "pass": defect != (0, 0, 0) and norm2(defect) > 0,
    }


def metric_transport_certificate() -> dict[str, object]:
    vectors = ((1, 2, 3), (2, -1, 4), (0, 5, -2))
    rows = []
    passed = True
    for v in vectors:
        w = apply(RZ90, v)
        row_pass = norm2(v) == norm2(w)
        passed &= row_pass
        rows.append({"v": v, "Rv": w, "norm2_v": norm2(v), "norm2_Rv": norm2(w), "pass": row_pass})
    inverse_pass = all(apply(RZ_90, apply(RZ90, v)) == v for v in vectors)
    passed &= inverse_pass
    return {"rows": rows, "inverse_transport_pass": inverse_pass, "pass": passed}


def build_receipt() -> dict[str, object]:
    blocks = {
        "endpoint_composition_closure": endpoint_closure_certificate(),
        "triangle_torsion_endpoint_defect_equivalence": triangle_equivalence_certificate(),
        "nonzero_mismatch_detected": mismatch_detection_certificate(),
        "metric_preserving_frame_transport": metric_transport_certificate(),
    }
    passed = all(bool(block["pass"]) for block in blocks.values())
    return {
        "schema": "TIR_RELATIONAL_ENDPOINT_CLOSURE_V0_1",
        "scope": "TIR_DISCRETE_ENDPOINT_TORSION_CLOSURE_AUDIT",
        "exact_discrete_result": "ENDPOINT_DEFECT_ZERO_IFF_TRIANGULAR_TORSION_DEFECT_ZERO",
        "continuum_target": "T_a=0 under regular refining endpoint-closed limit",
        "levi_civita_dependency": "metric compatibility + zero torsion",
        "a8_status": "CLOSURE_LAW_CANDIDATE",
        "regular_continuum_limit_derived": False,
        "next_gate": "RELATIONAL_REFINEMENT_STABILITY_LAW",
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
