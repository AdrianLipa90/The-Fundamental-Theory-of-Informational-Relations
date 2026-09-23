#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

SCHEMA = "TIR_MUMMU_ADAPTIVE_GAIN_STABILITY_SELECTION_NOGO_VALIDATION_V0_1"


def main():
    checks = []

    d = 0.01
    dt = 0.01
    z = d * dt

    checks.append({
        "name": "source_decay_step_is_strictly_inside_euler_stability_interval",
        "status": "PASS" if 0.0 < z < 2.0 else "FAIL",
        "d": d,
        "dt": dt,
        "d_dt": z,
        "upper_boundary": 2.0,
        "fraction_of_upper_boundary": z / 2.0,
        "stable_d_max": 2.0 / dt,
        "margin_factor_to_upper_boundary": (2.0 / dt) / d,
    })

    # Exact error contraction across a range of stable decay rates.
    rng = np.random.default_rng(260923)
    e0 = rng.normal(size=(36, 36))
    probes = [0.001, 0.01, 1.0, 50.0, 99.0, 150.0, 199.0]
    contractions = []
    all_stable = True
    for dp in probes:
        factor = 1.0 - dp * dt
        e1 = factor * e0
        ratio = float(np.linalg.norm(e1, "fro") / np.linalg.norm(e0, "fro"))
        contractions.append({"d": dp, "factor": factor, "norm_ratio": ratio})
        all_stable = all_stable and ratio < 1.0
    checks.append({
        "name": "many_distinct_decay_gains_are_stable",
        "status": "PASS" if all_stable else "FAIL",
        "probes": contractions,
    })

    # Strict Lyapunov descent has exactly the squared contraction ratio.
    d_probe = 73.0
    factor = 1.0 - d_probe * dt
    F0 = 0.5 * float(np.sum(e0 * e0))
    e1 = factor * e0
    F1 = 0.5 * float(np.sum(e1 * e1))
    expected_ratio = factor * factor
    lyap_error = abs(F1 / F0 - expected_ratio)
    checks.append({
        "name": "discrete_quadratic_lyapunov_ratio_matches_euler_factor_squared",
        "status": "PASS" if lyap_error < 1e-15 and F1 < F0 else "FAIL",
        "d": d_probe,
        "F1_over_F0": F1 / F0,
        "expected": expected_ratio,
        "abs_error": lyap_error,
    })

    # At boundary d*dt=2, energy does not decrease; beyond it grows.
    boundary_factor = 1.0 - (2.0 / dt) * dt
    beyond_factor = 1.0 - (2.1 / dt) * dt
    checks.append({
        "name": "stability_boundary_is_exact_not_gain_selecting",
        "status": (
            "PASS"
            if abs(boundary_factor) == 1.0 and abs(beyond_factor) > 1.0
            else "FAIL"
        ),
        "boundary_abs_factor": abs(boundary_factor),
        "beyond_abs_factor": abs(beyond_factor),
    })

    # Projection onto box is nonexpansive under Frobenius norm.
    X = rng.normal(size=(36, 36)) * 3.0
    Y = rng.normal(size=(36, 36)) * 3.0
    PX = np.clip(X, -1.0, 1.0)
    PY = np.clip(Y, -1.0, 1.0)
    before = float(np.linalg.norm(X - Y, "fro"))
    after = float(np.linalg.norm(PX - PY, "fro"))
    checks.append({
        "name": "entrywise_box_projection_is_nonexpansive",
        "status": "PASS" if after <= before + 1e-14 else "FAIL",
        "distance_before": before,
        "distance_after": after,
    })

    # Hebbian term translates fixed point but does not change scalar Hessian d I.
    C = rng.normal(size=(36, 36))
    g0 = np.zeros((36, 36))
    h_values = [-7.0, -0.1, 0.0, 0.2, 9.0]
    hessian_values = []
    for h in h_values:
        # finite-difference derivative of vector field wrt g in one coordinate
        eps = 1e-7
        g = rng.normal(size=(36, 36))
        base = h * C - d * (g - g0)
        gp = g.copy()
        gp[0, 0] += eps
        perturbed = h * C - d * (gp - g0)
        derivative = (perturbed[0, 0] - base[0, 0]) / eps
        hessian_values.append(derivative)
    max_hess_error = max(abs(x + d) for x in hessian_values)
    checks.append({
        "name": "hebbian_linear_gain_does_not_change_frozen_flow_curvature",
        "status": "PASS" if max_hess_error < 1e-8 else "FAIL",
        "probe_h_values": h_values,
        "flow_jacobian_diagonal_estimates": hessian_values,
        "max_abs_error_vs_minus_d": max_hess_error,
    })

    status = "PASS" if all(c["status"] == "PASS" for c in checks) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "claim_scope": (
            "frozen local Euler/Lyapunov stability constrains the effective decay "
            "rate to an interval and does not uniquely select the current PNCS gain; "
            "the linear Hebbian and weak drives are not fixed by the quadratic "
            "curvature stability condition"
        ),
        "checks": checks,
        "summary": {
            "passed": sum(c["status"] == "PASS" for c in checks),
            "total": len(checks),
        },
    }

    Path(__file__).with_name(
        "TIR_MUMMU_ADAPTIVE_GAIN_STABILITY_SELECTION_NOGO_VALIDATION_V0_1.json"
    ).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
