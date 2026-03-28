#!/usr/bin/env python3
"""Export real repository object-state and coupling tables from the current checkout."""

from __future__ import annotations

import argparse
from pathlib import Path

from src.ciel_foundations.solvers.repo_object_state_extractor import write_repository_state_exports


def main() -> int:
    parser = argparse.ArgumentParser(description="Export objects_state.csv and couplings.csv from the current repository checkout.")
    parser.add_argument("--repo-root", default=".", help="Path to the repository root. Defaults to the current directory.")
    parser.add_argument("--objects-out", default="exports/objects_state.csv", help="Output path for objects_state.csv")
    parser.add_argument("--couplings-out", default="exports/couplings.csv", help="Output path for couplings.csv")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    objects_out = Path(args.objects_out)
    couplings_out = Path(args.couplings_out)

    rows, couplings = write_repository_state_exports(repo_root, objects_out, couplings_out)

    print(f"repo_root={repo_root}")
    print(f"objects_rows={len(rows)}")
    print(f"couplings_rows={len(couplings)}")
    print(f"objects_out={objects_out}")
    print(f"couplings_out={couplings_out}")
    print(f"norm_energy_sum={sum(float(r['norm_energy']) for r in rows):.12f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
