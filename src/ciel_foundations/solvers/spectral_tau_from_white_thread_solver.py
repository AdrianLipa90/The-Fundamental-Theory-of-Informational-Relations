"""Spectral bridge from effective White-Thread amplitudes to tau modes."""

from __future__ import annotations

from typing import Sequence
import numpy as np


def hermitian_projection_entry(w_ij: complex, w_ji: complex | None = None) -> float:
    if w_ji is None:
        w_ji = complex(w_ij).conjugate()
    val = 0.5 * (complex(w_ij) + complex(w_ji).conjugate())
    return float(val.real)


def build_symmetric_coupling_matrix(a12: float, a13: float, a23: float) -> np.ndarray:
    return np.array([
        [0.0, float(a12), float(a13)],
        [float(a12), 0.0, float(a23)],
        [float(a13), float(a23), 0.0],
    ], dtype=float)


def spectral_tau_modes(matrix: Sequence[Sequence[float]]) -> np.ndarray:
    vals = np.linalg.eigvalsh(np.array(matrix, dtype=float))
    return vals[::-1]


def characteristic_coefficients_3x3_zero_diag(a12: float, a13: float, a23: float) -> tuple[float, float]:
    s2 = float(a12)**2 + float(a13)**2 + float(a23)**2
    s3 = 2.0 * float(a12) * float(a13) * float(a23)
    return s2, s3
