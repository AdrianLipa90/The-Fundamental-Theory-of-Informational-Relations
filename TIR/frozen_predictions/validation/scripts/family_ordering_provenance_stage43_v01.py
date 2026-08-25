#!/usr/bin/env python3
"""Stage 43 — provenance audit for an existing family-path ordering rule.

The gate checks two pre-existing TIR statements:
1. the formal Hamiltonian accumulates intention phase in ordered Collatz steps;
2. the canonical Euler-Berry freeze still lists the exact Collatz/twin-prime
   rhythm rho_s(k) as an open derivation debt.

No numerical rhythm ansatz is promoted by this stage.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[2]
FORMAL = REPO / "archive" / "v7.9" / "full" / "01_foundational_formal_notes" / "Hilbert_Kahler_Phase_Intention_Hamiltonian.tex"
FREEZE = REPO / "archive" / "v7.9" / "full" / "02_canonical_freezes_and_audits" / "metatime_eulerberry_freeze_v0_1" / "METATIME_EULERBERRY_FREEZE_v0_1.json"
REFERENCE_SIM = REPO / "archive" / "v7.9" / "full" / "01_foundational_formal_notes" / "phase_hamiltonian_english_derivations" / "scripts" / "collatz_phase_sim.py"
OUT = ROOT / "results"
OUT.mkdir(parents=True, exist_ok=True)


def main():
    formal = FORMAL.read_text(encoding="utf-8")
    freeze = json.loads(FREEZE.read_text(encoding="utf-8"))
    sim = REFERENCE_SIM.read_text(encoding="utf-8")

    ordered_sum_present = "\\Theta_{\\mathcal I}(K)=\\sum_{k=0}^{K-1}" in formal
    rhythm_debt = any("exact Collatz/twin-prime rhythm" in x for x in freeze.get("open_derivation_debts", []))
    reference_choice_declared = "The exact rhythm map is a model choice" in sim
    eta_default_present = "eta: float = 0.35" in sim

    passed = ordered_sum_present and rhythm_debt and reference_choice_declared and eta_default_present
    receipt = {
        "schema": "TIR_POLYGONAL_STAGE43_FAMILY_ORDERING_PROVENANCE_V0_1",
        "status": "STAGE_43_ORDERING_PRINCIPLE_FOUND__EXACT_WEIGHT_MAP_OPEN" if passed else "STAGE_43_AUDIT_FAIL",
        "ordered_collatz_accumulation_present": ordered_sum_present,
        "exact_rho_s_derivation_debt_present": rhythm_debt,
        "reference_simulation_declares_model_choice": reference_choice_declared,
        "reference_simulation_eta_default": 0.35 if eta_default_present else None,
        "eta_promoted_to_family_selector": False,
        "result": "TIR contains an ordered Collatz-step accumulation principle, while the exact rho_s(k) weighting remains an explicit derivation debt.",
        "admissible_next_step": "derive or freeze rho_s(k) independently before using Collatz ordering to select a quantitative SU(3)_F path",
        "uses_observed_CKM": False,
        "uses_observed_masses": False,
        "pass": passed,
    }
    path = OUT / "TIR_POLYGONAL_STAGE43_FAMILY_ORDERING_PROVENANCE_RECEIPT_V0_1.json"
    path.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    print(json.dumps(receipt, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
