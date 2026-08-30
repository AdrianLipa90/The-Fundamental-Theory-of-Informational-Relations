#!/usr/bin/env python3
from __future__ import annotations

import json
import math

L3, L4, L5 = 7, 2, 5
KAPPA = math.log(2.0) / (24.0 * math.pi)
C_E_CM = 2.4e-16
BOUND_E_CM = 1.8e-26


def main() -> None:
    exponent = L3 + L4 + L5
    suppression = (L4 / L3) ** exponent
    theta_qcd = KAPPA * suppression
    dn = theta_qcd * C_E_CM
    bound_ratio = dn / BOUND_E_CM

    checks = {
        "exponent_is_14": exponent == 14,
        "suppression_matches_corrected_value": abs(suppression - 2.4157243620710218e-8) < 1e-22,
        "theta_matches_corrected_value": abs(theta_qcd - 2.2208116434538389e-10) < 1e-24,
        "nedm_matches_frozen_value": abs(dn - 5.329947944289213e-26) < 1e-39,
        "physical_bound_is_exceeded": bound_ratio > 1.0,
        "bound_ratio_about_2_96": abs(bound_ratio - 2.9610821912717853) < 1e-12,
    }
    status = "PASS_ARITHMETIC_PHYSICAL_FAIL_RETAINED" if all(checks.values()) else "FAIL_AUDIT"
    receipt = {
        "schema": "TIR_V12_STRONG_CP_NEDM_AUDIT_V0_1",
        "status": status,
        "inputs": {
            "kappa": KAPPA,
            "L4_over_L3": L4 / L3,
            "exponent": exponent,
            "hadronic_conversion_e_cm": C_E_CM,
            "experimental_bound_e_cm": BOUND_E_CM,
        },
        "outputs": {
            "suppression": suppression,
            "theta_QCD": theta_qcd,
            "d_n_e_cm": dn,
            "bound_ratio": bound_ratio,
        },
        "verdicts": {
            "arithmetic": "PASS",
            "frozen_physical_gate": "FAIL",
            "theta_source_derivation": "OPEN",
            "next_source_axis": "SU3_holonomy_to_topological_CP_phase_to_theta_QCD",
        },
        "checks": checks,
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS_ARITHMETIC_PHYSICAL_FAIL_RETAINED" else 1)


if __name__ == "__main__":
    main()
