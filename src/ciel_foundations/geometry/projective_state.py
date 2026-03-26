"""Minimal projective-state geometry for the CP1/Bloch foundations layer."""

from __future__ import annotations

import cmath
import math
from typing import Iterable, Sequence, Tuple

ComplexVec2 = Tuple[complex, complex]


def _as_vec2(state: Sequence[complex]) -> ComplexVec2:
    if len(state) != 2:
        raise ValueError("state must have length 2")
    return complex(state[0]), complex(state[1])


def norm_sq(state: Sequence[complex]) -> float:
    a, b = _as_vec2(state)
    return (a.conjugate() * a + b.conjugate() * b).real


def normalize_state(state: Sequence[complex]) -> ComplexVec2:
    a, b = _as_vec2(state)
    n2 = norm_sq((a, b))
    if n2 <= 0.0:
        raise ValueError("state must be nonzero")
    n = math.sqrt(n2)
    return a / n, b / n


def inner_product(psi: Sequence[complex], phi: Sequence[complex]) -> complex:
    a1, b1 = normalize_state(psi)
    a2, b2 = normalize_state(phi)
    return a1.conjugate() * a2 + b1.conjugate() * b2


def projective_overlap(psi: Sequence[complex], phi: Sequence[complex]) -> float:
    return abs(inner_product(psi, phi))


def fs_distance(psi: Sequence[complex], phi: Sequence[complex]) -> float:
    overlap = max(0.0, min(1.0, projective_overlap(psi, phi)))
    return math.acos(overlap)


def bloch_vector(state: Sequence[complex]) -> Tuple[float, float, float]:
    a, b = normalize_state(state)
    x = 2.0 * (a.conjugate() * b).real
    y = 2.0 * (a.conjugate() * b).imag
    z = (a.conjugate() * a - b.conjugate() * b).real
    return float(x), float(y), float(z)


def state_from_angles(theta: float, phi: float) -> ComplexVec2:
    return (
        math.cos(theta / 2.0),
        cmath.exp(1j * phi) * math.sin(theta / 2.0),
    )
