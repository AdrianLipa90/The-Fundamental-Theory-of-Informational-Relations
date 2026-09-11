from __future__ import annotations

import cmath
import math
from fractions import Fraction
from typing import Iterable


TAU = 2.0 * math.pi


def as_fraction(value: Fraction | int) -> Fraction:
    """Return an exact rational turn value."""
    return value if isinstance(value, Fraction) else Fraction(value)


def mod_one(value: Fraction | int) -> Fraction:
    """Reduce an exact turn coordinate into the canonical [0, 1) representative."""
    q = as_fraction(value)
    return q % 1


def exact_turn_sum(turns: Iterable[Fraction | int]) -> tuple[Fraction, Fraction]:
    """Return the lifted total and its exact R/Z residue, without using pi."""
    total = sum((as_fraction(turn) for turn in turns), Fraction(0, 1))
    return total, mod_one(total)


def is_exactly_closed(turns: Iterable[Fraction | int]) -> bool:
    """Test exact closure in R/Z using rational arithmetic only."""
    _, residue = exact_turn_sum(turns)
    return residue == 0


def winding_from_lift(start: Fraction | int, end: Fraction | int) -> int:
    """Return integer winding for a lifted path whose endpoints differ by whole turns."""
    delta = as_fraction(end) - as_fraction(start)
    if delta.denominator != 1:
        raise ValueError("lifted endpoint difference is not an integer winding")
    return delta.numerator


def radian_phase(q: Fraction | int) -> float:
    """Map normalized turns to the standard radian representative phi = 2*pi*q."""
    return TAU * float(as_fraction(q))


def normalized_holonomy(q: Fraction | int) -> complex:
    """Evaluate the U(1) character exp(2*pi*i*q) from a normalized turn."""
    return cmath.exp(2j * math.pi * float(mod_one(q)))


def radian_holonomy(phi: float) -> complex:
    """Evaluate the same U(1) holonomy from a radian phase."""
    return cmath.exp(1j * phi)


def spinor_sheet_sign(projective_winding: int) -> int:
    """Spin-1/2 sheet sign after an integer number of projective recurrences."""
    if not isinstance(projective_winding, int):
        raise TypeError("projective_winding must be an integer")
    return -1 if projective_winding % 2 else 1


def rational_cycle_certificate(order: int) -> dict[str, object]:
    """Construct an exact n-step 1/n cycle closure certificate in normalized turns."""
    if order <= 0:
        raise ValueError("order must be positive")
    step = Fraction(1, order)
    total, residue = exact_turn_sum([step] * order)
    return {
        "order": order,
        "step": step,
        "lifted_total": total,
        "residue_mod_1": residue,
        "winding": winding_from_lift(0, total),
        "closed": residue == 0,
        "uses_pi_for_exact_closure": False,
    }
