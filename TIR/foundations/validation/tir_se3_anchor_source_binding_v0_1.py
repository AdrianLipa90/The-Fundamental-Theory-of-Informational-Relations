#!/usr/bin/env python3
"""Deterministic gate for TIR SE(3) anchor-source binding v0.1."""
from __future__ import annotations

import json
import math
import random

TOL = 1e-11


def mm(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)) for i in range(3))


def mv(a, v):
    return tuple(sum(a[i][k] * v[k] for k in range(3)) for i in range(3))


def vt(a, b):
    return tuple(a[i] + b[i] for i in range(3))


def vs(a, b):
    return tuple(a[i] - b[i] for i in range(3))


def transpose(a):
    return tuple(tuple(a[j][i] for j in range(3)) for i in range(3))


def rz(theta):
    c, s = math.cos(theta), math.sin(theta)
    return ((c, -s, 0.0), (s, c, 0.0), (0.0, 0.0, 1.0))


def ry(theta):
    c, s = math.cos(theta), math.sin(theta)
    return ((c, 0.0, s), (0.0, 1.0, 0.0), (-s, 0.0, c))


def compose(g2, g1):
    r2, t2 = g2
    r1, t1 = g1
    return mm(r2, r1), vt(mv(r2, t1), t2)


def inverse(g):
    r, t = g
    ri = transpose(r)
    nti = tuple(-x for x in mv(ri, t))
    return ri, nti


def transition(qa, ra, qb, rb):
    rba = mm(transpose(qb), qa)
    tba = mv(transpose(qb), vs(ra, rb))
    return rba, tba


def coords(q, anchor, point):
    return mv(transpose(q), vs(point, anchor))


def maxm(a, b):
    return max(abs(a[i][j] - b[i][j]) for i in range(3) for j in range(3))


def maxv(a, b):
    return max(abs(a[i] - b[i]) for i in range(3))


def identity_error(g):
    I = ((1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0))
    return max(maxm(g[0], I), max(abs(x) for x in g[1]))


def main():
    checks = []

    qa = mm(rz(0.37), ry(-0.21))
    qb = mm(rz(-0.58), ry(0.31))
    ra = (0.2, -0.4, 0.1)
    rb = (-0.3, 0.25, -0.15)
    point = (0.55, -0.1, 0.7)
    gba = transition(qa, ra, qb, rb)
    xa = coords(qa, ra, point)
    xb = coords(qb, rb, point)
    xb_from_a = vt(mv(gba[0], xa), gba[1])
    checks.append({"name": "anchored_coordinate_transform", "pass": maxv(xb, xb_from_a) < TOL})

    gab = transition(qb, rb, qa, ra)
    inv_err = max(maxm(gab[0], inverse(gba)[0]), maxv(gab[1], inverse(gba)[1]))
    checks.append({"name": "pair_inverse", "pass": inv_err < TOL, "max_error": inv_err})

    qc = mm(rz(0.91), ry(0.13))
    rc = (0.1, 0.3, -0.45)
    gcb = transition(qb, rb, qc, rc)
    gca = transition(qa, ra, qc, rc)
    composed = compose(gcb, gba)
    cocycle_err = max(maxm(composed[0], gca[0]), maxv(composed[1], gca[1]))
    checks.append({"name": "three_chart_cocycle", "pass": cocycle_err < TOL, "max_error": cocycle_err})

    frames = [qa, qb, qc, mm(rz(-0.44), ry(-0.27))]
    anchors = [ra, rb, rc, (-0.2, -0.1, 0.35)]
    loop = (((1.0,0.0,0.0),(0.0,1.0,0.0),(0.0,0.0,1.0)), (0.0,0.0,0.0))
    for i in range(len(frames)):
        j = (i + 1) % len(frames)
        edge = transition(frames[i], anchors[i], frames[j], anchors[j])
        loop = compose(edge, loop)
    loop_err = identity_error(loop)
    checks.append({"name": "finite_pure_atlas_loop_identity", "pass": loop_err < TOL, "max_error": loop_err})

    rng = random.Random(20260829)
    random_max = 0.0
    for _ in range(64):
        a1, a2, a3 = [rng.uniform(-1.0, 1.0) for _ in range(3)]
        q1 = mm(rz(a1), ry(a2))
        q2 = mm(rz(a2), ry(a3))
        r1 = tuple(rng.uniform(-0.9, 0.9) for _ in range(3))
        r2 = tuple(rng.uniform(-0.9, 0.9) for _ in range(3))
        p = tuple(rng.uniform(-1.0, 1.0) for _ in range(3))
        g21 = transition(q1, r1, q2, r2)
        x1 = coords(q1, r1, p)
        x2 = coords(q2, r2, p)
        err = maxv(x2, vt(mv(g21[0], x1), g21[1]))
        random_max = max(random_max, err)
    checks.append({"name": "randomized_anchor_frame_transform", "pass": random_max < TOL, "max_error": random_max})

    # Non-coboundary perturbation breaks pure-atlas loop identity.
    bad_edge = transition(frames[0], anchors[0], frames[1], anchors[1])
    bad_edge = (bad_edge[0], vt(bad_edge[1], (0.03, -0.02, 0.01)))
    bad_loop = (((1.0,0.0,0.0),(0.0,1.0,0.0),(0.0,0.0,1.0)), (0.0,0.0,0.0))
    for i in range(len(frames)):
        j = (i + 1) % len(frames)
        edge = bad_edge if i == 0 else transition(frames[i], anchors[i], frames[j], anchors[j])
        bad_loop = compose(edge, bad_loop)
    checks.append({"name": "noncoboundary_breaks_loop_identity", "pass": identity_error(bad_loop) > 1e-4, "loop_error": identity_error(bad_loop)})

    # Infinitesimal affine generator: Q(dt)^T Q(0), r(dt)=u dt.
    omega = 0.7
    u = (0.4, -0.15, 0.2)
    x = (0.3, -0.8, 0.5)
    J = ((0.0, -1.0, 0.0), (1.0, 0.0, 0.0), (0.0, 0.0, 0.0))
    Omega = tuple(tuple(-omega * J[i][j] for j in range(3)) for i in range(3))
    expected = vt(tuple(-z for z in u), mv(Omega, x))
    convergence = []
    for dt in (1e-3, 5e-4, 2.5e-4):
        q0 = rz(0.0)
        q1 = rz(omega * dt)
        r0 = (0.0, 0.0, 0.0)
        r1 = tuple(z * dt for z in u)
        g10 = transition(q0, r0, q1, r1)
        x1 = vt(mv(g10[0], x), g10[1])
        rate = tuple((x1[i] - x[i]) / dt for i in range(3))
        convergence.append(maxv(rate, expected))
    conv_ok = convergence[1] < convergence[0] and convergence[2] < convergence[1] and convergence[2] < 5e-4
    checks.append({"name": "infinitesimal_affine_generator_convergence", "pass": conv_ok, "errors": convergence})

    passed = all(c["pass"] for c in checks)
    receipt = {
        "schema": "TIR_SE3_ANCHOR_SOURCE_BINDING_VALIDATION_V0_1",
        "technical_status": "PASS" if passed else "FAIL",
        "verdict": "PASS_TIR_SE3_ANCHOR_SOURCE_BINDING" if passed else "FAIL_TIR_SE3_ANCHOR_SOURCE_BINDING",
        "checks": checks,
        "pure_atlas_holonomy": "TRIVIAL",
        "connection_holonomy": "SEPARATE_DOWNSTREAM_GATE",
        "adm_shift_binding": "CANDIDATE_ONLY",
        "gremlin_authority": "CANDIDATE_ONLY",
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
