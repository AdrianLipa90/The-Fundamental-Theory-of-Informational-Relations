#!/usr/bin/env python3
"""Stage 59 — A5 action on the six antipodal icosahedral axes.

Reconstructs the 60 orientation-preserving icosahedral rotations from the
standard vertex set, derives their permutations of the six antipodal axes,
checks the fixed-axis character, verifies the reduced character is the A5
five-dimensional irrep, and checks equivariance of e_a -> Q_a.
"""
from __future__ import annotations

import itertools
import json
import math
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results"
OUT.mkdir(parents=True, exist_ok=True)
TOL = 1e-10


def canonical_axis(u: np.ndarray) -> np.ndarray:
    u = u.copy()
    for value in u:
        if abs(value) > 1e-12:
            if value < 0:
                u = -u
            return u
    raise ValueError("zero axis")


def permutation_order(p: tuple[int, ...]) -> int:
    seen = [False] * len(p)
    order = 1
    for i in range(len(p)):
        if seen[i]:
            continue
        j = i
        length = 0
        while not seen[j]:
            seen[j] = True
            j = p[j]
            length += 1
        order = math.lcm(order, length)
    return order


def main() -> None:
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

    # Stable unique ordering.
    unique_vertices: list[np.ndarray] = []
    for v in vertices:
        if not any(np.max(np.abs(v - w)) < 1e-12 for w in unique_vertices):
            unique_vertices.append(v)
    vertices = unique_vertices

    # Pick the first linearly independent vertex triple as a reference frame.
    ref = None
    for inds in itertools.combinations(range(len(vertices)), 3):
        X = np.stack([vertices[i] for i in inds], axis=1)
        if abs(np.linalg.det(X)) > 1e-10:
            ref = inds
            break
    if ref is None:
        raise RuntimeError("no independent reference triple")

    X = np.stack([vertices[i] for i in ref], axis=1)
    gram_ref = X.T @ X

    rotations: list[np.ndarray] = []
    for inds in itertools.permutations(range(len(vertices)), 3):
        Y = np.stack([vertices[i] for i in inds], axis=1)
        if np.max(np.abs(Y.T @ Y - gram_ref)) > 1e-10:
            continue
        R = Y @ np.linalg.inv(X)
        if np.max(np.abs(R.T @ R - np.eye(3))) > 1e-10:
            continue
        if abs(np.linalg.det(R) - 1.0) > 1e-10:
            continue
        mapped = [(R @ v) for v in vertices]
        if not all(any(np.max(np.abs(w - v)) < 1e-9 for v in vertices) for w in mapped):
            continue
        if not any(np.max(np.abs(R - Q)) < 1e-9 for Q in rotations):
            rotations.append(R)

    norm = float(np.linalg.norm(vertices[0]))
    axes: list[np.ndarray] = []
    for v in vertices:
        u = canonical_axis(v / norm)
        if not any(np.max(np.abs(u - a)) < 1e-12 for a in axes):
            axes.append(u)

    quadrupoles = [np.outer(u, u) - np.eye(3) / 3.0 for u in axes]

    def axis_index(w: np.ndarray) -> int:
        for i, a in enumerate(axes):
            if np.max(np.abs(w - a)) < 1e-9 or np.max(np.abs(w + a)) < 1e-9:
                return i
        raise RuntimeError("axis image not found")

    permutations: list[tuple[int, ...]] = []
    equivariance_residual = 0.0
    stats: dict[tuple[int, int], int] = {}

    for R in rotations:
        p = tuple(axis_index(R @ a) for a in axes)
        permutations.append(p)
        order = permutation_order(p)
        fixed = sum(i == p[i] for i in range(len(p)))
        stats[(order, fixed)] = stats.get((order, fixed), 0) + 1

        for a, image in enumerate(p):
            residual = float(np.max(np.abs(R @ quadrupoles[a] @ R.T - quadrupoles[image])))
            equivariance_residual = max(equivariance_residual, residual)

    unique_permutations = set(permutations)

    expected_stats = {
        (1, 6): 1,
        (2, 2): 15,
        (3, 0): 20,
        (5, 1): 24,
    }

    # Reduced character chi_5 = chi_perm - 1, grouped by element order.
    reduced_character = {1: 5, 2: 1, 3: -1, 5: 0}
    character_norm = (
        1 * reduced_character[1] ** 2
        + 15 * reduced_character[2] ** 2
        + 20 * reduced_character[3] ** 2
        + 24 * reduced_character[5] ** 2
    ) / 60.0

    q_matrix = np.stack([Q.ravel() for Q in quadrupoles], axis=1)
    q_rank = int(np.linalg.matrix_rank(q_matrix, TOL))
    kernel_dimension = 6 - q_rank
    sum_residual = float(np.max(np.abs(sum(quadrupoles))))

    passed = (
        len(rotations) == 60
        and len(unique_permutations) == 60
        and len(axes) == 6
        and stats == expected_stats
        and abs(character_norm - 1.0) < 1e-12
        and q_rank == 5
        and kernel_dimension == 1
        and sum_residual < 1e-12
        and equivariance_residual < 1e-12
    )

    receipt = {
        "schema": "TIR_POLYGONAL_STAGE59_A5_SIX_AXIS_REDUCED_PERMUTATION_RECEIPT_V0_1",
        "status": (
            "STAGE_59_A5_SIX_AXIS_REDUCED_PERMUTATION_FIVE_PASS"
            if passed
            else "STAGE_59_FAIL"
        ),
        "icosahedral_rotation_count": len(rotations),
        "axis_count": len(axes),
        "faithful_axis_permutation_image_size": len(unique_permutations),
        "fixed_axis_statistics": {
            f"order_{order}_fixed_{fixed}": count
            for (order, fixed), count in sorted(stats.items())
        },
        "permutation_character_A5_classes": [6, 2, 0, 1, 1],
        "reduced_character_A5_classes": [5, 1, -1, 0, 0],
        "reduced_character_norm": character_norm,
        "quadrupole_map_rank": q_rank,
        "quadrupole_map_kernel_dimension": kernel_dimension,
        "quadrupole_sum_residual": sum_residual,
        "equivariance_max_residual": equivariance_residual,
        "result": "The six-axis permutation carrier decomposes as 1 + 5, and the reduced 5 is A5-equivariantly isomorphic to the quadrupole Sym^2_0(R^3) carrier.",
        "stage6_six_state_action_identified_with_stage59": False,
        "uses_observed_CKM": False,
        "uses_observed_masses": False,
        "uses_fitted_coefficients": False,
        "pass": passed,
    }

    path = OUT / "TIR_POLYGONAL_STAGE59_A5_SIX_AXIS_REDUCED_PERMUTATION_RECEIPT_V0_1.json"
    path.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    print(json.dumps(receipt, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
