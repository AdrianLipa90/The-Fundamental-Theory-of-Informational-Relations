#!/usr/bin/env python3
"""Deterministic publication dependency audit v0.2 with physical realizability."""
from __future__ import annotations

from collections import defaultdict, deque
from pathlib import Path
import json

NODES = {
    "P0", "C1", "C2", "C3", "C4", "R1", "E1", "E2", "E3", "R2", "E4",
    "T1", "T2", "T3", "T4", "Q1",
}

EDGES = (
    ("P0", "C1"),
    ("C1", "C2"),
    ("C2", "C3"),
    ("C3", "C4"),
    ("C1", "R1"),
    ("C3", "R1"),
    ("C2", "E1"),
    ("C4", "E2"),
    ("E1", "E3"),
    ("E2", "E3"),
    ("R1", "R2"),
    ("C4", "R2"),
    ("E1", "R2"),
    ("R2", "E4"),
    ("E3", "E4"),
    ("C1", "T1"),
    ("T1", "T2"),
    ("C4", "T3"),
    ("T2", "T3"),
    ("T3", "T4"),
    ("C1", "Q1"),
    ("T4", "Q1"),
)

REQUIRED_SURFACES = (
    "TIR/subrepos/the-space-of-geometry/RESEARCH_SPINE_V0_10.md",
    "TIR/subrepos/the-space-of-geometry/foundations/CANONICAL_SPATIAL_RELATION_EXTRACTION_V0_1.md",
    "TIR/subrepos/the-space-of-geometry/foundations/PHYSICAL_RELATION_CHORD_REALIZABILITY_V0_1.md",
    "TIR/subrepos/the-space-of-geometry/foundations/A5_A7_SIMPLEX_EDGE_ORBIT_REGULARITY_V0_1.md",
    "TIR/subrepos/the-space-of-geometry/foundations/LOCAL_EUCLIDEAN_PYTHAGOREAN_CLOSURE_V0_1.md",
    "TIR/subrepos/the-space-of-geometry/validation/physical_relation_chord_realizability_v0_1.py",
    "TIR/subrepos/the-space-of-geometry/paper/THE_SPACE_OF_GEOMETRY_V1_0.tex",
    "TIR/subrepos/the-space-of-geometry/publication/PROOF_DEPENDENCY_AUDIT_V0_2.md",
)


def topological_order() -> list[str]:
    indegree = {n: 0 for n in NODES}
    graph: dict[str, list[str]] = defaultdict(list)
    for a, b in EDGES:
        graph[a].append(b)
        indegree[b] += 1
    q = deque(sorted(n for n, d in indegree.items() if d == 0))
    order: list[str] = []
    while q:
        n = q.popleft()
        order.append(n)
        for m in sorted(graph[n]):
            indegree[m] -= 1
            if indegree[m] == 0:
                q.append(m)
    return order


def ancestors(target: str) -> set[str]:
    rev: dict[str, list[str]] = defaultdict(list)
    for a, b in EDGES:
        rev[b].append(a)
    seen: set[str] = set()
    stack = [target]
    while stack:
        n = stack.pop()
        for p in rev[n]:
            if p not in seen:
                seen.add(p)
                stack.append(p)
    return seen


def descendants(source: str) -> set[str]:
    graph: dict[str, list[str]] = defaultdict(list)
    for a, b in EDGES:
        graph[a].append(b)
    seen: set[str] = set()
    stack = [source]
    while stack:
        n = stack.pop()
        for c in graph[n]:
            if c not in seen:
                seen.add(c)
                stack.append(c)
    return seen


def build_receipt() -> dict[str, object]:
    order = topological_order()
    acyclic = len(order) == len(NODES)

    e3_anc = ancestors("E3")
    e4_anc = ancestors("E4")
    t4_anc = ancestors("T4")
    q1_desc = descendants("Q1")

    tetra_nodes = {"T1", "T2", "T3", "T4", "Q1"}
    pythagoras_tetra_independent = not bool(e3_anc & tetra_nodes)
    physical_pythagoras_tetra_independent = not bool(e4_anc & tetra_nodes)
    sic_not_premise = (
        "Q1" not in e3_anc
        and "Q1" not in e4_anc
        and "Q1" not in t4_anc
        and not q1_desc
    )

    physical_realizability_chain = all(
        node in e4_anc for node in ("P0", "C1", "C2", "C3", "C4", "R1", "E1", "R2", "E3")
    )
    carrier_pythagoras_chain = all(node in e3_anc for node in ("P0", "C1", "C2", "C4", "E1", "E2"))
    finite_cell_chain = all(node in t4_anc for node in ("C1", "T1", "T2", "T3"))

    surfaces = {path: Path(path).is_file() for path in REQUIRED_SURFACES}
    all_surfaces_present = all(surfaces.values())

    passed = all((
        acyclic,
        pythagoras_tetra_independent,
        physical_pythagoras_tetra_independent,
        sic_not_premise,
        physical_realizability_chain,
        carrier_pythagoras_chain,
        finite_cell_chain,
        all_surfaces_present,
    ))

    return {
        "schema": "TIR_SPACE_OF_GEOMETRY_PUBLICATION_PROOF_AUDIT_V0_2",
        "technical_status": "PASS" if passed else "FAIL",
        "publication_verdict": (
            "PASS_LOCAL_DEPENDENCY_GRAPH_AND_PHYSICAL_REALIZABILITY"
            if passed else "FAIL_DEPENDENCY_GRAPH"
        ),
        "node_count": len(NODES),
        "edge_count": len(EDGES),
        "acyclic": acyclic,
        "topological_order": order,
        "common_carrier": "Herm_0(2)~=R3",
        "physical_relation_domain": "R1=radius_two_ball",
        "carrier_pythagorean_endpoint": "E3",
        "physical_pythagorean_endpoint": "E4",
        "regular_tetrahedron_endpoint": "T4",
        "sic_crosscheck": "Q1",
        "tetrahedron_required_for_pythagoras": not pythagoras_tetra_independent,
        "tetrahedron_required_for_physical_pythagoras": not physical_pythagoras_tetra_independent,
        "sic_is_premise_of_main_endpoints": not sic_not_premise,
        "physical_realizability_chain_complete": physical_realizability_chain,
        "carrier_pythagoras_chain_complete": carrier_pythagoras_chain,
        "finite_cell_chain_complete": finite_cell_chain,
        "normalized_physical_certificate": "3/5,4/5,1",
        "global_extent_status": "DOWNSTREAM_LOCAL_CARRIER_GLUING",
        "required_surfaces": surfaces,
        "all_required_surfaces_present": all_surfaces_present,
    }


def main() -> None:
    receipt = build_receipt()
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if receipt["technical_status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
