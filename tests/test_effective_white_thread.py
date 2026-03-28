from src.ciel_foundations.solvers.effective_white_thread_solver import effective_white_thread, normalize_weights


def test_normalize_weights_returns_convex_coefficients():
    alpha = normalize_weights([2.0, 3.0, 5.0])
    assert abs(sum(alpha) - 1.0) < 1e-12
    assert all(a >= 0.0 for a in alpha)


def test_effective_white_thread_reduces_to_primitive_for_single_channel():
    z = effective_white_thread([0.3 + 0.4j], [1.0])
    assert abs(z - (0.3 + 0.4j)) < 1e-12


def test_effective_white_thread_remains_bounded_for_bounded_primitives():
    z = effective_white_thread([0.6 + 0.0j, 0.0 + 0.8j], [0.5, 0.5])
    assert abs(z) <= 1.0 + 1e-12
