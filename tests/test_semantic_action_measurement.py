import math

from src.ciel_foundations.solvers.semantic_action_measurement_solver import (
    closure_defect_cost,
    phase_cost_discrete,
    semantic_action_full,
    semantic_action_online,
    semantic_length_discrete,
    truth_audit_cost,
    truth_structural_cost,
)


def test_phase_cost_is_zero_for_constant_phase():
    assert abs(phase_cost_discrete([0.2, 0.2, 0.2])) < 1e-12


def test_closure_defect_vanishes_for_three_phase_euler_closure():
    row = [0.0, 2.0 * math.pi / 3.0, 4.0 * math.pi / 3.0]
    assert closure_defect_cost([row]) < 1e-12


def test_truth_structural_cost_is_zero_for_perfect_resonance():
    assert abs(truth_structural_cost([1.0, 1.0, 1.0])) < 1e-12


def test_truth_audit_cost_counts_registered_failures():
    assert abs(truth_audit_cost(1, 1, 0, 0, 1, 10) - 0.3) < 1e-12


def test_online_and_full_action_decompose_correctly():
    L = semantic_length_discrete([1.0, 2.0], [1.0, 4.0])
    P = phase_cost_discrete([0.0, math.pi])
    D = closure_defect_cost([[0.0, 0.0]])
    T = truth_structural_cost([0.5, 1.0])
    online = semantic_action_online(L, P, D, T, alpha=1.0, beta=2.0, kappa=3.0, mu=4.0)
    full = semantic_action_full(online, 0.25, nu=5.0)
    assert abs(full - (online + 5.0 * 0.25)) < 1e-12
