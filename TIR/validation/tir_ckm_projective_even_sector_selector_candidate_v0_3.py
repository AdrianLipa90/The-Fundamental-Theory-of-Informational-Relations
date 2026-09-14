#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path

import tir_600cell_mckay_e8_closure_candidate_v0_3 as mckay

ROOT = Path(__file__).resolve().parents[2]
STAGE33 = ROOT / "TIR/frozen_predictions/validation/TIR_POLYGONAL_EXCITATION_STAGE33_MCKAY_ENDPOINT_CKM_DICTIONARY_V0_1.md"
STAGE32_SCRIPT = ROOT / "TIR/frozen_predictions/validation/scripts/ckm_provenance_stage32_v01.py"
STAGE37 = ROOT / "TIR/frozen_predictions/validation/TIR_POLYGONAL_EXCITATION_STAGE37_COMMON_FAMILY_AXIS_NOGO_V0_1.md"

KAPPA = math.log(2.0) / (24.0 * math.pi)


def jarlskog(s12: float, s23: float, s13: float, cdelta: float) -> float:
    c12 = math.sqrt(1.0 - s12 * s12)
    c23 = math.sqrt(1.0 - s23 * s23)
    c13 = math.sqrt(1.0 - s13 * s13)
    sdelta = math.sqrt(1.0 - cdelta * cdelta)
    return s12 * s23 * s13 * c12 * c23 * c13 * c13 * sdelta


def main() -> int:
    restrictions = mckay.sym_power_restrictions(7)
    reducible = [ell for ell in range(8) if sum(restrictions[ell].values()) > 1]
    assert reducible and reducible[0] == 6
    first_branch = reducible[0]

    # Central -I acts as (-1)^ell on Sym^ell(C^2); projective sectors are even.
    projective_nontrivial = [ell for ell in range(1, first_branch + 1) if ell % 2 == 0]
    assert projective_nontrivial == [2, 4, 6]
    dims = [mckay.representation_dimension(restrictions[ell]) for ell in projective_nontrivial]
    assert dims == [3, 5, 7]

    q = mckay.IRREP_DIMS[mckay.validate()["fundamental_irrep"]]
    assert q == 2

    d1, d2, d3 = dims
    w12 = Fraction(q, d1 * d1)
    bridge = Fraction(q, d2)
    w23 = Fraction(q, d3 * d3)
    a = Fraction(q, d3)
    w13 = w12 * bridge * w23

    assert w12 == Fraction(2, 9)
    assert bridge == Fraction(2, 5)
    assert a == Fraction(2, 7)
    assert w23 == Fraction(2, 49)
    assert w23 == a * a / q
    assert w13 == Fraction(8, 2205)

    # Conditional selector uniqueness: through the first branching threshold
    # there is exactly one ordered nontrivial center-even triple.
    all_even_subsets = []
    evens = [ell for ell in range(1, first_branch + 1) if ell % 2 == 0]
    if len(evens) == 3:
        all_even_subsets.append(tuple(evens))
    assert all_even_subsets == [(2, 4, 6)]

    base_s12 = float(w12)
    s23 = float(w23)
    s13 = float(w13)
    cdelta = float(bridge)
    base_J = jarlskog(base_s12, s23, s13, cdelta)

    refined_s12 = base_s12 + float(a) * KAPPA
    refined_J = jarlskog(refined_s12, s23, s13, cdelta)
    assert math.isclose(base_J, 2.9381740008251395e-05, rel_tol=0.0, abs_tol=2e-18)
    assert math.isclose(refined_J, 2.9710657666807235e-05, rel_tol=0.0, abs_tol=2e-18)

    stage33 = STAGE33.read_text(encoding="utf-8")
    stage32_script = STAGE32_SCRIPT.read_text(encoding="utf-8")
    stage37 = STAGE37.read_text(encoding="utf-8")

    provenance_checks = {
        "stage33_ratio_reconstruction_retrospective": "STAGE_33_ENDPOINT_RATIO_RECONSTRUCTION_PASS__FUNCTIONAL_SELECTION_RETROSPECTIVE" in stage33,
        "stage33_has_a_2_over_7": r"a=\frac{s}{n_-}=\frac27" in stage33,
        "stage33_has_b_2_over_9": r"b=\frac{s}{n_+}=\frac29" in stage33,
        "stage33_has_c_2_over_5": r"c=\frac{s}{N_+}=\frac25" in stage33,
        "stage32_records_lambda_refinement_after_comparison": "r1 changes lambda after the earlier comparison" in stage32_script,
        "stage37_common_axis_no_go_retained": "STAGE_37_COMMON_FAMILY_AXIS_NOGO_PASS" in stage37,
        "stage37_requires_noncommuting_pair": r"[H_u,H_d]\neq0" in stage37,
    }
    assert all(provenance_checks.values())

    checks = {
        "first_reducible_mckay_sector_is_ell6": first_branch == 6,
        "projective_nontrivial_sectors_through_branch_are_2_4_6": projective_nontrivial == [2, 4, 6],
        "projective_sector_dimensions_are_3_5_7": dims == [3, 5, 7],
        "fundamental_doublet_dimension_is_2": q == 2,
        "left_outer_coefficient_fraction_is_2_over_9": w12 == Fraction(2, 9),
        "middle_representation_bridge_is_2_over_5": bridge == Fraction(2, 5),
        "right_outer_representation_fraction_is_2_over_7": a == Fraction(2, 7),
        "right_outer_coefficient_fraction_is_2_over_49": w23 == Fraction(2, 49),
        "historical_half_factor_is_rep_to_coefficient_conversion": w23 == a * a / q,
        "A2_composite_weight_is_8_over_2205": w13 == Fraction(8, 2205),
        "base_selector_is_unique_under_declared_rule": all_even_subsets == [(2, 4, 6)],
        "base_jarlskog_reproduced": math.isclose(base_J, 2.9381740008251395e-05, abs_tol=2e-18, rel_tol=0.0),
        "refined_jarlskog_reproduced_but_not_promoted": math.isclose(refined_J, 2.9710657666807235e-05, abs_tol=2e-18, rel_tol=0.0),
        **provenance_checks,
    }

    status = "PASS" if all(checks.values()) else "FAIL"
    out = {
        "schema": "TIR_CKM_PROJECTIVE_EVEN_SECTOR_SELECTOR_CANDIDATE_V0_3",
        "status": status,
        "epistemic_status": "CONDITIONAL_BASE_SELECTOR_CLOSURE__EXACT_A2_COMPOSITE_ROOT__KAPPA_REFINEMENT_OPEN_POSTDICTIVE",
        "physical_promotion": False,
        "predictive_status": "POSTDICTIVE_BASE_FORM_RECONSTRUCTION_NOT_NEW_PREDICTION",
        "selector_rule": {
            "projective_condition": "ell even because center -I acts as (-1)^ell on Sym^ell(C^2)",
            "branch_boundary": first_branch,
            "ordered_sectors": projective_nontrivial,
            "representation_dimensions": dims,
            "fundamental_dimension": q,
            "simple_root_rule": "same normalized coefficient-space doublet fraction q/d_outer^2 on each exclusive outer endpoint",
            "middle_bridge_rule": "q/d_middle",
            "composite_root_rule": "A2 bracket [E12,E23]=E13 with middle bridge contraction",
        },
        "weights": {
            "s12_base": str(w12),
            "s23": str(w23),
            "middle_bridge_cos_delta": str(bridge),
            "right_outer_amplitude_a": str(a),
            "s13": str(w13),
        },
        "numerics": {
            "kappa": KAPPA,
            "s12_base": base_s12,
            "s12_refined_current": refined_s12,
            "J_base": base_J,
            "J_refined_current": refined_J,
            "J_refinement_relative_change": refined_J / base_J - 1.0,
        },
        "checks": checks,
        "closed_conditional": {
            "base_rational_simple_root_weights": True,
            "middle_bridge": True,
            "composite_root_weight": True,
        },
        "open": {
            "derive_selector_rule_from_deeper_dynamics": True,
            "derive_additive_a_kappa_operator": True,
            "prospective_physical_validation": True,
            "clean_noncommuting_complex_family_pair_from_600cell_only": True,
        },
    }
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
