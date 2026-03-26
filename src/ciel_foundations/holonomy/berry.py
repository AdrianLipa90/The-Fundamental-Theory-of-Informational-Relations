"""Minimal Berry-phase helpers for the CP1/Bloch foundations layer."""

from __future__ import annotations

import cmath
import math


def berry_connection_phi(theta: float, monopole_charge: float = 0.5) -> float:
    """Return the azimuthal Berry connection component in a simple gauge."""
    return monopole_charge * (1.0 - math.cos(theta))


def berry_phase_latitude(theta: float, delta_phi: float = 2.0 * math.pi, monopole_charge: float = 0.5) -> float:
    """Return the Berry phase accumulated along a latitude cycle."""
    return berry_connection_phi(theta, monopole_charge=monopole_charge) * delta_phi


def spinor_sign_from_phase(phase: float) -> complex:
    return cmath.exp(1j * phase)


def is_spin_half_cycle(phase: float, atol: float = 1e-9) -> bool:
    z = spinor_sign_from_phase(phase)
    return abs(z.real + 1.0) <= atol and abs(z.imag) <= atol
