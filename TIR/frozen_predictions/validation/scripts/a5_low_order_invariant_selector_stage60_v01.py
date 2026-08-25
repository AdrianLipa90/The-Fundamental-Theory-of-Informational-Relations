#!/usr/bin/env python3
"""Stage 60 — low-order invariant multiplicity audit for the A5 five-dimensional carrier.

Computes symmetric-power invariant multiplicities from the spin-two eigenvalue
sets of the A5 conjugacy classes and verifies that the cubic invariant space has
dimension two. Also constructs two explicit independent invariant cubic tensors:
tr(S^3) and sum_a tr(S Q_a)^3.
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
MAX_DEGREE = 8


def symmetric_power_characters(eigenvalues: np.ndarray, max_degree: int) -> np.ndarray:
    coeff = np.zeros(max_degree + 1, dtype=complex)
    coeff[0] = 1.0
    for lam in eigenvalues:
        new = np.zeros_like(coeff)
        for n in range(max_degree + 1):
            if abs(coeff[n]) < 1e-18:
                continue
            for k in range(max_degree - n + 1):
                new[n + k] += coeff[n] * lam**k
        coeff = new
    return coeff


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


def sym0_basis() -> list[np.ndarray]:
    B: list[np.ndarray] = []
    B.append(np.diag([1.0, -1.0, 0.0]) / math.sqrt(2.0))
    B.append(np.diag([1.0, 1.0, -2.0]) / math.sqrt(6.0))

    M = np.zeros((3, 3))
    M[0, 1] = M[1, 0] = 1.0 / math.sqrt(2.0)
    B.append(M.copy())

    M = np.zeros((3, 3))
    M[0, 2] = M[2, 0] = 1.0 / math.sqrt(2.0)
    B.append(M.copy())

    M = np.zeros((3, 3))
    M[1, 2] = M[2, 1] = 1.0 / math.sqrt(2.0)
    B.append(M.copy())
    return B


def main() -> None:
    omega = np.exp(2j * math.pi / 3.0)
    zeta = np.exp(2j * math.pi / 5.0)

    classes = [
        (1, np.array([1, 1, 1, 1, 1], dtype=complex)),
        (15, np.array([1, 1, 1, -1, -1], dtype=complex)),
        (20, np.array([1, omega, omega, omega**2, omega**2], dtype=complex)),
        (24, np.array([1, zeta, zeta**2, zeta**3, zeta**4], dtype=complex)),
    ]

    chars = [(size, symmetric_power_characters(eigs, MAX_DEGREE)) for size, eigs in classes]
    multiplicities_float: list[complex] = []
    multiplicities: list[int] = []
    max_integer_residual = 0.0
    for degree in range(MAX_DEGREE + 1):
        value = sum(size * coeffs[degree] for size, coeffs in chars) / 60.0
        multiplicities_float.append(value)
        rounded = int(round(value.real))
        multiplicities.append(rounded)
        max_integer_residual = max(
            max_integer_residual,
            abs(value.real - rounded),
            abs(value.imag),
        )

    expected = [1, 0, 1, 2, 2, 4, 7, 7, 12]

    axes = canonical_axes()
    quadrupoles = [np.outer(u, u) - np.eye(3) / 3.0 for u in axes]
    basis = sym0_basis()

    # Check orthonormality of the Sym^2_0 basis.
    basis_gram = np.array([[np.trace(A @ B) for B in basis] for A in basis])
    basis_residual = float(np.max(np.abs(basis_gram - np.eye(5))))

    # Cubic tensor for tr(S^3), symmetrized over the coordinate indices.
    T_iso = np.zeros((5, 5, 5), dtype=float)
    for i, j, k in itertools.product(range(5), repeat=3):
        values = []
        for perm in set(itertools.permutations((i, j, k), 3)):
            values.append(np.trace(basis[perm[0]] @ basis[perm[1]] @ basis[perm[2]]))
        T_iso[i, j, k] = float(np.mean(values))

    # Cubic tensor for sum_a tr(S Q_a)^3.
    T_a5 = np.zeros((5, 5, 5), dtype=float)
    for Q in quadrupoles:
        v = np.array([np.trace(B @ Q) for B in basis], dtype=float)
        T_a5 += np.einsum("i,j,k->ijk", v, v, v)

    cubic_tensor_rank = int(
        np.linalg.matrix_rank(
            np.stack([T_iso.ravel(), T_a5.ravel()], axis=1),
            TOL,
        )
    )
    cubic_tensor_correlation = float(
        np.dot(T_iso.ravel(), T_a5.ravel())
        / (np.linalg.norm(T_iso) * np.linalg.norm(T_a5))
    )

    passed = (
        multiplicities == expected
        and max_integer_residual < 1e-12
        and basis_residual < 1e-12
        and cubic_tensor_rank == 2
    )

    receipt = {
        "schema": "TIR_POLYGONAL_STAGE60_A5_LOW_ORDER_INVARIANT_SELECTOR_RECEIPT_V0_1",
        "status": (
            "STAGE_60_A5_LOW_ORDER_SELECTOR_NONUNIQUENESS_PASS"
            if passed
            else "STAGE_60_FAIL"
        ),
        "molien_invariant_multiplicities_degree_0_to_8": multiplicities,
        "molien_max_integer_residual": max_integer_residual,
        "degree_1_invariant_dimension": multiplicities[1],
        "degree_2_invariant_dimension": multiplicities[2],
        "degree_3_invariant_dimension": multiplicities[3],
        "sym0_basis_orthonormality_residual": basis_residual,
        "explicit_cubic_tensor_rank": cubic_tensor_rank,
        "explicit_cubic_tensor_correlation": cubic_tensor_correlation,
        "explicit_cubic_invariants": [
            "tr(S^3)",
            "sum_a tr(S Q_a)^3",
        ],
        "result": "A5 has no invariant linear direction, one quadratic norm, and a two-dimensional cubic invariant space; A5 symmetry alone does not select a unique low-order anisotropic family functional.",
        "uses_observed_CKM": False,
        "uses_observed_masses": False,
        "uses_fitted_coefficients": False,
        "pass": passed,
    }

    path = OUT / "TIR_POLYGONAL_STAGE60_A5_LOW_ORDER_INVARIANT_SELECTOR_RECEIPT_V0_1.json"
    path.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    print(json.dumps(receipt, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
