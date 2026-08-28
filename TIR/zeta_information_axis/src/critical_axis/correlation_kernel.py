"""Correlation-kernel diagnostics for the Riemann Xi programme.

This module implements numerical representatives of the n=2 correlation
kernel used by Dimitrov--Xu (arXiv:1606.05011) and the corresponding Jensen /
Laguerre quantity. Their theorem-level density criterion is external
mathematics; finite numerical evaluations here are diagnostics only and carry
no authority to promote the global L1-density or strict-positivity conditions.

XF-5 also exposes the classical complex Laguerre geometry: for a real entire
function f and z=x+iy,

    d^2/dy^2 |f(x+iy)|^2
      = 2 (|f'(z)|^2 - Re(f(z) conjugate(f''(z)))).

For the Riemann Xi function this identifies twice the XF-4 scalar with the
transverse curvature of |Xi|^2.
"""

from __future__ import annotations

import mpmath as mp

from .xi_kernel import completed_xi_on_z_axis, riemann_phi


def even_riemann_phi(t: float | mp.mpf, *, max_terms: int = 12) -> mp.mpf:
    """Numerical even realization of the standard Riemann Xi kernel."""
    return riemann_phi(abs(mp.mpf(t)), max_terms=max_terms)


def correlation_nu2(
    t: float | mp.mpf,
    *,
    max_terms: int = 12,
    cutoff: float | mp.mpf = 4,
) -> mp.mpf:
    r"""Evaluate the n=2 correlation kernel

        nu_2(t) = integral (t-2s)^2 Phi(t-s) Phi(s) ds.

    The analytic integral runs over R. `cutoff` is an explicit symmetric
    numerical truncation used only for reproducible diagnostics.
    """
    tt = mp.mpf(t)
    radius = mp.mpf(cutoff)
    if radius <= 0:
        raise ValueError("cutoff must be positive")
    if int(max_terms) < 1:
        raise ValueError("max_terms must be positive")

    def integrand(s: mp.mpf) -> mp.mpf:
        return (
            (tt - 2 * s) ** 2
            * even_riemann_phi(tt - s, max_terms=max_terms)
            * even_riemann_phi(s, max_terms=max_terms)
        )

    anchors = [-radius]
    for point in (-2, -1, 0, 1, 2):
        p = mp.mpf(point)
        if -radius < p < radius:
            anchors.append(p)
    anchors.append(radius)
    return mp.quad(integrand, anchors)


def phi_2_y(
    t: float | mp.mpf,
    y: float | mp.mpf,
    *,
    max_terms: int = 12,
    cutoff: float | mp.mpf = 4,
) -> mp.mpf:
    r"""Evaluate Phi_{2,y}(t)=cosh(t y) nu_2(t).

    The Dimitrov--Xu RH-equivalent density criterion uses 0 < |y| < 1/2.
    This evaluator enforces the open critical-strip interval and rejects y=0
    for that criterion-specific interface.
    """
    yy = mp.mpf(y)
    if yy == 0 or abs(yy) >= mp.mpf("0.5"):
        raise ValueError("density-criterion y must satisfy 0 < |y| < 1/2")
    tt = mp.mpf(t)
    return mp.cosh(tt * yy) * correlation_nu2(
        tt, max_terms=max_terms, cutoff=cutoff
    )


def xi_laguerre_quantity(z: complex | mp.mpc) -> mp.mpf:
    r"""Return |Xi'(z)|^2 - Re(Xi(z) conjugate(Xi''(z))).

    The complex Laguerre criterion identifies global nonnegativity of this
    quantity with Laguerre--Polya membership for Xi under the standard
    real-entire strip-class hypotheses. Numerical evaluation at finitely many
    z is a regression diagnostic only.
    """
    zz = mp.mpc(z)
    f = completed_xi_on_z_axis
    value = f(zz)
    first = mp.diff(f, zz, 1)
    second = mp.diff(f, zz, 2)
    return abs(first) ** 2 - mp.re(value * mp.conj(second))


def xi_wiener_laguerre_scalar(
    x: float | mp.mpf,
    y: float | mp.mpf,
) -> mp.mpf:
    r"""Evaluate the XF-4 scalar Q_Xi(x,y) on the open critical strip.

    For real x and 0 < |y| < 1/2,

        Q_Xi(x,y) = |Xi'(x+iy)|^2
                    - Re(Xi(x+iy) conjugate(Xi''(x+iy))).

    Dimitrov--Xu's Fourier--Wronskian identity together with Wiener's L1
    Tauberian theorem identifies the global condition Q_Xi(x,y)>0 for every
    real x and every admissible y with their translation-density criterion.
    This function evaluates a point only; global strict positivity remains a
    theorem-level proof obligation.
    """
    xx = mp.mpf(x)
    yy = mp.mpf(y)
    if yy == 0 or abs(yy) >= mp.mpf("0.5"):
        raise ValueError("XF-4 y must satisfy 0 < |y| < 1/2")
    return xi_laguerre_quantity(mp.mpc(xx, yy))


def xi_transverse_modulus_curvature(
    x: float | mp.mpf,
    y: float | mp.mpf,
) -> mp.mpf:
    r"""Return d^2/dy^2 |Xi(x+iy)|^2 via the complex Laguerre identity.

    For every real x,y,

        curvature_y |Xi(x+iy)|^2 = 2 Q_Xi(x,y).

    This is an analytic identity. Its pointwise numerical evaluation has only
    diagnostic authority; the universally quantified nonnegativity condition
    is the classical complex-Laguerre RH-equivalent criterion.
    """
    xx = mp.mpf(x)
    yy = mp.mpf(y)
    return 2 * xi_laguerre_quantity(mp.mpc(xx, yy))


def xi_wronskian2_real(x: float | mp.mpf) -> mp.mpf:
    r"""Return W_2(Xi;x)=Xi Xi''-(Xi')^2 on the real axis."""
    xx = mp.mpf(x)
    f = completed_xi_on_z_axis
    value = mp.re(f(xx))
    first = mp.re(mp.diff(f, xx, 1))
    second = mp.re(mp.diff(f, xx, 2))
    return value * second - first**2
