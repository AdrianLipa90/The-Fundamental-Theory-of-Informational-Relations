"""XF-6 transverse mass envelope for the correlated Xi-kernel surface.

Let

    M(a,b) = Phi(a+b) Phi(a-b),        a > |b|,

where Phi is the positive Riemann Xi kernel in the repository normalization.
For f = log Phi, strict log-concavity gives the conditional analytic chain

    f'' < 0
      => M(a,b) < M(a,0) for b != 0,
      => d_b log M(a,b) < 0 for b > 0.

If additionally -f'' >= lambda > 0 throughout [a-|b|, a+|b|], then

    M(a,b) <= M(a,0) exp(-lambda b^2).

Independently of the log-concavity premise, the XF-5 local curvature kernel
has an exact positive central corridor.  For x != 0,

    |b| <= min(a/2, pi/(8|x|))

implies cos(2xb) >= 1/sqrt(2), and therefore

    L(x,y;a,b)
      >= (a^2/sqrt(2)-b^2) cosh(2|y|a) > 0.

At x=0 the complete admissible b-domain is pointwise positive.

The calculus implications are theorem-level conditional statements.  The
current external claim that the Riemann Xi kernel is globally strictly
log-concave is tracked separately at the research-firewall level.  Runtime
derivatives below use the finite `riemann_phi` evaluator and therefore provide
numerical diagnostics.
"""

from __future__ import annotations

from dataclasses import dataclass

import mpmath as mp

from .nonlocal_curvature import theta_curvature_kernel
from .xi_kernel import riemann_phi


@dataclass(frozen=True)
class TransverseMassHessian:
    """Numerical Hessian data for log M in diagonal coordinates."""

    aa: mp.mpf
    ab: mp.mpf
    bb: mp.mpf
    eigen_plus: mp.mpf
    eigen_minus: mp.mpf


def _validate_diagonal_coordinates(
    a: float | mp.mpf,
    b: float | mp.mpf,
) -> tuple[mp.mpf, mp.mpf]:
    aa = mp.mpf(a)
    bb = mp.mpf(b)
    if aa <= 0:
        raise ValueError("a must be positive")
    if aa <= abs(bb):
        raise ValueError("diagonal coordinates require a > |b|")
    return aa, bb


def _positive_phi(u: mp.mpf, *, max_terms: int) -> mp.mpf:
    value = riemann_phi(u, max_terms=max_terms)
    if value <= 0:
        raise ValueError("finite Phi evaluator must be positive on the requested point")
    return value


def transverse_mass(
    a: float | mp.mpf,
    b: float | mp.mpf,
    *,
    max_terms: int = 12,
) -> mp.mpf:
    """Return the finite-evaluator mass M(a,b)=Phi(a+b)Phi(a-b)."""
    aa, bb = _validate_diagonal_coordinates(a, b)
    return _positive_phi(aa + bb, max_terms=max_terms) * _positive_phi(
        aa - bb, max_terms=max_terms
    )


def transverse_mass_ratio(
    a: float | mp.mpf,
    b: float | mp.mpf,
    *,
    max_terms: int = 12,
) -> mp.mpf:
    """Return M(a,b)/M(a,0), a scale-invariant concentration diagnostic."""
    aa, bb = _validate_diagonal_coordinates(a, b)
    center = transverse_mass(aa, mp.mpf("0"), max_terms=max_terms)
    return transverse_mass(aa, bb, max_terms=max_terms) / center


def log_phi_slope(
    u: float | mp.mpf,
    *,
    max_terms: int = 12,
) -> mp.mpf:
    """Numerically evaluate d/du log(Phi(u)) for the finite Phi evaluator."""
    uu = mp.mpf(u)
    if uu < 0:
        raise ValueError("u must be nonnegative")
    return mp.diff(lambda t: mp.log(_positive_phi(t, max_terms=max_terms)), uu)


def log_phi_curvature(
    u: float | mp.mpf,
    *,
    max_terms: int = 12,
) -> mp.mpf:
    """Numerically evaluate d^2/du^2 log(Phi(u))."""
    uu = mp.mpf(u)
    if uu < 0:
        raise ValueError("u must be nonnegative")
    return mp.diff(
        lambda t: mp.log(_positive_phi(t, max_terms=max_terms)),
        uu,
        2,
    )


def transverse_log_mass_slope_b(
    a: float | mp.mpf,
    b: float | mp.mpf,
    *,
    max_terms: int = 12,
) -> mp.mpf:
    """Return d_b log M = f'(a+b)-f'(a-b)."""
    aa, bb = _validate_diagonal_coordinates(a, b)
    return log_phi_slope(aa + bb, max_terms=max_terms) - log_phi_slope(
        aa - bb, max_terms=max_terms
    )


def transverse_log_gap(
    a: float | mp.mpf,
    b: float | mp.mpf,
    *,
    max_terms: int = 12,
) -> mp.mpf:
    """Return 2 log Phi(a)-log Phi(a+b)-log Phi(a-b).

    Under strict log-concavity this quantity is positive for b != 0 and
    equals -log(M(a,b)/M(a,0)).
    """
    aa, bb = _validate_diagonal_coordinates(a, b)
    center = mp.log(_positive_phi(aa, max_terms=max_terms))
    plus = mp.log(_positive_phi(aa + bb, max_terms=max_terms))
    minus = mp.log(_positive_phi(aa - bb, max_terms=max_terms))
    return 2 * center - plus - minus


def transverse_log_mass_hessian(
    a: float | mp.mpf,
    b: float | mp.mpf,
    *,
    max_terms: int = 12,
) -> TransverseMassHessian:
    """Return the Hessian of log M and its diagonal-coordinate eigenvalues.

    For f=log Phi,

        H = [[f''(a+b)+f''(a-b), f''(a+b)-f''(a-b)],
             [f''(a+b)-f''(a-b), f''(a+b)+f''(a-b)]],

    with eigenvalues 2 f''(a+b) and 2 f''(a-b).
    """
    aa, bb = _validate_diagonal_coordinates(a, b)
    cpp = log_phi_curvature(aa + bb, max_terms=max_terms)
    cmm = log_phi_curvature(aa - bb, max_terms=max_terms)
    diag = cpp + cmm
    cross = cpp - cmm
    return TransverseMassHessian(
        aa=diag,
        ab=cross,
        bb=diag,
        eigen_plus=2 * cpp,
        eigen_minus=2 * cmm,
    )


def gaussian_mass_envelope(
    a: float | mp.mpf,
    b: float | mp.mpf,
    curvature_floor: float | mp.mpf,
    *,
    max_terms: int = 12,
) -> mp.mpf:
    """Return M(a,0) exp(-lambda b^2) for a supplied lambda>0.

    The value is a rigorous upper envelope when the caller has independently
    established -d^2 log(Phi)/du^2 >= lambda throughout the full interval
    [a-|b|, a+|b|].  The function treats that lower-curvature certificate as
    an explicit premise.
    """
    aa, bb = _validate_diagonal_coordinates(a, b)
    lam = mp.mpf(curvature_floor)
    if lam <= 0:
        raise ValueError("curvature_floor must be positive")
    center = transverse_mass(aa, mp.mpf("0"), max_terms=max_terms)
    return center * mp.exp(-lam * bb**2)


def curvature_positive_corridor_radius(
    x: float | mp.mpf,
    a: float | mp.mpf,
) -> mp.mpf:
    """Return a conservative radius with exact pointwise L>0.

    At x=0 the full interior |b|<a is positive.  For x!=0 the returned radius
    is min(a/2, pi/(8|x|)).
    """
    xx = abs(mp.mpf(x))
    aa = mp.mpf(a)
    if aa <= 0:
        raise ValueError("a must be positive")
    if xx == 0:
        return aa
    return min(aa / 2, mp.pi / (8 * xx))


def theta_curvature_corridor_lower_bound(
    x: float | mp.mpf,
    y: float | mp.mpf,
    a: float | mp.mpf,
    b: float | mp.mpf,
) -> mp.mpf:
    """Return an exact positive lower bound inside the XF-6 central corridor."""
    xx = mp.mpf(x)
    yy = mp.mpf(y)
    aa, bb = _validate_diagonal_coordinates(a, b)
    radius = curvature_positive_corridor_radius(xx, aa)
    if abs(bb) > radius:
        raise ValueError("point lies outside the certified positive corridor")
    if xx == 0:
        return aa**2 * mp.cosh(2 * abs(yy) * aa)
    return (aa**2 / mp.sqrt(2) - bb**2) * mp.cosh(2 * abs(yy) * aa)


def theta_curvature_corridor_margin(
    x: float | mp.mpf,
    y: float | mp.mpf,
    a: float | mp.mpf,
    b: float | mp.mpf,
) -> mp.mpf:
    """Return L minus its exact XF-6 corridor lower bound."""
    lower = theta_curvature_corridor_lower_bound(x, y, a, b)
    actual = theta_curvature_kernel(x, y, a, b)
    return actual - lower
