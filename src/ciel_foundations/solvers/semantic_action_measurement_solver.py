"""Toy measurement operators for semantic action components."""

from __future__ import annotations

import math
from typing import Sequence


def semantic_length_discrete(step_lengths: Sequence[float], metric_weights: Sequence[float]) -> float:
    if len(step_lengths) != len(metric_weights):
        raise ValueError("step_lengths and metric_weights must have equal length")
    total = 0.0
    for dl, g in zip(step_lengths, metric_weights):
        dl = float(dl)
        g = float(g)
        if dl < 0.0 or g < 0.0:
            raise ValueError("lengths and metric weights must be nonnegative")
        total += math.sqrt(g) * dl
    return total


def phase_cost_discrete(phases: Sequence[float]) -> float:
    vals = [float(p) for p in phases]
    if len(vals) < 2:
        return 0.0
    return sum(1.0 - math.cos(vals[k + 1] - vals[k]) for k in range(len(vals) - 1))


def closure_defect_cost(phase_vectors: Sequence[Sequence[float]]) -> float:
    rows = [list(map(float, row)) for row in phase_vectors]
    if not rows:
        return 0.0
    total = 0.0
    for row in rows:
        z = sum(complex(math.cos(phi), math.sin(phi)) for phi in row)
        total += abs(z) ** 2
    return total / len(rows)


def truth_structural_cost(resonances: Sequence[float]) -> float:
    vals = [float(r) for r in resonances]
    if not vals:
        return 0.0
    if any(r < 0.0 or r > 1.0 for r in vals):
        raise ValueError("resonances must lie in [0,1]")
    return sum(1.0 - r for r in vals) / len(vals)


def truth_audit_cost(false_count: int, unmarked_count: int, omit_count: int, hall_count: int, smooth_count: int, total_facts: int) -> float:
    vals = [false_count, unmarked_count, omit_count, hall_count, smooth_count, total_facts]
    if any(v < 0 for v in vals):
        raise ValueError("audit counts must be nonnegative")
    if total_facts == 0:
        raise ValueError("total_facts must be positive")
    return float(false_count + unmarked_count + omit_count + hall_count + smooth_count) / float(total_facts)


def semantic_action_online(length_cost: float, phase_cost: float, rel_defect: float, truth_struct_cost: float, alpha: float = 1.0, beta: float = 1.0, kappa: float = 1.0, mu: float = 1.0) -> float:
    vals = [length_cost, phase_cost, rel_defect, truth_struct_cost, alpha, beta, kappa, mu]
    if any(v < 0.0 for v in vals):
        raise ValueError("costs and coefficients must be nonnegative")
    return alpha * length_cost + beta * phase_cost + kappa * rel_defect + mu * truth_struct_cost


def semantic_action_full(online_cost: float, truth_audit: float, nu: float = 1.0) -> float:
    vals = [online_cost, truth_audit, nu]
    if any(v < 0.0 for v in vals):
        raise ValueError("online_cost, truth_audit, and nu must be nonnegative")
    return online_cost + nu * truth_audit
