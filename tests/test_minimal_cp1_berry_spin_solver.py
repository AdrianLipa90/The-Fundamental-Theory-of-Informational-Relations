from src.ciel_foundations.solvers.minimal_cp1_berry_spin_solver import (
    final_equatorial_spinor_sign,
    solve_equatorial_cycle,
)


def test_solver_returns_expected_number_of_rows():
    rows = solve_equatorial_cycle(num_steps=8)
    assert len(rows) == 9


def test_solver_final_sign_is_minus_one_for_full_equatorial_cycle():
    z = final_equatorial_spinor_sign(num_steps=16)
    assert abs(z.real + 1.0) < 1e-12
    assert abs(z.imag) < 1e-12
