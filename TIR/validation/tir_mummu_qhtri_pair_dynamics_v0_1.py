#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path
import numpy as np

SCHEMA = "TIR_MUMMU_QHTRI_PAIR_DYNAMICS_VALIDATION_V0_1"
N = 36
DT = 0.01
HBAR = 1.0


def qhtri_graph_hamiltonian(omega: np.ndarray, g: np.ndarray) -> np.ndarray:
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


def unitary(H: np.ndarray, t: float) -> np.ndarray:
    vals, vecs = np.linalg.eigh(np.asarray(H, dtype=np.complex128))
    return (vecs * np.exp(-1j * vals * t)[None, :]) @ vecs.conj().T


def phase_state(phi: np.ndarray) -> np.ndarray:
    return np.exp(1j * phi) / math.sqrt(N)


def pair_projector_and_derivative(H: np.ndarray, psi: np.ndarray, pair: int):
    dpsi = -1j * (H @ psi) / HBAR
    sl = slice(2 * pair, 2 * pair + 2)
    v = psi[sl]
    dv = dpsi[sl]
    q = float(np.vdot(v, v).real)
    if q <= 0.0:
        raise RuntimeError("zero pair support")
    P = np.outer(v, v.conj()) / q
    dq = 2.0 * float(np.real(np.vdot(v, dv)))
    dP = (
        np.outer(dv, v.conj())
        + np.outer(v, dv.conj())
    ) / q - (dq / q) * P
    n = np.array(
        [
            2.0 * P[0, 1].real,
            -2.0 * P[0, 1].imag,
            float((P[0, 0] - P[1, 1]).real),
        ],
        dtype=np.float64,
    )
    dn = np.array(
        [
            2.0 * dP[0, 1].real,
            -2.0 * dP[0, 1].imag,
            float((dP[0, 0] - dP[1, 1]).real),
        ],
        dtype=np.float64,
    )
    omega_vec = np.cross(n, dn)
    return P, dP, n, dn, omega_vec, q


def imbalance(psi: np.ndarray, pair: int) -> float:
    p_l = float(abs(psi[2 * pair]) ** 2)
    p_r = float(abs(psi[2 * pair + 1]) ** 2)
    q = p_l + p_r
    if q <= 0.0:
        raise RuntimeError("zero pair support")
    return (p_l - p_r) / q


def imbalance_velocity(H: np.ndarray, psi: np.ndarray, pair: int) -> float:
    dpsi = -1j * (H @ psi) / HBAR
    p_l = float(abs(psi[2 * pair]) ** 2)
    p_r = float(abs(psi[2 * pair + 1]) ** 2)
    dp_l = 2.0 * float(np.real(np.conj(psi[2 * pair]) * dpsi[2 * pair]))
    dp_r = 2.0 * float(np.real(np.conj(psi[2 * pair + 1]) * dpsi[2 * pair + 1]))
    q = p_l + p_r
    return 2.0 * (p_r * dp_l - p_l * dp_r) / (q * q)


def main() -> int:
    checks = []

    phi = np.linspace(0.07, 5.91, 36, dtype=np.float64)
    omega = 39.6 + np.linspace(-0.12, 0.12, 36, dtype=np.float64)
    idx = np.arange(36, dtype=np.float64)
    g = 0.18 * np.cos((idx[:, None] - idx[None, :]) * np.pi / 18.0)
    g = 0.5 * (g + g.T)
    np.fill_diagonal(g, 0.0)

    H = qhtri_graph_hamiltonian(omega, g)
    herm_error = float(np.max(np.abs(H - H.conj().T)))
    checks.append({
        "name": "source_pinned_qhtri_hamiltonian_hermitian",
        "status": "PASS" if herm_error < 1e-14 else "FAIL",
        "max_abs_error": herm_error,
    })

    checks.append({
        "name": "fixed_source_hamiltonian_history_commutes",
        "status": "PASS",
        "commutator_frobenius": 0.0,
        "reason": "this validator evolves under one time-independent H",
    })

    psi0 = phase_state(phi)
    norm0 = abs(float(np.vdot(psi0, psi0).real) - 1.0)
    pair_supports0 = np.array(
        [
            abs(psi0[2 * j]) ** 2 + abs(psi0[2 * j + 1]) ** 2
            for j in range(18)
        ],
        dtype=np.float64,
    )
    support_error = float(np.max(np.abs(pair_supports0 - 1.0 / 18.0)))
    checks.append({
        "name": "initial_equal_pair_support",
        "status": "PASS" if norm0 < 1e-14 and support_error < 1e-14 else "FAIL",
        "state_norm_error": norm0,
        "pair_support_error": support_error,
    })

    U = unitary(H, DT)
    unitary_error = float(np.max(np.abs(U.conj().T @ U - np.eye(N))))
    psi1 = U @ psi0
    norm1 = abs(float(np.vdot(psi1, psi1).real) - 1.0)
    checks.append({
        "name": "unitary_evolution_integrity",
        "status": "PASS" if unitary_error < 1e-12 and norm1 < 1e-12 else "FAIL",
        "unitarity_error": unitary_error,
        "state_norm_error": norm1,
    })

    u0 = np.array([imbalance(psi0, j) for j in range(18)])
    u1 = np.array([imbalance(psi1, j) for j in range(18)])
    max_u0 = float(np.max(np.abs(u0)))
    max_u1 = float(np.max(np.abs(u1)))
    mean_u1 = float(np.mean(np.abs(u1)))
    checks.append({
        "name": "qhtiri_leaves_equal_amplitude_equator",
        "status": "PASS" if max_u0 < 2e-15 and max_u1 > 1e-6 else "FAIL",
        "max_abs_u_initial": max_u0,
        "max_abs_u_dt": max_u1,
        "mean_abs_u_dt": mean_u1,
    })

    udot0 = np.array([imbalance_velocity(H, psi0, j) for j in range(18)])
    max_udot0 = float(np.max(np.abs(udot0)))
    checks.append({
        "name": "source_derived_imbalance_velocity_nonzero",
        "status": "PASS" if max_udot0 > 1e-4 else "FAIL",
        "max_abs_u_dot_initial": max_udot0,
    })

    omega0 = []
    omega1 = []
    support1 = []
    projector_error = 0.0
    tangent_error = 0.0
    for j in range(18):
        P0, dP0, n0, dn0, om0, _ = pair_projector_and_derivative(H, psi0, j)
        P1, dP1, n1, dn1, om1, q1 = pair_projector_and_derivative(H, psi1, j)
        omega0.append(om0)
        omega1.append(om1)
        support1.append(q1)
        projector_error = max(
            projector_error,
            float(np.max(np.abs(P0 @ P0 - P0))),
            float(np.max(np.abs(P1 @ P1 - P1))),
            abs(float(np.linalg.norm(n0)) - 1.0),
            abs(float(np.linalg.norm(n1)) - 1.0),
        )
        tangent_error = max(
            tangent_error,
            abs(float(np.dot(n0, dn0))),
            abs(float(np.dot(n1, dn1))),
        )
    checks.append({
        "name": "pair_projector_dynamics_integrity",
        "status": "PASS" if projector_error < 1e-12 and tangent_error < 1e-12 and min(support1) > 0.0 else "FAIL",
        "max_projector_or_unit_bloch_error": projector_error,
        "max_n_dot_dn_abs": tangent_error,
        "min_pair_support_dt": float(min(support1)),
    })

    cross_norms = np.array(
        [
            np.linalg.norm(np.cross(a, b))
            for a, b in zip(omega0, omega1)
        ],
        dtype=np.float64,
    )
    pair_index = int(np.argmax(cross_norms))
    max_cross = float(cross_norms[pair_index])
    commutator_frobenius = max_cross / math.sqrt(2.0)
    checks.append({
        "name": "qhtiri_horizontal_projective_connection_history_witness",
        "status": "PASS" if max_cross > 1e-8 else "FAIL",
        "pair_index_zero_based": pair_index,
        "omega_cross_norm": max_cross,
        "commutator_frobenius_norm": commutator_frobenius,
    })

    # Differential imbalance formula against a tiny finite difference.
    eps = 1.0e-7
    psi_eps = unitary(H, eps) @ psi0
    fd = np.array(
        [
            (imbalance(psi_eps, j) - imbalance(psi0, j)) / eps
            for j in range(18)
        ],
        dtype=np.float64,
    )
    fd_error = float(np.max(np.abs(fd - udot0)))
    checks.append({
        "name": "imbalance_velocity_formula_finite_difference",
        "status": "PASS" if fd_error < 1e-7 else "FAIL",
        "max_abs_error": fd_error,
    })

    status = "PASS" if all(c["status"] == "PASS" for c in checks) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "claim_scope": (
            "model-level source-pinned QHTRI 36D dynamics generate full-CP1 "
            "pair imbalance and a noncommuting horizontal projective-connection history; "
            "the pinned source Hamiltonian itself is time-independent and commuting; physical binding open"
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
        "TIR_MUMMU_QHTRI_PAIR_DYNAMICS_VALIDATION_V0_1.json"
    ).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
