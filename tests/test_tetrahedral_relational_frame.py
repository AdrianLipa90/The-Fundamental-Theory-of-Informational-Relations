import math

from src.ciel_foundations.solvers.tetrahedral_relational_frame_solver import (
    pairwise_dot_matrix,
    regular_tetrahedron_vertices,
    relative_phase_triple,
)


def test_regular_tetrahedron_vertices_lie_on_unit_sphere():
    for v in regular_tetrahedron_vertices():
        n2 = v[0] ** 2 + v[1] ** 2 + v[2] ** 2
        assert abs(n2 - 1.0) < 1e-12


def test_regular_tetrahedron_pairwise_dots_match_definition():
    mat = pairwise_dot_matrix()
    for i in range(4):
        for j in range(4):
            expected = 1.0 if i == j else -1.0 / 3.0
            assert abs(mat[i][j] - expected) < 1e-12


def test_relative_phase_triple_is_global_phase_invariant():
    phases = [0.1, 0.4, 1.2, -0.7]
    shifted = [p + 0.9 for p in phases]
    a = relative_phase_triple(phases)
    b = relative_phase_triple(shifted)
    for x, y in zip(a, b):
        assert abs(x - y) < 1e-12
