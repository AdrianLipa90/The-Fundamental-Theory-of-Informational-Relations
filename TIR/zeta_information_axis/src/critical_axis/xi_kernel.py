"""Canonical two-branch decomposition of the Riemann Xi Fourier kernel.

Analytic identity
-----------------
With Xi(z) = xi(1/2 + i z), the standard Riemann kernel can be written

    Phi(u) = sum_{n>=1} (4*pi^2*n^4*exp(9u/2)
                        - 6*pi*n^2*exp(5u/2))
                       * exp(-pi*n^2*exp(2u)),

and

    Xi(z) = 2 * integral_0^infinity Phi(u) cos(z u) du
          = A_+(z) + A_-(z),

where

    A_+(z) = integral_0^infinity Phi(u) exp(+i z u) du,
    A_-(z) = integral_0^infinity Phi(u) exp(-i z u) du.

Therefore every zero of Xi satisfies the exact algebraic cancellation
A_+(z) = -A_-(z).  On the real z axis, reality of Phi additionally gives
A_-(z) = conjugate(A_+(z)).

The runtime helpers below are numerical evaluators of these analytic objects.
They deliberately expose finite series/integration cutoffs and must not be
confused with a proof that all zeros have real z.  In particular, the branch
cancellation identity holds at hypothetical complex Xi zeros as well; the
remaining RH-level bridge is the identification of a branch-derived
population with the affine critical-strip coordinate Re(s).
"""

from __future__ import annotations

from dataclasses import dataclass

import mpmath as mp

from .core import completed_xi


@dataclass(frozen=True)
class XiKernelBranches:
    """Numerical realization of the two canonical exponential branches."""

    z: mp.mpc
    plus: mp.mpc
    minus: mp.mpc
    max_terms: int
    cutoff: mp.mpf

    @property
    def reconstructed_xi(self) -> mp.mpc:
        return self.plus + self.minus

    @property
    def cancellation_residual(self) -> mp.mpf:
        return abs(self.reconstructed_xi)

    @property
    def branch_norm(self) -> mp.mpf:
        return abs(self.plus) + abs(self.minus)

    def population_plus(self) -> mp.mpf:
        """Return |A_+|^2/(|A_+|^2+|A_-|^2) for a nondegenerate pair."""
        p2 = abs(self.plus) ** 2
        m2 = abs(self.minus) ** 2
        denom = p2 + m2
        if denom == 0:
            raise ZeroDivisionError("kernel branch population is undefined for two zero branches")
        return p2 / denom


def riemann_phi(u: float | mp.mpf, *, max_terms: int = 12) -> mp.mpf:
    """Evaluate a finite truncation of the standard Riemann Xi kernel Phi(u).

    The analytic kernel is the infinite series documented in the module
    docstring.  `max_terms` is a numerical truncation control only.
    """
    x = mp.mpf(u)
    nmax = int(max_terms)
    if x < 0:
        raise ValueError("riemann_phi runtime evaluator expects u >= 0")
    if nmax < 1:
        raise ValueError("max_terms must be positive")

    exp_2u = mp.exp(2 * x)
    exp_5u_over_2 = mp.exp(mp.mpf("2.5") * x)
    exp_9u_over_2 = mp.exp(mp.mpf("4.5") * x)
    total = mp.mpf("0")
    for n in range(1, nmax + 1):
        nn = mp.mpf(n)
        prefactor = (
            4 * mp.pi**2 * nn**4 * exp_9u_over_2
            - 6 * mp.pi * nn**2 * exp_5u_over_2
        )
        total += prefactor * mp.exp(-mp.pi * nn**2 * exp_2u)
    return total


def xi_kernel_branch(
    z: complex | mp.mpc,
    *,
    sign: int,
    max_terms: int = 12,
    cutoff: float | mp.mpf = 4,
) -> mp.mpc:
    """Numerically integrate A_+ (sign=+1) or A_- (sign=-1).

    The exact analytic definition integrates to infinity.  The finite cutoff
    is explicit and is used only for reproducible numerical validation.
    """
    if sign not in (-1, 1):
        raise ValueError("sign must be +1 or -1")
    umax = mp.mpf(cutoff)
    if umax <= 0:
        raise ValueError("cutoff must be positive")
    zz = mp.mpc(z)
    integrand = lambda u: riemann_phi(u, max_terms=max_terms) * mp.exp(sign * 1j * zz * u)
    knots = [mp.mpf("0"), mp.mpf("1"), mp.mpf("2")]
    if umax <= 1:
        knots = [mp.mpf("0"), umax]
    elif umax <= 2:
        knots = [mp.mpf("0"), mp.mpf("1"), umax]
    else:
        knots.append(umax)
    return mp.quad(integrand, knots)


def xi_kernel_branches(
    z: complex | mp.mpc,
    *,
    max_terms: int = 12,
    cutoff: float | mp.mpf = 4,
) -> XiKernelBranches:
    zz = mp.mpc(z)
    return XiKernelBranches(
        z=zz,
        plus=xi_kernel_branch(zz, sign=1, max_terms=max_terms, cutoff=cutoff),
        minus=xi_kernel_branch(zz, sign=-1, max_terms=max_terms, cutoff=cutoff),
        max_terms=int(max_terms),
        cutoff=mp.mpf(cutoff),
    )


def completed_xi_on_z_axis(z: complex | mp.mpc) -> mp.mpc:
    """Return Xi(z) := xi(1/2 + i z), allowing complex z."""
    zz = mp.mpc(z)
    return completed_xi(mp.mpf("0.5") + 1j * zz)


def zeta_s_to_xi_z(s: complex | mp.mpc) -> mp.mpc:
    """Map s to z through s = 1/2 + i z.

    For s=beta+i*gamma this gives z=gamma+i*(1/2-beta).  Thus RH is
    equivalent to the statement that every nontrivial zero maps to real z.
    """
    ss = mp.mpc(s)
    return -1j * (ss - mp.mpf("0.5"))


def kernel_reconstruction_residual(
    z: complex | mp.mpc,
    *,
    max_terms: int = 12,
    cutoff: float | mp.mpf = 4,
) -> mp.mpf:
    """Numerical |A_+ + A_- - Xi(z)| at explicit truncation settings."""
    branches = xi_kernel_branches(z, max_terms=max_terms, cutoff=cutoff)
    return abs(branches.reconstructed_xi - completed_xi_on_z_axis(z))
