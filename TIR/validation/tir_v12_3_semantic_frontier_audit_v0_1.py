#!/usr/bin/env python3
"""Fail-closed semantic-frontier audit for TIR monograph v12.3."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MONO = ROOT / "TIR/monograph"
REGISTRY = MONO / "v12/SEMANTIC_FRONTIER_V12_3.json"
CH21 = MONO / "v12/chapters/ch21_open_theorems_completion_frontier.tex"
FRONT = MONO / "frontmatter/publication_frontmatter_v12_0.tex"
README = MONO / "v12/README.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def main() -> int:
    registry = json.loads(read(REGISTRY))
    ch21 = read(CH21)
    front = read(FRONT)
    readme = read(README)

    gates = {g["id"]: g for g in registry.get("gates", [])}
    core_start = ch21.find(r"\section{Current unresolved core}")
    core_end = ch21.find(r"\section{Completion invariant}")
    core = ch21[core_start:core_end] if core_start >= 0 and core_end > core_start else ""

    checks = {
        "schema": registry.get("schema") == "TIR_MONOGRAPH_SEMANTIC_FRONTIER_V12_3",
        "fourteen_legacy_coordinates_audited": len(gates) == 14,
        "tir_head_pinned": registry.get("pinned_heads", {}).get("TIR") == "45b54c0c8aa60ec92607e6132b69aca9ab766d75",
        "idt_head_pinned": registry.get("pinned_heads", {}).get("IDT") == "58f453a4725bf0304417a5d07730f2dc1765dea5",
        "rfc_head_pinned": registry.get("pinned_heads", {}).get("RFC") == "ce4af9ddd480ea40dfb5a3ee26ed396a58cb0e54",
        "soh_head_pinned": registry.get("pinned_heads", {}).get("SOH") == "d99545aa447ef86bc253d8241a3fee9adb8a42c1",
        "einstein_adm_derivation_closed": gates.get("G3_EINSTEIN_ADM_CONSTRAINT_EVOLUTION", {}).get("formal_status", "").startswith("CLOSED_LOCAL_ACTION_LEVEL_ADM"),
        "einstein_global_production_still_open": "OPEN" in gates.get("G3_EINSTEIN_ADM_CONSTRAINT_EVOLUTION", {}).get("production_status", ""),
        "coefficient_magnitude_closed_selector_open": gates.get("G4_COEFFICIENT_MAGNITUDES_AND_SELECTOR", {}).get("verdict") == "PARTIAL_CLOSED_SELECTOR_OPEN",
        "hypercharge_relative_uniqueness_closed": gates.get("G8_HYPERCHARGE_AND_QUARK_MASS", {}).get("verdict") == "HYPERCHARGE_CLOSED_QUARK_MAP_OPEN",
        "neutrino_repair_closed_physical_open": gates.get("G9_NEUTRINO_ABSOLUTE_ACTION_REPAIR", {}).get("verdict") == "CLOSED_DERIVATION_PHYSICAL_OPEN",
        "collatz_interface_closed_coupling_open": gates.get("G13_COLLATZ_FS_PHYSICAL_BINDING", {}).get("verdict") == "INTERFACE_CLOSED_PHYSICAL_COUPLING_OPEN",
        "li_weil_remains_open": gates.get("G14_LI_WEIL_CRITICAL_AXIS", {}).get("verdict") == "OPEN",
        "chapter_marks_einstein_stale": "former Einstein constraint/evolution item is stale" in ch21,
        "chapter_marks_neutrino_repair_closed": "derivational repair is CLOSED" in ch21,
        "chapter_marks_hypercharge_closed": "Relative uniqueness is therefore CLOSED" in ch21,
        "chapter_keeps_production_geometry_open": "Production-global geometry frontier" in ch21 and r"\vTwelveStatus{B}{--}{OPEN}" in ch21,
        "chapter_keeps_rh_open": "Riemann Hypothesis" in ch21 and "riemann\\_hypothesis\\_in\\_closure=false" in ch21,
        "current_core_does_not_reopen_einstein_derivation": "Einstein constraint/evolution closure" not in core,
        "current_core_does_not_reopen_neutrino_repair": "neutrino absolute-action repair" not in core.lower(),
        "current_core_does_not_reopen_hypercharge_relative_uniqueness": "hypercharge source uniqueness" not in core.lower(),
        "current_core_has_coefficient_selector": "transition-parent selector" in core,
        "current_core_has_gauge_running": "continuum gauge normalization and running" in core,
        "current_core_has_strong_cp": "strong-CP source theorem" in core,
        "current_core_has_li_weil": "Li--Weil" in core,
        "frontmatter_v12_3": "Version 12.3" in front and "Local Einstein/ADM constraints" in front,
        "readme_v12_3": "TIR Monograph v12.3" in readme and "Current semantic frontier" in readme,
        "physical_promotion_from_software_forbidden": registry.get("authority", {}).get("physical_promotion_from_software") is False,
        "main_merge_not_authorized": registry.get("authority", {}).get("merge_to_main") is False,
    }

    status = "PASS" if all(checks.values()) else "FAIL"
    receipt = {
        "schema": "TIR_V12_3_SEMANTIC_FRONTIER_AUDIT_V0_1",
        "status": status,
        "registry": str(REGISTRY.relative_to(ROOT)),
        "chapter": str(CH21.relative_to(ROOT)),
        "checks": checks,
        "failed": sorted(k for k, v in checks.items() if not v),
        "physical_promotion": False,
        "riemann_hypothesis_in_closure": False,
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
