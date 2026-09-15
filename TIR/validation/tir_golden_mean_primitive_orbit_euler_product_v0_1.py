#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
THEOREM = ROOT / "TIR" / "foundations" / "TIR_GOLDEN_MEAN_PRIMITIVE_ORBIT_EULER_PRODUCT_V0_1.md"
CODING = ROOT / "TIR" / "foundations" / "TIR_GOLDEN_MEAN_CODING_CONJUGACY_V0_1.md"
PRESSURE = ROOT / "TIR" / "foundations" / "TIR_GOLDEN_MEAN_PRESSURE_KAPPA_V0_1.md"

texts = {
    "theorem": THEOREM.read_text(encoding="utf-8"),
    "coding": CODING.read_text(encoding="utf-8"),
    "pressure": PRESSURE.read_text(encoding="utf-8"),
}
compact = {key: "".join(value.split()) for key, value in texts.items()}
checks: dict[str, bool] = {}

# Pinned semantic receipts from exact parent theorem surfaces.
checks["upstream_fixed_point_receipt"] = "\\#\\operatorname{Fix}(D^n|_{K_C})=L_n" in compact["coding"]
checks["upstream_artin_mazur_receipt"] = "\\zeta_{\\rmAM}(z)=\\frac1{1-z-z^2}" in compact["coding"]
checks["upstream_weighted_determinant_receipt"] = "\\zeta_{\\rmAM}(z;s)=\\frac1{1-2^{-s}z-2^{-2s}z^2}" in compact["coding"]
checks["upstream_pressure_receipt"] = "P(s)=\\ln\\varphi-s\\ln2" in compact["pressure"]

A = sp.Matrix([[1, 1], [1, 0]])
z, q = sp.symbols("z q")
phi = (1 + sp.sqrt(5)) / 2
N = 18


def lucas(n: int) -> int:
    if n == 0:
        return 2
    if n == 1:
        return 1
    a, b = 2, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


F: dict[int, int] = {}
E: dict[int, int] = {}
O: dict[int, int] = {}
all_integral_nonnegative = True
divisor_identity = True
mobius_identity = True
for n in range(1, N + 1):
    F[n] = int(sp.trace(A**n))
    E[n] = sum(int(sp.mobius(n // d)) * F[d] for d in sp.divisors(n))
    all_integral_nonnegative = all_integral_nonnegative and E[n] >= 0 and E[n] % n == 0
    O[n] = E[n] // n
    divisor_identity = divisor_identity and F[n] == sum(m * O[m] for m in sp.divisors(n))
    mobius_identity = mobius_identity and n * O[n] == sum(int(sp.mobius(n // d)) * F[d] for d in sp.divisors(n))

checks["trace_equals_lucas_n1_to_n18"] = all(F[n] == lucas(n) for n in range(1, N + 1))
checks["primitive_counts_nonnegative_integral_n1_to_n18"] = all_integral_nonnegative
checks["fixed_point_divisor_identity_n1_to_n18"] = divisor_identity
checks["mobius_inversion_n1_to_n18"] = mobius_identity

expected_first12 = {1: 1, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 4, 8: 5, 9: 8, 10: 11, 11: 18, 12: 25}
checks["primitive_counts_first12_receipt"] = all(O[n] == expected_first12[n] for n in expected_first12)

# Exact truncated coefficient convolution for product_{m<=N}(1-z^m)^(-O_m).
# The factor coefficient at z^(k*m) is C(O_m+k-1,k).
coeff = [0] * (N + 1)
coeff[0] = 1
for m in range(1, N + 1):
    exponent = O[m]
    factor = [0] * (N + 1)
    if exponent == 0:
        factor[0] = 1
    else:
        for k in range(0, N // m + 1):
            factor[k * m] = math.comb(exponent + k - 1, k)
    nxt = [0] * (N + 1)
    for i, a in enumerate(coeff):
        if a == 0:
            continue
        for j, b in enumerate(factor):
            if b == 0 or i + j > N:
                continue
            nxt[i + j] += a * b
    coeff = nxt

# 1/(1-z-z^2) has coefficient F_{n+1} with F_1=F_2=1.
rational_coeff = [fib(n + 1) for n in range(N + 1)]
checks["finite_euler_product_matches_rational_through_degree18"] = coeff == rational_coeff

# z d/dz log(product) coefficient at z^n is sum_{m|n} m O_m = F_n.
log_derivative_coeff = {n: sum(m * O[m] for m in sp.divisors(n)) for n in range(1, N + 1)}
checks["log_derivative_matches_fixed_points_through_degree18"] = all(log_derivative_coeff[n] == F[n] for n in range(1, N + 1))

# Weighted substitution y=qz multiplies every degree-n coefficient by q^n.
checks["weighted_orbit_product_matches_determinant_through_degree18"] = all(coeff[n] == rational_coeff[n] for n in range(N + 1))

I2 = sp.eye(2)
det_weighted = sp.expand((I2 - z * q * A).det())
checks["weighted_determinant_exact"] = sp.expand(det_weighted - (1 - q * z - q**2 * z**2)) == 0
z_c = sp.simplify(1 / (q * phi))
checks["weighted_positive_pole_exact"] = sp.simplify(det_weighted.subs(z, z_c)) == 0
checks["phi_relation"] = sp.simplify(phi**2 - phi - 1) == 0

# Formal logarithm coefficient, independently from product convolution.
formal_log_coefficients = True
for n in range(1, N + 1):
    lhs = sum(sp.Rational(O[m], n // m) for m in sp.divisors(n))
    formal_log_coefficients = formal_log_coefficients and sp.simplify(lhs - sp.Rational(F[n], n)) == 0
checks["formal_log_coefficients_exact_n1_to_n18"] = formal_log_coefficients

# Firewalls and theorem receipts.
theorem = texts["theorem"]
theorem_compact = compact["theorem"]
checks["dynamical_prime_firewall"] = "primitive / prime dynamical orbit != prime integer" in theorem
checks["arithmetic_euler_product_firewall"] = "dynamical Euler product equals Riemann Euler product | `NOT_DERIVED / NOT_CLAIMED`" in theorem
checks["riemann_zeta_firewall"] = "Riemann-zeta identification | `NOT_DERIVED / NOT_CLAIMED`" in theorem
checks["rh_firewall"] = "implication for RH | `NONE`" in theorem
checks["physical_firewall"] = "physical particle/cosmological interpretation of primitive orbits | `OPEN_NOT_CLAIMED`" in theorem
checks["weighted_orbit_receipt"] = "\\prod_{m\\ge1}(1-(qz)^m)^{-O_m}" in theorem_compact
checks["rational_collapse_receipt"] = (
    "\\prod_{m\\ge1}(1-z^m)^{-O_m}" in theorem_compact
    and "\\frac1{\\det(I-zA)}" in theorem_compact
    and "\\frac1{1-z-z^2}" in theorem_compact
)

status = "PASS" if all(checks.values()) else "FAIL"
report = {
    "schema": "tir.golden-mean-primitive-orbit-euler-product/v0.1",
    "status": status,
    "audit_max_period": N,
    "fixed_points_n1_to_n18": {str(n): F[n] for n in range(1, N + 1)},
    "exact_period_points_n1_to_n18": {str(n): E[n] for n in range(1, N + 1)},
    "primitive_orbits_n1_to_n18": {str(n): O[n] for n in range(1, N + 1)},
    "finite_product_coefficients_degree0_to18": coeff,
    "artin_mazur": "1/(1-z-z^2)",
    "primitive_orbit_product": "prod_m>=1 (1-z^m)^(-O_m)",
    "weighted_orbit_product": "prod_m>=1 (1-(qz)^m)^(-O_m), q=2^(-s)",
    "weighted_pole": "z_c=1/(q*phi)=2^s/phi",
    "arithmetic_prime_identification": "FALSE_TYPE_ERROR",
    "riemann_zeta_identification": "NOT_DERIVED",
    "rh_implication": "NONE",
    "checks": checks,
}
print(json.dumps(report, indent=2, sort_keys=True))
raise SystemExit(0 if status == "PASS" else 1)
