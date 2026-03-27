"""Toy solver for dynamic path weights from semantic action."""

from __future__ import annotations

import math
from typing import Sequence, List


def path_action(length: float, delta_phi: float, d_rel: float, truth_penalty: float, alpha: float = 1.0, beta: float = 1.0, kappa: float = 1.0, mu: float = 1.0) -> float:
    vals = [length, delta_phi, d_rel, truth_penalty, alpha, beta, kappa, mu]
    if any(v < 0.0 for v in vals):
        raise ValueError("path action inputs and coefficients must be nonnegative")
    return alpha * length + beta * delta_phi + kappa * d_rel + mu * truth_penalty


def softmax_weights(actions: Sequence[float], sigma: float = 1.0) -> List[float]:
    acts = [float(a) for a in actions]
    if not acts:
        raise ValueError("actions must be nonempty")
    if sigma < 0.0:
        raise ValueError("sigma must be nonnegative")
    vals = [math.exp(-sigma * a) for a in acts]
    z = sum(vals)
    return [v / z for v in vals]


def effective_white_thread_from_actions(primitives: Sequence[complex], actions: Sequence[float], sigma: float = 1.0) -> complex:
    if len(primitives) != len(actions):
        raise ValueError("primitives and actions must have equal length")
    alpha = softmax_weights(actions, sigma=sigma)
    return sum(a * complex(w) for a, w in zip(alpha, primitives))
