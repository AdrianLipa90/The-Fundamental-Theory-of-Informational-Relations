#!/usr/bin/env python3
"""Exact finite-state audit for TIR Stage 6 C3 x Z2 six-state lift.

Standard library only. No physical inputs.
"""

from math import gcd


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def p3(state: int) -> int:
    if state not in (0, 1, 2):
        raise ValueError("C3 state must be 0, 1, or 2")
    return (state + 1) % 3


def x2(sheet: int) -> int:
    if sheet not in (0, 1):
        raise ValueError("Z2 sheet must be 0 or 1")
    return 1 - sheet


def g(state: tuple[int, int]) -> tuple[int, int]:
    return p3(state[0]), x2(state[1])


def orbit(start: tuple[int, int], max_steps: int = 12) -> list[tuple[int, int]]:
    out = [start]
    current = start
    for _ in range(max_steps):
        current = g(current)
        out.append(current)
        if current == start:
            return out
    raise RuntimeError("orbit did not close within max_steps")


def audit() -> None:
    o = orbit((0, 0))
    period = len(o) - 1
    assert period == 6
    assert o[3][0] == o[0][0]
    assert o[3][1] != o[0][1]
    assert o[6] == o[0]

    projected = [s for s, _ in o]
    assert projected[:4] == [0, 1, 2, 0]

    assert lcm(3, 2) == 6

    generic = {m: lcm(m, 2) for m in range(2, 11)}
    assert generic[3] == 6
    assert generic[4] == 4
    assert generic[5] == 10
    assert generic[6] == 6

    print("STAGE_6_PURE_MATHEMATICS_PASS")
    print("lifted_period=6")
    print("projected_period=3")
    print("step3=base_return_sheet_flip")
    print("step6=full_identity")
    print("generic_orders=", generic)


if __name__ == "__main__":
    audit()
