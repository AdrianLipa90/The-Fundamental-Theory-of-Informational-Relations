#!/usr/bin/env python3
from __future__ import annotations

import cmath
import itertools
import json
import math
from pathlib import Path

SCHEMA = "TIR_MUMMU_ORBITAL_ALGEBRA_GAUGE_CLOSURE_VALIDATION_V0_1"


def h_centered(n: int) -> int:
    return 3 * n * n + 3 * n + 1


def eisenstein_norm(a: int, b: int) -> int:
    return a * a - a * b + b * b


omega = cmath.exp(2j * math.pi / 3)
U6 = [1, -1, omega, -omega, omega**2, -(omega**2)]


def address(word, lam: float = 0.25, r0: float = 1.0) -> complex:
    z = 0j
    prod = 1 + 0j
    for k, letter in enumerate(word):
        prod *= U6[letter]
        z += r0 * (lam**k) * prod
    return z


def mm(a, b):
    return [
        [sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2)]
        for i in range(2)
    ]


def madd(a, b):
    return [[a[i][j] + b[i][j] for j in range(2)] for i in range(2)]


def msub(a, b):
    return [[a[i][j] - b[i][j] for j in range(2)] for i in range(2)]


def mscale(c, a):
    return [[c * a[i][j] for j in range(2)] for i in range(2)]


def dag(a):
    return [[a[j][i].conjugate() for j in range(2)] for i in range(2)]


def trace(a):
    return a[0][0] + a[1][1]


def frob2(a):
    return sum(abs(a[i][j]) ** 2 for i in range(2) for j in range(2))


def comm(a, b):
    return msub(mm(a, b), mm(b, a))


def maxerr(a, b):
    return max(abs(a[i][j] - b[i][j]) for i in range(2) for j in range(2))


I = [[1 + 0j, 0j], [0j, 1 + 0j]]
MINUS_I = [[-1 + 0j, 0j], [0j, -1 + 0j]]
SX = [[0j, 1 + 0j], [1 + 0j, 0j]]
SY = [[0j, -1j], [1j, 0j]]
SZ = [[1 + 0j, 0j], [0j, -1 + 0j]]
SIGMA = [SX, SY, SZ]


def axisdot(v):
    out = [[0j, 0j], [0j, 0j]]
    for coeff, sigma in zip(v, SIGMA):
        out = madd(out, mscale(coeff, sigma))
    return out


def su2(axis, angle):
    n = math.sqrt(sum(x * x for x in axis))
    unit = tuple(x / n for x in axis)
    return madd(
        mscale(math.cos(angle / 2), I),
        mscale(-1j * math.sin(angle / 2), axisdot(unit)),
    )


def generator(v):
    return mscale(-0.5j, axisdot(v))


def edge(parent, letter):
    depth = len(parent)
    axes = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    axis = axes[(sum(parent) + letter + depth) % 3]
    angle = (letter + 1) * (math.pi / 17) + (depth + 1) * (math.pi / 29)
    return su2(axis, angle)


def transport(word, edgefun=edge):
    w = I
    parent = ()
    for letter in word:
        e = edgefun(parent, letter)
        w = mm(w, e)
        parent = parent + (letter,)
    return w


def gauge(node):
    s = sum(node) + 1
    d = len(node) + 1
    axis = ((s % 3) + 1, ((s + d) % 5) + 1, ((2 * s + d) % 7) + 1)
    return su2(axis, 0.07 * s + 0.03 * d)


def edge_gauged(parent, letter):
    child = parent + (letter,)
    return mm(mm(gauge(parent), edge(parent, letter)), dag(gauge(child)))


def obstruction(hats):
    return 0.5 * sum(
        frob2(comm(hats[i], hats[j]))
        for i in range(len(hats))
        for j in range(i)
    )


def centrality_defect(h):
    return 1.0 - (abs(trace(h)) ** 2) / 4.0


def main() -> int:
    checks = []

    shell_ok = all(
        h_centered(n) - h_centered(n - 1) == 6 * n
        and h_centered(n) == eisenstein_norm(n + 1, -n)
        for n in range(1, 100)
    )
    checks.append(
        {
            "name": "centered_hexagonal_eisenstein_source_identity",
            "status": "PASS" if shell_ok else "FAIL",
        }
    )

    lam = 0.25
    words = [()]
    for depth in range(1, 5):
        words.extend(itertools.product(range(6), repeat=depth))
    points = [address(word, lam=lam) for word in words]
    min_sep = min(
        abs(points[i] - points[j])
        for i in range(len(points))
        for j in range(i)
    )
    nonprefix_bound = (1.0 - 3.0 * lam) / (1.0 - lam)
    prefix_bound = (1.0 - 2.0 * lam) / (1.0 - lam)
    checks.append(
        {
            "name": "orbital_address_prefix_separation_probe",
            "status": (
                "PASS"
                if min_sep > 1e-6 and nonprefix_bound > 0 and prefix_bound > 0
                else "FAIL"
            ),
            "lambda": lam,
            "word_count": len(words),
            "min_address_separation_depth_le_4": min_sep,
            "nonprefix_bound_factor": nonprefix_bound,
            "prefix_extension_bound_factor": prefix_bound,
        }
    )

    nodes = [(0, 1), (2, 4, 1), (5, 3), (1, 2, 0)]

    max_path_covariance_error = 0.0
    for word in nodes:
        w = transport(word)
        wg = transport(word, edge_gauged)
        target = mm(mm(gauge(()), w), dag(gauge(word)))
        max_path_covariance_error = max(
            max_path_covariance_error, maxerr(wg, target)
        )
    checks.append(
        {
            "name": "orbital_path_endpoint_gauge_covariance",
            "status": "PASS" if max_path_covariance_error < 1e-12 else "FAIL",
            "max_abs_error": max_path_covariance_error,
        }
    )

    vectors = {
        nodes[0]: (0.8, 0.2, -0.1),
        nodes[1]: (-0.3, 0.7, 0.4),
        nodes[2]: (0.2, -0.6, 0.9),
        nodes[3]: (0.5, 0.1, 0.3),
    }

    def transported(word):
        w = transport(word)
        a = generator(vectors[word])
        return mm(mm(w, a), dag(w))

    def transported_gauged(word):
        wg = transport(word, edge_gauged)
        a = generator(vectors[word])
        ag = mm(mm(gauge(word), a), dag(gauge(word)))
        return mm(mm(wg, ag), dag(wg))

    root_gauge = gauge(())
    max_generator_covariance_error = 0.0
    for word in nodes:
        target = mm(mm(root_gauge, transported(word)), dag(root_gauge))
        max_generator_covariance_error = max(
            max_generator_covariance_error,
            maxerr(transported_gauged(word), target),
        )
    checks.append(
        {
            "name": "transported_generator_common_root_covariance",
            "status": (
                "PASS" if max_generator_covariance_error < 1e-12 else "FAIL"
            ),
            "max_abs_error": max_generator_covariance_error,
        }
    )

    o_plain = obstruction([transported(word) for word in nodes])
    o_gauge = obstruction([transported_gauged(word) for word in nodes])
    checks.append(
        {
            "name": "orbital_nonabelian_obstruction_gauge_invariance",
            "status": "PASS" if abs(o_plain - o_gauge) < 1e-12 else "FAIL",
            "plain": o_plain,
            "gauged": o_gauge,
            "abs_difference": abs(o_plain - o_gauge),
        }
    )

    central_ok = True
    word = nodes[0]
    w = transport(word)
    a = generator(vectors[word])
    base = mm(mm(w, a), dag(w))
    for h in (I, MINUS_I):
        w_alt = mm(h, w)
        alt = mm(mm(w_alt, a), dag(w_alt))
        central_ok = central_ok and maxerr(base, alt) < 1e-12
    checks.append(
        {
            "name": "central_holonomy_path_independence",
            "status": "PASS" if central_ok else "FAIL",
            "delta_plus_I": centrality_defect(I),
            "delta_minus_I": centrality_defect(MINUS_I),
        }
    )

    h_noncentral = su2((0, 0, 1), math.pi / 2)
    noncentral_defect = centrality_defect(h_noncentral)
    checks.append(
        {
            "name": "noncentral_lagrange_loop_defect",
            "status": (
                "PASS" if abs(noncentral_defect - 0.5) < 1e-12 else "FAIL"
            ),
            "defect": noncentral_defect,
        }
    )

    witness = generator((1, 0, 0))
    moved = mm(mm(h_noncentral, witness), dag(h_noncentral))
    witness_change = maxerr(witness, moved)
    checks.append(
        {
            "name": "noncentral_holonomy_path_memory_witness",
            "status": "PASS" if witness_change > 0.1 else "FAIL",
            "max_abs_generator_change": witness_change,
        }
    )

    status = "PASS" if all(c["status"] == "PASS" for c in checks) else "FAIL"
    result = {
        "schema": SCHEMA,
        "status": status,
        "claim_scope": (
            "orbital address injectivity probe, SU(2) path endpoint covariance, "
            "gauge-invariant transported obstruction, and central-holonomy path "
            "independence; physical orbital/MUMMU realization remains open"
        ),
        "checks": checks,
        "summary": {
            "passed": sum(c["status"] == "PASS" for c in checks),
            "total": len(checks),
        },
        "source_pins": {
            "pncs_main": "8855abed440e9949f576ffbe2153325f69e78963",
            "on_primes_centered_hexagonal": "465e36061fe3c3e6e072b93020f33d5a60fe0c2f",
        },
    }

    receipt = Path(__file__).with_name(
        "TIR_MUMMU_ORBITAL_ALGEBRA_GAUGE_CLOSURE_VALIDATION_V0_1.json"
    )
    receipt.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
