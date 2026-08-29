#!/usr/bin/env python3
from __future__ import annotations

import json
import math


TOL = 2.0e-12


def transpose(a):
    return [list(row) for row in zip(*a)]


def matmul(a, b):
    bt = transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def scale(a, c):
    return [[c * x for x in row] for row in a]


def eye(n):
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


def max_abs_diff(a, b):
    return max(abs(x - y) for ra, rb in zip(a, b) for x, y in zip(ra, rb))


def columns(a):
    return [list(col) for col in zip(*a)]


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def norm(x):
    return math.sqrt(dot(x, x))


def sub(x, y):
    return [a - b for a, b in zip(x, y)]


def det3(a):
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def tetra_volume(frame):
    pts = columns(frame)
    e1 = sub(pts[1], pts[0])
    e2 = sub(pts[2], pts[0])
    e3 = sub(pts[3], pts[0])
    matrix = [[e1[i], e2[i], e3[i]] for i in range(3)]
    return abs(det3(matrix)) / 6.0


def canonical_frame():
    s = 1.0 / math.sqrt(3.0)
    # 3 x 4 matrix, vectors are columns.
    return [
        [s, s, -s, -s],
        [s, -s, s, -s],
        [s, -s, -s, s],
    ]


def rotation_matrix():
    # Deterministic proper rotation Rz(0.37) Ry(-0.51).
    a = 0.37
    b = -0.51
    rz = [
        [math.cos(a), -math.sin(a), 0.0],
        [math.sin(a), math.cos(a), 0.0],
        [0.0, 0.0, 1.0],
    ]
    ry = [
        [math.cos(b), 0.0, math.sin(b)],
        [0.0, 1.0, 0.0],
        [-math.sin(b), 0.0, math.cos(b)],
    ]
    return matmul(rz, ry)


def permute_columns(frame, order):
    cols = columns(frame)
    picked = [cols[i] for i in order]
    return transpose(picked)


def gram(frame):
    return matmul(transpose(frame), frame)


def second_moment(frame):
    return matmul(frame, transpose(frame))


def build_receipt():
    n = canonical_frame()
    r = rotation_matrix()
    # Even permutation to preserve orientation class.
    m = permute_columns(matmul(r, n), (1, 2, 0, 3))

    g_n = gram(n)
    g_m = gram(m)
    expected_g = [
        [1.0 if i == j else -1.0 / 3.0 for j in range(4)]
        for i in range(4)
    ]
    expected_second = scale(eye(3), 4.0 / 3.0)

    q = scale(matmul(m, transpose(n)), 3.0 / 4.0)
    q_orth_defect = max_abs_diff(matmul(q, transpose(q)), eye(3))
    mapping_defect = max_abs_diff(matmul(q, n), m)

    cols_n = columns(n)
    edge = norm(sub(cols_n[0], cols_n[1]))
    volume_n = tetra_volume(n)
    volume_m = tetra_volume(m)
    dot_off = dot(cols_n[0], cols_n[1])
    chi = math.acos(dot_off)
    cos_alpha = (math.cos(chi) - math.cos(chi) ** 2) / (math.sin(chi) ** 2)
    alpha = math.acos(cos_alpha)
    sphere_face_area = 3.0 * alpha - math.pi
    fs_face_area = sphere_face_area / 4.0
    fs_total_area = 4.0 * fs_face_area
    shape_coeff = volume_n / fs_total_area

    checks = {
        "spatial_gram": max_abs_diff(g_n, expected_g) < TOL,
        "sic_gram": max_abs_diff(g_m, expected_g) < TOL,
        "common_gram": max_abs_diff(g_n, g_m) < TOL,
        "spatial_second_moment": max_abs_diff(second_moment(n), expected_second) < TOL,
        "sic_second_moment": max_abs_diff(second_moment(m), expected_second) < TOL,
        "orthogonal_q": q_orth_defect < TOL,
        "q_maps_spatial_to_sic": mapping_defect < TOL,
        "proper_orientation": abs(det3(q) - 1.0) < TOL,
        "edge_length": abs(edge - math.sqrt(8.0 / 3.0)) < TOL,
        "volume_invariant": abs(volume_n - volume_m) < TOL,
        "volume_value": abs(volume_n - 8.0 / (9.0 * math.sqrt(3.0))) < TOL,
        "fs_face_area": abs(fs_face_area - math.pi / 4.0) < TOL,
        "fs_total_area": abs(fs_total_area - math.pi) < TOL,
        "shape_coefficient": abs(shape_coeff - 8.0 / (9.0 * math.sqrt(3.0) * math.pi)) < TOL,
    }

    passed = all(checks.values())
    return {
        "schema": "TIR_TETRAHEDRAL_CONGRUENCE_CLASS_CLOSURE_V0_1",
        "technical_status": "PASS" if passed else "FAIL",
        "verdict": "PASS_COMMON_TETRAHEDRAL_CONGRUENCE_CLASS" if passed else "FAIL_COMMON_TETRAHEDRAL_CONGRUENCE_CLASS",
        "checks": checks,
        "defects": {
            "gram": max_abs_diff(g_n, g_m),
            "orthogonality": q_orth_defect,
            "mapping": mapping_defect,
        },
        "det_q": det3(q),
        "edge": edge,
        "volume": volume_n,
        "fs_face_area": fs_face_area,
        "fs_total_area": fs_total_area,
        "shape_coefficient": shape_coeff,
        "semantic_role_binding": "SEPARATE_DOWNSTREAM_BINDING",
    }


def main():
    receipt = build_receipt()
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if receipt["technical_status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
