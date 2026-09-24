#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path

SCHEMA = "TIR_MUMMU_NEUTRINO_LAYERED_PROJECTOR_VALIDATION_V0_1"
HBAR_C_EVM = 1.973269804e-7
MASSES = [0.005009993910798034, 0.010019987821596087, 0.050099939107979864]


def rot2(theta, v):
    c, s = math.cos(theta), math.sin(theta)
    x, y = v
    return (c * x - s * y, s * x + c * y)


def norm(v):
    return math.sqrt(sum(x * x for x in v))


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def moire_exact(a, theta):
    return a / (2.0 * math.sin(abs(theta) / 2.0))


def explicit_sum(N, chi):
    z = 0j
    for n in range(N):
        z += complex(math.cos(n * chi), math.sin(n * chi))
    return z


def dirichlet(N, chi):
    if abs(math.sin(chi / 2)) < 1e-14:
        return complex(N, 0)
    amp = math.sin(N * chi / 2) / math.sin(chi / 2)
    phase = (N - 1) * chi / 2
    return amp * complex(math.cos(phase), math.sin(phase))


def main():
    checks = []

    raw = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]
    verts = []
    for v in raw:
        n = tuple(x / math.sqrt(3) for x in v)
        verts += [n, tuple(-x for x in n)]
    dots = sorted(
        set(round(sum(a * b for a, b in zip(v, w)), 12) for v in verts for w in verts)
    )
    target = [-1.0, -1 / 3, 1 / 3, 1.0]
    checks.append(
        {
            "name": "stella_dot_spectrum",
            "status": "PASS"
            if all(abs(a - b) < 1e-11 for a, b in zip(dots, target))
            else "FAIL",
            "value": dots,
        }
    )

    max_rel = 0.0
    a = 3.938667070526838e-6
    k = 2 * math.pi / a
    for th in [1e-6, 1e-4, 1e-2, 0.2]:
        q = norm(sub(rot2(th, (k, 0.0)), (k, 0.0)))
        L_vec = 2 * math.pi / q
        L_formula = moire_exact(a, th)
        max_rel = max(max_rel, abs(L_vec - L_formula) / L_formula)
    checks.append(
        {
            "name": "exact_moire_vector_identity",
            "status": "PASS" if max_rel < 1e-11 else "FAIL",
            "max_relative_error": max_rel,
        }
    )

    max_abs = 0.0
    for N in [2, 3, 8, 36]:
        for chi in [0.07, 0.31, 1.1, 2.2]:
            max_abs = max(max_abs, abs(explicit_sum(N, chi) - dirichlet(N, chi)))
    checks.append(
        {
            "name": "n_layer_dirichlet_projector",
            "status": "PASS" if max_abs < 1e-11 else "FAIL",
            "max_abs_error": max_abs,
        }
    )

    N = 36
    chi0 = 2 * math.pi / N
    peak = abs(explicit_sum(N, 0.0)) ** 2
    zero = abs(explicit_sum(N, chi0)) ** 2
    checks.append(
        {
            "name": "coherent_peak_N2",
            "status": "PASS" if abs(peak - N * N) < 1e-10 else "FAIL",
            "N": N,
            "peak": peak,
        }
    )
    checks.append(
        {
            "name": "first_zero_resolution_1_over_N",
            "status": "PASS" if zero < 1e-20 else "FAIL",
            "N": N,
            "zero_intensity": zero,
        }
    )

    lengths = [HBAR_C_EVM / m for m in MASSES]
    ratio = [x / lengths[0] for x in lengths]
    target_ratio = [1.0, 0.5, 0.1]
    rerr = max(abs(x - y) for x, y in zip(ratio, target_ratio))
    checks.append(
        {
            "name": "neutrino_phase_clock_inverse_mass_ratio",
            "status": "PASS" if rerr < 1e-12 else "FAIL",
            "lengths_m": lengths,
            "ratio": ratio,
        }
    )

    torsion_samples = []
    max_tauL_err = 0.0
    for L in [1.0, 6.371e6, 1.495978707e11, 3.085677581e16]:
        theta = 2 * math.asin(a / (2 * L))
        tau = theta / a
        prod = tau * L
        max_tauL_err = max(max_tauL_err, abs(prod - 1.0))
        torsion_samples.append(
            {
                "target_L_m": L,
                "delta_theta_rad": theta,
                "tau_L_per_m": tau,
                "tau_times_L": prod,
            }
        )
    checks.append(
        {
            "name": "equal_spacing_torsion_radius_collapse",
            "status": "PASS" if max_tauL_err < 1e-9 else "FAIL",
            "max_abs_tauL_minus_1": max_tauL_err,
            "samples": torsion_samples,
        }
    )

    max_lin = 0.0
    for u in [1e-9, 1e-8, 1e-7, 1e-6]:
        exact = math.exp(-2 * u)
        linear = 1 - 2 * u
        max_lin = max(max_lin, abs(exact - linear))
    checks.append(
        {
            "name": "weak_field_metric_linearization",
            "status": "PASS" if max_lin < 3e-12 else "FAIL",
            "max_abs_error": max_lin,
        }
    )

    status = "PASS" if all(c["status"] == "PASS" for c in checks) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "claim_scope": "formal layered interference and scaling only; physical neutrino/gravity binding open",
        "checks": checks,
        "summary": {
            "passed": sum(c["status"] == "PASS" for c in checks),
            "total": len(checks),
        },
        "derived": {
            "phase_clock_lengths_m": lengths,
            "phase_clock_lengths_um": [1e6 * x for x in lengths],
            "N36_peak_gain": 1296,
            "N36_first_zero_fraction_of_moire_period": 1 / 36,
        },
    }
    outpath = Path(__file__).with_name(
        "TIR_MUMMU_NEUTRINO_LAYERED_PROJECTOR_VALIDATION_V0_1.json"
    )
    outpath.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
