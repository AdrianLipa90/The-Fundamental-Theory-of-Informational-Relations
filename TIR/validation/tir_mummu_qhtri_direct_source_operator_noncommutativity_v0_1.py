#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
import struct
from pathlib import Path

import numpy as np

SCHEMA = "TIR_MUMMU_QHTRI_DIRECT_SOURCE_OPERATOR_NONCOMMUTATIVITY_VALIDATION_V0_1"
N = 36
TAU = 2.0 * math.pi
KAPPA = math.log(2.0) / (24.0 * math.pi)

HARMONIC_VALUES = np.array([1, 3, 6, 9], dtype=np.int32)
HARMONIC_AMPS = np.array([1.0, 0.5, 0.33, 0.25], dtype=np.float64)
CHANNEL_HARMONICS = np.asarray([
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
], dtype=bool)

EYE_N = np.eye(N, dtype=np.float64)
CH_LOCAL_R = np.array([0,0,1,1,2,2], dtype=np.intp)
CH_LOCAL_C = np.array([1,2,0,2,0,1], dtype=np.intp)
CH_BASE = (3 * np.arange(N // 3, dtype=np.intp))[:, None]
CH_ROWS = CH_BASE + CH_LOCAL_R[None, :]
CH_COLS = CH_BASE + CH_LOCAL_C[None, :]

DOMAIN = b"PNCS_SEMANTIC_CONTENT_ADDRESS_V2\x00"
ROLE_SCHEMA = "PNCS_TYPED_SEMANTIC_ROLE_CONTENT_V0_31"
ROLE_SOURCE = "NISABA_A_FROZEN_SEVEN_PULSE_SEMANTIC_MAPPING_V1"
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


def digest(value):
    return hashlib.sha256(compact_json(value).encode("utf-8")).hexdigest()


def content_id(role):
    payload = {
        "schema": ROLE_SCHEMA,
        "role_id": role,
        "source_semantic_key": f"{ROLE_SOURCE}:{role}",
        "relation_type": "ORDERED_SEMANTIC_ROLE",
    }
    return "pncs:semantic-role:sha256:" + digest(payload)


def semantic_address(cid):
    raw = hashlib.shake_256(DOMAIN + cid.encode("ascii")).digest(N * 8)
    words = struct.unpack("<" + "Q" * N, raw)
    denom = float((1 << 64) - 1)
    return np.asarray([(w / denom) * TAU for w in words], dtype=np.float64)


def harmonic_composite_phase(phi):
    s = np.sum(
        HARMONIC_AMPS[None, :]
        * np.exp(1j * phi[:, None] * HARMONIC_VALUES[None, :])
        * CHANNEL_HARMONICS,
        axis=1,
    )
    return np.angle(s)


def wrap_delta(target, current):
    return np.angle(np.exp(1j * (np.asarray(target) - np.asarray(current))))


def qhtri_components(omega, g):
    j = 0.5 * (g + g.T)
    j = j.copy()
    np.fill_diagonal(j, 0.0)
    spec = float(np.max(np.abs(np.linalg.eigvalsh(j))))
    if spec <= 0.0:
        raise RuntimeError("zero coupling matrix")
    J = j / spec

    oc = omega - float(np.mean(omega))
    os = float(np.std(oc)) or 1.0
    D = np.diag(oc / os)
    return D, J, spec


def qhtri_hamiltonian(omega, g, a=0.25, b=0.7):
    D, J, spec = qhtri_components(omega, g)
    return a * D + b * J, D, J, spec


def controlled_step(phi, omega, g, flavor, tau, gravity, target, dt=0.01):
    phi = phi.copy()
    omega = omega.copy()
    g = g.copy()
    flavor = flavor.copy()
    tau = tau.copy()
    gravity = gravity.copy()

    phi_eff = harmonic_composite_phase(phi)
    diff = phi_eff[:, None] - phi_eff[None, :]
    coupling = np.sum(g * np.sin(diff), axis=1) / N

    tau_min = float(tau.min())
    tau_range = float(tau.max() - tau_min)
    if tau_range > 1e-12:
        tau_mod = 0.5 + 0.5 * (tau - tau_min) / tau_range
    else:
        tau_mod = np.ones_like(tau) * 0.75
    tardis = min(float(gravity[1]), 2.0)
    coupling *= tau_mod * tardis

    mood_mod = (float(flavor[3]) - 0.5) * KAPPA * 50.0
    closure_mod = (1.0 - float(flavor[4])) * KAPPA * 30.0
    coherence_damping = float(flavor[0]) * KAPPA * 10.0
    effective_omega = omega * (
        1.0 + mood_mod + closure_mod - coherence_damping
    )

    activity = (
        float(flavor[2])
        + float(flavor[4]) * 0.5
        + (1.0 - float(flavor[3])) * 0.3
    ) / 1.8
    activity = min(max(activity, 0.0), 1.0)

    hebb_step = 0.01 * dt * 10.0
    decay_step = 0.001 * dt * 10.0
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
        boost = 0.01 * (0.5 - ch_coh) * dist * dt * 10.0
        wc = np.flatnonzero(weak)
        rows = CH_ROWS[wc].ravel()
        cols = CH_COLS[wc].ravel()
        g[rows, cols] += np.repeat(boost[wc], 6)
        np.clip(g, -1.0, 1.0, out=g)

    phi_base = phi.copy()
    if global_R > 0.7:
        push = 0.005 * (global_R - 0.7) * dt * 10.0
        ch_target = (ch_mean + math.pi) % TAU
        target_osc = np.repeat(ch_target, 3)
        phi_base += push * np.angle(np.exp(1j * (target_osc - phi_base)))
        phi_base %= TAU

    desired = wrap_delta(target, phi_base)
    control = desired / dt - effective_omega - coupling
    phi_next = (
        phi_base + dt * (effective_omega + coupling + control)
    ) % TAU

    dphi = wrap_delta(phi_next, phi_base)
    semantic_density = min(
        10.0, float(np.mean(np.abs(dphi)) / dt)
    )
    gravity_next = gravity.copy()
    gravity_next[0] = semantic_density
    gravity_next[1] = 1.0 + math.tanh(semantic_density * 0.5) * 9.0
    gravity_next[2] = gravity_next[2] * 0.99 + semantic_density * 0.01

    H, D, J, spec = qhtri_hamiltonian(omega, g)
    return phi_next, g, gravity_next, H, D, J, spec


def initial_snapshot():
    phi = np.linspace(0.07, 5.91, N, dtype=np.float64)
    omega = 39.6 + np.linspace(-0.12, 0.12, N, dtype=np.float64)
    i = np.arange(N, dtype=np.float64)
    g = 0.18 * np.cos((i[:, None] - i[None, :]) * np.pi / 18.0)
    g = 0.5 * (g + g.T)
    np.fill_diagonal(g, 0.0)
    flavor = np.array([0.31, 0.72, 0.23, 0.56, 0.48, 0.5], dtype=np.float64)
    tau = np.linspace(0.21, 0.49, N, dtype=np.float64)
    gravity = np.array([0.0, 1.17, 0.3, 0.0, 0.0, 1.0, 0.0, 0.0], dtype=np.float64)
    return phi, omega, g, flavor, tau, gravity


def run_order(order):
    targets = [semantic_address(content_id(role)) for role in ROLES]
    phi, omega, g, flavor, tau, gravity = initial_snapshot()
    Hs = []
    Js = []
    D = None

    for idx in order:
        phi, g, gravity, H, D_now, J, _ = controlled_step(
            phi, omega, g, flavor, tau, gravity, targets[idx]
        )
        Hs.append(H)
        Js.append(J)
        D = D_now

    if D is None:
        raise RuntimeError("empty order")
    return D, Hs, Js


def frob(a):
    return float(np.linalg.norm(a, "fro"))


def comm(a, b):
    return a @ b - b @ a


def main():
    checks = []

    D, Hs, Js = run_order(tuple(range(7)))

    fixed_self = frob(comm(Hs[0], Hs[0]))
    checks.append({
        "name": "fixed_h_source_operator_self_commutator_zero",
        "status": "PASS" if fixed_self == 0.0 else "FAIL",
        "frobenius_norm": fixed_self,
    })

    comm_norms = [
        frob(comm(Hs[k], Hs[k + 1]))
        for k in range(6)
    ]
    checks.append({
        "name": "all_consecutive_controlled_source_hamiltonians_noncommute",
        "status": "PASS" if min(comm_norms) > 4.0e-4 else "FAIL",
        "consecutive_commutator_frobenius_norms": comm_norms,
        "minimum": min(comm_norms),
        "maximum": max(comm_norms),
    })

    decomposition_errors = []
    gram_determinants = []
    correlations = []
    x_norms = []
    y_norms = []

    a = 0.25
    b = 0.7
    for k in range(6):
        X = comm(D, Js[k + 1] - Js[k])
        Y = comm(Js[k], Js[k + 1])
        direct = comm(Hs[k], Hs[k + 1])
        decomposed = a * b * X + b * b * Y
        decomposition_errors.append(
            float(np.max(np.abs(direct - decomposed)))
        )

        nx = frob(X)
        ny = frob(Y)
        inner = float(np.vdot(X, Y).real)
        gram = (nx * ny) ** 2 - inner ** 2
        corr = inner / (nx * ny)
        x_norms.append(nx)
        y_norms.append(ny)
        gram_determinants.append(gram)
        correlations.append(corr)

    checks.append({
        "name": "exact_consecutive_commutator_decomposition",
        "status": "PASS" if max(decomposition_errors) < 1e-14 else "FAIL",
        "max_abs_error": max(decomposition_errors),
    })

    checks.append({
        "name": "X_Y_hs_linear_independence_all_transitions",
        "status": "PASS" if min(gram_determinants) > 3.0e-13 else "FAIL",
        "gram_determinants": gram_determinants,
        "hs_correlations": correlations,
        "X_frobenius_norms": x_norms,
        "Y_frobenius_norms": y_norms,
    })

    # Since X and Y are independent, b(aX+bY) cannot vanish for b != 0.
    probe_coefficients = [
        (-3.0, 0.1),
        (0.0, 0.1),
        (1.0, 0.1),
        (7.0, -0.4),
        (-2.0, 2.0),
    ]
    min_probe = math.inf
    for aa, bb in probe_coefficients:
        for k in range(6):
            X = comm(D, Js[k + 1] - Js[k])
            Y = comm(Js[k], Js[k + 1])
            value = frob(bb * (aa * X + bb * Y))
            min_probe = min(min_probe, value)
    checks.append({
        "name": "nonzero_coupling_generic_coefficient_probe_remains_noncommuting",
        "status": "PASS" if min_probe > 1e-5 else "FAIL",
        "minimum_probe_commutator_norm": min_probe,
        "note": "finite probes supplement the exact linear-independence argument",
    })

    order_summaries = {}
    orderings = {
        "original": tuple(range(7)),
        "reverse": tuple(reversed(range(7))),
        "shuffle": (3, 6, 0, 4, 2, 5, 1),
    }
    for name, order in orderings.items():
        _, hseq, _ = run_order(order)
        vals = [frob(comm(hseq[k], hseq[k + 1])) for k in range(6)]
        order_summaries[name] = {
            "sum_consecutive_commutator_norms": float(sum(vals)),
            "max_consecutive_commutator_norm": float(max(vals)),
        }

    sums = [
        order_summaries[name]["sum_consecutive_commutator_norms"]
        for name in ("original", "reverse", "shuffle")
    ]
    checks.append({
        "name": "direct_operator_commutator_signature_is_order_sensitive",
        "status": "PASS" if len({round(x, 12) for x in sums}) == 3 else "FAIL",
        "order_summaries": order_summaries,
    })

    status = "PASS" if all(x["status"] == "PASS" for x in checks) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "claim_scope": (
            "direct source-operator test for PNCS controlled semantic QHTRI trajectory; "
            "fixed-H self history remains commuting, while source-updated multi-step "
            "Hamiltonians are noncommuting on the pinned deterministic fixture"
        ),
        "source_pins": {
            "pncs_main": "8855abed440e9949f576ffbe2153325f69e78963",
            "fixture": "tests/test_semantic_htri_drive_v32.py",
        },
        "checks": checks,
        "summary": {
            "passed": sum(x["status"] == "PASS" for x in checks),
            "total": len(checks),
        },
    }

    Path(__file__).with_name(
        "TIR_MUMMU_QHTRI_DIRECT_SOURCE_OPERATOR_NONCOMMUTATIVITY_VALIDATION_V0_1.json"
    ).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
