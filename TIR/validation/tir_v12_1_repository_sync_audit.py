#!/usr/bin/env python3
"""Fail-closed repository-to-monograph synchronization audit for TIR v12.1."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MONO = ROOT / "TIR/monograph"
CH = MONO / "v12/chapters"
APP = MONO / "v12/appendices"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def main() -> None:
    master = read(MONO / "tir_monograph_v12.tex")
    ch7 = read(CH / "ch07_connections_holonomy_se3_solder_torsion.tex")
    ch10 = read(CH / "ch10_discrete_structural_labels.tex")
    ch21 = read(CH / "ch21_open_theorems_completion_frontier.tex")
    app_e = read(APP / "appE_v12_1_repository_state_sync.tex")
    current = read(ROOT / "TIR/CURRENT_STATUS.md")
    dep = json.loads(read(ROOT / "DEPENDENCY_EXPORT.json"))

    checks = {
        "master_v12_1_marker": "Version 12.1 Audited Repository Synchronization" in master,
        "master_includes_v12_1_appendix": r"\include{v12/appendices/appE_v12_1_repository_state_sync}" in master,
        "chapter7_cartan_a2": "Gate A2" in ch7 and "TIR_CARTAN_CONTINUUM_REFINEMENT_V0_1.md" in ch7,
        "chapter7_levi_civita_a3": "Gate A3" in ch7 and "TIR_ZERO_TORSION_LEVI_CIVITA_SELECTION_V0_1.md" in ch7,
        "chapter7_metric_jet_a4": "Gate A4" in ch7 and "TIR_LEADING_LOOP_LOCALITY_METRIC_JET_V0_1.md" in ch7,
        "chapter7_global_certifier_a5": "Gate A5" in ch7 and "TIR_GLOBAL_3MANIFOLD_SMOOTH_CERTIFICATE_V0_1.md" in ch7,
        "chapter10_platonic_source": "TIR_PLATONIC_L_CONSTANTS_CLOSURE_V0_1.md" in ch10,
        "chapter10_indices": "[S_4:A_4]" in ch10 and "[A_5:A_4]" in ch10,
        "chapter10_collatz_crosscheck_retained": "Collatz" in ch10 and "independent" in ch10.lower(),
        "chapter21_no_stale_23_8_15_snapshot": "23 resolved nodes" not in ch21 and "fifteen open gates" not in ch21,
        "chapter21_production_spatial_input_open": "PRODUCTION_GLOBAL_SPATIAL_COMPLEX_INPUT" in ch21,
        "chapter21_matching_input_open": "PRODUCTION_INTERLEAF_MATCHING_FIELD_INPUT" in ch21,
        "chapter21_rh_open": "RIEMANN_HYPOTHESIS" in ch21 and "OPEN" in ch21,
        "appendix_e_baseline": "0f63c823961a58770de22d14b5f53e2bfa38a9b3" in app_e,
        "appendix_e_empirical_firewall": "merged theorem/contract PASS" in app_e and "physical observable PASS" in app_e,
        "current_l_constants_merged": "TIR_L_CONSTANTS = CLOSED_INTERNAL_PLATONIC_COSET_DERIVATION / MERGED_MAIN" in current,
        "current_cartan_updated": "TIR_CARTAN_REFINEMENT_A2 = CLOSED_CONDITIONAL_LOCAL_REFINEMENT" in current,
        "current_a5_input_firewall": "TIR_GLOBAL_3MANIFOLD_A5 = CERTIFIER_CLOSED / PRODUCTION_INPUT_OPEN" in current,
        "dependency_export_baseline": dep.get("source_commit") == "0f63c823961a58770de22d14b5f53e2bfa38a9b3",
        "dependency_export_l_constants": any(c.get("claim_id") == "TIR.L_CONSTANTS.PLATONIC_CLOSURE" for c in dep.get("claims", [])),
        "dependency_export_phase_interface": any(c.get("claim_id") == "TIR.COLLATZ_FS.RELATIONAL_PHASE_INTERFACE" for c in dep.get("claims", [])),
    }
    status = "PASS" if all(checks.values()) else "FAIL"
    out = {
        "schema": "TIR_V12_1_REPOSITORY_SYNC_AUDIT_V0_1",
        "status": status,
        "baseline_main": "0f63c823961a58770de22d14b5f53e2bfa38a9b3",
        "physical_promotion": False,
        "checks": checks,
    }
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
