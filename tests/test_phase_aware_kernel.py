import math

from src.ciel_foundations.solvers.phase_aware_kernel_solver import closure_weight, pairwise_kernel_from_holonomy, phase_alignment_weight


def test_phase_alignment_weight_is_symmetric_under_exchange():
    a = phase_alignment_weight(0.7)
    b = phase_alignment_weight(-0.7)
    assert abs(a - b) < 1e-12


def test_closure_weight_decreases_with_larger_defect():
    assert closure_weight(0.0) > closure_weight(1.0)


def test_pairwise_kernel_is_nonnegative():
    Aij = pairwise_kernel_from_holonomy(2.0, 0.1, 1.2, 0.4)
    assert Aij >= 0.0


def test_pairwise_kernel_reduces_to_holonomy_when_modulators_are_trivial():
    Aij = pairwise_kernel_from_holonomy(2.0, 0.5, 0.5, 0.0, lam=0.0, mu=0.0)
    assert abs(Aij - 2.0) < 1e-12
