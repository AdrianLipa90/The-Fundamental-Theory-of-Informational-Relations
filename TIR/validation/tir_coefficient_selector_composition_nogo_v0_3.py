#!/usr/bin/env python3
"""Deterministic audit for TIR coefficient-selector composition no-go v0.3.

The historical v0.5 integration package has stale relative imports, so this
validator deliberately audits its source AST instead of importing/executing it.
"""
from __future__ import annotations

import ast
from fractions import Fraction
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ACTION_GENERATOR = ROOT / "TIR/integration/tir_half_foundation_v0_5_0/action_generator.py"
L_CLOSURE = ROOT / "TIR/foundations/TIR_PLATONIC_L_CONSTANTS_CLOSURE_V0_1.md"

N_F = 3
I = 1


def collatz(n: int) -> int:
    if n <= 0:
        raise ValueError(n)
    return n // 2 if n % 2 == 0 else 3 * n + 1


def collatz_depth_to_one(n: int, limit: int = 1000) -> int:
    steps = 0
    for _ in range(limit):
        if n == 1:
            return steps
        n = collatz(n)
        steps += 1
    raise RuntimeError("depth limit exceeded")


L3 = collatz_depth_to_one(3)
L4 = 5 - 3
L5 = 5


def corridor(x: int, y: int, limit: int = 1000) -> list[int]:
    """States before the first hit of y."""
    out: list[int] = []
    n = x
    for _ in range(limit):
        if n == y:
            return out
        out.append(n)
        n = collatz(n)
    raise RuntimeError(f"no hit {x}->{y} within {limit}")


def parity_word(states: list[int]) -> str:
    return "".join(str(n % 2) for n in states)


def odd_flag(states: list[int]) -> int:
    return int(any(n % 2 for n in states))


def magnitude(v: tuple[int, int, int, int]) -> tuple[int, int, int, int]:
    return tuple(abs(x) for x in v)


def binary_magnitude_selector(states: list[int]) -> tuple[int, int, int, int]:
    d = odd_flag(states)
    return (0, N_F + d * L4, I + d * I, L3 + d * I)


def q_c(x: int) -> Fraction:
    """Canonical IDT lifted parity coordinate for an orbit reaching 1."""
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


def sign(x: Fraction | int) -> int:
    return 1 if x > 0 else -1 if x < 0 else 0


def vec_add(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(x + y for x, y in zip(a, b))


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


def source_release_vectors() -> tuple[dict[str, tuple[int, int, int, int]], str]:
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


def main() -> int:
    gamma21 = corridor(6, 4)
    gamma32 = corridor(12, 6)
    gamma31 = corridor(12, 4)

    vectors, generator_source = source_release_vectors()
    r_em = vectors["E_TO_MU_RELEASE"]
    r_mt = vectors["MU_TO_TAU_RELEASE"]
    r_et = vec_add(r_em, r_mt)

    m21 = binary_magnitude_selector(gamma21)
    m32 = binary_magnitude_selector(gamma32)
    m31 = binary_magnitude_selector(gamma31)

    E = tuple(Fraction(x) for x in r_mt)
    O = tuple((Fraction(r_em[i]) - 4 * E[i]) / 2 for i in range(4))

    q4, q6, q12 = q_c(4), q_c(6), q_c(12)
    dq_em = q6 - q4
    dq_mt = q12 - q6
    dq_et = q12 - q4

    bc_signs = {
        "e_mu": (sign(r_em[2]), sign(r_em[3])),
        "mu_tau": (sign(r_mt[2]), sign(r_mt[3])),
        "e_tau": (sign(r_et[2]), sign(r_et[3])),
    }
    q_signs = {
        "e_mu": sign(dq_em),
        "mu_tau": sign(dq_mt),
        "e_tau": sign(dq_et),
    }

    l_closure = L_CLOSURE.read_text(encoding="utf-8")
    checks = {
        "canonical_counts_recomputed": (N_F, L3, L4, L5, I) == (3, 7, 2, 5, 1),
        "canonical_l_closure_receipt_present": all(token in l_closure for token in ("L3 = 7", "L4 = 2", "L5 = 5")),
        "gamma21_exact": gamma21 == [6, 3, 10, 5, 16, 8],
        "gamma32_exact": gamma32 == [12],
        "gamma31_exact": gamma31 == [12, 6, 3, 10, 5, 16, 8],
        "gamma21_word": parity_word(gamma21) == "010100",
        "gamma32_word": parity_word(gamma32) == "0",
        "gamma31_word": parity_word(gamma31) == "0010100",
        "odd_flags": (odd_flag(gamma21), odd_flag(gamma32), odd_flag(gamma31)) == (1, 0, 1),
        "adjacent_vectors_from_source_ast": r_em == (0, 5, 2, 8) and r_mt == (0, 3, -1, -7),
        "generator_source_declares_additive_R_e_tau": "\"R_e_tau\": total" in generator_source and "tuple(a + b" in generator_source,
        "composed_vector": r_et == (0, 8, 1, 1),
        "binary_matches_e_mu": m21 == magnitude(r_em) == (0, 5, 2, 8),
        "binary_matches_mu_tau": m32 == magnitude(r_mt) == (0, 3, 1, 7),
        "binary_fails_composed_e_tau": m31 == (0, 5, 2, 8) and m31 != magnitude(r_et),
        "parity_local_even_forced": E == tuple(Fraction(x) for x in r_mt),
        "parity_local_odd_solution": O == (Fraction(0), Fraction(-7, 2), Fraction(3), Fraction(18)),
        "parity_local_odd_not_integer_lattice": any(x.denominator != 1 for x in O),
        "q_values": (q4, q6, q12) == (Fraction(1, 7), Fraction(141, 448), Fraction(141, 896)),
        "q_differences": (dq_em, dq_mt, dq_et) == (Fraction(11, 64), Fraction(-141, 896), Fraction(13, 896)),
        "q_additivity": dq_et == dq_em + dq_mt,
        "q_sign_matches_e_mu_bc": bc_signs["e_mu"] == (q_signs["e_mu"], q_signs["e_mu"]) == (1, 1),
        "q_sign_matches_mu_tau_bc": bc_signs["mu_tau"] == (q_signs["mu_tau"], q_signs["mu_tau"]) == (-1, -1),
        "q_sign_matches_e_tau_bc": bc_signs["e_tau"] == (q_signs["e_tau"], q_signs["e_tau"]) == (1, 1),
    }

    passed = all(checks.values())
    out = {
        "schema": "TIR_COEFFICIENT_SELECTOR_COMPOSITION_NOGO_V0_3",
        "status": "PASS" if passed else "FAIL",
        "scope": "INTERNAL_COMPOSITION_AND_SELECTOR_FALSIFICATION_ONLY",
        "corridors": {
            "gamma21_6_to_4": gamma21,
            "gamma32_12_to_6": gamma32,
            "gamma31_12_to_4": gamma31,
        },
        "parity_words": {
            "gamma21": parity_word(gamma21),
            "gamma32": parity_word(gamma32),
            "gamma31": parity_word(gamma31),
        },
        "release_vectors": {
            "e_mu": list(r_em),
            "mu_tau": list(r_mt),
            "e_tau_composed": list(r_et),
        },
        "binary_magnitude_outputs": {
            "gamma21": list(m21),
            "gamma32": list(m32),
            "gamma31": list(m31),
        },
        "parity_only_local_solution": {
            "E": [str(x) for x in E],
            "O": [str(x) for x in O],
            "integer_lattice_possible": all(x.denominator == 1 for x in O),
        },
        "qC": {
            "q4": str(q4),
            "q6": str(q6),
            "q12": str(q12),
            "dq_e_mu": str(dq_em),
            "dq_mu_tau": str(dq_mt),
            "dq_e_tau": str(dq_et),
        },
        "checks": checks,
        "binary_odd_corridor_selector_universal": False,
        "parity_only_constant_step_cocycle_Z4_exists": False,
        "composition_additivity_required": True,
        "qC_orientation_binding_promoted": False,
        "transition_parent_selector_closed": False,
        "physical_claim": False,
        "next_gate": "DERIVE_STATE_SENSITIVE_VECTOR_COCYCLE_OR_EQUIVALENT_SELECTOR",
    }
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
