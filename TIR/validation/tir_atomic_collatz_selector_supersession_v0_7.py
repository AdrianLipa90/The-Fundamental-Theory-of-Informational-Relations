#!/usr/bin/env python3
"""Regression gate for fail-closed supersession of the stale Collatz selector candidate."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
OPERATOR = ROOT / "TIR/integration/tir_half_foundation_v0_6_0/atomic_assignment_operator.py"
OLD_RECEIPT = ROOT / "TIR/integration/tir_half_foundation_v0_6_0/ATOMIC_CANONIZATION_RECEIPT.json"
NEW_RECEIPT = ROOT / "TIR/integration/tir_half_foundation_v0_6_0/ATOMIC_CANONIZATION_SUPERSESSION_V0_7.json"
STAGE22 = ROOT / "TIR/frozen_predictions/validation/TIR_POLYGONAL_EXCITATION_STAGE22_SEED_PRECEDENCE_V0_1.md"
THEOREM = ROOT / "TIR/foundations/TIR_COEFFICIENT_TRANSITION_SELECTOR_PRECEDENCE_FALSIFICATION_V0_2.md"


def load_operator():
    name = "tir_atomic_assignment_operator"
    spec = importlib.util.spec_from_file_location(name, OPERATOR)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load atomic assignment operator")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    try:
        spec.loader.exec_module(module)
    except Exception:
        sys.modules.pop(name, None)
        raise
    return module


old_receipt = json.loads(OLD_RECEIPT.read_text(encoding="utf-8"))
new_receipt = json.loads(NEW_RECEIPT.read_text(encoding="utf-8"))
stage22 = STAGE22.read_text(encoding="utf-8")
theorem = THEOREM.read_text(encoding="utf-8")
module = load_operator()
result = module.retrospective_collatz_candidate()

active = result["active_stage22_precedence"]
legacy = result["legacy_precedence_observation"]

checks = {
    "old_receipt_remains_historical_v06": old_receipt.get("schema") == "tir-half/atomic-assignment-canonization/v0.6",
    "old_receipt_not_silently_reclassified": old_receipt.get("not_promoted", {}).get("collatz_destination_curvature_magnitude") == "RETROSPECTIVE_CANDIDATE_UNDERDETERMINED",
    "superseding_receipt_present": new_receipt.get("schema") == "tir-half/atomic-assignment-canonization-supersession/v0.7",
    "supersession_keeps_selector_open": new_receipt.get("current_classifications", {}).get("coefficient_transition_parent_selector") == "OPEN",
    "stage22_active_order_present": all(token in stage22 for token in ("(3,5)\\to1", "(5,7)\\to2", "(11,13)\\to3")),
    "falsification_theorem_present": "EXACT_ACTIVE_PRECEDENCE_FALSIFICATION" in theorem,
    "falsification_magnitude_statement_present": "fails on both successive transitions under active precedence" in theorem,
    "runtime_status_fail_closed": result.get("status") == "FALSIFIED_UNDER_ACTIVE_STAGE22_PRECEDENCE_DO_NOT_PROMOTE",
    "runtime_selector_not_promoted": result.get("selector_promoted") is False,
    "runtime_points_to_superseding_theorem": result.get("superseding_theorem") == "TIR_COEFFICIENT_TRANSITION_SELECTOR_PRECEDENCE_FALSIFICATION_V0_2",
    "legacy_values_preserved_for_provenance": legacy["e_to_mu"] == {"ell_source": 2, "ell_destination": 9, "predicted_sign": 1, "candidate_abs_c": 8} and legacy["mu_to_tau"] == {"ell_source": 9, "ell_destination": 8, "predicted_sign": -1, "candidate_abs_c": 7},
    "active_e_to_mu_is_2_to_8": active["e_to_mu"] == {"ell_source": 2, "ell_destination": 8, "predicted_sign": 1, "candidate_abs_c": 7},
    "active_mu_to_tau_is_8_to_9": active["mu_to_tau"] == {"ell_source": 8, "ell_destination": 9, "predicted_sign": 1, "candidate_abs_c": 8},
    "active_candidate_differs_from_legacy": active["e_to_mu"]["candidate_abs_c"] != legacy["e_to_mu"]["candidate_abs_c"] and active["mu_to_tau"]["candidate_abs_c"] != legacy["mu_to_tau"]["candidate_abs_c"],
}

passed = all(checks.values())
payload = {
    "schema": "TIR_ATOMIC_COLLATZ_SELECTOR_SUPERSESSION_V0_7",
    "technical_status": "PASS" if passed else "FAIL",
    "runtime_status": result.get("status"),
    "selector_promoted": result.get("selector_promoted"),
    "active_stage22_precedence": active,
    "legacy_precedence_observation": legacy,
    "claim_scope": {
        "stale_runtime_candidate": "FAIL_CLOSED",
        "historical_receipt": "PRESERVED_UNCHANGED",
        "stopping_length_selector": "FALSIFIED_UNDER_ACTIVE_PRECEDENCE",
        "coefficient_transition_parent_selector": "OPEN",
        "physical_binding": "NOT_CLAIMED",
    },
    "checks": checks,
}
print(json.dumps(payload, indent=2, sort_keys=True))
raise SystemExit(0 if passed else 1)
