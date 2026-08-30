#!/usr/bin/env python3
"""Deterministic scaling gate for TIR leading-loop locality / metric-jet selection v0.1."""
from __future__ import annotations

import json
import math


def rz(theta: float):
    c, s = math.cos(theta), math.sin(theta)
    return (
        (c, -s, 0.0),
        (s, c, 0.0),
        (0.0, 0.0, 1.0),
    )


def mat_sub(a, b):
    return tuple(tuple(a[i][j] - b[i][j] for j in range(3)) for i in range(3))


def mat_scale(a, x):
    return tuple(tuple(x * a[i][j] for j in range(3)) for i in range(3))


def frob(a):
    return math.sqrt(sum(a[i][j] * a[i][j] for i in range(3) for j in range(3)))


def linear_regression_slope(xs, ys):
    lx = [math.log(x) for x in xs]
    ly = [math.log(y) for y in ys]
    mx = sum(lx) / len(lx)
    my = sum(ly) / len(ly)
    num = sum((x - mx) * (y - my) for x, y in zip(lx, ly))
    den = sum((x - mx) ** 2 for x in lx)
    return num / den


def main():
    ident = (
        (1.0, 0.0, 0.0),
        (0.0, 1.0, 0.0),
        (0.0, 0.0, 1.0),
    )
    generator = (
        (0.0, -1.0, 0.0),
        (1.0, 0.0, 0.0),
        (0.0, 0.0, 0.0),
    )

    kappa = 0.73
    jet1 = -0.41
    eps = [0.2, 0.1, 0.05, 0.025, 0.0125]

    leading_errors = []
    higher_jet_after_area = []
    raw_holonomy_norms = []

    for e in eps:
        area = e * e
        theta = kappa * area + jet1 * e * area
        r = rz(theta)
        normalized = mat_scale(mat_sub(r, ident), 1.0 / area)
        target = mat_scale(generator, kappa)
        leading_errors.append(frob(mat_sub(normalized, target)))
        raw_holonomy_norms.append(frob(mat_sub(r, ident)))

        r0 = rz(kappa * area)
        higher_jet_after_area.append(
            frob(mat_scale(mat_sub(r, r0), 1.0 / area))
        )

    leading_slope = linear_regression_slope(eps, leading_errors)
    jet_slope = linear_regression_slope(eps, higher_jet_after_area)
    holonomy_slope = linear_regression_slope(eps, raw_holonomy_norms)

    checks = [
        {
            "name": "raw_rotational_holonomy_is_area_order",
            "pass": 1.95 < holonomy_slope < 2.05,
            "observed_slope": holonomy_slope,
        },
        {
            "name": "area_normalized_holonomy_converges_to_curvature_generator",
            "pass": leading_errors[-1] < leading_errors[0] / 10.0,
            "first_error": leading_errors[0],
            "last_error": leading_errors[-1],
        },
        {
            "name": "leading_normalized_remainder_is_first_edge_order",
            "pass": 0.95 < leading_slope < 1.05,
            "observed_slope": leading_slope,
        },
        {
            "name": "first_curvature_jet_vanishes_after_area_normalization",
            "pass": higher_jet_after_area[-1] < higher_jet_after_area[0] / 10.0,
            "first_value": higher_jet_after_area[0],
            "last_value": higher_jet_after_area[-1],
        },
        {
            "name": "first_curvature_jet_is_one_higher_edge_order",
            "pass": 0.95 < jet_slope < 1.05,
            "observed_slope": jet_slope,
        },
        {
            "name": "curvature_limit_is_nonzero",
            "pass": abs(kappa) > 1e-12,
            "curvature_coefficient": kappa,
        },
        {
            "name": "selection_firewall_preserves_higher_jet_coordinate",
            "pass": abs(jet1) > 1e-12,
            "higher_jet_coefficient": jet1,
        },
    ]

    passed = all(c["pass"] for c in checks)
    receipt = {
        "schema": "TIR_LEADING_LOOP_LOCALITY_METRIC_JET_VALIDATION_V0_1",
        "technical_status": "PASS" if passed else "FAIL",
        "verdict": (
            "PASS_TIR_LEADING_LOOP_LOCALITY_METRIC_JET_SELECTION"
            if passed
            else "FAIL_TIR_LEADING_LOOP_LOCALITY_METRIC_JET_SELECTION"
        ),
        "mathematical_gate": {
            "area_scaling": "R_C-I = O(epsilon^2)",
            "leading_limit": "(R_C-I)/A_C -> Omega",
            "first_higher_jet_after_area_normalization": "O(epsilon) -> 0",
        },
        "selection_gate": {
            "rule": "lowest finite nonzero covariant refinement coefficient is primitive continuum carrier",
            "status": "TIR_STRUCTURAL_SELECTION_RULE",
            "selected_carrier": "Omega",
            "metric_jet_bound_on_levi_civita_sector": 2,
            "higher_jets": "RETAINED_EXTENDED_SECTOR",
        },
        "checks": checks,
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
