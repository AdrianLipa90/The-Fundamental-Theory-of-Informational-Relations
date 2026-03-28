"""Fixture demo and runtime export for repository object-state extraction."""

from __future__ import annotations

from pathlib import Path
import tempfile

from src.ciel_foundations.solvers.repo_object_state_extractor import write_repository_state_exports


FIXTURE_README = "# Demo\nSee `definitions/DEF-0001-projective-ray-and-cp1.md` and `src/ciel_foundations/solvers/demo_solver.py`.\n"
FIXTURE_DEF = "# DEF-0001\nDepends on `src/ciel_foundations/solvers/demo_solver.py`.\n"
FIXTURE_SOLVER = '"""Demo solver."""\n\nVALUE = 1\n'


def _build_fixture(root: Path) -> None:
    (root / "definitions").mkdir()
    (root / "src/ciel_foundations/solvers").mkdir(parents=True)
    (root / "README.md").write_text(FIXTURE_README, encoding="utf-8")
    (root / "definitions/DEF-0001-projective-ray-and-cp1.md").write_text(FIXTURE_DEF, encoding="utf-8")
    (root / "src/ciel_foundations/solvers/demo_solver.py").write_text(FIXTURE_SOLVER, encoding="utf-8")


def write_fixture_exports(objects_csv: str | Path, couplings_csv: str | Path) -> None:
    with tempfile.TemporaryDirectory() as tmpdir:
        root = Path(tmpdir)
        _build_fixture(root)
        write_repository_state_exports(root, objects_csv, couplings_csv)


if __name__ == "__main__":
    write_fixture_exports(
        "Simulations/results/ART-0010-repo-object-state-fixture-demo.csv",
        "Simulations/results/ART-0011-repo-couplings-fixture-demo.csv",
    )
