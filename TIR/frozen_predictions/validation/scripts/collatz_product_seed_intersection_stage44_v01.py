#!/usr/bin/env python3
"""Stage 44 — exact Collatz product-seed orbit-intersection geometry.

Uses the pre-existing foundational scalar-seed convention n0=p(p+2) for the
ordered twin-prime family labels (3,5), (5,7), (11,13).  No rhythm ansatz,
continuous parameter, CKM value, or mass is used.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results"
OUT.mkdir(parents=True, exist_ok=True)

PAIRS = [(3, 5), (5, 7), (11, 13)]
SCALAR_SEEDS = [p * q for p, q in PAIRS]


def collatz(n: int) -> int:
    return n // 2 if n % 2 == 0 else 3 * n + 1


def orbit(n: int):
    values = [n]
    while n != 1:
        n = collatz(n)
        values.append(n)
    return values


def meeting(a, b):
    oa, ob = orbit(a), orbit(b)
    ia = {v: k for k, v in enumerate(oa)}
    ib = {v: k for k, v in enumerate(ob)}
    common = set(ia) & set(ib)
    # Canonical earliest joint meeting by minimum total directed step count;
    # max-step and node value only break exact ties.
    node = min(common, key=lambda v: (ia[v] + ib[v], max(ia[v], ib[v]), v))
    union = set(oa) | set(ob)
    return {
        "meeting_node": node,
        "steps_from_a": ia[node],
        "steps_from_b": ib[node],
        "total_meeting_steps": ia[node] + ib[node],
        "common_node_count": len(common),
        "orbit_union_node_count": len(union),
        "orbit_jaccard": len(common) / len(union),
    }


def main():
    orbits = [orbit(n) for n in SCALAR_SEEDS]
    pairs = {
        "1_2": meeting(SCALAR_SEEDS[0], SCALAR_SEEDS[1]),
        "1_3": meeting(SCALAR_SEEDS[0], SCALAR_SEEDS[2]),
        "2_3": meeting(SCALAR_SEEDS[1], SCALAR_SEEDS[2]),
    }
    distances = {k: v["total_meeting_steps"] for k, v in pairs.items()}
    hierarchy_pass = distances["1_2"] < distances["1_3"] and distances["1_2"] < distances["2_3"]

    receipt = {
        "schema": "TIR_POLYGONAL_STAGE44_COLLATZ_PRODUCT_SEED_INTERSECTION_V0_1",
        "status": "STAGE_44_COLLATZ_PRODUCT_SEED_INTERSECTION_PASS" if hierarchy_pass else "STAGE_44_FAIL",
        "ordered_twin_prime_pairs": [list(x) for x in PAIRS],
        "scalar_seed_rule": "n0=p*(p+2)",
        "scalar_seeds": SCALAR_SEEDS,
        "stopping_lengths": [len(o) - 1 for o in orbits],
        "pair_meetings": pairs,
        "meeting_distance_matrix": [
            [0, distances["1_2"], distances["1_3"]],
            [distances["1_2"], 0, distances["2_3"]],
            [distances["1_3"], distances["2_3"], 0],
        ],
        "distance_hierarchy": "d12 << d13 ~= d23",
        "ratio_d13_over_d12": distances["1_3"] / distances["1_2"],
        "ratio_d23_over_d12": distances["2_3"] / distances["1_2"],
        "uses_rhythm_eta": False,
        "uses_observed_CKM": False,
        "uses_observed_masses": False,
        "uses_fitted_coefficients": False,
        "pass": hierarchy_pass,
    }
    path = OUT / "TIR_POLYGONAL_STAGE44_COLLATZ_PRODUCT_SEED_INTERSECTION_RECEIPT_V0_1.json"
    path.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    print(json.dumps(receipt, indent=2))
    if not hierarchy_pass:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
