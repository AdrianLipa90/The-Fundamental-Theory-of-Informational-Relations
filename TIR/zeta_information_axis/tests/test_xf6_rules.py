from __future__ import annotations

from critical_axis.xf6_rules import XF6_SOLVER


def test_xf6_does_not_promote_external_log_concavity_claim() -> None:
    closure = XF6_SOLVER.closure({"xi_fourier_kernel"})
    assert "xf6_exact_positive_curvature_corridor" in closure.facts
    assert "xi_kernel_strict_log_concavity_tp2" not in closure.facts
    assert "xf6_transverse_mass_center_dominance" not in closure.facts
    assert "xf6_global_core_tail_domination" not in closure.facts
    assert "riemann_hypothesis" not in closure.facts


def test_supplied_tp2_premise_derives_only_conditional_mass_geometry() -> None:
    closure = XF6_SOLVER.closure(
        {"xi_fourier_kernel", "xi_kernel_strict_log_concavity_tp2"}
    )
    assert "xf6_transverse_mass_center_dominance" in closure.facts
    assert "xf6_transverse_mass_strict_abs_b_decay" in closure.facts
    assert "xf6_slice_gaussian_mass_envelope_exists" in closure.facts
    assert "xf6_exact_positive_curvature_corridor" in closure.facts
    assert "xf6_global_core_tail_domination" not in closure.facts
    assert "xi_wiener_laguerre_strict_positivity" not in closure.facts
    assert "riemann_hypothesis" not in closure.facts


def test_global_core_tail_gate_is_the_explicit_sign_bridge() -> None:
    closure = XF6_SOLVER.closure(
        {
            "xi_fourier_kernel",
            "phi2y_fourier_equals_xi_wiener_laguerre_scalar",
            "xi_transverse_curvature_identity",
            "xf6_global_core_tail_domination",
        }
    )
    assert "xi_wiener_laguerre_strict_positivity" in closure.facts
    assert "xi_strict_transverse_convexity_critical_strip" in closure.facts
    assert "xi_vertical_growth_outer_halfplane" in closure.facts
    assert "xi_vertical_growth_critical_strip" in closure.facts
    assert "xi_vertical_growth_halfplane" in closure.facts
    assert "riemann_hypothesis" in closure.facts
