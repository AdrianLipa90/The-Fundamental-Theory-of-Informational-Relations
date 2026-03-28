import math

from src.ciel_foundations.solvers.white_thread_primitive_solver import u1_holonomy, u1_holonomy_phase, white_thread_matrix_element


def test_u1_holonomy_has_unit_modulus():
    z = u1_holonomy(math.pi / 3.0)
    assert abs(abs(z) - 1.0) < 1e-12


def test_white_thread_reduces_to_overlap_at_zero_phase():
    psi_i = [1.0 + 0j, 0.0 + 0j]
    psi_j = [1.0 + 0j, 0.0 + 0j]
    z = white_thread_matrix_element(psi_i, psi_j, 0.0)
    assert abs(z - 1.0) < 1e-12


def test_white_thread_amplitude_is_bounded_by_one_for_normalized_states():
    psi_i = [1.0 + 0j, 0.0 + 0j]
    psi_j = [0.6 + 0j, 0.8 + 0j]
    z = white_thread_matrix_element(psi_i, psi_j, math.pi / 5.0)
    assert abs(z) <= 1.0 + 1e-12


def test_holonomy_phase_adds_segment_integrals():
    phase = u1_holonomy_phase([0.2, 0.3, -0.1])
    assert abs(phase - 0.4) < 1e-12
