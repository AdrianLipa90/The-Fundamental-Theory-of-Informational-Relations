import math

from src.ciel_foundations.solvers.tau_from_coupling_solver import laplacian_matrix, log_tau_from_coupling, strength_vector, tau_from_coupling


def test_strength_vector_for_simple_kernel():
    A = [[0.0, 1.0], [1.0, 0.0]]
    assert strength_vector(A) == [1.0, 1.0]


def test_laplacian_matrix_for_simple_kernel():
    A = [[0.0, 1.0], [1.0, 0.0]]
    assert laplacian_matrix(A) == [[1.0, -1.0], [-1.0, 1.0]]


def test_tau_from_uniform_kernel_is_degenerate():
    A = [
        [0.0, 1.0, 1.0],
        [1.0, 0.0, 1.0],
        [1.0, 1.0, 0.0],
    ]
    taus = tau_from_coupling(A)
    assert all(abs(t - 1.0) < 1e-12 for t in taus)


def test_tau_from_heterogeneous_kernel_is_positive_and_split():
    A = [
        [0.0, 1.0, 0.2],
        [1.0, 0.0, 0.5],
        [0.2, 0.5, 0.0],
    ]
    taus = tau_from_coupling(A)
    assert all(t > 0.0 for t in taus)
    assert max(taus) - min(taus) > 1e-6


def test_log_tau_solution_is_gauge_fixed_to_zero_mean():
    A = [
        [0.0, 1.0, 0.2],
        [1.0, 0.0, 0.5],
        [0.2, 0.5, 0.0],
    ]
    xi = log_tau_from_coupling(A)
    assert abs(sum(xi)) < 1e-12
