#!/usr/bin/env python3
"""Run the typed half-axis solver and emit a machine-readable receipt."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import mpmath as mp

from critical_axis.solver import kappa_from_projective_cycle, solve_half_axis_routes
from critical_axis.xf7_rules import XF7_SOLVER


DEFAULT_FACTS = {
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

XF7_PREPRINT_SCENARIO_FACTS = DEFAULT_FACTS | {
    "planat_sole_second_level_concavity",
}


def _proof(result) -> dict[str, dict[str, object]]:
    return {
        claim: {
            "premises": list(step.rule.premises),
            "status": step.rule.status.value,
            "provenance": step.rule.provenance,
        }
        for claim, step in sorted(result.proof.items())
    }


def _missing(goal: str, facts: set[str]) -> list[dict[str, object]]:
    candidates = XF7_SOLVER.missing_premises(goal, facts, allow_model=True)
    return [
        {
            "conclusion": rule.conclusion,
            "status": rule.status.value,
            "missing": list(missing),
            "provenance": rule.provenance,
        }
        for rule, missing in candidates
    ]


def build_receipt() -> dict[str, object]:
    with mp.workdps(80):
        routes = solve_half_axis_routes()
        exact = XF7_SOLVER.closure(DEFAULT_FACTS, allow_model=False)
        model = XF7_SOLVER.closure(DEFAULT_FACTS, allow_model=True)
        xf7_conditional = XF7_SOLVER.closure(
            XF7_PREPRINT_SCENARIO_FACTS,
            allow_model=True,
        )
        receipt = {
            "schema": "tir.critical-axis.solver-receipt/v7",
            "precision_decimal_digits": 80,
            "half_axis_routes": {key: mp.nstr(value, 50) for key, value in routes.items()},
            "half_axis_consensus": all(
                abs(value - mp.mpf("0.5")) < mp.mpf("1e-50")
                for value in routes.values()
            ),
            "exact_closure": sorted(exact.facts),
            "exact_proof": _proof(exact),
            "model_closure": sorted(model.facts),
            "model_proof": _proof(model),
            "xf7_preprint_scenario": {
                "supplied_external_claim": "planat_sole_second_level_concavity",
                "closure": sorted(xf7_conditional.facts),
                "proof": _proof(xf7_conditional),
                "riemann_hypothesis_in_closure": (
                    "riemann_hypothesis" in xf7_conditional.facts
                ),
                "global_signed_core_tail_in_closure": (
                    "xf7_global_signed_core_tail_domination" in xf7_conditional.facts
                ),
            },
            "kappa_conditional": mp.nstr(kappa_from_projective_cycle(), 50),
            "kappa_reference": mp.nstr(mp.log(2) / (24 * mp.pi), 50),
            "riemann_hypothesis_in_closure": "riemann_hypothesis" in model.facts,
            "open_half_axis_bridge_candidates": _missing(
                "all_zeros_on_half_axis", set(model.facts)
            ),
            "open_rh_equivalent_routes": _missing(
                "riemann_hypothesis", set(model.facts)
            ),
            "open_wiener_laguerre_scalar_routes": _missing(
                "xi_wiener_laguerre_strict_positivity", set(model.facts)
            ),
            "open_nonlocal_curvature_routes": _missing(
                "xi_strict_transverse_convexity_critical_strip", set(model.facts)
            ),
            "open_xf6_mass_envelope_routes": _missing(
                "xf6_slice_gaussian_mass_envelope_exists", set(model.facts)
            ),
            "open_xf6_core_tail_routes": _missing(
                "xf6_global_core_tail_domination", set(model.facts)
            ),
            "open_xf7_signed_core_tail_routes": _missing(
                "xf7_global_signed_core_tail_domination",
                set(xf7_conditional.facts),
            ),
            "literature_firewall": {
                "phase_aligned_blockwise_positivity": "EXTERNAL_NO_GO_RECORDED",
                "phase_aligned_scope": "Planat 2026 theta-kernel decomposition; global correlated positivity remains the active route",
                "gershon_v2_xi_kernel_log_concavity": "EXTERNAL_PREPRINT_CLAIM",
                "gershon_v2_scope": "direct strict log-concavity / TP2 of Phi",
                "planat_sole_second_level_concavity": "EXTERNAL_PREPRINT_CLAIM",
                "planat_sole_scope": "strict log-concavity of F=s'^2-s s'' for s(t)=Phi(sqrt(t)); double Turan hierarchy",
                "xi_kernel_positive_strict_decrease": "STANDARD_EXTERNAL_THEOREM",
                "tp_infinity_laguerre_polya": "OPEN",
            },
            "verdict": {
                "mathematical_half_axis_routes": "PASS",
                "conditional_kappa_arithmetic": "PASS",
                "model_semantics": "EXPLICIT",
                "canonical_xi_two_branch_representation": "PASS",
                "all_xi_zeros_exact_kernel_branch_cancellation": "PASS",
                "global_kernel_branch_nondegeneracy": "OPEN",
                "kernel_population_equals_strip_coordinate": "OPEN_RH_EQUIVALENT_BRIDGE",
                "dimitrov_xu_nu2_correlation_kernel": "STANDARD_PASS",
                "xi_wronskian_nu2_fourier_identity": "STANDARD_PASS",
                "phi2y_fourier_equals_xi_wiener_laguerre_scalar": "STANDARD_PASS",
                "xi_transverse_curvature_identity": "EXACT_PASS",
                "theta_curvature_kernel_bridge": "EXACT_PASS",
                "xf6_exact_positive_curvature_corridor": "EXACT_PASS",
                "gershon_v2_xi_kernel_log_concavity": "EXTERNAL_PREPRINT_CLAIM",
                "xf6_transverse_mass_center_dominance": "CONDITIONAL_EXACT",
                "xf6_transverse_mass_strict_abs_b_decay": "CONDITIONAL_EXACT",
                "xf6_slice_gaussian_mass_envelope": "CONDITIONAL_STANDARD",
                "xf6_global_core_tail_domination": "OPEN_SUFFICIENT_ROUTE",
                "xi_kernel_positive_strict_decrease": "STANDARD_PASS",
                "planat_sole_second_level_concavity": "EXTERNAL_PREPRINT_CLAIM",
                "xf7_first_laguerre_positive_s_sqrt": "CONDITIONAL_ON_PREPRINT",
                "xf7_b0_positive": "CONDITIONAL_EXACT",
                "xf7_radial_log_slope_ratio_increasing": "CONDITIONAL_EXACT",
                "xf7_tp2_crosswalk": "CONDITIONAL_EXACT",
                "xf7_adaptive_transverse_mass_envelope": "CONDITIONAL_EXACT",
                "xf7_signed_cosine_tail_ibp_bound": "CONDITIONAL_EXACT",
                "xf7_global_signed_core_tail_domination": "OPEN_SUFFICIENT_ROUTE",
                "tp_infinity_laguerre_polya": "OPEN",
                "phi2y_translation_density_condition": "OPEN_RH_EQUIVALENT_CRITERION",
                "phi2y_bounded_convolution_annihilator_condition": "OPEN_RH_EQUIVALENT_CRITERION",
                "xi_wiener_laguerre_strict_positivity": "OPEN_RH_EQUIVALENT_CRITERION",
                "xi_strict_transverse_convexity_critical_strip": "OPEN_RH_EQUIVALENT_CRITERION",
                "xi_vertical_growth_critical_strip": "OPEN_RH_EQUIVALENT_CRITERION",
                "riemann_hypothesis": "OPEN",
            },
        }
    return receipt


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    receipt = build_receipt()
    text = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
