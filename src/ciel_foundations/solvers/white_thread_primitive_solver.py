"""Minimal solver for the White-Thread U(1) holonomy primitive."""

from __future__ import annotations

import cmath
from typing import Sequence


def u1_holonomy_phase(segment_integrals: Sequence[float]) -> float:
    return float(sum(float(x) for x in segment_integrals))


def u1_holonomy(phase: float) -> complex:
    return cmath.exp(1j * float(phase))


def _inner_product(psi_i: Sequence[complex], psi_j: Sequence[complex]) -> complex:
    if len(psi_i) != len(psi_j):
        raise ValueError("state vectors must have equal length")
    return sum(complex(a).conjugate() * complex(b) for a, b in zip(psi_i, psi_j))


def white_thread_matrix_element(psi_i: Sequence[complex], psi_j: Sequence[complex], phase: float) -> complex:
    return _inner_product(psi_i, psi_j) * u1_holonomy(phase)
