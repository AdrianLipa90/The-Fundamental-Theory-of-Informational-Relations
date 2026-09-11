from __future__ import annotations

from critical_axis.solver import DEFAULT_SOLVER
from critical_axis.xf7_rules import XF7_SOLVER


def test_xf7_preprint_gate_stays_out_of_default_closure():
    closure = XF7_SOLVER.closure({"xi_fourier_kernel"})
    assert closure.derives("xi_kernel_positive_strict_decrease")
    assert not closure.derives("planat_sole_second_level_concavity")
    assert not closure.derives("xf7_first_laguerre_positive_s_sqrt")
    assert not closure.derives("xf7_b0_positive")
    assert not closure.derives("xf7_global_signed_core_tail_domination")
    assert not closure.derives("riemann_hypothesis")


def test_supplied_preprint_claim_reaches_exact_crosswalk_but_stops_at_global_gate():
    closure = XF7_SOLVER.closure(
        {"xi_fourier_kernel", "planat_sole_second_level_concavity"}
    )
    assert closure.derives("xf7_first_laguerre_positive_s_sqrt")
    assert closure.derives("xf7_double_turan_hierarchy")
    assert closure.derives("xf7_b0_positive")
    assert closure.derives("xf7_radial_log_slope_ratio_increasing")
    assert closure.derives("xi_kernel_strict_log_concavity_tp2")
    assert closure.derives("xf6_transverse_mass_strict_abs_b_decay")
    assert closure.derives("xf7_adaptive_transverse_mass_envelope")
    assert closure.derives("xf7_signed_cosine_tail_ibp_bound")
    assert not closure.derives("xf7_global_signed_core_tail_domination")
    assert not closure.derives("xi_wiener_laguerre_strict_positivity")
    assert not closure.derives("riemann_hypothesis")


def test_explicit_global_signed_gate_is_a_sufficient_route_to_rh():
    closure = XF7_SOLVER.closure(
        {
            "xi_fourier_kernel",
            "planat_sole_second_level_concavity",
            "xf7_global_signed_core_tail_domination",
        }
    )
    assert closure.derives("xi_wiener_laguerre_strict_positivity")
    assert closure.derives("riemann_hypothesis")


def test_default_solver_is_unchanged_by_xf7_extension():
    closure = DEFAULT_SOLVER.closure(
        {"xi_fourier_kernel", "planat_sole_second_level_concavity"}
    )
    assert not closure.derives("xf7_b0_positive")
    assert not closure.derives("xf7_signed_cosine_tail_ibp_bound")
