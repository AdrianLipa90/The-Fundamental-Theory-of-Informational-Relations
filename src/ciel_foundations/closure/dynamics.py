from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Literal

import numpy as np

from Simulations.code.closure.closure_operator import closure_operator
from src.ciel_foundations.closure.admissibility import admissibility_correction

UpdateMode = Literal["accept_if_nonworsening", "rollback", "correct"]


@dataclass(frozen=True)
class DynamicsStepResult:
    gamma_in: tuple[float, float]
    velocity: tuple[float, float]
    dt: float
    gamma_prop: tuple[float, float]
    gamma_out: tuple[float, float]
    mode: UpdateMode
    c_in: float
    c_prop: float
    c_out: float
    accepted: bool
    rolled_back: bool
    corrected: bool


def _wrap(gamma: Iterable[float]) -> tuple[float, float]:
    vals = tuple(float(x) for x in gamma)
    return tuple(float(np.mod(v, 2.0 * np.pi)) for v in vals)  # type: ignore[return-value]


def minimal_update_step(
    gamma_in: Iterable[float],
    velocity: Iterable[float],
    dt: float,
    mode: UpdateMode = "accept_if_nonworsening",
    epsilon_c: float = 1e-12,
) -> DynamicsStepResult:
    g_in = _wrap(gamma_in)
    vel = tuple(float(x) for x in velocity)
    g_prop = _wrap((g_in[0] + dt * vel[0], g_in[1] + dt * vel[1]))

    _, _, c_in_raw = closure_operator(g_in)
    _, _, c_prop_raw = closure_operator(g_prop)
    c_in = float(c_in_raw)
    c_prop = float(c_prop_raw)

    if mode == "accept_if_nonworsening":
        accepted = bool(c_prop <= c_in)
        g_out = g_prop if accepted else g_in
        _, _, c_out_raw = closure_operator(g_out)
        c_out = float(c_out_raw)
        return DynamicsStepResult(gamma_in=g_in, velocity=vel, dt=float(dt), gamma_prop=g_prop, gamma_out=g_out, mode=mode, c_in=c_in, c_prop=c_prop, c_out=c_out, accepted=accepted, rolled_back=bool(not accepted), corrected=False)

    if mode == "rollback":
        accepted = bool(c_prop <= float(epsilon_c))
        g_out = g_prop if accepted else g_in
        _, _, c_out_raw = closure_operator(g_out)
        c_out = float(c_out_raw)
        return DynamicsStepResult(gamma_in=g_in, velocity=vel, dt=float(dt), gamma_prop=g_prop, gamma_out=g_out, mode=mode, c_in=c_in, c_prop=c_prop, c_out=c_out, accepted=accepted, rolled_back=bool(not accepted), corrected=False)

    corr = admissibility_correction(g_prop, epsilon_c=epsilon_c, mode="correct")
    g_out = corr.gamma_out if corr.gamma_out is not None else g_in
    return DynamicsStepResult(gamma_in=g_in, velocity=vel, dt=float(dt), gamma_prop=g_prop, gamma_out=g_out, mode=mode, c_in=c_in, c_prop=c_prop, c_out=float(corr.c_out if corr.c_out is not None else c_in), accepted=True, rolled_back=False, corrected=bool(corr.corrected))
