from __future__ import annotations

import numpy as np

from Simulations.code.closure.closure_operator import closure_operator
from src.ciel_foundations.closure.phase_channels import state_to_phase_channels


def main() -> None:
    psi = np.array([1.0 / np.sqrt(2.0), 1j / np.sqrt(2.0)], dtype=np.complex128)
    channels = state_to_phase_channels(psi)
    delta, R, C = closure_operator(channels.gamma)
    print(channels)
    print(delta, R, C)


if __name__ == "__main__":
    main()
