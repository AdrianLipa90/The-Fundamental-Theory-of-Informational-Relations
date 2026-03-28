import math
import numpy as np

from src.ciel_foundations.solvers.object_state_energy_solver import (
    amplitudes_from_normalized_energy,
    local_states,
    normalize_energies,
    phase_from_seed_text,
    raw_energy_linear,
)


def test_normalized_energies_sum_to_one():
    vals = normalize_energies([2.0, 3.0, 5.0])
    assert abs(float(vals.sum()) - 1.0) < 1e-12


def test_amplitudes_squared_sum_to_one():
    amps = amplitudes_from_normalized_energy([0.2, 0.3, 0.5])
    assert abs(float(np.sum(amps**2)) - 1.0) < 1e-12


def test_phase_from_seed_text_is_in_range():
    phi = phase_from_seed_text("toy-seed-1")
    assert 0.0 <= phi < 2.0 * math.pi


def test_local_state_magnitude_equals_amplitude():
    amps = np.array([0.4, 0.5])
    phases = np.array([0.1, 1.2])
    psi = local_states(amps, phases)
    assert np.allclose(np.abs(psi), amps)


def test_raw_energy_linear_matches_registered_default_sum():
    val = raw_energy_linear(0.4, 0.2, 1.0, 0.3, 0.5, 0.8, 0.6)
    assert abs(val - 3.8) < 1e-12
