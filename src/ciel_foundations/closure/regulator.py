"""Active closure regulator for the minimal foundations layer."""

from __future__ import annotations

from typing import Sequence

from src.ciel_foundations.closure.euler import closure_defect, closure_magnitude


def accept_by_threshold(phases: Sequence[float], rho_c: float) -> bool:
    if rho_c < 0.0:
        raise ValueError("rho_c must be nonnegative")
    return closure_magnitude(phases) <= rho_c


def classify_phases(phases: Sequence[float], rho_c: float) -> str:
    return "accept" if accept_by_threshold(phases, rho_c) else "rollback"
