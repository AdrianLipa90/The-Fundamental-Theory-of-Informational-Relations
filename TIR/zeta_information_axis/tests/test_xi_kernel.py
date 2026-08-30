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


@pytest.fixture(autouse=True)
def _xf_kernel_precision():
    """Give XF tests local precision without mutating the pytest session."""
    with mp.workdps(50):
        yield


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


def test_constant_real_branch_mixing_class_has_sign_changing_hb_margin() -> None:
    # For E_c = Xi + c(A_- - A_+) with real c, one has
    # |E_c|^2-|E_c#|^2 = 4c (|A_-|^2-|A_+|^2).
    # The branch margin changes sign in the upper half-plane, so no fixed
    # nonzero real c can make this class Hermite-Biehler globally.
    positive = xi_kernel_branches(mp.mpc("10", "0.1"))
    negative = xi_kernel_branches(mp.mpc("17", "0.1"))
    margin_positive = abs(positive.minus) ** 2 - abs(positive.plus) ** 2
    margin_negative = abs(negative.minus) ** 2 - abs(negative.plus) ** 2
    assert margin_positive > mp.mpf("1e-4")
    assert margin_negative < mp.mpf("-1e-7")


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
