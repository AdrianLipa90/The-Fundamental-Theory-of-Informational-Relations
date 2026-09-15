#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
THEOREM = ROOT / "TIR" / "foundations" / "TIR_GOLDEN_MEAN_PRIME_ORBIT_ASYMPTOTIC_V0_1.md"
EULER = ROOT / "TIR" / "foundations" / "TIR_GOLDEN_MEAN_PRIMITIVE_ORBIT_EULER_PRODUCT_V0_1.md"
CODING = ROOT / "TIR" / "foundations" / "TIR_GOLDEN_MEAN_CODING_CONJUGACY_V0_1.md"
TRANSFER = ROOT / "TIR" / "foundations" / "TIR_GOLDEN_MEAN_TRANSFER_KAPPA_V0_1.md"

texts = {p.stem: p.read_text(encoding="utf-8") for p in (THEOREM, EULER, CODING, TRANSFER)}
compact = {key: "".join(value.split()) for key, value in texts.items()}
checks: dict[str, bool] = {}

theorem = texts[THEOREM.stem]
euler = texts[EULER.stem]
coding = texts[CODING.stem]
transfer = texts[TRANSFER.stem]

# Parent receipts.
checks["upstream_mobius_orbit_receipt"] = "O_n=\\frac1n\\sum_{d\\midn}\\mu" in compact[EULER.stem]
checks["upstream_lucas_fixed_point_receipt"] = "F_n:=\\#\\operatorname{Fix}(D^n|_{K_C})=\\operatorname{tr}(A^n)=L_n" in compact[EULER.stem]
checks["upstream_entropy_receipt"] = "h_{\\rmtop}=\\ln\\varphi" in compact[TRANSFER.stem]
checks["upstream_kappa_dimension_receipt"] = "h_{\\rmtop}=24\\pi\\kappa\\,\\dim_HK_C" in compact[TRANSFER.stem]

phi = (1 + sp.sqrt(5)) / 2
psi = -1 / phi
A = sp.Matrix([[1, 1], [1, 0]])
N = 80


def lucas(n: int) -> int:
    if n == 0:
        return 2
    if n == 1:
        return 1
    a, b = 2, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


F: dict[int, int] = {}
O: dict[int, int] = {}
proper_divisor_bound = True
integral_orbits = True
for n in range(1, N + 1):
    F[n] = int(sp.trace(A**n))
    exact_points = sum(int(sp.mobius(n // d)) * F[d] for d in sp.divisors(n))
    integral_orbits = integral_orbits and exact_points >= 0 and exact_points % n == 0
    O[n] = exact_points // n
    if n >= 2:
        proper_divisor_bound = proper_divisor_bound and all(d <= n / 2 for d in sp.divisors(n) if d < n)

checks["trace_equals_lucas_n1_to_n80"] = all(F[n] == lucas(n) for n in range(1, N + 1))
checks["primitive_orbits_integral_n1_to_n80"] = integral_orbits
checks["proper_divisors_at_most_half_n2_to_n80"] = proper_divisor_bound

# High-precision finite witnesses for the analytic bounds proved in the theorem.
phi_f = (1.0 + math.sqrt(5.0)) / 2.0
tau_bound_witness = True
coarse_bound_witness = True
relative_bound_witness = True
ratios: dict[str, float] = {}
for n in range(2, N + 1):
    main = phi_f**n / n
    remainder = abs(O[n] - main)
    tau_n = len(sp.divisors(n))
    tau_bound = phi_f**(-n) / n + 2.0 * (tau_n - 1) * phi_f**(n / 2.0) / n
    coarse_bound = 2.0 * phi_f**(n / 2.0) + 1.0 / n
    relative = abs(n * O[n] / (phi_f**n) - 1.0)
    relative_bound = 2.0 * n * phi_f**(-n / 2.0) + phi_f**(-2 * n)
    tau_bound_witness = tau_bound_witness and remainder <= tau_bound * (1 + 1e-12)
    coarse_bound_witness = coarse_bound_witness and remainder <= coarse_bound * (1 + 1e-12)
    relative_bound_witness = relative_bound_witness and relative <= relative_bound * (1 + 1e-12)
    if n in (8, 16, 32, 64, 80):
        ratios[str(n)] = n * O[n] / (phi_f**n)

checks["tau_remainder_bound_witness_n2_to_n80"] = tau_bound_witness
checks["coarse_remainder_bound_witness_n2_to_n80"] = coarse_bound_witness
checks["relative_error_bound_witness_n2_to_n80"] = relative_bound_witness

# Symbolic normalization identities.
h = sp.log(phi)
d_h = sp.log(phi) / sp.log(2)
kappa = sp.log(2) / (24 * sp.pi)
checks["entropy_dimension_kappa_identity"] = sp.simplify(h - 24 * sp.pi * kappa * d_h) == 0
checks["perron_exponential_rewrite"] = sp.simplify(sp.exp(h) - phi) == 0
checks["kappa_exponential_rewrite"] = sp.simplify(sp.exp(24 * sp.pi * kappa * d_h) - phi) == 0

# Analytic proof receipts / type firewalls.
theorem_compact = compact[THEOREM.stem]
checks["explicit_tau_bound_receipt"] = "\\frac{\\varphi^{-n}}n+\\frac{2(\\tau(n)-1)}n\\varphi^{n/2}" in theorem_compact
checks["asymptotic_receipt"] = "O_n\\sim\\frac{\\varphi^n}n" in theorem_compact
checks["limit_receipt"] = "\\lim_{n\\to\\infty}\\frac{nO_n}{\\varphi^n}=1" in theorem_compact
checks["dynamical_prime_firewall"] = "primitive dynamical orbit = arithmetic prime integer     FALSE / TYPE_ERROR" in theorem
checks["pnt_firewall"] = "arithmetic prime-number theorem derived | `NOT_DERIVED`" in theorem
checks["riemann_firewall"] = "Riemann-zeta identification | `NOT_DERIVED`" in theorem
checks["rh_firewall"] = "implication for RH | `NONE`" in theorem
checks["physical_firewall"] = "physical particle/cosmological interpretation | `OPEN_NOT_CLAIMED`" in theorem

status = "PASS" if all(checks.values()) else "FAIL"
report = {
    "schema": "tir.golden-mean-prime-orbit-asymptotic/v0.1",
    "status": status,
    "audit_max_period": N,
    "asymptotic": "O_n ~ phi^n/n = exp(n*h_top)/n",
    "coarse_error_bound": "|O_n-phi^n/n| <= 2*phi^(n/2)+1/n",
    "normalized_ratios": ratios,
    "arithmetic_prime_identification": "FALSE_TYPE_ERROR",
    "arithmetic_pnt_derived": False,
    "riemann_zeta_identification": "NOT_DERIVED",
    "rh_implication": "NONE",
    "checks": checks,
}
print(json.dumps(report, indent=2, sort_keys=True))
raise SystemExit(0 if status == "PASS" else 1)
