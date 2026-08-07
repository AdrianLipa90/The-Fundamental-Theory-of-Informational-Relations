"""Core identities for the information-spinor critical-axis programme.

The module deliberately separates exact mathematics from model identifications.
No function in this file claims a proof of the Riemann hypothesis.

v0.2 adds the centred reciprocal chart, radial compactification, generic U(1)
holonomy helpers, an Aharonov--Bohm phase wrapper, and a dimensionless Hubble
radial normalization.  The latter two are kept separate from any claim that
they are the same physical field or potential.
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


def centered_coordinate(s: complex | mp.mpc) -> mp.mpc:
    """Translate the critical line Re(s)=1/2 to the imaginary axis."""
    return mp.mpc(s) - mp.mpf("0.5")


def centered_zeta_involution(u: complex | mp.mpc) -> mp.mpc:
    """Zeta anti-linear involution in u=s-1/2 coordinates: u -> -conj(u)."""
    return -mp.conj(mp.mpc(u))


def reciprocal_map(u: complex | mp.mpc) -> mp.mpc:
    """Reciprocal chart I(u)=1/u on the punctured plane.

    I is holomorphic and conformal wherever u != 0.  It exchanges the local
    neighbourhood of the centred point with the asymptotic region.
    """
    z = mp.mpc(u)
    if z == 0:
        raise ValueError("reciprocal_map is undefined at u=0")
    return 1 / z


def centered_inversion(s: complex | mp.mpc) -> mp.mpc:
    """Apply the reciprocal chart after centring at s=1/2."""
    return reciprocal_map(centered_coordinate(s))


def compactified_radius(u: complex | mp.mpc) -> mp.mpf:
    """Non-holomorphic radial compactification r -> r/(1+r) in [0,1)."""
    r = abs(mp.mpc(u))
    return r / (1 + r)


def radial_compactification(u: complex | mp.mpc) -> mp.mpc:
    """Map C radially into the open unit disk while preserving angle.

    C(u)=u/(1+|u|) sends u=0 to the disk centre and |u|->infinity to the
    unit-circle boundary.  Unlike 1/u, this map is intentionally non-conformal.
    """
    z = mp.mpc(u)
    return z / (1 + abs(z))


def strip_probability_coordinate(s: complex | mp.mpc) -> mp.mpf:
    """Affine endpoint-preserving strip coordinate p=Re(s).

    This implements the unique affine map from Re(s) in [0,1] to a binary
    probability p in [0,1] that maps the strip boundaries to 0 and 1.
    It does not assert that a zeta zero is physically a probability state.
    """
    sigma = mp.re(mp.mpc(s))
    if sigma < 0 or sigma > 1:
        raise ValueError("Re(s) must lie in the critical strip [0,1]")
    return mp.mpf(sigma)


def u1_holonomy(loop_phase: float | mp.mpf | mp.mpc) -> mp.mpc:
    """Holonomy exp(i*theta) for a dimensionless U(1) loop phase theta."""
    return mp.e ** (1j * mp.mpc(loop_phase))


def aharonov_bohm_holonomy(
    loop_integral: float | mp.mpf | mp.mpc,
    charge_over_hbar: float | mp.mpf | mp.mpc = 1,
) -> mp.mpc:
    """Aharonov--Bohm U(1) holonomy.

    `loop_integral` represents integral A_mu dx^mu in a chosen convention and
    `charge_over_hbar` supplies the conversion to a dimensionless phase.
    """
    theta = mp.mpc(charge_over_hbar) * mp.mpc(loop_integral)
    return u1_holonomy(theta)


def hubble_length(
    hubble_rate: float | mp.mpf,
    propagation_speed: float | mp.mpf = 1,
) -> mp.mpf:
    """Return the scale L_H = c/H for positive H and c.

    The default propagation_speed=1 is suitable for natural/unitless tests.
    No cosmological horizon claim is implied.
    """
    h = mp.mpf(hubble_rate)
    c = mp.mpf(propagation_speed)
    if h <= 0:
        raise ValueError("hubble_rate must be positive")
    if c <= 0:
        raise ValueError("propagation_speed must be positive")
    return c / h


def normalized_hubble_radius(
    length: float | mp.mpf,
    hubble_rate: float | mp.mpf,
    propagation_speed: float | mp.mpf = 1,
) -> mp.mpf:
    """Dimensionless radial coordinate H*L/c.

    It equals one at L=c/H.  Interpreting that scale as a boundary or
    potential-tension normalization is a model postulate, not an identity.
    """
    ell = mp.mpf(length)
    h = mp.mpf(hubble_rate)
    c = mp.mpf(propagation_speed)
    if ell < 0:
        raise ValueError("length must be non-negative")
    if h <= 0:
        raise ValueError("hubble_rate must be positive")
    if c <= 0:
        raise ValueError("propagation_speed must be positive")
    return h * ell / c


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
