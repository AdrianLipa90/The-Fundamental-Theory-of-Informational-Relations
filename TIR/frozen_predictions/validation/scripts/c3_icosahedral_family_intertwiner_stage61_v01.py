#!/usr/bin/env python3
"""Stage 61 — explicit C3-compatible intertwiner between TIR family operators
and the six-axis icosahedral quadrupole carrier.

Verifies:
  * frozen P3 is an icosahedral order-3 symmetry,
  * the six axes split into two P3 3-cycles,
  * pair differences span the 3D off-diagonal symmetric sector,
  * pair sums span the 2D diagonal traceless sector,
  * A_seed = sqrt(5)/4 (Q1-Q4),
  * D0 is an exact linear combination of the three pair sums,
  * C3 orbits of A_seed and D0 have ranks 3 and 2 respectively.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results"
OUT.mkdir(parents=True, exist_ok=True)
TOL = 1e-10


def canonical_axes() -> list[np.ndarray]:
    phi = (1.0 + math.sqrt(5.0)) / 2.0
    vertices: list[np.ndarray] = []
    for s1 in (-1.0, 1.0):
        for s2 in (-1.0, 1.0):
            vertices.extend(
                [
                    np.array([0.0, s1, s2 * phi]),
                    np.array([s1, s2 * phi, 0.0]),
                    np.array([s2 * phi, 0.0, s1]),
                ]
            )
    norm = float(np.linalg.norm(vertices[0]))
    axes: list[np.ndarray] = []
    for v in vertices:
        u = v / norm
        for value in u:
            if abs(value) > 1e-12:
                if value < 0:
                    u = -u
                break
        if not any(np.max(np.abs(u - a)) < 1e-12 for a in axes):
            axes.append(u)
    return axes


def span_rank(mats: list[np.ndarray]) -> int:
    return int(np.linalg.matrix_rank(np.stack([M.ravel() for M in mats], axis=1), TOL))


def main() -> None:
    axes = canonical_axes()
    quadrupoles = [np.outer(u, u) - np.eye(3) / 3.0 for u in axes]

    P3 = np.array(
        [
            [0.0, 0.0, 1.0],
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
        ]
    )

    def axis_index(w: np.ndarray) -> int:
        for i, a in enumerate(axes):
            if np.max(np.abs(w - a)) < 1e-10 or np.max(np.abs(w + a)) < 1e-10:
                return i
        raise RuntimeError("axis image not found")

    permutation = tuple(axis_index(P3 @ a) for a in axes)
    expected_permutation = (2, 0, 1, 5, 3, 4)

    diffs = [quadrupoles[i] - quadrupoles[i + 3] for i in range(3)]
    sums = [quadrupoles[i] + quadrupoles[i + 3] for i in range(3)]

    E12 = np.zeros((3, 3)); E12[0, 1] = E12[1, 0] = 1.0
    E23 = np.zeros((3, 3)); E23[1, 2] = E23[2, 1] = 1.0
    E13 = np.zeros((3, 3)); E13[0, 2] = E13[2, 0] = 1.0
    diff_targets = [
        (2.0 / math.sqrt(5.0)) * E23,
        (2.0 / math.sqrt(5.0)) * E12,
        (2.0 / math.sqrt(5.0)) * E13,
    ]
    pair_difference_identity_residual = max(
        float(np.max(np.abs(diffs[i] - diff_targets[i]))) for i in range(3)
    )

    diff_rank = span_rank(diffs)
    sum_rank = span_rank(sums)
    combined_rank = span_rank(diffs + sums)
    sum_relation_residual = float(np.max(np.abs(sum(sums))))

    Aseed = 0.5 * E12
    Aseed_reconstruction = (math.sqrt(5.0) / 4.0) * (quadrupoles[1] - quadrupoles[4])
    Aseed_residual = float(np.max(np.abs(Aseed - Aseed_reconstruction)))

    D = np.diag([-1.0 / 3.0, 0.0, 1.0 / math.sqrt(5.0)])
    D0 = D - np.trace(D) / 3.0 * np.eye(3)
    alpha = (19.0 + 3.0 * math.sqrt(5.0)) / 72.0
    beta = -(5.0 + 3.0 * math.sqrt(5.0)) / 72.0
    gamma = -7.0 / 36.0
    D_reconstruction = (
        alpha * (quadrupoles[0] + quadrupoles[3])
        + beta * (quadrupoles[1] + quadrupoles[4])
        + gamma * (quadrupoles[2] + quadrupoles[5])
    )
    D_residual = float(np.max(np.abs(D0 - D_reconstruction)))
    coefficient_sum_residual = abs(alpha + beta + gamma)

    A_orbit: list[np.ndarray] = []
    D_orbit: list[np.ndarray] = []
    A_current = Aseed.copy()
    D_current = D0.copy()
    for _ in range(3):
        A_orbit.append(A_current)
        D_orbit.append(D_current)
        A_current = P3 @ A_current @ P3.T
        D_current = P3 @ D_current @ P3.T

    A_orbit_rank = span_rank(A_orbit)
    D_orbit_rank = span_rank(D_orbit)
    orbit_union_rank = span_rank(A_orbit + D_orbit)

    p3_orthogonality_residual = float(np.max(np.abs(P3.T @ P3 - np.eye(3))))
    p3_order3_residual = float(np.max(np.abs(np.linalg.matrix_power(P3, 3) - np.eye(3))))
    p3_det_residual = abs(float(np.linalg.det(P3)) - 1.0)

    passed = (
        len(axes) == 6
        and permutation == expected_permutation
        and p3_orthogonality_residual < 1e-12
        and p3_order3_residual < 1e-12
        and p3_det_residual < 1e-12
        and pair_difference_identity_residual < 1e-12
        and diff_rank == 3
        and sum_rank == 2
        and combined_rank == 5
        and sum_relation_residual < 1e-12
        and Aseed_residual < 1e-12
        and D_residual < 1e-12
        and coefficient_sum_residual < 1e-12
        and A_orbit_rank == 3
        and D_orbit_rank == 2
        and orbit_union_rank == 5
    )

    receipt = {
        "schema": "TIR_POLYGONAL_STAGE61_C3_ICOSAHEDRAL_FAMILY_INTERTWINER_RECEIPT_V0_1",
        "status": (
            "STAGE_61_C3_ICOSAHEDRAL_FAMILY_INTERTWINER_PASS"
            if passed
            else "STAGE_61_FAIL"
        ),
        "axis_count": len(axes),
        "P3_axis_permutation": list(permutation),
        "P3_cycle_notation": "(0 2 1)(3 5 4)",
        "P3_orthogonality_residual": p3_orthogonality_residual,
        "P3_order3_residual": p3_order3_residual,
        "P3_det1_residual": p3_det_residual,
        "pair_difference_identity_residual": pair_difference_identity_residual,
        "pair_difference_span_dimension": diff_rank,
        "pair_sum_span_dimension": sum_rank,
        "combined_span_dimension": combined_rank,
        "pair_sum_linear_relation_residual": sum_relation_residual,
        "Aseed_identity": "A_seed = sqrt(5)/4 * (Q1-Q4)",
        "Aseed_identity_residual": Aseed_residual,
        "D0_pair_sum_coefficients": {
            "alpha": alpha,
            "beta": beta,
            "gamma": gamma
        },
        "D0_coefficient_sum_residual": coefficient_sum_residual,
        "D0_reconstruction_residual": D_residual,
        "C3_orbit_Aseed_rank": A_orbit_rank,
        "C3_orbit_D0_rank": D_orbit_rank,
        "C3_orbit_union_rank": orbit_union_rank,
        "result": "The frozen C3 cycle, seed-incidence operator, and ordered polygonal axis admit an explicit parameter-free intertwiner with the N=5 six-axis quadrupole carrier: A_seed fills the 3D pair-difference sector and D0 fills the 2D pair-sum sector.",
        "embedding_uniqueness_established": False,
        "uses_observed_CKM": False,
        "uses_observed_masses": False,
        "uses_fitted_coefficients": False,
        "pass": passed
    }

    path = OUT / "TIR_POLYGONAL_STAGE61_C3_ICOSAHEDRAL_FAMILY_INTERTWINER_RECEIPT_V0_1.json"
    path.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    print(json.dumps(receipt, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
