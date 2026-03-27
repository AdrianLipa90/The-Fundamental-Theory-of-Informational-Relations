from src.ciel_foundations.solvers.piko_fractal_spine_solver import build_spine_snapshot, spine_consistency_score


def test_piko_fractal_spine_snapshot_contains_all_layers():
    snap = build_spine_snapshot()
    assert "cp1_bloch" in snap
    assert "tetrahedron_vertices" in snap
    assert "local_poles" in snap
    assert "nonlocal_vortex" in snap


def test_piko_fractal_spine_consistency_score_is_one_for_registered_snapshot():
    snap = build_spine_snapshot()
    assert abs(spine_consistency_score(snap) - 1.0) < 1e-12
