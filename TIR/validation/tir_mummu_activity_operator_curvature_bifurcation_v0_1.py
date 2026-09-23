#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np

SCHEMA = "TIR_MUMMU_ACTIVITY_OPERATOR_CURVATURE_BIFURCATION_VALIDATION_V0_1"
HERE = Path(__file__).resolve().parent
SOURCE_VALIDATOR = HERE / "tir_mummu_source_operator_nonabelianity_firewall_v0_1.py"

spec = importlib.util.spec_from_file_location("mummu_source_firewall", SOURCE_VALIDATOR)
if spec is None or spec.loader is None:
    raise RuntimeError("unable to load source-operator firewall validator")
src = importlib.util.module_from_spec(spec)
spec.loader.exec_module(src)


def activity(f2: float, f3: float, f4: float) -> float:
    raw = (f2 + 0.5 * f4 + 0.3 * (1.0 - f3)) / 1.8
    return min(max(raw, 0.0), 1.0)


def raw_activity(f2: float, f3: float, f4: float) -> float:
    return (10.0 * f2 + 5.0 * f4 + 3.0 * (1.0 - f3)) / 18.0


def main():
    checks = []

    # Exact algebraic equivalence of decimal and integer-weight forms.
    rng = np.random.default_rng(260923)
    samples = rng.normal(size=(100, 3)) * 2.0
    form_errors = []
    sign_errors = []
    for f2, f3, f4 in samples:
        raw_decimal = (f2 + 0.5 * f4 + 0.3 * (1.0 - f3)) / 1.8
        raw_integer = raw_activity(float(f2), float(f3), float(f4))
        form_errors.append(abs(raw_decimal - raw_integer))

        A = activity(float(f2), float(f3), float(f4))
        lhs = np.sign(A - 0.5)
        rhs = np.sign(raw_integer - 0.5)
        sign_errors.append(abs(float(lhs - rhs)))

    checks.append({
        "name": "integer_weight_activity_form_and_clipped_sign_boundary",
        "status": (
            "PASS"
            if max(form_errors) < 2e-15 and max(sign_errors) == 0.0
            else "FAIL"
        ),
        "max_form_abs_error": max(form_errors),
        "max_sign_difference": max(sign_errors),
    })

    # Hyperplane samples: exact midpoint and both sides.
    midpoint = activity(0.6, 0.2, 0.2)
    # 10*.6 + 5*.2 + 3*.8 = 9.4, not midpoint; construct exactly:
    # choose f3=.5, f4=.5 -> 10 f2 + 2.5 + 1.5 = 9 => f2=.5
    midpoint = activity(0.5, 0.5, 0.5)
    below = activity(0.49, 0.5, 0.5)
    above = activity(0.51, 0.5, 0.5)
    checks.append({
        "name": "activity_half_hyperplane_controls_hebbian_sign",
        "status": (
            "PASS"
            if abs(midpoint - 0.5) < 1e-15
            and below < 0.5
            and above > 0.5
            else "FAIL"
        ),
        "midpoint": midpoint,
        "below": below,
        "above": above,
    })

    # Conditional convexity for normalized inputs.
    normalized = rng.uniform(0.0, 1.0, size=(1000, 3))
    raw_vals = np.asarray([
        raw_activity(float(f2), float(f3), float(f4))
        for f2, f3, f4 in normalized
    ])
    weights_sum = 5.0/9.0 + 5.0/18.0 + 1.0/6.0
    checks.append({
        "name": "normalized_flavor_domain_gives_barycentric_activity",
        "status": (
            "PASS"
            if abs(weights_sum - 1.0) < 1e-15
            and float(raw_vals.min()) >= 0.0
            and float(raw_vals.max()) <= 1.0
            else "FAIL"
        ),
        "weights": [5.0/9.0, 5.0/18.0, 1.0/6.0],
        "weights_sum": weights_sum,
        "sample_min": float(raw_vals.min()),
        "sample_max": float(raw_vals.max()),
    })

    # Pinned source value.
    f2, f3, f4 = 0.23, 0.56, 0.48
    A0 = activity(f2, f3, f4)
    lambda0 = 0.1 * (A0 - 0.5)
    checks.append({
        "name": "pinned_source_activity_and_signed_gain",
        "status": (
            "PASS"
            if abs(A0 - 0.33444444444444443) < 1e-15
            and abs(lambda0 + 0.016555555555555556) < 1e-15
            else "FAIL"
        ),
        "activity": A0,
        "lambda_h": lambda0,
    })

    # Source operator curvature factorization.
    phi = np.linspace(0.07, 5.91, src.N, dtype=np.float64)
    idx = np.arange(src.N, dtype=np.float64)
    g = 0.18 * np.cos((idx[:, None] - idx[None, :]) * np.pi / 18.0)
    g = 0.5 * (g + g.T)
    np.fill_diagonal(g, 0.0)

    phase = src.harmonic_composite_phase(phi)
    C = np.cos(phase[:, None] - phase[None, :])
    C = 0.5 * (C + C.T)
    np.fill_diagonal(C, 0.0)

    j = 0.5 * (g + g.T)
    np.fill_diagonal(j, 0.0)
    rho = float(np.max(np.abs(np.linalg.eigvalsh(j))))
    geom_comm = j @ C - C @ j
    geom_norm = float(np.linalg.norm(geom_comm, "fro"))

    def curvature(A):
        lam = 0.1 * (A - 0.5)
        M = (lam / (rho * rho)) * geom_comm
        return M, float(np.linalg.norm(M, "fro"))

    M_minus, norm_minus = curvature(0.3)
    M_zero, norm_zero = curvature(0.5)
    M_plus, norm_plus = curvature(0.7)
    orientation_error = float(np.max(np.abs(M_plus + M_minus)))
    magnitude_error = abs(norm_plus - norm_minus)
    checks.append({
        "name": "activity_half_is_exact_hebbian_operator_curvature_bifurcation",
        "status": (
            "PASS"
            if geom_norm > 1.0
            and norm_zero == 0.0
            and norm_minus > 0.0
            and norm_plus > 0.0
            and orientation_error < 1e-15
            and magnitude_error < 1e-15
            else "FAIL"
        ),
        "geometry_commutator_frobenius": geom_norm,
        "negative_side_curvature_norm": norm_minus,
        "midpoint_curvature_norm": norm_zero,
        "positive_side_curvature_norm": norm_plus,
        "orientation_reversal_max_abs_error": orientation_error,
        "symmetric_magnitude_abs_error": magnitude_error,
    })

    # Gain range follows only from clipping.
    probe_raw = [-100.0, -1.0, 0.0, 0.5, 1.0, 2.0, 100.0]
    gains = [
        0.1 * (min(max(x, 0.0), 1.0) - 0.5)
        for x in probe_raw
    ]
    checks.append({
        "name": "clipped_activity_bounds_hebbian_gain",
        "status": "PASS" if min(gains) >= -0.05 and max(gains) <= 0.05 else "FAIL",
        "min_gain": min(gains),
        "max_gain": max(gains),
    })

    status = "PASS" if all(c["status"] == "PASS" for c in checks) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "claim_scope": (
            "the PNCS activity law defines an exact affine sign hyperplane for the "
            "Hebbian gain and, when weak boost/clipping are locally inactive, an exact "
            "operator-curvature sign bifurcation; barycentric interpretation requires "
            "normalized flavor inputs and the 10:5:3 weights remain source policy"
        ),
        "source_pins": {
            "pncs_main": "8855abed440e9949f576ffbe2153325f69e78963",
            "source_firewall_validator": SOURCE_VALIDATOR.name,
        },
        "checks": checks,
        "summary": {
            "passed": sum(c["status"] == "PASS" for c in checks),
            "total": len(checks),
        },
    }

    Path(__file__).with_name(
        "TIR_MUMMU_ACTIVITY_OPERATOR_CURVATURE_BIFURCATION_VALIDATION_V0_1.json"
    ).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
