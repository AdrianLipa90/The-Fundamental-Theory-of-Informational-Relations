from __future__ import annotations

from dataclasses import dataclass
from math import atan2
from typing import Iterable, Literal

import numpy as np

from Simulations.code.closure.closure_operator import closure_operator

DecisionMode = Literal["reject", "correct"]


@dataclass(frozen=True)
class AdmissibilityResult:
    admissible: bool
    mode: DecisionMode
    gamma_in: tuple[float, float]
    gamma_out: tuple[float, float] | None
    delta_in: complex
    r_in: float
    c_in: float
    delta_out: complex | None
    r_out: float | None
    c_out: float | None
    rejected: bool
    corrected: bool



def _phasor_arg(z: complex) -> float:
    return float(atan2(z.imag, z.real))



def _coherent_projection(gamma: Iterable[float]) -> tuple[float, float]:
    g1, g2 = tuple(float(x) for x in gamma)
    delta, _, _ = closure_operator((g1, g2))
    if np.isclose(np.abs(delta), 0.0, atol=1e-12):
        gamma_ref = g1
    else:
        gamma_ref = _phasor_arg(delta)
    return (gamma_ref, gamma_ref)



def admissibility_correction(
    gamma: Iterable[float],
    epsilon_c: float = 1e-12,
    mode: DecisionMode = "correct",
) -> AdmissibilityResult:
    g_in = tuple(float(x) for x in gamma)
    delta_in, r_in, c_in = closure_operator(g_in)

    if c_in <= epsilon_c:
        return AdmissibilityResult(
            admissible=True,
            mode=mode,
            gamma_in=g_in,
            gamma_out=g_in,
            delta_in=delta_in,
            r_in=r_in,
            c_in=c_in,
            delta_out=delta_in,
            r_out=r_in,
            c_out=c_in,
            rejected=False,
            corrected=False,
        )

    if mode == "reject":
        return AdmissibilityResult(
            admissible=False,
            mode=mode,
            gamma_in=g_in,
            gamma_out=None,
            delta_in=delta_in,
            r_in=r_in,
            c_in=c_in,
            delta_out=None,
            r_out=None,
            c_out=None,
            rejected=True,
            corrected=False,
        )

    g_out = _coherent_projection(g_in)
    delta_out, r_out, c_out = closure_operator(g_out)
    return AdmissibilityResult(
        admissible=True,
        mode=mode,
        gamma_in=g_in,
        gamma_out=g_out,
        delta_in=delta_in,
        r_in=r_in,
        c_in=c_in,
        delta_out=delta_out,
        r_out=r_out,
        c_out=c_out,
        rejected=False,
        corrected=True,
    )
