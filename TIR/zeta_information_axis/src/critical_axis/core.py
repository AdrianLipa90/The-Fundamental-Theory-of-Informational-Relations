"""Core identities for the information-spinor critical-axis programme.

The module deliberately separates exact mathematics from model identifications.
No function in this file claims a proof of the Riemann hypothesis.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import mpmath as mp


@dataclass(frozen=True)
class CancellationResult:
    sigma: mp.mpf
    phase: mp.mpf
    amplitude: mp.mpc
    intensity: mp.mpf


def binary_entropy(sigma: float | mp.mpf) -> mp.mpf:
    """Binary Shannon entropy in nats.

    The continuous endpoint values are defined as zero.
    """
    p = mp.mpf(sigma)
    if p < 0 or p > 1:
        raise ValueError("sigma must lie in [0, 1]")
    if p == 0 or p == 1:
        return mp.mpf("0")
    return -p * mp.log(p) - (1 - p) * mp.log(1 - p)


def binary_entropy_prime(sigma: float | mp.mpf) -> mp.mpf:
    p = mp.mpf(sigma)
    if not 0 < p < 1:
        raise ValueError("sigma must lie in (0, 1)")
    return mp.log((1 - p) / p)


def binary_entropy_second(sigma: float | mp.mpf) -> mp.mpf:
    p = mp.mpf(sigma)
    if not 0 < p < 1:
        raise ValueError("sigma must lie in (0, 1)")
    return -(1 / p) - (1 / (1 - p))


def two_channel_amplitude(sigma: float | mp.mpf, phase: float | mp.mpf) -> mp.mpc:
    """Coherent sum of complementary probability amplitudes."""
    p = mp.mpf(sigma)
    phi = mp.mpf(phase)
    if p < 0 or p > 1:
        raise ValueError("sigma must lie in [0, 1]")
    return mp.sqrt(p) + mp.e ** (1j * phi) * mp.sqrt(1 - p)


def cancellation_result(sigma: float | mp.mpf, phase: float | mp.mpf) -> CancellationResult:
    amp = two_channel_amplitude(sigma, phase)
    return CancellationResult(
        sigma=mp.mpf(sigma),
        phase=mp.mpf(phase),
        amplitude=amp,
        intensity=abs(amp) ** 2,
    )


def berry_phase_latitude(sigma: float | mp.mpf) -> mp.mpf:
    """Berry phase for one azimuthal cycle of the qubit state used here.

    State convention:
        |psi> = sqrt(sigma)|0> + exp(i phi) sqrt(1-sigma)|1>.

    With gamma = i integral <psi|d psi>, one obtains gamma=-2*pi*(1-sigma).
    The physical holonomy exp(i gamma) is gauge invariant.
    """
    p = mp.mpf(sigma)
    if p < 0 or p > 1:
        raise ValueError("sigma must lie in [0, 1]")
    return -2 * mp.pi * (1 - p)


def berry_holonomy(sigma: float | mp.mpf) -> mp.mpc:
    return mp.e ** (1j * berry_phase_latitude(sigma))


def zeta_involution(s: complex | mp.mpc) -> mp.mpc:
    z = mp.mpc(s)
    return 1 - mp.conj(z)


def completed_xi(s: complex | mp.mpc) -> mp.mpc:
    """Riemann's completed xi function in the standard entire normalization."""
    z = mp.mpc(s)
    return mp.mpf("0.5") * z * (z - 1) * mp.power(mp.pi, -z / 2) * mp.gamma(z / 2) * mp.zeta(z)


def dirichlet_eta(s: complex | mp.mpc) -> mp.mpc:
    return mp.altzeta(mp.mpc(s))


def eta_prefactor(s: complex | mp.mpc) -> mp.mpc:
    z = mp.mpc(s)
    return 1 - mp.power(2, 1 - z)


def first_nontrivial_zeros(count: int = 10) -> list[mp.mpc]:
    if count < 1:
        raise ValueError("count must be positive")
    return [mp.zetazero(k) for k in range(1, count + 1)]


def symmetry_residuals(points: Iterable[complex | mp.mpc]) -> list[mp.mpf]:
    """Return |xi(s)-xi(1-s)| for supplied points."""
    out: list[mp.mpf] = []
    for point in points:
        z = mp.mpc(point)
        out.append(abs(completed_xi(z) - completed_xi(1 - z)))
    return out
