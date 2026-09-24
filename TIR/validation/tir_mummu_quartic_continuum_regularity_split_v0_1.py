#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path
import numpy as np

SCHEMA = "TIR_MUMMU_QUARTIC_CONTINUUM_REGULARITY_SPLIT_VALIDATION_V0_1"
N = 36
HBAR = 1.0


def sigma(v):
    x, y, z = v
    return np.array([[z, x - 1j*y], [x + 1j*y, -z]], dtype=np.complex128)


def su2_exp_vector(v):
    v = np.asarray(v, dtype=np.float64)
    a = float(np.linalg.norm(v))
    if a < 1e-18:
        return np.eye(2, dtype=np.complex128)
    return math.cos(a/2.0) * np.eye(2) - 1j * math.sin(a/2.0) * sigma(v/a)


def normalized_character(U):
    return float((0.5 * np.trace(U)).real)


def qhtri_graph_hamiltonian(omega, g):
    j = 0.5 * (g + g.T)
    j = j.copy()
    np.fill_diagonal(j, 0.0)
    spec = float(np.max(np.abs(np.linalg.eigvalsh(j))))
    if spec <= 0.0:
        raise RuntimeError("zero coupling matrix")
    jn = j / spec
    oc = omega - float(np.mean(omega))
    os = float(np.std(oc)) or 1.0
    on = oc / os
    return 0.25 * np.diag(on) + 0.7 * jn


def fixture():
    phi = np.linspace(0.07, 5.91, 36, dtype=np.float64)
    omega = 39.6 + np.linspace(-0.12, 0.12, 36, dtype=np.float64)
    idx = np.arange(36, dtype=np.float64)
    g = 0.18 * np.cos((idx[:, None] - idx[None, :]) * np.pi / 18.0)
    g = 0.5 * (g + g.T)
    np.fill_diagonal(g, 0.0)
    H = qhtri_graph_hamiltonian(omega, g)
    psi0 = np.exp(1j * phi) / math.sqrt(N)
    vals, vecs = np.linalg.eigh(H.astype(np.complex128))
    coeff = vecs.conj().T @ psi0
    return H, psi0, vals, vecs, coeff


def pair_omega(psi, H, pair):
    dpsi = -1j * (H @ psi) / HBAR
    sl = slice(2*pair, 2*pair+2)
    v = psi[sl]
    dv = dpsi[sl]
    q = float(np.vdot(v, v).real)
    if q <= 0.0:
        raise RuntimeError("zero pair support")
    P = np.outer(v, v.conj()) / q
    dq = 2.0 * float(np.real(np.vdot(v, dv)))
    dP = (
        np.outer(dv, v.conj()) + np.outer(v, dv.conj())
    ) / q - (dq / q) * P
    n = np.array(
        [2.0*P[0,1].real, -2.0*P[0,1].imag, float((P[0,0]-P[1,1]).real)],
        dtype=np.float64,
    )
    dn = np.array(
        [2.0*dP[0,1].real, -2.0*dP[0,1].imag, float((dP[0,0]-dP[1,1]).real)],
        dtype=np.float64,
    )
    return np.cross(n, dn)


def smooth_character_difference(H, vals, vecs, coeff, T, *, pair=9, steps=4096):
    dt = T / steps
    U = np.eye(2, dtype=np.complex128)
    integrated = np.zeros(3, dtype=np.float64)
    for k in range(steps):
        t = (k + 0.5) * dt
        psi = vecs @ (np.exp(-1j * vals * t) * coeff)
        om = pair_omega(psi, H, pair)
        integrated += om * dt
        U = su2_exp_vector(om * dt) @ U
    U_int = su2_exp_vector(integrated)
    return normalized_character(U) - normalized_character(U_int)


def main():
    checks = []

    # General two-layer quartic theorem numerical probe.
    a = np.array([0.7, -0.2, 0.4], dtype=np.float64)
    b = np.array([-0.3, 0.8, 0.5], dtype=np.float64)
    exact_c4 = float(np.linalg.norm(np.cross(a, b)) ** 2 / 96.0)
    estimates = []
    for eps in (0.08, 0.06, 0.04):
        K_seq = normalized_character(su2_exp_vector(eps*a) @ su2_exp_vector(eps*b))
        K_const = normalized_character(su2_exp_vector(eps*(a+b)))
        estimates.append((K_seq - K_const) / eps**4)
    best = estimates[-1]
    relative_error = abs(best - exact_c4) / exact_c4
    checks.append({
        "name": "general_two_layer_quartic_cross_product_coefficient",
        "status": "PASS" if relative_error < 5e-4 else "FAIL",
        "exact_cross_product_coefficient": exact_c4,
        "epsilon_coefficient_estimates": estimates,
        "relative_error_smallest_epsilon": relative_error,
    })

    # Orthogonal special case recovers alpha^2 beta^2 / 96.
    alpha = 0.73
    beta = 0.41
    special = np.linalg.norm(np.cross([alpha,0,0], [0,beta,0]))**2 / 96.0
    expected = alpha**2 * beta**2 / 96.0
    checks.append({
        "name": "orthogonal_alpha_beta_special_case",
        "status": "PASS" if abs(special-expected) < 1e-15 else "FAIL",
        "residual": abs(special-expected),
    })

    # Commutator/Frobenius equivalent coefficient.
    A = -0.5j * sigma(a)
    B = -0.5j * sigma(b)
    comm = A @ B - B @ A
    fro2 = float(np.sum(np.abs(comm)**2))
    comm_coeff = fro2 / 48.0
    checks.append({
        "name": "quartic_coefficient_commutator_form",
        "status": "PASS" if abs(comm_coeff-exact_c4) < 1e-14 else "FAIL",
        "cross_product_form": exact_c4,
        "commutator_form": comm_coeff,
        "residual": abs(comm_coeff-exact_c4),
    })

    # Source-pinned smooth QHTRI path.
    H, psi0, vals, vecs, coeff = fixture()
    herm = float(np.max(np.abs(H-H.conj().T)))
    checks.append({
        "name": "source_pinned_qhtri_fixture_hermitian",
        "status": "PASS" if herm < 1e-14 else "FAIL",
        "max_abs_error": herm,
    })

    windows = (0.2, 0.4, 0.8)
    deltas = [
        smooth_character_difference(H, vals, vecs, coeff, T, pair=9, steps=4096)
        for T in windows
    ]
    ratio_04_02 = deltas[1] / deltas[0]
    ratio_08_04 = deltas[2] / deltas[1]
    slope_08_04 = math.log(abs(ratio_08_04), 2.0)
    checks.append({
        "name": "smooth_qhtri_character_memory_is_sixth_order_consistent",
        "status": (
            "PASS"
            if deltas[1] > 0.0
            and deltas[2] > 0.0
            and 55.0 < ratio_08_04 < 72.0
            and 5.75 < slope_08_04 < 6.2
            else "FAIL"
        ),
        "windows": list(windows),
        "character_differences": deltas,
        "ratio_0p4_over_0p2": ratio_04_02,
        "ratio_0p8_over_0p4": ratio_08_04,
        "log2_ratio_0p8_over_0p4": slope_08_04,
        "expected_doubling_ratio_for_order_6": 64.0,
    })

    # Explicitly reject a quartic smooth-time interpretation for the robust window.
    quartic_ratio = 16.0
    distance_to_quartic = abs(ratio_08_04 - quartic_ratio)
    distance_to_sixth = abs(ratio_08_04 - 64.0)
    checks.append({
        "name": "smooth_qhtri_not_quartic_under_time_window_scaling",
        "status": "PASS" if distance_to_sixth < distance_to_quartic else "FAIL",
        "observed_ratio": ratio_08_04,
        "quartic_expected_ratio": quartic_ratio,
        "sixth_order_expected_ratio": 64.0,
    })

    status = "PASS" if all(c["status"] == "PASS" for c in checks) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "claim_scope": (
            "finite two-layer amplitude scaling has exact quartic cross-product coefficient; "
            "source-pinned smooth QHTRI short-time path is consistent with sixth-order "
            "scalar-character memory, not quartic time-window scaling"
        ),
        "source_pins": {
            "pncs_main": "8855abed440e9949f576ffbe2153325f69e78963",
            "fixture": "tests/test_semantic_htri_drive_v32.py::snapshot",
        },
        "checks": checks,
        "summary": {
            "passed": sum(c["status"] == "PASS" for c in checks),
            "total": len(checks),
        },
    }
    Path(__file__).with_name(
        "TIR_MUMMU_QUARTIC_CONTINUUM_REGULARITY_SPLIT_VALIDATION_V0_1.json"
    ).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
