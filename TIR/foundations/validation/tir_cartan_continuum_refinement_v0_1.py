#!/usr/bin/env python3
"""Synthetic convergence gate for TIR Cartan continuum refinement v0.1."""
from __future__ import annotations

import json
import math

TOL = 1e-10
N_EDGE_STEPS = 192

I3 = (
    (1.0, 0.0, 0.0),
    (0.0, 1.0, 0.0),
    (0.0, 0.0, 1.0),
)
Z3 = (
    (0.0, 0.0, 0.0),
    (0.0, 0.0, 0.0),
    (0.0, 0.0, 0.0),
)


def mm(a, b):
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )


def mv(a, v):
    return tuple(sum(a[i][k] * v[k] for k in range(3)) for i in range(3))


def ma(a, b):
    return tuple(tuple(a[i][j] + b[i][j] for j in range(3)) for i in range(3))


def ms(a, b):
    return tuple(tuple(a[i][j] - b[i][j] for j in range(3)) for i in range(3))


def smul(s, a):
    return tuple(tuple(s * a[i][j] for j in range(3)) for i in range(3))


def va(a, b):
    return tuple(a[i] + b[i] for i in range(3))


def vs(a, b):
    return tuple(a[i] - b[i] for i in range(3))


def vscale(s, a):
    return tuple(s * x for x in a)


def transpose(a):
    return tuple(tuple(a[j][i] for j in range(3)) for i in range(3))


def vnorm(v):
    return math.sqrt(sum(x * x for x in v))


def mnorm(a):
    return math.sqrt(sum(a[i][j] ** 2 for i in range(3) for j in range(3)))


def maxv(a, b):
    return max(abs(a[i] - b[i]) for i in range(3))


def maxm(a, b):
    return max(abs(a[i][j] - b[i][j]) for i in range(3) for j in range(3))


def skew(axis):
    x, y, z = axis
    return (
        (0.0, -z, y),
        (z, 0.0, -x),
        (-y, x, 0.0),
    )


def exp_so3(a):
    # a is already the integrated skew generator.
    vx = a[2][1]
    vy = a[0][2]
    vz = a[1][0]
    theta = math.sqrt(vx * vx + vy * vy + vz * vz)
    if theta < 1e-14:
        return ma(I3, a)
    a2 = mm(a, a)
    s1 = math.sin(theta) / theta
    s2 = (1.0 - math.cos(theta)) / (theta * theta)
    return ma(I3, ma(smul(s1, a), smul(s2, a2)))


def rz(theta):
    c, s = math.cos(theta), math.sin(theta)
    return ((c, -s, 0.0), (s, c, 0.0), (0.0, 0.0, 1.0))


def ry(theta):
    c, s = math.cos(theta), math.sin(theta)
    return ((c, 0.0, s), (0.0, 1.0, 0.0), (-s, 0.0, c))


def rotation(a, b):
    return mm(rz(a), ry(b))


def commutator(a, b):
    return ms(mm(a, b), mm(b, a))


def determinant(a):
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def base_coframe(mu, p):
    x1, x2 = p
    if mu == 0:
        return (1.0 + 0.1 * x1, 0.4 * x2, 0.2 * x2)
    if mu == 1:
        return (0.25 * x1, 1.0 - 0.1 * x2, -0.3 * x1)
    if mu == 2:
        return (0.0, 0.0, 1.0)
    raise ValueError("mu must be 0,1,2")


OMEGA_1 = smul(0.3, skew((0.0, 0.0, 1.0)))
OMEGA_2 = smul(-0.2, skew((0.0, 1.0, 0.0)))


def base_omega(mu, _p):
    if mu == 0:
        return OMEGA_1
    if mu == 1:
        return OMEGA_2
    if mu == 2:
        return Z3
    raise ValueError("mu must be 0,1,2")


def line_generator(omega_fn, p, dx):
    out = Z3
    for mu in range(2):
        out = ma(out, smul(dx[mu], omega_fn(mu, p)))
    return out


def edge_integral(start, end, coframe_fn, omega_fn, steps=N_EDGE_STEPS):
    start = tuple(float(x) for x in start)
    end = tuple(float(x) for x in end)
    dx = tuple((end[i] - start[i]) / steps for i in range(2))
    u = I3
    e_total = (0.0, 0.0, 0.0)
    for k in range(steps):
        p_mid = tuple(start[i] + (k + 0.5) * dx[i] for i in range(2))
        a_step = line_generator(omega_fn, p_mid, dx)
        u_mid = mm(u, exp_so3(smul(0.5, a_step)))
        e_line = (0.0, 0.0, 0.0)
        for mu in range(2):
            e_line = va(e_line, vscale(dx[mu], coframe_fn(mu, p_mid)))
        e_total = va(e_total, mv(u_mid, e_line))
        u = mm(u, exp_so3(a_step))
    return e_total, u


def anti(a):
    return smul(0.5, ms(a, transpose(a)))


def triangle_sample(h, coframe_fn=base_coframe, omega_fn=base_omega):
    x = (0.0, 0.0)
    y = (h, 0.0)
    z = (0.0, h)
    exy, rxy = edge_integral(x, y, coframe_fn, omega_fn)
    eyz, ryz = edge_integral(y, z, coframe_fn, omega_fn)
    ezx, rzx = edge_integral(z, x, coframe_fn, omega_fn)
    _exz, rxz = edge_integral(x, z, coframe_fn, omega_fn)

    torsion_disc = va(va(exy, mv(rxy, eyz)), mv(rxz, ezx))
    affine_loop_translation = va(va(exy, mv(rxy, eyz)), mv(mm(rxy, ryz), ezx))
    r_loop = mm(mm(rxy, ryz), rzx)
    area = 0.5 * h * h
    return {
        "h": h,
        "area": area,
        "torsion_density": vscale(1.0 / area, torsion_disc),
        "affine_translation_density": vscale(1.0 / area, affine_loop_translation),
        "translation_solder_gap_density": vscale(
            1.0 / area, vs(affine_loop_translation, torsion_disc)
        ),
        "curvature_density": smul(1.0 / area, anti(r_loop)),
        "raw_torsion": torsion_disc,
        "raw_loop_translation": affine_loop_translation,
        "raw_rotation": r_loop,
    }


def reference_torsion_12():
    # d_1 e_2 - d_2 e_1 at x=0.
    d1e2 = (0.25, 0.0, -0.3)
    d2e1 = (0.0, 0.4, 0.2)
    e1 = base_coframe(0, (0.0, 0.0))
    e2 = base_coframe(1, (0.0, 0.0))
    return va(vs(d1e2, d2e1), vs(mv(OMEGA_1, e2), mv(OMEGA_2, e1)))


def reference_curvature_12():
    # Constant connection: d omega = 0, Omega_12=[omega_1,omega_2].
    return commutator(OMEGA_1, OMEGA_2)


def euclidean_coframe(mu, _p):
    return ((1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0))[mu]


def zero_omega(_mu, _p):
    return Z3


def transformed_fields(q):
    qt = transpose(q)

    def coframe(mu, p):
        return mv(q, base_coframe(mu, p))

    def omega(mu, p):
        return mm(q, mm(base_omega(mu, p), qt))

    return coframe, omega


def coframe_matrix_at(p, coframe_fn=base_coframe):
    # columns are e_mu internal vectors
    cols = [coframe_fn(mu, p) for mu in range(3)]
    return tuple(tuple(cols[j][i] for j in range(3)) for i in range(3))


def gram_metric(e_matrix):
    return mm(transpose(e_matrix), e_matrix)


def strictly_descending(values):
    return all(values[i + 1] < values[i] for i in range(len(values) - 1))


def contraction_ratios(values):
    return [values[i + 1] / values[i] for i in range(len(values) - 1) if values[i] > 0.0]


def main():
    checks = []
    tref = reference_torsion_12()
    oref = reference_curvature_12()

    hs = (0.2, 0.1, 0.05, 0.025)
    samples = [triangle_sample(h) for h in hs]
    torsion_errors = [vnorm(vs(s["torsion_density"], tref)) for s in samples]
    affine_errors = [vnorm(vs(s["affine_translation_density"], tref)) for s in samples]
    gap_errors = [vnorm(s["translation_solder_gap_density"]) for s in samples]
    curvature_errors = [mnorm(ms(s["curvature_density"], oref)) for s in samples]

    convergence_ok = (
        strictly_descending(torsion_errors)
        and strictly_descending(affine_errors)
        and strictly_descending(gap_errors)
        and strictly_descending(curvature_errors)
        and max(contraction_ratios(torsion_errors)) < 0.7
        and max(contraction_ratios(affine_errors)) < 0.7
        and max(contraction_ratios(gap_errors)) < 0.7
        and max(contraction_ratios(curvature_errors)) < 0.7
        and torsion_errors[-1] < 4e-3
        and affine_errors[-1] < 4e-3
        and gap_errors[-1] < 2e-3
        and curvature_errors[-1] < 4e-4
    )
    checks.append({
        "name": "cartan_torsion_and_curvature_refinement_convergence",
        "pass": convergence_ok,
        "h": list(hs),
        "torsion_errors": torsion_errors,
        "affine_translation_errors": affine_errors,
        "translation_solder_gap_errors": gap_errors,
        "curvature_errors": curvature_errors,
    })

    # The analytic target is nondegenerate in both torsion and curvature channels.
    checks.append({
        "name": "analytic_reference_channels_nonzero",
        "pass": vnorm(tref) > 0.1 and mnorm(oref) > 0.01,
        "torsion_12": tref,
        "curvature_12_frobenius": mnorm(oref),
    })

    # Constant internal frame covariance.
    q = rotation(0.41, -0.27)
    coframe_q, omega_q = transformed_fields(q)
    base_sample = triangle_sample(0.05)
    q_sample = triangle_sample(0.05, coframe_q, omega_q)
    q_tref = mv(q, tref)
    q_oref = mm(q, mm(oref, transpose(q)))
    frame_error = max(
        maxv(q_sample["torsion_density"], mv(q, base_sample["torsion_density"])),
        maxv(
            q_sample["affine_translation_density"],
            mv(q, base_sample["affine_translation_density"]),
        ),
        maxm(
            q_sample["curvature_density"],
            mm(q, mm(base_sample["curvature_density"], transpose(q))),
        ),
        vnorm(vs(q_tref, mv(q, tref))),
        mnorm(ms(q_oref, mm(q, mm(oref, transpose(q))))),
    )
    checks.append({
        "name": "constant_internal_frame_covariance",
        "pass": frame_error < TOL,
        "max_error": frame_error,
    })

    # Euclidean torsion-free / curvature-free baseline.
    flat = triangle_sample(0.13, euclidean_coframe, zero_omega)
    flat_error = max(
        vnorm(flat["torsion_density"]),
        vnorm(flat["affine_translation_density"]),
        mnorm(ms(flat["raw_rotation"], I3)),
    )
    checks.append({
        "name": "euclidean_zero_torsion_zero_curvature_baseline",
        "pass": flat_error < 1e-11,
        "max_error": flat_error,
    })

    # Full-rank coframe and positive spatial metric on the reference patch.
    metric_min_det = float("inf")
    metric_sym_error = 0.0
    for p in ((0.0, 0.0), (0.1, 0.0), (0.0, 0.1), (0.1, 0.1)):
        e = coframe_matrix_at(p)
        h = gram_metric(e)
        metric_min_det = min(metric_min_det, determinant(h))
        metric_sym_error = max(metric_sym_error, maxm(h, transpose(h)))
    checks.append({
        "name": "full_rank_coframe_positive_metric_reference_patch",
        "pass": metric_min_det > 0.5 and metric_sym_error < TOL,
        "minimum_metric_determinant": metric_min_det,
        "symmetry_error": metric_sym_error,
    })

    # Explicit leading-limit agreement at finest scale.
    finest = samples[-1]
    leading_error = max(
        vnorm(vs(finest["torsion_density"], tref)),
        vnorm(vs(finest["affine_translation_density"], tref)),
        mnorm(ms(finest["curvature_density"], oref)),
    )
    checks.append({
        "name": "finest_scale_leading_cartan_limit",
        "pass": leading_error < 4e-3,
        "max_error": leading_error,
    })

    passed = all(check["pass"] for check in checks)
    receipt = {
        "schema": "TIR_CARTAN_CONTINUUM_REFINEMENT_VALIDATION_V0_1",
        "technical_status": "PASS" if passed else "FAIL",
        "evidence_class": "SYNTHETIC_ANALYTIC_FAMILY_CONVERGENCE_REFERENCE",
        "verdict": (
            "PASS_TIR_CARTAN_CONTINUUM_REFINEMENT"
            if passed
            else "FAIL_TIR_CARTAN_CONTINUUM_REFINEMENT"
        ),
        "continuum_targets": {
            "torsion": "T^a = de^a + omega^a_b wedge e^b",
            "curvature": "Omega^a_b = d omega^a_b + omega^a_c wedge omega^c_b",
            "metric": "h_mn = delta_ab e^a_m e^b_n",
        },
        "refinement_results": {
            "T_disc_over_area": "converges to T_12",
            "SE3_translation_over_area": "converges to T_12",
            "antisymmetric_rotation_holonomy_over_area": "converges to Omega_12",
            "SE3_translation_minus_solder_torsion_over_area": "converges to zero",
        },
        "physical_refining_family_binding": "NEXT_SOURCE_RECEIPT",
        "checks": checks,
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
