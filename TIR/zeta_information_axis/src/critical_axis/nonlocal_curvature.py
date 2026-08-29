"""XF-5 nonlocal-curvature bridge for the Riemann Xi programme.

The module records two exact identities around the XF-4 scalar

    Q_Xi(x,y) = |Xi'(z)|^2 - Re(Xi(z) conjugate(Xi''(z))),
    z = x + i y.

First, for real x,y,

    d^2/dy^2 |Xi(x+i y)|^2 = 2 Q_Xi(x,y).

Second, writing the verified TIR Fourier normalization as

    Xi(z) = 2 integral_0^infinity Phi(u) cos(z u) du,

and using diagonal coordinates u=a+b, v=a-b, define

    K(x,y;a,b)
      = (a/2) cos(2 x b) sinh(2 y a)
        + (b/2) cos(2 x a) sinh(2 y b).

Then

    dK/dy
      = a^2 cos(2 x b) cosh(2 y a)
        + b^2 cos(2 x a) cosh(2 y b).

The global sign of the resulting curvature integral retains OPEN status.
Finite evaluations exposed here are numerical diagnostics.
"""

from __future__ import annotations

import mpmath as mp

from .correlation_kernel import xi_laguerre_quantity
from .xi_kernel import completed_xi_on_z_axis, riemann_phi


def xi_modulus_squared(x: float | mp.mpf, y: float | mp.mpf) -> mp.mpf:
    """Return |Xi(x+i y)|^2 for real coordinates x,y."""
    z = mp.mpc(mp.mpf(x), mp.mpf(y))
    return abs(completed_xi_on_z_axis(z)) ** 2


def xi_transverse_curvature(x: float | mp.mpf, y: float | mp.mpf) -> mp.mpf:
    r"""Return the exact transverse curvature d_y^2 |Xi(x+i y)|^2.

    Analytic differentiation gives

        d_y^2 |Xi|^2 = 2 (|Xi'|^2 - Re(Xi conjugate(Xi''))) = 2 Q_Xi.

    This identity is valid wherever Xi is entire, including y=0.
    """
    z = mp.mpc(mp.mpf(x), mp.mpf(y))
    return 2 * xi_laguerre_quantity(z)


def xi_transverse_curvature_direct(
    x: float | mp.mpf,
    y: float | mp.mpf,
) -> mp.mpf:
    """Differentiate |Xi(x+i y)|^2 directly as a regression diagnostic."""
    xx = mp.mpf(x)
    yy = mp.mpf(y)
    return mp.diff(lambda eta: xi_modulus_squared(xx, eta), yy, 2)


def _validate_diagonal_coordinates(a: mp.mpf, b: mp.mpf) -> None:
    if a <= 0 or abs(b) >= a:
        raise ValueError("theta-kernel coordinates require a > |b| with a > 0")


def theta_growth_kernel(
    x: float | mp.mpf,
    y: float | mp.mpf,
    a: float | mp.mpf,
    b: float | mp.mpf,
) -> mp.mpf:
    r"""Return the symmetrized first-y-derivative theta kernel K(x,y;a,b)."""
    xx, yy, aa, bb = map(mp.mpf, (x, y, a, b))
    _validate_diagonal_coordinates(aa, bb)
    return (
        (aa / 2) * mp.cos(2 * xx * bb) * mp.sinh(2 * yy * aa)
        + (bb / 2) * mp.cos(2 * xx * aa) * mp.sinh(2 * yy * bb)
    )


def theta_curvature_kernel(
    x: float | mp.mpf,
    y: float | mp.mpf,
    a: float | mp.mpf,
    b: float | mp.mpf,
) -> mp.mpf:
    r"""Return d_y K, the XF-5 local curvature kernel."""
    xx, yy, aa, bb = map(mp.mpf, (x, y, a, b))
    _validate_diagonal_coordinates(aa, bb)
    return (
        aa**2 * mp.cos(2 * xx * bb) * mp.cosh(2 * yy * aa)
        + bb**2 * mp.cos(2 * xx * aa) * mp.cosh(2 * yy * bb)
    )


def theta_curvature_integrand(
    x: float | mp.mpf,
    y: float | mp.mpf,
    a: float | mp.mpf,
    b: float | mp.mpf,
    *,
    max_terms: int = 12,
) -> mp.mpf:
    r"""Return Phi(a+b) Phi(a-b) d_y K at one diagonal-coordinate point.

    Under the TIR normalization, the theorem-level global identity is

        Q_Xi(x,y) = 4 integral integral M(a,b) d_y K da db,

    over a>|b|. This helper evaluates only the local integrand.
    """
    aa = mp.mpf(a)
    bb = mp.mpf(b)
    _validate_diagonal_coordinates(aa, bb)
    mass = riemann_phi(aa + bb, max_terms=max_terms) * riemann_phi(
        aa - bb, max_terms=max_terms
    )
    return mass * theta_curvature_kernel(x, y, aa, bb)
