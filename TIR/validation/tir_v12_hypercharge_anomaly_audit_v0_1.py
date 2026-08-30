#!/usr/bin/env python3
from __future__ import annotations

import json
from fractions import Fraction

NC = 3
Y_Q = Fraction(1, 6)
Y_UR = Fraction(2, 3)
Y_DR = Fraction(-1, 3)
Y_L = Fraction(-1, 2)
Y_ER = Fraction(-1, 1)


def q(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)


def main() -> None:
    # All anomaly sums are written over left-handed Weyl fields. Right-handed
    # fermions therefore enter through their charge-conjugate left-handed fields,
    # which supplies the minus signs below.
    a_su3_su3_y = 2 * Y_Q - Y_UR - Y_DR
    a_su2_su2_y = NC * Y_Q + Y_L
    a_y3 = NC * (2 * Y_Q**3 - Y_UR**3 - Y_DR**3) + (2 * Y_L**3 - Y_ER**3)
    a_grav_y = NC * (2 * Y_Q - Y_UR - Y_DR) + (2 * Y_L - Y_ER)

    # Global SU(2) Witten consistency: 3 coloured Q_L doublets + one L_L doublet.
    su2_doublet_count = NC + 1

    # Baryon number is a global current in the SM. For the conventional
    # T(fund)=1/2 normalization, the SU(2)_L^2 U(1)_B coefficient per generation is
    # 3*(1/3)*(1/2)=1/2.
    baryon_current_coefficient = Fraction(NC, 1) * Fraction(1, 3) * Fraction(1, 2)

    # Legacy Ch.28 labels 3Y_Q-Y_uR-Y_dR as [SU(2)]^2 U(1)_B. That expression uses
    # hypercharges rather than baryon charges and evaluates to 1/6.
    legacy_a5_expression = 3 * Y_Q - Y_UR - Y_DR

    checks = {
        "su3_squared_u1y_cancels": a_su3_su3_y == 0,
        "su2_squared_u1y_cancels": a_su2_su2_y == 0,
        "u1y_cubed_cancels": a_y3 == 0,
        "gravity_squared_u1y_cancels": a_grav_y == 0,
        "witten_su2_doublet_count_even": su2_doublet_count % 2 == 0,
        "legacy_a5_is_not_baryon_current_coefficient": legacy_a5_expression != baryon_current_coefficient,
        "legacy_a5_value_is_one_sixth": legacy_a5_expression == Fraction(1, 6),
        "baryon_current_coefficient_is_one_half_in_declared_normalization": baryon_current_coefficient == Fraction(1, 2),
    }

    status = "PASS_WITH_LEGACY_A5_QUARANTINE" if all(checks.values()) else "FAIL_AUDIT"
    receipt = {
        "schema": "TIR_V12_HYPERCHARGE_ANOMALY_AUDIT_V0_1",
        "status": status,
        "hypercharges": {"Q_L": q(Y_Q), "u_R": q(Y_UR), "d_R": q(Y_DR), "L_L": q(Y_L), "e_R": q(Y_ER)},
        "left_weyl_anomaly_coefficients": {
            "SU3^2_U1Y": q(a_su3_su3_y),
            "SU2^2_U1Y": q(a_su2_su2_y),
            "U1Y^3": q(a_y3),
            "grav^2_U1Y": q(a_grav_y),
        },
        "witten_SU2_doublet_count_per_generation": su2_doublet_count,
        "legacy_A5_expression_value": q(legacy_a5_expression),
        "SU2^2_U1B_global_current_coefficient_Tfund_half": q(baryon_current_coefficient),
        "legacy_A5_status": "QUARANTINED_LABEL_AND_CHARGE_MISMATCH",
        "tir_hypercharge_source_status": "ARITHMETIC_MAP_PASS_UNIQUENESS_OPEN",
        "checks": checks,
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS_WITH_LEGACY_A5_QUARANTINE" else 1)


if __name__ == "__main__":
    main()
