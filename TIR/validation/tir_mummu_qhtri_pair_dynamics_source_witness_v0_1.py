#!/usr/bin/env python3
from __future__ import annotations

import cmath
import json
import math
from pathlib import Path

SCHEMA = "TIR_MUMMU_QHTRI_PAIR_DYNAMICS_SOURCE_WITNESS_VALIDATION_V0_1"
N = 36


def dotc(a, b):
    return sum(x.conjugate() * y for x, y in zip(a, b))


def norm2(v):
    return sum(abs(x) ** 2 for x in v)


def matvec(h, v):
    return [
        sum(h[i][j] * v[j] for j in range(N))
        for i in range(N)
    ]


def vadd(a, b, scale=1.0):
    return [x + scale * y for x, y in zip(a, b)]


def rhs(h, psi):
    return [-1j * z for z in matvec(h, psi)]


def rk4_step(h, psi, dt):
    k1 = rhs(h, psi)
    k2 = rhs(h, vadd(psi, k1, 0.5 * dt))
    k3 = rhs(h, vadd(psi, k2, 0.5 * dt))
    k4 = rhs(h, vadd(psi, k3, dt))
    return [
        psi[i] + (dt / 6.0) * (k1[i] + 2.0 * k2[i] + 2.0 * k3[i] + k4[i])
        for i in range(N)
    ]


def evolve_rk4(h, psi0, total, steps):
    dt = total / steps
    psi = list(psi0)
    for _ in range(steps):
        psi = rk4_step(h, psi, dt)
    return psi


def build_fixture():
    phi = [0.07 + (5.91 - 0.07) * k / 35.0 for k in range(N)]
    omega = [39.6 - 0.12 + 0.24 * k / 35.0 for k in range(N)]

    mean = sum(omega) / N
    std = math.sqrt(sum((w - mean) ** 2 for w in omega) / N)
    on = [(w - mean) / std for w in omega]

    # Deterministic PNCS fixture:
    # g_mn = 0.18*cos((m-n)pi/18), m!=n, g_mm=0.
    # The full cosine Gram matrix has nonzero eigenvalue 3.24 and removing
    # 0.18 I gives spectral radius 3.06, hence g/spec = cos(...)/17 off-diagonal.
    h = []
    for m in range(N):
        row = []
        for n in range(N):
            value = 0.0
            if m == n:
                value += 0.25 * on[m]
            else:
                value += (0.7 / 17.0) * math.cos((m - n) * math.pi / 18.0)
            row.append(complex(value, 0.0))
        h.append(row)

    psi0 = [cmath.exp(1j * x) / math.sqrt(N) for x in phi]
    return phi, omega, h, psi0


def pair_kinematics(h, psi, pair_index):
    psi_dot = rhs(h, psi)
    hpsi = matvec(h, psi)
    h2psi = matvec(h, hpsi)
    psi_ddot = [-z for z in h2psi]

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
    if q <= 0.0:
        raise ValueError("pair support must be positive")
    q_dot = p_l_dot + p_r_dot
    q_ddot = p_l_ddot + p_r_ddot

    s = a * b.conjugate()
    s_dot = ad * b.conjugate() + a * bd.conjugate()
    s_ddot = add * b.conjugate() + 2.0 * ad * bd.conjugate() + a * bdd.conjugate()

    numerators = [
        (2.0 * s.real, 2.0 * s_dot.real, 2.0 * s_ddot.real),
        (-2.0 * s.imag, -2.0 * s_dot.imag, -2.0 * s_ddot.imag),
        (p_l - p_r, p_l_dot - p_r_dot, p_l_ddot - p_r_ddot),
    ]

    n = []
    n_dot = []
    n_ddot = []
    for x, xd, xdd in numerators:
        n.append(x / q)
        n_dot.append(xd / q - x * q_dot / (q * q))
        n_ddot.append(
            xdd / q
            - 2.0 * xd * q_dot / (q * q)
            - x * q_ddot / (q * q)
            + 2.0 * x * q_dot * q_dot / (q * q * q)
        )

    u_dot_direct = (
        2.0 * (p_r * p_l_dot - p_l * p_r_dot)
        / (q * q)
    )

    return {
        "q": q,
        "n": tuple(n),
        "n_dot": tuple(n_dot),
        "n_ddot": tuple(n_ddot),
        "u": n[2],
        "u_dot": n_dot[2],
        "u_dot_direct": u_dot_direct,
    }


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def vnorm(v):
    return math.sqrt(sum(x * x for x in v))


def main():
    checks = []
    phi, omega, h, psi0 = build_fixture()

    herm_error = max(
        abs(h[i][j] - h[j][i].conjugate())
        for i in range(N)
        for j in range(N)
    )
    checks.append({
        "name": "source_fixture_qhtri_hamiltonian_hermitian",
        "status": "PASS" if herm_error < 1e-15 else "FAIL",
        "max_abs_error": herm_error,
    })

    norm_error = abs(norm2(psi0) - 1.0)
    checks.append({
        "name": "source_phase_state_normalized",
        "status": "PASS" if norm_error < 1e-14 else "FAIL",
        "norm_error": norm_error,
    })

    k0 = pair_kinematics(h, psi0, 0)
    u_dot_error = abs(k0["u_dot"] - k0["u_dot_direct"])
    checks.append({
        "name": "pair_imbalance_derivative_from_36d_schrodinger",
        "status": "PASS" if u_dot_error < 1e-14 else "FAIL",
        "u": k0["u"],
        "u_dot": k0["u_dot"],
        "formula_abs_error": u_dot_error,
    })

    n = k0["n"]
    nd = k0["n_dot"]
    ndd = k0["n_ddot"]
    omega0 = cross(n, nd)
    omega_dot0 = cross(n, ndd)
    witness_vec = cross(omega0, omega_dot0)
    witness = vnorm(witness_vec)

    checks.append({
        "name": "source_derived_local_nonabelian_acceleration_witness",
        "status": "PASS" if witness > 8e-4 else "FAIL",
        "omega": list(omega0),
        "omega_dot": list(omega_dot0),
        "omega_cross_omega_dot": list(witness_vec),
        "witness_norm": witness,
    })

    # Short-time convergence:
    # ||Omega(0) x Omega(eps)|| / eps -> ||Omega x Omega_dot||.
    eps_values = [0.01, 0.005, 0.0025]
    ratios = []
    for eps in eps_values:
        psi_eps = evolve_rk4(h, psi0, eps, 40)
        ke = pair_kinematics(h, psi_eps, 0)
        omega_eps = cross(ke["n"], ke["n_dot"])
        ratios.append(vnorm(cross(omega0, omega_eps)) / eps)

    short_rel_error = abs(ratios[-1] - witness) / witness
    checks.append({
        "name": "short_time_commutator_converges_to_local_witness",
        "status": "PASS" if short_rel_error < 0.01 else "FAIL",
        "eps_values": eps_values,
        "scaled_cross_norms": ratios,
        "relative_error_finest": short_rel_error,
    })

    psi_half = evolve_rk4(h, psi0, 0.5, 1000)
    k_half = pair_kinematics(h, psi_half, 0)
    omega_half = cross(k_half["n"], k_half["n_dot"])
    finite_cross = vnorm(cross(omega0, omega_half))
    norm_half_error = abs(norm2(psi_half) - 1.0)

    checks.append({
        "name": "finite_time_pair_imbalance_emerges",
        "status": "PASS" if abs(k_half["u"]) > 0.009 and norm_half_error < 1e-10 else "FAIL",
        "u_t0": k0["u"],
        "u_t05": k_half["u"],
        "state_norm_error_t05": norm_half_error,
    })

    checks.append({
        "name": "finite_time_generator_direction_changes",
        "status": "PASS" if finite_cross > 4e-4 else "FAIL",
        "omega_t0": list(omega0),
        "omega_t05": list(omega_half),
        "cross_norm": finite_cross,
    })

    status = "PASS" if all(c["status"] == "PASS" for c in checks) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "claim_scope": (
            "model-level source-derived QHTRI 36D wave evolution produces a "
            "non-Abelian local CP1 pair-history witness; physical binding and "
            "fundamental status of QHTRI coefficients remain open"
        ),
        "source_pins": {
            "pncs_main": "8855abed440e9949f576ffbe2153325f69e78963"
        },
        "checks": checks,
        "summary": {
            "passed": sum(c["status"] == "PASS" for c in checks),
            "total": len(checks),
        },
    }

    Path(__file__).with_name(
        "TIR_MUMMU_QHTRI_PAIR_DYNAMICS_SOURCE_WITNESS_VALIDATION_V0_1.json"
    ).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
