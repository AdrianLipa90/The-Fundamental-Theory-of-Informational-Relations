#!/usr/bin/env python3
"""Validate the frozen Collatz–Poincare branch-rhythm candidate v0.1.

This gate validates mathematical admissibility and provenance only.
It does not promote rho_geo to the unique physical Hamiltonian rhythm.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
FREEZE = ROOT / "frozen_predictions" / "TIR_COLLATZ_POINCARE_BRANCH_RHYTHM_FREEZE_V0_1.md"
STAGE48 = (
    ROOT
    / "frozen_predictions"
    / "validation"
    / "TIR_POLYGONAL_EXCITATION_STAGE48_COLLATZ_BRANCH_WORD_OPERATOR_INTERFACE_V0_1.md"
)
STAGE49 = (
    ROOT
    / "frozen_predictions"
    / "validation"
    / "TIR_POLYGONAL_EXCITATION_STAGE49_COLLATZ_MOBIUS_POINCARE_LIFT_V0_1.md"
)
REFERENCE_SIM = (
    REPO
    / "archive"
    / "v7.9"
    / "full"
    / "01_foundational_formal_notes"
    / "phase_hamiltonian_english_derivations"
    / "scripts"
    / "collatz_phase_sim.py"
)
OUT = ROOT / "validation" / "results"
OUT.mkdir(parents=True, exist_ok=True)

TOL = 1.0e-12


def main() -> None:
    freeze = FREEZE.read_text(encoding="utf-8")
    stage48 = STAGE48.read_text(encoding="utf-8")
    stage49 = STAGE49.read_text(encoding="utf-8")
    sim = REFERENCE_SIM.read_text(encoding="utf-8")

    tr_e = 3.0 / math.sqrt(2.0)
    tr_o = 4.0 / math.sqrt(3.0)
    ell_e = 2.0 * math.acosh(tr_e / 2.0)
    ell_o = 2.0 * math.acosh(tr_o / 2.0)

    rho_e = math.log(2.0)
    rho_o = math.log(3.0)
    sigma_e = math.log(0.5)
    sigma_o = math.log(3.0)

    w1_sum = 2.0 * rho_e + 2.0 * rho_o
    w1_exact = math.log(36.0)

    w3_sum = 56.0 * rho_e + 34.0 * rho_o
    w3_exact = math.log((2.0 ** 56) * (3.0 ** 34))

    checks = {
        "freeze_status_present": (
            "COLLATZ_POINCARE_BRANCH_RHYTHM_CANDIDATE_FROZEN_PREVALIDATION"
            in freeze
        ),
        "stage49_even_translation_length_ln2": abs(ell_e - rho_e) < TOL,
        "stage49_odd_translation_length_ln3": abs(ell_o - rho_o) < TOL,
        "rho_positive": rho_e > 0.0 and rho_o > 0.0,
        "signed_even_factorization": abs(sigma_e + rho_e) < TOL,
        "signed_odd_factorization": abs(sigma_o - rho_o) < TOL,
        "stage48_w1_counts_present": (
            "w_1=\\texttt{OEOE}" in stage48
            and "odd-step count `2`, even-step count `2`" in stage48
        ),
        "stage48_w3_counts_present": (
            "length `90`, odd-step count `34`, even-step count `56`"
            in stage48
        ),
        "w1_additive_rhythm": abs(w1_sum - w1_exact) < TOL,
        "w3_additive_rhythm": abs(w3_sum - w3_exact) < 1.0e-10,
        "reference_rhythm_declares_model_choice": (
            "The exact rhythm map is a model choice" in sim
        ),
        "reference_formal_requirement_only_positive": (
            "rho_s(k) > 0" in sim
        ),
        "freeze_excludes_target_inputs": all(
            token in freeze
            for token in (
                "CKM entries or phase",
                "PMNS entries",
                "fermion masses",
                "reference eta=0.35",
                "retrospective observable tuning",
            )
        ),
        "physical_uniqueness_not_claimed": (
            "physical rhythm uniqueness: NOT CLAIMED" in freeze
        ),
        "branch_family_operator_remains_open": (
            "branch -> family operator: OPEN" in freeze
        ),
        "stage49_source_tokens_present": (
            "STAGE_49_COLLATZ_MOBIUS_POINCARE_LIFT_PASS" in stage49
            and "\\operatorname{tr}(\\widehat M_E)=\\frac3{\\sqrt2}>2"
            in stage49
            and "\\operatorname{tr}(\\widehat M_O)=\\frac4{\\sqrt3}>2"
            in stage49
        ),
    }

    passed = all(checks.values())
    receipt = {
        "schema": "TIR_COLLATZ_POINCARE_BRANCH_RHYTHM_RECEIPT_V0_1",
        "status": (
            "PASS_CANDIDATE_MATHEMATICAL_AND_PROVENANCE_VALIDATION__PHYSICAL_RHYTHM_NOT_PROMOTED"
            if passed
            else "FAIL"
        ),
        "candidate_status": "FROZEN_PREVALIDATION",
        "rho_E": rho_e,
        "rho_O": rho_o,
        "rho_E_exact": "ln(2)",
        "rho_O_exact": "ln(3)",
        "sigma_E_exact": "-ln(2)",
        "sigma_O_exact": "+ln(3)",
        "w1_rhythm": w1_sum,
        "w1_exact": "ln(36)",
        "w3_rhythm": w3_sum,
        "w3_exact": "56*ln(2)+34*ln(3)",
        "uses_observed_CKM": False,
        "uses_observed_PMNS": False,
        "uses_observed_masses": False,
        "uses_fitted_coefficients": False,
        "physical_rhythm_promoted": False,
        "branch_to_family_operator_status": "OPEN",
        "checks": checks,
    }

    path = OUT / "TIR_COLLATZ_POINCARE_BRANCH_RHYTHM_RECEIPT_V0_1.json"
    path.write_text(json.dumps(receipt, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
