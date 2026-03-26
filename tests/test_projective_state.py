import math

from src.ciel_foundations.geometry.projective_state import (
    bloch_vector,
    fs_distance,
    normalize_state,
    state_from_angles,
)


def test_normalize_state_unit_norm():
    psi = normalize_state((3 + 0j, 4 + 0j))
    n2 = abs(psi[0]) ** 2 + abs(psi[1]) ** 2
    assert abs(n2 - 1.0) < 1e-12


def test_bloch_vector_for_basis_state_zero_is_north_pole():
    x, y, z = bloch_vector((1 + 0j, 0 + 0j))
    assert abs(x) < 1e-12
    assert abs(y) < 1e-12
    assert abs(z - 1.0) < 1e-12


def test_fs_distance_for_orthogonal_states_is_pi_over_two():
    d = fs_distance((1 + 0j, 0 + 0j), (0 + 0j, 1 + 0j))
    assert abs(d - math.pi / 2.0) < 1e-12


def test_state_from_angles_zero_is_basis_zero():
    psi = state_from_angles(0.0, 0.0)
    assert abs(psi[0] - 1.0) < 1e-12
    assert abs(psi[1]) < 1e-12
