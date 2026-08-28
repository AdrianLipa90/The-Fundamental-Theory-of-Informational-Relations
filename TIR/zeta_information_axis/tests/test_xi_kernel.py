from __future__ import annotations

import mpmath as mp
import pytest

from critical_axis.xi_kernel import (
    completed_xi_on_z_axis,
    kernel_reconstruction_residual,
    riemann_phi,
    xi_kernel_branches,
    zeta_s_to_xi_z,
)

mp.mp.dps = 35


def test_riemann_phi_runtime_truncation_is_positive_on_reference_points() -> None:
    assert riemann_phi(0) > 0
    assert riemann_phi(mp.mpf("0.5")) > 0
    assert riemann_phi(1) > 0


def test_kernel_branches_reconstruct_completed_xi() -> None:
    for z in (mp.mpf("0"), mp.mpf("1")):
        residual = kernel_reconstruction_residual(z)
        assert residual < mp.mpf("1e-28")
        branches = xi_kernel_branches(z)
        assert abs(branches.reconstructed_xi - completed_xi_on_z_axis(z)) < mp.mpf("1e-28")


def test_real_axis_branches_are_conjugate() -> None:
    branches = xi_kernel_branches(mp.mpf("1"))
    assert abs(branches.minus - mp.conj(branches.plus)) < mp.mpf("1e-30")


def test_first_known_zero_is_non_degenerate_exact_branch_cancellation_numerically() -> None:
    s0 = mp.zetazero(1)
    z0 = zeta_s_to_xi_z(s0)
    assert abs(mp.im(z0)) < mp.mpf("1e-30")

    branches = xi_kernel_branches(z0)
    assert branches.cancellation_residual < mp.mpf("1e-28")
    assert abs(branches.plus) > mp.mpf("1e-3")
    assert abs(branches.minus) > mp.mpf("1e-3")
    assert abs(branches.plus + branches.minus) < mp.mpf("1e-28")
    assert abs(branches.population_plus() - mp.mpf("0.5")) < mp.mpf("1e-30")


def test_naive_minus_branch_is_not_a_global_hermite_biehler_candidate() -> None:
    # For E=A_- and E#=A_+, the HB inequality in Im(z)>0 would require
    # |A_-|>|A_+| everywhere.  This reproducible upper-half-plane witness
    # has the opposite sign, so the raw branch choice is rejected.
    z = mp.mpc("17", "0.1")
    branches = xi_kernel_branches(z)
    margin = abs(branches.minus) ** 2 - abs(branches.plus) ** 2
    assert margin < mp.mpf("-1e-7")


def test_s_to_z_map_exposes_off_axis_displacement() -> None:
    s = mp.mpc("0.4", "14")
    z = zeta_s_to_xi_z(s)
    assert abs(mp.re(z) - 14) < mp.mpf("1e-30")
    assert abs(mp.im(z) - mp.mpf("0.1")) < mp.mpf("1e-30")


def test_runtime_controls_fail_closed() -> None:
    with pytest.raises(ValueError):
        riemann_phi(-1)
    with pytest.raises(ValueError):
        riemann_phi(0, max_terms=0)
    with pytest.raises(ValueError):
        xi_kernel_branches(0, cutoff=0)
