"""Minimal closure-functional helpers for the CP1/Bloch foundations layer."""

from __future__ import annotations

import cmath
from typing import Iterable, Sequence


def closure_defect(phases: Sequence[float]) -> complex:
    total = 0j
    for phase in phases:
        total += cmath.exp(1j * phase)
    return total


def closure_magnitude(phases: Sequence[float]) -> float:
    return abs(closure_defect(phases)) ** 2
