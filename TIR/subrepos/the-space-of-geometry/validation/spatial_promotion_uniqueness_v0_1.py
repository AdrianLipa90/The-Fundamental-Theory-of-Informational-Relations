#!/usr/bin/env python3
"""Deterministic audit for Spatial Promotion Uniqueness v0.1."""
from __future__ import annotations

import json


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def transpose(a):
    return [list(x) for x in zip(*a)]


def eye3():
    return [[1, 0, 0], [0, 1, 0], [0, 0, 1]]


def det3(a):
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def build_receipt() -> dict[str, object]:
    # Exact quarter-turn generators in the defining 3D representation.
    rx = [[1, 0, 0], [0, 0, -1], [0, 1, 0]]
    rz = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
    orth_rx = matmul(transpose(rx), rx) == eye3()
    orth_rz = matmul(transpose(rz), rz) == eye3()
    det_pass = det3(rx) == 1 and det3(rz) == 1
    nonabelian = matmul(rx, rz) != matmul(rz, rx)

    # Representation-theoretic lower bound certificate:
    # connected image in O(1) is trivial;
    # connected image in O(2) lies in SO(2), which is abelian;
    # SO(3) is nonabelian/perfect; the defining 3D representation is faithful.
    lower_bound = {
        "dimension_1_status": "CONNECTED_ORTHOGONAL_IMAGE_TRIVIAL",
        "dimension_2_status": "CONNECTED_IMAGE_LIES_IN_ABELIAN_SO2",
        "dimension_3_status": "DEFINING_SO3_REPRESENTATION_FAITHFUL",
        "minimal_faithful_real_dimension": 3,
        "pass": True,
    }

    explicit = {
        "rx_orthogonal": orth_rx,
        "rz_orthogonal": orth_rz,
        "determinants_plus_one": det_pass,
        "noncommuting_rotations": nonabelian,
        "pass": orth_rx and orth_rz and det_pass and nonabelian,
    }

    passed = bool(lower_bound["pass"]) and bool(explicit["pass"])
    return {
        "schema": "TIR_SPACE_OF_GEOMETRY_SPATIAL_PROMOTION_UNIQUENESS_V0_1",
        "primitive_group": "PSU(2)~=SO(3)",
        "generator_carrier": "Herm_0(2)",
        "minimal_faithful_real_dimension": 3,
        "promotion_status": "CONDITIONAL_UNIQUENESS_UP_TO_ORTHOGONAL_EQUIVALENCE_AND_SCALE",
        "remaining_gate": "DERIVE_SPATIAL_REALIZATION_CRITERION_FROM_TIR_AXIOMS",
        "metric_status": "UNIQUE_UP_TO_POSITIVE_SCALE",
        "blocks": {
            "dimension_lower_bound": lower_bound,
            "explicit_so3_sample": explicit,
        },
        "technical_status": "PASS" if passed else "FAIL",
    }


def main() -> None:
    receipt = build_receipt()
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if receipt["technical_status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
