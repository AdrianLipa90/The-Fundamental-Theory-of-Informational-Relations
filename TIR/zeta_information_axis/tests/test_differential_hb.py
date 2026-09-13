from __future__ import annotations

import mpmath as mp
import pytest

from critical_axis.differential_hb import (
    xi_differential_hb_margin,
    xi_differential_hb_pair,
    xi_integrated_laguerre_margin,
    xi_modulus_y_derivative,
    xi_weyl_log_derivative,
)
from critical_axis.xi_kernel import zeta_s_to_xi_z


@pytest.fixture(autouse=True)
def _xf8_precision():
    with mp.workdps(50):
        yield


def test_differential_pair_reconstructs_xi_exactly_numerically() -> None:
    z = mp.mpc("10", "0.1")
    pair = xi_differential_hb_pair(z)
    reconstructed = (pair.e + pair.e_sharp) / 2
    assert abs(reconstructed - pair.xi) < mp.mpf("1e-45")


def test_hb_margin_equals_twice_transverse_modulus_derivative() -> None:
    for x, y in (("0", "0.1"), ("10", "0.1"), ("14", "0.4")):
        margin = xi_differential_hb_margin(mp.mpc(x, y))
        derivative = xi_modulus_y_derivative(mp.mpf(x), mp.mpf(y))
        assert abs(margin - 2 * derivative) < mp.mpf("1e-40")


def test_hb_margin_matches_integrated_laguerre_curvature() -> None:
    x = mp.mpf("10")
    y = mp.mpf("0.1")
    margin = xi_differential_hb_margin(mp.mpc(x, y))
    integrated = xi_integrated_laguerre_margin(x, y)
    assert abs(margin - integrated) < mp.mpf("1e-30")


def test_hb_margin_matches_weyl_herglotz_form() -> None:
    z = mp.mpc("10", "0.1")
    pair = xi_differential_hb_pair(z)
    m_xi = xi_weyl_log_derivative(z)
    rhs = 4 * abs(pair.xi) ** 2 * mp.im(m_xi)
    assert abs(pair.margin - rhs) < mp.mpf("1e-40")


def test_first_known_simple_zero_has_pi_boundary_phase() -> None:
    s0 = mp.zetazero(1)
    z0 = zeta_s_to_xi_z(s0)
    pair = xi_differential_hb_pair(z0)
    assert abs(pair.xi) < mp.mpf("1e-45")
    assert abs(pair.xi_prime) > mp.mpf("1e-6")
    assert abs(pair.theta() + 1) < mp.mpf("1e-38")


def test_reference_upper_half_plane_margins_are_positive_diagnostics_only() -> None:
    # Finite points are regression diagnostics, not evidence for the global
    # RH-equivalent strict-margin condition.
    for z in (mp.mpc("0", "0.1"), mp.mpc("10", "0.1"), mp.mpc("17", "0.1")):
        assert xi_differential_hb_margin(z) > 0
