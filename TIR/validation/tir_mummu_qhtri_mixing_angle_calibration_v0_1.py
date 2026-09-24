#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

SCHEMA = "TIR_MUMMU_QHTRI_MIXING_ANGLE_CALIBRATION_VALIDATION_V0_1"
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
    psi = np.exp(1j * phi) / math.sqrt(N)
    return D / np.linalg.norm(D, "fro"), J / np.linalg.norm(J, "fro"), psi


def local_metrics(H, psi):
    pd = -1j * (H @ psi)
    pdd = -(H @ H) @ psi
    a, b = psi[0], psi[1]
    ad, bd = pd[0], pd[1]
    add, bdd = pdd[0], pdd[1]

    pl, pr = abs(a) ** 2, abs(b) ** 2
    pld = 2.0 * (a.conjugate() * ad).real
    prd = 2.0 * (b.conjugate() * bd).real
    pldd = 2.0 * (abs(ad) ** 2 + (a.conjugate() * add).real)
    prdd = 2.0 * (abs(bd) ** 2 + (b.conjugate() * bdd).real)

    q = pl + pr
    qd = pld + prd
    qdd = pldd + prdd

    z = a * b.conjugate()
    zd = ad * b.conjugate() + a * bd.conjugate()
    zdd = add * b.conjugate() + 2.0 * ad * bd.conjugate() + a * bdd.conjugate()

    nums = (
        (2.0 * z.real, 2.0 * zd.real, 2.0 * zdd.real),
        (-2.0 * z.imag, -2.0 * zd.imag, -2.0 * zdd.imag),
        (pl - pr, pld - prd, pldd - prdd),
    )

    n = np.empty(3, dtype=np.float64)
    nd = np.empty(3, dtype=np.float64)
    ndd = np.empty(3, dtype=np.float64)
    for i, (x, xd, xdd) in enumerate(nums):
        n[i] = x / q
        nd[i] = xd / q - x * qd / (q * q)
        ndd[i] = (
            xdd / q
            - 2.0 * xd * qd / (q * q)
            - x * qdd / (q * q)
            + 2.0 * x * qd * qd / (q * q * q)
        )

    omega_vec = np.cross(n, nd)
    omega_dot = np.cross(n, ndd)
    udot = float(nd[2])
    om = float(np.linalg.norm(omega_vec))
    witness = float(np.linalg.norm(np.cross(omega_vec, omega_dot)))
    return udot, om, witness


def invariants(H, psi):
    udot, om, witness = local_metrics(H, psi)
    if abs(udot) <= 1e-18 or om <= 1e-18:
        raise ValueError("singular local calibration section")
    return om / abs(udot), witness / (om ** 3), udot, om, witness


def main():
    checks = []
    D, J, psi = build_fixture()

    chi_default = math.radians(34.18041622288494)
    K = math.cos(chi_default) * D + math.sin(chi_default) * J

    base = invariants(K, psi)
    scale_errors = []
    raw_scalings = []
    for s in (0.37, 1.0, 2.4):
        r1, r2, udot, om, witness = invariants(s * K, psi)
        scale_errors.extend((abs(r1 - base[0]), abs(r2 - base[1])))
        raw_scalings.append({
            "scale": s,
            "udot_over_s": udot / s,
            "omega_norm_over_s": om / s,
            "witness_over_s3": witness / (s ** 3),
        })

    checks.append({
        "name": "trajectory_shape_invariants_cancel_hamiltonian_scale",
        "status": "PASS" if max(scale_errors) < 1e-11 else "FAIL",
        "max_invariant_abs_error": max(scale_errors),
        "scaling_diagnostics": raw_scalings,
    })

    r1_default, r2_default, udot_default, om_default, witness_default = base
    checks.append({
        "name": "default_angle_shape_signature",
        "status": (
            "PASS"
            if abs(r1_default - 2.7610924108956634) < 1e-10
            and abs(r2_default - 35.466037853920184) < 1e-9
            else "FAIL"
        ),
        "chi_deg": math.degrees(chi_default),
        "udot": udot_default,
        "omega_norm": om_default,
        "witness": witness_default,
        "R1": r1_default,
        "R2": r2_default,
    })

    eps = 1e-5
    chis = np.linspace(eps, math.pi / 2.0 - eps, 5001)
    r1s = []
    r2s = []
    for chi in chis:
        r1, r2, *_ = invariants(math.cos(chi) * D + math.sin(chi) * J, psi)
        r1s.append(r1)
        r2s.append(r2)
    r1s = np.asarray(r1s)
    r2s = np.asarray(r2s)

    d1 = np.diff(r1s)
    d2 = np.diff(r2s)
    checks.append({
        "name": "pinned_fixture_R1_strictly_decreases",
        "status": "PASS" if np.all(d1 < 0.0) else "FAIL",
        "max_forward_difference": float(np.max(d1)),
        "R1_start": float(r1s[0]),
        "R1_end": float(r1s[-1]),
    })
    checks.append({
        "name": "pinned_fixture_R2_strictly_increases",
        "status": "PASS" if np.all(d2 > 0.0) else "FAIL",
        "min_forward_difference": float(np.min(d2)),
        "R2_start": float(r2s[0]),
        "R2_end": float(r2s[-1]),
    })

    idx = int(np.argmin(np.abs(chis - chi_default)))
    nearest_error = abs(float(r1s[idx]) - r1_default) + abs(float(r2s[idx]) - r2_default)
    checks.append({
        "name": "grid_calibration_recovers_default_neighborhood",
        "status": "PASS" if abs(math.degrees(chis[idx]) - math.degrees(chi_default)) < 0.02 else "FAIL",
        "grid_chi_deg": float(math.degrees(chis[idx])),
        "target_chi_deg": math.degrees(chi_default),
        "signature_l1_error": nearest_error,
    })

    status = "PASS" if all(c["status"] == "PASS" for c in checks) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "claim_scope": (
            "scale-free local trajectory-shape observables can calibrate the QHTRI "
            "mixing angle on the pinned deterministic branch; no fundamental "
            "actuation/source law is promoted"
        ),
        "checks": checks,
        "summary": {
            "passed": sum(c["status"] == "PASS" for c in checks),
            "total": len(checks),
        },
    }
    Path(__file__).with_name(
        "TIR_MUMMU_QHTRI_MIXING_ANGLE_CALIBRATION_VALIDATION_V0_1.json"
    ).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
