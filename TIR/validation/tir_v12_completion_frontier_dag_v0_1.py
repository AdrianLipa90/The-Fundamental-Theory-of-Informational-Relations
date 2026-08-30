#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import defaultdict, deque

ROOTS = {
    "KAPPA_FLAVOUR_NORMALIZATION",
    "LOCAL_R3_GEOMETRY",
    "TETRAHEDRAL_CLOSURE",
    "WIJ_TYPED_HOLONOMY",
    "SE3_DISCRETE_SOLDER_TORSION",
    "COEFFICIENT_ROLE_SIGN_FORCING",
    "THREE_FLAVOUR_CARRIER",
    "V12_EVIDENCE_TAXONOMY",
}

GATES = {
    "CARTAN_CONTINUUM_REFINEMENT": ["SE3_DISCRETE_SOLDER_TORSION", "WIJ_TYPED_HOLONOMY"],
    "ZERO_TORSION_SPATIAL_GR_SECTOR": ["CARTAN_CONTINUUM_REFINEMENT"],
    "TIR_IDT_ADM_JOIN": ["ZERO_TORSION_SPATIAL_GR_SECTOR"],
    "EINSTEIN_CONSTRAINT_EVOLUTION_CLOSURE": ["TIR_IDT_ADM_JOIN"],
    "COEFFICIENT_MAGNITUDE_EXTRACTION": ["COEFFICIENT_ROLE_SIGN_FORCING", "KAPPA_FLAVOUR_NORMALIZATION"],
    "CONTINUUM_GAUGE_NORMALIZATION": ["WIJ_TYPED_HOLONOMY"],
    "ELECTROWEAK_SCHEME_SCALE_CLOSURE": ["CONTINUUM_GAUGE_NORMALIZATION", "KAPPA_FLAVOUR_NORMALIZATION"],
    "HIGGS_SCALAR_ACTION_BINDING": ["ELECTROWEAK_SCHEME_SCALE_CLOSURE", "COEFFICIENT_MAGNITUDE_EXTRACTION"],
    "STRONG_CP_HOLONOMIC_SOURCE": ["WIJ_TYPED_HOLONOMY"],
    "MESON_ABSOLUTE_ACTION_BASELINE": ["WIJ_TYPED_HOLONOMY", "COEFFICIENT_MAGNITUDE_EXTRACTION"],
    "NEUTRINO_ABSOLUTE_ACTION_REPAIR": ["TETRAHEDRAL_CLOSURE", "KAPPA_FLAVOUR_NORMALIZATION"],
    "COSMOLOGY_SCALE_RHOCRIT_BINDING": ["LOCAL_R3_GEOMETRY", "KAPPA_FLAVOUR_NORMALIZATION"],
    "GREMLIN_GLOBAL_GLUING_PROMOTION": ["SE3_DISCRETE_SOLDER_TORSION", "WIJ_TYPED_HOLONOMY"],
    "SOH_NATIVE_LI_WEIL_POSITIVITY": [],
    "RERUN_UNIFIED_EVIDENCE_MATRIX": [
        "COEFFICIENT_MAGNITUDE_EXTRACTION",
        "ELECTROWEAK_SCHEME_SCALE_CLOSURE",
        "HIGGS_SCALAR_ACTION_BINDING",
        "STRONG_CP_HOLONOMIC_SOURCE",
        "MESON_ABSOLUTE_ACTION_BASELINE",
        "NEUTRINO_ABSOLUTE_ACTION_REPAIR",
        "COSMOLOGY_SCALE_RHOCRIT_BINDING",
    ],
}


def topo() -> tuple[list[str], list[str]]:
    nodes = set(ROOTS) | set(GATES)
    indegree = {n: 0 for n in nodes}
    children: dict[str, list[str]] = defaultdict(list)
    missing: list[str] = []
    for child, parents in GATES.items():
        for parent in parents:
            if parent not in nodes:
                missing.append(parent)
                continue
            indegree[child] += 1
            children[parent].append(child)
    q = deque(sorted(n for n, d in indegree.items() if d == 0))
    order: list[str] = []
    while q:
        node = q.popleft()
        order.append(node)
        for child in sorted(children[node]):
            indegree[child] -= 1
            if indegree[child] == 0:
                q.append(child)
    cyclic = sorted(n for n, d in indegree.items() if d > 0)
    return order, sorted(set(missing) | set(cyclic))


def main() -> None:
    order, blockers = topo()
    checks = {
        "all_parent_nodes_resolve": not blockers,
        "dag_is_acyclic": len(order) == len(ROOTS) + len(GATES),
        "evidence_rerun_is_downstream": order.index("RERUN_UNIFIED_EVIDENCE_MATRIX") > order.index("ELECTROWEAK_SCHEME_SCALE_CLOSURE"),
        "cartan_precedes_gr_sector": order.index("CARTAN_CONTINUUM_REFINEMENT") < order.index("ZERO_TORSION_SPATIAL_GR_SECTOR"),
        "gr_sector_precedes_adm": order.index("ZERO_TORSION_SPATIAL_GR_SECTOR") < order.index("TIR_IDT_ADM_JOIN"),
        "adm_precedes_einstein_closure": order.index("TIR_IDT_ADM_JOIN") < order.index("EINSTEIN_CONSTRAINT_EVOLUTION_CLOSURE"),
        "role_sign_precedes_magnitude": order.index("COEFFICIENT_ROLE_SIGN_FORCING") < order.index("COEFFICIENT_MAGNITUDE_EXTRACTION"),
        "gauge_normalization_precedes_ew_closure": order.index("CONTINUUM_GAUGE_NORMALIZATION") < order.index("ELECTROWEAK_SCHEME_SCALE_CLOSURE"),
    }
    status = "PASS" if all(checks.values()) else "FAIL"
    receipt = {
        "schema": "TIR_V12_COMPLETION_FRONTIER_DAG_V0_1",
        "status": status,
        "closed_root_count": len(ROOTS),
        "open_gate_count": len(GATES),
        "closed_roots": sorted(ROOTS),
        "open_gates": GATES,
        "topological_order": order,
        "blockers": blockers,
        "checks": checks,
        "gremlin_role": "CANDIDATE_GRAPH_SEARCH_ONLY_PROMOTION_THEOREM_VALIDATOR_GATED",
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
