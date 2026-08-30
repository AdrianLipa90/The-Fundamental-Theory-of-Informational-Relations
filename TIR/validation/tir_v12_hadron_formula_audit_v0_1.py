#!/usr/bin/env python3
from __future__ import annotations

import json
import math

KAPPA = math.log(2.0) / (24.0 * math.pi)
E_PROTON_MEV = 938.272
E_PLANCK_MEV = 1.22089e22
L3, L4, L5 = 7, 2, 5
Q_U, Q_D, Q_S = 3, 5, 7


def relerr(a: float, b: float) -> float:
    return abs(a - b) / abs(b)


def main() -> None:
    # Legacy octet M0 text defines S0=((s+u)/L3)*kappa, but the stated
    # universal exponential would then contain S0/kappa=(s+u)/L3.
    s0_over_kappa = (Q_S + Q_U) / L3
    literal_planck_m0 = E_PLANCK_MEV * math.exp(-s0_over_kappa)

    # The printed numerical M0 instead uses a proton-anchored first-order map
    # with x=((s+u)/L3)*kappa.
    anchored_x = s0_over_kappa * KAPPA
    printed_map_m0 = E_PROTON_MEV * (1.0 - anchored_x)
    exact_anchored_exp_m0 = E_PROTON_MEV * math.exp(-anchored_x)

    alpha = E_PROTON_MEV * KAPPA * (Q_S**2 - Q_U**2 - Q_D**2 + L3)
    beta = -alpha * (L3**2 - 1) / L3**2
    gamma = alpha * L4 * (L3 - L4) / L3**2

    octet = {
        "N": printed_map_m0 + alpha + beta + gamma / 2.0,
        "Lambda": printed_map_m0 + alpha,
        "Sigma": printed_map_m0 + alpha + 2.0 * gamma,
        "Xi": printed_map_m0 + alpha - beta + gamma / 2.0,
    }
    gmo_left = 0.5 * (octet["N"] + octet["Xi"])
    gmo_right = 0.75 * octet["Lambda"] + 0.25 * octet["Sigma"]

    # Legacy pseudoscalar printed exponentials.
    pion_literal_mev = E_PLANCK_MEV * math.exp(-6.0 / math.pi)
    kaon_literal_mev = E_PLANCK_MEV * math.exp(-(math.pi**2 / 6.0 - 1.0))

    checks = {
        "kappa_finite": math.isfinite(KAPPA),
        "legacy_M0_exponent_is_10_over_7": abs(s0_over_kappa - 10.0 / 7.0) < 1e-15,
        "printed_M0_map_reproduces_925_95": relerr(printed_map_m0, 925.95) < 2e-5,
        "universal_planck_exponential_does_not_reproduce_printed_M0": relerr(literal_planck_m0, 925.95) > 1e12,
        "anchored_linearization_is_distinct_from_declared_planck_exponential": relerr(printed_map_m0, literal_planck_m0) > 1e12,
        "gmo_identity_holds_for_constructed_octet": abs(gmo_left - gmo_right) < 1e-10,
        "pion_printed_exponential_fails_target": relerr(pion_literal_mev, 139.57) > 1e12,
        "kaon_printed_exponential_fails_target": relerr(kaon_literal_mev, 493.68) > 1e12,
    }

    status = "PASS_WITH_QUARANTINES" if all(checks.values()) else "FAIL_AUDIT"
    receipt = {
        "schema": "TIR_V12_HADRON_FORMULA_AUDIT_V0_1",
        "status": status,
        "kappa": KAPPA,
        "octet_m0": {
            "legacy_declared_S0_over_kappa": s0_over_kappa,
            "literal_planck_exponential_MeV": literal_planck_m0,
            "printed_proton_anchored_linear_map_MeV": printed_map_m0,
            "proton_anchored_exact_exponential_MeV": exact_anchored_exp_m0,
            "v12_status": "QUARANTINED_DERIVATION",
        },
        "octet_coefficients_MeV": {"alpha": alpha, "beta": beta, "gamma": gamma},
        "octet_constructed_masses_MeV": octet,
        "gmo_identity_residual_MeV": gmo_left - gmo_right,
        "pseudoscalar_literal_MeV": {"pion": pion_literal_mev, "kaon": kaon_literal_mev},
        "pseudoscalar_v12_status": "FAIL_LEGACY_PRINTED_FORMULAS",
        "heavy_vector_table_status": "QUARANTINED_PROVENANCE_INCOMPLETE",
        "checks": checks,
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS_WITH_QUARANTINES" else 1)


if __name__ == "__main__":
    main()
