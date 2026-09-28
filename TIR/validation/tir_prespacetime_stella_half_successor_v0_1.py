from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations
import json

PLUS = 1
MINUS = -1

@dataclass(frozen=True)
class State:
    cycle: int
    sector: int

def half_index(x: State) -> Fraction:
    if x.cycle < 0 or x.sector not in (PLUS, MINUS):
        raise ValueError("invalid pretime state")
    return Fraction(x.cycle, 1) if x.sector == PLUS else Fraction(x.cycle, 1) + Fraction(1, 2)

def half_successor(x: State) -> State:
    if x.cycle < 0 or x.sector not in (PLUS, MINUS):
        raise ValueError("invalid pretime state")
    return State(x.cycle, MINUS) if x.sector == PLUS else State(x.cycle + 1, PLUS)

def successor(x: State) -> State:
    if x.cycle < 0 or x.sector not in (PLUS, MINUS):
        raise ValueError("invalid pretime state")
    return State(x.cycle + 1, x.sector)

def edge(n: int) -> frozenset[int]:
    if n < 0:
        raise ValueError("n must be non-negative")
    return frozenset((n, n + 1))

def gram(i: int, j: int) -> Fraction:
    if not (0 <= i < 4 and 0 <= j < 4):
        raise ValueError("tetrahedral vertex index out of range")
    return Fraction(1, 1) if i == j else Fraction(-1, 3)

def validate(limit: int = 64) -> dict[str, object]:
    states = [State(n, s) for n in range(limit) for s in (PLUS, MINUS)]
    checks = {
        "H2_equals_S": all(half_successor(half_successor(x)) == successor(x) for x in states),
        "H_increment_half": all(half_index(half_successor(x)) - half_index(x) == Fraction(1, 2) for x in states),
        "S_increment_one": all(half_index(successor(x)) - half_index(x) == 1 for x in states),
        "H_flips_sector": all(half_successor(x).sector == -x.sector for x in states),
        "S_preserves_sector": all(successor(x).sector == x.sector for x in states),
        "adjacent_edge_overlap": all(edge(n) & edge(n + 1) == frozenset((n + 1,)) for n in range(limit)),
        "Hilbert_shift_edge_covariance": all(frozenset(k + 1 for k in edge(n)) == edge(n + 1) for n in range(limit)),
        "S4_gram_invariance": all(
            gram(p[i], p[j]) == gram(i, j)
            for p in permutations(range(4))
            for i in range(4)
            for j in range(4)
        ),
    }
    return {
        "schema": "TIR_PRESPACETIME_STELLA_HALF_SUCCESSOR_VALIDATION_V0_1",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "limit": limit,
        "physical_time_claimed": False,
        "physical_space_claimed": False,
        "canon_allowed": False,
    }

if __name__ == "__main__":
    print(json.dumps(validate(), indent=2, sort_keys=True))
