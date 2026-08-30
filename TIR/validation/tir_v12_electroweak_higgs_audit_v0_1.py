#!/usr/bin/env python3
from __future__ import annotations

import json
import math

L3, L4, L5 = 7, 2, 5
E_PROTON_MEV = 938.272
KAPPA = math.log(2.0) / (24.0 * math.pi)


def main() -> None:
    v_gev = E_PROTON_MEV * (L3**2 * L5 + L3 * L4 + L4) / 1000.0
    sin2w0 = L4 / (L3 + L4) + KAPPA
    sinw0 = math.sqrt(sin2w0)
    cosw0 = math.sqrt(1.0 - sin2w0)
    g0 = L4 / L3 + L4 / L5
    mw0 = g0 * v_gev / 2.0
    mz0 = mw0 / cosw0

    alpha_inv_tir = (L3 * L4) ** 2 - L3**2 - L4 * L5 + L4**2 * KAPPA
    alpha_tir = 1.0 / alpha_inv_tir
    e_from_alpha = math.sqrt(4.0 * math.pi * alpha_tir)

    e_from_gtheta = g0 * sinw0
    alpha_inv_from_gtheta = 4.0 * math.pi / (e_from_gtheta**2)
    g_required_by_alpha_theta = e_from_alpha / sinw0

    higgs_mass_gev = v_gev * KAPPA * (L3**2 + L4 + L5)

    checks = {
        "vev_arithmetic_reproduces_244_89_GeV": abs(v_gev - 244.89) < 0.01,
        "weak_angle_arithmetic_reproduces_0_23141537": abs(sin2w0 - 0.23141537) < 1e-8,
        "g0_is_24_over_35": abs(g0 - 24.0 / 35.0) < 1e-15,
        "mw_tree_arithmetic_reproduces_83_96_GeV": abs(mw0 - 83.96) < 0.01,
        "mz_tree_arithmetic_reproduces_95_77_GeV": abs(mz0 - 95.77) < 0.01,
        "alpha_inverse_arithmetic_reproduces_137_0367726": abs(alpha_inv_tir - 137.0367726) < 1e-9,
        "higgs_arithmetic_reproduces_126_07_GeV": abs(higgs_mass_gev - 126.07) < 0.01,
        "tree_level_charge_closure_fails": abs(alpha_inv_from_gtheta - alpha_inv_tir) > 1.0,
        "g0_differs_from_alpha_theta_required_g": abs(g0 - g_required_by_alpha_theta) > 0.01,
    }

    status = "PASS_WITH_EW_CLOSURE_GATE" if all(checks.values()) else "FAIL_AUDIT"
    receipt = {
        "schema": "TIR_V12_ELECTROWEAK_HIGGS_AUDIT_V0_1",
        "status": status,
        "structural_values": {
            "kappa": KAPPA,
            "v0_GeV": v_gev,
            "sin2_thetaW0": sin2w0,
            "g0": g0,
            "MW0_GeV": mw0,
            "MZ0_GeV": mz0,
            "alpha_inverse_TIR": alpha_inv_tir,
            "MH_retrospective_GeV": higgs_mass_gev,
        },
        "tree_level_charge_closure": {
            "e_from_g0_thetaW0": e_from_gtheta,
            "alpha_inverse_implied_by_g0_thetaW0": alpha_inv_from_gtheta,
            "e_from_TIR_alpha": e_from_alpha,
            "g_required_by_TIR_alpha_and_thetaW0": g_required_by_alpha_theta,
            "closure_status": "OPEN_INCONSISTENT_RAW_STRUCTURAL_TRIPLE",
            "required_map": "R_EW(mu,scheme) binding g, thetaW, alpha, v to one declared observable scheme",
        },
        "verdicts": {
            "v0": "OPEN",
            "sin2_thetaW0": "TENSION",
            "alpha_inverse_zero_momentum_interpretation": "FAIL",
            "MW0": "FAIL",
            "MZ0": "FAIL",
            "MH_retrospective": "FAIL",
        },
        "checks": checks,
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS_WITH_EW_CLOSURE_GATE" else 1)


if __name__ == "__main__":
    main()
