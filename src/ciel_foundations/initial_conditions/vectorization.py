from __future__ import annotations

from dataclasses import dataclass
from math import acos, atan2, isclose
from typing import Iterable, Tuple

import numpy as np


@dataclass(frozen=True)
class VectorizationResult:
    bloch: tuple[float, float, float]
    theta: float
    phi: float
    norm: float
    pole_chart: bool



def normalize_state(psi: Iterable[complex]) -> np.ndarray:
    arr = np.asarray(list(psi), dtype=np.complex128)
    if arr.shape != (2,):
        raise ValueError("psi must have shape (2,)")
    norm = float(np.linalg.norm(arr))
    if isclose(norm, 0.0):
        raise ValueError("psi must be nonzero")
    return arr / norm



def projector(psi: Iterable[complex]) -> np.ndarray:
    v = normalize_state(psi)
    return np.outer(v, np.conjugate(v))



def bloch_vector(psi: Iterable[complex]) -> tuple[float, float, float]:
    v = normalize_state(psi)
    a, b = v[0], v[1]
    nx = float(2.0 * np.real(a * np.conjugate(b)))
    ny = float(2.0 * np.imag(a * np.conjugate(b)))
    nz = float(np.abs(a) ** 2 - np.abs(b) ** 2)
    return (nx, ny, nz)



def chart_angles_from_bloch(bloch: Tuple[float, float, float]) -> tuple[float, float, bool]:
    nx, ny, nz = bloch
    nz_clamped = max(-1.0, min(1.0, nz))
    theta = float(acos(nz_clamped))
    pole_chart = isclose(abs(nz_clamped), 1.0, rel_tol=0.0, abs_tol=1e-12)
    phi = 0.0 if pole_chart else float(atan2(ny, nx))
    return theta, phi, pole_chart



def vectorize_state(psi: Iterable[complex]) -> VectorizationResult:
    v = normalize_state(psi)
    bloch = bloch_vector(v)
    theta, phi, pole_chart = chart_angles_from_bloch(bloch)
    return VectorizationResult(
        bloch=bloch,
        theta=theta,
        phi=phi,
        norm=float(np.linalg.norm(np.asarray(bloch, dtype=float))),
        pole_chart=pole_chart,
    )
