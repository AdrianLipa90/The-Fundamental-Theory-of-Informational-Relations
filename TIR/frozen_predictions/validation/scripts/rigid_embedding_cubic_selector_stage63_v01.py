#!/usr/bin/env python3
"""Stage 63 — rigid-embedding cubic selector no-go.

Tests whether the frozen Stage-61/62 operators A_seed and D0 reduce the
Stage-60 two-dimensional A5 cubic invariant space to a unique line.
No CKM/mass inputs or fitted coefficients are used.
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
TOL = 1e-12


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


def t_iso(X: np.ndarray, Y: np.ndarray, Z: np.ndarray) -> float:
    values = []
    for perm in itertools.permutations((X, Y, Z), 3):
        values.append(np.trace(perm[0] @ perm[1] @ perm[2]))
    return float(np.mean(values))


def t_a5(X: np.ndarray, Y: np.ndarray, Z: np.ndarray, quadrupoles: list[np.ndarray]) -> float:
    return float(
        sum(
            np.trace(X @ Q) * np.trace(Y @ Q) * np.trace(Z @ Q)
            for Q in quadrupoles
        )
    )


def main() -> None:
    axes = canonical_axes()
    quadrupoles = [np.outer(u, u) - np.eye(3) / 3.0 for u in axes]

    E12 = np.zeros((3, 3))
    E12[0, 1] = E12[1, 0] = 1.0
    A = 0.5 * E12

    D = np.diag([-1.0 / 3.0, 0.0, 1.0 / math.sqrt(5.0)])
    D0 = D - np.trace(D) / 3.0 * np.eye(3)

    probe = np.array(
        [
            [t_iso(D0, D0, D0), t_a5(D0, D0, D0, quadrupoles)],
            [t_iso(A, A, D0), t_a5(A, A, D0, quadrupoles)],
        ],
        dtype=float,
    )

    vanish_AAA = max(abs(t_iso(A, A, A)), abs(t_a5(A, A, A, quadrupoles)))
    vanish_ADD = max(abs(t_iso(A, D0, D0)), abs(t_a5(A, D0, D0, quadrupoles)))

    determinant = float(np.linalg.det(probe))
    determinant_exact_numeric = (100.0 * math.sqrt(5.0) + 259.0) / 182250.0
    determinant_residual = abs(determinant - determinant_exact_numeric)
    rank = int(np.linalg.matrix_rank(probe, TOL))

    expected = {
        "iso_DDD": math.sqrt(5.0) / 675.0 + 17.0 / 1215.0,
        "a5_DDD": 98.0 / 6075.0 + 28.0 * math.sqrt(5.0) / 3375.0,
        "iso_AAD": -math.sqrt(5.0) / 30.0 - 1.0 / 36.0,
        "a5_AAD": -math.sqrt(5.0) / 75.0 - 1.0 / 45.0,
    }
    probe_expected = np.array(
        [
            [expected["iso_DDD"], expected["a5_DDD"]],
            [expected["iso_AAD"], expected["a5_AAD"]],
        ]
    )
    exact_probe_residual = float(np.max(np.abs(probe - probe_expected)))

    passed = (
        len(axes) == 6
        and vanish_AAA < TOL
        and vanish_ADD < TOL
        and exact_probe_residual < TOL
        and determinant > 0.0
        and determinant_residual < TOL
        and rank == 2
    )

    receipt = {
        "schema": "TIR_POLYGONAL_STAGE63_RIGID_EMBEDDING_CUBIC_SELECTOR_RECEIPT_V0_1",
        "status": (
            "STAGE_63_RIGID_EMBEDDING_CUBIC_SELECTOR_NONUNIQUENESS_PASS"
            if passed
            else "STAGE_63_FAIL"
        ),
        "probe_matrix": probe.tolist(),
        "probe_matrix_rank": rank,
        "AAA_vanishing_residual": vanish_AAA,
        "ADD_vanishing_residual": vanish_ADD,
        "exact_probe_formula_residual": exact_probe_residual,
        "probe_determinant": determinant,
        "exact_probe_determinant": "(100*sqrt(5)+259)/182250",
        "probe_determinant_formula_residual": determinant_residual,
        "result": "The rigid frozen A_seed/D0 embedding distinguishes both independent A5 cubic invariant directions; geometry and embedding rigidity alone do not select a unique cubic family action.",
        "additional_scalar_dynamical_condition_required": True,
        "uses_observed_CKM": False,
        "uses_observed_masses": False,
        "uses_fitted_coefficients": False,
        "pass": passed,
    }

    path = OUT / "TIR_POLYGONAL_STAGE63_RIGID_EMBEDDING_CUBIC_SELECTOR_RECEIPT_V0_1.json"
    path.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    print(json.dumps(receipt, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
