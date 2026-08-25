#!/usr/bin/env python3
"""Stage 46: exact low-complexity arithmetic multiplicity audit.

Frozen grammar:
- leaves: L3=7, L4=2, L5=5, repetition allowed;
- binary ops: +, -, *, /;
- at most three binary operations;
- exact Fraction arithmetic;
- lexical canonicalization of operand order for + and *.
"""
from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
import json
from pathlib import Path

VALUES = {"L3": Fraction(7), "L4": Fraction(2), "L5": Fraction(5)}
OPS = ("+", "-", "*", "/")
TARGETS = (4, 88, 90)
MAX_OPS = 3


@lru_cache(maxsize=None)
def generate(nops: int):
    if nops == 0:
        return frozenset((name, value) for name, value in VALUES.items())

    out = set()
    for left_ops in range(nops):
        right_ops = nops - 1 - left_ops
        for left_expr, left_val in generate(left_ops):
            for right_expr, right_val in generate(right_ops):
                for op in OPS:
                    if op in ("+", "*") and left_expr > right_expr:
                        continue
                    if op == "+":
                        value = left_val + right_val
                    elif op == "-":
                        value = left_val - right_val
                    elif op == "*":
                        value = left_val * right_val
                    else:
                        if right_val == 0:
                            continue
                        value = left_val / right_val
                    out.add((f"({left_expr}{op}{right_expr})", value))
    return frozenset(out)


def main() -> None:
    all_expr = []
    counts_by_nops = {}
    for nops in range(MAX_OPS + 1):
        layer = generate(nops)
        counts_by_nops[str(nops)] = len(layer)
        all_expr.extend((nops, expr, value) for expr, value in layer)

    hits = {}
    for target in TARGETS:
        rows = sorted(
            [(nops, expr) for nops, expr, value in all_expr if value == target],
            key=lambda x: (x[0], x[1]),
        )
        hits[str(target)] = [
            {"operation_count": nops, "expression": expr} for nops, expr in rows
        ]

    expected_88 = "(((L3*L3)-L5)*L4)"
    expected_90 = {
        "((L3+L4)*(L4*L5))",
        "(((L5*L5)-L3)*L5)",
        "(((L3+L4)*L5)*L4)",
        "(((L3+L4)*L4)*L5)",
        "((L3+L4)*(L5+L5))",
    }

    status = {
        "schema": "TIR_POLYGONAL_STAGE46_LOW_COMPLEXITY_DISTANCE_IDENTITY_V0_1",
        "constants": {"L3": 7, "L4": 2, "L5": 5},
        "targets": list(TARGETS),
        "max_binary_operations": MAX_OPS,
        "operators": list(OPS),
        "commutative_operand_order_canonicalized": True,
        "exact_rational_arithmetic": True,
        "expression_counts_by_operation_count": counts_by_nops,
        "hit_counts": {k: len(v) for k, v in hits.items()},
        "hits": hits,
        "checks": {
            "d12_nonunique": len(hits["4"]) > 1,
            "d13_unique_in_frozen_grammar": len(hits["88"]) == 1,
            "d13_expected_expression": len(hits["88"]) == 1
            and hits["88"][0]["expression"] == expected_88,
            "d23_five_tree_hits": len(hits["90"]) == 5,
            "d23_expected_tree_set": {x["expression"] for x in hits["90"]} == expected_90,
        },
        "physical_amplitude_claim": False,
        "distance_to_amplitude_rule_promoted": False,
    }
    status["pass"] = all(status["checks"].values())

    print(json.dumps(status, indent=2, sort_keys=True))
    if not status["pass"]:
        raise SystemExit("Stage 46 audit failed")


if __name__ == "__main__":
    main()
