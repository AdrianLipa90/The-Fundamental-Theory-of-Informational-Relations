#!/usr/bin/env python3
from __future__ import annotations

import cmath
import itertools
import json
import math

SCHEMA = "TIR_CKM_JARLSKOG_INVARIANT_CLOSURE_V0_1"
TOL = 1e-12


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def dagger(a):
    return [[a[j][i].conjugate() for j in range(len(a))] for i in range(len(a[0]))]


def eye(n):
    return [[1.0 + 0j if i == j else 0j for j in range(n)] for i in range(n)]


def det3(a):
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def maxdiff(a, b):
    return max(abs(a[i][j] - b[i][j]) for i in range(len(a)) for j in range(len(a[0])))


def build_ckm(s12: float, s23: float, s13: float, delta: float):
    c12 = math.sqrt(1.0 - s12 * s12)
    c23 = math.sqrt(1.0 - s23 * s23)
    c13 = math.sqrt(1.0 - s13 * s13)

    r12 = [
        [c12, s12, 0.0],
        [-s12, c12, 0.0],
        [0.0, 0.0, 1.0],
    ]
    r13 = [
        [c13, 0.0, s13 * cmath.exp(-1j * delta)],
        [0.0, 1.0, 0.0],
        [-s13 * cmath.exp(1j * delta), 0.0, c13],
    ]
    r23 = [
        [1.0, 0.0, 0.0],
        [0.0, c23, s23],
        [0.0, -s23, c23],
    ]
    return mm(mm(r23, r13), r12), (c12, c23, c13)


def quartet(V, i: int, j: int, a: int, b: int) -> float:
    q = V[i][a] * V[j][b] * V[i][b].conjugate() * V[j][a].conjugate()
    return float(q.imag)


def main() -> int:
    kappa = math.log(2.0) / (24.0 * math.pi)
    A = 2.0 / 7.0
    B = 2.0 / 9.0
    C = 2.0 / 5.0

    s12 = B + A * kappa
    s23 = A * A / 2.0
    s13 = A * A * B * C / 2.0
    delta = math.acos(C)

    V, (c12, c23, c13) = build_ckm(s12, s23, s13, delta)
    J_formula = s12 * s23 * s13 * c12 * c23 * c13 * c13 * math.sin(delta)
    J_quartet = quartet(V, 0, 1, 0, 1)

    quartet_values = {}
    quartet_magnitudes = []
    for i, j in itertools.combinations(range(3), 2):
        for a, b in itertools.combinations(range(3), 2):
            q = quartet(V, i, j, a, b)
            quartet_values[f"rows_{i}{j}_cols_{a}{b}"] = q
            quartet_magnitudes.append(abs(q))

    unitarity_residual = maxdiff(mm(V, dagger(V)), eye(3))
    determinant_residual = abs(det3(V) - 1.0)
    quartet_spread = max(abs(x - abs(J_formula)) for x in quartet_magnitudes)

    J_old = kappa * kappa * C * (1.0 - C * C / 2.0)
    old_relative_gap = abs(J_old - abs(J_formula)) / J_old
    mixing_jacobian = (
        s12 * s23 * s13 * c12 * c23 * c13 * c13
    ) / (kappa * kappa * C)
    exact_factorization = kappa * kappa * C * mixing_jacobian * math.sqrt(1.0 - C * C)

    stage32_wrong_denominator = s12 * s23 * s13 * c12 * c23 * c13
    exact_denominator = s12 * s23 * s13 * c12 * c23 * c13 * c13

    checks = {
        "ckm_unitary": unitarity_residual < TOL,
        "ckm_det_one": determinant_residual < TOL,
        "standard_formula_matches_reference_quartet": abs(J_formula - J_quartet) < TOL,
        "all_nine_quartets_share_common_abs_J": quartet_spread < TOL,
        "historical_assignment_is_not_exact_current_ckm_J": abs(J_old - abs(J_formula)) > 1e-7,
        "historical_gap_matches_recorded_four_point_four_percent_scale": 0.044 < old_relative_gap < 0.045,
        "factorized_exact_J_matches_standard_J": abs(exact_factorization - abs(J_formula)) < TOL,
        "stage32_denominator_missing_one_c13_factor": abs(stage32_wrong_denominator * c13 - exact_denominator) < TOL,
    }

    status = "PASS" if all(checks.values()) else "FAIL"
    receipt = {
        "schema": SCHEMA,
        "status": status,
        "epistemic": "EXACT_CKM_INVARIANT_CLOSURE__MIXING_WEIGHT_UPSTREAM_OPEN",
        "inputs": {
            "kappa": kappa,
            "A": A,
            "B": B,
            "C": C,
            "s12": s12,
            "s23": s23,
            "s13": s13,
            "delta_deg": math.degrees(delta),
        },
        "invariant": {
            "J_standard_formula": J_formula,
            "J_reference_quartet": J_quartet,
            "quartets": quartet_values,
            "quartet_abs_spread": quartet_spread,
        },
        "matrix_checks": {
            "unitarity_residual_max_abs": unitarity_residual,
            "determinant_minus_one_abs": determinant_residual,
        },
        "historical_assignment": {
            "J_old": J_old,
            "relative_gap_to_exact_current_ckm_J": old_relative_gap,
            "status": "DEPRECATED_AS_INDEPENDENT_JARLSKOG_ASSIGNMENT",
        },
        "exact_factorization": {
            "mixing_jacobian": mixing_jacobian,
            "sin_delta": math.sqrt(1.0 - C * C),
            "kappa2_C_M_sin_delta": exact_factorization,
        },
        "stage32_formal_correction": {
            "historical_denominator_power_c13": 1,
            "exact_denominator_power_c13": 2,
            "historical_denominator": stage32_wrong_denominator,
            "exact_denominator": exact_denominator,
        },
        "checks": checks,
        "closed": {
            "J_not_independent_once_ckm_inputs_fixed": True,
            "rephasing_invariant_quartet_closure": status == "PASS",
            "historical_independent_J_assignment_deprecated": status == "PASS",
        },
        "open": {
            "first_principles_forcing_s12": True,
            "first_principles_forcing_s23": True,
            "first_principles_forcing_s13": True,
        },
        "physical_claim": False,
    }

    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
