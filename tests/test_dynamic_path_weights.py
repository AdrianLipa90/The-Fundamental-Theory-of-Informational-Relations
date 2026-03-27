from src.ciel_foundations.solvers.dynamic_path_weights_solver import effective_white_thread_from_actions, path_action, softmax_weights


def test_softmax_weights_are_normalized_and_nonnegative():
    alpha = softmax_weights([1.0, 2.0, 3.0], sigma=1.0)
    assert abs(sum(alpha) - 1.0) < 1e-12
    assert all(a >= 0.0 for a in alpha)


def test_lower_action_receives_higher_weight_for_positive_sigma():
    alpha = softmax_weights([1.0, 2.0], sigma=1.0)
    assert alpha[0] > alpha[1]


def test_path_action_is_linear_in_registered_components():
    s = path_action(1.0, 0.2, 0.3, 0.4, alpha=2.0, beta=3.0, kappa=4.0, mu=5.0)
    assert abs(s - (2.0 * 1.0 + 3.0 * 0.2 + 4.0 * 0.3 + 5.0 * 0.4)) < 1e-12


def test_effective_white_thread_from_actions_prefers_lower_action_path():
    z = effective_white_thread_from_actions([1.0 + 0j, 0.0 + 1.0j], [0.0, 5.0], sigma=2.0)
    assert z.real > z.imag
