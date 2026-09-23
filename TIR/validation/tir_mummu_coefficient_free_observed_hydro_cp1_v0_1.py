#!/usr/bin/env python3
from __future__ import annotations

import cmath
import json
import math
from pathlib import Path

import numpy as np

SCHEMA = "TIR_MUMMU_COEFFICIENT_FREE_OBSERVED_HYDRO_CP1_VALIDATION_V0_1"
N = 36
TAU = 2.0 * math.pi


def temporal_z(u: float) -> complex:
    w = 1j * float(u)
    return (w - 1.0) / (w + 1.0)


def phase(z: complex) -> float:
    return float(cmath.phase(z) % TAU)


def temporal_theta(times: np.ndarray, now: float, scale: float) -> np.ndarray:
    return np.asarray(
        [phase(temporal_z((float(t) - now) / scale)) for t in times],
        dtype=np.float64,
    )


def gaussian_post_probabilities(
    times: np.ndarray, *, now: float, sigma: float
) -> np.ndarray:
    amps = np.asarray(
        [complex(math.cos(i / 7.0), math.sin(i / 7.0)) for i in range(N)],
        dtype=np.complex128,
    )
    amps /= np.linalg.norm(amps)
    weights = np.exp(-0.25 * ((times - now) / sigma) ** 2)
    post = amps * weights
    post /= np.linalg.norm(post)
    return np.abs(post) ** 2


def hydro_step(
    theta: np.ndarray,
    velocity: np.ndarray,
    drive: np.ndarray,
    *,
    density: float = 1.0,
    viscosity: float = 0.0,
    drive_gain: float = 0.05,
    coordinate_dt: float = 0.01,
) -> tuple[np.ndarray, np.ndarray, float]:
    sound_speed = math.sqrt(density)
    lapse = min(8.0, max(1.0 / 64.0, sound_speed / (1.0 + viscosity)))
    proper_dt = lapse * coordinate_dt

    d = drive / np.linalg.norm(drive)
    dot_ud = float(np.dot(velocity, d))
    force = density * d + velocity * dot_ud
    accel = drive_gain * force - viscosity * velocity
    new_velocity = velocity + proper_dt * accel
    new_theta = (theta + proper_dt * new_velocity) % TAU
    return new_theta, new_velocity, proper_dt


def omega_fixed_u(u: float, delta: float, delta_dot: float) -> np.ndarray:
    r = math.sqrt(max(0.0, 1.0 - u * u))
    return delta_dot * np.asarray(
        (
            -u * r * math.cos(delta),
            -u * r * math.sin(delta),
            r * r,
        ),
        dtype=np.float64,
    )


def w_fixed_u(u: float, delta: float) -> np.ndarray:
    r = math.sqrt(max(0.0, 1.0 - u * u))
    return np.asarray(
        (
            -u * r * math.cos(delta),
            -u * r * math.sin(delta),
            r * r,
        ),
        dtype=np.float64,
    )


def gaussian_meridian_generator(u: float, delta: float) -> np.ndarray:
    r = math.sqrt(1.0 - u * u)
    n = np.asarray(
        (r * math.cos(delta), r * math.sin(delta), u),
        dtype=np.float64,
    )
    dn_du = np.asarray(
        (
            -(u / r) * math.cos(delta),
            -(u / r) * math.sin(delta),
            1.0,
        ),
        dtype=np.float64,
    )
    return np.cross(n, dn_du)


def main() -> int:
    checks: list[dict[str, object]] = []

    # Exact canonical dual-pair NOW invariance.
    deltas = np.asarray([float(i) for i in range(1, 19)], dtype=np.float64)
    scale = 3.0

    def dual_theta(now: float) -> np.ndarray:
        out = []
        for delta in deltas:
            past = temporal_z(((now - delta) - now) / scale)
            future = 1.0 / past
            out.extend((phase(past), phase(future)))
        return np.asarray(out, dtype=np.float64)

    dual_now_error = float(np.max(np.abs(dual_theta(0.0) - dual_theta(17.25))))
    checks.append(
        {
            "name": "canonical_dual_pair_now_translation_invariant",
            "status": "PASS" if dual_now_error == 0.0 else "FAIL",
            "max_abs_error": dual_now_error,
        }
    )

    # Gaussian localization at fixed phase is a one-axis meridian flow.
    delta_probe = 0.7
    gu1 = gaussian_meridian_generator(0.2, delta_probe)
    gu2 = gaussian_meridian_generator(0.6, delta_probe)
    meridian_cross = float(np.linalg.norm(np.cross(gu1, gu2)))
    checks.append(
        {
            "name": "gaussian_fixed_phase_meridian_is_locally_abelian",
            "status": "PASS" if meridian_cross < 1e-14 else "FAIL",
            "generator_u02": gu1.tolist(),
            "generator_u06": gu2.tolist(),
            "cross_norm": meridian_cross,
        }
    )

    # Source temporal observation fixture.
    times = np.arange(N, dtype=np.float64) - 18.0
    theta0 = temporal_theta(times, now=0.0, scale=4.0)
    probs = gaussian_post_probabilities(times, now=0.0, sigma=1.0)

    left, right = 18, 19
    p_l = float(probs[left])
    p_r = float(probs[right])
    q = p_l + p_r
    u = (p_l - p_r) / q
    expected_u = math.tanh(0.25)
    checks.append(
        {
            "name": "gaussian_observation_pair_imbalance_exact_tanh_quarter",
            "status": "PASS" if abs(u - expected_u) < 2e-15 else "FAIL",
            "p_left": p_l,
            "p_right": p_r,
            "pair_support": q,
            "u": u,
            "tanh_quarter": expected_u,
            "abs_error": abs(u - expected_u),
        }
    )

    # Source hydrodynamic phase-flow fixture; no QHTRI graph Hamiltonian.
    drive = np.zeros(N, dtype=np.float64)
    drive[left] = 1.0
    theta = theta0.copy()
    velocity = np.zeros(N, dtype=np.float64)
    snapshots: dict[int, tuple[np.ndarray, np.ndarray, float, float, np.ndarray]] = {}

    for step in range(1, 101):
        theta, velocity, _ = hydro_step(theta, velocity, drive)
        if step in (50, 100):
            delta = float(((theta[right] - theta[left] + math.pi) % TAU) - math.pi)
            delta_dot = float(velocity[right] - velocity[left])
            omega = omega_fixed_u(u, delta, delta_dot)
            snapshots[step] = (theta.copy(), velocity.copy(), delta, delta_dot, omega)

    omega50 = snapshots[50][4]
    omega100 = snapshots[100][4]
    omega_cross = np.cross(omega50, omega100)
    witness = float(np.linalg.norm(omega_cross))
    checks.append(
        {
            "name": "observed_hydro_pair_nonabelian_witness_without_qhtri_graph_coefficients",
            "status": "PASS" if witness > 5.0e-6 else "FAIL",
            "step50_delta": snapshots[50][2],
            "step50_delta_dot": snapshots[50][3],
            "step50_omega": omega50.tolist(),
            "step100_delta": snapshots[100][2],
            "step100_delta_dot": snapshots[100][3],
            "step100_omega": omega100.tolist(),
            "omega_cross": omega_cross.tolist(),
            "cross_norm": witness,
            "uses_qhtri_graph_hamiltonian": False,
        }
    )

    # Exact cross-product identity for the fixed-imbalance carrier.
    d1 = snapshots[50][2]
    d2 = snapshots[100][2]
    r = math.sqrt(1.0 - u * u)
    w1 = w_fixed_u(u, d1)
    w2 = w_fixed_u(u, d2)
    formula = np.asarray(
        (
            u * r**3 * (math.sin(d2) - math.sin(d1)),
            u * r**3 * (math.cos(d1) - math.cos(d2)),
            u * u * r * r * math.sin(d2 - d1),
        ),
        dtype=np.float64,
    )
    cross_identity_error = float(np.max(np.abs(np.cross(w1, w2) - formula)))
    checks.append(
        {
            "name": "fixed_imbalance_cross_product_identity",
            "status": "PASS" if cross_identity_error < 1e-15 else "FAIL",
            "max_abs_error": cross_identity_error,
        }
    )

    # Canonical minimum-Frobenius Hermitian lift of the known trajectory.
    theta50 = snapshots[50][0]
    velocity50 = snapshots[50][1]
    psi = np.sqrt(probs) * np.exp(1j * theta50)
    psi /= np.linalg.norm(psi)
    psi_dot = 1j * velocity50 * psi
    v = 1j * psi_dot
    a = np.vdot(psi, v)

    h_min = (
        np.outer(v, psi.conjugate())
        + np.outer(psi, v.conjugate())
        - a * np.outer(psi, psi.conjugate())
    )
    herm_error = float(np.max(np.abs(h_min - h_min.conjugate().T)))
    map_error = float(np.max(np.abs(h_min @ psi - v)))
    checks.append(
        {
            "name": "minimum_norm_lift_is_hermitian_and_maps_trajectory",
            "status": "PASS" if herm_error < 1e-15 and map_error < 1e-15 else "FAIL",
            "psi_norm_error": abs(float(np.vdot(psi, psi).real) - 1.0),
            "psi_v_inner_real": float(a.real),
            "psi_v_inner_imag_abs": abs(float(a.imag)),
            "hermiticity_error": herm_error,
            "mapping_error": map_error,
            "Hmin_frobenius_norm": float(np.linalg.norm(h_min, "fro")),
        }
    )

    # Any Hermitian B with B psi=0 is extra norm. Use a deterministic nonzero witness.
    projector_perp = np.eye(N, dtype=np.complex128) - np.outer(psi, psi.conjugate())
    b = (
        projector_perp
        @ np.diag(np.linspace(-0.2, 0.3, N, dtype=np.float64))
        @ projector_perp
    )
    h_alt = h_min + b
    b_psi_error = float(np.max(np.abs(b @ psi)))
    b_herm_error = float(np.max(np.abs(b - b.conjugate().T)))
    alt_map_error = float(np.max(np.abs(h_alt @ psi - v)))
    hmin_norm2 = float(np.linalg.norm(h_min, "fro") ** 2)
    halt_norm2 = float(np.linalg.norm(h_alt, "fro") ** 2)
    b_norm2 = float(np.linalg.norm(b, "fro") ** 2)
    pythag_error = abs((halt_norm2 - hmin_norm2) - b_norm2)

    checks.append(
        {
            "name": "minimum_frobenius_lift_strictly_beats_nonzero_orthogonal_extension",
            "status": (
                "PASS"
                if b_psi_error < 1e-15
                and b_herm_error < 1e-15
                and alt_map_error < 1e-15
                and halt_norm2 > hmin_norm2
                and pythag_error < 1e-12
                else "FAIL"
            ),
            "B_psi_error": b_psi_error,
            "B_hermiticity_error": b_herm_error,
            "alternate_mapping_error": alt_map_error,
            "Hmin_norm2": hmin_norm2,
            "Halt_norm2": halt_norm2,
            "B_norm2": b_norm2,
            "pythagorean_norm2_error": pythag_error,
        }
    )

    status = "PASS" if all(c["status"] == "PASS" for c in checks) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "claim_scope": (
            "source-component temporal observation amplitudes plus PNCS hydrodynamic "
            "T36 phase flow admit a conditional coefficient-free local CP1 "
            "non-Abelian witness and a unique minimum-Frobenius descriptive "
            "Hermitian lift; native PNCS observation-to-hydro cross-binding and "
            "physical realization remain open"
        ),
        "source_pins": {
            "pncs_main": "8855abed440e9949f576ffbe2153325f69e78963"
        },
        "explicit_firewalls": {
            "qhtri_graph_coefficients_used": False,
            "native_observation_hydro_binding_exists": False,
            "predictive_hamiltonian_claimed": False,
            "physical_binding_claimed": False,
        },
        "checks": checks,
        "summary": {
            "passed": sum(c["status"] == "PASS" for c in checks),
            "total": len(checks),
        },
    }

    Path(__file__).with_name(
        "TIR_MUMMU_COEFFICIENT_FREE_OBSERVED_HYDRO_CP1_VALIDATION_V0_1.json"
    ).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
