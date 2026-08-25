#!/usr/bin/env python3
"""Stage 48: exact Collatz O/E branch words to the Stage 47 common seed."""
from __future__ import annotations

import hashlib
import json

SEEDS = [15, 35, 143]
TARGET = 35


def collatz_step(n: int):
    if n % 2:
        return "O", 3 * n + 1
    return "E", n // 2


def word_to_target(n: int, target: int, max_steps: int = 10000):
    word = []
    values = [n]
    for _ in range(max_steps + 1):
        if n == target:
            return "".join(word), values
        branch, n = collatz_step(n)
        word.append(branch)
        values.append(n)
    raise RuntimeError("target not reached")


def main() -> None:
    rows = []
    for seed in SEEDS:
        word, values = word_to_target(seed, TARGET)
        rows.append({
            "seed": seed,
            "target": TARGET,
            "word": word,
            "length": len(word),
            "odd_branch_count": word.count("O"),
            "even_branch_count": word.count("E"),
            "sha256": hashlib.sha256(word.encode("ascii")).hexdigest(),
            "terminal_value": values[-1],
        })

    checks = {
        "w1_exact": rows[0]["word"] == "OEOE",
        "w1_length_4": rows[0]["length"] == 4,
        "w2_empty": rows[1]["word"] == "" and rows[1]["length"] == 0,
        "w3_length_90": rows[2]["length"] == 90,
        "w3_odd_even_counts": rows[2]["odd_branch_count"] == 34 and rows[2]["even_branch_count"] == 56,
        "all_reach_35": all(r["terminal_value"] == TARGET for r in rows),
    }

    result = {
        "schema": "TIR_POLYGONAL_STAGE48_COLLATZ_BRANCH_WORD_V0_1",
        "alphabet": {"O": "3n+1 on odd n", "E": "n/2 on even n"},
        "target": TARGET,
        "rows": rows,
        "checks": checks,
        "pass": all(checks.values()),
        "branch_to_operator_assignment_selected": False,
        "exact_rhythm_selected": False,
        "CKM_input_used": False,
        "mass_input_used": False,
    }
    print(json.dumps(result, indent=2))
    if not result["pass"]:
        raise SystemExit("Stage 48 audit failed")


if __name__ == "__main__":
    main()
