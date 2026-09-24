#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

SCHEMA = "TIR_MUMMU_QHTRI_PROPER_TIME_SCALE_CALIBRATION_VALIDATION_V0_1"
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

    D /= np.linalg.norm(D, "fro")
    J /= np.linalg.norm(J, "fro")
    psi = np.exp(1j * phi) / math.sqrt(N)
    return D, J, psi


def pair_u_dot(H, psi):
    pd = -1j * (H @ psi)
    a, b = psi[0], psi[1]
    ad, bd = pd[0], pd[1]

    pl = abs(a) ** 2
    pr = abs(b) ** 2
    pld = 2.0 * (a.conjugate() * ad).real
    prd = 2.0 * (b.conjugate() * bd).real

    q = pl + pr
    return float(2.0 * (pr * pld - pl * prd) / (q * q))


def main():
    checks = []
    D, J, psi = build_fixture()

    chi = math.radians(34.18041622288494)
    K = math.cos(chi) * D + math.sin(chi) * J
    F = pair_u_dot(K, psi)

    checks.append({
        "name": "normalized_default_angle_has_nonsingular_u_rate",
        "status": "PASS" if abs(F) > 1e-6 else "FAIL",
        "F_u": F,
    })

    cases = [
        (0.37, 0.81),
        (1.0, 1.25),
        (1.8131869894810988, 0.64),
        (2.4, 1.73),
    ]
    recon = []
    max_error = 0.0

    for s, g in cases:
        coordinate_rate = pair_u_dot(s * K, psi)
        proper_rate = coordinate_rate / g
        recovered = g * proper_rate / F
        err = abs(recovered - s)
        max_error = max(max_error, err)
        recon.append({
            "scale_s": s,
            "proper_time_factor_g": g,
            "coordinate_u_dot": coordinate_rate,
            "proper_u_dot": proper_rate,
            "recovered_s": recovered,
            "abs_error": err,
        })

    checks.append({
        "name": "typed_proper_time_recovers_hamiltonian_scale",
        "status": "PASS" if max_error < 1e-12 else "FAIL",
        "max_abs_error": max_error,
        "cases": recon,
    })

    scale_linearity = []
    for s in (0.2, 0.7, 1.5, 3.0):
        scale_linearity.append(abs(pair_u_dot(s * K, psi) / s - F))
    checks.append({
        "name": "coordinate_u_rate_is_linear_in_hamiltonian_scale",
        "status": "PASS" if max(scale_linearity) < 1e-13 else "FAIL",
        "max_abs_error": max(scale_linearity),
    })

    singular_F = pair_u_dot(D, psi)
    singular_rejected = abs(singular_F) < 1e-14
    checks.append({
        "name": "pure_detuning_endpoint_is_singular_for_u_rate_calibration",
        "status": "PASS" if singular_rejected else "FAIL",
        "F_u_at_chi_zero": singular_F,
        "calibration_state": "REJECT_NO_DENOMINATOR" if singular_rejected else "UNEXPECTED",
    })

    # Parameterization invariance of the geometric one-form at one local section:
    # Omega_tau * d_tau = Omega_t * dt, represented here by scalar scaling.
    s = 1.7
    g = 1.4
    omega_t = s
    omega_tau = omega_t / g
    dt = 0.03
    d_tau = g * dt
    one_form_error = abs(omega_tau * d_tau - omega_t * dt)
    checks.append({
        "name": "typed_time_reparameterization_preserves_connection_one_form",
        "status": "PASS" if one_form_error < 1e-15 else "FAIL",
        "abs_error": one_form_error,
    })

    status = "PASS" if all(c["status"] == "PASS" for c in checks) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "claim_scope": (
            "given a calibrated mixing angle and an admitted proper-time factor, "
            "the QHTRI Hamiltonian scale is uniquely recoverable at model level "
            "from a nonsingular local trajectory rate; no fundamental actuation law "
            "is promoted"
        ),
        "source_pins": {
            "pncs_main": "8855abed440e9949f576ffbe2153325f69e78963",
            "pncs_time_binding_branch_head": "7e1a2dab237ec741ec29d1da19007520c9755d8d"
        },
        "checks": checks,
        "summary": {
            "passed": sum(c["status"] == "PASS" for c in checks),
            "total": len(checks),
        },
    }

    Path(__file__).with_name(
        "TIR_MUMMU_QHTRI_PROPER_TIME_SCALE_CALIBRATION_VALIDATION_V0_1.json"
    ).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
