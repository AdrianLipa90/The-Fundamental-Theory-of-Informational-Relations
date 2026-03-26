import math

from src.ciel_foundations.closure.euler import closure_defect, closure_magnitude
from src.ciel_foundations.holonomy.berry import (
    berry_connection_phi,
    berry_phase_latitude,
    is_spin_half_cycle,
    spinor_sign_from_phase,
)


def test_berry_connection_equator_is_one_half_for_default_charge():
    assert abs(berry_connection_phi(math.pi / 2.0) - 0.5) < 1e-12


def test_equatorial_berry_phase_has_pi_magnitude():
    phase = berry_phase_latitude(math.pi / 2.0)
    assert abs(abs(phase) - math.pi) < 1e-12


def test_spin_half_cycle_returns_minus_one():
    z = spinor_sign_from_phase(math.pi)
    assert abs(z.real + 1.0) < 1e-12
    assert abs(z.imag) < 1e-12
    assert is_spin_half_cycle(math.pi)


def test_closure_defect_pair_zero_and_pi_closes_exactly():
    defect = closure_defect([0.0, math.pi])
    assert abs(defect) < 1e-12
    assert abs(closure_magnitude([0.0, math.pi])) < 1e-12
