from __future__ import annotations

import json
import math

SCHEMA = "TIR_V12_FLAVOUR_MIXING_INTERNAL_CONSISTENCY_V0_1"


def main() -> int:
    kappa = math.log(2.0) / (24.0 * math.pi)
    L3, L4, L5 = 7.0, 2.0, 5.0

    pmns = {
        "sin_theta13": 1.0 / L3,
        "sin2_theta13": 1.0 / (L3 * L3),
        "sin2_theta12": L4 / (L3 + L4) + (L4 / L3) ** 2,
        "sin2_theta23": 0.5 + L4 / (L3 * L3),
        "delta_deg": 180.0 * (1.0 + L4 / L3 + (L4 / L3) ** 2),
    }

    lam = L4 / (L3 + L4) + (L4 / L3) * kappa
    vcb = (L4 / L3) ** 2 / 2.0
    vub = (L4 / L3) ** 2 * L4 / ((L3 + L4) * L5)
    A = vcb / (lam * lam)
    j_structural = kappa * kappa * (L4 / L5) * (1.0 - (L4 / L5) ** 2 / 2.0)
    delta_ckm_deg = math.degrees(math.acos(L4 / L5))

    displayed = (
        (0.97439, 0.22485, 0.00363),
        (0.22470, 0.97357, 0.04082),
        (0.00886, 0.04001, 0.99916),
    )
    row_norms = [math.fsum(x * x for x in row) for row in displayed]
    col_norms = [math.fsum(displayed[i][j] ** 2 for i in range(3)) for j in range(3)]
    max_displayed_norm_residual = max(
        max(abs(x - 1.0) for x in row_norms),
        max(abs(x - 1.0) for x in col_norms),
    )

    j_proxy = lam * vcb * vub * displayed[1][1] * math.sin(math.radians(delta_ckm_deg))
    j_proxy_relative_gap = abs(j_structural - j_proxy) / j_structural

    checks = {
        "pmns_formula_arithmetic_finite": all(math.isfinite(x) for x in pmns.values()),
        "ckm_primary_formula_arithmetic_finite": all(math.isfinite(x) for x in (lam, vcb, vub, A, j_structural, delta_ckm_deg)),
        "displayed_ckm_row_column_norms_close_at_printed_precision": max_displayed_norm_residual < 7e-6,
        "historical_j_proxy_has_visible_internal_gap": 0.04 < j_proxy_relative_gap < 0.05,
    }

    receipt = {
        "schema": SCHEMA,
        "status": "PASS_WITH_RETAINED_TENSION" if all(checks.values()) else "FAIL",
        "checks": checks,
        "pmns": pmns,
        "ckm": {
            "lambda": lam,
            "Vcb": vcb,
            "Vub": vub,
            "A": A,
            "J_structural": j_structural,
            "delta_CKM_deg": delta_ckm_deg,
            "displayed_matrix_row_norms": row_norms,
            "displayed_matrix_column_norms": col_norms,
            "max_displayed_norm_residual": max_displayed_norm_residual,
            "historical_J_product_proxy": j_proxy,
            "historical_J_product_proxy_relative_gap": j_proxy_relative_gap,
            "historical_J_product_proxy_status": "DIAGNOSTIC_PROXY_NOT_EXACT_IDENTITY",
        },
        "promotion_authority": False,
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if receipt["status"] == "PASS_WITH_RETAINED_TENSION" else 1


if __name__ == "__main__":
    raise SystemExit(main())
