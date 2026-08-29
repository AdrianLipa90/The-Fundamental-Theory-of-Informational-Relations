from __future__ import annotations

import mpmath as mp
import pytest

from critical_axis.nonlocal_curvature import (
    theta_curvature_integrand,
    theta_curvature_kernel,
    theta_growth_kernel,
    xi_transverse_curvature,
    xi_transverse_curvature_direct,
)
from critical_axis.correlation_kernel import xi_wiener_laguerre_scalar


def test_transverse_curvature_is_twice_xf4_scalar() -> None:
    with mp.workdps(50):
        x = mp.mpf("1.25")
        y = mp.mpf("0.2")
        lhs = xi_transverse_curvature(x, y)
        rhs = 2 * xi_wiener_laguerre_scalar(x, y)
        assert abs(lhs - rhs) < mp.mpf("1e-42")


def test_direct_y_curvature_matches_analytic_identity() -> None:
    with mp.workdps(50):
        x = mp.mpf("0.75")
        y = mp.mpf("0.15")
        direct = xi_transverse_curvature_direct(x, y)
        analytic = xi_transverse_curvature(x, y)
        assert abs(direct - analytic) < mp.mpf("1e-36")


def test_theta_curvature_kernel_is_y_derivative_of_growth_kernel() -> None:
    with mp.workdps(50):
        x = mp.mpf("2.0")
        y = mp.mpf("0.17")
        a = mp.mpf("0.8")
        b = mp.mpf("0.2")
        direct = mp.diff(lambda eta: theta_growth_kernel(x, eta, a, b), y)
        analytic = theta_curvature_kernel(x, y, a, b)
        assert abs(direct - analytic) < mp.mpf("1e-42")


def test_x_zero_curvature_integrand_is_pointwise_positive() -> None:
    with mp.workdps(40):
        value = theta_curvature_integrand(
            mp.mpf("0"), mp.mpf("0.2"), mp.mpf("0.7"), mp.mpf("0.1"), max_terms=12
        )
        assert value > 0


def test_theta_coordinates_fail_closed() -> None:
    with pytest.raises(ValueError):
        theta_curvature_kernel(1, 0.1, 0.5, 0.5)
    with pytest.raises(ValueError):
        theta_growth_kernel(1, 0.1, -0.5, 0.1)
