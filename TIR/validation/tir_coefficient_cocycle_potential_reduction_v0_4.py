#!/usr/bin/env python3
"""Deterministic audit for TIR coefficient cocycle/potential reduction v0.4.

The historical v0.5 integration package has stale relative imports.  We source-
audit its coefficient dictionary rather than importing/executing that package.
The SU(3)-perfectness statement is carried as an explicit standard-theorem
dependency; this validator does not pretend to numerically prove a Lie-group
structure theorem.
"""
from __future__ import annotations

import ast
from fractions import Fraction
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ACTION_GENERATOR = ROOT / "TIR/integration/tir_half_foundation_v0_5_0/action_generator.py"
STAGE24 = ROOT / "TIR/frozen_predictions/validation/TIR_POLYGONAL_EXCITATION_STAGE24_TIR_SEED_CHIRALITY_E8_INTERTWINER_V0_1.md"
PARENT_EVAL = ROOT / "TIR/foundations/TIR_COEFFICIENT_MAGNITUDE_PARENT_EVALUATION_V0_1.md"
THEOREM = ROOT / "TIR/foundations/TIR_COEFFICIENT_COCYCLE_POTENTIAL_REDUCTION_V0_4.md"


def collatz(n: int) -> int:
    if n <= 0:
        raise ValueError(n)
    return n // 2 if n % 2 == 0 else 3 * n + 1


def collatz_depth_to_one(n: int, limit: int = 1000) -> int:
    for k in range(limit + 1):
        if n == 1:
            return k
        n = collatz(n)
    raise RuntimeError("depth limit exceeded")


L3 = collatz_depth_to_one(3)
L4 = 5 - 3
L5 = 5
N_F = 3
I = 1


def eval_int(node: ast.AST, env: dict[str, int]) -> int:
    if isinstance(node, ast.Constant) and isinstance(node.value, int):
        return int(node.value)
    if isinstance(node, ast.Name) and node.id in env:
        return env[node.id]
    if isinstance(node, ast.UnaryOp):
        value = eval_int(node.operand, env)
        if isinstance(node.op, ast.UAdd):
            return value
        if isinstance(node.op, ast.USub):
            return -value
    if isinstance(node, ast.BinOp):
        left = eval_int(node.left, env)
        right = eval_int(node.right, env)
        if isinstance(node.op, ast.Add):
            return left + right
        if isinstance(node.op, ast.Sub):
            return left - right
        if isinstance(node.op, ast.Mult):
            return left * right
    raise AssertionError(f"unsupported integer expression: {ast.dump(node)}")


def source_vectors() -> tuple[dict[str, tuple[int, int, int, int]], str]:
    source = ACTION_GENERATOR.read_text(encoding="utf-8")
    tree = ast.parse(source)
    env = {"L3": L3, "L4": L4, "L5": L5}
    vectors: dict[str, tuple[int, int, int, int]] = {}
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if not any(isinstance(t, ast.Name) and t.id == "COEFFICIENT_STATES" for t in node.targets):
            continue
        if not isinstance(node.value, ast.Dict):
            raise AssertionError("COEFFICIENT_STATES is not a dict")
        for key_node, state_node in zip(node.value.keys, node.value.values):
            if not isinstance(key_node, ast.Constant) or not isinstance(key_node.value, str):
                continue
            if not isinstance(state_node, ast.Call) or len(state_node.args) < 2:
                continue
            coeff_node = state_node.args[1]
            if not isinstance(coeff_node, ast.Call) or len(coeff_node.args) != 4:
                continue
            vectors[key_node.value] = tuple(eval_int(arg, env) for arg in coeff_node.args)
        break
    return vectors, source


def add(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(x + y for x, y in zip(a, b))


def sub(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(x - y for x, y in zip(a, b))


def neg(a: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(-x for x in a)


def q_c(x: int) -> Fraction:
    bits: list[int] = []
    n = x
    for _ in range(1000):
        if n == 1:
            length = len(bits)
            prefix = sum(Fraction(bit, 2 ** (k + 1)) for k, bit in enumerate(bits))
            return prefix + Fraction(4, 7 * (2 ** length))
        bits.append(n % 2)
        n = collatz(n)
    raise RuntimeError(f"orbit did not reach 1: {x}")


def sign(x: int | Fraction) -> int:
    return 1 if x > 0 else -1 if x < 0 else 0


def main() -> int:
    vectors, generator_source = source_vectors()
    r12 = vectors["E_TO_MU_RELEASE"]
    r23 = vectors["MU_TO_TAU_RELEASE"]
    r13 = add(r12, r23)
    r31 = neg(r13)
    zero4 = (0, 0, 0, 0)

    K = {
        "s1": zero4,
        "s2": r12,
        "s3": r13,
    }

    q1, q2, q3 = q_c(4), q_c(6), q_c(12)
    dq12 = q2 - q1
    dq23 = q3 - q2
    dq31 = q1 - q3

    valuation = {
        "0": 0,
        "I": I,
        "X4": L4,
        "F": N_F,
        "X5": L5,
        "X3": L3,
        "X3_PLUS_I": L3 + I,
    }
    inverse_valuation = {value: key for key, value in valuation.items()}

    parent_packets_from_magnitudes = {}
    for edge_name, edge in {"R12": r12, "R23": r23, "R31": r31}.items():
        abs_values = [abs(x) for x in edge]
        parent_packets_from_magnitudes[edge_name] = [inverse_valuation.get(x) for x in abs_values]

    ab_det = r12[1] * r23[2] - r23[1] * r12[2]

    stage24 = STAGE24.read_text(encoding="utf-8")
    parent_eval = PARENT_EVAL.read_text(encoding="utf-8")
    theorem = THEOREM.read_text(encoding="utf-8")

    checks = {
        "canonical_counts": (N_F, L3, L4, L5, I) == (3, 7, 2, 5, 1),
        "stage24_cycle_declared": all(token in stage24 for token in (
            "P_s|s_1\\rangle=|s_2\\rangle",
            "P_s|s_2\\rangle=|s_3\\rangle",
            "P_s|s_3\\rangle=|s_1\\rangle",
        )),
        "stage24_keeps_collatz_dynamics_separate": "Dynamical Collatz transition status is tracked separately" in stage24,
        "source_adjacent_vectors": r12 == (0, 5, 2, 8) and r23 == (0, 3, -1, -7),
        "source_additive_identity_present": "\"R_e_tau\": total" in generator_source and "tuple(a + b" in generator_source,
        "r13_exact": r13 == (0, 8, 1, 1),
        "r31_forced": r31 == (0, -8, -1, -1),
        "cycle_sum_zero": add(add(r12, r23), r31) == zero4,
        "K_edge_12": sub(K["s2"], K["s1"]) == r12,
        "K_edge_23": sub(K["s3"], K["s2"]) == r23,
        "K_edge_31": sub(K["s1"], K["s3"]) == r31,
        "parent_alphabet_present": all(token in parent_eval for token in ("0,I,F,X_3,X_4,X_5,X_3+I", "nu(X_3+I)")),
        "current_parent_valuation_injective": len(set(valuation.values())) == len(valuation),
        "all_closed_cycle_magnitudes_in_parent_alphabet": all(
            abs(x) in inverse_valuation for edge in (r12, r23, r31) for x in edge
        ),
        "q_values": (q1, q2, q3) == (Fraction(1, 7), Fraction(141, 448), Fraction(141, 896)),
        "q_edges": (dq12, dq23, dq31) == (Fraction(11, 64), Fraction(-141, 896), Fraction(-13, 896)),
        "q_cycle_sum_zero": dq12 + dq23 + dq31 == 0,
        "q_sign_matches_R12_b_c": (sign(dq12), sign(r12[2]), sign(r12[3])) == (1, 1, 1),
        "q_sign_matches_R23_b_c": (sign(dq23), sign(r23[2]), sign(r23[3])) == (-1, -1, -1),
        "q_sign_matches_R31_b_c": (sign(dq31), sign(r31[2]), sign(r31[3])) == (-1, -1, -1),
        "q_sign_not_global_a_slot_rule": sign(dq23) != sign(r23[1]),
        "scalar_linear_map_ab_projection_noncollinear": ab_det == -11 and ab_det != 0,
        "su3_perfectness_explicitly_typed_standard_theorem": "IMPOSSIBLE_BY_STANDARD_PERFECT_GROUP_THEOREM" in theorem,
        "endpoint_holonomy_no_go_not_claimed_as_numeric_proof": "standard-theorem dependency" in theorem,
        "selector_stays_open": "COEFFICIENT_TRANSITION_PARENT_SELECTOR = OPEN" in theorem,
    }

    passed = all(checks.values())
    out = {
        "schema": "TIR_COEFFICIENT_COCYCLE_POTENTIAL_REDUCTION_V0_4",
        "status": "PASS" if passed else "FAIL",
        "scope": "INTERNAL_COCYCLE_POTENTIAL_ARCHITECTURE_ONLY",
        "release_edges": {
            "R12": list(r12),
            "R23": list(r23),
            "R13": list(r13),
            "R31_cycle_closure": list(r31),
        },
        "vertex_potential_gauge_K_s1_zero": {k: list(v) for k, v in K.items()},
        "parent_valuation": valuation,
        "parent_packets_from_closed_cycle_magnitudes": parent_packets_from_magnitudes,
        "qC": {
            "q1": str(q1),
            "q2": str(q2),
            "q3": str(q3),
            "dq12": str(dq12),
            "dq23": str(dq23),
            "dq31": str(dq31),
        },
        "scalar_linear_map_ab_determinant": ab_det,
        "standard_theorem_dependencies": {
            "SU3_is_perfect": True,
            "role": "STANDARD_LIE_GROUP_THEOREM_NOT_NUMERICALLY_REPROVED_HERE",
            "consequence": "ANY_GROUP_HOMOMORPHISM_SU3_TO_ABELIAN_Z4_IS_TRIVIAL",
        },
        "checks": checks,
        "coefficient_cycle_is_exact_Z4_coboundary": True,
        "parent_valuation_injective_on_current_alphabet": True,
        "IDT_phase_cycle_is_exact_scalar_coboundary": True,
        "fixed_linear_q_to_full_coefficient_vector_exists": False,
        "endpoint_SU3_homomorphic_nonzero_Z4_selector_exists": False,
        "coefficient_free_K_derived": False,
        "transition_parent_selector_closed": False,
        "physical_claim": False,
        "next_gate": "DERIVE_COEFFICIENT_FREE_VERTEX_POTENTIAL_OR_PATH_LOCAL_INTEGER_COCHAIN",
    }
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
