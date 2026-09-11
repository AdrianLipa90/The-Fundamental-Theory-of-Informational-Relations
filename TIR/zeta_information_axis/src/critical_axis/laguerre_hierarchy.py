"""XF-7 Laguerre-hierarchy crosswalk for the Riemann Xi kernel.

Planat--Sole (arXiv:2608.19160, 2026) study

    s(t) = Phi(sqrt(t)),
    F(t) = s'(t)^2 - s(t) s''(t),                  t > 0,

and report strict concavity of log F on (0, infinity).  That source-level
result is tracked by the research firewall as an external preprint claim.

The identities implemented here are ordinary calculus and are independent of
that claim.  Writing r=sqrt(t),

    F(r^2)
      = [r(Phi'^2-Phi Phi'') + Phi Phi']/(4 r^3).

For

    A0(r) = -Phi'(r)/Phi(r),
    B0(r) = r A0'(r) - A0(r),

this becomes

    F(r^2) = Phi(r)^2 B0(r)/(4 r^3),

and

    d/dr [A0(r)/r] = B0(r)/r^2.

Consequently F>0 is exactly equivalent to B0>0 wherever Phi>0.  If A0>0 and
B0>0 on a radial interval, q(r)=A0(r)/r is positive and increasing.  For the
XF-6 transverse mass M(a,b)=Phi(a+b)Phi(a-b), 0<=b<a, this gives

    -d_b log M(a,b) >= 2 b q(a-b)

and, after integration,

    M(a,b) <= M(a,0) exp[-b^2 q(a-b)].

That final envelope is an exact conditional implication: callers must supply
(or independently establish) the A0>0 and B0>0 premises on the required
interval.  The runtime helpers below use the finite ``riemann_phi`` evaluator,
so their sampled signs are numerical validation rather than global proofs.
"""

from __future__ import annotations

from dataclasses import dataclass

import mpmath as mp

from .transverse_mass import transverse_mass
from .xi_kernel import riemann_phi


@dataclass(frozen=True)
class LaguerreCrosswalk:
    """Finite-evaluator values entering the exact XF-7 crosswalk."""

    r: mp.mpf
    phi: mp.mpf
    phi_prime: mp.mpf
    phi_second: mp.mpf
    first_laguerre: mp.mpf
    a0: mp.mpf
    b0: mp.mpf


def _positive_radius(r: float | mp.mpf) -> mp.mpf:
    rr = mp.mpf(r)
    if rr <= 0:
        raise ValueError("r must be positive")
    return rr


def _positive_time(t: float | mp.mpf) -> mp.mpf:
    tt = mp.mpf(t)
    if tt <= 0:
        raise ValueError("t must be positive")
    return tt


def _positive_phi(r: mp.mpf, *, max_terms: int) -> mp.mpf:
    value = riemann_phi(r, max_terms=max_terms)
    if value <= 0:
        raise ValueError("finite Phi evaluator must be positive at the requested radius")
    return value


def phi_derivatives(
    r: float | mp.mpf,
    *,
    max_terms: int = 12,
) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    """Return Phi, Phi', Phi'' for the finite Xi-kernel evaluator."""
    rr = _positive_radius(r)
    value = _positive_phi(rr, max_terms=max_terms)
    first = mp.diff(lambda u: riemann_phi(u, max_terms=max_terms), rr)
    second = mp.diff(lambda u: riemann_phi(u, max_terms=max_terms), rr, 2)
    return value, first, second


def planat_sole_s(
    t: float | mp.mpf,
    *,
    max_terms: int = 12,
) -> mp.mpf:
    """Return the finite-evaluator s(t)=Phi(sqrt(t)), t>0."""
    tt = _positive_time(t)
    return _positive_phi(mp.sqrt(tt), max_terms=max_terms)


def first_laguerre_direct(
    t: float | mp.mpf,
    *,
    max_terms: int = 12,
) -> mp.mpf:
    """Numerically evaluate F(t)=s'(t)^2-s(t)s''(t)."""
    tt = _positive_time(t)
    s = lambda u: planat_sole_s(u, max_terms=max_terms)
    value = s(tt)
    first = mp.diff(s, tt)
    second = mp.diff(s, tt, 2)
    return first**2 - value * second


def first_laguerre_phi_crosswalk(
    r: float | mp.mpf,
    *,
    max_terms: int = 12,
) -> mp.mpf:
    """Evaluate the exact Phi/Phi'/Phi'' expression for F(r^2)."""
    rr = _positive_radius(r)
    value, first, second = phi_derivatives(rr, max_terms=max_terms)
    numerator = rr * (first**2 - value * second) + value * first
    return numerator / (4 * rr**3)


def a0_log_slope(
    r: float | mp.mpf,
    *,
    max_terms: int = 12,
) -> mp.mpf:
    """Return A0(r)=-Phi'(r)/Phi(r) for the finite evaluator."""
    rr = _positive_radius(r)
    value, first, _ = phi_derivatives(rr, max_terms=max_terms)
    return -first / value


def b0_laguerre_curvature(
    r: float | mp.mpf,
    *,
    max_terms: int = 12,
) -> mp.mpf:
    """Return B0(r)=r A0'(r)-A0(r)."""
    rr = _positive_radius(r)
    a0 = a0_log_slope(rr, max_terms=max_terms)
    a0_prime = mp.diff(lambda u: a0_log_slope(u, max_terms=max_terms), rr)
    return rr * a0_prime - a0


def first_laguerre_b0_crosswalk(
    r: float | mp.mpf,
    *,
    max_terms: int = 12,
) -> mp.mpf:
    """Evaluate F(r^2)=Phi(r)^2 B0(r)/(4 r^3)."""
    rr = _positive_radius(r)
    value = _positive_phi(rr, max_terms=max_terms)
    b0 = b0_laguerre_curvature(rr, max_terms=max_terms)
    return value**2 * b0 / (4 * rr**3)


def radial_log_slope_ratio(
    r: float | mp.mpf,
    *,
    max_terms: int = 12,
) -> mp.mpf:
    """Return q(r)=A0(r)/r."""
    rr = _positive_radius(r)
    return a0_log_slope(rr, max_terms=max_terms) / rr


def radial_log_slope_ratio_derivative(
    r: float | mp.mpf,
    *,
    max_terms: int = 12,
) -> mp.mpf:
    """Return q'(r), exactly equal to B0(r)/r^2."""
    rr = _positive_radius(r)
    return mp.diff(lambda u: radial_log_slope_ratio(u, max_terms=max_terms), rr)


def b0_ratio_derivative_crosswalk(
    r: float | mp.mpf,
    *,
    max_terms: int = 12,
) -> mp.mpf:
    """Return B0(r)/r^2 for comparison with d(A0/r)/dr."""
    rr = _positive_radius(r)
    return b0_laguerre_curvature(rr, max_terms=max_terms) / rr**2


def second_level_log_curvature(
    t: float | mp.mpf,
    *,
    max_terms: int = 12,
) -> mp.mpf:
    """Numerically evaluate d^2/dt^2 log F(t) for F(t)>0.

    The global negative sign reported by Planat--Sole is an external preprint
    claim.  This helper is only a finite-evaluator diagnostic.
    """
    tt = _positive_time(t)

    def log_first_laguerre(u: mp.mpf) -> mp.mpf:
        value = first_laguerre_direct(u, max_terms=max_terms)
        if value <= 0:
            raise ValueError("finite first Laguerre evaluator must be positive")
        return mp.log(value)

    return mp.diff(log_first_laguerre, tt, 2)


def laguerre_crosswalk(
    r: float | mp.mpf,
    *,
    max_terms: int = 12,
) -> LaguerreCrosswalk:
    """Collect the finite-evaluator XF-7 crosswalk at one radius."""
    rr = _positive_radius(r)
    value, first, second = phi_derivatives(rr, max_terms=max_terms)
    a0 = -first / value
    a0_prime = mp.diff(lambda u: a0_log_slope(u, max_terms=max_terms), rr)
    b0 = rr * a0_prime - a0
    numerator = rr * (first**2 - value * second) + value * first
    return LaguerreCrosswalk(
        r=rr,
        phi=value,
        phi_prime=first,
        phi_second=second,
        first_laguerre=numerator / (4 * rr**3),
        a0=a0,
        b0=b0,
    )


def adaptive_transverse_mass_envelope(
    a: float | mp.mpf,
    b: float | mp.mpf,
    *,
    max_terms: int = 12,
) -> mp.mpf:
    """Return the XF-7 conditional adaptive Gaussian envelope.

    For 0<=|b|<a, if A0>0 and B0>0 throughout the required radial interval,
    q=A0/r is positive and increasing and the returned value satisfies

        M(a,b) <= M(a,0) exp[-b^2 q(a-|b|)].

    The function evaluates the right-hand side only; certification of those
    analytic premises remains external to this numerical helper.
    """
    aa = mp.mpf(a)
    bb = abs(mp.mpf(b))
    if aa <= 0:
        raise ValueError("a must be positive")
    if bb >= aa:
        raise ValueError("adaptive envelope requires |b| < a")
    inner = aa - bb
    q_inner = radial_log_slope_ratio(inner, max_terms=max_terms)
    if q_inner <= 0:
        raise ValueError("finite q=A0/r evaluator must be positive")
    center = transverse_mass(aa, mp.mpf("0"), max_terms=max_terms)
    return center * mp.exp(-(bb**2) * q_inner)
