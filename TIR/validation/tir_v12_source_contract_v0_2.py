#!/usr/bin/env python3
"""Fail-closed source contract for the integrated TIR monograph v12 publication surface."""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MONOGRAPH = ROOT / "TIR/monograph"
MASTER = MONOGRAPH / "tir_monograph_v12.tex"
FRONTMATTER = MONOGRAPH / "frontmatter/publication_frontmatter_v12_0.tex"
CHAPTER_DIR = MONOGRAPH / "v12/chapters"
HADRON_RECEIPT = ROOT / "TIR/validation/TIR_V12_HADRON_FORMULA_AUDIT_V0_2.json"

CHAPTERS = [
    "ch01_first_distinction_relational_kernel",
    "ch02_half_binary_information_ln2",
    "ch03_complex_carrier_information_geometry",
    "ch04_c2_to_herm0_r3",
    "ch05_euclidean_geometry_dimension_gate",
    "ch06_tetrahedral_closure",
    "ch07_connections_holonomy_se3_solder_torsion",
    "ch08_three_flavour_carrier_su3",
    "ch09_kappa_normalization",
    "ch10_discrete_structural_labels",
    "ch11_action_architecture_coefficient_forcing",
    "ch12_charged_leptons_neutrinos",
    "ch13_ckm_pmns_flavour_mixing",
    "ch14_hadrons_baryons_mesons",
    "ch15_gauge_hypercharge_anomalies",
    "ch16_electroweak_higgs",
    "ch17_strong_cp_neutron_edm",
    "ch18_cosmological_extension",
    "ch19_unified_evidence_matrix",
    "ch20_prospective_predictions_falsification",
    "ch21_open_theorems_completion_frontier",
]

WRAPPER_MARKERS = (
    r"\section*{v12 source integration map}",
    r"\section*{Migration invariant}",
)

MATH_ENVIRONMENTS = (
    "equation",
    "equation*",
    "align",
    "align*",
    "gather",
    "gather*",
    "multline",
    "multline*",
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def math_mode_path_hits(text: str) -> list[str]:
    r"""Return compact witnesses for \path used inside display-math surfaces."""
    hits: list[str] = []
    for match in re.finditer(r"\\\[(.*?)\\\]", text, flags=re.S):
        if r"\path{" in match.group(1):
            line = text.count("\n", 0, match.start()) + 1
            hits.append(f"display-math@L{line}")
    for env in MATH_ENVIRONMENTS:
        pattern = re.compile(
            rf"\\begin\{{{re.escape(env)}\}}(.*?)\\end\{{{re.escape(env)}\}}",
            flags=re.S,
        )
        for match in pattern.finditer(text):
            if r"\path{" in match.group(1):
                line = text.count("\n", 0, match.start()) + 1
                hits.append(f"{env}@L{line}")
    return hits


def main() -> None:
    checks: dict[str, bool] = {}
    detail: dict[str, object] = {}

    checks["master_exists"] = MASTER.is_file()
    master = read(MASTER) if MASTER.is_file() else ""

    expected_includes = [rf"\include{{v12/chapters/{name}}}" for name in CHAPTERS]
    include_positions = [master.find(item) for item in expected_includes]
    checks["master_has_21_chapters_exactly_once"] = all(master.count(item) == 1 for item in expected_includes)
    checks["master_chapter_order_is_dependency_order"] = include_positions == sorted(include_positions) and all(pos >= 0 for pos in include_positions)
    checks["master_is_content_migration_candidate"] = "Version 12.0 Content-Migration Candidate" in master

    missing: list[str] = []
    short: list[str] = []
    wrappers: list[str] = []
    chapter_labels: list[tuple[str, str]] = []
    chapter_sizes: dict[str, int] = {}

    for name in CHAPTERS:
        path = CHAPTER_DIR / f"{name}.tex"
        if not path.is_file():
            missing.append(name)
            continue
        text = read(path)
        chapter_sizes[name] = len(text)
        if len(text) < 1500 or "\\chapter" not in text:
            short.append(name)
        if any(marker in text for marker in WRAPPER_MARKERS):
            wrappers.append(name)
        for label in re.findall(r"\\label\{([^}]+)\}", text):
            chapter_labels.append((name, label))

    checks["all_21_chapter_files_exist"] = not missing and len(chapter_sizes) == 21
    checks["all_21_chapters_substantive"] = not short
    checks["no_main_chapter_wrapper_markers"] = not wrappers

    label_counts = Counter(label for _, label in chapter_labels)
    duplicate_labels = sorted(label for label, count in label_counts.items() if count > 1)
    checks["main_chapter_labels_unique"] = not duplicate_labels

    math_path_hits: dict[str, list[str]] = {}
    v12_tex_surfaces = [MASTER, FRONTMATTER]
    v12_tex_surfaces.extend(sorted((MONOGRAPH / "v12").rglob("*.tex")))
    for path in v12_tex_surfaces:
        if not path.is_file():
            continue
        hits = math_mode_path_hits(read(path))
        if hits:
            math_path_hits[str(path.relative_to(ROOT))] = hits
    checks["no_path_command_inside_display_math"] = not math_path_hits

    ch9 = read(CHAPTER_DIR / "ch09_kappa_normalization.tex") if (CHAPTER_DIR / "ch09_kappa_normalization.tex").is_file() else ""
    checks["canonical_kappa_owner_marker_present"] = "V12_CANONICAL_KAPPA_OWNER" in ch9
    checks["canonical_kappa_source_bound"] = "TIR/foundations/TIR_KAPPA_FLAVOUR_MIXING_NORMALIZATION_V0_1.md" in ch9
    checks["kappa_formula_present_in_owner"] = r"\kappa" in ch9 and r"24\pi" in ch9 and r"\ln2" in ch9

    ch6 = read(CHAPTER_DIR / "ch06_tetrahedral_closure.tex") if (CHAPTER_DIR / "ch06_tetrahedral_closure.tex").is_file() else ""
    checks["tetrahedral_regular_gram_present"] = r"-\frac13" in ch6 and "orthogonal-congruence class" in ch6
    checks["legacy_tetrahedral_semantics_firewall_present"] = "Legacy tetrahedral semantics" in ch6 and "sector-level provenance" in ch6

    ch7 = read(CHAPTER_DIR / "ch07_connections_holonomy_se3_solder_torsion.tex") if (CHAPTER_DIR / "ch07_connections_holonomy_se3_solder_torsion.tex").is_file() else ""
    checks["atlas_holonomy_firewall_present"] = "holonomy firewall" in ch7.lower() and r"G_C^{atlas}=e_{SE(3)}" in ch7
    checks["universal_loop_torsion_identity_present"] = r"\mathcal T_{xyz}=-\mathcal C_{xyz}" in ch7 and r"\mathbf t_C" in ch7
    checks["cartan_refinement_target_present"] = r"T^a" in ch7 and r"\Omega^a{}_b" in ch7

    ch14 = read(CHAPTER_DIR / "ch14_hadrons_baryons_mesons.tex") if (CHAPTER_DIR / "ch14_hadrons_baryons_mesons.tex").is_file() else ""
    checks["hadron_audit_v0_2_source_bound"] = (
        "tir_v12_hadron_formula_audit_v0_2.py" in ch14
        and "TIR_V12_HADRON_FORMULA_AUDIT_V0_2.json" in ch14
    )
    checks["hadron_audit_v0_2_receipt_exists"] = HADRON_RECEIPT.is_file()
    hadron_receipt_status = None
    hadron_receipt_schema = None
    if HADRON_RECEIPT.is_file():
        try:
            hadron_receipt = json.loads(read(HADRON_RECEIPT))
            hadron_receipt_status = hadron_receipt.get("status")
            hadron_receipt_schema = hadron_receipt.get("schema")
        except json.JSONDecodeError:
            pass
    checks["hadron_audit_v0_2_receipt_typed"] = (
        hadron_receipt_schema == "TIR_V12_HADRON_FORMULA_AUDIT_V0_2"
        and hadron_receipt_status == "PASS_WITH_QUARANTINES"
    )

    ch19 = read(CHAPTER_DIR / "ch19_unified_evidence_matrix.tex") if (CHAPTER_DIR / "ch19_unified_evidence_matrix.tex").is_file() else ""
    checks["evidence_single_owner_invariant_present"] = "Single-owner invariant" in ch19
    checks["anomaly_evidence_split_present"] = all(
        token in ch19
        for token in (
            "Hypercharge source map",
            "Standard local anomaly sums + Witten count",
            "Legacy A5 baryon-current row",
        )
    )
    checks["retained_nedm_fail_present"] = "Strong-CP $\\to$ neutron EDM" in ch19 and "FAIL" in ch19

    ch20 = read(CHAPTER_DIR / "ch20_prospective_predictions_falsification.tex") if (CHAPTER_DIR / "ch20_prospective_predictions_falsification.tex").is_file() else ""
    checks["prospective_two_observable_contract_present"] = "y_c/y_\\mu" in ch20 and "y_c/y_t" in ch20 and "three" in ch20.lower()

    ch21 = read(CHAPTER_DIR / "ch21_open_theorems_completion_frontier.tex") if (CHAPTER_DIR / "ch21_open_theorems_completion_frontier.tex").is_file() else ""
    checks["completion_dag_receipt_present"] = all(
        token in ch21 for token in ("23 resolved nodes", "eight closed roots", "fifteen open gates", "tir_v12_completion_frontier_dag_v0_1.py")
    )

    root_readme = read(ROOT / "README.md") if (ROOT / "README.md").is_file() else ""
    v12_readme = read(MONOGRAPH / "v12/README.md") if (MONOGRAPH / "v12/README.md").is_file() else ""
    frontmatter = read(FRONTMATTER) if FRONTMATTER.is_file() else ""
    manifest = read(MONOGRAPH / "v12/MIGRATION_MANIFEST.yaml") if (MONOGRAPH / "v12/MIGRATION_MANIFEST.yaml").is_file() else ""

    checks["root_readme_uses_derived_kappa_surface"] = (
        "TIR_KAPPA_FLAVOUR_MIXING_NORMALIZATION_V0_1.md" in root_readme
        and "MODEL POSTULATE" not in root_readme
    )
    checks["v12_readme_integrated_status"] = (
        "INTEGRATED_ON_MAIN" in v12_readme
        and "Canonical branch: `main`" in v12_readme
        and "all twenty-one" in v12_readme.lower()
    )
    checks["frontmatter_content_migration_status"] = "twenty-one main chapters" in frontmatter and "wrapper chapters" not in frontmatter.lower()
    checks["manifest_content_migration_status"] = 'version: "12.0-content-migration"' in manifest and "all-21-main-chapters-substantive" in manifest

    detail["missing_chapters"] = missing
    detail["short_or_nonchapter_files"] = short
    detail["wrapper_marker_files"] = wrappers
    detail["duplicate_labels"] = duplicate_labels
    detail["math_mode_path_hits"] = math_path_hits
    detail["chapter_sizes"] = chapter_sizes
    detail["main_label_count"] = len(chapter_labels)
    detail["hadron_receipt_schema"] = hadron_receipt_schema
    detail["hadron_receipt_status"] = hadron_receipt_status

    status = "PASS" if all(checks.values()) else "FAIL"
    receipt = {
        "schema": "TIR_V12_SOURCE_CONTRACT_V0_2",
        "technical_status": status,
        "supersedes": "TIR_V12_SOURCE_CONTRACT_V0_1",
        "master": str(MASTER.relative_to(ROOT)),
        "chapter_count": len(CHAPTERS),
        "checks": checks,
        "detail": detail,
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
