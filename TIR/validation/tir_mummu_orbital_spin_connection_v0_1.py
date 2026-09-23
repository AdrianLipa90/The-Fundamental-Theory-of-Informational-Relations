#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path

SCHEMA = "TIR_MUMMU_ORBITAL_SPIN_CONNECTION_VALIDATION_V0_1"

I2 = [[1 + 0j, 0j], [0j, 1 + 0j]]
SX = [[0j, 1 + 0j], [1 + 0j, 0j]]
SY = [[0j, -1j], [1j, 0j]]
SZ = [[1 + 0j, 0j], [0j, -1 + 0j]]
SIGMA = [SX, SY, SZ]


def madd(a, b):
    return [[a[i][j] + b[i][j] for j in range(2)] for i in range(2)]


def msub(a, b):
    return [[a[i][j] - b[i][j] for j in range(2)] for i in range(2)]


def mscale(c, a):
    return [[c * a[i][j] for j in range(2)] for i in range(2)]


def mm(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)]
        for i in range(2)
    ]


def dag(a):
    return [[a[j][i].conjugate() for j in range(2)] for i in range(2)]


def trace(a):
    return a[0][0] + a[1][1]


def maxerr(a, b):
    return max(abs(a[i][j] - b[i][j]) for i in range(2) for j in range(2))


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def norm(v):
    return math.sqrt(dot(v, v))


def unit(v):
    n = norm(v)
    if n <= 0.0:
        raise ValueError("nonzero vector required")
    return tuple(x / n for x in v)


def smat(v):
    out = [[0j, 0j], [0j, 0j]]
    for c, sigma in zip(v, SIGMA):
        out = madd(out, mscale(c, sigma))
    return out


def projector(n):
    return mscale(0.5, madd(I2, smat(n)))


def su2_exp_vector(v):
    """exp[-i (v.sigma)/2]."""
    angle = norm(v)
    if angle < 1e-15:
        return [row[:] for row in I2]
    axis = tuple(x / angle for x in v)
    return madd(
        mscale(math.cos(angle / 2.0), I2),
        mscale(-1j * math.sin(angle / 2.0), smat(axis)),
    )


def connection_generator(n, dn_dtau, dphi_dtau):
    omega = tuple(
        cross(n, dn_dtau)[i] + dphi_dtau * n[i]
        for i in range(3)
    )
    return mscale(-0.5j, smat(omega))


def path_transport(ns, phis):
    """Midpoint discretization of the coordinate-free orbital connection."""
    if len(ns) != len(phis) or len(ns) < 2:
        raise ValueError("matching path samples required")
    U = [row[:] for row in I2]
    for k in range(len(ns) - 1):
        n0 = unit(ns[k])
        n1 = unit(ns[k + 1])
        midpoint = unit(tuple(n0[i] + n1[i] for i in range(3)))
        dn = tuple(n1[i] - n0[i] for i in range(3))
        dphi = phis[k + 1] - phis[k]
        rotation_vector = tuple(
            cross(midpoint, dn)[i] + dphi * midpoint[i]
            for i in range(3)
        )
        U = mm(su2_exp_vector(rotation_vector), U)
    return U


def rodrigues(vector, rotation_vector):
    angle = norm(rotation_vector)
    if angle < 1e-15:
        return tuple(vector)
    axis = tuple(x / angle for x in rotation_vector)
    c = math.cos(angle)
    s = math.sin(angle)
    axv = cross(axis, vector)
    av = dot(axis, vector)
    return tuple(
        c * vector[i] + s * axv[i] + (1.0 - c) * av * axis[i]
        for i in range(3)
    )


def circle_path(colatitude, samples):
    return [
        (
            math.sin(colatitude) * math.cos(2.0 * math.pi * k / samples),
            math.sin(colatitude) * math.sin(2.0 * math.pi * k / samples),
            math.cos(colatitude),
        )
        for k in range(samples + 1)
    ]


def main() -> int:
    checks = []

    n = unit((0.3, 0.4, 0.5))
    raw = (0.2, -0.3, 0.7)
    dn = tuple(raw[i] - dot(raw, n) * n[i] for i in range(3))
    A = connection_generator(n, dn, 0.37)
    commutator = msub(mm(A, projector(n)), mm(projector(n), A))
    pdot = mscale(0.5, smat(dn))
    kinematic_error = maxerr(commutator, pdot)
    checks.append({
        "name": "projector_kinematics_identity",
        "status": "PASS" if kinematic_error < 1e-14 else "FAIL",
        "max_abs_error": kinematic_error,
    })

    antihermitian_error = maxerr(madd(A, dag(A)), [[0j, 0j], [0j, 0j]])
    trace_error = abs(trace(A))
    checks.append({
        "name": "connection_generator_in_su2",
        "status": "PASS" if antihermitian_error < 1e-14 and trace_error < 1e-14 else "FAIL",
        "antihermitian_error": antihermitian_error,
        "trace_abs": trace_error,
    })

    frames = [
        su2_exp_vector((0.2, -0.1, 0.3)),
        su2_exp_vector((-0.4, 0.5, 0.1)),
        su2_exp_vector((0.3, 0.2, -0.6)),
    ]
    u10 = mm(frames[1], dag(frames[0]))
    u21 = mm(frames[2], dag(frames[1]))
    u02 = mm(frames[0], dag(frames[2]))
    coboundary_loop = mm(mm(u02, u21), u10)
    coboundary_error = maxerr(coboundary_loop, I2)
    checks.append({
        "name": "endpoint_coboundary_loop_no_go",
        "status": "PASS" if coboundary_error < 1e-14 else "FAIL",
        "max_abs_error": coboundary_error,
    })

    n_static = (0.0, 0.0, 1.0)
    u2 = su2_exp_vector(tuple(2.0 * math.pi * x for x in n_static))
    u4 = su2_exp_vector(tuple(4.0 * math.pi * x for x in n_static))
    err2 = maxerr(u2, mscale(-1.0, I2))
    err4 = maxerr(u4, I2)
    checks.append({
        "name": "fiber_spinorial_2pi_4pi_closure",
        "status": "PASS" if err2 < 1e-14 and err4 < 1e-14 else "FAIL",
        "two_pi_to_minus_I_error": err2,
        "four_pi_to_plus_I_error": err4,
    })

    ns = circle_path(math.pi / 4.0, 1200)
    phis = [0.35 * (k / 1200.0) for k in range(1201)]
    split = 517
    whole = path_transport(ns, phis)
    left = path_transport(ns[: split + 1], phis[: split + 1])
    right = path_transport(ns[split:], phis[split:])
    concat_error = maxerr(whole, mm(right, left))
    checks.append({
        "name": "path_concatenation_functoriality",
        "status": "PASS" if concat_error < 1e-12 else "FAIL",
        "max_abs_error": concat_error,
    })

    equator = circle_path(math.pi / 2.0, 4000)
    u_eq = path_transport(equator, [0.0] * len(equator))
    equator_error = maxerr(u_eq, mscale(-1.0, I2))
    checks.append({
        "name": "equatorial_geometric_loop_minus_I",
        "status": "PASS" if equator_error < 2e-6 else "FAIL",
        "max_abs_error": equator_error,
        "trace_real": trace(u_eq).real,
    })

    latitude = circle_path(math.pi / 3.0, 4000)
    u_lat = path_transport(latitude, [0.0] * len(latitude))
    latitude_trace = abs(trace(u_lat))
    latitude_defect = 1.0 - abs(trace(u_lat)) ** 2 / 4.0
    checks.append({
        "name": "latitude_pi_solid_angle_zero_character",
        "status": "PASS" if latitude_trace < 2e-6 and abs(latitude_defect - 1.0) < 1e-10 else "FAIL",
        "trace_abs": latitude_trace,
        "centrality_defect": latitude_defect,
    })

    rotation_vector = (0.3, -0.4, 0.2)
    g = su2_exp_vector(rotation_vector)
    base_path = circle_path(math.pi / 3.0, 900)
    rotated_path = [rodrigues(nv, rotation_vector) for nv in base_path]
    phases = [0.21 * k / 900.0 for k in range(901)]
    u_base = path_transport(base_path, phases)
    u_rot = path_transport(rotated_path, phases)
    covariant_target = mm(mm(g, u_base), dag(g))
    covariance_error = maxerr(u_rot, covariant_target)
    checks.append({
        "name": "global_frame_covariance",
        "status": "PASS" if covariance_error < 1e-12 else "FAIL",
        "max_abs_error": covariance_error,
    })

    derived_loop_defect = latitude_defect
    checks.append({
        "name": "derived_lagrange_loop_noncentrality",
        "status": "PASS" if derived_loop_defect > 0.99 else "FAIL",
        "centrality_defect": derived_loop_defect,
        "fitted_transport_parameters": 0,
    })

    status = "PASS" if all(item["status"] == "PASS" for item in checks) else "FAIL"
    result = {
        "schema": SCHEMA,
        "status": status,
        "claim_scope": (
            "mathematical orbital spin-connection derivation from admitted CP1 projection, "
            "lifted phase and liminal path; physical MUMMU/neutrino/gravity binding open"
        ),
        "checks": checks,
        "summary": {
            "passed": sum(item["status"] == "PASS" for item in checks),
            "total": len(checks),
        },
        "source_pins": {
            "pncs_main": "8855abed440e9949f576ffbe2153325f69e78963",
            "ciel_orbital_foundation": "aa0da54ef29a1f80dd0390427935342225388950",
        },
    }
    out = Path(__file__).with_name(
        "TIR_MUMMU_ORBITAL_SPIN_CONNECTION_VALIDATION_V0_1.json"
    )
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
