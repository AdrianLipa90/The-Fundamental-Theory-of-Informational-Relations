#!/usr/bin/env python3
from __future__ import annotations
import json

EARLY_V05 = [
    ((3, 5), 0.44017743117972435, 1),
    ((11, 13), 0.4129797750528312, 2),
    ((5, 7), 0.34380299602647096, 3),
]

FULL_ACTION_V10 = [
    ((3, 5), 0.8471633855025916, 1),
    ((5, 7), 0.6088811663290957, 2),
    ((11, 13), 0.23926393244694075, 3),
]

ordered = sorted(FULL_ACTION_V10, key=lambda row: -row[1])
expected = [(3, 5), (5, 7), (11, 13)]
checks = {
    "three_unique_seeds": len({row[0] for row in FULL_ACTION_V10}) == 3,
    "strict_full_action_order": all(ordered[i][1] > ordered[i+1][1] for i in range(2)),
    "expected_v10_order": [row[0] for row in ordered] == expected,
    "generation_labels_match_order": [row[2] for row in ordered] == [1, 2, 3],
    "historical_order_preserved_as_distinct": [row[0] for row in EARLY_V05] != expected,
}
report = {
    "schema": "tir.polygonal.stage22.seed-precedence/v0.1",
    "status": "PASS" if all(checks.values()) else "FAIL",
    "active_order": [list(x) for x in expected],
    "full_action_values": {f"{p}-{q}": v for (p, q), v, _ in FULL_ACTION_V10},
    "checks": checks,
    "mass_input_used": False,
    "scope": "ordered seed-label basis",
}
print(json.dumps(report, indent=2, sort_keys=True))
raise SystemExit(0 if report["status"] == "PASS" else 1)
