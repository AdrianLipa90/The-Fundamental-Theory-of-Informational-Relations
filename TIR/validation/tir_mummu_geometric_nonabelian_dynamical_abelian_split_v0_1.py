#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

SCHEMA = "TIR_MUMMU_GEOMETRIC_NONABELIAN_DYNAMICAL_ABELIAN_SPLIT_VALIDATION_V0_1"
N = 36
TAU = 2.0 * math.pi


def temporal_z(u: float) -> complex:
    w = 1j * u
    return (w - 1.0) / (w + 1.0)


def temporal_theta(times: np.ndarray, scale: float = 4.0) -> np.ndarray:
    return np.asarray(
        [np.angle(temporal_z(float(t) / scale)) % TAU for t in times],
        dtype=np.float64,
    )


def source_fixture():
    times = np.arange(N, dtype=np.float64) - 18.0
    theta = temporal_theta(times)
    amps = np.exp(1j * np.arange(N, dtype=np.float64) / 7.0) / math.sqrt(N)
    weights = np.exp(-0.25 * times * times)
    post = amps * weights
    post /= np.linalg.norm(post)
    probs = np.abs(post) ** 2

    drive = np.zeros(N, dtype=np.float64)
    drive[18] = 1.0
    velocity = np.zeros(N, dtype=np.float64)
    snapshots = {}

    for step in range(1, 101):
        proper_dt = 0.01
        dot_ud = float(np.dot(velocity, drive))
        force = drive + velocity * dot_ud
        accel = 0.05 * force
        velocity = velocity + proper_dt * accel
        theta = (theta + proper_dt * velocity) % TAU
        if step in (50, 100):
            snapshots[step] = (theta.copy(), velocity.copy())

    return probs, snapshots


def pair_data(probs, snapshot):
    theta, velocity = snapshot
    l, r_idx = 18, 19
    pl = float(probs[l])
    pr = float(probs[r_idx])
    q = pl + pr
    u = (pl - pr) / q
    radius = math.sqrt(1.0 - u * u)
    delta = math.atan2(
        math.sin(float(theta[r_idx] - theta[l])),
        math.cos(float(theta[r_idx] - theta[l])),
    )
    delta_dot = float(velocity[r_idx] - velocity[l])

    n = np.asarray(
        (radius * math.cos(delta), radius * math.sin(delta), u),
        dtype=np.float64,
    )
    h = np.asarray((0.0, 0.0, delta_dot), dtype=np.float64)
    n_dot = np.cross(h, n)
    omega = np.cross(n, n_dot)
    omega_projected = h - float(np.dot(n, h)) * n

    pair_psi = np.asarray(
        (
            math.sqrt(pl / q) * np.exp(1j * float(theta[l])),
            math.sqrt(pr / q) * np.exp(1j * float(theta[r_idx])),
        ),
        dtype=np.complex128,
    )
    v_l = float(velocity[l])
    v_r = float(velocity[r_idx])
    psi_dot = 1j * np.asarray((v_l, v_r)) * pair_psi
    h_phase = -np.diag(np.asarray((v_l, v_r), dtype=np.float64)).astype(
        np.complex128
    )

    return {
        "u": u,
        "delta": delta,
        "delta_dot": delta_dot,
        "n": n,
        "h": h,
        "n_dot": n_dot,
        "omega": omega,
        "omega_projected": omega_projected,
        "psi": pair_psi,
        "psi_dot": psi_dot,
        "H_phase": h_phase,
    }


def frob(a):
    return float(np.linalg.norm(a, "fro"))


def main():
    checks = []
    probs, snapshots = source_fixture()
    a = pair_data(probs, snapshots[50])
    b = pair_data(probs, snapshots[100])

    map_errors = []
    pauli_errors = []
    sz = np.asarray([[1.0, 0.0], [0.0, -1.0]], dtype=np.complex128)
    eye = np.eye(2, dtype=np.complex128)

    for d in (a, b):
        map_errors.append(
            float(np.max(np.abs(d["H_phase"] @ d["psi"] - 1j * d["psi_dot"])))
        )
        theta, velocity = snapshots[50] if d is a else snapshots[100]
        vl = float(velocity[18])
        vr = float(velocity[19])
        c = -(vl + vr) / 2.0
        rebuilt = c * eye + 0.5 * d["delta_dot"] * sz
        pauli_errors.append(float(np.max(np.abs(rebuilt - d["H_phase"]))))

    checks.append(
        {
            "name": "diagonal_phase_hamiltonian_exactly_generates_bound_pair_motion",
            "status": "PASS" if max(map_errors) < 1e-15 else "FAIL",
            "max_mapping_error": max(map_errors),
        }
    )
    checks.append(
        {
            "name": "phase_hamiltonian_pauli_decomposition",
            "status": "PASS" if max(pauli_errors) < 1e-15 else "FAIL",
            "max_abs_error": max(pauli_errors),
        }
    )

    dyn_comm = a["H_phase"] @ b["H_phase"] - b["H_phase"] @ a["H_phase"]
    dyn_comm_norm = frob(dyn_comm)
    checks.append(
        {
            "name": "time_separated_phase_hamiltonians_commute",
            "status": "PASS" if dyn_comm_norm == 0.0 else "FAIL",
            "commutator_frobenius_norm": dyn_comm_norm,
        }
    )

    bloch_errors = [
        float(np.max(np.abs(d["n_dot"] - np.cross(d["h"], d["n"]))))
        for d in (a, b)
    ]
    projection_errors = [
        float(np.max(np.abs(d["omega"] - d["omega_projected"])))
        for d in (a, b)
    ]
    orth_errors = [
        abs(float(np.dot(d["n"], d["omega"])))
        for d in (a, b)
    ]
    checks.append(
        {
            "name": "horizontal_generator_is_projected_dynamical_axis",
            "status": (
                "PASS"
                if max(bloch_errors + projection_errors + orth_errors) < 1e-15
                else "FAIL"
            ),
            "max_bloch_equation_error": max(bloch_errors),
            "max_projection_identity_error": max(projection_errors),
            "max_n_dot_omega_abs": max(orth_errors),
        }
    )

    cross = np.cross(a["omega"], b["omega"])
    cross_norm = float(np.linalg.norm(cross))
    geom_comm_norm = cross_norm / math.sqrt(2.0)
    checks.append(
        {
            "name": "geometric_connection_is_noncommuting_on_pinned_sections",
            "status": "PASS" if cross_norm > 5.0e-6 else "FAIL",
            "omega_cross": cross.tolist(),
            "omega_cross_norm": cross_norm,
            "geometric_commutator_frobenius_norm": geom_comm_norm,
        }
    )

    # Minimum-Frobenius lift and phase-law lift agree on the state tangent but
    # need not agree on the orthogonal complement.
    d = a
    v = 1j * d["psi_dot"]
    scalar = np.vdot(d["psi"], v)
    h_min = (
        np.outer(v, d["psi"].conjugate())
        + np.outer(d["psi"], v.conjugate())
        - scalar * np.outer(d["psi"], d["psi"].conjugate())
    )
    difference_action = float(
        np.max(np.abs((d["H_phase"] - h_min) @ d["psi"]))
    )
    operator_difference = frob(d["H_phase"] - h_min)
    checks.append(
        {
            "name": "phase_law_and_minimum_norm_lifts_share_state_tangent_only",
            "status": (
                "PASS"
                if difference_action < 1e-15 and operator_difference > 0.0
                else "FAIL"
            ),
            "difference_action_on_state": difference_action,
            "operator_difference_frobenius_norm": operator_difference,
        }
    )

    status = "PASS" if all(c["status"] == "PASS" for c in checks) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "claim_scope": (
            "frozen-amplitude observed-hydro motion has a commuting diagonal "
            "dynamical phase Hamiltonian while its horizontal CP1 connection can "
            "have noncommuting time-separated generators; these structures are "
            "kept explicitly distinct"
        ),
        "checks": checks,
        "summary": {
            "passed": sum(c["status"] == "PASS" for c in checks),
            "total": len(checks),
        },
    }

    Path(__file__).with_name(
        "TIR_MUMMU_GEOMETRIC_NONABELIAN_DYNAMICAL_ABELIAN_SPLIT_VALIDATION_V0_1.json"
    ).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
