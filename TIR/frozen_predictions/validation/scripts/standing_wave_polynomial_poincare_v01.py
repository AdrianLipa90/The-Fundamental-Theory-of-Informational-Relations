#!/usr/bin/env python3
"""Stage 8 pure-mathematics audit.

Checks:
- standing-wave nodes,
- Chebyshev-U zeros,
- regular polygon roots of z^N-r^N,
- C_N cyclic closure,
- C3 x Z2 lifted-state cardinality separation.

No physical data are used.
"""

from __future__ import annotations

import cmath
import math


def standing_wave_nodes(k: float, nmax: int):
    return [n * math.pi / k for n in range(nmax + 1)]


def chebyshev_u_roots(N: int):
    return [math.cos(j * math.pi / (N + 1)) for j in range(1, N + 1)]


def polygon_roots(N: int, r: float):
    return [r * cmath.exp(2j * math.pi * j / N) for j in range(N)]


def q_nr(z: complex, N: int, r: float):
    return z**N - r**N


def rotate(z: complex, N: int):
    return cmath.exp(2j * math.pi / N) * z


def close(a: complex, b: complex, tol: float = 1e-12):
    return abs(a - b) <= tol


def main():
    # Standing-wave discreteness
    nodes = standing_wave_nodes(k=2.0, nmax=5)
    expected = [n * math.pi / 2.0 for n in range(6)]
    assert all(abs(a - b) < 1e-12 for a, b in zip(nodes, expected))

    # Chebyshev-U root identity via sin((N+1)theta)=0
    for N in range(1, 10):
        roots = chebyshev_u_roots(N)
        for j, x in enumerate(roots, start=1):
            theta = j * math.pi / (N + 1)
            assert abs(x - math.cos(theta)) < 1e-12
            assert abs(math.sin((N + 1) * theta)) < 1e-12

    # Polygon polynomial and cyclic closure inside unit disk
    for N in range(3, 13):
        r = 0.7
        roots = polygon_roots(N, r)
        assert all(abs(q_nr(z, N, r)) < 1e-10 for z in roots)
        assert all(abs(z) < 1.0 for z in roots)

        z0 = roots[0]
        z = z0
        for _ in range(N):
            z = rotate(z, N)
        assert close(z, z0, 1e-10)

        # no earlier closure for a primitive Nth-root rotation
        z = z0
        for step in range(1, N):
            z = rotate(z, N)
            assert not close(z, z0, 1e-10)

    # Explicit C3 root orbit
    r = 0.7
    roots3 = polygon_roots(3, r)
    z = roots3[0]
    orbit = [z]
    orbit.append(rotate(orbit[-1], 3))
    orbit.append(rotate(orbit[-1], 3))
    assert all(any(close(a, b, 1e-10) for b in roots3) for a in orbit)
    assert close(rotate(orbit[-1], 3), orbit[0], 1e-10)

    # Stage 7 separation: 3 geometric roots x 2 sheets = 6 lifted states
    lifted = [(j, s) for j in range(3) for s in (-1, +1)]
    assert len(lifted) == 6
    assert len(roots3) == 3

    print("STAGE_8_PURE_MATHEMATICS_PASS_WITH_BOUNDARY_CONDITION_SEPARATION")


if __name__ == "__main__":
    main()
