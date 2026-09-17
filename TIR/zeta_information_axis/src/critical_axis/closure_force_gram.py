"""XF-9 closure-defect radial force and regularized Gram-kernel bridge.

Coordinates
-----------
Xi(z) = xi(1/2 + i z), z = x + i y.

For y>=0, functional-equation and reality symmetry give

    |Xi(x+i y)|^2 = |xi(1/2 + y + i x)|^2.

Thus r=y^2 is the same squared transverse displacement used by the
secret-of-a-half closure defect.

This module implements exact identities only. Finite mpmath evaluations are
regression diagnostics and do not promote the Riemann hypothesis.
"""

from __future__ import annotations

import mpmath as mp

from .core import completed_xi
from .correlation_kernel import xi_laguerre_quantity
from .xi_kernel import completed_xi_on_z_axis


def _nonnegative_radius(r: float | mp.mpf) -> mp.mpf:
    rr = mp.mpf(r)
    if rr < 0:
        raise ValueError("closure radius r must be non-negative")
    return rr


def closure_potential(
    x: float | mp.mpf,
    r: float | mp.mpf,
) -> mp.mpf:
    """Return V_x(r)=|Xi(x+i*sqrt(r))|^2."""
    xx = mp.mpf(x)
    rr = _nonnegative_radius(r)
    y = mp.sqrt(rr)
    return abs(completed_xi_on_z_axis(mp.mpc(xx, y))) ** 2


def closure_radial_force(
    x: float | mp.mpf,
    r: float | mp.mpf,
) -> mp.mpf:
    r"""Return d_r V_x(r).

    For r>0 and z=x+i*y, y=sqrt(r),

        d_r |Xi(z)|^2 = Im(Xi(z) conjugate(Xi'(z))) / y.

    The r=0 limit is the first Laguerre quantity

        |Xi'(x)|^2 - Xi(x) Xi''(x).
    """
    xx = mp.mpf(x)
    rr = _nonnegative_radius(r)
    if rr == 0:
        return xi_laguerre_quantity(mp.mpc(xx, 0))
    y = mp.sqrt(rr)
    z = mp.mpc(xx, y)
    f = completed_xi_on_z_axis
    value = f(z)
    first = mp.diff(f, z, 1)
    return mp.im(value * mp.conj(first)) / y


def closure_radial_force_direct(
    x: float | mp.mpf,
    r: float | mp.mpf,
) -> mp.mpf:
    """Differentiate the closure potential directly; regression helper."""
    xx = mp.mpf(x)
    rr = _nonnegative_radius(r)
    return mp.diff(lambda q: closure_potential(xx, q), rr)


def normalized_closure_force(
    x: float | mp.mpf,
    r: float | mp.mpf,
) -> mp.mpf:
    """Return d_r log V where V is non-zero."""
    value = closure_potential(x, r)
    if value == 0:
        raise ZeroDivisionError("normalized force is undefined at an Xi zero")
    return closure_radial_force(x, r) / value


def lagarias_normalized_force(
    t: float | mp.mpf,
    r: float | mp.mpf,
) -> mp.mpf:
    r"""Return Re[(xi'/xi)(1/2+sqrt(r)+it)]/sqrt(r), r>0.

    By xi functional-equation/reality symmetry this equals the normalized
    closure force evaluated in the Xi coordinate, away from zeros.
    """
    tt = mp.mpf(t)
    rr = _nonnegative_radius(r)
    if rr == 0:
        raise ValueError("Lagarias normalized force requires r>0")
    y = mp.sqrt(rr)
    s = mp.mpc(mp.mpf("0.5") + y, tt)
    value = completed_xi(s)
    if value == 0:
        raise ZeroDivisionError("xi'/xi is undefined at a zero")
    first = mp.diff(completed_xi, s, 1)
    return mp.re(first / value) / y


def differential_branches(
    z: complex | mp.mpc,
) -> tuple[mp.mpc, mp.mpc]:
    """Return E_D=Xi+iXi' and E_D#=Xi-iXi'."""
    zz = mp.mpc(z)
    f = completed_xi_on_z_axis
    value = f(zz)
    first = mp.diff(f, zz, 1)
    return value + 1j * first, value - 1j * first


def differential_margin(
    z: complex | mp.mpc,
) -> mp.mpf:
    """Return |E_D|^2-|E_D#|^2."""
    e, esharp = differential_branches(z)
    return abs(e) ** 2 - abs(esharp) ** 2


def regularized_pick_kernel(
    z: complex | mp.mpc,
    w: complex | mp.mpc,
) -> mp.mpc:
    r"""Return the pole-free Xi Pick/Gram kernel off the removable diagonal.

        Khat(z,w) =
          [Xi(z) conj(Xi'(w)) - Xi'(z) conj(Xi(w))]
          / [z-conj(w)].
    """
    zz = mp.mpc(z)
    ww = mp.mpc(w)
    denom = zz - mp.conj(ww)
    if denom == 0:
        raise ZeroDivisionError(
            "use regularized_pick_kernel_diagonal on the removable diagonal"
        )
    f = completed_xi_on_z_axis
    fz = f(zz)
    fw = f(ww)
    fpz = mp.diff(f, zz, 1)
    fpw = mp.diff(f, ww, 1)
    return (fz * mp.conj(fpw) - fpz * mp.conj(fw)) / denom


def regularized_pick_kernel_diagonal(
    x: float | mp.mpf,
    y: float | mp.mpf,
) -> mp.mpf:
    """Return Khat(z,z)=d_r |Xi(x+i sqrt(r))|^2 with r=y^2."""
    yy = mp.mpf(y)
    if yy == 0:
        return closure_radial_force(x, mp.mpf("0"))
    return closure_radial_force(x, yy * yy)


def debranges_kernel(
    z: complex | mp.mpc,
    w: complex | mp.mpc,
) -> mp.mpc:
    r"""Return the standard de Branges kernel for E_D off the diagonal.

    Convention:

        K_E(z,w) =
        [E(z)conj(E(w))-E#(z)conj(E#(w))]
        / [2*pi*i*(conj(w)-z)].

    With E_D=Xi+iXi', exact algebra gives

        regularized_pick_kernel(z,w) = pi * K_E(z,w).
    """
    zz = mp.mpc(z)
    ww = mp.mpc(w)
    denom = 2 * mp.pi * 1j * (mp.conj(ww) - zz)
    if denom == 0:
        raise ZeroDivisionError("de Branges kernel diagonal requires a limit")
    ez, ezsharp = differential_branches(zz)
    ew, ewsharp = differential_branches(ww)
    numerator = ez * mp.conj(ew) - ezsharp * mp.conj(ewsharp)
    return numerator / denom


def xf8_force_from_margin(
    x: float | mp.mpf,
    r: float | mp.mpf,
) -> mp.mpf:
    r"""Return Delta_D/(4 sqrt(r)); exact for r>0."""
    xx = mp.mpf(x)
    rr = _nonnegative_radius(r)
    if rr == 0:
        return closure_radial_force(xx, rr)
    y = mp.sqrt(rr)
    delta = differential_margin(mp.mpc(xx, y))
    return delta / (4 * y)
