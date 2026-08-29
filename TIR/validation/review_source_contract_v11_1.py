#!/usr/bin/env python3
"""Static source-contract audit for the current integrated TIR publication surfaces."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "monograph"


def count(path: Path, needle: str) -> int:
    return path.read_text(encoding="utf-8").count(needle)


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def build_receipt() -> dict[str, object]:
    failures: list[str] = []

    root_tex = MONOGRAPH / "metatime_monograph.tex"
    app_a = MONOGRAPH / "appendices" / "appA_kappa_derivation.tex"
    app_i = MONOGRAPH / "appendices" / "appI_source_code.tex"
    app_p = MONOGRAPH / "appendices" / "appP_secret_half_cross_relation.tex"
    app_spinor = MONOGRAPH / "appendices" / "appP_information_spinor_crosswalk.tex"
    ch02 = MONOGRAPH / "chapters" / "ch02_metatime_framework.tex"
    cross_review = ROOT / "docs" / "cross_reviews" / "TIR_SECRET_HALF_2026-08-07.md"
    phase_patch = MONOGRAPH / "apply_kappa_phase_rate_patch.py"
    paper_patch = ROOT / "apply_metatime_paper_review_patch.py"
    legacy_runner = ROOT / "run_audit.py"
    phase_validator = ROOT / "validation" / "kappa_phase_rate_identity_v11_1.py"
    mixing_validator = ROOT / "validation" / "tir_kappa_flavour_mixing_normalization_v0_1.py"
    mixing_theorem = ROOT / "foundations" / "TIR_KAPPA_FLAVOUR_MIXING_NORMALIZATION_V0_1.md"

    required_paths = (
        root_tex,
        app_a,
        app_i,
        app_p,
        app_spinor,
        ch02,
        cross_review,
        phase_patch,
        paper_patch,
        legacy_runner,
        phase_validator,
        mixing_validator,
        mixing_theorem,
    )
    for path in required_paths:
        require(path.is_file(), f"missing required review source: {path.relative_to(ROOT)}", failures)

    if root_tex.is_file():
        require(
            count(root_tex, r"\include{appendices/appP_secret_half_cross_relation}") == 1,
            "Appendix P must be included exactly once by the monograph root",
            failures,
        )

    if app_a.is_file():
        text = app_a.read_text(encoding="utf-8")
        require(count(app_a, r"\label{app:kappa-phase-rate}") == 1,
                "Appendix A must contain exactly one κ phase-rate section label", failures)
        require(count(app_a, r"\label{app:kappa-constraint-manifold}") == 1,
                "Appendix A must contain exactly one κ constraint-manifold label", failures)
        require(r"\frac{\ln2}{12}" in text,
                "Appendix A must retain the ln2/12 closed form", failures)
        require(r"\dim_{\mathbb R}\mathfrak{su}(3)_F=3^2-1=8" in text,
                "Appendix A must retain the eight-dimensional SU(3)_F mixing algebra", failures)
        require(r"N_{\rm mix}" in text and r"3\cdot8" in text,
                "Appendix A must retain the 3x8 mixing-channel derivation", failures)
        require(r"\Phi_{\rm mix}" in text and r"24\pi" in text,
                "Appendix A must retain the 24pi mixing-phase measure", failures)

    if app_spinor.is_file():
        text = app_spinor.read_text(encoding="utf-8")
        require(r"N_{\rm mix}=N_F(N_F^2-1)=3(3^2-1)=24" in text,
                "Information-spinor crosswalk must retain canonical 3x8 mixing count", failures)
        require(r"3\dim\mathfrak{su}(3)_F" in text and r"|S_4|" in text,
                "Information-spinor crosswalk must retain tetrahedral order crosscheck", failures)

    if app_i.is_file():
        text = app_i.read_text(encoding="utf-8")
        require("TIR_SELECTED_LEGACY_REPRODUCIBILITY_V11_1" in text,
                "Source-code appendix must describe the selected legacy reproducibility schema", failures)
        require("kappa_phase_rate_identity_v11_1.py" in text,
                "Source-code appendix must link the exact κ phase-rate validator", failures)
        require("review_source_contract_v11_1.py" in text,
                "Source-code appendix must link the review source contract", failures)

    if app_p.is_file():
        text = app_p.read_text(encoding="utf-8")
        require(text.count("% CITATION_CONTEXT_V10_9_BEGIN") == 1
                and text.count("% CITATION_CONTEXT_V10_9_END") == 1,
                "Secret-half Appendix P must retain one established-context block", failures)
        require(all(key in text for key in ("shannon1948", "Fisher1925", "Rao1945")),
                "Secret-half Appendix P must retain Shannon and Fisher–Rao sources", failures)
        require(r"\label{eq:self-duality-not-extremality}" in text,
                "Secret-half Appendix P must retain self-duality boundary", failures)

    if ch02.is_file():
        text = ch02.read_text(encoding="utf-8")
        require("A full-sphere solid angle $4\\pi$ instead gives magnitude $2\\pi$" in text,
                "Chapter 2 must retain corrected full-sphere Berry normalization", failures)
        require(r"\label{eq:mixing-channel-count}" in text,
                "Chapter 2 must expose mixing-channel-count equation", failures)
        require(r"\label{eq:mixing-phase-measure}" in text,
                "Chapter 2 must expose mixing-phase-measure equation", failures)
        require(r"\label{eq:kappa_construction}" in text,
                "Chapter 2 must expose κ construction equation", failures)

    if cross_review.is_file():
        text = cross_review.read_text(encoding="utf-8")
        lowered = text.lower()
        has_reciprocal_boundary = (
            "reciprocal symmetry" in lowered
            and ("does **not**" in lowered or r"\not\Rightarrow" in text
                 or "false in declared stage m universe" in lowered)
        )
        require(has_reciprocal_boundary,
                "Cross-review record must retain the negative self-duality boundary", failures)

    if legacy_runner.is_file():
        source = legacy_runner.read_text(encoding="utf-8")
        try:
            compile(source, str(legacy_runner), "exec")
        except SyntaxError as exc:
            failures.append(f"legacy runner syntax failure: {exc}")
        require("Selected legacy reproducibility subset only" in source,
                "Legacy runner must retain its technical/physical scope label", failures)
        require('"selected_check_count"' in source,
                "Legacy runner must expose the selected check count", failures)

    return {
        "schema": "TIR_REVIEW_SOURCE_CONTRACT_CURRENT",
        "review_date": "2026-08-29",
        "kappa_provenance": "SU3F_3x8_MIXING_PLUS_HALF_TURN",
        "required_files": [str(path.relative_to(ROOT)) for path in required_paths],
        "failure_count": len(failures),
        "failures": failures,
        "technical_status": "PASS" if not failures else "FAIL",
    }


def main() -> None:
    receipt = build_receipt()
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if receipt["technical_status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
