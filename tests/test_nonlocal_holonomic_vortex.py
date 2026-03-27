import math

from src.ciel_foundations.solvers.nonlocal_holonomic_vortex_solver import (
    coriolis_term,
    is_nonlocal_holonomic_vortex,
    order_parameter,
    point_on_equator,
    poles_from_axis,
    spacetime_circulation,
)


def test_poles_from_axis_returns_antipodal_unit_vectors():
    p_plus, p_minus = poles_from_axis((0.0, 0.0, 2.0))
    assert p_plus == (0.0, 0.0, 1.0)
    assert p_minus == (-0.0, -0.0, -1.0)


def test_point_on_equator_for_z_axis_accepts_x_direction():
    assert point_on_equator((1.0, 0.0, 0.0), (0.0, 0.0, 1.0))


def test_order_parameter_returns_expected_complex_value():
    z = order_parameter(4.0, math.pi / 2.0)
    assert abs(z.real) < 1e-12
    assert abs(z.imag - 2.0) < 1e-12


def test_coriolis_term_for_z_axis_and_x_velocity_points_minus_y():
    fx, fy, fz = coriolis_term((0.0, 0.0, 1.0), (1.0, 0.0, 0.0))
    assert abs(fx) < 1e-12
    assert abs(fy + 2.0) < 1e-12
    assert abs(fz) < 1e-12


def test_nonlocal_holonomic_vortex_has_nonzero_spacetime_circulation():
    displacements = [
        (0.0, 1.0, 0.0, 0.0),
        (1.0, 0.0, 0.0, 0.0),
        (0.0, -1.0, 0.0, 0.0),
        (-1.0, 0.0, 0.0, 0.0),
    ]
    u_forms = [
        (0.0, 1.0, 0.0, 0.0),
        (1.0, 0.0, 0.0, 0.0),
        (0.0, -1.0, 0.0, 0.0),
        (-1.0, 0.0, 0.0, 0.0),
    ]
    assert abs(spacetime_circulation(displacements, u_forms) - 4.0) < 1e-12
    assert is_nonlocal_holonomic_vortex(displacements, u_forms)
