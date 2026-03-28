from pathlib import Path

from src.ciel_foundations.solvers.repo_object_state_extractor import (
    discover_repository_files,
    extract_repository_object_states,
)


def _build_fixture(root: Path) -> None:
    (root / "definitions").mkdir()
    (root / "src/ciel_foundations/solvers").mkdir(parents=True)
    (root / "README.md").write_text(
        "# Demo\nSee `definitions/DEF-0001-projective-ray-and-cp1.md` and `src/ciel_foundations/solvers/demo_solver.py`.\n",
        encoding="utf-8",
    )
    (root / "definitions/DEF-0001-projective-ray-and-cp1.md").write_text(
        "# DEF-0001\nDepends on `src/ciel_foundations/solvers/demo_solver.py`.\n",
        encoding="utf-8",
    )
    (root / "src/ciel_foundations/solvers/demo_solver.py").write_text(
        '"""Demo solver."""\n\nVALUE = 1\n',
        encoding="utf-8",
    )


def test_discover_repository_files_lists_fixture_paths(tmp_path: Path):
    _build_fixture(tmp_path)
    files = discover_repository_files(tmp_path)
    assert files == [
        "README.md",
        "definitions/DEF-0001-projective-ray-and-cp1.md",
        "src/ciel_foundations/solvers/demo_solver.py",
    ]


def test_extractor_builds_fixture_couplings_and_normalized_energy(tmp_path: Path):
    _build_fixture(tmp_path)
    rows, couplings = extract_repository_object_states(tmp_path)
    assert len(rows) == 3
    assert len(couplings) == 3
    assert abs(sum(float(r["norm_energy"]) for r in rows) - 1.0) < 1e-12
    ids = {r["id"] for r in rows}
    assert ids == {
        "README.md",
        "definitions/DEF-0001-projective-ray-and-cp1.md",
        "src/ciel_foundations/solvers/demo_solver.py",
    }
    edges = {(c["source"], c["target"]) for c in couplings}
    assert ("README.md", "definitions/DEF-0001-projective-ray-and-cp1.md") in edges
    assert ("README.md", "src/ciel_foundations/solvers/demo_solver.py") in edges
    assert ("definitions/DEF-0001-projective-ray-and-cp1.md", "src/ciel_foundations/solvers/demo_solver.py") in edges
