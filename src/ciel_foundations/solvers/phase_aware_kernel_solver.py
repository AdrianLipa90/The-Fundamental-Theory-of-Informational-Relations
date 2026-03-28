"""Toy solver for phase-aware pairwise kernel composition."""

from __future__ import annotations

import math
from typing import Sequence


def phase_alignment_weight(delta_gamma: float, lam: float = 1.0) -> float:
    if lam < 0.0:
        raise ValueError("lambda must be nonnegative")
    return math.exp(-lam * (1.0 - math.cos(delta_gamma)))


def closure_weight(R_H: float, mu: float = 1.0) -> float:
    if mu < 0.0:
        raise ValueError("mu must be nonnegative")
    if R_H < 0.0:
        raise ValueError("R_H must be nonnegative")
    return math.exp(-mu * R_H)


def pairwise_kernel_from_holonomy(W_abs: float, gamma_i: float, gamma_j: float, R_H: float, lam: float = 1.0, mu: float = 1.0) -> float:
    if W_abs < 0.0:
        raise ValueError("|W_ij| must be nonnegative")
    return W_abs * phase_alignment_weight(gamma_i - gamma_j, lam=lam) * closure_weight(R_H, mu=mu)
