#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

SCHEMA = "TIR_MUMMU_QHTRI_COEFFICIENT_IDENTIFIABILITY_VALIDATION_V0_1"
N = 36


def build_fixture():
    phi = np.linspace(0.07, 5.91, N, dtype=np.float64)
    omega = np.linspace(39.48, 39.72, N, dtype=np.float64)
    on = (omega - omega.mean()) / omega.std()
    D = np.diag(on)

    J = np.empty((N, N), dtype=np.float64)
    for m in range(N):
        for n in range(N):
            J[m, n] = 0.0 if m == n else math.cos((m - n) * math.pi / 18.0) / 17.0

    psi0 = np.exp(1j * phi) / math.sqrt(N)
    return D, J, psi0


def pair_witness(H, psi, pair_index=0):
    psi_dot = -1j * (H @ psi)
    psi_ddot = -(H @ H) @ psi

    l = 2 * pair_index
    r = l + 1
    a, b = psi[l], psi[r]
    ad, bd = psi_dot[l], psi_dot[r]
    add, bdd = psi_ddot[l], psi_ddot[r]

    p_l = abs(a) ** 2
    p_r = abs(b) ** 2
    p_l_dot = 2.0 * (a.conjugate() * ad).real
    p_r_dot = 2.0 * (b.conjugate() * bd).real
    p_l_ddot = 2.0 * (abs(ad) ** 2 + (a.conjugate() * add).real)
    p_r_ddot = 2.0 * (abs(bd) ** 2 + (b.conjugate() * bdd).real)

    q = p_l + p_r
    q_dot = p_l_dot + p_r_dot
    q_ddot = p_l_ddot + p_r_ddot

    s = a * b.conjugate()
    s_dot = ad * b.conjugate() + a * bd.conjugate()
    s_ddot = add * b.conjugate() + 2.0 * ad * bd.conjugate() + a * bdd.conjugate()

    nums = (
        (2.0 * s.real, 2.0 * s_dot.real, 2.0 * s_ddot.real),
        (-2.0 * s.imag, -2.0 * s_dot.imag, -2.0 * s_ddot.imag),
        (p_l - p_r, p_l_dot - p_r_dot, p_l_ddot - p_r_ddot),
    )

    n = np.empty(3, dtype=np.float64)
    nd = np.empty(3, dtype=np.float64)
    ndd = np.empty(3, dtype=np.float64)

    for i, (x, xd, xdd) in enumerate(nums):
        n[i] = x / q
        nd[i] = xd / q - x * q_dot / (q * q)
        ndd[i] = (
            xdd / q
            - 2.0 * xd * q_dot / (q * q)
            - x * q_ddot / (q * q)
            + 2.0 * x * q_dot * q_dot / (q * q * q)
        )

    omega_vec = np.cross(n, nd)
    omega_dot = np.cross(n, ndd)
    return float(np.linalg.norm(np.cross(omega_vec, omega_dot)))


def unitary(H, t):
    vals, vecs = np.linalg.eigh(H)
    return (vecs * np.exp(-1j * vals * t)[None, :]) @ vecs.conj().T


def main():
    checks = []
    D, J, psi0 = build_fixture()

    hs_inner = float(np.trace(D.T @ J))
    d_norm = float(np.linalg.norm(D, "fro"))
    j_norm = float(np.linalg.norm(J, "fro"))

    checks.append({
        "name": "detuning_coupling_hilbert_schmidt_orthogonality",
        "status": "PASS" if abs(hs_inner) < 1e-14 else "FAIL",
        "hs_inner": hs_inner,
    })

    checks.append({
        "name": "standardized_36d_detuning_frobenius_norm",
        "status": "PASS" if abs(d_norm - 6.0) < 1e-14 else "FAIL",
        "D_frobenius_norm": d_norm,
        "J_frobenius_norm": j_norm,
    })

    Dhat = D / d_norm
    Jhat = J / j_norm
    orthonormal_error = max(
        abs(float(np.trace(Dhat.T @ Dhat)) - 1.0),
        abs(float(np.trace(Jhat.T @ Jhat)) - 1.0),
        abs(float(np.trace(Dhat.T @ Jhat))),
    )
    checks.append({
        "name": "normalized_hs_basis_is_orthonormal",
        "status": "PASS" if orthonormal_error < 1e-14 else "FAIL",
        "max_abs_error": orthonormal_error,
    })

    angles = np.linspace(0.0, math.pi / 2.0, 33)
    quad = []
    for chi in angles:
        H = math.cos(chi) * Dhat + math.sin(chi) * Jhat
        quad.append(float(np.trace(H.T @ H)))
    quad_spread = max(quad) - min(quad)
    checks.append({
        "name": "quadratic_hs_action_cannot_select_mixing_angle",
        "status": "PASS" if quad_spread < 1e-14 else "FAIL",
        "min_trace_H2": min(quad),
        "max_trace_H2": max(quad),
        "spread": quad_spread,
    })

    chi = 0.713
    scale = 1.83
    K = math.cos(chi) * Dhat + math.sin(chi) * Jhat
    t = 0.271
    scale_time_error = float(np.max(np.abs(unitary(scale * K, t) - unitary(K, scale * t))))
    checks.append({
        "name": "overall_scale_is_unitary_time_reparameterization",
        "status": "PASS" if scale_time_error < 1e-13 else "FAIL",
        "max_abs_error": scale_time_error,
    })

    a = 0.25
    b = 0.7
    A = a * d_norm
    B = b * j_norm
    s = math.hypot(A, B)
    chi_default = math.atan2(B, A)
    checks.append({
        "name": "source_defaults_reduce_to_hs_scale_and_angle",
        "status": "PASS" if abs(chi_default - 0.5965608027914262) < 1e-12 else "FAIL",
        "A": A,
        "B": B,
        "scale_s": s,
        "chi_rad": chi_default,
        "chi_deg": math.degrees(chi_default),
        "raw_ratio_b_over_a": b / a,
    })

    scan_angles = np.linspace(0.0, math.pi / 2.0, 2001)
    witnesses = np.asarray([
        pair_witness(math.cos(x) * Dhat + math.sin(x) * Jhat, psi0)
        for x in scan_angles
    ])
    imax = int(np.argmax(witnesses))
    chi_max = float(scan_angles[imax])
    w_max = float(witnesses[imax])
    w_default = pair_witness(
        math.cos(chi_default) * Dhat + math.sin(chi_default) * Jhat,
        psi0,
    )
    default_fraction = w_default / w_max

    checks.append({
        "name": "default_angle_not_extremum_of_fixture_witness",
        "status": "PASS" if abs(chi_default - chi_max) > math.radians(5.0) else "FAIL",
        "chi_default_deg": math.degrees(chi_default),
        "chi_witness_max_deg": math.degrees(chi_max),
        "w_default": w_default,
        "w_max": w_max,
        "default_fraction_of_max": default_fraction,
    })

    chi_eq = math.pi / 4.0
    raw_ratio_eq = d_norm / j_norm
    h_eq = (Dhat + Jhat) / math.sqrt(2.0)
    h_eq_norm = float(np.linalg.norm(h_eq, "fro"))
    checks.append({
        "name": "equal_hs_neutral_benchmark",
        "status": "PASS" if abs(h_eq_norm - 1.0) < 1e-14 else "FAIL",
        "chi_deg": math.degrees(chi_eq),
        "raw_ratio_b_over_a": raw_ratio_eq,
        "frobenius_norm": h_eq_norm,
        "promotion_state": "BENCHMARK_CONVENTION_ONLY",
    })

    status = "PASS" if all(c["status"] == "PASS" for c in checks) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "claim_scope": (
            "QHTRI two-coefficient sector reduces to an overall time scale and one "
            "dimensionless Hilbert-Schmidt mixing angle; quadratic norm/action cannot "
            "select that angle; PNCS defaults remain reference parameters"
        ),
        "source_pins": {
            "pncs_main": "8855abed440e9949f576ffbe2153325f69e78963",
            "origin_commit": "bfe21eaa3e5c0d5e33dc2e449c88c6bd0e10cf52",
        },
        "checks": checks,
        "summary": {
            "passed": sum(c["status"] == "PASS" for c in checks),
            "total": len(checks),
        },
    }
    Path(__file__).with_name(
        "TIR_MUMMU_QHTRI_COEFFICIENT_IDENTIFIABILITY_VALIDATION_V0_1.json"
    ).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
