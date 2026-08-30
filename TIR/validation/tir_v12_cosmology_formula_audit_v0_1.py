#!/usr/bin/env python3
from __future__ import annotations

import json
import math

L3, L4, L5 = 7, 2, 5
M_PLANCK_GEV = 1.22089e19
M_REDUCED_PLANCK_GEV = 2.435e18
LEGACY_PRINTED_GEV4 = 3.3e-47


def main() -> None:
    exponent = L3 * (L4 ** L5)
    suppression = (L4 / L3) ** exponent
    log10_suppression = math.log10(suppression)

    rho_unreduced = suppression * M_PLANCK_GEV**4
    rho_reduced = suppression * M_REDUCED_PLANCK_GEV**4
    scale_required_for_legacy_value = (LEGACY_PRINTED_GEV4 / suppression) ** 0.25

    checks = {
        "exponent_is_224": exponent == 224,
        "suppression_is_finite_positive": math.isfinite(suppression) and suppression > 0.0,
        "legacy_10_minus_119_5_intermediate_mismatch": abs(log10_suppression - (-119.5)) > 1.0,
        "correct_log10_is_about_minus_121_871": abs(log10_suppression + 121.87124193446175) < 1e-12,
        "unreduced_planck_conversion_differs_from_legacy_print": abs(rho_unreduced / LEGACY_PRINTED_GEV4 - 1.0) > 1.0,
        "reduced_planck_conversion_differs_from_legacy_print": abs(rho_reduced / LEGACY_PRINTED_GEV4 - 1.0) > 0.9,
        "required_scale_is_distinct_from_both_named_planck_scales": abs(scale_required_for_legacy_value / M_PLANCK_GEV - 1.0) > 0.1 and abs(scale_required_for_legacy_value / M_REDUCED_PLANCK_GEV - 1.0) > 0.1,
    }

    status = "PASS_WITH_COSMOLOGY_QUARANTINE" if all(checks.values()) else "FAIL_AUDIT"
    receipt = {
        "schema": "TIR_V12_COSMOLOGY_FORMULA_AUDIT_V0_1",
        "status": status,
        "structural_expression": "rho_dimensionless=(L4/L3)^(L3*L4^L5)",
        "exponent": exponent,
        "dimensionless_suppression": suppression,
        "log10_dimensionless_suppression": log10_suppression,
        "unit_reconstructions_GeV4": {
            "using_unreduced_Planck_mass_1_22089e19_GeV": rho_unreduced,
            "using_reduced_Planck_mass_2_435e18_GeV": rho_reduced,
            "legacy_printed_value": LEGACY_PRINTED_GEV4,
            "mass_scale_required_to_reproduce_legacy_printed_value_GeV": scale_required_for_legacy_value,
        },
        "verdicts": {
            "dimensionless_power_arithmetic": "PASS",
            "legacy_intermediate_10^-119.5": "FAIL",
            "legacy_GeV4_conversion": "QUARANTINED_UNIT_CONVENTION",
            "Omega_Lambda_0_685": "QUARANTINED_RHO_CRIT_DERIVATION_REQUIRED",
            "label_L3_as_SU3_colour_dimension": "QUARANTINED_TYPE_LABEL",
        },
        "checks": checks,
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS_WITH_COSMOLOGY_QUARANTINE" else 1)


if __name__ == "__main__":
    main()
