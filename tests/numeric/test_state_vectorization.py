from __future__ import annotations

import math

import numpy as np

from src.ciel_foundations.initial_conditions.vectorization import (
    bloch_vector,
    normalize_state,
    projector,
    vectorize_state,
)


def test_normalize_state_returns_unit_norm() -> None:
    psi = np.array([2.0 + 0.0j, 0.0 + 0.0j])
    out = normalize_state(psi)
    assert math.isclose(float(np.linalg.norm(out)), 1.0, rel_tol=0.0, abs_tol=1e-12)



def test_projector_is_global_phase_invariant() -> None:
    psi = np.array([1.0 / np.sqrt(2.0), 1.0j / np.sqrt(2.0)], dtype=np.complex128)
    alpha = 0.731
    psi2 = np.exp(1j * alpha) * psi
    p1 = projector(psi)
    p2 = projector(psi2)
    assert np.allclose(p1, p2, atol=1e-12)



def test_bloch_vector_is_global_phase_invariant() -> None:
    psi = np.array([1.0 / np.sqrt(2.0), 1.0j / np.sqrt(2.0)], dtype=np.complex128)
    alpha = -1.123
    psi2 = np.exp(1j * alpha) * psi
    b1 = np.asarray(bloch_vector(psi), dtype=float)
    b2 = np.asarray(bloch_vector(psi2), dtype=float)
    assert np.allclose(b1, b2, atol=1e-12)



def test_bloch_norm_is_one_for_pure_state() -> None:
    psi = np.array([1.0 / np.sqrt(2.0), np.exp(1j * 0.3) / np.sqrt(2.0)], dtype=np.complex128)
    result = vectorize_state(psi)
    assert math.isclose(result.norm, 1.0, rel_tol=0.0, abs_tol=1e-12)



def test_chart_matches_north_pole_state() -> None:
    psi = np.array([1.0 + 0.0j, 0.0 + 0.0j], dtype=np.complex128)
    result = vectorize_state(psi)
    nx, ny, nz = result.bloch
    assert math.isclose(nx, 0.0, rel_tol=0.0, abs_tol=1e-12)
    assert math.isclose(ny, 0.0, rel_tol=0.0, abs_tol=1e-12)
    assert math.isclose(nz, 1.0, rel_tol=0.0, abs_tol=1e-12)
    assert math.isclose(result.theta, 0.0, rel_tol=0.0, abs_tol=1e-12)
    assert result.pole_chart is True
