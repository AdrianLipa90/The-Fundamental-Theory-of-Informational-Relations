#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "foundations"
SCHEMA = "TIR_MUMMU_MARKDOWN_INTEGRITY_VALIDATION_V0_1"
ALLOWED_CONTROL = {10}  # LF only


def main() -> int:
    files = sorted(ROOT.glob("TIR_MUMMU*.md"))
    checks = []
    for path in files:
        raw = path.read_bytes()
        bad = [(i, b) for i, b in enumerate(raw) if b < 32 and b not in ALLOWED_CONTROL]
        checks.append(
            {
                "path": str(path.relative_to(ROOT.parent)),
                "status": "PASS" if not bad else "FAIL",
                "control_count": len(bad),
                "control_codes": sorted({b for _, b in bad}),
                "first_offsets": [i for i, _ in bad[:12]],
            }
        )

    status = "PASS" if all(c["status"] == "PASS" for c in checks) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "rule": "MUMMU markdown must contain no ASCII control bytes except LF",
        "files_checked": len(checks),
        "failed": sum(c["status"] == "FAIL" for c in checks),
        "checks": checks,
    }
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
