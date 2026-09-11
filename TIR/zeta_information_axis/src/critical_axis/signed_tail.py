"""XF-7 signed oscillatory-tail bounds for the correlated Xi-kernel mass.

For fixed a>0 let

    M_a(b) = Phi(a+b) Phi(a-b),       0 <= b <= a.

Whenever M_a is nonincreasing on [r,a] and x != 0, one integration by parts
preserves the oscillatory cancellation and gives the exact conditional bound

    | integral_r^a M_a(b) cos(2 x b) db | <= M_a(r)/|x|.

Indeed the boundary contribution is bounded by [M_a(a)+M_a(r)]/(2|x|),
while the total variation term is [M_a(r)-M_a(a)]/(2|x|).

XF-7 can combine this with the adaptive Laguerre-hierarchy envelope

    M_a(r) <= M_a(0) exp[-r^2 A0(a-r)/(a-r)]

when A0>0 and B0>0 on the required radial interval.  The result retains a
1/|x| gain from phase cancellation instead of replacing the cosine by its
absolute value before integration.

All returned bounds are theorem-level conditional expressions.  Numerical
integrals use the finite ``riemann_phi`` evaluator only as diagnostics.
"""

from __future__ import annotations

import mpmath as mp

from .laguerre_hierarchy import adaptive_transverse_mass_envelope
from .transverse_mass import transverse_mass
from .xi_kernel import riemann_phi


def _validate_tail_coordinates(
    a: float | mp.mpf,
    r: float | mp.mpf,
    x: float | mp.mpf,
) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
    aa = mp.mpf(a)
    rr = mp.mpf(r)
    xx = mp.mpf(x)
    if aa <= 0:
        raise ValueError("a must be positive")
    if rr < 0 or rr >= aa:
        raise ValueError("tail radius must satisfy 0 <= r < a")
    if xx == 0:
        raise ValueError("signed oscillatory-tail bound requires x != 0")
    return aa, rr, xx


def oscillatory_tail_ibp_bound(
    a: float | mp.mpf,
    r: float | mp.mpf,
    x: float | mp.mpf,
    *,
    max_terms: int = 12,
) -> mp.mpf:
    """Return M(a,r)/|x|, valid when b->M(a,b) is nonincreasing on [r,a]."""
    aa, rr, xx = _validate_tail_coordinates(a, r, x)
    return transverse_mass(aa, rr, max_terms=max_terms) / abs(xx)


def adaptive_oscillatory_tail_bound(
    a: float | mp.mpf,
    r: float | mp.mpf,
    x: float | mp.mpf,
    *,
    max_terms: int = 12,
) -> mp.mpf:
    """Return the XF-7 adaptive upper bound for the signed cosine tail.

    Analytic validity requires the monotone-mass premise plus the XF-7
    A0>0/B0>0 premises used by ``adaptive_transverse_mass_envelope``.
    """
    aa, rr, xx = _validate_tail_coordinates(a, r, x)
    return adaptive_transverse_mass_envelope(
        aa, rr, max_terms=max_terms
    ) / abs(xx)


def longitudinal_curvature_tail_bound(
    x: float | mp.mpf,
    y: float | mp.mpf,
    a: float | mp.mpf,
    r: float | mp.mpf,
    *,
    adaptive: bool = True,
    max_terms: int = 12,
) -> mp.mpf:
    """Bound the signed b-tail of the a^2 cos(2xb) cosh(2ya) sector."""
    aa, rr, xx = _validate_tail_coordinates(a, r, x)
    yy = mp.mpf(y)
    if adaptive:
        base = adaptive_oscillatory_tail_bound(
            aa, rr, xx, max_terms=max_terms
        )
    else:
        base = oscillatory_tail_ibp_bound(
            aa, rr, xx, max_terms=max_terms
        )
    return aa**2 * mp.cosh(2 * abs(yy) * aa) * base


def oscillatory_tail_integral_diagnostic(
    a: float | mp.mpf,
    r: float | mp.mpf,
    x: float | mp.mpf,
    *,
    max_terms: int = 12,
) -> mp.mpf:
    """Numerically integrate the finite-evaluator cosine tail.

    This helper is a validation diagnostic.  It evaluates M directly so that
    the endpoint b=a, where Phi(a-b)=Phi(0), is included continuously.
    """
    aa, rr, xx = _validate_tail_coordinates(a, r, x)

    def integrand(b: mp.mpf) -> mp.mpf:
        mass = riemann_phi(aa + b, max_terms=max_terms) * riemann_phi(
            aa - b, max_terms=max_terms
        )
        return mass * mp.cos(2 * xx * b)

    return mp.quad(integrand, [rr, aa])
