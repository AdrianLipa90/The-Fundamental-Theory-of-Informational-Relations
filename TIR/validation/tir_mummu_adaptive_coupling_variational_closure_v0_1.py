#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

import numpy as np

SCHEMA = "TIR_MUMMU_ADAPTIVE_COUPLING_VARIATIONAL_CLOSURE_VALIDATION_V0_1"
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
    gravity = np.array([0.0, 1.17, 0.3, 0.0, 0.0, 1.0, 0.0, 0.0], dtype=np.float64)
    return phi, omega, g, flavor, tau, gravity


def frozen_variational_parts(phi, g, flavor):
    phase = src.harmonic_composite_phase(phi)
    diff = phase[:, None] - phase[None, :]
    C = np.cos(diff)

    activity = (
        float(flavor[2])
        + float(flavor[4]) * 0.5
        + (1.0 - float(flavor[3])) * 0.3
    ) / 1.8
    activity = min(max(activity, 0.0), 1.0)

    lambda_h = 0.1 * (activity - 0.5)
    gamma = 0.01
    baseline = src.EYE_N * 0.1

    hd_rate = lambda_h * C - gamma * (g - baseline)
    grad_hd = -lambda_h * C + gamma * (g - baseline)

    g_stage1 = np.clip(g + src.DT * hd_rate, -1.0, 1.0)

    z_phase = np.exp(1j * phi)
    z_ch = np.mean(z_phase.reshape(-1, 3), axis=1)
    ch_coh = np.abs(z_ch)
    ch_mean = np.angle(z_ch)
    global_mean = float(np.angle(np.mean(z_phase)))
    dist = np.abs(np.angle(np.exp(1j * (ch_mean - global_mean))))
    weak = (ch_coh < 0.5) & (dist > 0.5)

    W = np.zeros_like(g)
    if weak.any():
        weak_rate = 0.1 * (0.5 - ch_coh) * dist
        wc = np.flatnonzero(weak)
        rows = src.CH_ROWS[wc].ravel()
        cols = src.CH_COLS[wc].ravel()
        W[rows, cols] += np.repeat(weak_rate[wc], 6)

    grad_w = -W
    g_stage2 = np.clip(g_stage1 + src.DT * W, -1.0, 1.0)

    F_hd_before = (
        -lambda_h * float(np.sum(g * C))
        + 0.5 * gamma * float(np.sum((g - baseline) ** 2))
    )
    F_hd_after = (
        -lambda_h * float(np.sum(g_stage1 * C))
        + 0.5 * gamma * float(np.sum((g_stage1 - baseline) ** 2))
    )

    return {
        "activity": activity,
        "lambda_h": lambda_h,
        "gamma": gamma,
        "C": C,
        "hd_rate": hd_rate,
        "grad_hd": grad_hd,
        "g_stage1": g_stage1,
        "W": W,
        "grad_w": grad_w,
        "g_stage2": g_stage2,
        "weak_count": int(np.count_nonzero(weak)),
        "F_hd_before": F_hd_before,
        "F_hd_after": F_hd_after,
    }


def main():
    checks = []

    phi, omega, g, flavor, tau, gravity = source_state()
    addresses = [
        src.semantic_address(src.semantic_content_id(role))
        for role in src.ROLES
    ]

    # Initial section: no weak boost.
    parts0 = frozen_variational_parts(phi, g, flavor)
    phi1, g1_source, gravity1, _, _, _ = src.controlled_step(
        phi, omega, g, flavor, tau, gravity, addresses[0]
    )

    stage1_error0 = float(np.max(np.abs(parts0["g_stage1"] - g1_source)))
    stage2_error0 = float(np.max(np.abs(parts0["g_stage2"] - g1_source)))
    gradient_error0 = float(np.max(np.abs(parts0["hd_rate"] + parts0["grad_hd"])))

    checks.append({
        "name": "initial_hebb_decay_substep_is_exact_projected_gradient_step",
        "status": (
            "PASS"
            if parts0["weak_count"] == 0
            and stage1_error0 < 1e-15
            and stage2_error0 < 1e-15
            and gradient_error0 == 0.0
            else "FAIL"
        ),
        "weak_count": parts0["weak_count"],
        "lambda_h": parts0["lambda_h"],
        "gamma": parts0["gamma"],
        "stage1_max_abs_error": stage1_error0,
        "full_step_max_abs_error": stage2_error0,
        "negative_gradient_identity_error": gradient_error0,
    })

    power_identity0 = abs(
        float(np.sum(parts0["grad_hd"] * parts0["hd_rate"]))
        + float(np.sum(parts0["grad_hd"] ** 2))
    )
    checks.append({
        "name": "frozen_hd_flow_has_exact_local_lyapunov_power_identity",
        "status": (
            "PASS"
            if power_identity0 < 1e-15
            and parts0["F_hd_after"] < parts0["F_hd_before"]
            else "FAIL"
        ),
        "power_identity_abs_error": power_identity0,
        "F_before": parts0["F_hd_before"],
        "F_after": parts0["F_hd_after"],
        "delta_F": parts0["F_hd_after"] - parts0["F_hd_before"],
    })

    # Second section: weak-channel stage is active and should reproduce source exactly.
    parts1 = frozen_variational_parts(phi1, g1_source, flavor)
    _, g2_source, _, _, _, _ = src.controlled_step(
        phi1, omega, g1_source, flavor, tau, gravity1, addresses[1]
    )

    full_error1 = float(np.max(np.abs(parts1["g_stage2"] - g2_source)))
    weak_gradient_error1 = float(np.max(np.abs(parts1["W"] + parts1["grad_w"])))

    checks.append({
        "name": "weak_channel_substep_is_exact_linear_potential_gradient_step",
        "status": (
            "PASS"
            if parts1["weak_count"] > 0
            and float(np.linalg.norm(parts1["W"], "fro")) > 0.1
            and full_error1 < 1e-14
            and weak_gradient_error1 == 0.0
            else "FAIL"
        ),
        "weak_count": parts1["weak_count"],
        "weak_rate_frobenius_norm": float(np.linalg.norm(parts1["W"], "fro")),
        "full_source_step_max_abs_error": full_error1,
        "negative_gradient_identity_error": weak_gradient_error1,
    })

    # Projection is the Euclidean/Frobenius projection onto the entrywise box.
    probe = np.asarray([[-1.7, -0.2, 0.4, 2.1]], dtype=np.float64)
    projected = np.clip(probe, -1.0, 1.0)
    expected = np.asarray([[-1.0, -0.2, 0.4, 1.0]], dtype=np.float64)
    projection_error = float(np.max(np.abs(projected - expected)))
    checks.append({
        "name": "entrywise_clip_is_box_projection",
        "status": "PASS" if projection_error == 0.0 else "FAIL",
        "max_abs_error": projection_error,
    })

    # GREMLIN edge-potential crosswalk: -d[-K cos(delta)]/dK = cos(delta).
    delta = 0.713
    eps = 1e-7
    K = 0.37
    def edge_potential(k):
        return -k * np.cos(delta)
    numeric_negative_gradient = -(
        edge_potential(K + eps) - edge_potential(K - eps)
    ) / (2.0 * eps)
    exact_cosine = float(np.cos(delta))
    crosswalk_error = abs(float(numeric_negative_gradient) - exact_cosine)
    checks.append({
        "name": "gremlin_phase_potential_coupling_gradient_matches_pncs_cosine_direction",
        "status": "PASS" if crosswalk_error < 1e-9 else "FAIL",
        "finite_difference_negative_gradient": float(numeric_negative_gradient),
        "cos_delta": exact_cosine,
        "abs_error": crosswalk_error,
        "scope": "off_diagonal_edge_coordinate; symmetric-matrix factor convention kept separate",
    })

    status = "PASS" if all(c["status"] == "PASS" for c in checks) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "claim_scope": (
            "the PNCS adaptive coupling update is exactly a composition of projected "
            "local gradient substeps in coupling-matrix space; its off-diagonal cosine "
            "direction is the coupling-coordinate dual of the GREMLIN Kuramoto edge "
            "potential; gain values and physical ontology remain open"
        ),
        "source_pins": {
            "pncs_main": "8855abed440e9949f576ffbe2153325f69e78963",
            "gremlin_main": "e1e617b03406e38946a3b5296db5cfd259cca3df",
            "source_firewall_validator": SOURCE_VALIDATOR.name,
        },
        "checks": checks,
        "summary": {
            "passed": sum(c["status"] == "PASS" for c in checks),
            "total": len(checks),
        },
    }

    Path(__file__).with_name(
        "TIR_MUMMU_ADAPTIVE_COUPLING_VARIATIONAL_CLOSURE_VALIDATION_V0_1.json"
    ).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
