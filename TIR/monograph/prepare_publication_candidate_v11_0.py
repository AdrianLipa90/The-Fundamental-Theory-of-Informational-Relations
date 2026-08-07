#!/usr/bin/env python3
from __future__ import annotations

import re
import runpy
from pathlib import Path

_original_sub = re.sub


def _literal_hyperref_sub(pattern, repl, string, count=0, flags=0):
    if isinstance(repl, str) and "hyperref" in str(pattern):
        return _original_sub(
            pattern,
            lambda _match: repl,
            string,
            count=count,
            flags=flags,
        )
    return _original_sub(pattern, repl, string, count=count, flags=flags)


def _deduplicate_publication_macros(root: Path) -> None:
    """Keep exactly one copy of publication status macros after source preparation.

    The historical implementation inserts these definitions by textual replacement.
    The wrapper is the canonical entrypoint, so it enforces idempotence after every
    implementation run rather than relying on CI-only cleanup.
    """
    path = root / "metatime_monograph.tex"
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    targets = {
        r"\newcommand{\claimstatus}[1]{\par\noindent\textbf{Claim status: #1}\par}",
        r"\newcommand{\datasetstatus}[1]{\par\noindent\textbf{Data status: #1}\par}",
    }
    seen: set[str] = set()
    output: list[str] = []
    for line in lines:
        stripped = line.rstrip("\r\n")
        if stripped in targets:
            if stripped in seen:
                continue
            seen.add(stripped)
        output.append(line)
    missing = targets - seen
    if missing:
        raise SystemExit(f"Missing publication status macro definitions: {sorted(missing)}")
    path.write_text("".join(output), encoding="utf-8")


ROOT = Path(__file__).resolve().parent
re.sub = _literal_hyperref_sub
runpy.run_path(
    str(ROOT / "prepare_publication_candidate_v11_0_impl.py"),
    run_name="__main__",
)
_deduplicate_publication_macros(ROOT)
