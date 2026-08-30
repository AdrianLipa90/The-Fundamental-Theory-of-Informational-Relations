from __future__ import annotations

import mpmath as mp
import pytest

from critical_axis.correlation_kernel import (
    correlation_nu2,
    even_riemann_phi,
    phi_2_y,
    xi_laguerre_quantity,
    xi_wiener_laguerre_scalar,
    xi_wronskian2_real,
)


def test_even_riemann_kernel_extension_is_symmetric() -> None:
    with mp.workdps(35):
        t = mp.mpf("0.4")
        assert even_riemann_phi(t, max_terms=8) > 0
        assert abs(
            even_riemann_phi(t, max_terms=8)
            - even_riemann_phi(-t, max_terms=8)
        ) < mp.mpf("1e-32")


def test_nu2_is_positive_and_even_on_reference_point() -> None:
    with mp.workdps(35):
        positive = correlation_nu2(mp.mpf("0.5"), max_terms=8, cutoff=3)
        negative = correlation_nu2(mp.mpf("-0.5"), max_terms=8, cutoff=3)
        assert positive > 0
        assert abs(positive - negative) < mp.mpf("1e-28")


def test_nu2_origin_matches_stable_reference_diagnostic() -> None:
    with mp.workdps(35):
        value = correlation_nu2(0, max_terms=8, cutoff=3)
        reference = mp.mpf("0.031438117053372116363774399391986")
        assert abs(value - reference) < mp.mpf("1e-30")


def test_phi2y_is_even_in_y_and_positive_on_reference_point() -> None:
    with mp.workdps(35):
        plus = phi_2_y(mp.mpf("0.5"), mp.mpf("0.2"), max_terms=8, cutoff=3)
        minus = phi_2_y(mp.mpf("0.5"), mp.mpf("-0.2"), max_terms=8, cutoff=3)
        assert plus > 0
        assert abs(plus - minus) < mp.mpf("1e-28")


def test_real_axis_laguerre_and_wronskian_identity_closes() -> None:
    with mp.workdps(50):
        for x in (mp.mpf("0"), mp.mpf("1"), mp.mpf("5")):
            residual = xi_laguerre_quantity(x) + xi_wronskian2_real(x)
            assert abs(residual) < mp.mpf("1e-40")


def test_sampled_laguerre_quantity_is_positive_diagnostic() -> None:
    # Finite sampled positivity is a regression diagnostic only; the global
    # Laguerre-Polya/RH condition remains an analytic proof obligation.
    with mp.workdps(45):
        values = [xi_laguerre_quantity(mp.mpf(x)) for x in ("0", "1", "5", "10")]
        assert all(value > 0 for value in values)


def test_xf4_scalar_is_even_in_y_on_reference_points() -> None:
    with mp.workdps(45):
        for x, y in (("0", "0.1"), ("1", "0.2"), ("5", "0.4")):
            plus = xi_wiener_laguerre_scalar(mp.mpf(x), mp.mpf(y))
            minus = xi_wiener_laguerre_scalar(mp.mpf(x), -mp.mpf(y))
            assert abs(plus - minus) < mp.mpf("1e-35")


def test_xf4_origin_scalar_is_strictly_positive_diagnostic() -> None:
    # Dimitrov--Xu prove positivity at x=0 analytically for admissible y.
    # These finite values are implementation checks for that theorem input.
    with mp.workdps(45):
        for y in ("0.1", "0.2", "0.4"):
            assert xi_wiener_laguerre_scalar(0, mp.mpf(y)) > 0


def test_xf4_scalar_interface_fails_closed_outside_open_y_domain() -> None:
    for y in ("0", "0.5", "-0.5", "0.75"):
        with pytest.raises(ValueError):
            xi_wiener_laguerre_scalar(0, mp.mpf(y))


def test_density_criterion_interface_fails_closed() -> None:
    with pytest.raises(ValueError):
        phi_2_y(0, 0)
    with pytest.raises(ValueError):
        phi_2_y(0, mp.mpf("0.5"))
    with pytest.raises(ValueError):
        phi_2_y(0, mp.mpf("-0.5"))
    with pytest.raises(ValueError):
        correlation_nu2(0, cutoff=0)
    with pytest.raises(ValueError):
        correlation_nu2(0, max_terms=0)
