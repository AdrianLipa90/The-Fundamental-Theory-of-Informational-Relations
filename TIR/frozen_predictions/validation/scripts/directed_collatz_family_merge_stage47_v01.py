#!/usr/bin/env python3
"""Stage 47: exact directed Collatz reachability and pairwise merge audit."""
from __future__ import annotations

import json
from math import inf

SEEDS = [15, 35, 143]


def collatz(n: int) -> int:
    return n // 2 if n % 2 == 0 else 3 * n + 1


def orbit(n: int, max_steps: int = 10000):
    out = [n]
    for _ in range(max_steps):
        if out[-1] == 1:
            return out
        out.append(collatz(out[-1]))
    raise RuntimeError("orbit did not reach 1 within max_steps")


def directed_time(a: int, b: int):
    oa = orbit(a)
    try:
        return oa.index(b)
    except ValueError:
        return None


def first_merge(a: int, b: int):
    oa = orbit(a)
    ob = orbit(b)
    pos_b = {x: j for j, x in enumerate(ob)}
    candidates = [(i + pos_b[x], i, pos_b[x], x) for i, x in enumerate(oa) if x in pos_b]
    return min(candidates)


def main() -> None:
    T = [[directed_time(a, b) for b in SEEDS] for a in SEEDS]
    merges = {}
    for i in range(3):
        for j in range(i + 1, 3):
            total, si, sj, node = first_merge(SEEDS[i], SEEDS[j])
            merges[f"{i+1}{j+1}"] = {
                "seed_i": SEEDS[i],
                "seed_j": SEEDS[j],
                "merge_node": node,
                "steps_i": si,
                "steps_j": sj,
                "total_cost": total,
            }

    checks = {
        "15_reaches_35_in_4": T[0][1] == 4,
        "143_reaches_35_in_90": T[2][1] == 90,
        "35_is_unique_common_reachable_seed": T[0][1] is not None and T[2][1] is not None
        and T[1][0] is None and T[1][2] is None,
        "merge_12_is_35": merges["12"]["merge_node"] == 35 and merges["12"]["total_cost"] == 4,
        "merge_13_is_46": merges["13"]["merge_node"] == 46 and merges["13"]["total_cost"] == 88,
        "merge_23_is_35": merges["23"]["merge_node"] == 35 and merges["23"]["total_cost"] == 90,
        "46_reaches_35_in_3": directed_time(46, 35) == 3,
    }

    result = {
        "schema": "TIR_POLYGONAL_STAGE47_DIRECTED_COLLATZ_FAMILY_MERGE_V0_1",
        "seeds": SEEDS,
        "directed_reachability_steps": T,
        "pairwise_first_merges": merges,
        "checks": checks,
        "pass": all(checks.values()),
        "physical_generation_preference_claim": False,
        "distance_to_amplitude_rule_promoted": False,
    }
    print(json.dumps(result, indent=2))
    if not result["pass"]:
        raise SystemExit("Stage 47 audit failed")


if __name__ == "__main__":
    main()
