#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

SCHEMA = "TIR_MUMMU_COUPLING_MOBILITY_GAIN_IDENTIFIABILITY_NOGO_VALIDATION_V0_1"
N = 36


def frozen_flow(g, C, g0, mu, alpha, beta):
    return mu * alpha * C - mu * beta * (g - g0)


def main():
    checks = []

    idx = np.arange(N, dtype=np.float64)
    phi = np.linspace(0.07, 5.91, N, dtype=np.float64)
    C = np.cos(phi[:, None] - phi[None, :])
    g = 0.18 * np.cos((idx[:, None] - idx[None, :]) * math.pi / 18.0)
    g0 = 0.1 * np.eye(N, dtype=np.float64)

    mu = 2.7
    alpha = -0.006131687242798354
    beta = 0.003703703703703704
    h = mu * alpha
    d = mu * beta

    reference = frozen_flow(g, C, g0, mu, alpha, beta)
    gauge_errors = []
    for c in (0.13, 0.7, 1.0, 3.4, 11.0):
        got = frozen_flow(
            g, C, g0,
            c * mu,
            alpha / c,
            beta / c,
        )
        gauge_errors.append(float(np.max(np.abs(got - reference))))

    checks.append({
        "name": "mobility_potential_rescaling_gauge",
        "status": "PASS" if max(gauge_errors) < 1e-15 else "FAIL",
        "max_abs_error": max(gauge_errors),
        "probe_scalings": [0.13, 0.7, 1.0, 3.4, 11.0],
    })

    product_error = max(
        abs(h - mu * alpha),
        abs(d - mu * beta),
        abs((h / d) - (alpha / beta)),
    )
    checks.append({
        "name": "runtime_products_and_ratio_identity",
        "status": "PASS" if product_error < 1e-15 else "FAIL",
        "h": h,
        "d": d,
        "h_over_d": h / d,
        "alpha_over_beta": alpha / beta,
        "max_abs_error": product_error,
    })

    activity = (0.23 + 0.48 * 0.5 + (1.0 - 0.56) * 0.3) / 1.8
    h_pncs = 0.1 * (activity - 0.5)
    d_pncs = 0.01
    ratio = h_pncs / d_pncs
    expected_ratio = 10.0 * (activity - 0.5)
    checks.append({
        "name": "pinned_pncs_effective_gain_ratio",
        "status": "PASS" if abs(ratio - expected_ratio) < 1e-15 else "FAIL",
        "activity": activity,
        "h": h_pncs,
        "d": d_pncs,
        "h_over_d": ratio,
        "expected": expected_ratio,
    })

    g_star = g0 + ratio * C
    stationarity = h_pncs * C - d_pncs * (g_star - g0)
    stationary_error = float(np.max(np.abs(stationarity)))
    outside_fraction = float(np.mean((g_star < -1.0) | (g_star > 1.0)))
    checks.append({
        "name": "frozen_unconstrained_stationary_point",
        "status": (
            "PASS"
            if stationary_error < 1e-15 and outside_fraction > 0.0
            else "FAIL"
        ),
        "max_stationarity_error": stationary_error,
        "fraction_outside_box": outside_fraction,
        "g_star_min": float(np.min(g_star)),
        "g_star_max": float(np.max(g_star)),
    })

    # Common rate scaling is exactly time reparameterization for the frozen
    # affine flow. Analytic solution:
    # g(t)-g* = exp(-d t) [g(0)-g*].
    t = 0.37
    s = 4.2
    base = g_star + math.exp(-d_pncs * t) * (g - g_star)
    scaled = g_star + math.exp(-(s * d_pncs) * (t / s)) * (g - g_star)
    time_error = float(np.max(np.abs(base - scaled)))
    checks.append({
        "name": "common_flow_rate_is_time_reparameterization_before_clock_binding",
        "status": "PASS" if time_error < 1e-15 else "FAIL",
        "max_abs_error": time_error,
        "scale": s,
    })

    # Proper-time factor can recover h,d from their coordinate-time rates, but
    # cannot split h=mu*alpha or d=mu*beta.
    q = 1.73
    h_tau = h_pncs / q
    d_tau = d_pncs / q
    recovered_h = q * h_tau
    recovered_d = q * d_tau
    c = 5.0
    mu_a, alpha_a, beta_a = 1.0, h_pncs, d_pncs
    mu_b, alpha_b, beta_b = c, h_pncs / c, d_pncs / c
    split_same = max(
        abs(mu_a * alpha_a - mu_b * alpha_b),
        abs(mu_a * beta_a - mu_b * beta_b),
    )
    checks.append({
        "name": "proper_time_recovers_effective_rates_not_internal_factorization",
        "status": (
            "PASS"
            if abs(recovered_h - h_pncs) < 1e-15
            and abs(recovered_d - d_pncs) < 1e-15
            and split_same < 1e-15
            and mu_a != mu_b
            else "FAIL"
        ),
        "proper_time_factor": q,
        "recovered_h": recovered_h,
        "recovered_d": recovered_d,
        "alternative_mobilities": [mu_a, mu_b],
        "factorization_product_error": split_same,
    })

    # Same gauge in a frozen weak-channel direction.
    W = np.zeros((N, N), dtype=np.float64)
    W[0, 1] = W[1, 0] = 0.23
    zeta = 0.041
    weak_ref = mu * zeta * W
    weak_alt = (c * mu) * (zeta / c) * W
    weak_error = float(np.max(np.abs(weak_ref - weak_alt)))
    checks.append({
        "name": "weak_channel_mobility_gain_factorization_is_also_nonidentifiable",
        "status": "PASS" if weak_error < 1e-15 else "FAIL",
        "max_abs_error": weak_error,
    })

    status = "PASS" if all(x["status"] == "PASS" for x in checks) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "claim_scope": (
            "a scalar coupling-space gradient mobility and potential normalization "
            "are not separately identifiable from the adaptive coupling trajectory; "
            "only their effective products are, while proper-time binding calibrates "
            "flow rates but does not break the internal mobility/potential gauge"
        ),
        "checks": checks,
        "summary": {
            "passed": sum(x["status"] == "PASS" for x in checks),
            "total": len(checks),
        },
    }

    Path(__file__).with_name(
        "TIR_MUMMU_COUPLING_MOBILITY_GAIN_IDENTIFIABILITY_NOGO_VALIDATION_V0_1.json"
    ).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
