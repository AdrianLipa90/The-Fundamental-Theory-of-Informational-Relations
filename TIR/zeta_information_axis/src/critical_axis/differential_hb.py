"""Differential Hermite--Biehler bridge for the Riemann Xi programme.

Let A(z)=Xi(z)=xi(1/2+i z), which is a real entire function.  Define

    E_D(z)      = A(z) + i A'(z),
    E_D^#(z)    = A(z) - i A'(z).

Then A=(E_D+E_D^#)/2 exactly.  The Hermite--Biehler margin satisfies

    |E_D|^2 - |E_D^#|^2
      = 4 Im(A conjugate(A'))
      = 2 d_y |A(x+i y)|^2
      = 4 integral_0^y Q_Xi(x,v) dv,

where Q_Xi is the XF-5 Laguerre scalar.  The identities are exact; global
strict positivity of the margin in the upper half-plane remains RH-level and
is not asserted by these numerical helpers.
"""

from __future__ import annotations

from dataclasses import dataclass

import mpmath as mp

from .correlation_kernel import xi_laguerre_quantity
from .xi_kernel import completed_xi_on_z_axis


@dataclass(frozen=True)
class DifferentialHBPair:
    z: mp.mpc
    xi: mp.mpc
    xi_prime: mp.mpc
    e: mp.mpc
    e_sharp: mp.mpc

    @property
    def margin(self) -> mp.mpf:
        return abs(self.e) ** 2 - abs(self.e_sharp) ** 2

    def theta(self) -> mp.mpc:
        """Return E_D^#/E_D where defined."""
        if self.e == 0:
            raise ZeroDivisionError("differential HB quotient is undefined where E_D vanishes")
        return self.e_sharp / self.e


def xi_differential_hb_pair(z: complex | mp.mpc) -> DifferentialHBPair:
    """Evaluate the canonical differential pair E_D=Xi+iXi'."""
    zz = mp.mpc(z)
    value = completed_xi_on_z_axis(zz)
    first = mp.diff(completed_xi_on_z_axis, zz, 1)
    return DifferentialHBPair(
        z=zz,
        xi=value,
        xi_prime=first,
        e=value + 1j * first,
        e_sharp=value - 1j * first,
    )


def xi_differential_hb_margin(z: complex | mp.mpc) -> mp.mpf:
    """Return |E_D|^2-|E_D^#|^2 at one point."""
    return xi_differential_hb_pair(z).margin


def xi_modulus_y_derivative(x: float | mp.mpf, y: float | mp.mpf) -> mp.mpf:
    """Return d_y |Xi(x+i y)|^2 via the analytic first derivative."""
    zz = mp.mpc(mp.mpf(x), mp.mpf(y))
    value = completed_xi_on_z_axis(zz)
    first = mp.diff(completed_xi_on_z_axis, zz, 1)
    return 2 * mp.im(value * mp.conj(first))


def xi_integrated_laguerre_margin(x: float | mp.mpf, y: float | mp.mpf) -> mp.mpf:
    """Numerically realize 4*integral_0^y Q_Xi(x,v) dv.

    This is an identity check / diagnostic only.  Finite numerical quadrature
    does not establish the globally quantified RH-equivalent sign condition.
    """
    xx = mp.mpf(x)
    yy = mp.mpf(y)
    if yy == 0:
        return mp.mpf("0")
    return 4 * mp.quad(lambda v: xi_laguerre_quantity(mp.mpc(xx, v)), [0, yy])
