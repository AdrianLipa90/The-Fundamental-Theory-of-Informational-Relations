#!/usr/bin/env python3
from __future__ import annotations

import itertools
import json
import math
from pathlib import Path

import numpy as np

SCHEMA = "TIR_MUMMU_STELLA_ADAPTIVE_COUPLING_QUARTIC_CROSSWALK_VALIDATION_V0_1"


def vertices():
    return np.asarray([
        (sx, sy, sz)
        for sx, sy, sz in itertools.product((-1.0, 1.0), repeat=3)
    ], dtype=np.float64) / math.sqrt(3.0)


def structure_factor(q):
    V = vertices()
    return complex(np.mean(np.exp(1j * (V @ q))))


def factorized(q):
    return (
        math.cos(q[0] / math.sqrt(3.0))
        * math.cos(q[1] / math.sqrt(3.0))
        * math.cos(q[2] / math.sqrt(3.0))
    )


def c4(q):
    q = np.asarray(q, dtype=np.float64)
    r2 = float(np.dot(q, q))
    return float(np.sum(q ** 4) - (3.0 / 5.0) * (r2 ** 2))


def quartic_expansion(q):
    q = np.asarray(q, dtype=np.float64)
    r2 = float(np.dot(q, q))
    return 1.0 - r2 / 6.0 + (r2 ** 2) / 120.0 - c4(q) / 108.0


def main():
    checks = []

    rng = np.random.default_rng(260923)
    factor_errors = []
    imag_parts = []
    for _ in range(100):
        q = rng.normal(size=3)
        S = structure_factor(q)
        factor_errors.append(abs(S.real - factorized(q)))
        imag_parts.append(abs(S.imag))
    checks.append({
        "name": "stella_structure_factor_exact_factorization",
        "status": (
            "PASS"
            if max(factor_errors) < 1e-14 and max(imag_parts) < 1e-14
            else "FAIL"
        ),
        "max_factorization_abs_error": max(factor_errors),
        "max_imaginary_abs": max(imag_parts),
    })

    V = vertices()
    second = np.einsum("ni,nj->ij", V, V) / len(V)
    second_error = float(np.max(np.abs(second - np.eye(3) / 3.0)))
    third = np.einsum("ni,nj,nk->ijk", V, V, V) / len(V)
    third_norm = float(np.max(np.abs(third)))
    checks.append({
        "name": "stella_isotropic_second_and_zero_third_moments",
        "status": "PASS" if second_error < 1e-15 and third_norm < 1e-15 else "FAIL",
        "second_moment_max_abs_error": second_error,
        "third_moment_max_abs": third_norm,
    })

    q0 = np.asarray((0.7, -0.4, 0.2), dtype=np.float64)
    target_coeff = -c4(q0) / 108.0
    eps_values = [0.25, 0.15, 0.1, 0.06, 0.04]
    scaled = []
    for eps in eps_values:
        q = eps * q0
        S = structure_factor(q).real
        r2 = float(np.dot(q, q))
        isotropic_through_4 = 1.0 - r2 / 6.0 + (r2 ** 2) / 120.0
        scaled.append((S - isotropic_through_4) / (eps ** 4))
    rel_error = abs(scaled[-1] - target_coeff) / max(abs(target_coeff), 1e-30)
    checks.append({
        "name": "quartic_anisotropy_converges_to_minus_C4_over_108",
        "status": "PASS" if rel_error < 0.002 else "FAIL",
        "q0": q0.tolist(),
        "C4_q0": c4(q0),
        "target_coefficient": target_coeff,
        "eps_values": eps_values,
        "scaled_anisotropic_residuals": scaled,
        "relative_error_finest": rel_error,
    })

    # Equal-shell coupling potential derivative.
    q = np.asarray((0.41, -0.23, 0.67), dtype=np.float64)
    lam = -0.016555555555555556
    S = structure_factor(q).real

    def potential(gbar):
        return -lam * gbar * S

    gbar = 0.37
    eps = 1e-7
    negative_derivative = -(
        potential(gbar + eps) - potential(gbar - eps)
    ) / (2.0 * eps)
    expected_force = lam * S
    derivative_error = abs(negative_derivative - expected_force)
    checks.append({
        "name": "equal_shell_hebbian_force_equals_activity_times_stella_factor",
        "status": "PASS" if derivative_error < 1e-10 else "FAIL",
        "lambda_h": lam,
        "S_q": S,
        "finite_difference_force": negative_derivative,
        "expected_force": expected_force,
        "abs_error": derivative_error,
    })

    # Explicit finite-shell sum equals same force.
    cos_mean = float(np.mean(np.cos(V @ q)))
    shell_error = abs(cos_mean - S)
    checks.append({
        "name": "finite_cosine_shell_and_complex_structure_factor_are_same_readout",
        "status": "PASS" if shell_error < 1e-15 else "FAIL",
        "cosine_shell_mean": cos_mean,
        "structure_factor_real": S,
        "abs_error": shell_error,
    })

    # Activity reversal flips the adaptive force and its quartic coefficient.
    A_minus, A_zero, A_plus = 0.3, 0.5, 0.7
    l_minus = 0.1 * (A_minus - 0.5)
    l_zero = 0.1 * (A_zero - 0.5)
    l_plus = 0.1 * (A_plus - 0.5)
    coeff_minus = -l_minus * c4(q0) / 108.0
    coeff_zero = -l_zero * c4(q0) / 108.0
    coeff_plus = -l_plus * c4(q0) / 108.0
    checks.append({
        "name": "activity_bifurcation_flips_adaptive_stella_quartic_term",
        "status": (
            "PASS"
            if coeff_zero == 0.0
            and abs(coeff_plus + coeff_minus) < 1e-18
            and coeff_plus != 0.0
            else "FAIL"
        ),
        "coefficient_A03": coeff_minus,
        "coefficient_A05": coeff_zero,
        "coefficient_A07": coeff_plus,
        "orientation_reversal_error": abs(coeff_plus + coeff_minus),
    })

    status = "PASS" if all(c["status"] == "PASS" for c in checks) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "claim_scope": (
            "conditional on an admitted equal-weight binding of local coupling "
            "channels to the canonical eight-direction Stella relation shell, the "
            "scalar Hebbian coupling force is exactly lambda_H times the Stella "
            "structure factor and inherits the same -C4/108 quartic anisotropy"
        ),
        "checks": checks,
        "summary": {
            "passed": sum(c["status"] == "PASS" for c in checks),
            "total": len(checks),
        },
    }

    Path(__file__).with_name(
        "TIR_MUMMU_STELLA_ADAPTIVE_COUPLING_QUARTIC_CROSSWALK_VALIDATION_V0_1.json"
    ).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
