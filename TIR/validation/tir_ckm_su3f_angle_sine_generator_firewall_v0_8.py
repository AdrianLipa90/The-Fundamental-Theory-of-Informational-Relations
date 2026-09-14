#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from fractions import Fraction

Q = Fraction


def build_receipt() -> dict[str, object]:
    a = Q(2, 7)
    b = Q(2, 9)
    one_minus_b2 = Q(1) - b * b
    linear_angle_coeff_sq = a * a / one_minus_b2
    expected_coeff_sq = Q(324, 3773)  # (18/(7 sqrt(77)))^2

    kappa = math.log(2.0) / (24.0 * math.pi)
    s12 = float(b) + float(a) * kappa
    theta0 = math.asin(float(b))
    theta = math.asin(s12)
    delta_theta = theta - theta0
    first_order_angle_coeff = float(a) / math.sqrt(float(one_minus_b2))
    exact_lift_residual = abs(math.sin(theta) - s12)
    naive_angle_sine = math.sin(theta0 + float(a) * kappa)
    naive_connection_residual = naive_angle_sine - s12

    checks = {
        "one_minus_b_squared_is_77_over_81": one_minus_b2 == Q(77, 81),
        "angle_linear_coefficient_squared_exact": linear_angle_coeff_sq == expected_coeff_sq,
        "angle_linear_coefficient_is_not_a": linear_angle_coeff_sq != a * a,
        "exact_angle_lift_reconstructs_s12": exact_lift_residual < 2e-16,
        "naive_additive_connection_angle_does_not_equal_additive_sine": abs(naive_connection_residual) > 1e-6,
        "stage34_group_parameter_must_be_angle_not_sine": True,
        "primitive_coproduct_cannot_by_itself_prove_b_plus_a_kappa_as_sine": True,
        "physical_angle_to_readout_map_remains_open": True,
    }

    return {
        "schema": "TIR_CKM_SU3F_ANGLE_SINE_GENERATOR_FIREWALL_V0_8",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "epistemic_status": "EXACT_ANGLE_SINE_DISTINCTION__NAIVE_CONNECTION_ADDITIVITY_NO_GO__NONLINEAR_ANGLE_LIFT_EXACT__PHYSICAL_READOUT_MAP_OPEN_POSTDICTIVE",
        "physical_promotion": False,
        "predictive_status": "POSTDICTIVE_MECHANISM_FIREWALL_NOT_NEW_PREDICTION",
        "inputs": {"a": str(a), "b": str(b), "kappa": kappa},
        "sine_coordinate": {"s12": s12, "formula": "b+a*kappa"},
        "group_angle": {
            "theta0": theta0,
            "theta12": theta,
            "delta_theta_exact": delta_theta,
            "formula": "asin(b+a*kappa)-asin(b)",
            "linear_coefficient_at_kappa_0": first_order_angle_coeff,
            "linear_coefficient_exact": "18/(7*sqrt(77))",
            "linear_coefficient_squared": str(linear_angle_coeff_sq),
        },
        "naive_connection_test": {
            "ansatz": "theta12=asin(b)+a*kappa",
            "resulting_sine": naive_angle_sine,
            "target_sine": s12,
            "residual": naive_connection_residual,
            "verdict": "FAIL_AS_EXACT_DERIVATION",
        },
        "consequence": "A Lie-algebra primitive coproduct controls additive infinitesimal angles/generators. It cannot by itself derive an exactly additive CKM sine coordinate b+a*kappa. A separate TIR map from connection flow to the sine readout is required.",
        "open": {
            "derive_angle_to_sine_readout_map_from_TIR": True,
            "derive_exact_delta_theta_from_connection_holonomy": True,
            "prospective_validation": True,
        },
        "checks": checks,
    }


def main() -> int:
    receipt = build_receipt()
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if receipt["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
