#!/usr/bin/env python3
"""Method-status correction for the v10.2 sector-holonomy audit.

The numerical operator and fingerprint are unchanged.  This revision corrects
only the epistemic classification: the v10.2 formula was selected after review
of the v10.1 residual pattern, so it is a retrospective structural candidate,
not a prospective sealed test.  No continuous coefficient was fitted and no
particle-specific residual correction was inserted, but canonical promotion is
still forbidden until an independent prospective test is performed.
"""
from __future__ import annotations

import json
from pathlib import Path

import collatz_sector_holonomy_mass_audit_v10_2 as core

OUT = Path(__file__).resolve().parent / "results"


def main() -> None:
    """
    Run the audit benchmark and write the method-status correction report.
    
    The report records benchmark results, operator identity, methodological status,
    and restrictions on current promotion claims. It is written to the results
    directory and printed to standard output.
    """
    structural = core.structural_inputs()
    frozen = core.freeze_operator(structural)
    result = core.benchmark(frozen)

    payload = {
        "schema": "TIR_COLLATZ_SECTOR_HOLONOMY_MASS_AUDIT_V10_2R1",
        "supersedes_method_status_of": (
            "TIR_COLLATZ_SECTOR_HOLONOMY_MASS_AUDIT_V10_2"
        ),
        "numerical_operator_changed": False,
        "operator_trace_sha256": frozen["operator_trace_sha256"],
        "technical_status": "PASS",
        "methodological_status": (
            "RETROSPECTIVE_STRUCTURAL_CANDIDATE_NOT_PROSPECTIVE_TEST"
        ),
        "comparative_status": (
            "RETROSPECTIVE_SIGNAL_GLOBAL_ERROR_REDUCTION"
        ),
        "sector_relative_status": (
            "RETROSPECTIVE_SIGNAL_EXCLUDING_OPEN_UP_SECTOR_BASELINE"
        ),
        "physical_mass_spectrum_status": "FAIL_OPEN",
        "debt9_status": "OPEN_NOT_CLOSED",
        "canon_allowed": False,
        "current_promotion": "DENY_CURRENT",
        "mass_derivation_claimed": False,
        "method_history": {
            "formula_selected_after_v10_1_residual_review": True,
            "continuous_parameters_fitted": False,
            "particle_specific_residual_corrections": False,
            "prospective_validation_claimed": False,
            "independent_holdout_test_available": False,
            "promotion_eligible": False,
        },
        "benchmark": {
            "quarter_summary": result["quarter_summary"],
            "sector_summary": result["sector_summary"],
            "non_anchor_excluding_u_summary": result[
                "non_anchor_excluding_u_summary"
            ],
            "generation_order": result["generation_order"],
            "u_sector_offset": result["u_sector_offset"],
            "improved_slots": result["improved_slots"],
            "worsened_slots": result["worsened_slots"],
        },
        "next_allowed_claim": (
            "Use v10.2 only as a retrospective hypothesis generator. "
            "Freeze a new operator or independent observable before any "
            "further validation result is inspected."
        ),
    }

    OUT.mkdir(parents=True, exist_ok=True)
    output = OUT / "collatz_sector_holonomy_mass_audit_v10_2r1.json"
    output.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
