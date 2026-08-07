from __future__ import annotations

import mpmath as mp
import pytest

from critical_axis.core import (
    aharonov_bohm_holonomy,
    berry_holonomy,
    binary_entropy,
    binary_entropy_prime,
    binary_entropy_second,
    centered_coordinate,
    centered_inversion,
    centered_zeta_involution,
    compactified_radius,
    completed_xi,
    dirichlet_eta,
    eta_prefactor,
    first_nontrivial_zeros,
    hubble_length,
    normalized_hubble_radius,
    radial_compactification,
    reciprocal_map,
    strip_probability_coordinate,
    two_channel_amplitude,
    u1_holonomy,
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


def test_centered_coordinate_conjugates_zeta_involution() -> None:
    s = mp.mpc("0.37", "8.25")
    lhs = centered_coordinate(zeta_involution(s))
    rhs = centered_zeta_involution(centered_coordinate(s))
    assert abs(lhs - rhs) < mp.mpf("1e-45")


def test_reciprocal_map_is_an_involution() -> None:
    u = mp.mpc("0.3", "2.7")
    assert abs(reciprocal_map(reciprocal_map(u)) - u) < mp.mpf("1e-45")


def test_centered_reciprocal_preserves_critical_axis() -> None:
    s = mp.mpc("0.5", "14.134725")
    v = centered_inversion(s)
    assert abs(mp.re(v)) < mp.mpf("1e-45")
    assert abs(v + 1j / mp.mpf("14.134725")) < mp.mpf("1e-45")


def test_reciprocal_commutes_with_centered_involution() -> None:
    u = mp.mpc("0.23", "4.5")
    lhs = reciprocal_map(centered_zeta_involution(u))
    rhs = centered_zeta_involution(reciprocal_map(u))
    assert abs(lhs - rhs) < mp.mpf("1e-45")


def test_naive_centered_reciprocal_is_not_zero_set_symmetry() -> None:
    for zero in first_nontrivial_zeros(10):
        mapped_s = mp.mpf("0.5") + centered_inversion(zero)
        assert abs(mp.zeta(mapped_s)) > mp.mpf("0.1")


def test_reciprocal_rejects_center() -> None:
    with pytest.raises(ValueError):
        reciprocal_map(0)


def test_radial_compactification_center_and_boundary_limit() -> None:
    assert radial_compactification(0) == 0
    assert compactified_radius(0) == 0
    u = mp.mpc("3", "4")
    mapped = radial_compactification(u)
    assert abs(mapped) < 1
    assert mp.almosteq(abs(mapped), mp.mpf("5") / 6)
    assert compactified_radius(mp.mpf("1e20")) > mp.mpf("0.9999999999999999999")


def test_affine_strip_probability_and_complement_covariance() -> None:
    s = mp.mpc("0.31", "7")
    p = strip_probability_coordinate(s)
    jp = strip_probability_coordinate(zeta_involution(s))
    assert mp.almosteq(p, mp.mpf("0.31"))
    assert mp.almosteq(jp, 1 - p)


def test_u1_and_ab_holonomy_close_at_pi() -> None:
    assert abs(u1_holonomy(mp.pi) + 1) < mp.mpf("1e-45")
    assert abs(aharonov_bohm_holonomy(mp.pi) + 1) < mp.mpf("1e-45")


def test_hubble_normalization_is_unit_at_hubble_length() -> None:
    h = mp.mpf("2.3")
    c = mp.mpf("7.1")
    ell = hubble_length(h, c)
    assert mp.almosteq(normalized_hubble_radius(ell, h, c), 1)


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
