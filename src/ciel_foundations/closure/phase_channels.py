from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Tuple

from src.ciel_foundations.initial_conditions.vectorization import vectorize_state


@dataclass(frozen=True)
class PhaseChannelResult:
    gamma: tuple[float, float]
    pole_chart: bool



def state_to_phase_channels(psi: Iterable[complex]) -> PhaseChannelResult:
    vec = vectorize_state(psi)
    return PhaseChannelResult(gamma=(vec.theta, vec.phi), pole_chart=vec.pole_chart)
