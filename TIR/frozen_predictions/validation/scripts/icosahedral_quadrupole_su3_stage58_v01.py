#!/usr/bin/env python3
"""Stage 58 — explicit SU(3) generation from icosahedral quadrupoles.

Uses the six antipodal axes of the regular icosahedron. For each unit axis u,
define Q = u u^T - I/3. The audit verifies:
  * six unique antipodal axes,
  * Q-span dimension 5,
  * exact regular-simplex Gram target (2/3 diagonal, -2/15 off diagonal),
  * zero quadrupole sum,
  * pairwise commutator span dimension 3,
  * real Lie closure of {iQ_a} has dimension 8 = dim su(3).
No CKM, masses, fitted coefficients, or amplitude kernels are used.
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


def canonical_axis(u: np.ndarray) -> np.ndarray:
    u = u.copy()
    for value in u:
        if abs(value) > 1e-12:
            if value < 0:
                u = -u
            return u
    raise ValueError("zero axis")


def real_vector(X: np.ndarray) -> np.ndarray:
    return np.concatenate([X.real.ravel(), X.imag.ravel()])


def lie_closure_dimension(generators: list[np.ndarray]) -> tuple[int, float]:
    mats: list[np.ndarray] = []
    vecs: list[np.ndarray] = []

    def add(X: np.ndarray) -> bool:
        v = real_vector(X)
        if not vecs:
            mats.append(X)
            vecs.append(v)
            return True
        old_rank = np.linalg.matrix_rank(np.stack(vecs, axis=1), TOL)
        new_rank = np.linalg.matrix_rank(np.stack(vecs + [v], axis=1), TOL)
        if new_rank > old_rank:
            mats.append(X)
            vecs.append(v)
            return True
        return False

    for X in generators:
        add(X)

    changed = True
    while changed and len(mats) < 8:
        changed = False
        current = list(mats)
        for i in range(len(current)):
            for j in range(i + 1, len(current)):
                K = current[i] @ current[j] - current[j] @ current[i]
                if np.max(np.abs(K)) > 1e-12 and add(K):
                    changed = True
                    if len(mats) >= 8:
                        break
            if len(mats) >= 8:
                break

    residual = max(
        max(float(np.max(np.abs(M.conj().T + M))), float(abs(np.trace(M))))
        for M in mats
    )
    return len(mats), residual


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

    norm = float(np.linalg.norm(vertices[0]))
    axes: list[np.ndarray] = []
    for v in vertices:
        u = canonical_axis(v / norm)
        if not any(np.max(np.abs(u - a)) < 1e-12 for a in axes):
            axes.append(u)

    quadrupoles = [np.outer(u, u) - np.eye(3) / 3.0 for u in axes]

    gram = np.array(
        [[np.trace(Qa @ Qb) for Qb in quadrupoles] for Qa in quadrupoles],
        dtype=float,
    )
    target = np.full((6, 6), -2.0 / 15.0)
    np.fill_diagonal(target, 2.0 / 3.0)

    q_matrix = np.stack([Q.ravel() for Q in quadrupoles], axis=1)
    q_rank = int(np.linalg.matrix_rank(q_matrix, TOL))
    q_sum_residual = float(np.max(np.abs(sum(quadrupoles))))
    gram_residual = float(np.max(np.abs(gram - target)))
    gram_eigenvalues = np.linalg.eigvalsh(gram)

    commutators = [
        quadrupoles[i] @ quadrupoles[j] - quadrupoles[j] @ quadrupoles[i]
        for i in range(len(quadrupoles))
        for j in range(i + 1, len(quadrupoles))
    ]
    comm_matrix = np.stack([K.ravel() for K in commutators], axis=1)
    comm_rank = int(np.linalg.matrix_rank(comm_matrix, TOL))

    lie_dim, structure_residual = lie_closure_dimension([1j * Q for Q in quadrupoles])

    passed = (
        len(axes) == 6
        and q_rank == 5
        and comm_rank == 3
        and lie_dim == 8
        and gram_residual < 1e-12
        and q_sum_residual < 1e-12
        and structure_residual < 1e-12
    )

    receipt = {
        "schema": "TIR_POLYGONAL_STAGE58_ICOSAHEDRAL_QUADRUPOLE_SU3_RECEIPT_V0_1",
        "status": (
            "STAGE_58_ICOSAHEDRAL_QUADRUPOLE_SU3_GENERATION_PASS"
            if passed
            else "STAGE_58_FAIL"
        ),
        "icosahedron_vertex_count": len(vertices),
        "antipodal_axis_count": len(axes),
        "quadrupole_span_dimension": q_rank,
        "quadrupole_sum_max_residual": q_sum_residual,
        "gram_target_diagonal": 2.0 / 3.0,
        "gram_target_off_diagonal": -2.0 / 15.0,
        "gram_max_residual": gram_residual,
        "gram_eigenvalues": [float(x) for x in gram_eigenvalues],
        "commutator_span_dimension": comm_rank,
        "lie_closure_dimension": lie_dim,
        "skew_hermitian_traceless_residual": structure_residual,
        "result": "The six icosahedral quadrupoles form a regular 5-simplex spanning Sym^2_0(R^3); their commutators span so(3); iQ_a generate full su(3).",
        "uses_observed_CKM": False,
        "uses_observed_masses": False,
        "uses_fitted_coefficients": False,
        "uses_amplitude_kernel": False,
        "pass": passed,
    }

    path = OUT / "TIR_POLYGONAL_STAGE58_ICOSAHEDRAL_QUADRUPOLE_SU3_RECEIPT_V0_1.json"
    path.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    print(json.dumps(receipt, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
