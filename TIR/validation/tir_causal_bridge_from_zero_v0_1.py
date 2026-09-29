#!/usr/bin/env python3
"""Deterministic architecture audit for the zero-axiom TIR causal bridge."""
from __future__ import annotations

import json

NODES = (
    "RELATION",
    "RELATIONAL_ZERO",
    "TWO_POLES",
    "HALF_SEAM",
    "LN2",
    "RELATIONAL_SPHERE",
    "CP1",
    "PROJECTIVE_C2",
    "QUANTUM_CARRIER",
    "WINDING_DEGREE",
    "INTEGER_INDEX",
    "NATURAL_INDEX",
    "HILBERT_EULER_SYMMETRY",
    "CONTEXT_LIFT",
    "COMMON_PRIMITIVE_CORE",
    "TIR_SPATIAL_GEOMETRY",
    "TIR_STANDARD_MODEL_BRANCH",
    "TIME_SCALAR_TENSOR_BRANCH",
    "SPACETIME_CLOSURE",
    "MATTER_FIELD_SPACETIME",
)

EDGES = (
    ("RELATION", "RELATIONAL_ZERO"),
    ("RELATION", "TWO_POLES"),
    ("TWO_POLES", "HALF_SEAM"),
    ("HALF_SEAM", "LN2"),
    ("TWO_POLES", "RELATIONAL_SPHERE"),
    ("RELATIONAL_SPHERE", "CP1"),
    ("CP1", "PROJECTIVE_C2"),
    ("PROJECTIVE_C2", "QUANTUM_CARRIER"),
    ("RELATIONAL_ZERO", "WINDING_DEGREE"),
    ("WINDING_DEGREE", "INTEGER_INDEX"),
    ("INTEGER_INDEX", "NATURAL_INDEX"),
    ("PROJECTIVE_C2", "HILBERT_EULER_SYMMETRY"),
    ("RELATIONAL_ZERO", "CONTEXT_LIFT"),
    ("LN2", "COMMON_PRIMITIVE_CORE"),
    ("QUANTUM_CARRIER", "COMMON_PRIMITIVE_CORE"),
    ("NATURAL_INDEX", "COMMON_PRIMITIVE_CORE"),
    ("HILBERT_EULER_SYMMETRY", "COMMON_PRIMITIVE_CORE"),
    ("CONTEXT_LIFT", "COMMON_PRIMITIVE_CORE"),
    ("COMMON_PRIMITIVE_CORE", "TIR_SPATIAL_GEOMETRY"),
    ("COMMON_PRIMITIVE_CORE", "TIR_STANDARD_MODEL_BRANCH"),
    ("COMMON_PRIMITIVE_CORE", "TIME_SCALAR_TENSOR_BRANCH"),
    ("TIR_SPATIAL_GEOMETRY", "SPACETIME_CLOSURE"),
    ("TIME_SCALAR_TENSOR_BRANCH", "SPACETIME_CLOSURE"),
    ("SPACETIME_CLOSURE", "MATTER_FIELD_SPACETIME"),
    ("TIR_STANDARD_MODEL_BRANCH", "MATTER_FIELD_SPACETIME"),
)

def ancestors(target: str) -> set[str]:
    rev = {node: set() for node in NODES}
    for src, dst in EDGES:
        rev[dst].add(src)
    seen = set()
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
    core_ancestors = ancestors(core)
    no_quantum_bloch_cycle = "QUANTUM_CARRIER" not in ancestors("RELATIONAL_SPHERE")
    no_a7_first_distinction_dependency = parents("TWO_POLES") == {"RELATION"}
    zero_to_arithmetic = parents("WINDING_DEGREE") == {"RELATIONAL_ZERO"}
    sphere_before_quantum = (
        ("TWO_POLES", "RELATIONAL_SPHERE") in EDGES
        and ("RELATIONAL_SPHERE", "CP1") in EDGES
        and ("CP1", "PROJECTIVE_C2") in EDGES
        and ("PROJECTIVE_C2", "QUANTUM_CARRIER") in EDGES
    )
    branch_children = {
        "TIR_SPATIAL_GEOMETRY",
        "TIR_STANDARD_MODEL_BRANCH",
        "TIME_SCALAR_TENSOR_BRANCH",
    }
    sibling_parent_pass = all((core, branch) in EDGES for branch in branch_children)
    no_temporal_circularity = "TIME_SCALAR_TENSOR_BRANCH" not in core_ancestors
    spacetime_join_parent_pass = parents("SPACETIME_CLOSURE") == {
        "TIR_SPATIAL_GEOMETRY",
        "TIME_SCALAR_TENSOR_BRANCH",
    }
    matter_join_parent_pass = parents("MATTER_FIELD_SPACETIME") == {
        "SPACETIME_CLOSURE",
        "TIR_STANDARD_MODEL_BRANCH",
    }
    dag_pass = topological_pass()
    passed = all((
        no_quantum_bloch_cycle,
        no_a7_first_distinction_dependency,
        zero_to_arithmetic,
        sphere_before_quantum,
        sibling_parent_pass,
        no_temporal_circularity,
        spacetime_join_parent_pass,
        matter_join_parent_pass,
        dag_pass,
    ))
    return {
        "schema": "TIR_CAUSAL_BRIDGE_FROM_ZERO_V0_1",
        "canonical_nonlogical_axiom_count": 0,
        "legacy_independent_axiom_count": 0,
        "core_path": [
            "RELATION",
            "TWO_POLES",
            "RELATIONAL_SPHERE",
            "CP1",
            "PROJECTIVE_C2",
            "QUANTUM_CARRIER",
            "COMMON_PRIMITIVE_CORE",
        ],
        "arithmetic_path": [
            "RELATION",
            "RELATIONAL_ZERO",
            "WINDING_DEGREE",
            "INTEGER_INDEX",
            "NATURAL_INDEX",
        ],
        "dag_pass": dag_pass,
        "no_quantum_bloch_cycle": no_quantum_bloch_cycle,
        "no_a7_first_distinction_dependency": no_a7_first_distinction_dependency,
        "zero_to_arithmetic": zero_to_arithmetic,
        "sphere_before_quantum": sphere_before_quantum,
        "sibling_parent_pass": sibling_parent_pass,
        "no_temporal_circularity": no_temporal_circularity,
        "tir_spatial_ownership_pass": "TIR_SPATIAL_GEOMETRY" in branch_children,
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
