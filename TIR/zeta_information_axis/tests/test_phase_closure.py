import math
from fractions import Fraction

import pytest

from critical_axis.phase_closure import (
    aharonov_bohm_turn_phase,
    berry_turn_phase,
    exact_turn_sum,
    is_exactly_closed,
    ln2_per_normalized_mixing_turn_factor,
    mixing_channel_count,
    normalized_holonomy,
    normalized_mixing_measure,
    radian_holonomy,
    radian_kappa_from_normalized_structure,
    radian_phase,
    rational_cycle_certificate,
    spinor_sheet_sign,
    structural_kappa_certificate,
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


def test_balanced_berry_phase_is_exact_half_turn_class() -> None:
    q_berry = berry_turn_phase(Fraction(1, 2))
    assert q_berry == Fraction(1, 2)
    assert abs(normalized_holonomy(q_berry) + 1) < 1e-12


@pytest.mark.parametrize(
    ("sigma", "expected"),
    [
        (Fraction(0), Fraction(0)),
        (Fraction(1, 4), Fraction(1, 4)),
        (Fraction(1, 2), Fraction(1, 2)),
        (Fraction(3, 4), Fraction(3, 4)),
        (Fraction(1), Fraction(0)),
    ],
)
def test_berry_normalization_removes_numeric_pi(sigma: Fraction, expected: Fraction) -> None:
    assert berry_turn_phase(sigma) == expected


def test_half_flux_quantum_matches_balanced_berry_u1_class() -> None:
    q_ab = aharonov_bohm_turn_phase(Fraction(1, 2))
    q_berry = berry_turn_phase(Fraction(1, 2))
    assert q_ab == q_berry == Fraction(1, 2)
    assert abs(normalized_holonomy(q_ab) + 1) < 1e-12


def test_integer_flux_quantum_is_closed_u1_class() -> None:
    assert aharonov_bohm_turn_phase(1) == 0
    assert aharonov_bohm_turn_phase(3) == 0


def test_three_flavour_structure_forces_twelve_normalized_turns() -> None:
    assert mixing_channel_count(3) == 24
    assert normalized_mixing_measure(3) == Fraction(12, 1)
    assert ln2_per_normalized_mixing_turn_factor(3) == Fraction(1, 12)


def test_radian_kappa_is_jacobian_image_of_normalized_coefficient() -> None:
    expected = math.log(2.0) / (24.0 * math.pi)
    assert math.isclose(radian_kappa_from_normalized_structure(3), expected, rel_tol=0.0, abs_tol=1e-16)


def test_structural_kappa_certificate_preserves_exact_discrete_factors() -> None:
    certificate = structural_kappa_certificate(3)
    assert certificate["mixing_channels"] == 24
    assert certificate["normalized_half_turn"] == Fraction(1, 2)
    assert certificate["normalized_mixing_measure"] == Fraction(12, 1)
    assert certificate["ln2_per_normalized_turn_factor"] == Fraction(1, 12)
    assert certificate["radian_jacobian"] == "1/(2*pi)"


def test_invalid_flavour_carrier_fails_closed() -> None:
    with pytest.raises(ValueError):
        mixing_channel_count(1)
    with pytest.raises(TypeError):
        mixing_channel_count(3.0)  # type: ignore[arg-type]
