#!/usr/bin/env python3
from __future__ import annotations

import cmath
import json
import math
from pathlib import Path

SCHEMA = "TIR_MUMMU_QUARTIC_SEAM_ABELIAN_REDUCIBILITY_VALIDATION_V0_1"


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def norm2(a):
    return dot(a, a)


def stella_form(q):
    s3 = math.sqrt(3.0)
    return (
        math.cos(q[0] / s3)
        * math.cos(q[1] / s3)
        * math.cos(q[2] / s3)
    )


def c4(q):
    r2 = norm2(q)
    return sum(x**4 for x in q) - 3.0 * r2 * r2 / 5.0


def stella_quartic(q):
    r2 = norm2(q)
    return 1.0 - r2 / 6.0 + r2 * r2 / 120.0 - c4(q) / 108.0


def k_seq(a, b):
    return math.cos(a / 2.0) * math.cos(b / 2.0)


def k_const(a, b):
    return math.cos(math.hypot(a, b) / 2.0)


def obstruction(vectors):
    return 0.5 * sum(
        norm2(cross(vectors[i], vectors[j]))
        for i in range(len(vectors))
        for j in range(i + 1, len(vectors))
    )


def main() -> int:
    checks = []

    vertices = [
        (sx / math.sqrt(3.0), sy / math.sqrt(3.0), sz / math.sqrt(3.0))
        for sx in (-1.0, 1.0)
        for sy in (-1.0, 1.0)
        for sz in (-1.0, 1.0)
    ]

    probes = [
        (0.1, -0.2, 0.3),
        (0.7, 0.4, -0.5),
        (1.1, -0.9, 0.2),
    ]
    max_factorization_error = 0.0
    for q in probes:
        direct = sum(cmath.exp(1j * dot(q, n)) for n in vertices) / 8.0
        max_factorization_error = max(
            max_factorization_error,
            abs(direct - stella_form(q)),
        )
    checks.append(
        {
            "name": "stella_exact_factorization",
            "status": "PASS" if max_factorization_error < 1e-14 else "FAIL",
            "max_abs_error": max_factorization_error,
        }
    )

    scaled_remainders = []
    q0 = (0.7, -0.4, 0.2)
    for eps in [1e-1, 5e-2, 2.5e-2, 1.25e-2]:
        q = tuple(eps * x for x in q0)
        remainder = abs(stella_form(q) - stella_quartic(q))
        scaled_remainders.append(remainder / (eps**6))
    spread = max(scaled_remainders[:-1]) / min(scaled_remainders[:-1])
    checks.append(
        {
            "name": "stella_quartic_remainder_order6",
            "status": "PASS" if spread < 1.2 else "FAIL",
            "scaled_remainders": scaled_remainders,
            "spread": spread,
        }
    )

    mean = [sum(v[k] for v in vertices) / 8.0 for k in range(3)]
    second = [
        [
            sum(v[i] * v[j] for v in vertices) / 8.0
            for j in range(3)
        ]
        for i in range(3)
    ]
    third_max = max(
        abs(
            sum(v[i] * v[j] * v[k] for v in vertices) / 8.0
        )
        for i in range(3)
        for j in range(3)
        for k in range(3)
    )
    second_error = max(
        abs(second[i][j] - (1.0 / 3.0 if i == j else 0.0))
        for i in range(3)
        for j in range(3)
    )
    checks.append(
        {
            "name": "stella_isotropy_through_order3",
            "status": (
                "PASS"
                if max(map(abs, mean)) < 1e-15
                and second_error < 1e-15
                and third_max < 1e-15
                else "FAIL"
            ),
            "mean": mean,
            "second_moment_error": second_error,
            "third_moment_max_abs": third_max,
        }
    )

    commuting = [(1.0, 0.0, 0.0), (2.0, 0.0, 0.0), (-3.0, 0.0, 0.0)]
    noncommuting = [(1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0)]
    commuting_obstruction = obstruction(commuting)
    noncommuting_obstruction = obstruction(noncommuting)
    checks.append(
        {
            "name": "abelian_obstruction_zero_iff_collinear_samples",
            "status": (
                "PASS"
                if commuting_obstruction < 1e-15
                and noncommuting_obstruction > 0.0
                else "FAIL"
            ),
            "commuting_obstruction": commuting_obstruction,
            "noncommuting_obstruction": noncommuting_obstruction,
        }
    )

    a0, b0 = 0.8, 0.6
    quartic_target = (a0 * a0 * b0 * b0) / 96.0
    scaled_coefficients = []
    for eps in [1e-1, 5e-2, 2.5e-2, 1.25e-2]:
        delta = k_seq(eps * a0, eps * b0) - k_const(eps * a0, eps * b0)
        scaled_coefficients.append(delta / (eps**4))
    quartic_error = max(
        abs(value - quartic_target)
        for value in scaled_coefficients[:-1]
    )
    checks.append(
        {
            "name": "nonabelian_history_quartic_coefficient",
            "status": "PASS" if quartic_error < 2e-5 else "FAIL",
            "target": quartic_target,
            "scaled_coefficients": scaled_coefficients,
            "max_abs_error": quartic_error,
        }
    )

    eps1, eps2 = 2e-2, 1e-2
    delta1 = abs(k_seq(eps1 * a0, eps1 * b0) - k_const(eps1 * a0, eps1 * b0))
    delta2 = abs(k_seq(eps2 * a0, eps2 * b0) - k_const(eps2 * a0, eps2 * b0))
    halving_ratio = delta1 / delta2
    checks.append(
        {
            "name": "history_difference_scales_quartic",
            "status": "PASS" if 14.5 < halving_ratio < 17.5 else "FAIL",
            "ratio_halving_epsilon": halving_ratio,
        }
    )

    q0 = (0.3, -0.5, 0.4)
    a0, b0 = 0.7, 0.9
    predicted = -c4(q0) / 108.0 + (a0 * a0 * b0 * b0) / 96.0
    seam_coefficients = []
    for eps in [1e-1, 5e-2, 2.5e-2, 1.25e-2]:
        q = tuple(eps * x for x in q0)
        r2 = norm2(q)
        isotropic_stella = 1.0 - r2 / 6.0 + r2 * r2 / 120.0
        projector = stella_form(q) * k_seq(eps * a0, eps * b0)
        baseline = isotropic_stella * k_const(eps * a0, eps * b0)
        seam_coefficients.append((projector - baseline) / (eps**4))
    seam_error = max(
        abs(value - predicted)
        for value in seam_coefficients[:-1]
    )
    checks.append(
        {
            "name": "combined_mummu_quartic_seam",
            "status": "PASS" if seam_error < 2e-5 else "FAIL",
            "predicted_coefficient": predicted,
            "scaled_coefficients": seam_coefficients,
            "max_abs_error": seam_error,
        }
    )

    status = "PASS" if all(check["status"] == "PASS" for check in checks) else "FAIL"
    result = {
        "schema": SCHEMA,
        "status": status,
        "claim_scope": (
            "exact finite Stella factorization, common-frame SU(2) reducibility "
            "obstruction, and quartic asymptotics; physical MUMMU/neutrino/gravity "
            "binding remains open"
        ),
        "checks": checks,
        "summary": {
            "passed": sum(check["status"] == "PASS" for check in checks),
            "total": len(checks),
        },
    }

    receipt = Path(__file__).with_name(
        "TIR_MUMMU_QUARTIC_SEAM_ABELIAN_REDUCIBILITY_VALIDATION_V0_1.json"
    )
    receipt.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
