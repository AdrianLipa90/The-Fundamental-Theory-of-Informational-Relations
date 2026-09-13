"""Translation-Gram diagnostics for the XF-8C Xi Loewner-flow programme.

Analytically, with the even Riemann Xi kernel Phi_e and

    f_y(u) = Phi_e(u) exp(-y u),

set

    C_y(t) = integral_R f_y(u+t) f_y(u) du.

Then C_y is an autocorrelation and every finite translation matrix

    G_y[j,k] = C_y(t_j-t_k)

is positive semidefinite.  Its y derivative has entries

    d_y G_y[j,k] = H_y(t_j-t_k),

where H_y=d_y C_y.  Global PSD of all derivative Gram matrices for
0<y<1/2 is RH-equivalent through XF-8A/XF-8C.

The evaluators below use finite Xi-kernel series and integration cutoffs and
therefore provide numerical diagnostics only; they do not prove the global
Loewner gate.
"""

from __future__ import annotations

from collections.abc import Sequence

import mpmath as mp

from .correlation_kernel import even_riemann_phi


def xi_tilted_autocorrelation(
    t: float | mp.mpf,
    y: float | mp.mpf,
    *,
    max_terms: int = 12,
    cutoff: float | mp.mpf = 4,
) -> mp.mpf:
    """Finite diagnostic for C_y(t) in the centered positive-a form."""
    tt = mp.mpf(t)
    yy = mp.mpf(y)
    radius = mp.mpf(cutoff)
    if int(max_terms) < 1:
        raise ValueError("max_terms must be positive")
    if radius <= 0:
        raise ValueError("cutoff must be positive")

    def g(a: mp.mpf) -> mp.mpf:
        return (
            even_riemann_phi(a + tt / 2, max_terms=max_terms)
            * even_riemann_phi(a - tt / 2, max_terms=max_terms)
        )

    anchors = [mp.mpf("0")]
    for point in ("0.5", "1", "2", "3"):
        p = mp.mpf(point)
        if p < radius:
            anchors.append(p)
    anchors.append(radius)
    return 2 * mp.quad(lambda a: g(a) * mp.cosh(2 * yy * a), anchors)


def xi_tilted_autocorrelation_derivative(
    t: float | mp.mpf,
    y: float | mp.mpf,
    *,
    max_terms: int = 12,
    cutoff: float | mp.mpf = 4,
) -> mp.mpf:
    """Finite diagnostic for H_y(t)=d_y C_y(t)."""
    tt = mp.mpf(t)
    yy = mp.mpf(y)
    radius = mp.mpf(cutoff)
    if int(max_terms) < 1:
        raise ValueError("max_terms must be positive")
    if radius <= 0:
        raise ValueError("cutoff must be positive")

    def g(a: mp.mpf) -> mp.mpf:
        return (
            even_riemann_phi(a + tt / 2, max_terms=max_terms)
            * even_riemann_phi(a - tt / 2, max_terms=max_terms)
        )

    anchors = [mp.mpf("0")]
    for point in ("0.5", "1", "2", "3"):
        p = mp.mpf(point)
        if p < radius:
            anchors.append(p)
    anchors.append(radius)
    return 4 * mp.quad(
        lambda a: a * g(a) * mp.sinh(2 * yy * a),
        anchors,
    )


def xi_translation_gram(
    translations: Sequence[float | mp.mpf],
    y: float | mp.mpf,
    *,
    derivative: bool = False,
    max_terms: int = 12,
    cutoff: float | mp.mpf = 4,
) -> mp.matrix:
    """Return a finite numerical C_y- or H_y-translation Gram matrix."""
    points = [mp.mpf(t) for t in translations]
    if not points:
        raise ValueError("at least one translation is required")
    evaluator = (
        xi_tilted_autocorrelation_derivative
        if derivative
        else xi_tilted_autocorrelation
    )
    return mp.matrix(
        [
            [
                evaluator(
                    tj - tk,
                    y,
                    max_terms=max_terms,
                    cutoff=cutoff,
                )
                for tk in points
            ]
            for tj in points
        ]
    )


def hermitian_min_eigenvalue(matrix: mp.matrix) -> mp.mpf:
    """Return the smallest eigenvalue of a finite real/Hermitian diagnostic."""
    if matrix.rows != matrix.cols or matrix.rows < 1:
        raise ValueError("matrix must be nonempty and square")
    eigenvalues, _ = mp.eigsy(matrix)
    return min(eigenvalues)
