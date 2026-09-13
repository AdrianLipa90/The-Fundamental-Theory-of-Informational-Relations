"""Cayley-Schur and de Branges-Pick diagnostics for the Xi programme.

The exact analytic identities are:

    m_Xi(z) = -Xi'(z)/Xi(z),
    Theta_D(z) = (1 + i m_Xi(z)) / (1 - i m_Xi(z)),

for Xi(z) != 0, where Theta_D=E_D#/E_D and

    E_D = Xi + i Xi',
    E_D# = Xi - i Xi'.

The unnormalised de Branges-type kernel is

    K_D(z,w) = [E_D(z) conj(E_D(w)) - E_D#(z) conj(E_D#(w))]
               / [-i (z-conj(w))].

On the diagonal in the upper half-plane,

    K_D(z,z) = Delta_D(z)/(2 Im z).

Global positive semidefiniteness of the associated Pick kernel is RH-level and
is deliberately not inferred from finite numerical evaluations.
"""

from __future__ import annotations

import mpmath as mp

from .differential_hb import xi_differential_hb_pair, xi_weyl_log_derivative
from .xi_kernel import completed_xi_on_z_axis


def xi_cayley_theta(z: complex | mp.mpc) -> mp.mpc:
    """Return the differential branch quotient E_D#/E_D where defined."""
    pair = xi_differential_hb_pair(z)
    return pair.theta()


def xi_cayley_theta_from_weyl(z: complex | mp.mpc) -> mp.mpc:
    """Return (1+i m_Xi)/(1-i m_Xi) away from Xi zeros."""
    m_xi = xi_weyl_log_derivative(z)
    denom = 1 - 1j * m_xi
    if denom == 0:
        raise ZeroDivisionError("Cayley denominator vanishes")
    return (1 + 1j * m_xi) / denom


def xi_debranges_pick_kernel(z: complex | mp.mpc, w: complex | mp.mpc) -> mp.mpc:
    """Return the unnormalised de Branges/Pick kernel K_D(z,w).

    The conventional positive normalisation constant used in de Branges-space
    literature is intentionally omitted; only sign and PSD structure matter
    for this audit.
    """
    zz = mp.mpc(z)
    ww = mp.mpc(w)
    denom = -1j * (zz - mp.conj(ww))
    if denom == 0:
        raise ZeroDivisionError("Pick kernel denominator vanishes on this pair")
    pz = xi_differential_hb_pair(zz)
    pw = xi_differential_hb_pair(ww)
    numerator = pz.e * mp.conj(pw.e) - pz.e_sharp * mp.conj(pw.e_sharp)
    return numerator / denom


def xi_debranges_pick_kernel_wronskian(
    z: complex | mp.mpc,
    w: complex | mp.mpc,
) -> mp.mpc:
    """Return the exact divided-Wronskian form of K_D(z,w)."""
    zz = mp.mpc(z)
    ww = mp.mpc(w)
    denom = mp.conj(ww) - zz
    if denom == 0:
        raise ZeroDivisionError("divided-Wronskian denominator vanishes on this pair")
    a_z = completed_xi_on_z_axis(zz)
    a_w_bar = completed_xi_on_z_axis(mp.conj(ww))
    ap_z = mp.diff(completed_xi_on_z_axis, zz, 1)
    ap_w_bar = mp.diff(completed_xi_on_z_axis, mp.conj(ww), 1)
    return 2 * (ap_z * a_w_bar - a_z * ap_w_bar) / denom


def xi_schur_pick_kernel(z: complex | mp.mpc, w: complex | mp.mpc) -> mp.mpc:
    """Return the normalised Schur-Pick kernel where Theta_D is defined."""
    zz = mp.mpc(z)
    ww = mp.mpc(w)
    denom = -1j * (zz - mp.conj(ww))
    if denom == 0:
        raise ZeroDivisionError("Pick kernel denominator vanishes on this pair")
    theta_z = xi_cayley_theta(zz)
    theta_w = xi_cayley_theta(ww)
    return (1 - theta_z * mp.conj(theta_w)) / denom
