from __future__ import annotations

import mpmath as mp
import pytest

from critical_axis.signed_tail import (
    adaptive_oscillatory_tail_bound,
    oscillatory_tail_ibp_bound,
    oscillatory_tail_integral_diagnostic,
)


@pytest.fixture(autouse=True)
def _xf7_tail_precision():
    with mp.workdps(50):
        yield


@pytest.mark.parametrize(
    ("a", "r", "x"),
    [("0.5", "0.1", "8"), ("1.0", "0.2", "5"), ("1.0", "0.4", "10"), ("2.0", "0.5", "3")],
)
def test_reference_signed_tail_is_below_ibp_bound_diagnostic(a: str, r: str, x: str):
    integral = abs(oscillatory_tail_integral_diagnostic(a, r, x))
    bound = oscillatory_tail_ibp_bound(a, r, x)
    assert integral <= bound


@pytest.mark.parametrize(
    ("a", "r", "x"),
    [("0.5", "0.1", "8"), ("1.0", "0.2", "5"), ("1.0", "0.4", "10")],
)
def test_reference_adaptive_signed_tail_bound_dominates_integral_diagnostic(
    a: str, r: str, x: str
):
    integral = abs(oscillatory_tail_integral_diagnostic(a, r, x))
    bound = adaptive_oscillatory_tail_bound(a, r, x)
    assert integral <= bound


def test_ibp_bound_retains_inverse_frequency_gain():
    low = oscillatory_tail_ibp_bound("1.0", "0.2", "5")
    high = oscillatory_tail_ibp_bound("1.0", "0.2", "10")
    assert mp.almosteq(high, low / 2)


@pytest.mark.parametrize(
    ("a", "r", "x"),
    [("0", "0", "1"), ("1", "-0.1", "1"), ("1", "1", "1"), ("1", "0.2", "0")],
)
def test_signed_tail_domain_fails_closed(a: str, r: str, x: str):
    with pytest.raises(ValueError):
        oscillatory_tail_ibp_bound(a, r, x)
