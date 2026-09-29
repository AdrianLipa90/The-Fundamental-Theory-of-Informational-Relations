"""Regression checks for TIR general orbital algebra v0.1.

This file is not a proof assistant artifact. It checks executable identities used by
TIR_GENERAL_ORBITAL_ALGEBRA_RELATIONAL_ZERO_V0_1.md and fails closed on drift.
"""

from __future__ import annotations

import cmath
import math
import random


TOL = 1e-12


def close(a: complex | float, b: complex | float, tol: float = TOL) -> bool:
    return abs(a - b) <= tol


def exchange(x: float, a: float, b: float) -> float:
    return a + b - x


def normalized_q(x: float, a: float, b: float) -> float:
    if close(a, b):
        raise ValueError("degenerate relation: endpoints must be distinct")
    return (x - a) / (b - a)


def centered_z(q: float) -> float:
    return 2.0 * q - 1.0


def rotation(phi: float, z: complex) -> complex:
    return cmath.exp(1j * phi) * z


def lift(phi: float, n: int) -> complex:
    if n < 1:
        raise ValueError("cover degree n must be positive")
    return cmath.exp(1j * phi / n)


def zeta_centered_real(s: complex) -> float:
    return 2.0 * s.real - 1.0


def zeta_reflection(s: complex) -> complex:
    return 1.0 - s.conjugate()


def check_relational_midpoint() -> None:
    rng = random.Random(20260929)
    for _ in range(512):
        a = rng.uniform(-100.0, 100.0)
        b = rng.uniform(-100.0, 100.0)
        if abs(a - b) < 1e-6:
            b += 1.0
        m = 0.5 * (a + b)
        assert close(exchange(m, a, b), m)
        q = normalized_q(m, a, b)
        assert close(q, 0.5)
        assert close(centered_z(q), 0.0)


def check_exchange_oddness() -> None:
    rng = random.Random(134)
    for _ in range(512):
        q = rng.uniform(-4.0, 4.0)
        assert close(centered_z(1.0 - q), -centered_z(q))


def check_u1_orbit() -> None:
    rng = random.Random(36)
    for _ in range(512):
        phi = rng.uniform(-20.0 * math.pi, 20.0 * math.pi)
        z = complex(rng.uniform(-10.0, 10.0), rng.uniform(-10.0, 10.0))
        assert close(abs(rotation(phi, z)), abs(z))
        assert close(rotation(phi, 0j), 0j)
        assert close(rotation(phi + 2.0 * math.pi, z), rotation(phi, z))


def check_double_cover() -> None:
    rng = random.Random(12)
    for _ in range(256):
        phi = rng.uniform(-20.0 * math.pi, 20.0 * math.pi)
        w = lift(phi, 2)
        w_2pi = lift(phi + 2.0 * math.pi, 2)
        w_4pi = lift(phi + 4.0 * math.pi, 2)
        assert close(w_2pi, -w)
        assert close(w_4pi, w)
        assert close(w * w, cmath.exp(1j * phi))


def check_nfold_monodromy() -> None:
    phi = 0.731
    for n in range(1, 17):
        w = lift(phi, n)
        one_turn = lift(phi + 2.0 * math.pi, n)
        n_turns = lift(phi + 2.0 * math.pi * n, n)
        assert close(one_turn, cmath.exp(2j * math.pi / n) * w)
        assert close(n_turns, w)


def check_projective_half_seam() -> None:
    phases = [0.0, 0.1, 1.0, math.pi, 2.0 * math.pi - 0.2]
    for phi in phases:
        z0 = 1.0 / math.sqrt(2.0)
        z1 = cmath.exp(1j * phi) / math.sqrt(2.0)
        q = abs(z1) ** 2 / (abs(z0) ** 2 + abs(z1) ** 2)
        xi = z1 / z0
        assert close(q, 0.5)
        assert close(centered_z(q), 0.0)
        assert close(abs(xi), 1.0)


def check_critical_axis_reflection() -> None:
    for t in (-100.0, -3.0, 0.0, 2.5, 100.0):
        s = complex(0.5, t)
        assert close(zeta_reflection(s), s)
        assert close(zeta_centered_real(s), 0.0)

    samples = [
        complex(0.1, 3.0),
        complex(0.27, -8.0),
        complex(0.8, 4.2),
        complex(1.2, -0.5),
    ]
    for s in samples:
        sr = zeta_reflection(s)
        assert close(zeta_centered_real(sr), -zeta_centered_real(s))



def check_moire_pair_identity() -> None:
    rng = random.Random(1024)
    for _ in range(256):
        amplitude = rng.uniform(0.1, 5.0)
        phi1 = rng.uniform(-8.0 * math.pi, 8.0 * math.pi)
        phi2 = rng.uniform(-8.0 * math.pi, 8.0 * math.pi)
        lhs = amplitude * cmath.exp(1j * phi1) + amplitude * cmath.exp(1j * phi2)
        mean = 0.5 * (phi1 + phi2)
        delta = phi1 - phi2
        rhs = 2.0 * amplitude * cmath.exp(1j * mean) * math.cos(0.5 * delta)
        assert close(lhs, rhs)


def check_kappa_information_operator() -> None:
    n_flavour = 3
    su3_dim = n_flavour * n_flavour - 1
    n_mix = n_flavour * su3_dim
    relational_half_turn = 0.5
    q_mix = n_mix * relational_half_turn
    kappa_q = math.log(2.0) / q_mix
    kappa_phi = kappa_q / (2.0 * math.pi)

    assert n_mix == 24
    assert close(q_mix, 12.0)
    assert close(kappa_q, math.log(2.0) / 12.0)
    assert close(kappa_phi, math.log(2.0) / (24.0 * math.pi))

    # Coordinate covariance of the information one-form:
    # dI = kappa_q dq = kappa_phi dphi, with phi = 2*pi*q.
    rng = random.Random(24)
    for _ in range(256):
        dq = rng.uniform(-4.0, 4.0)
        dphi = 2.0 * math.pi * dq
        assert close(kappa_q * dq, kappa_phi * dphi)

def run() -> None:
    checks = [
        check_relational_midpoint,
        check_exchange_oddness,
        check_u1_orbit,
        check_double_cover,
        check_nfold_monodromy,
        check_projective_half_seam,
        check_moire_pair_identity,
        check_kappa_information_operator,
        check_critical_axis_reflection,
    ]
    for check in checks:
        check()
        print(f"PASS {check.__name__}")
    print(f"PASS all={len(checks)}")


if __name__ == "__main__":
    run()
