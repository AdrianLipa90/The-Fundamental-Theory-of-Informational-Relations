#!/usr/bin/env python3
"""Deterministic architecture audit for the TIR causal bridge from zero."""
from __future__ import annotations

import json

NODES = (
    "ZERO",
    "POINT",
    "FIRST_DISTINCTION",
    "TWO_POLES",
    "HALF_SEAM",
    "LN2",
    "QUANTUM_PHASE_GEOMETRY_CORE",
    "STANDARD_MODEL_BRANCH",
    "TIME_BRANCH",
    "SPACE_BRANCH",
)

EDGES = (
    ("ZERO", "POINT"),
    ("POINT", "FIRST_DISTINCTION"),
    ("FIRST_DISTINCTION", "TWO_POLES"),
    ("TWO_POLES", "HALF_SEAM"),
    ("HALF_SEAM", "LN2"),
    ("LN2", "QUANTUM_PHASE_GEOMETRY_CORE"),
    ("QUANTUM_PHASE_GEOMETRY_CORE", "STANDARD_MODEL_BRANCH"),
    ("QUANTUM_PHASE_GEOMETRY_CORE", "TIME_BRANCH"),
    ("QUANTUM_PHASE_GEOMETRY_CORE", "SPACE_BRANCH"),
)


def ancestors(target: str) -> set[str]:
    rev: dict[str, set[str]] = {node: set() for node in NODES}
    for src, dst in EDGES:
        rev[dst].add(src)
    seen: set[str] = set()
    frontier = list(rev[target])
    while frontier:
        node = frontier.pop()
        if node in seen:
            continue
        seen.add(node)
        frontier.extend(rev[node] - seen)
    return seen


def topological_pass() -> bool:
    indegree = {node: 0 for node in NODES}
    adjacency = {node: [] for node in NODES}
    for src, dst in EDGES:
        adjacency[src].append(dst)
        indegree[dst] += 1
    queue = [node for node, degree in indegree.items() if degree == 0]
    visited = 0
    while queue:
        node = queue.pop()
        visited += 1
        for dst in adjacency[node]:
            indegree[dst] -= 1
            if indegree[dst] == 0:
                queue.append(dst)
    return visited == len(NODES)


def build_receipt() -> dict[str, object]:
    core = "QUANTUM_PHASE_GEOMETRY_CORE"
    branches = ("STANDARD_MODEL_BRANCH", "TIME_BRANCH", "SPACE_BRANCH")
    core_ancestors = ancestors(core)
    sibling_parent_pass = all((core, branch) in EDGES for branch in branches)
    branch_not_core_ancestor = all(branch not in core_ancestors for branch in branches)
    no_temporal_circularity = "TIME_BRANCH" not in core_ancestors
    dag_pass = topological_pass()
    passed = sibling_parent_pass and branch_not_core_ancestor and no_temporal_circularity and dag_pass
    return {
        "schema": "TIR_CAUSAL_BRIDGE_FROM_ZERO_V0_1",
        "causal_relation": "strict_structural_dependency_precedes_temporal_order",
        "core_path": [
            "ZERO",
            "POINT",
            "FIRST_DISTINCTION",
            "TWO_POLES",
            "HALF_SEAM",
            "LN2",
            "QUANTUM_PHASE_GEOMETRY_CORE",
        ],
        "sibling_branches": list(branches),
        "core_ancestors": sorted(core_ancestors),
        "dag_pass": dag_pass,
        "sibling_parent_pass": sibling_parent_pass,
        "branch_not_core_ancestor": branch_not_core_ancestor,
        "no_temporal_circularity": no_temporal_circularity,
        "technical_status": "PASS" if passed else "FAIL",
    }


def main() -> None:
    receipt = build_receipt()
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if receipt["technical_status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
