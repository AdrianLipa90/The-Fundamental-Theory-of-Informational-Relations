#!/usr/bin/env python3
"""Publication v1.1 dependency and synchronization audit."""
from __future__ import annotations

from collections import defaultdict, deque
from pathlib import Path
import json

NODES = {
    "P0", "C1", "C2", "C3", "C4", "R1", "E1", "E2", "E3", "R2", "E4",
    "T1", "T2", "T3", "T4", "Q1",
}

EDGES = (
    ("P0", "C1"), ("C1", "C2"), ("C2", "C3"), ("C3", "C4"),
    ("C1", "R1"), ("C3", "R1"),
    ("C2", "E1"), ("C4", "E2"), ("E1", "E3"), ("E2", "E3"),
    ("R1", "R2"), ("C4", "R2"), ("E1", "R2"), ("R2", "E4"), ("E3", "E4"),
    ("C1", "T1"), ("T1", "T2"), ("C4", "T3"), ("T2", "T3"), ("T3", "T4"),
    ("C1", "Q1"), ("T4", "Q1"),
)

REQUIRED = (
    "TIR/subrepos/the-space-of-geometry/README.md",
    "TIR/subrepos/the-space-of-geometry/RESEARCH_SPINE_V0_10.md",
    "TIR/subrepos/the-space-of-geometry/foundations/CANONICAL_SPATIAL_RELATION_EXTRACTION_V0_1.md",
    "TIR/subrepos/the-space-of-geometry/foundations/PHYSICAL_RELATION_CHORD_REALIZABILITY_V0_1.md",
    "TIR/subrepos/the-space-of-geometry/foundations/A5_A7_SIMPLEX_EDGE_ORBIT_REGULARITY_V0_1.md",
    "TIR/subrepos/the-space-of-geometry/paper/THE_SPACE_OF_GEOMETRY_V1_1.tex",
    "TIR/subrepos/the-space-of-geometry/publication/PROOF_DEPENDENCY_AUDIT_V0_3.md",
    "TIR/subrepos/the-space-of-geometry/validation/physical_relation_chord_realizability_v0_1.py",
)

MANUSCRIPT_TOKENS = (
    "Physical relation chord domain",
    "Theorem R: physical-state Pythagorean realization",
    r"\mathcal R_{\rm phys}",
    r"\frac9{25}+\frac{16}{25}=1",
    "Theorem T1: minimal finite full-dimensional support",
    "Theorem Q: independent tetrahedral informational convergence",
)


def topo() -> list[str]:
    indeg = {n: 0 for n in NODES}
    graph: dict[str, list[str]] = defaultdict(list)
    for a, b in EDGES:
        graph[a].append(b)
        indeg[b] += 1
    q = deque(sorted(n for n, d in indeg.items() if d == 0))
    out: list[str] = []
    while q:
        n = q.popleft()
        out.append(n)
        for m in sorted(graph[n]):
            indeg[m] -= 1
            if indeg[m] == 0:
                q.append(m)
    return out


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


def build_receipt() -> dict[str, object]:
    order = topo()
    acyclic = len(order) == len(NODES)
    e3 = ancestors("E3")
    e4 = ancestors("E4")
    t4 = ancestors("T4")
    tetra = {"T1", "T2", "T3", "T4", "Q1"}

    carrier_tetra_independent = not bool(e3 & tetra)
    physical_tetra_independent = not bool(e4 & tetra)
    sic_not_premise = "Q1" not in e3 and "Q1" not in e4 and "Q1" not in t4

    surface_map = {p: Path(p).is_file() for p in REQUIRED}
    surfaces_present = all(surface_map.values())

    manuscript = Path("TIR/subrepos/the-space-of-geometry/paper/THE_SPACE_OF_GEOMETRY_V1_1.tex")
    text = manuscript.read_text(encoding="utf-8") if manuscript.is_file() else ""
    token_map = {token: token in text for token in MANUSCRIPT_TOKENS}
    manuscript_synchronized = all(token_map.values())

    passed = all((
        acyclic,
        carrier_tetra_independent,
        physical_tetra_independent,
        sic_not_premise,
        surfaces_present,
        manuscript_synchronized,
        "R1" in e4,
        "E3" in e4,
        "T1" in t4,
    ))

    return {
        "schema": "TIR_SPACE_OF_GEOMETRY_PUBLICATION_PROOF_AUDIT_V0_3",
        "technical_status": "PASS" if passed else "FAIL",
        "publication_verdict": "PASS_V1_1_SYNCHRONIZED_LOCAL_PROOF_GRAPH" if passed else "FAIL_V1_1_PROOF_GRAPH",
        "canonical_manuscript": "THE_SPACE_OF_GEOMETRY_V1_1.tex",
        "acyclic": acyclic,
        "node_count": len(NODES),
        "edge_count": len(EDGES),
        "tetrahedron_required_for_carrier_pythagoras": not carrier_tetra_independent,
        "tetrahedron_required_for_physical_pythagoras": not physical_tetra_independent,
        "sic_is_premise_of_main_endpoints": not sic_not_premise,
        "physical_relation_domain": "radius_two_ball",
        "physical_certificate": "3/5,4/5,1",
        "manuscript_physical_realizability_synchronized": manuscript_synchronized,
        "manuscript_tokens": token_map,
        "all_required_surfaces_present": surfaces_present,
        "required_surfaces": surface_map,
        "global_extent_status": "DOWNSTREAM_LOCAL_CARRIER_GLUING",
        "topological_order": order,
    }


def main() -> None:
    receipt = build_receipt()
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if receipt["technical_status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
