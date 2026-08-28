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
    "COMMON_PRIMITIVE_CORE",
    "TIR_SPATIAL_GEOMETRY",
    "TIR_STANDARD_MODEL_BRANCH",
    "TIME_SCALAR_TENSOR_BRANCH",
    "SPACETIME_CLOSURE",
    "MATTER_FIELD_SPACETIME",
)

EDGES = (
    ("ZERO", "POINT"),
    ("POINT", "FIRST_DISTINCTION"),
    ("FIRST_DISTINCTION", "TWO_POLES"),
    ("TWO_POLES", "HALF_SEAM"),
    ("HALF_SEAM", "LN2"),
    ("LN2", "COMMON_PRIMITIVE_CORE"),
    ("COMMON_PRIMITIVE_CORE", "TIR_SPATIAL_GEOMETRY"),
    ("COMMON_PRIMITIVE_CORE", "TIR_STANDARD_MODEL_BRANCH"),
    ("COMMON_PRIMITIVE_CORE", "TIME_SCALAR_TENSOR_BRANCH"),
    ("TIR_SPATIAL_GEOMETRY", "SPACETIME_CLOSURE"),
    ("TIME_SCALAR_TENSOR_BRANCH", "SPACETIME_CLOSURE"),
    ("SPACETIME_CLOSURE", "MATTER_FIELD_SPACETIME"),
    ("TIR_STANDARD_MODEL_BRANCH", "MATTER_FIELD_SPACETIME"),
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


def parents(target: str) -> set[str]:
    return {src for src, dst in EDGES if dst == target}


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
    core = "COMMON_PRIMITIVE_CORE"
    branch_children = {
        "TIR_SPATIAL_GEOMETRY",
        "TIR_STANDARD_MODEL_BRANCH",
        "TIME_SCALAR_TENSOR_BRANCH",
    }
    core_ancestors = ancestors(core)
    sibling_parent_pass = all((core, branch) in EDGES for branch in branch_children)
    branch_not_core_ancestor = all(branch not in core_ancestors for branch in branch_children)
    no_temporal_circularity = "TIME_SCALAR_TENSOR_BRANCH" not in core_ancestors
    tir_spatial_ownership_pass = "TIR_SPATIAL_GEOMETRY" in branch_children
    spacetime_join_parent_pass = parents("SPACETIME_CLOSURE") == {
        "TIR_SPATIAL_GEOMETRY",
        "TIME_SCALAR_TENSOR_BRANCH",
    }
    matter_join_parent_pass = parents("MATTER_FIELD_SPACETIME") == {
        "SPACETIME_CLOSURE",
        "TIR_STANDARD_MODEL_BRANCH",
    }
    dag_pass = topological_pass()
    passed = all(
        (
            sibling_parent_pass,
            branch_not_core_ancestor,
            no_temporal_circularity,
            tir_spatial_ownership_pass,
            spacetime_join_parent_pass,
            matter_join_parent_pass,
            dag_pass,
        )
    )
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
            "COMMON_PRIMITIVE_CORE",
        ],
        "core_children": sorted(branch_children),
        "spacetime_join_parents": sorted(parents("SPACETIME_CLOSURE")),
        "matter_join_parents": sorted(parents("MATTER_FIELD_SPACETIME")),
        "core_ancestors": sorted(core_ancestors),
        "dag_pass": dag_pass,
        "sibling_parent_pass": sibling_parent_pass,
        "branch_not_core_ancestor": branch_not_core_ancestor,
        "no_temporal_circularity": no_temporal_circularity,
        "tir_spatial_ownership_pass": tir_spatial_ownership_pass,
        "spacetime_join_parent_pass": spacetime_join_parent_pass,
        "matter_join_parent_pass": matter_join_parent_pass,
        "technical_status": "PASS" if passed else "FAIL",
    }


def main() -> None:
    receipt = build_receipt()
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if receipt["technical_status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
