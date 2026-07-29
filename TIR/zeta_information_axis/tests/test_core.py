from __future__ import annotations

import mpmath as mp
import pytest

from critical_axis.core import (
    berry_holonomy,
    binary_entropy,
    binary_entropy_prime,
    binary_entropy_second,
    completed_xi,
    dirichlet_eta,
    eta_prefactor,
    first_nontrivial_zeros,
    two_channel_amplitude,
    zeta_involution,
)

mp.mp.dps = 50


def test_shannon_balance() -> None:
    assert mp.almosteq(binary_entropy(mp.mpf("0.5")), mp.log(2))
    assert mp.almosteq(binary_entropy_prime(mp.mpf("0.5")), 0)
    assert binary_entropy_second(mp.mpf("0.5")) < 0


def test_exact_destructive_interference() -> None:
    amp = two_channel_amplitude(mp.mpf("0.5"), mp.pi)
    assert abs(amp) < mp.mpf("1e-45")


@pytest.mark.parametrize("sigma", ["0.1", "0.25", "0.49", "0.51", "0.75", "0.9"])
def test_pi_phase_does_not_cancel_unequal_weights(sigma: str) -> None:
    amp = two_channel_amplitude(mp.mpf(sigma), mp.pi)
    assert abs(amp) > mp.mpf("1e-8")


def test_equatorial_berry_holonomy_is_minus_one() -> None:
    assert abs(berry_holonomy(mp.mpf("0.5")) + 1) < mp.mpf("1e-45")


def test_involution_fixed_axis() -> None:
    s = mp.mpc(mp.mpf("0.5"), mp.mpf("14.134725"))
    assert abs(zeta_involution(s) - s) < mp.mpf("1e-45")


def test_xi_functional_symmetry_numerically() -> None:
    for s in [mp.mpc("0.2", "3.0"), mp.mpc("0.7", "8.0"), mp.mpc("1.3", "2.5")]:
        assert abs(completed_xi(s) - completed_xi(1 - s)) < mp.mpf("1e-40")


def test_eta_factorization() -> None:
    for s in [mp.mpc("0.7", "3.2"), mp.mpc("1.2", "5.1"), mp.mpc("2.0", "0.5")]:
        lhs = dirichlet_eta(s)
        rhs = eta_prefactor(s) * mp.zeta(s)
        assert abs(lhs - rhs) < mp.mpf("1e-40")


def test_eta_at_one() -> None:
    assert abs(dirichlet_eta(1) - mp.log(2)) < mp.mpf("1e-45")


def test_first_zeros_are_on_critical_line_in_mpmath_table() -> None:
    zeros = first_nontrivial_zeros(10)
    assert all(abs(mp.re(z) - mp.mpf("0.5")) < mp.mpf("1e-45") for z in zeros)
