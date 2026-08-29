from __future__ import annotations

import mpmath as mp
import pytest

from critical_axis.laguerre_hierarchy import (
    adaptive_transverse_mass_envelope,
    a0_log_slope,
    b0_laguerre_curvature,
    b0_ratio_derivative_crosswalk,
    first_laguerre_b0_crosswalk,
    first_laguerre_direct,
    first_laguerre_phi_crosswalk,
    radial_log_slope_ratio_derivative,
    second_level_log_curvature,
)
from critical_axis.transverse_mass import transverse_mass


@pytest.fixture(autouse=True)
def _xf7_precision():
    with mp.workdps(50):
        yield


@pytest.mark.parametrize("r", ["0.25", "0.5", "1.0", "2.0"])
def test_exact_first_laguerre_coordinate_crosswalk(r: str):
    rr = mp.mpf(r)
    direct = first_laguerre_direct(rr**2)
    via_phi = first_laguerre_phi_crosswalk(rr)
    via_b0 = first_laguerre_b0_crosswalk(rr)
    scale = max(mp.mpf("1"), abs(direct), abs(via_phi), abs(via_b0))
    assert abs(direct - via_phi) <= mp.mpf("1e-35") * scale
    assert abs(direct - via_b0) <= mp.mpf("1e-35") * scale


@pytest.mark.parametrize("r", ["0.25", "0.5", "1.0", "2.0"])
def test_exact_b0_radial_ratio_derivative_crosswalk(r: str):
    direct = radial_log_slope_ratio_derivative(r)
    via_b0 = b0_ratio_derivative_crosswalk(r)
    scale = max(mp.mpf("1"), abs(direct), abs(via_b0))
    assert abs(direct - via_b0) <= mp.mpf("1e-34") * scale


def test_reference_finite_kernel_laguerre_signs_are_diagnostic():
    for r in map(mp.mpf, ("0.25", "0.5", "1.0", "2.0")):
        assert first_laguerre_phi_crosswalk(r) > 0
        assert a0_log_slope(r) > 0
        assert b0_laguerre_curvature(r) > 0


def test_reference_second_level_log_curvature_is_negative_diagnostic():
    for t in map(mp.mpf, ("0.25", "1.0", "4.0")):
        assert second_level_log_curvature(t) < 0


@pytest.mark.parametrize(
    ("a", "b"),
    [("0.5", "0.1"), ("1.0", "0.2"), ("1.0", "0.4"), ("2.0", "0.5")],
)
def test_reference_adaptive_envelope_dominates_finite_mass_diagnostic(a: str, b: str):
    mass = transverse_mass(a, b)
    envelope = adaptive_transverse_mass_envelope(a, b)
    assert mass <= envelope


def test_adaptive_envelope_matches_center_at_zero_offset():
    center = transverse_mass("1.0", "0")
    envelope = adaptive_transverse_mass_envelope("1.0", "0")
    assert mp.almosteq(center, envelope)


@pytest.mark.parametrize("bad", ["0", "-0.5"])
def test_laguerre_radius_domain_fails_closed(bad: str):
    with pytest.raises(ValueError):
        first_laguerre_phi_crosswalk(bad)


@pytest.mark.parametrize(("a", "b"), [("0", "0"), ("1", "1"), ("1", "1.1")])
def test_adaptive_envelope_domain_fails_closed(a: str, b: str):
    with pytest.raises(ValueError):
        adaptive_transverse_mass_envelope(a, b)
