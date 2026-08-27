from __future__ import annotations

import mpmath as mp

from critical_axis.solver import (
    DEFAULT_SOLVER,
    kappa_from_projective_cycle,
    solve_half_axis_routes,
    validate_half_axis_routes,
)

mp.mp.dps = 60


def test_four_independent_half_axis_routes_agree() -> None:
    routes = solve_half_axis_routes()
    assert set(routes) == {"complement", "entropy", "berry_minus_one", "cancellation"}
    assert all(abs(value - mp.mpf("0.5")) < mp.mpf("1e-40") for value in routes.values())
    assert validate_half_axis_routes(mp.mpf("1e-40"))


def test_exact_closure_does_not_promote_model_or_open_claims() -> None:
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
    }
    result = DEFAULT_SOLVER.closure(facts)
    assert result.derives("entropy_max_ln2")
    assert result.derives("berry_minus_one")
    assert result.derives("exact_cancellation")
    assert result.derives("reciprocal_axis_invariant")
    assert result.derives("spinor_double_cover")
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
    }
    result = DEFAULT_SOLVER.closure(facts, allow_model=True)
    assert result.derives("information_per_turn_ln2_over_12")
    assert result.derives("kappa_ln2_over_24pi")
    assert result.derives("twenty_four_sector_count")
    assert result.derives("twenty_four_pi_normalization")
    assert not result.derives("riemann_hypothesis")


def test_solver_exposes_missing_zero_state_bridge() -> None:
    facts = {"exact_cancellation", "sigma_equals_real_part_coordinate"}
    missing = DEFAULT_SOLVER.missing_premises("all_zeros_on_half_axis", facts, allow_model=True)
    assert missing
    assert any("zero_state_representation" in absent for _, absent in missing)


def test_kappa_normalization_matches_runtime_value() -> None:
    expected = mp.log(2) / (24 * mp.pi)
    assert abs(kappa_from_projective_cycle() - expected) < mp.mpf("1e-50")
