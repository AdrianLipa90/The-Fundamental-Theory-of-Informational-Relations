#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction


def half_step(state: tuple[int, int]) -> tuple[int, int]:
    n, sector = state
    if n < 0 or sector not in (0, 1):
        raise ValueError("state must lie in N_0 x Z_2")
    return (n, 1) if sector == 0 else (n + 1, 0)


def successor(state: tuple[int, int]) -> tuple[int, int]:
    n, sector = state
    if n < 0 or sector not in (0, 1):
        raise ValueError("state must lie in N_0 x Z_2")
    return n + 1, sector


def grade(state: tuple[int, int]) -> Fraction:
    n, sector = state
    if n < 0 or sector not in (0, 1):
        raise ValueError("state must lie in N_0 x Z_2")
    return Fraction(n, 1) + Fraction(sector, 2)


def edge(n: int) -> frozenset[int]:
    if n < 1:
        raise ValueError("edge index must be >=1")
    return frozenset((n, n + 1))


def hilbert_shift(n: int) -> int:
    if n < 1:
        raise ValueError("Hilbert room index must be >=1")
    return n + 1


def validate(bound: int = 256) -> dict[str, object]:
    if bound < 4:
        raise ValueError("bound must be >=4")

    for n in range(bound):
        for sector in (0, 1):
            x = (n, sector)
            assert half_step(half_step(x)) == successor(x)
            assert grade(half_step(x)) - grade(x) == Fraction(1, 2)
            assert grade(successor(x)) - grade(x) == 1

    for n in range(1, bound):
        assert edge(n).intersection(edge(n + 1)) == frozenset((n + 1,))
        assert frozenset(hilbert_shift(v) for v in edge(n)) == edge(n + 1)

    image = {hilbert_shift(n) for n in range(1, bound + 1)}
    assert 1 not in image
    assert len(image) == bound

    return {
        "schema": "TIR_STELLA_PRESPACETIME_HALFSTEP_SUCCESSOR_V0_1",
        "status": "PASS",
        "bound": bound,
        "half_step_square_equals_successor": True,
        "half_grade_exact": True,
        "adjacent_edge_overlap_exact": True,
        "hilbert_shift_incidence_preserved": True,
        "hilbert_shift_injective_non_surjective": True,
        "physical_time_assumed": False,
        "physical_space_assumed": False,
        "canon_allowed": False,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(validate(), sort_keys=True))
