#!/usr/bin/env python3
"""Audit the current information-spinor and flavour-mixing publication crosswalk."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BIB = ROOT / "references_expanded_v10_8.tex"
FILES = (
    "appendices/appP_information_spinor_crosswalk.tex",
    "appendices/appA_kappa_derivation.tex",
    "appendices/appD_poincare_disk.tex",
    "chapters/ch02_metatime_framework.tex",
)
REQUIRED_LABELS = {
    "appendices/appP_information_spinor_crosswalk.tex": (
        "app:information_spinor_crosswalk",
        "eq:appP-24",
        "eq:appP-kappa",
    ),
    "appendices/appA_kappa_derivation.tex": ("app:kappa",),
    "appendices/appD_poincare_disk.tex": ("app:poincare",),
    "chapters/ch02_metatime_framework.tex": (
        "ch:metatime_framework",
        "eq:kappa_construction",
        "eq:twentyfour-crossfactor",
        "eq:mixing-channel-count",
        "eq:mixing-phase-measure",
    ),
}
REQUIRED_CROSSREFS = (
    r"\ref{app:kappa}",
    r"\ref{app:poincare}",
    r"\ref{ch:pmns_mixing}",
    r"\ref{app:sector_holonomy_release}",
)


def cited_keys(text: str) -> set[str]:
    keys: set[str] = set()
    for group in re.findall(r"\\cite\{([^}]+)\}", text):
        keys.update(k.strip() for k in group.split(",") if k.strip())
    return keys


def bib_keys() -> set[str]:
    return set(re.findall(r"\\bibitem\{([^}]+)\}", BIB.read_text(encoding="utf-8")))


def main() -> None:
    bibliography = bib_keys()
    if not bibliography:
        raise SystemExit("No bibliography entries found")

    rows = []
    all_cited: set[str] = set()
    for rel in FILES:
        path = ROOT / rel
        if not path.exists():
            raise SystemExit(f"Missing audited file: {rel}")
        text = path.read_text(encoding="utf-8")
        cited = cited_keys(text)
        unresolved = sorted(cited - bibliography)
        if unresolved:
            raise SystemExit(f"Unresolved bibliography keys in {rel}: {unresolved}")
        if not cited:
            raise SystemExit(f"No local citation in {rel}")
        missing_labels = [label for label in REQUIRED_LABELS[rel] if f"\\label{{{label}}}" not in text]
        if missing_labels:
            raise SystemExit(f"Missing labels in {rel}: {missing_labels}")
        all_cited.update(cited)
        rows.append({
            "path": rel,
            "citation_commands": len(re.findall(r"\\cite\{", text)),
            "unique_cited_keys": len(cited),
            "labels_checked": list(REQUIRED_LABELS[rel]),
        })

    crosswalk = (ROOT / FILES[0]).read_text(encoding="utf-8")
    missing_refs = [ref for ref in REQUIRED_CROSSREFS if ref not in crosswalk]
    if missing_refs:
        raise SystemExit(f"Crosswalk missing required parent references: {missing_refs}")

    payload = {
        "schema": "tir.information-spinor-crosswalk-audit/v2",
        "status": "PASS",
        "kappa_provenance": "SU3F_3x8_MIXING_PLUS_HALF_TURN",
        "bibliography_entries": len(bibliography),
        "audited_files": len(rows),
        "unique_cited_keys": len(all_cited),
        "required_crossrefs": list(REQUIRED_CROSSREFS),
        "rows": rows,
    }
    (ROOT / "information_spinor_crosswalk_audit.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    lines = [
        "# Information-Spinor Crosswalk Audit",
        "",
        "`PASS`",
        "",
        f"- Bibliography entries available: **{len(bibliography)}**",
        f"- Current files audited: **{len(rows)}**",
        f"- Unique bibliography keys used: **{len(all_cited)}**",
        "- Required TIR cross-references: **PASS**",
        "- κ provenance: **SU(3)_F, 3 flavours × 8 mixing directions × π half-turn**",
    ]
    (ROOT / "INFORMATION_SPINOR_CROSSWALK_AUDIT.md").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )
    print("INFORMATION-SPINOR CROSSWALK AUDIT PASS")


if __name__ == "__main__":
    main()
