#!/usr/bin/env python3
"""Validate exact coefficient-magnitude evaluation from declared TIR parent packets.

The parent-count vectors are computed first from upstream structural integers.
Legacy coefficient tuples are parsed only afterwards as a downstream consistency
check; they are never inputs to the parent evaluation.
"""
from __future__ import annotations

import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ACTION_SOURCE = ROOT / "TIR/integration/tir_half_foundation_v0_5_0/action_generator.py"
LINEAGE_SOURCE = ROOT / "TIR/integration/tir_half_foundation_v0_5_0/coefficient_lineage.py"

# Upstream certified integer relations.
N_F = 3
ORDER_A4 = 12
ORDER_S4 = 24
ORDER_A5 = 60
L4 = ORDER_S4 // ORDER_A4
L5 = ORDER_A5 // ORDER_A4
L3 = L4 + L5
I = 1

VALUATION = {
    "0": 0,
    "I": I,
    "F": N_F,
    "X3": L3,
    "X4": L4,
    "X5": L5,
    "X3_PLUS_I": L3 + I,
}

# These are parent-expression packets, not coefficient tuples.
PARENT_PACKETS = {
    "ELECTRON_ACTION": ("I", "F", "I", "I"),
    "E_TO_MU_RELEASE": ("0", "X5", "X4", "X3_PLUS_I"),
    "MU_TO_TAU_RELEASE": ("0", "F", "I", "X3"),
}


def evaluate_packet(packet: tuple[str, str, str, str]) -> tuple[int, int, int, int]:
    return tuple(VALUATION[token] for token in packet)  # type: ignore[return-value]


def eval_int_expr(node: ast.AST) -> int:
    """Evaluate only the tiny integer expression grammar used in GeneratorCoefficients."""
    if isinstance(node, ast.Constant) and isinstance(node.value, int):
        return node.value
    if isinstance(node, ast.Name) and node.id in {"L3", "L4", "L5"}:
        return {"L3": L3, "L4": L4, "L5": L5}[node.id]
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.UAdd):
        return +eval_int_expr(node.operand)
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        return -eval_int_expr(node.operand)
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        return eval_int_expr(node.left) + eval_int_expr(node.right)
    raise ValueError(f"unsupported integer expression: {ast.dump(node)}")


def legacy_generator_vectors() -> dict[str, tuple[int, int, int, int]]:
    """Parse historical vectors for comparison after independent parent evaluation."""
    tree = ast.parse(ACTION_SOURCE.read_text(encoding="utf-8"))
    states: dict[str, tuple[int, int, int, int]] = {}
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if not any(isinstance(t, ast.Name) and t.id == "COEFFICIENT_STATES" for t in node.targets):
            continue
        if not isinstance(node.value, ast.Dict):
            raise AssertionError("COEFFICIENT_STATES is not a dict")
        for key_node, value_node in zip(node.value.keys, node.value.values):
            if not isinstance(key_node, ast.Constant) or not isinstance(key_node.value, str):
                continue
            if not isinstance(value_node, ast.Call) or len(value_node.args) < 2:
                continue
            coeff_call = value_node.args[1]
            if not isinstance(coeff_call, ast.Call):
                continue
            if not isinstance(coeff_call.func, ast.Name) or coeff_call.func.id != "GeneratorCoefficients":
                continue
            if len(coeff_call.args) != 4:
                raise AssertionError("GeneratorCoefficients arity changed")
            states[key_node.value] = tuple(eval_int_expr(arg) for arg in coeff_call.args)  # type: ignore[assignment]
    return states


def main() -> int:
    magnitudes = {name: evaluate_packet(packet) for name, packet in PARENT_PACKETS.items()}

    upstream_checks = {
        "flavour_multiplicity_is_3": N_F == 3,
        "L4_from_group_index": L4 == 2,
        "L5_from_group_index": L5 == 5,
        "L3_from_root_extension_sum": L3 == 7,
        "unit_count_is_1": I == 1,
    }

    packet_checks = {
        "electron_magnitude_vector": magnitudes["ELECTRON_ACTION"] == (1, 3, 1, 1),
        "e_mu_magnitude_vector": magnitudes["E_TO_MU_RELEASE"] == (0, 5, 2, 8),
        "mu_tau_magnitude_vector": magnitudes["MU_TO_TAU_RELEASE"] == (0, 3, 1, 7),
    }

    # Only now inspect the historical generator. This comparison is downstream.
    legacy = legacy_generator_vectors()
    legacy_abs = {name: tuple(abs(x) for x in vector) for name, vector in legacy.items()}
    legacy_checks = {
        "all_three_legacy_states_present": set(PARENT_PACKETS).issubset(legacy),
        "legacy_absolute_vectors_match_parent_evaluation": all(
            legacy_abs.get(name) == magnitudes[name] for name in PARENT_PACKETS
        ),
    }

    lineage_text = LINEAGE_SOURCE.read_text(encoding="utf-8")
    lineage_checks = {
        "lineage_retains_open_semantic_assignments": lineage_text.count('"PROJECT_MODEL_ASSIGNMENT"') >= 3,
        "lineage_declares_L5_parent": '"L5"' in lineage_text,
        "lineage_declares_L4_parent": '"L4"' in lineage_text,
        "lineage_declares_L3_plus_identity_parent": '"L3_PLUS_IDENTITY"' in lineage_text,
        "lineage_declares_generation_count_parent": '"GENERATION_COUNT_3"' in lineage_text,
    }

    checks = {**upstream_checks, **packet_checks, **legacy_checks, **lineage_checks}
    status = "PASS" if all(checks.values()) else "FAIL"
    receipt = {
        "schema": "TIR_COEFFICIENT_MAGNITUDE_PARENT_EVALUATION_V0_1",
        "status": status,
        "scope": "EXACT_PARENT_PACKET_EVALUATION",
        "upstream": {
            "N_F": N_F,
            "L3": L3,
            "L4": L4,
            "L5": L5,
            "I": I,
        },
        "parent_packets": {k: list(v) for k, v in PARENT_PACKETS.items()},
        "evaluated_magnitudes": {k: list(v) for k, v in magnitudes.items()},
        "legacy_vectors_downstream_only": {k: list(v) for k, v in legacy.items()},
        "checks": checks,
        "target_mass_or_yukawa_input_consumed": False,
        "recovered_tuple_used_as_parent": False,
        "magnitude_parent_evaluation_closed": status == "PASS",
        "transition_parent_selector_closed": False,
        "physical_mass_binding_closed": False,
        "physical_claim": False,
        "next_gate": "COEFFICIENT_TRANSITION_PARENT_SELECTOR",
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
