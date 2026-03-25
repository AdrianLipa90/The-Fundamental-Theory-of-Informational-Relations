from __future__ import annotations

import numpy as np

from src.ciel_foundations.initial_conditions.vectorization import vectorize_state


def main() -> None:
    psi = np.array([1.0 + 0.0j, 0.0 + 0.0j])
    result = vectorize_state(psi)
    print(result)


if __name__ == "__main__":
    main()
