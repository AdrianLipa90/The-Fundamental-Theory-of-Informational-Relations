#!/usr/bin/env python3
"""Stage 66 — solve the frozen Stage-65 stationary selector and classify it.

Inputs are only the previously frozen A5 quadrupole carrier, ordered D0 axis,
and the Stage-60 cubic invariant definitions. A_seed is excluded from solving
eta and is used only after the solution as an independent eigendirection check.
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


def proj0(M: np.ndarray) -> np.ndarray:
    return 0.5 * (M + M.T) - np.trace(M) / 3.0 * np.eye(3)


def grad_iso(S: np.ndarray) -> np.ndarray:
    return 3.0 * proj0(S @ S)


def grad_a5(S: np.ndarray, quadrupoles: list[np.ndarray]) -> np.ndarray:
    return 3.0 * sum((np.trace(S @ Q) ** 2) * Q for Q in quadrupoles)


def hess_iso_action(S: np.ndarray, X: np.ndarray) -> np.ndarray:
    return 3.0 * proj0(S @ X + X @ S)


def hess_a5_action(S: np.ndarray, X: np.ndarray, quadrupoles: list[np.ndarray]) -> np.ndarray:
    return 6.0 * sum(
        np.trace(S @ Q) * np.trace(X @ Q) * Q
        for Q in quadrupoles
    )


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


def coordinates(M: np.ndarray, basis: list[np.ndarray]) -> np.ndarray:
    return np.array([np.trace(B @ M) for B in basis], dtype=float)


def main() -> None:
    axes = canonical_axes()
    quadrupoles = [np.outer(u, u) - np.eye(3) / 3.0 for u in axes]

    D = np.diag([-1.0 / 3.0, 0.0, 1.0 / math.sqrt(5.0)])
    D0 = D - np.trace(D) / 3.0 * np.eye(3)

    # Solve grad_iso(D0) + eta grad_A5(D0) = lambda D0.
    g0 = grad_iso(D0)
    g1 = grad_a5(D0, quadrupoles)
    linear = np.column_stack([np.diag(g1), -np.diag(D0)])
    rhs = -np.diag(g0)
    eta, lagrange_lambda = np.linalg.lstsq(linear, rhs, rcond=None)[0]

    eta_exact = -75.0 * (59.0 + 21.0 * math.sqrt(5.0)) / 638.0
    lambda_exact = -(8765.0 + 4758.0 * math.sqrt(5.0)) / 4785.0
    eta_formula_residual = abs(float(eta) - eta_exact)
    lambda_formula_residual = abs(float(lagrange_lambda) - lambda_exact)
    stationarity_residual = float(
        np.max(np.abs(g0 + eta * g1 - lagrange_lambda * D0))
    )

    basis = sym0_basis()
    basis_gram = np.array([[np.trace(A @ B) for B in basis] for A in basis])
    basis_residual = float(np.max(np.abs(basis_gram - np.eye(5))))

    H = np.zeros((5, 5), dtype=float)
    for i, X in enumerate(basis):
        Y = hess_iso_action(D0, X) + eta * hess_a5_action(D0, X, quadrupoles)
        for j, B in enumerate(basis):
            H[j, i] = np.trace(B @ Y)

    d = coordinates(D0, basis)
    d /= np.linalg.norm(d)
    _, _, vh = np.linalg.svd(d.reshape(1, -1))
    tangent = vh[1:].T

    constrained = tangent.T @ (H - lagrange_lambda * np.eye(5)) @ tangent
    constrained = 0.5 * (constrained + constrained.T)
    eigenvalues, eigenvectors_tangent = np.linalg.eigh(constrained)
    eigenvectors_full = tangent @ eigenvectors_tangent

    # Independently frozen C3 orbit of A_seed; used only after eta is solved.
    E12 = np.zeros((3, 3))
    E12[0, 1] = E12[1, 0] = 1.0
    Aseed = 0.5 * E12
    P3 = np.array(
        [
            [0.0, 0.0, 1.0],
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
        ]
    )
    A_orbit = [Aseed]
    for _ in range(2):
        A_orbit.append(P3 @ A_orbit[-1] @ P3.T)

    orbit_vectors = []
    for A in A_orbit:
        v = coordinates(A, basis)
        orbit_vectors.append(v / np.linalg.norm(v))
    orbit_vectors = np.stack(orbit_vectors, axis=0)
    alignment = np.abs(orbit_vectors @ eigenvectors_full)

    negative_indices = np.where(eigenvalues < -1e-9)[0]
    positive_indices = np.where(eigenvalues > 1e-9)[0]
    zero_indices = np.where(np.abs(eigenvalues) <= 1e-9)[0]

    neg_index = int(negative_indices[0]) if len(negative_indices) == 1 else -1
    negative_mode_orbit_overlaps = (
        alignment[:, neg_index].tolist() if neg_index >= 0 else []
    )
    negative_mode_best_orbit_index = (
        int(np.argmax(alignment[:, neg_index])) if neg_index >= 0 else -1
    )
    negative_mode_best_alignment = (
        float(np.max(alignment[:, neg_index])) if neg_index >= 0 else 0.0
    )

    # Exact tangent eigenvalue targets in the natural channel basis.
    exact_targets = sorted(
        [
            -(2075.0 + 771.0 * math.sqrt(5.0)) / 319.0,
            6.0 * (1415.0 + 628.0 * math.sqrt(5.0)) / 1595.0,
            (8765.0 + 4758.0 * math.sqrt(5.0)) / 1595.0,
            3.0 * (710.0 + 323.0 * math.sqrt(5.0)) / 319.0,
        ]
    )
    spectrum_formula_residual = float(
        np.max(np.abs(np.sort(eigenvalues) - np.array(exact_targets)))
    )

    passed = (
        len(axes) == 6
        and eta_formula_residual < TOL
        and lambda_formula_residual < TOL
        and stationarity_residual < TOL
        and basis_residual < TOL
        and len(negative_indices) == 1
        and len(positive_indices) == 3
        and len(zero_indices) == 0
        and spectrum_formula_residual < TOL
        and negative_mode_best_orbit_index == 1
        and abs(negative_mode_best_alignment - 1.0) < TOL
    )

    receipt = {
        "schema": "TIR_POLYGONAL_STAGE66_STATIONARY_SELECTOR_RECEIPT_V0_1",
        "status": (
            "STAGE_66_UNIQUE_STATIONARY_SELECTOR_PASS_WITH_SADDLE_CLASSIFICATION"
            if passed
            else "STAGE_66_FAIL"
        ),
        "eta": float(eta),
        "eta_exact": "-75*(59+21*sqrt(5))/638",
        "eta_formula_residual": eta_formula_residual,
        "lagrange_lambda": float(lagrange_lambda),
        "lagrange_lambda_exact": "-(8765+4758*sqrt(5))/4785",
        "lagrange_lambda_formula_residual": lambda_formula_residual,
        "stationarity_residual": stationarity_residual,
        "sym0_basis_orthonormality_residual": basis_residual,
        "constrained_hessian_eigenvalues": eigenvalues.tolist(),
        "constrained_hessian_signature": {
            "negative": int(len(negative_indices)),
            "zero": int(len(zero_indices)),
            "positive": int(len(positive_indices))
        },
        "constrained_hessian_classification": "SADDLE",
        "spectrum_exact_formula_residual": spectrum_formula_residual,
        "Aseed_C3_orbit_alignment_matrix_abs": alignment.tolist(),
        "negative_mode_best_Aseed_orbit_index": negative_mode_best_orbit_index,
        "negative_mode_best_Aseed_orbit_label": "P3 A_seed P3^T",
        "negative_mode_best_alignment": negative_mode_best_alignment,
        "Aseed_used_to_solve_eta": False,
        "uses_observed_CKM": False,
        "uses_observed_masses": False,
        "uses_fitted_coefficients": False,
        "pass": passed
    }

    path = OUT / "TIR_POLYGONAL_STAGE66_STATIONARY_SELECTOR_RECEIPT_V0_1.json"
    path.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    print(json.dumps(receipt, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
