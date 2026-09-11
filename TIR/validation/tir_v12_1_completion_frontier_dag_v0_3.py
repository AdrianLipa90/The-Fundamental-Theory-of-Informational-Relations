#!/usr/bin/env python3
"""Fail-closed TIR v12.1 completion-frontier DAG after coefficient parent evaluation."""
from __future__ import annotations

import json
from collections import defaultdict, deque

CLOSED = {
    "KAPPA_FLAVOUR_NORMALIZATION",
    "LOCAL_R3_GEOMETRY",
    "TETRAHEDRAL_CLOSURE",
    "PLATONIC_L_CONSTANT_CLOSURE",
    "WIJ_TYPED_HOLONOMY",
    "SE3_DISCRETE_SOLDER_TORSION",
    "CARTAN_CONTINUUM_REFINEMENT_A2",
    "ZERO_TORSION_LEVI_CIVITA_A3",
    "LEADING_LOOP_METRIC_JET_A4",
    "GLOBAL_3MANIFOLD_CERTIFIER_A5",
    "GLOBAL_SPATIAL_INPUT_CONTRACT",
    "INTERLEAF_MATCHING_INPUT_CONTRACT",
    "COEFFICIENT_ROLE_SIGN_FORCING",
    "COEFFICIENT_MAGNITUDE_PARENT_EVALUATION",
    "THREE_FLAVOUR_CARRIER",
    "COLLATZ_FS_MATHEMATICAL_INTERFACE",
    "V12_EVIDENCE_TAXONOMY",
}

OPEN = {
    "PRODUCTION_GLOBAL_SPATIAL_COMPLEX_INPUT": ["GLOBAL_SPATIAL_INPUT_CONTRACT", "GLOBAL_3MANIFOLD_CERTIFIER_A5"],
    "PRODUCTION_INTERLEAF_MATCHING_FIELD_INPUT": ["INTERLEAF_MATCHING_INPUT_CONTRACT"],
    "GLOBAL_TIR_IDT_RFC_SPACETIME_ADM_JOIN": ["PRODUCTION_GLOBAL_SPATIAL_COMPLEX_INPUT", "PRODUCTION_INTERLEAF_MATCHING_FIELD_INPUT", "ZERO_TORSION_LEVI_CIVITA_A3"],
    "EINSTEIN_CONSTRAINT_EVOLUTION_CLOSURE": ["GLOBAL_TIR_IDT_RFC_SPACETIME_ADM_JOIN", "LEADING_LOOP_METRIC_JET_A4"],
    "COEFFICIENT_TRANSITION_PARENT_SELECTOR": ["COEFFICIENT_ROLE_SIGN_FORCING", "COEFFICIENT_MAGNITUDE_PARENT_EVALUATION", "PLATONIC_L_CONSTANT_CLOSURE", "THREE_FLAVOUR_CARRIER"],
    "CONTINUUM_GAUGE_NORMALIZATION": ["WIJ_TYPED_HOLONOMY"],
    "HYPERCHARGE_SOURCE_UNIQUENESS": ["CONTINUUM_GAUGE_NORMALIZATION", "THREE_FLAVOUR_CARRIER"],
    "QUARK_MASS_MAP": ["PLATONIC_L_CONSTANT_CLOSURE", "COEFFICIENT_TRANSITION_PARENT_SELECTOR"],
    "ELECTROWEAK_SCHEME_SCALE_CLOSURE": ["CONTINUUM_GAUGE_NORMALIZATION", "KAPPA_FLAVOUR_NORMALIZATION"],
    "HIGGS_SCALAR_ACTION_BINDING": ["ELECTROWEAK_SCHEME_SCALE_CLOSURE", "COEFFICIENT_TRANSITION_PARENT_SELECTOR"],
    "STRONG_CP_HOLONOMIC_SOURCE": ["WIJ_TYPED_HOLONOMY", "CONTINUUM_GAUGE_NORMALIZATION"],
    "MESON_ABSOLUTE_ACTION_BASELINE": ["WIJ_TYPED_HOLONOMY", "COEFFICIENT_TRANSITION_PARENT_SELECTOR"],
    "NEUTRINO_ABSOLUTE_ACTION_REPAIR": ["TETRAHEDRAL_CLOSURE", "KAPPA_FLAVOUR_NORMALIZATION"],
    "COSMOLOGY_DIMENSIONFUL_SCALE_BINDING": ["LOCAL_R3_GEOMETRY", "PLATONIC_L_CONSTANT_CLOSURE", "KAPPA_FLAVOUR_NORMALIZATION"],
    "COLLATZ_FS_PHYSICAL_BINDING": ["COLLATZ_FS_MATHEMATICAL_INTERFACE"],
    "GREMLIN_GLOBAL_GLUING_PROMOTION": ["PRODUCTION_GLOBAL_SPATIAL_COMPLEX_INPUT", "PRODUCTION_INTERLEAF_MATCHING_FIELD_INPUT", "WIJ_TYPED_HOLONOMY"],
    "SOH_NATIVE_LI_WEIL_POSITIVITY": [],
    "CRITICAL_AXIS_GLOBAL_POSITIVITY_NONDEGENERACY": ["SOH_NATIVE_LI_WEIL_POSITIVITY"],
    "RIEMANN_HYPOTHESIS": ["CRITICAL_AXIS_GLOBAL_POSITIVITY_NONDEGENERACY"],
    "RERUN_UNIFIED_EVIDENCE_MATRIX": [
        "COEFFICIENT_TRANSITION_PARENT_SELECTOR",
        "ELECTROWEAK_SCHEME_SCALE_CLOSURE",
        "HIGGS_SCALAR_ACTION_BINDING",
        "STRONG_CP_HOLONOMIC_SOURCE",
        "MESON_ABSOLUTE_ACTION_BASELINE",
        "NEUTRINO_ABSOLUTE_ACTION_REPAIR",
        "COSMOLOGY_DIMENSIONFUL_SCALE_BINDING",
    ],
}


def topo() -> tuple[list[str], list[str]]:
    nodes = set(CLOSED) | set(OPEN)
    indegree = {node: 0 for node in nodes}
    children: dict[str, list[str]] = defaultdict(list)
    unresolved: set[str] = set()
    for child, parents in OPEN.items():
        for parent in parents:
            if parent not in nodes:
                unresolved.add(parent)
                continue
            indegree[child] += 1
            children[parent].append(child)
    queue = deque(sorted(node for node, degree in indegree.items() if degree == 0))
    order: list[str] = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for child in sorted(children[node]):
            indegree[child] -= 1
            if indegree[child] == 0:
                queue.append(child)
    unresolved.update(node for node, degree in indegree.items() if degree > 0)
    return order, sorted(unresolved)


def main() -> int:
    order, blockers = topo()
    checks = {
        "all_parent_nodes_resolve": not blockers,
        "dag_is_acyclic": len(order) == len(CLOSED) + len(OPEN),
        "a2_a3_a4_closed": all(node in CLOSED for node in (
            "CARTAN_CONTINUUM_REFINEMENT_A2",
            "ZERO_TORSION_LEVI_CIVITA_A3",
            "LEADING_LOOP_METRIC_JET_A4",
        )),
        "a5_certifier_closed_but_production_input_open": (
            "GLOBAL_3MANIFOLD_CERTIFIER_A5" in CLOSED
            and "PRODUCTION_GLOBAL_SPATIAL_COMPLEX_INPUT" in OPEN
        ),
        "matching_contract_closed_but_production_input_open": (
            "INTERLEAF_MATCHING_INPUT_CONTRACT" in CLOSED
            and "PRODUCTION_INTERLEAF_MATCHING_FIELD_INPUT" in OPEN
        ),
        "coefficient_parent_evaluation_closed": "COEFFICIENT_MAGNITUDE_PARENT_EVALUATION" in CLOSED,
        "coefficient_transition_selector_open": "COEFFICIENT_TRANSITION_PARENT_SELECTOR" in OPEN,
        "old_coarse_magnitude_gate_removed": "COEFFICIENT_MAGNITUDE_EXTRACTION" not in CLOSED and "COEFFICIENT_MAGNITUDE_EXTRACTION" not in OPEN,
        "quark_map_waits_for_selector": "COEFFICIENT_TRANSITION_PARENT_SELECTOR" in OPEN["QUARK_MASS_MAP"],
        "meson_baseline_waits_for_selector": "COEFFICIENT_TRANSITION_PARENT_SELECTOR" in OPEN["MESON_ABSOLUTE_ACTION_BASELINE"],
        "rh_is_open_node": "RIEMANN_HYPOTHESIS" in OPEN,
        "evidence_rerun_downstream": order.index("RERUN_UNIFIED_EVIDENCE_MATRIX") > order.index("COEFFICIENT_TRANSITION_PARENT_SELECTOR"),
        "spacetime_join_waits_for_both_production_inputs": all(
            p in OPEN["GLOBAL_TIR_IDT_RFC_SPACETIME_ADM_JOIN"]
            for p in ("PRODUCTION_GLOBAL_SPATIAL_COMPLEX_INPUT", "PRODUCTION_INTERLEAF_MATCHING_FIELD_INPUT")
        ),
    }
    status = "PASS" if all(checks.values()) else "FAIL"
    receipt = {
        "schema": "TIR_V12_1_COMPLETION_FRONTIER_DAG_V0_3",
        "status": status,
        "closed_or_implemented_nodes": sorted(CLOSED),
        "open_nodes": OPEN,
        "topological_order": order,
        "blockers": blockers,
        "checks": checks,
        "riemann_hypothesis_in_closure": False,
        "physical_promotion": False,
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
