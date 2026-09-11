from fractions import Fraction

import pytest

from critical_axis.phase_closure import (
    exact_turn_sum,
    is_exactly_closed,
    normalized_holonomy,
    radian_holonomy,
    radian_phase,
    rational_cycle_certificate,
    spinor_sheet_sign,
    winding_from_lift,
)


@pytest.mark.parametrize("order", [2, 3, 4, 5, 7, 12, 24, 60])
def test_rational_cycles_close_exactly_without_pi(order: int) -> None:
    certificate = rational_cycle_certificate(order)
    assert certificate["lifted_total"] == Fraction(1, 1)
    assert certificate["residue_mod_1"] == Fraction(0, 1)
    assert certificate["winding"] == 1
    assert certificate["closed"] is True
    assert certificate["uses_pi_for_exact_closure"] is False


def test_exact_turn_arithmetic_distinguishes_closed_and_open_paths() -> None:
    total, residue = exact_turn_sum([Fraction(1, 7)] * 6)
    assert total == Fraction(6, 7)
    assert residue == Fraction(6, 7)
    assert not is_exactly_closed([Fraction(1, 7)] * 6)
    assert is_exactly_closed([Fraction(1, 7)] * 7)


def test_winding_is_integer_lift_difference() -> None:
    assert winding_from_lift(Fraction(1, 3), Fraction(7, 3)) == 2
    with pytest.raises(ValueError):
        winding_from_lift(0, Fraction(3, 2))


@pytest.mark.parametrize("q", [Fraction(0), Fraction(1, 2), Fraction(1, 3), Fraction(2, 7), Fraction(5, 12)])
def test_normalized_and_radian_holonomy_are_same_representation(q: Fraction) -> None:
    z_turn = normalized_holonomy(q)
    z_rad = radian_holonomy(radian_phase(q))
    assert abs(z_turn - z_rad) < 1e-12


def test_spin_half_sheet_closes_after_two_projective_windings() -> None:
    assert spinor_sheet_sign(0) == 1
    assert spinor_sheet_sign(1) == -1
    assert spinor_sheet_sign(2) == 1
    assert spinor_sheet_sign(3) == -1


def test_normalized_closure_has_zero_exact_residual_for_full_turn() -> None:
    total, residue = exact_turn_sum([Fraction(1, 24)] * 24)
    assert total == 1
    assert residue == 0
