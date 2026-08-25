#!/usr/bin/env python3
"""Stage 45 — provenance audit for a distance/path-cost to amplitude map.

The audit checks the archived v5.0 White-Thread derivability no-go and the
subsequent v5.1 quadratic amplitude candidate.  It does not evaluate CKM or
invent a new kernel.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[2]
V50 = REPO / "archive" / "v7.9" / "full" / "50_whitethread_wij_lepton_gate_derivability_v5_0" / "METATIME_SM_WHITETHREAD_WIJ_LEPTON_GATE_DERIVABILITY_v5_0.md"
V51 = REPO / "archive" / "v7.9" / "full" / "51_whitethread_quadratic_amplitude_map_v5_1" / "scripts" / "whitethread_quadratic_amplitude_map_v5_1.py"
OUT = ROOT / "results"
OUT.mkdir(parents=True, exist_ok=True)


def main():
    v50 = V50.read_text(encoding="utf-8")
    v51 = V51.read_text(encoding="utf-8")

    checks = {
        "v50_open_holonomy_phase_present": "W_ij = exp(i ∫ A)" in v50,
        "v50_amplitude_map_undefined": "bounded but not explicitly derived" in v50,
        "v50_no_go_promotion": "NO_GO_FOR_STRONG_CHARGED_LEPTON_F_PROMOTION" in v50,
        "v51_quadratic_candidate_present": "S_ij = (Delta tau_v2_preference_quanta)^2 / (2 * L3 * DeltaGeneration)" in v51,
        "v51_exponential_gate_present": "F_ij = exp(-OIB * S_ij)" in v51,
        "v51_candidate_after_audit": "candidate derived after v5.0 derivability audit" in v51,
        "v51_allpair_fail": "PARTIAL_DERIVATION_CANDIDATE_ROOT_GATES_PASS_ALLPAIR_FAIL" in v51,
        "v51_canon_denied": "'canon_allowed': False" in v51 and "'current_promotion': 'DENY_CURRENT'" in v51,
    }
    passed = all(checks.values())

    receipt = {
        "schema": "TIR_POLYGONAL_STAGE45_DISTANCE_AMPLITUDE_PROVENANCE_V0_1",
        "status": "STAGE_45_CANONICAL_DISTANCE_TO_AMPLITUDE_MAP_NOT_FOUND__PROVENANCE_NOGO_PASS" if passed else "STAGE_45_AUDIT_FAIL",
        "checks": checks,
        "canonical_rule_available_for_stage44_distance_matrix": False,
        "v5_0_result": "phase holonomy available; amplitude map f explicitly underived",
        "v5_1_result": "quadratic exponential amplitude is a later non-canon candidate and fails the full all-pair diagnostic",
        "stage44_substitution_into_v5_1_allowed_as_existing_law": False,
        "inverse_distance_promoted": False,
        "exponential_distance_promoted": False,
        "next_methodological_action": "freeze any candidate distance kernels as separate hypotheses before comparison; do not select a kernel by CKM fit",
        "uses_observed_CKM": False,
        "uses_observed_masses": False,
        "pass": passed,
    }
    path = OUT / "TIR_POLYGONAL_STAGE45_DISTANCE_AMPLITUDE_PROVENANCE_RECEIPT_V0_1.json"
    path.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    print(json.dumps(receipt, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
