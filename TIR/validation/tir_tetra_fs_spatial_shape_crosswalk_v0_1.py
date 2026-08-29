#!/usr/bin/env python3
from __future__ import annotations

import json
import math

import numpy as np

SCHEMA = "TIR_TETRA_FS_SPATIAL_SHAPE_CROSSWALK_V0_1"


def canonical_vertices() -> np.ndarray:
    s = 1.0 / math.sqrt(3.0)
    return s * np.array(
        [
            [1.0, 1.0, 1.0],
            [1.0, -1.0, -1.0],
            [-1.0, 1.0, -1.0],
            [-1.0, -1.0, 1.0],
        ],
        dtype=float,
    )


def tetra_volume(vertices: np.ndarray) -> float:
    a, b, c, d = vertices
    return abs(float(np.linalg.det(np.column_stack((b-a, c-a, d-a))))) / 6.0


def main() -> None:
    v = canonical_vertices()
    gram = v @ v.T
    target_gram = np.full((4, 4), -1.0/3.0)
    np.fill_diagonal(target_gram, 1.0)

    edge2 = float(np.sum((v[0] - v[1])**2))
    edge = math.sqrt(edge2)
    volume = tetra_volume(v)
    expected_volume = 8.0 / (9.0 * math.sqrt(3.0))

    cos_chi = -1.0/3.0
    sin2_chi = 1.0 - cos_chi*cos_chi
    cos_alpha = (cos_chi - cos_chi*cos_chi) / sin2_chi
    alpha = math.acos(cos_alpha)
    unit_sphere_face_area = 3.0 * alpha - math.pi
    fs_face_area = 0.25 * unit_sphere_face_area
    fs_total_area = 4.0 * fs_face_area

    coefficient = volume / fs_total_area
    expected_coefficient = 8.0 / (9.0 * math.sqrt(3.0) * math.pi)

    checks = {
        "tetra_gram": bool(np.allclose(gram, target_gram, atol=1e-13, rtol=0.0)),
        "edge2_8_over_3": math.isclose(edge2, 8.0/3.0, rel_tol=0.0, abs_tol=1e-13),
        "edge_sqrt_8_over_3": math.isclose(edge, math.sqrt(8.0/3.0), rel_tol=0.0, abs_tol=1e-13),
        "volume_exact": math.isclose(volume, expected_volume, rel_tol=0.0, abs_tol=1e-13),
        "spherical_angle_2pi_over_3": math.isclose(alpha, 2.0*math.pi/3.0, rel_tol=0.0, abs_tol=1e-13),
        "unit_sphere_face_area_pi": math.isclose(unit_sphere_face_area, math.pi, rel_tol=0.0, abs_tol=1e-13),
        "fs_face_area_pi_over_4": math.isclose(fs_face_area, math.pi/4.0, rel_tol=0.0, abs_tol=1e-13),
        "fs_total_area_pi": math.isclose(fs_total_area, math.pi, rel_tol=0.0, abs_tol=1e-13),
        "dual_shape_coefficient": math.isclose(coefficient, expected_coefficient, rel_tol=0.0, abs_tol=1e-13),
    }

    passed = all(checks.values())
    receipt = {
        "schema": SCHEMA,
        "technical_status": "PASS" if passed else "FAIL",
        "shared_realization_status": "CONDITIONAL_SHARED_TETRAHEDRAL_CARRIER",
        "physical_scale_status": "OPEN",
        "edge_squared": edge2,
        "dimensionless_volume": volume,
        "fs_face_area": fs_face_area,
        "fs_total_area": fs_total_area,
        "dual_shape_coefficient": coefficient,
        "dual_shape_coefficient_exact": "8/(9*sqrt(3)*pi)",
        "checks": checks,
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
