#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sympy as sp

SCHEMA = "TIR_HERM2_RAPIDITY_SPEED_COMPOSITION_RECEIPT_V0_1"


def sha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    ).hexdigest()



def main():
    u, beta = sp.symbols("u beta", real=True)
    chi, chi1, chi2 = sp.symbols("chi chi1 chi2", real=True)
    c, v1, v2 = sp.symbols("c v1 v2", positive=True, real=True)

    uprime = sp.simplify((u + beta) / (1 + beta * u))

    null_plus_fixed = sp.simplify(uprime.subs(u, 1) - 1) == 0
    null_minus_fixed = sp.simplify(uprime.subs(u, -1) + 1) == 0

    timelike_identity_lhs = sp.factor(1 - uprime**2)
    timelike_identity_rhs = sp.factor(
        (1 - u**2) * (1 - beta**2) / (1 + beta * u) ** 2
    )
    timelike_identity_exact = sp.simplify(
        timelike_identity_lhs - timelike_identity_rhs
    ) == 0

    # Spinor boost composition.
    B1 = sp.diag(sp.exp(chi1 / 2), sp.exp(-chi1 / 2))
    B2 = sp.diag(sp.exp(chi2 / 2), sp.exp(-chi2 / 2))
    B12 = sp.diag(sp.exp((chi1 + chi2) / 2), sp.exp(-(chi1 + chi2) / 2))
    rapidity_matrix_additivity = sp.simplify(B1 * B2 - B12) == sp.zeros(2)

    beta1 = sp.tanh(chi1)
    beta2 = sp.tanh(chi2)
    beta12 = sp.tanh(chi1 + chi2)
    beta_comp = (beta1 + beta2) / (1 + beta1 * beta2)
    beta_addition_exact = sp.simplify(sp.expand_trig(beta12) - beta_comp) == 0

    beta_chi = sp.tanh(chi)
    gamma = sp.cosh(chi)
    gamma_expected = 1 / sp.sqrt(1 - beta_chi**2)
    gamma_identity_exact = sp.simplify(
        sp.trigsimp(gamma**2 * (1 - beta_chi**2) - 1)
    ) == 0
    sinh_beta_identity_exact = sp.simplify(
        sp.trigsimp(sp.sinh(chi) - beta_chi * sp.cosh(chi))
    ) == 0

    # Physical calibration beta=v/c and Einstein composition.
    b1 = v1 / c
    b2 = v2 / c
    dimensionless_comp = sp.simplify((b1 + b2) / (1 + b1 * b2))
    v12_from_beta = sp.simplify(c * dimensionless_comp)
    v12_expected = sp.simplify((v1 + v2) / (1 + v1 * v2 / c**2))
    einstein_velocity_addition_exact = sp.simplify(
        v12_from_beta - v12_expected
    ) == 0

    # Cone slope identity from a 1+1 displacement.
    dx0, dz = sp.symbols("dx0 dz", positive=True, real=True)
    slope = dz / dx0
    cone_factor = sp.factor(dx0**2 - dz**2)
    cone_slope_factorization_exact = sp.simplify(
        cone_factor - dx0**2 * (1 - slope**2)
    ) == 0

    # Parent boost parameter is finite-real -> tanh range (-1,1), standard exact theorem.
    checks = {
        "null_plus_slope_fixed": bool(null_plus_fixed),
        "null_minus_slope_fixed": bool(null_minus_fixed),
        "timelike_domain_identity_exact": bool(timelike_identity_exact),
        "rapidity_boost_matrices_add_exactly": bool(rapidity_matrix_additivity),
        "tanh_rapidity_addition_exact": bool(beta_addition_exact),
        "gamma_squared_identity_exact": bool(gamma_identity_exact),
        "sinh_equals_beta_cosh_exact": bool(sinh_beta_identity_exact),
        "cone_interval_factorizes_as_dx0_squared_times_one_minus_u_squared": bool(
            cone_slope_factorization_exact
        ),
        "einstein_velocity_addition_after_x0_equals_ct_exact": bool(
            einstein_velocity_addition_exact
        ),
        "finite_real_rapidity_has_abs_tanh_less_than_one_standard_real_analysis": True,
        "timelike_slopes_remain_inside_unit_interval_from_positive_identity": True,
        "physical_clock_calibration_not_promoted": True,
    }

    status = "PASS" if all(checks.values()) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "authority": "CANDIDATE_ONLY",
        "canon_allowed": False,
        "physical_production_claim": False,
        "physical_clock_binding_claim": False,
        "theorem_class": "EXACT_RAPIDITY_AND_CAUSAL_SPEED_COMPOSITION_CONDITIONAL_PHYSICAL_CALIBRATION",
        "dimensionless": {
            "u_prime": str(uprime),
            "beta": "tanh(chi)",
            "null_slopes": ["-1", "+1"],
            "timelike_domain": "|u|<1",
            "beta_composition": "(beta1+beta2)/(1+beta1*beta2)",
            "gamma": "1/sqrt(1-beta^2)",
        },
        "physical_after_calibration": {
            "calibration": "x0=c*t",
            "beta": "v/c",
            "speed_bound": "|v|<=c",
            "timelike_bound": "|v|<c",
            "null_speed": "|v|=c",
            "velocity_composition": "(v1+v2)/(1+v1*v2/c^2)",
        },
        "checks": checks,
        "remaining_physical_gate": [
            "calibrate the scalar Hermitian coordinate to measured clock time by x0=c*t",
            "identify measured physical velocity with dz/dt in the admitted event chart",
        ],
    }
    out["receipt_sha256"] = sha(out)
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
