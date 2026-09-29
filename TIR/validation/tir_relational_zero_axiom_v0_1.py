#!/usr/bin/env python3
"""Deterministic validator for the TIR relational-zero foundation."""

from __future__ import annotations

import json
import math


def binary_entropy(p: float) -> float:
    q = 1.0 - p
    return -(p * math.log(p) + q * math.log(q))


def main() -> int:
    zero_support: tuple[()] = ()
    zero_relations: tuple[()] = ()

    checks = {
        "relational_zero_support_empty": len(zero_support) == 0,
        "relational_zero_relations_empty": len(zero_relations) == 0,
        "relational_zero_contains_no_object": not zero_support,
        "minimal_nonempty_support_cardinality": len(("p",)) == 1,
    }

    # A nontrivial partition must have at least two nonempty blocks.
    candidate_block_counts = [n for n in range(0, 8) if n > 1]
    checks["minimal_nontrivial_distinction_is_binary"] = min(candidate_block_counts) == 2

    w_n = w_s = 0.5
    checks["exchange_invariant_normalization"] = (
        math.isclose(w_n + w_s, 1.0, rel_tol=0.0, abs_tol=0.0)
        and math.isclose(w_n, w_s, rel_tol=0.0, abs_tol=0.0)
    )
    checks["half_fixed_point"] = math.isclose(1.0 - 0.5, 0.5, rel_tol=0.0, abs_tol=0.0)
    checks["binary_entropy_ln2"] = math.isclose(
        binary_entropy(0.5), math.log(2.0), rel_tol=0.0, abs_tol=1e-15
    )

    status = "PASS" if all(checks.values()) else "FAIL"
    receipt = {
        "schema": "TIR_RELATIONAL_ZERO_AXIOM_VALIDATION_V0_1",
        "status": status,
        "checks": checks,
        "claim_boundary": {
            "relational_zero": "DEFINITIONAL",
            "minimal_support": "SET_THEORETIC",
            "minimal_binary_distinction": "DEFINITIONAL_SET_THEORETIC",
            "half_and_ln2": "EXACT",
            "quantum_lift": "NOT_TESTED_HERE_CONDITIONAL_POSTULATE",
            "physical_claim": False,
        },
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
