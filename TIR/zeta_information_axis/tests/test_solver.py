from __future__ import annotations

import mpmath as mp

from critical_axis.solver import (
    DEFAULT_SOLVER,
    kappa_from_projective_cycle,
    solve_half_axis_routes,
    validate_half_axis_routes,
)


def test_four_independent_half_axis_routes_agree() -> None:
    with mp.workdps(60):
        routes = solve_half_axis_routes()
        assert set(routes) == {"complement", "entropy", "berry_minus_one", "cancellation"}
        assert all(abs(value - mp.mpf("0.5")) < mp.mpf("1e-40") for value in routes.values())
        assert validate_half_axis_routes(mp.mpf("1e-40"))


def test_exact_closure_admits_xi_kernel_cancellation_but_keeps_open_bridges_blocked() -> None:
    facts = {
        "sigma_half",
        "qubit_representation",
        "symmetric_readout",
        "half_turn_phase",
        "centered_zeta_chart",
        "reciprocal_chart",
        "affine_endpoint_map",
        "projective_cycle",
        "spin_half",
        "binary_information",
        "twelve_projective_cycles",
        "radian_closure_tau",
        "eight_mix_sectors",
        "three_flavours",
        "xi_fourier_kernel",
    }
    result = DEFAULT_SOLVER.closure(facts)
    assert result.derives("entropy_max_ln2")
    assert result.derives("berry_minus_one")
    assert result.derives("exact_cancellation")
    assert result.derives("reciprocal_axis_invariant")
    assert result.derives("spinor_double_cover")
    assert result.derives("canonical_xi_two_branch_representation")
    assert result.derives("all_xi_zeros_exact_kernel_branch_cancellation")
    assert result.derives("dimitrov_xu_nu2_correlation_kernel")
    assert result.derives("xi_wronskian_nu2_fourier_identity")
    assert result.derives("phi2y_fourier_equals_xi_wiener_laguerre_scalar")
    assert result.derives("xi_transverse_curvature_identity")
    assert result.derives("xi_vertical_growth_outer_halfplane")
    assert not result.derives("global_kernel_branch_nondegeneracy")
    assert not result.derives("kernel_population_equals_strip_coordinate")
    assert not result.derives("all_xi_zero_kernel_population_half")
    assert not result.derives("phi2y_translation_density_condition")
    assert not result.derives("phi2y_bounded_convolution_annihilator_condition")
    assert not result.derives("xi_wiener_laguerre_strict_positivity")
    assert not result.derives("xi_strict_transverse_convexity_critical_strip")
    assert not result.derives("xi_vertical_growth_critical_strip")
    assert not result.derives("xi_vertical_growth_halfplane")
    assert not result.derives("kappa_ln2_over_24pi")
    assert not result.derives("twenty_four_sector_count")
    assert not result.derives("riemann_hypothesis")


def test_model_closure_can_derive_kappa_but_never_open_rh_bridge() -> None:
    facts = {
        "binary_information",
        "twelve_projective_cycles",
        "radian_closure_tau",
        "eight_mix_sectors",
        "three_flavours",
        "half_turn_phase",
        "xi_fourier_kernel",
        "affine_endpoint_map",
    }
    result = DEFAULT_SOLVER.closure(facts, allow_model=True)
    assert result.derives("information_per_turn_ln2_over_12")
    assert result.derives("kappa_ln2_over_24pi")
    assert result.derives("twenty_four_sector_count")
    assert result.derives("twenty_four_pi_normalization")
    assert result.derives("all_xi_zeros_exact_kernel_branch_cancellation")
    assert result.derives("dimitrov_xu_nu2_correlation_kernel")
    assert result.derives("xi_wronskian_nu2_fourier_identity")
    assert result.derives("phi2y_fourier_equals_xi_wiener_laguerre_scalar")
    assert result.derives("xi_transverse_curvature_identity")
    assert not result.derives("global_kernel_branch_nondegeneracy")
    assert not result.derives("kernel_population_equals_strip_coordinate")
    assert not result.derives("phi2y_translation_density_condition")
    assert not result.derives("phi2y_bounded_convolution_annihilator_condition")
    assert not result.derives("xi_wiener_laguerre_strict_positivity")
    assert not result.derives("xi_strict_transverse_convexity_critical_strip")
    assert not result.derives("riemann_hypothesis")


def test_solver_exposes_sharpened_xf1_open_bridges() -> None:
    facts = {"xi_fourier_kernel", "affine_endpoint_map"}
    missing = DEFAULT_SOLVER.missing_premises("all_zeros_on_half_axis", facts, allow_model=True)
    assert missing
    absent = {premise for _, premises in missing for premise in premises}
    assert "global_kernel_branch_nondegeneracy" in absent
    assert "kernel_population_equals_strip_coordinate" in absent


def test_explicit_admission_of_both_xf1_open_premises_closes_conditional_chain() -> None:
    facts = {
        "xi_fourier_kernel",
        "affine_endpoint_map",
        "global_kernel_branch_nondegeneracy",
        "kernel_population_equals_strip_coordinate",
    }
    result = DEFAULT_SOLVER.closure(facts)
    assert result.derives("all_xi_zeros_exact_kernel_branch_cancellation")
    assert result.derives("all_xi_zero_kernel_population_half")
    assert result.derives("all_zeros_on_half_axis")
    assert result.derives("riemann_hypothesis")


def test_xf3_standard_kernel_and_wronskian_are_admitted_but_density_is_open() -> None:
    result = DEFAULT_SOLVER.closure({"xi_fourier_kernel"})
    assert result.derives("dimitrov_xu_nu2_correlation_kernel")
    assert result.derives("xi_wronskian_nu2_fourier_identity")
    assert result.derives("phi2y_fourier_equals_xi_wiener_laguerre_scalar")
    assert not result.derives("phi2y_translation_density_condition")
    assert not result.derives("phi2y_bounded_convolution_annihilator_condition")
    assert not result.derives("xi_wiener_laguerre_strict_positivity")
    assert not result.derives("riemann_hypothesis")


def test_xf3_solver_exposes_two_global_rh_equivalent_routes() -> None:
    missing = DEFAULT_SOLVER.missing_premises(
        "riemann_hypothesis", {"xi_fourier_kernel"}, allow_model=True
    )
    assert missing
    absent = {premise for _, premises in missing for premise in premises}
    assert "phi2y_translation_density_condition" in absent
    assert "phi2y_bounded_convolution_annihilator_condition" in absent


def test_explicit_admission_of_xf3_density_condition_closes_standard_equivalence() -> None:
    result = DEFAULT_SOLVER.closure(
        {"xi_fourier_kernel", "phi2y_translation_density_condition"}
    )
    assert result.derives("xi_wiener_laguerre_strict_positivity")
    assert result.derives("xi_strict_transverse_convexity_critical_strip")
    assert result.derives("xi_vertical_growth_critical_strip")
    assert result.derives("xi_vertical_growth_halfplane")
    assert result.derives("riemann_hypothesis")
    assert result.derives("phi2y_bounded_convolution_annihilator_condition")


def test_xf4_solver_exposes_global_strict_positivity_as_open() -> None:
    facts = {"xi_fourier_kernel"}
    missing = DEFAULT_SOLVER.missing_premises(
        "xi_wiener_laguerre_strict_positivity", facts, allow_model=True
    )
    assert missing
    assert any(rule.status.value == "open" for rule, _ in missing)
    result = DEFAULT_SOLVER.closure(facts, allow_model=True)
    assert result.derives("phi2y_fourier_equals_xi_wiener_laguerre_scalar")
    assert not result.derives("xi_wiener_laguerre_strict_positivity")


def test_explicit_xf4_strict_positivity_closes_density_and_rh_equivalence() -> None:
    result = DEFAULT_SOLVER.closure(
        {"xi_fourier_kernel", "xi_wiener_laguerre_strict_positivity"}
    )
    assert result.derives("phi2y_fourier_equals_xi_wiener_laguerre_scalar")
    assert result.derives("xi_strict_transverse_convexity_critical_strip")
    assert result.derives("xi_vertical_growth_critical_strip")
    assert result.derives("xi_vertical_growth_halfplane")
    assert result.derives("phi2y_translation_density_condition")
    assert result.derives("riemann_hypothesis")
    assert result.derives("phi2y_bounded_convolution_annihilator_condition")


def test_xf5_curvature_identity_is_exact_while_global_convexity_stays_open() -> None:
    result = DEFAULT_SOLVER.closure({"xi_fourier_kernel"})
    assert result.derives("xi_transverse_curvature_identity")
    assert result.derives("xi_vertical_growth_outer_halfplane")
    assert not result.derives("xi_strict_transverse_convexity_critical_strip")
    assert not result.derives("xi_vertical_growth_critical_strip")
    assert not result.derives("xi_vertical_growth_halfplane")
    assert not result.derives("riemann_hypothesis")


def test_explicit_xf5_convexity_closes_growth_route() -> None:
    result = DEFAULT_SOLVER.closure(
        {"xi_fourier_kernel", "xi_strict_transverse_convexity_critical_strip"}
    )
    assert result.derives("xi_wiener_laguerre_strict_positivity")
    assert result.derives("xi_vertical_growth_critical_strip")
    assert result.derives("xi_vertical_growth_outer_halfplane")
    assert result.derives("xi_vertical_growth_halfplane")
    assert result.derives("riemann_hypothesis")


def test_kappa_normalization_matches_runtime_value() -> None:
    with mp.workdps(60):
        expected = mp.log(2) / (24 * mp.pi)
        assert abs(kappa_from_projective_cycle() - expected) < mp.mpf("1e-50")
