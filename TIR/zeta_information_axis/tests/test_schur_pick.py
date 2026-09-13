from __future__ import annotations

import mpmath as mp
import pytest

from critical_axis.differential_hb import (
    xi_differential_hb_margin,
    xi_differential_hb_pair,
)
from critical_axis.schur_pick import (
    xi_cayley_theta,
    xi_cayley_theta_from_weyl,
    xi_debranges_pick_kernel,
    xi_debranges_pick_kernel_wronskian,
    xi_schur_pick_kernel,
)


@pytest.fixture(autouse=True)
def _xf8b_precision():
    with mp.workdps(50):
        yield


def test_cayley_theta_matches_differential_branch_quotient() -> None:
    for z in (mp.mpc("0", "0.1"), mp.mpc("10", "0.1"), mp.mpc("17", "0.2")):
        direct = xi_cayley_theta(z)
        via_weyl = xi_cayley_theta_from_weyl(z)
        assert abs(direct - via_weyl) < mp.mpf("1e-40")


def test_debranges_kernel_matches_divided_wronskian() -> None:
    pairs = (
        (mp.mpc("10", "0.1"), mp.mpc("12", "0.2")),
        (mp.mpc("0", "0.15"), mp.mpc("3", "0.25")),
    )
    for z, w in pairs:
        direct = xi_debranges_pick_kernel(z, w)
        wronskian = xi_debranges_pick_kernel_wronskian(z, w)
        assert abs(direct - wronskian) < mp.mpf("1e-38")


def test_debranges_kernel_is_hermitian_numerically() -> None:
    z = mp.mpc("10", "0.1")
    w = mp.mpc("12", "0.2")
    lhs = xi_debranges_pick_kernel(z, w)
    rhs = mp.conj(xi_debranges_pick_kernel(w, z))
    assert abs(lhs - rhs) < mp.mpf("1e-40")


def test_diagonal_kernel_equals_margin_over_two_y() -> None:
    for x, y in (("0", "0.1"), ("10", "0.1"), ("14", "0.4")):
        z = mp.mpc(x, y)
        kernel = xi_debranges_pick_kernel(z, z)
        expected = xi_differential_hb_margin(z) / (2 * mp.mpf(y))
        assert abs(kernel - expected) < mp.mpf("1e-38")


def test_normalised_pick_kernel_is_congruent_to_debranges_kernel() -> None:
    z = mp.mpc("10", "0.1")
    w = mp.mpc("12", "0.2")
    pz = xi_differential_hb_pair(z)
    pw = xi_differential_hb_pair(w)
    normalised = xi_schur_pick_kernel(z, w)
    debranges = xi_debranges_pick_kernel(z, w)
    expected = pz.e * mp.conj(pw.e) * normalised
    assert abs(debranges - expected) < mp.mpf("1e-38")


def test_reference_upper_half_plane_theta_is_inside_disk_diagnostic_only() -> None:
    # Finite points are regression diagnostics only.  They do not establish
    # the global Schur/Pick condition, which remains RH-equivalent.
    for z in (mp.mpc("0", "0.1"), mp.mpc("10", "0.1"), mp.mpc("17", "0.1")):
        assert abs(xi_cayley_theta(z)) < 1
