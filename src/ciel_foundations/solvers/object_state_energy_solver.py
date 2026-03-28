"""Object-state energy normalization and topological seed phase mapping."""

from __future__ import annotations

import hashlib
import math
from typing import Sequence

import numpy as np


def raw_energy_linear(rho: float, p: float, w: float, nu: float, state_norm: float, chi_value: float, neighborhood_norm: float, alphas: Sequence[float] | None = None) -> float:
    vals = [rho, p, w, nu, state_norm, chi_value, neighborhood_norm]
    if any(float(v) < 0.0 for v in vals):
        raise ValueError("all raw-energy inputs must be nonnegative")
    if alphas is None:
        alphas = [1.0] * 7
    if len(alphas) != 7:
        raise ValueError("alphas must have length 7")
    return float(sum(float(a) * float(v) for a, v in zip(alphas, vals)))


def normalize_energies(raw_energies: Sequence[float]) -> np.ndarray:
    vals = np.array(raw_energies, dtype=float)
    if np.any(vals < 0.0):
        raise ValueError("raw energies must be nonnegative")
    total = float(vals.sum())
    if total <= 0.0:
        raise ValueError("total raw energy must be positive")
    return vals / total


def amplitudes_from_normalized_energy(norm_energies: Sequence[float]) -> np.ndarray:
    vals = np.array(norm_energies, dtype=float)
    if np.any(vals < 0.0):
        raise ValueError("normalized energies must be nonnegative")
    return np.sqrt(vals)


def phase_from_seed_text(seed_text: str) -> float:
    h = hashlib.sha256(seed_text.encode("utf-8")).hexdigest()
    x = int(h[:16], 16) / float(16**16)
    return 2.0 * math.pi * x


def local_states(amplitudes: Sequence[float], phases: Sequence[float]) -> np.ndarray:
    a = np.array(amplitudes, dtype=float)
    p = np.array(phases, dtype=float)
    if len(a) != len(p):
        raise ValueError("amplitudes and phases must have equal length")
    return a * np.exp(1j * p)
