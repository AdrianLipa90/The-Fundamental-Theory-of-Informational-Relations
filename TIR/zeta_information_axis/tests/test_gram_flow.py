from __future__ import annotations

import mpmath as mp
import pytest

from critical_axis.gram_flow import (
    hermitian_min_eigenvalue,
    xi_tilted_autocorrelation,
    xi_tilted_autocorrelation_derivative,
    xi_translation_gram,
)


@pytest.fixture(autouse=True)
def _xf8c_precision():
    with mp.workdps(40):
        yield


def test_autocorrelation_is_even_numerically() -> None:
    y = mp.mpf("0.1")
    t = mp.mpf("0.4")
    lhs = xi_tilted_autocorrelation(t, y)
    rhs = xi_tilted_autocorrelation(-t, y)
    assert abs(lhs - rhs) < mp.mpf("1e-35")


def test_h_is_transverse_derivative_of_c_numerically() -> None:
    y = mp.mpf("0.1")
    t = mp.mpf("0.4")
    analytic = xi_tilted_autocorrelation_derivative(t, y)
    direct = mp.diff(lambda yy: xi_tilted_autocorrelation(t, yy), y)
    assert abs(analytic - direct) < mp.mpf("1e-30")


def test_translation_autocorrelation_gram_is_psd_diagnostic() -> None:
    gram = xi_translation_gram(("0", "0.4", "0.9"), "0.1")
    assert hermitian_min_eigenvalue(gram) > mp.mpf("1e-6")


def test_reference_derivative_gram_is_psd_diagnostic_only() -> None:
    # This finite sample does not establish the global RH-equivalent Loewner gate.
    derivative_gram = xi_translation_gram(
        ("0", "0.4", "0.9"),
        "0.1",
        derivative=True,
    )
    assert hermitian_min_eigenvalue(derivative_gram) > mp.mpf("1e-6")


def test_reference_two_point_gate_has_h_t_below_h_zero() -> None:
    y = mp.mpf("0.1")
    h0 = xi_tilted_autocorrelation_derivative("0", y)
    ht = xi_tilted_autocorrelation_derivative("0.4", y)
    assert h0 > ht > 0


def test_gram_runtime_controls_fail_closed() -> None:
    with pytest.raises(ValueError):
        xi_tilted_autocorrelation(0, 0.1, cutoff=0)
    with pytest.raises(ValueError):
        xi_tilted_autocorrelation_derivative(0, 0.1, max_terms=0)
    with pytest.raises(ValueError):
        xi_translation_gram((), 0.1)
