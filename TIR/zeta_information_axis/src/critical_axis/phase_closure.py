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


def berry_turn_phase(sigma: Fraction | int) -> Fraction:
    """Return the normalized Berry phase class for the latitude convention used by TIR.

    The radian phase is gamma_B = -2*pi*(1-sigma), so gamma_B/(2*pi)
    is exactly -(1-sigma) mod 1.  No numerical value of pi is required.
    """
    p = as_fraction(sigma)
    if p < 0 or p > 1:
        raise ValueError("sigma must lie in [0, 1]")
    return mod_one(-(1 - p))


def aharonov_bohm_turn_phase(flux_ratio: Fraction | int) -> Fraction:
    """Return the normalized AB phase class q_AB = Phi/Phi_0 mod 1.

    In the standard convention gamma_AB = 2*pi*(Phi/Phi_0).  The flux ratio
    is therefore the intrinsic turn coordinate of the U(1) holonomy.
    """
    return mod_one(as_fraction(flux_ratio))


def spinor_sheet_sign(projective_winding: int) -> int:
    """Spin-1/2 sheet sign after an integer number of projective recurrences."""
    if not isinstance(projective_winding, int):
        raise TypeError("projective_winding must be an integer")
    return -1 if projective_winding % 2 else 1


def mixing_channel_count(n_flavours: int = 3) -> int:
    """Return N_F * dim(su(N_F)) = N_F*(N_F^2-1)."""
    if not isinstance(n_flavours, int):
        raise TypeError("n_flavours must be an integer")
    if n_flavours < 2:
        raise ValueError("n_flavours must be at least 2")
    return n_flavours * (n_flavours * n_flavours - 1)


def normalized_mixing_measure(n_flavours: int = 3) -> Fraction:
    """Total normalized-turn measure for one half-turn per mixing channel."""
    return Fraction(mixing_channel_count(n_flavours), 2)


def ln2_per_normalized_mixing_turn_factor(n_flavours: int = 3) -> Fraction:
    """Exact rational factor multiplying ln(2) in the normalized-turn coefficient."""
    return Fraction(1, 1) / normalized_mixing_measure(n_flavours)


def radian_kappa_from_normalized_structure(n_flavours: int = 3) -> float:
    """Evaluate the radian coefficient obtained from the normalized TIR structure."""
    turn_factor = ln2_per_normalized_mixing_turn_factor(n_flavours)
    return math.log(2.0) * float(turn_factor) / TAU


def structural_kappa_certificate(n_flavours: int = 3) -> dict[str, object]:
    """Return exact structural factors and the radian conversion witness."""
    channels = mixing_channel_count(n_flavours)
    half_turn = Fraction(1, 2)
    measure = normalized_mixing_measure(n_flavours)
    turn_factor = ln2_per_normalized_mixing_turn_factor(n_flavours)
    return {
        "n_flavours": n_flavours,
        "mixing_channels": channels,
        "normalized_half_turn": half_turn,
        "normalized_mixing_measure": measure,
        "ln2_per_normalized_turn_factor": turn_factor,
        "radian_jacobian": "1/(2*pi)",
        "radian_kappa": radian_kappa_from_normalized_structure(n_flavours),
    }


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
