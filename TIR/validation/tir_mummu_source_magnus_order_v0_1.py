#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path

SCHEMA = "TIR_MUMMU_SOURCE_MAGNUS_ORDER_VALIDATION_V0_1"
HERE = Path(__file__).resolve().parent
SOURCE_VALIDATOR = HERE / "tir_mummu_qhtri_pair_dynamics_source_witness_v0_1.py"

spec = importlib.util.spec_from_file_location("mummu_qhtri_source", SOURCE_VALIDATOR)
if spec is None or spec.loader is None:
    raise RuntimeError("unable to load QHTRI source validator")
src = importlib.util.module_from_spec(spec)
spec.loader.exec_module(src)


def mm(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)]
        for i in range(2)
    ]


def madd(a, b):
    return [[a[i][j] + b[i][j] for j in range(2)] for i in range(2)]


def mscale(c, a):
    return [[c * a[i][j] for j in range(2)] for i in range(2)]


def trace(a):
    return a[0][0] + a[1][1]


def frob(a):
    return math.sqrt(sum(abs(a[i][j]) ** 2 for i in range(2) for j in range(2)))


I2 = [[1 + 0j, 0j], [0j, 1 + 0j]]


def su2_exp(rotvec):
    angle = src.vnorm(rotvec)
    if angle < 1e-18:
        return [row[:] for row in I2]
    nx, ny, nz = (x / angle for x in rotvec)
    sigma = [
        [nz, nx - 1j * ny],
        [nx + 1j * ny, -nz],
    ]
    return madd(
        mscale(math.cos(angle / 2.0), I2),
        mscale(-1j * math.sin(angle / 2.0), sigma),
    )


def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(2)] for i in range(2)]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def path_order_diagnostics(h, psi0, *, t_max=0.5, steps=1000):
    dt = t_max / steps
    psi = list(psi0)
    u = [row[:] for row in I2]
    vint = [0.0, 0.0, 0.0]
    checkpoints = {}
    wanted = {0.1, 0.2, 0.3, 0.4, 0.5}

    for step in range(1, steps + 1):
        psi_mid = src.rk4_step(h, psi, 0.5 * dt)
        kin = src.pair_kinematics(h, psi_mid, 0)
        omega_mid = src.cross(kin["n"], kin["n_dot"])

        u_step = su2_exp(tuple(x * dt for x in omega_mid))
        u = mm(u_step, u)
        for k in range(3):
            vint[k] += omega_mid[k] * dt

        psi = src.rk4_step(h, psi, dt)
        t = step * dt
        rounded = round(t, 10)
        if rounded in wanted:
            u1 = su2_exp(tuple(vint))
            op_defect = frob(sub(u, u1))
            trace_defect = (trace(u) - trace(u1)).real
            checkpoints[rounded] = {
                "operator_defect": op_defect,
                "operator_over_t3": op_defect / (t ** 3),
                "trace_defect": trace_defect,
                "trace_over_t6": trace_defect / (t ** 6),
                "trace_over_t4": trace_defect / (t ** 4),
            }

    return checkpoints


def main():
    checks = []
    _, _, h, psi0 = src.build_fixture()
    kin0 = src.pair_kinematics(h, psi0, 0)
    omega0 = src.cross(kin0["n"], kin0["n_dot"])
    omega_dot0 = src.cross(kin0["n"], kin0["n_ddot"])
    witness_vec = src.cross(omega0, omega_dot0)
    witness = src.vnorm(witness_vec)

    predicted = witness / (12.0 * math.sqrt(2.0))
    checks.append({
        "name": "magnus_cubic_frobenius_coefficient_from_source_witness",
        "status": "PASS" if 5.2e-5 < predicted < 5.5e-5 else "FAIL",
        "witness_norm": witness,
        "predicted_coefficient": predicted,
    })

    orth0 = abs(dot(omega0, witness_vec))
    orth1 = abs(dot(omega_dot0, witness_vec))
    checks.append({
        "name": "quartic_scalar_cross_term_orthogonality",
        "status": "PASS" if max(orth0, orth1) < 1e-18 else "FAIL",
        "omega_dot_cross_inner_abs": orth0,
        "omega_derivative_dot_cross_inner_abs": orth1,
    })

    d = path_order_diagnostics(h, psi0)
    op_vals = [d[t]["operator_over_t3"] for t in (0.1, 0.2, 0.3)]
    op_rel = abs(op_vals[0] - predicted) / predicted
    checks.append({
        "name": "source_path_order_operator_defect_is_cubic",
        "status": "PASS" if op_rel < 0.03 and all(4.8e-5 < x < 6.2e-5 for x in op_vals) else "FAIL",
        "times": [0.1, 0.2, 0.3],
        "operator_defect_over_t3": op_vals,
        "predicted_local_limit": predicted,
        "relative_error_at_t01": op_rel,
    })

    sextic = [d[t]["trace_over_t6"] for t in (0.2, 0.3, 0.4, 0.5)]
    checks.append({
        "name": "source_character_defect_consistent_with_sextic_scaling",
        "status": "PASS" if all(5e-10 < x < 2e-9 for x in sextic) else "FAIL",
        "times": [0.2, 0.3, 0.4, 0.5],
        "trace_defect_over_t6": sextic,
    })

    q02 = abs(d[0.2]["trace_over_t4"])
    q04 = abs(d[0.4]["trace_over_t4"])
    checks.append({
        "name": "no_source_quartic_scalar_plateau",
        "status": "PASS" if q02 < q04 and q02 < 1e-10 else "FAIL",
        "trace_defect_over_t4_t02": q02,
        "trace_defect_over_t4_t04": q04,
        "quartic_source_binding": "FAIL",
    })

    status = "PASS" if all(c["status"] == "PASS" for c in checks) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "claim_scope": (
            "smooth source-derived QHTRI local connection has cubic operator "
            "path-order defect; the discrete quartic scalar seam does not bind "
            "as the leading smooth-source scalar term"
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
        "TIR_MUMMU_SOURCE_MAGNUS_ORDER_VALIDATION_V0_1.json"
    ).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
