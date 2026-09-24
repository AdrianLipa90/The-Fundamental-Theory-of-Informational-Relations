#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path

import numpy as np

SCHEMA = "TIR_MUMMU_QHTRI_UPSTREAM_TANGENT_MATCHING_NOGO_VALIDATION_V0_1"
HERE = Path(__file__).resolve().parent
SOURCE_VALIDATOR = HERE / "tir_mummu_source_operator_nonabelianity_firewall_v0_1.py"

spec = importlib.util.spec_from_file_location("mummu_source_firewall", SOURCE_VALIDATOR)
if spec is None or spec.loader is None:
    raise RuntimeError("unable to load source-operator firewall validator")
src = importlib.util.module_from_spec(spec)
spec.loader.exec_module(src)


def source_state():
    phi = np.linspace(0.07, 5.91, src.N, dtype=np.float64)
    omega = 39.6 + np.linspace(-0.12, 0.12, src.N, dtype=np.float64)
    idx = np.arange(src.N, dtype=np.float64)
    g = 0.18 * np.cos((idx[:, None] - idx[None, :]) * np.pi / 18.0)
    g = 0.5 * (g + g.T)
    np.fill_diagonal(g, 0.0)
    flavor = np.array([0.31, 0.72, 0.23, 0.56, 0.48, 0.5], dtype=np.float64)
    tau = np.linspace(0.21, 0.49, src.N, dtype=np.float64)
    gravity = np.array([0.0, 1.17, 0.3, 0.0, 1.0, 0.0, 0.0, 0.0], dtype=np.float64)
    # Correct source fixture gravity vector from PNCS test.
    gravity = np.array([0.0, 1.17, 0.3, 0.0, 0.0, 1.0, 0.0, 0.0], dtype=np.float64)
    return phi, omega, g, flavor, tau, gravity


def intrinsic_phase_velocity(phi, omega, g, flavor, tau, gravity):
    phi_eff = src.harmonic_composite_phase(phi)
    diff = phi_eff[:, None] - phi_eff[None, :]
    coupling = np.sum(g * np.sin(diff), axis=1) / src.N

    tau_min = float(tau.min())
    tau_range = float(tau.max() - tau_min)
    if tau_range > 1e-12:
        tau_mod = 0.5 + 0.5 * (tau - tau_min) / tau_range
    else:
        tau_mod = np.ones_like(tau) * 0.75
    tardis = min(float(gravity[1]), 2.0)
    coupling *= tau_mod * tardis

    mood_mod = (float(flavor[3]) - 0.5) * src.KAPPA * 50.0
    closure_mod = (1.0 - float(flavor[4])) * src.KAPPA * 30.0
    coherence_damping = float(flavor[0]) * src.KAPPA * 10.0
    effective_omega = omega * (
        1.0 + mood_mod + closure_mod - coherence_damping
    )
    return effective_omega + coupling


def tangent_fit(phi, D, J, velocity):
    psi = np.exp(1j * phi) / math.sqrt(src.N)
    centered = velocity - float(np.mean(velocity))
    y = -(centered * psi)

    A = np.column_stack((D @ psi, J @ psi))
    A_real = np.vstack((A.real, A.imag))
    y_real = np.concatenate((y.real, y.imag))

    coef, *_ = np.linalg.lstsq(A_real, y_real, rcond=None)
    target_norm = float(np.linalg.norm(y_real))
    best_residual = float(np.linalg.norm(A_real @ coef - y_real) / target_norm)
    default_residual = float(
        np.linalg.norm(A_real @ np.asarray((0.25, 0.7)) - y_real) / target_norm
    )
    reversed_default_residual = float(
        np.linalg.norm(A_real @ np.asarray((-0.25, -0.7)) - y_real) / target_norm
    )
    rank = int(np.linalg.matrix_rank(A_real))
    gauge_mean = float(abs(np.mean(centered)))

    return {
        "a_star": float(coef[0]),
        "b_star": float(coef[1]),
        "best_relative_residual": best_residual,
        "default_relative_residual": default_residual,
        "reversed_default_relative_residual": reversed_default_residual,
        "real_design_rank": rank,
        "centered_velocity_mean_abs": gauge_mean,
    }


def main():
    checks = []

    addresses = [
        src.semantic_address(src.semantic_content_id(role))
        for role in src.ROLES
    ]

    phi, omega, g, flavor, tau, gravity = source_state()
    rows = []

    for index, target in enumerate(addresses):
        velocity = intrinsic_phase_velocity(
            phi, omega, g, flavor, tau, gravity
        )

        phi_before = phi.copy()
        phi_next, g_next, gravity_next, _, D, J = src.controlled_step(
            phi, omega, g, flavor, tau, gravity, target
        )

        row = {"index": index, **tangent_fit(phi_before, D, J, velocity)}
        rows.append(row)

        phi, g, gravity = phi_next, g_next, gravity_next

    max_gauge_mean = max(r["centered_velocity_mean_abs"] for r in rows)
    checks.append({
        "name": "global_u1_phase_velocity_removed_before_matching",
        "status": "PASS" if max_gauge_mean < 1e-12 else "FAIL",
        "max_centered_velocity_mean_abs": max_gauge_mean,
    })

    min_rank = min(r["real_design_rank"] for r in rows)
    checks.append({
        "name": "two_generator_real_least_squares_is_well_posed",
        "status": "PASS" if min_rank == 2 else "FAIL",
        "minimum_real_design_rank": min_rank,
    })

    best = [r["best_relative_residual"] for r in rows]
    checks.append({
        "name": "exact_two_generator_tangent_lift_fails_on_all_pinned_sections",
        "status": "PASS" if min(best) > 0.04 else "FAIL",
        "best_relative_residuals": best,
        "minimum": min(best),
        "maximum": max(best),
    })

    defaults = [r["default_relative_residual"] for r in rows]
    reversed_defaults = [r["reversed_default_relative_residual"] for r in rows]
    checks.append({
        "name": "source_defaults_do_not_match_upstream_intrinsic_tangent",
        "status": (
            "PASS"
            if min(defaults) > 4.0
            and min(reversed_defaults) > 2.5
            else "FAIL"
        ),
        "default_relative_residuals": defaults,
        "reversed_default_relative_residuals": reversed_defaults,
    })

    coefficients = [
        {"index": r["index"], "a_star": r["a_star"], "b_star": r["b_star"]}
        for r in rows
    ]
    max_abs_b = max(abs(r["b_star"]) for r in rows)
    min_abs_a = min(abs(r["a_star"]) for r in rows)
    checks.append({
        "name": "best_fit_coefficients_are_not_source_defaults",
        "status": "PASS" if max_abs_b < 0.04 and min_abs_a > 0.07 else "FAIL",
        "coefficients": coefficients,
        "max_abs_b_star": max_abs_b,
        "min_abs_a_star": min_abs_a,
    })

    status = "PASS" if all(c["status"] == "PASS" for c in checks) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "claim_scope": (
            "after removing the global U(1) phase velocity, the pinned upstream "
            "intrinsic classical HTRI tangent is not exactly representable by the "
            "two-generator QHTRI span aD+bJ at any of seven frozen source sections; "
            "the current defaults are not recovered by this tangent-matching route"
        ),
        "source_pins": {
            "pncs_main": "8855abed440e9949f576ffbe2153325f69e78963",
            "source_firewall_validator": SOURCE_VALIDATOR.name,
        },
        "checks": checks,
        "rows": rows,
        "summary": {
            "passed": sum(c["status"] == "PASS" for c in checks),
            "total": len(checks),
        },
    }

    Path(__file__).with_name(
        "TIR_MUMMU_QHTRI_UPSTREAM_TANGENT_MATCHING_NOGO_VALIDATION_V0_1.json"
    ).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
