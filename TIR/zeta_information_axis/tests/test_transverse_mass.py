from __future__ import annotations

import mpmath as mp
import pytest

from critical_axis.nonlocal_curvature import theta_curvature_kernel
from critical_axis.transverse_mass import (
    curvature_positive_corridor_radius,
    gaussian_mass_envelope,
    theta_curvature_corridor_lower_bound,
    theta_curvature_corridor_margin,
    transverse_log_gap,
    transverse_log_mass_hessian,
    transverse_log_mass_slope_b,
    transverse_mass,
    transverse_mass_ratio,
)


def test_transverse_mass_is_even_in_b() -> None:
    with mp.workdps(50):
        a = mp.mpf("0.8")
        b = mp.mpf("0.2")
        plus = transverse_mass(a, b)
        minus = transverse_mass(a, -b)
        assert abs(plus - minus) < mp.mpf("1e-45")


def test_finite_phi_surface_is_transversely_concentrated_at_reference_point() -> None:
    with mp.workdps(50):
        ratio = transverse_mass_ratio(mp.mpf("0.8"), mp.mpf("0.2"))
        assert 0 < ratio < 1


def test_log_gap_matches_mass_ratio_identity() -> None:
    with mp.workdps(50):
        a = mp.mpf("0.9")
        b = mp.mpf("0.15")
        ratio = transverse_mass_ratio(a, b)
        gap = transverse_log_gap(a, b)
        assert abs(ratio - mp.exp(-gap)) < mp.mpf("1e-42")
        assert gap > 0


def test_transverse_log_mass_slope_is_odd_and_negative_for_positive_b() -> None:
    with mp.workdps(50):
        a = mp.mpf("0.8")
        b = mp.mpf("0.2")
        positive_b = transverse_log_mass_slope_b(a, b)
        negative_b = transverse_log_mass_slope_b(a, -b)
        assert positive_b < 0
        assert abs(positive_b + negative_b) < mp.mpf("1e-38")


def test_reference_hessian_has_negative_log_concavity_eigenvalues() -> None:
    with mp.workdps(50):
        hessian = transverse_log_mass_hessian(mp.mpf("0.8"), mp.mpf("0.2"))
        assert hessian.eigen_plus < 0
        assert hessian.eigen_minus < 0
        assert hessian.aa == hessian.bb


def test_exact_positive_corridor_lower_bound() -> None:
    with mp.workdps(50):
        x = mp.mpf("2.0")
        y = mp.mpf("0.2")
        a = mp.mpf("0.8")
        radius = curvature_positive_corridor_radius(x, a)
        b = radius / 2
        lower = theta_curvature_corridor_lower_bound(x, y, a, b)
        actual = theta_curvature_kernel(x, y, a, b)
        margin = theta_curvature_corridor_margin(x, y, a, b)
        assert lower > 0
        assert actual >= lower
        assert margin >= 0


def test_x_zero_corridor_covers_full_interior() -> None:
    with mp.workdps(50):
        a = mp.mpf("0.8")
        b = mp.mpf("0.79")
        assert curvature_positive_corridor_radius(0, a) == a
        lower = theta_curvature_corridor_lower_bound(0, mp.mpf("0.2"), a, b)
        assert lower > 0
        assert theta_curvature_kernel(0, mp.mpf("0.2"), a, b) >= lower


def test_gaussian_envelope_and_coordinates_fail_closed() -> None:
    with mp.workdps(40):
        envelope = gaussian_mass_envelope(
            mp.mpf("0.8"), mp.mpf("0.2"), mp.mpf("1.0")
        )
        center = transverse_mass(mp.mpf("0.8"), mp.mpf("0"))
        assert 0 < envelope < center

    with pytest.raises(ValueError):
        transverse_mass(0.5, 0.5)
    with pytest.raises(ValueError):
        transverse_mass(-0.5, 0.1)
    with pytest.raises(ValueError):
        gaussian_mass_envelope(0.8, 0.2, 0)
    with pytest.raises(ValueError):
        theta_curvature_corridor_lower_bound(10, 0.2, 0.8, 0.2)
