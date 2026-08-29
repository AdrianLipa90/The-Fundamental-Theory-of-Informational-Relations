#!/usr/bin/env python3
"""Deterministic gate for TIR Universal-Loop discrete torsion source binding v0.1."""
from __future__ import annotations

import json
import math
import random

TOL = 1e-11

I3 = (
    (1.0, 0.0, 0.0),
    (0.0, 1.0, 0.0),
    (0.0, 0.0, 1.0),
)


def mm(a, b):
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )


def mv(a, v):
    return tuple(sum(a[i][k] * v[k] for k in range(3)) for i in range(3))


def va(a, b):
    return tuple(a[i] + b[i] for i in range(3))


def vs(a, b):
    return tuple(a[i] - b[i] for i in range(3))


def vn(a):
    return tuple(-x for x in a)


def transpose(a):
    return tuple(tuple(a[j][i] for j in range(3)) for i in range(3))


def rz(theta):
    c, s = math.cos(theta), math.sin(theta)
    return ((c, -s, 0.0), (s, c, 0.0), (0.0, 0.0, 1.0))


def ry(theta):
    c, s = math.cos(theta), math.sin(theta)
    return ((c, 0.0, s), (0.0, 1.0, 0.0), (-s, 0.0, c))


def rx(theta):
    c, s = math.cos(theta), math.sin(theta)
    return ((1.0, 0.0, 0.0), (0.0, c, -s), (0.0, s, c))


def rotation(a, b, c):
    return mm(rz(a), mm(ry(b), rx(c)))


def norm(v):
    return math.sqrt(sum(x * x for x in v))


def maxv(a, b):
    return max(abs(a[i] - b[i]) for i in range(3))


def maxm(a, b):
    return max(abs(a[i][j] - b[i][j]) for i in range(3) for j in range(3))


def se3_mul(g_left, g_right):
    """Composition: g_left acts after g_right."""
    rl, tl = g_left
    rr, tr = g_right
    return mm(rl, rr), va(tl, mv(rl, tr))


def se3_inverse(g):
    r, t = g
    ri = transpose(r)
    return ri, vn(mv(ri, t))


def connection_edge(r_target_source, e_target_source):
    return r_target_source, tuple(e_target_source)


def endpoint_defect(rxy, exy, eyz, exz):
    return vs(exz, va(exy, mv(rxy, eyz)))


def reverse_edge_vector(r_forward, e_forward):
    """For forward target<-source edge, return reversed displacement in source frame."""
    r_reverse = transpose(r_forward)
    return vn(mv(r_reverse, e_forward))


def discrete_solder_torsion_vector(rxy, rxz, exy, eyz, exz):
    """vec(T_xyz)=e_xy+R_xy e_yz+R_xz e_zx in the x frame."""
    ezx = reverse_edge_vector(rxz, exz)
    return va(va(exy, mv(rxy, eyz)), mv(rxz, ezx))


def triangle_loop(gxy, gyz, gxz):
    return se3_mul(se3_mul(gxy, gyz), se3_inverse(gxz))


def loop_identity_error(g):
    return max(maxm(g[0], I3), max(abs(x) for x in g[1]))


def frame_transform_edge(gxy, qx, qy):
    rxy, exy = gxy
    return mm(qx, mm(rxy, transpose(qy))), mv(qx, exy)


def atlas_edge(q_target, r_target, q_source, r_source):
    """Exact anchored chart map source -> target."""
    rts = mm(transpose(q_target), q_source)
    tts = mv(transpose(q_target), vs(r_source, r_target))
    return rts, tts


def check_triangle(rxy, ryz, exy, eyz, exz):
    rxz = mm(rxy, ryz)
    gxy = connection_edge(rxy, exy)
    gyz = connection_edge(ryz, eyz)
    gxz = connection_edge(rxz, exz)
    c = endpoint_defect(rxy, exy, eyz, exz)
    torsion = discrete_solder_torsion_vector(rxy, rxz, exy, eyz, exz)
    loop = triangle_loop(gxy, gyz, gxz)
    return {
        "rxz": rxz,
        "c": c,
        "torsion": torsion,
        "loop": loop,
        "rotation_error": maxm(loop[0], I3),
        "translation_identity_error": maxv(loop[1], vn(c)),
        "torsion_endpoint_error": maxv(torsion, vn(c)),
        "torsion_loop_error": maxv(torsion, loop[1]),
        "norm_identity_error": max(
            abs(norm(loop[1]) - norm(c)),
            abs(norm(torsion) - norm(c)),
            abs(norm(torsion) - norm(loop[1])),
        ),
    }


def main():
    checks = []

    # Deterministic nonzero connection-lifted triangle.
    rxy = rotation(0.37, -0.21, 0.13)
    ryz = rotation(-0.44, 0.31, -0.27)
    exy = (0.2, -0.4, 0.1)
    eyz = (-0.3, 0.25, -0.15)
    direct_composed_defect = (0.05, -0.02, 0.04)
    exz = va(va(exy, mv(rxy, eyz)), direct_composed_defect)
    tri = check_triangle(rxy, ryz, exy, eyz, exz)
    checks.append({
        "name": "nonzero_triangle_rotational_closure",
        "pass": tri["rotation_error"] < TOL,
        "max_error": tri["rotation_error"],
    })
    checks.append({
        "name": "loop_translation_equals_negative_endpoint_defect",
        "pass": tri["translation_identity_error"] < TOL,
        "max_error": tri["translation_identity_error"],
    })
    checks.append({
        "name": "discrete_solder_torsion_equals_negative_endpoint_defect",
        "pass": tri["torsion_endpoint_error"] < TOL,
        "max_error": tri["torsion_endpoint_error"],
    })
    checks.append({
        "name": "loop_translation_equals_discrete_solder_torsion",
        "pass": tri["torsion_loop_error"] < TOL,
        "max_error": tri["torsion_loop_error"],
    })
    checks.append({
        "name": "torsion_source_norm_identity",
        "pass": tri["norm_identity_error"] < TOL and norm(tri["torsion"]) > 1e-6,
        "max_error": tri["norm_identity_error"],
        "tau": norm(tri["loop"][1]),
    })

    # Exact zero-defect / zero-torsion connection triangle.
    exz_zero = va(exy, mv(rxy, eyz))
    zero = check_triangle(rxy, ryz, exy, eyz, exz_zero)
    zero_error = max(
        loop_identity_error(zero["loop"]),
        norm(zero["c"]),
        norm(zero["torsion"]),
    )
    checks.append({
        "name": "zero_endpoint_defect_gives_zero_torsion_identity_loop",
        "pass": zero_error < TOL,
        "max_error": zero_error,
    })

    # Independent local vector-frame covariance.
    qx = rotation(0.19, -0.33, 0.28)
    qy = rotation(-0.51, 0.17, 0.42)
    qz = rotation(0.63, -0.26, -0.11)
    rxz = mm(rxy, ryz)
    gxy = (rxy, exy)
    gyz = (ryz, eyz)
    gxz = (rxz, exz)
    gxy_p = frame_transform_edge(gxy, qx, qy)
    gyz_p = frame_transform_edge(gyz, qy, qz)
    gxz_p = frame_transform_edge(gxz, qx, qz)
    c_p = endpoint_defect(gxy_p[0], gxy_p[1], gyz_p[1], gxz_p[1])
    torsion_p = discrete_solder_torsion_vector(
        gxy_p[0], gxz_p[0], gxy_p[1], gyz_p[1], gxz_p[1]
    )
    loop_p = triangle_loop(gxy_p, gyz_p, gxz_p)
    expected_c_p = mv(qx, tri["c"])
    expected_torsion_p = mv(qx, tri["torsion"])
    expected_loop_t_p = mv(qx, tri["loop"][1])
    covariance_error = max(
        maxv(c_p, expected_c_p),
        maxv(torsion_p, expected_torsion_p),
        maxv(loop_p[1], expected_loop_t_p),
        abs(norm(c_p) - norm(tri["c"])),
        abs(norm(torsion_p) - norm(tri["torsion"])),
        abs(norm(loop_p[1]) - norm(tri["loop"][1])),
    )
    checks.append({
        "name": "independent_local_frame_covariance",
        "pass": covariance_error < TOL and maxm(loop_p[0], I3) < TOL,
        "max_error": max(covariance_error, maxm(loop_p[0], I3)),
    })

    # Pure-atlas rotating-frame baseline from source-owned anchors.
    q_a = rotation(0.12, -0.28, 0.07)
    q_b = rotation(-0.35, 0.18, -0.16)
    q_c = rotation(0.47, 0.09, 0.23)
    r_a = (0.2, -0.1, 0.4)
    r_b = (-0.3, 0.25, 0.05)
    r_c = (0.15, 0.5, -0.2)
    # Target-source convention: x <- y, y <- z, x <- z.
    g_ab = atlas_edge(q_a, r_a, q_b, r_b)
    g_bc = atlas_edge(q_b, r_b, q_c, r_c)
    g_ac = atlas_edge(q_a, r_a, q_c, r_c)
    atlas_composed = se3_mul(g_ab, g_bc)
    atlas_loop = triangle_loop(g_ab, g_bc, g_ac)
    atlas_torsion = discrete_solder_torsion_vector(
        g_ab[0], g_ac[0], g_ab[1], g_bc[1], g_ac[1]
    )
    atlas_error = max(
        maxm(atlas_composed[0], g_ac[0]),
        maxv(atlas_composed[1], g_ac[1]),
        loop_identity_error(atlas_loop),
        norm(atlas_torsion),
    )
    checks.append({
        "name": "pure_atlas_coboundary_zero_torsion_baseline",
        "pass": atlas_error < TOL,
        "max_error": atlas_error,
    })

    # Deterministic randomized family: prescribed defect maps to solder torsion and loop translation.
    rng = random.Random(20260829)
    randomized_max = 0.0
    randomized_min_tau = float("inf")
    for _ in range(128):
        a = [rng.uniform(-1.0, 1.0) for _ in range(6)]
        r1 = rotation(a[0], a[1], a[2])
        r2 = rotation(a[3], a[4], a[5])
        e1 = tuple(rng.uniform(-0.8, 0.8) for _ in range(3))
        e2 = tuple(rng.uniform(-0.8, 0.8) for _ in range(3))
        defect = tuple(rng.uniform(-0.2, 0.2) for _ in range(3))
        e_direct = va(va(e1, mv(r1, e2)), defect)
        sample = check_triangle(r1, r2, e1, e2, e_direct)
        randomized_max = max(
            randomized_max,
            sample["rotation_error"],
            sample["translation_identity_error"],
            sample["torsion_endpoint_error"],
            sample["torsion_loop_error"],
            sample["norm_identity_error"],
        )
        randomized_min_tau = min(randomized_min_tau, norm(sample["loop"][1]))
    checks.append({
        "name": "randomized_connection_triangle_family",
        "pass": randomized_max < TOL,
        "max_error": randomized_max,
        "minimum_sample_tau": randomized_min_tau,
    })

    passed = all(check["pass"] for check in checks)
    receipt = {
        "schema": "TIR_UNIVERSAL_LOOP_TORSION_SOURCE_BINDING_VALIDATION_V0_1",
        "technical_status": "PASS" if passed else "FAIL",
        "verdict": (
            "PASS_TIR_UNIVERSAL_LOOP_TORSION_SOURCE_BINDING"
            if passed
            else "FAIL_TIR_UNIVERSAL_LOOP_TORSION_SOURCE_BINDING"
        ),
        "source_binding": {
            "rotation": "R_xy = Ad(W_xy^X)",
            "translation": "e_xy = vec(E_xy)",
            "connection_edge": "G_xy = (R_xy,e_xy)",
            "endpoint_defect": "c_xyz = e_xz-(e_xy+R_xy e_yz)",
            "discrete_solder_torsion": "vec(T_xyz) = -c_xyz",
            "loop_identity": "t_C = vec(T_xyz) = -c_xyz on R_xz=R_xy R_yz",
            "scalar_witness": "tau_C = ||t_C|| = ||vec(T_xyz)|| = ||c_xyz||",
        },
        "pure_atlas_baseline": (
            "PASS"
            if next(c for c in checks if c["name"] == "pure_atlas_coboundary_zero_torsion_baseline")["pass"]
            else "FAIL"
        ),
        "discrete_torsion_source_binding": "PASS" if passed else "FAIL",
        "continuum_refining_family_correspondence": "DOWNSTREAM_GATE",
        "checks": checks,
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
