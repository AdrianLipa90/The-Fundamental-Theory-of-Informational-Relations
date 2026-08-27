#!/usr/bin/env python3
"""Static source-contract audit for the 2026-08-07 TIR ↔ half review.

The publication build contains generators and post-generation review patches.
This audit makes the expected final source topology explicit so a later edit
cannot silently drop the κ closure, reintroduce the old Berry normalization,
or orphan the new cross-relation and reproducibility architecture.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MONOGRAPH = ROOT / "monograph"


def count(path: Path, needle: str) -> int:
    """Count literal occurrences of ``needle`` in one UTF-8 source file."""
    return path.read_text(encoding="utf-8").count(needle)


def require(condition: bool, message: str, failures: list[str]) -> None:
    """Append ``message`` when a source-contract condition is false."""
    if not condition:
        failures.append(message)


def build_receipt() -> dict[str, object]:
    """Audit the reviewed live-source invariants and return a JSON receipt."""
    failures: list[str] = []

    root_tex = MONOGRAPH / "metatime_monograph.tex"
    app_a = MONOGRAPH / "appendices" / "appA_kappa_derivation.tex"
    app_i = MONOGRAPH / "appendices" / "appI_source_code.tex"
    app_p = MONOGRAPH / "appendices" / "appP_secret_half_cross_relation.tex"
    ch02 = MONOGRAPH / "chapters" / "ch02_metatime_framework.tex"
    cross_review = ROOT / "docs" / "cross_reviews" / "TIR_SECRET_HALF_2026-08-07.md"
    phase_patch = MONOGRAPH / "apply_kappa_phase_rate_patch.py"
    paper_patch = ROOT / "apply_metatime_paper_review_patch.py"
    legacy_runner = ROOT / "run_audit.py"
    phase_validator = ROOT / "validation" / "kappa_phase_rate_identity_v11_1.py"

    required_paths = (
        root_tex,
        app_a,
        app_i,
        app_p,
        ch02,
        cross_review,
        phase_patch,
        paper_patch,
        legacy_runner,
        phase_validator,
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
        require(
            count(app_a, r"\label{app:kappa-phase-rate}") == 1,
            "Appendix A must contain exactly one κ phase-rate section label",
            failures,
        )
        require(
            count(app_a, r"\label{app:kappa-constraint-manifold}") == 1,
            "Appendix A must contain exactly one κ constraint-manifold label",
            failures,
        )
        require(
            r"\frac{\ln2}{12}" in app_a.read_text(encoding="utf-8"),
            "Appendix A must retain the ln2/12 closed form",
            failures,
        )

    if app_i.is_file():
        text = app_i.read_text(encoding="utf-8")
        require(
            "TIR_SELECTED_LEGACY_REPRODUCIBILITY_V11_1" in text,
            "Source-code appendix must describe the selected legacy reproducibility schema",
            failures,
        )
        require(
            "kappa_phase_rate_identity_v11_1.py" in text,
            "Source-code appendix must link the exact κ phase-rate validator",
            failures,
        )
        require(
            "review_source_contract_v11_1.py" in text,
            "Source-code appendix must link the review source contract",
            failures,
        )
        require(
            "all 26 SM parameters" not in text.lower(),
            "Source-code appendix must not retain the stale all-26-parameters claim",
            failures,
        )

    if app_p.is_file():
        text = app_p.read_text(encoding="utf-8")
        require(
            text.count("% CITATION_CONTEXT_V10_9_BEGIN") == 1
            and text.count("% CITATION_CONTEXT_V10_9_END") == 1,
            "Appendix P must retain one delimited established-context block",
            failures,
        )
        require(
            all(key in text for key in ("shannon1948", "Fisher1925", "Rao1945")),
            "Appendix P established context must cite Shannon and Fisher–Rao sources",
            failures,
        )
        require(
            r"\label{eq:self-duality-not-extremality}" in text,
            "Appendix P must retain the self-duality-not-extremality boundary",
            failures,
        )

    if ch02.is_file():
        text = ch02.read_text(encoding="utf-8")
        require(
            "A full-sphere solid angle $4\\pi$ instead gives magnitude $2\\pi$" in text,
            "Chapter 2 must retain the corrected full-sphere Berry normalization",
            failures,
        )
        require(
            "the Berry phase is:\n\n\\begin{equation}\n\\gamma_{\\text{spin}} = \\frac{4\\pi}{2} = \\pi" not in text,
            "Chapter 2 must not reintroduce the old 4π/2=π statement",
            failures,
        )

    if cross_review.is_file():
        text = cross_review.read_text(encoding="utf-8")
        lowered = text.lower()
        has_reciprocal_boundary = (
            "reciprocal symmetry" in lowered
            and (
                "does **not**" in lowered
                or r"\not\Rightarrow" in text
                or "false in declared stage m universe" in lowered
            )
        )
        require(
            has_reciprocal_boundary,
            "Cross-review record must retain the negative self-duality boundary",
            failures,
        )

    if legacy_runner.is_file():
        source = legacy_runner.read_text(encoding="utf-8")
        try:
            compile(source, str(legacy_runner), "exec")
        except SyntaxError as exc:
            failures.append(f"legacy runner syntax failure: {exc}")
        require(
            "Selected legacy reproducibility subset only" in source,
            "Legacy runner must retain its technical-vs-physical claim boundary",
            failures,
        )
        require(
            '"selected_check_count"' in source,
            "Legacy runner must expose the selected check count",
            failures,
        )

    return {
        "schema": "TIR_REVIEW_SOURCE_CONTRACT_V11_1",
        "review_date": "2026-08-07",
        "required_files": [str(path.relative_to(ROOT)) for path in required_paths],
        "failure_count": len(failures),
        "failures": failures,
        "technical_status": "PASS" if not failures else "FAIL",
    }


def main() -> None:
    """Print the deterministic source-contract receipt and fail on violations."""
    receipt = build_receipt()
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if receipt["technical_status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
