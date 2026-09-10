#!/usr/bin/env python3
"""Fail-closed identifiability audit for the TIR transition-parent selector.

This validator proves only that the current coarse routing/orientation inputs do
not yet select a unique magnitude-parent packet. It must not promote a selector
formula from retrospective charged-lepton examples.
"""
from __future__ import annotations

import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ATOMIC_OPERATOR = ROOT / "TIR/integration/tir_half_foundation_v0_6_0/atomic_assignment_operator.py"
CANON_RECEIPT = ROOT / "TIR/integration/tir_half_foundation_v0_6_0/ATOMIC_CANONIZATION_RECEIPT.json"
LEGACY_RELEASE = ROOT / "TIR/monograph/chapters/ch06_generation_release.tex"
LINEAGE = ROOT / "TIR/integration/tir_half_foundation_v0_5_0/coefficient_lineage.py"

L3 = 7
L4 = 2
L5 = 5

P_E_MU = ("0", "X5", "X4", "X3_PLUS_I")
P_MU_TAU = ("0", "F", "I", "X3")


def atomic_ast_facts() -> dict[str, object]:
    tree = ast.parse(ATOMIC_OPERATOR.read_text(encoding="utf-8"))
    state_fields: set[str] = set()
    orientation_attrs: set[str] = set()
    orientation_literal_strings: set[str] = set()

    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name == "AtomicGeometryState":
            for stmt in node.body:
                if isinstance(stmt, ast.AnnAssign) and isinstance(stmt.target, ast.Name):
                    state_fields.add(stmt.target.id)
        if isinstance(node, ast.FunctionDef) and node.name == "evaluate_orientation":
            for sub in ast.walk(node):
                if (
                    isinstance(sub, ast.Attribute)
                    and isinstance(sub.value, ast.Name)
                    and sub.value.id == "state"
                ):
                    orientation_attrs.add(sub.attr)
                if isinstance(sub, ast.Constant) and isinstance(sub.value, str):
                    orientation_literal_strings.add(sub.value)

    transition_fields = {
        "seed_from",
        "seed_to",
        "collatz_stop_from",
        "collatz_stop_to",
    }
    consumed_transition_fields = transition_fields & orientation_attrs
    selector_words = ("parent", "magnitude", "packet", "selector")
    selector_literal = any(
        any(word in value.lower() for word in selector_words)
        for value in orientation_literal_strings
    )

    return {
        "state_fields": sorted(state_fields),
        "orientation_state_attributes": sorted(orientation_attrs),
        "transition_sensitive_fields_declared": transition_fields.issubset(state_fields),
        "transition_sensitive_fields_consumed_by_orientation": sorted(consumed_transition_fields),
        "orientation_returns_selector_literal": selector_literal,
    }


def main() -> int:
    facts = atomic_ast_facts()
    receipt = json.loads(CANON_RECEIPT.read_text(encoding="utf-8"))
    legacy = LEGACY_RELEASE.read_text(encoding="utf-8")
    lineage = LINEAGE.read_text(encoding="utf-8")

    not_promoted = receipt.get("not_promoted", {})
    false_legacy_equality_present = "5 = L_4 + L_3" in legacy
    later_l5_correction_present = "L_5 = 5" in legacy

    checks = {
        "transition_sensitive_fields_exist_in_schema": bool(facts["transition_sensitive_fields_declared"]),
        "current_orientation_evaluator_does_not_consume_transition_fields": facts["transition_sensitive_fields_consumed_by_orientation"] == [],
        "current_orientation_evaluator_does_not_emit_parent_selector": not bool(facts["orientation_returns_selector_literal"]),
        "release_parent_packets_are_distinct": P_E_MU != P_MU_TAU,
        "release_parent_packets_share_same_slot_arity": len(P_E_MU) == len(P_MU_TAU) == 4,
        "both_release_packets_have_no_half_base_insertion": P_E_MU[0] == P_MU_TAU[0] == "0",
        "lineage_keeps_semantic_assignment_noncanonical": lineage.count('"PROJECT_MODEL_ASSIGNMENT"') >= 3,
        "canon_receipt_keeps_collatz_curvature_rule_underdetermined": not_promoted.get("collatz_destination_curvature_magnitude") == "RETROSPECTIVE_CANDIDATE_UNDERDETERMINED",
        "canon_receipt_keeps_gradient_binding_open": not_promoted.get("gradient_to_TIR_slot_binding") == "OPEN_PROSPECTIVE_VALIDATION_REQUIRED",
        "legacy_false_L4_plus_L3_equals_5_statement_is_present_as_history": false_legacy_equality_present,
        "legacy_false_equality_is_actually_false": L4 + L3 == 9 and L4 + L3 != 5,
        "legacy_passage_later_uses_L5_equals_5": later_l5_correction_present and L5 == 5,
    }

    status = "PASS" if all(checks.values()) else "FAIL"
    out = {
        "schema": "TIR_COEFFICIENT_TRANSITION_SELECTOR_IDENTIFIABILITY_V0_1",
        "status": status,
        "scope": "CURRENT_INPUT_NONIDENTIFIABILITY_ONLY",
        "atomic_operator_facts": facts,
        "release_parent_packets": {
            "E_TO_MU_RELEASE": list(P_E_MU),
            "MU_TO_TAU_RELEASE": list(P_MU_TAU),
        },
        "checks": checks,
        "role_only_selector_sufficient": False,
        "orientation_only_selector_sufficient": False,
        "current_orientation_evaluator_selects_magnitude_parent": False,
        "additional_transition_sensitive_invariant_required": True,
        "transition_parent_selector_closed": False,
        "retrospective_collatz_pattern_promoted": False,
        "physical_claim": False,
        "next_gate": "CONSTRUCT_AND_VALIDATE_COEFFICIENT_TRANSITION_PARENT_SELECTOR_SIGMA",
    }
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
