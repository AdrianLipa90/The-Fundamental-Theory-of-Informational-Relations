"""System-style solver for the minimal CP1/Berry/spin foundations layer."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List

from src.ciel_foundations.closure.euler import closure_defect, closure_magnitude
from src.ciel_foundations.geometry.projective_state import bloch_vector, state_from_angles
from src.ciel_foundations.holonomy.berry import berry_phase_latitude, spinor_sign_from_phase


@dataclass(frozen=True)
class SolverRow:
    step: int
    theta: float
    phi: float
    berry_phase: float
    sign_re: float
    sign_im: float
    closure_abs: float


def solve_equatorial_cycle(num_steps: int = 16) -> List[SolverRow]:
    rows: List[SolverRow] = []
    theta = 3.141592653589793 / 2.0
    for k in range(num_steps + 1):
        phi = 2.0 * 3.141592653589793 * k / num_steps
        phase = berry_phase_latitude(theta, delta_phi=phi)
        sign = spinor_sign_from_phase(phase)
        closure = abs(closure_defect([0.0, phase]))
        rows.append(
            SolverRow(
                step=k,
                theta=theta,
                phi=phi,
                berry_phase=phase,
                sign_re=float(sign.real),
                sign_im=float(sign.imag),
                closure_abs=float(closure),
            )
        )
    return rows


def final_equatorial_spinor_sign(num_steps: int = 16) -> complex:
    rows = solve_equatorial_cycle(num_steps=num_steps)
    last = rows[-1]
    return complex(last.sign_re, last.sign_im)
