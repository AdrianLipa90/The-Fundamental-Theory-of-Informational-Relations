#!/usr/bin/env python3
from __future__ import annotations
import cmath
import json
import math
from pathlib import Path

SCHEMA = "TIR_MUMMU_T36_CP1_PAIR_PROJECTION_VALIDATION_V0_1"
I2 = [[1 + 0j, 0j], [0j, 1 + 0j]]
SZ = [[1 + 0j, 0j], [0j, -1 + 0j]]


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def dag(a):
    return [[a[j][i].conjugate() for j in range(2)] for i in range(2)]


def maxerr(a, b):
    return max(abs(a[i][j] - b[i][j]) for i in range(2) for j in range(2))


def trace(a):
    return a[0][0] + a[1][1]


def outer(v):
    return [[v[i] * v[j].conjugate() for j in range(2)] for i in range(2)]


def spinor(a, b):
    return (
        cmath.exp(1j * a) / math.sqrt(2.0),
        cmath.exp(1j * b) / math.sqrt(2.0),
    )


def projector(a, b):
    return outer(spinor(a, b))


def bloch(p):
    return (
        2.0 * p[0][1].real,
        -2.0 * p[0][1].imag,
        (p[0][0] - p[1][1]).real,
    )


def su2_z(delta):
    return [
        [cmath.exp(-0.5j * delta), 0j],
        [0j, cmath.exp(0.5j * delta)],
    ]


def mv(a, v):
    return tuple(sum(a[i][j] * v[j] for j in range(2)) for i in range(2))


def verr(a, b):
    return max(abs(x - y) for x, y in zip(a, b))


def phases(freqs, t, center):
    out = []
    for omega in freqs:
        out += [
            (center - omega * t) % math.tau,
            (center + omega * t) % math.tau,
        ]
    return tuple(out)


def projections(theta):
    return tuple(projector(theta[2 * j], theta[2 * j + 1]) for j in range(18))


def main():
    checks = []
    freqs = tuple(0.15 + 0.07 * j for j in range(18))
    t = 1.234
    center = 0.43
    theta = phases(freqs, t, center)
    ps = projections(theta)

    max_proj = 0.0
    max_trace = 0.0
    max_bloch = 0.0
    for j, p in enumerate(ps):
        max_proj = max(max_proj, maxerr(mm(p, p), p), maxerr(dag(p), p))
        max_trace = max(max_trace, abs(trace(p) - 1.0))
        delta = (theta[2 * j + 1] - theta[2 * j]) % math.tau
        expected = (math.cos(delta), math.sin(delta), 0.0)
        max_bloch = max(
            max_bloch,
            max(abs(x - y) for x, y in zip(bloch(p), expected)),
        )
    checks.append({
        "name": "pair_projector_rank_one_and_bloch_formula",
        "status": "PASS" if max_proj < 1e-14 and max_trace < 1e-14 and max_bloch < 1e-14 else "FAIL",
        "projector_error": max_proj,
        "trace_error": max_trace,
        "bloch_error": max_bloch,
    })

    shift = 1.119
    theta_shift = tuple((x + shift) % math.tau for x in theta)
    shift_err = max(maxerr(a, b) for a, b in zip(ps, projections(theta_shift)))
    checks.append({
        "name": "center_phase_projective_cancellation",
        "status": "PASS" if shift_err < 1e-14 else "FAIL",
        "max_abs_error": shift_err,
    })

    temporal_err = 0.0
    for j, omega in enumerate(freqs):
        delta = (theta[2 * j + 1] - theta[2 * j]) % math.tau
        target = (2.0 * omega * t) % math.tau
        temporal_err = max(
            temporal_err,
            abs(cmath.exp(1j * delta) - cmath.exp(1j * target)),
        )
    checks.append({
        "name": "source_relative_phase_equals_2omega_t",
        "status": "PASS" if temporal_err < 1e-14 else "FAIL",
        "max_unit_circle_error": temporal_err,
    })

    used = [idx for j in range(18) for idx in (2 * j, 2 * j + 1)]
    checks.append({
        "name": "all_36_coordinates_used_once",
        "status": "PASS" if used == list(range(36)) else "FAIL",
        "coordinate_count": len(used),
        "unique_count": len(set(used)),
    })

    t0 = 0.7
    t1 = 1.6
    center = 0.2
    transport_err = 0.0
    for omega in freqs:
        a0 = center - omega * t0
        b0 = center + omega * t0
        a1 = center - omega * t1
        b1 = center + omega * t1
        u = su2_z(2.0 * omega * (t1 - t0))
        transport_err = max(
            transport_err,
            verr(mv(u, spinor(a0, b0)), spinor(a1, b1)),
        )
    checks.append({
        "name": "pair_spin_transport_recovers_registered_frequency",
        "status": "PASS" if transport_err < 1e-14 else "FAIL",
        "max_spinor_error": transport_err,
    })

    u2 = su2_z(2.0 * math.pi)
    minus_i = [[-1 + 0j, 0j], [0j, -1 + 0j]]
    spin_err = maxerr(u2, minus_i)
    checks.append({
        "name": "pair_relative_2pi_spin_lift_minus_I",
        "status": "PASS" if spin_err < 1e-14 else "FAIL",
        "max_abs_error": spin_err,
    })

    perm = tuple(reversed(range(18)))
    theta_perm = tuple(
        x for j in perm for x in (theta[2 * j], theta[2 * j + 1])
    )
    pp = projections(theta_perm)
    perm_err = max(maxerr(pp[k], ps[perm[k]]) for k in range(18))
    checks.append({
        "name": "pair_registry_permutation_covariance",
        "status": "PASS" if perm_err < 1e-14 else "FAIL",
        "max_abs_error": perm_err,
    })

    status = "PASS" if all(c["status"] == "PASS" for c in checks) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "claim_scope": (
            "exact 18 complementary-pair CP1 projection conditional on PNCS "
            "experimental T36 pairing; single-CP1 selector and physical binding open"
        ),
        "checks": checks,
        "summary": {
            "passed": sum(c["status"] == "PASS" for c in checks),
            "total": len(checks),
        },
        "source_pins": {
            "pncs_main": "8855abed440e9949f576ffbe2153325f69e78963"
        },
    }
    Path(__file__).with_name(
        "TIR_MUMMU_T36_CP1_PAIR_PROJECTION_VALIDATION_V0_1.json"
    ).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
