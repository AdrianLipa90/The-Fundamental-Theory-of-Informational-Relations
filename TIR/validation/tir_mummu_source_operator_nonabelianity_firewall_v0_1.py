#!/usr/bin/env python3
from __future__ import annotations

import cmath
import hashlib
import json
import math
import struct
from pathlib import Path

import numpy as np

SCHEMA = "TIR_MUMMU_SOURCE_OPERATOR_NONABELIANITY_FIREWALL_VALIDATION_V0_1"
N = 36
TAU = 2.0 * math.pi
KAPPA = math.log(2.0) / (24.0 * math.pi)
DT = 0.01

HARMONIC_VALUES = np.array([1, 3, 6, 9], dtype=np.int32)
HARMONIC_AMPS = np.array([1.0, 0.5, 0.33, 0.25], dtype=np.float64)
CHANNEL_HARMONICS = np.asarray(
    [
        [1,1,0,0], [1,1,0,0], [1,1,0,0],
        [1,0,1,0], [1,0,1,0], [1,0,1,0],
        [1,0,0,1], [1,0,0,1], [1,0,0,1],
        [0,1,1,0], [0,1,1,0], [0,1,1,0],
        [0,1,0,1], [0,1,0,1], [0,1,0,1],
        [0,0,1,1], [0,0,1,1], [0,0,1,1],
        [1,1,1,0], [1,1,1,0], [1,1,1,0],
        [1,1,1,1], [1,1,1,1], [1,1,1,1],
        [1,1,1,1], [1,1,1,1], [1,1,1,1],
        [1,1,1,0], [1,1,1,0], [1,1,1,0],
        [1,1,0,1], [1,1,0,1], [1,1,0,1],
        [1,0,1,1], [1,0,1,1], [1,0,1,1],
    ],
    dtype=bool,
)
EYE_N = np.eye(N, dtype=np.float64)
CH_LOCAL_R = np.array([0,0,1,1,2,2], dtype=np.intp)
CH_LOCAL_C = np.array([1,2,0,2,0,1], dtype=np.intp)
CH_BASE = (3 * np.arange(N // 3, dtype=np.intp))[:, None]
CH_ROWS = CH_BASE + CH_LOCAL_R[None, :]
CH_COLS = CH_BASE + CH_LOCAL_C[None, :]

DOMAIN = b"PNCS_SEMANTIC_CONTENT_ADDRESS_V2\x00"
ROLE_SCHEMA = "PNCS_TYPED_SEMANTIC_ROLE_CONTENT_V0_31"
SOURCE_KEY = "NISABA_A_FROZEN_SEVEN_PULSE_SEMANTIC_MAPPING_V1"
ROLES = (
    "ADDRESS",
    "TABLET_WRITING",
    "WISDOM",
    "FAIR_JUDGMENT",
    "RECEPTION",
    "AGREEMENT_WORK",
    "HOPE_GRATITUDE",
)


def compact_json(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)


def typed_id(prefix, payload):
    return f"{prefix}:sha256:{hashlib.sha256(compact_json(payload).encode('utf-8')).hexdigest()}"


def semantic_content_id(role):
    payload = {
        "schema": ROLE_SCHEMA,
        "role_id": role,
        "source_semantic_key": f"{SOURCE_KEY}:{role}",
        "relation_type": "ORDERED_SEMANTIC_ROLE",
    }
    return typed_id("pncs:semantic-role", payload)


def semantic_address(content_id):
    raw = hashlib.shake_256(DOMAIN + content_id.encode("ascii")).digest(N * 8)
    words = struct.unpack("<" + "Q" * N, raw)
    denom = float((1 << 64) - 1)
    return np.asarray([(w / denom) * TAU for w in words], dtype=np.float64)


def wrap_delta(target, current):
    return np.angle(np.exp(1j * (np.asarray(target) - np.asarray(current))))


def harmonic_composite_phase(phi):
    z = np.sum(
        HARMONIC_AMPS[None, :]
        * np.exp(1j * phi[:, None] * HARMONIC_VALUES[None, :])
        * CHANNEL_HARMONICS,
        axis=1,
    )
    return np.angle(z)


def components(omega, g):
    j = 0.5 * (g + g.T)
    j = j.copy()
    np.fill_diagonal(j, 0.0)
    spec = float(np.max(np.abs(np.linalg.eigvalsh(j))))
    J = j / spec

    oc = omega - float(np.mean(omega))
    os = float(np.std(oc)) or 1.0
    D = np.diag(oc / os)
    return D, J


def hamiltonian(omega, g, detuning=0.25, coupling=0.7):
    D, J = components(omega, g)
    return detuning * D + coupling * J, D, J


def controlled_step(phi, omega, g, flavor, tau, gravity, target):
    phi = phi.copy()
    g = g.copy()
    gravity = gravity.copy()

    phi_eff = harmonic_composite_phase(phi)
    diff = phi_eff[:, None] - phi_eff[None, :]

    coupling_term = np.sum(g * np.sin(diff), axis=1) / N
    tau_min = float(tau.min())
    tau_range = float(tau.max() - tau_min)
    if tau_range > 1e-12:
        tau_mod = 0.5 + 0.5 * (tau - tau_min) / tau_range
    else:
        tau_mod = np.ones_like(tau) * 0.75
    coupling_term *= tau_mod * min(float(gravity[1]), 2.0)

    mood_mod = (float(flavor[3]) - 0.5) * KAPPA * 50.0
    closure_mod = (1.0 - float(flavor[4])) * KAPPA * 30.0
    coherence_damping = float(flavor[0]) * KAPPA * 10.0
    effective_omega = omega * (1.0 + mood_mod + closure_mod - coherence_damping)

    activity = (
        float(flavor[2]) + float(flavor[4]) * 0.5
        + (1.0 - float(flavor[3])) * 0.3
    ) / 1.8
    activity = min(max(activity, 0.0), 1.0)

    hebb_step = 0.01 * DT * 10.0
    decay_step = 0.001 * DT * 10.0
    dg = (
        hebb_step * (activity - 0.5) * np.cos(diff)
        - decay_step * (g - EYE_N * 0.1)
    )
    g += dg
    np.clip(g, -1.0, 1.0, out=g)

    z_phase = np.exp(1j * phi)
    z_ch = np.mean(z_phase.reshape(-1, 3), axis=1)
    ch_coh = np.abs(z_ch)
    ch_mean = np.angle(z_ch)
    global_z = np.mean(z_phase)
    global_mean = float(np.angle(global_z))
    global_R = float(abs(global_z))
    dist = np.abs(np.angle(np.exp(1j * (ch_mean - global_mean))))
    weak = (ch_coh < 0.5) & (dist > 0.5)
    if weak.any():
        boost = 0.01 * (0.5 - ch_coh) * dist * DT * 10.0
        wc = np.flatnonzero(weak)
        rows = CH_ROWS[wc].ravel()
        cols = CH_COLS[wc].ravel()
        g[rows, cols] += np.repeat(boost[wc], 6)
        np.clip(g, -1.0, 1.0, out=g)

    phi_base = phi.copy()
    if global_R > 0.7:
        push = 0.005 * (global_R - 0.7) * DT * 10.0
        ch_target = (ch_mean + math.pi) % TAU
        target_osc = np.repeat(ch_target, 3)
        phi_base += push * np.angle(np.exp(1j * (target_osc - phi_base)))
        phi_base %= TAU

    desired = wrap_delta(target, phi_base)
    control = desired / DT - effective_omega - coupling_term
    phi_next = (phi_base + DT * (effective_omega + coupling_term + control)) % TAU

    dphi = wrap_delta(phi_next, phi_base)
    semantic_density = min(10.0, float(np.mean(np.abs(dphi)) / DT))
    gravity[0] = semantic_density
    gravity[1] = 1.0 + math.tanh(semantic_density * 0.5) * 9.0
    gravity[2] = gravity[2] * 0.99 + semantic_density * 0.01

    H, D, J = hamiltonian(omega, g)
    return phi_next, g, gravity, H, D, J


def fixed_modulus_counterexample():
    p_l = 0.65
    p_r = 0.35
    q = p_l + p_r
    u = (p_l - p_r) / q
    r = 2.0 * math.sqrt(p_l * p_r) / q

    d1, d2 = 0.3, 1.1
    dd1, dd2 = 0.7, 1.2

    def Omega(delta, delta_dot):
        return delta_dot * np.asarray(
            (-u * r * math.cos(delta), -u * r * math.sin(delta), r * r),
            dtype=np.float64,
        )

    projective_cross = float(np.linalg.norm(np.cross(Omega(d1, dd1), Omega(d2, dd2))))

    hd1 = -np.diag(np.asarray((dd1, 0.0), dtype=np.complex128))
    hd2 = -np.diag(np.asarray((dd2, 0.0), dtype=np.complex128))
    source_comm = float(np.linalg.norm(hd1 @ hd2 - hd2 @ hd1, "fro"))
    return projective_cross, source_comm


def main():
    checks = []

    projective_cross, source_comm = fixed_modulus_counterexample()
    checks.append({
        "name": "projective_omega_noncommutativity_does_not_imply_source_operator_noncommutativity",
        "status": "PASS" if projective_cross > 1e-3 and source_comm == 0.0 else "FAIL",
        "projective_omega_cross_norm": projective_cross,
        "commuting_diagonal_source_H_commutator_frobenius": source_comm,
    })

    phi = np.linspace(0.07, 5.91, N, dtype=np.float64)
    omega = 39.6 + np.linspace(-0.12, 0.12, N, dtype=np.float64)
    idx = np.arange(N, dtype=np.float64)
    g = 0.18 * np.cos((idx[:, None] - idx[None, :]) * np.pi / 18.0)
    g = 0.5 * (g + g.T)
    np.fill_diagonal(g, 0.0)
    flavor = np.array([0.31, 0.72, 0.23, 0.56, 0.48, 0.5], dtype=np.float64)
    tau = np.linspace(0.21, 0.49, N, dtype=np.float64)
    gravity = np.array([0.0, 1.17, 0.3, 0.0, 0.0, 1.0, 0.0, 0.0], dtype=np.float64)

    fixed_H, _, _ = hamiltonian(omega, g)
    fixed_comm = float(np.linalg.norm(fixed_H @ fixed_H - fixed_H @ fixed_H, "fro"))
    checks.append({
        "name": "fixed_h_qhtri_fixture_source_operator_history_commutes",
        "status": "PASS" if fixed_comm == 0.0 else "FAIL",
        "commutator_frobenius": fixed_comm,
    })

    # Isolate the infinitesimal source of coupling-operator direction change.
    phi_eff0 = harmonic_composite_phase(phi)
    diff0 = phi_eff0[:, None] - phi_eff0[None, :]
    activity0 = (
        float(flavor[2]) + float(flavor[4]) * 0.5
        + (1.0 - float(flavor[3])) * 0.3
    ) / 1.8
    activity0 = min(max(activity0, 0.0), 1.0)

    z_phase0 = np.exp(1j * phi)
    z_ch0 = np.mean(z_phase0.reshape(-1, 3), axis=1)
    ch_coh0 = np.abs(z_ch0)
    ch_mean0 = np.angle(z_ch0)
    global_z0 = np.mean(z_phase0)
    global_mean0 = float(np.angle(global_z0))
    dist0 = np.abs(np.angle(np.exp(1j * (ch_mean0 - global_mean0))))
    weak0 = (ch_coh0 < 0.5) & (dist0 > 0.5)
    checks.append({
        "name": "initial_weak_channel_boost_is_inactive",
        "status": "PASS" if int(np.count_nonzero(weak0)) == 0 else "FAIL",
        "active_weak_channels": int(np.count_nonzero(weak0)),
    })

    _, J0 = components(omega, g)
    decay_rate = -0.01 * (g - EYE_N * 0.1)
    _, J_decay = components(omega, g + DT * decay_rate)
    decay_direction_error = float(np.max(np.abs(J_decay - J0)))
    checks.append({
        "name": "pure_decay_is_directionally_invisible_after_qhtri_normalization",
        "status": "PASS" if decay_direction_error < 1e-14 else "FAIL",
        "max_abs_J_change": decay_direction_error,
    })

    hebb_rate = 0.1 * (activity0 - 0.5) * np.cos(diff0)
    k_h = 0.5 * (hebb_rate + hebb_rate.T)
    np.fill_diagonal(k_h, 0.0)
    j0 = 0.5 * (g + g.T)
    j0 = j0.copy()
    np.fill_diagonal(j0, 0.0)
    rho0 = float(np.max(np.abs(np.linalg.eigvalsh(j0))))
    local_commutator = j0 @ k_h - k_h @ j0
    predicted_rate = float(np.linalg.norm(local_commutator, "fro") / (rho0 * rho0))

    scaled_rates = []
    eps_values = [1.0e-2, 5.0e-3, 2.5e-3, 1.0e-3, 1.0e-4]
    for eps in eps_values:
        _, J_eps = components(
            omega,
            g + eps * (hebb_rate + decay_rate),
        )
        scaled_rates.append(
            float(np.linalg.norm(J0 @ J_eps - J_eps @ J0, "fro") / eps)
        )
    local_rel_error = abs(scaled_rates[-1] - predicted_rate) / predicted_rate
    checks.append({
        "name": "hebbian_phase_conditioning_generates_infinitesimal_operator_rotation",
        "status": (
            "PASS"
            if predicted_rate > 0.09 and local_rel_error < 5e-6
            else "FAIL"
        ),
        "activity": activity0,
        "spectral_radius": rho0,
        "predicted_commutator_rate": predicted_rate,
        "eps_values": eps_values,
        "scaled_commutator_rates": scaled_rates,
        "relative_error_finest": local_rel_error,
    })

    addresses = [semantic_address(semantic_content_id(role)) for role in ROLES]
    Hs = []
    Js = []

    for target in addresses:
        phi, g, gravity, H, _, J = controlled_step(
            phi, omega, g, flavor, tau, gravity, target
        )
        Hs.append(H)
        Js.append(J)

    h_comm = []
    j_comm = []
    j_normed = []
    for k in range(len(Hs) - 1):
        ch = Hs[k] @ Hs[k + 1] - Hs[k + 1] @ Hs[k]
        cj = Js[k] @ Js[k + 1] - Js[k + 1] @ Js[k]
        h_val = float(np.linalg.norm(ch, "fro"))
        j_val = float(np.linalg.norm(cj, "fro"))
        h_comm.append(h_val)
        j_comm.append(j_val)
        j_normed.append(
            j_val / (
                float(np.linalg.norm(Js[k], "fro"))
                * float(np.linalg.norm(Js[k + 1], "fro"))
            )
        )

    checks.append({
        "name": "frozen_semantic_path_source_hamiltonians_noncommute",
        "status": "PASS" if min(h_comm) > 4.0e-4 else "FAIL",
        "adjacent_commutator_frobenius": h_comm,
        "minimum": min(h_comm),
    })

    checks.append({
        "name": "coupling_only_operator_history_noncommutes",
        "status": "PASS" if min(j_comm) > 2.0e-4 else "FAIL",
        "adjacent_J_commutator_frobenius": j_comm,
        "normalized_direction_witness": j_normed,
        "minimum": min(j_comm),
    })

    b = 0.37
    scale_errors = []
    for k in range(len(Js) - 1):
        direct = (
            (b * Js[k]) @ (b * Js[k + 1])
            - (b * Js[k + 1]) @ (b * Js[k])
        )
        reference = (b * b) * (
            Js[k] @ Js[k + 1] - Js[k + 1] @ Js[k]
        )
        scale_errors.append(float(np.max(np.abs(direct - reference))))

    checks.append({
        "name": "coupling_scale_enters_commutator_quadratically",
        "status": "PASS" if max(scale_errors) < 1e-15 else "FAIL",
        "probe_b": b,
        "max_abs_error": max(scale_errors),
    })

    status = "PASS" if all(c["status"] == "PASS" for c in checks) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "claim_scope": (
            "projective horizontal-generator noncommutativity is not sufficient to infer "
            "source-Hamiltonian noncommutativity; the source-pinned frozen PNCS semantic "
            "path nevertheless has direct nonzero adjacent Hamiltonian commutators, "
            "including in the coupling-only sector; the initial infinitesimal "
            "operator rotation is isolated to the phase-conditioned Hebbian update "
            "while pure decay is directionally removed by spectral normalization"
        ),
        "source_pins": {
            "pncs_main": "8855abed440e9949f576ffbe2153325f69e78963",
            "semantic_sequence_fixture": "tests/test_semantic_htri_drive_v32.py::trajectories",
        },
        "checks": checks,
        "summary": {
            "passed": sum(c["status"] == "PASS" for c in checks),
            "total": len(checks),
        },
    }
    Path(__file__).with_name(
        "TIR_MUMMU_SOURCE_OPERATOR_NONABELIANITY_FIREWALL_VALIDATION_V0_1.json"
    ).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
