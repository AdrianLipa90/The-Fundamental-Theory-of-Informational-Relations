"""Toy solver for a loose-thread bundle and effective White-Thread amplitude."""

from __future__ import annotations

from typing import Sequence, List


def normalize_weights(weights: Sequence[float]) -> List[float]:
    vals = [float(w) for w in weights]
    if not vals:
        raise ValueError("weights must be nonempty")
    if any(w < 0.0 for w in vals):
        raise ValueError("weights must be nonnegative")
    s = sum(vals)
    if s <= 0.0:
        raise ValueError("weights must have positive sum")
    return [w / s for w in vals]


def effective_white_thread(primitives: Sequence[complex], weights: Sequence[float]) -> complex:
    if len(primitives) != len(weights):
        raise ValueError("primitives and weights must have equal length")
    alpha = normalize_weights(weights)
    return sum(a * complex(w) for a, w in zip(alpha, primitives))
