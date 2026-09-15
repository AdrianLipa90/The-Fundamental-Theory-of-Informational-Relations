#!/usr/bin/env python3
from __future__ import annotations

import itertools
import json
from fractions import Fraction
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
THEOREM = ROOT / "TIR" / "foundations" / "TIR_GOLDEN_MEAN_CODING_CONJUGACY_V0_1.md"
FRACTAL = ROOT / "TIR" / "foundations" / "TIR_CP1_DYADIC_FRACTAL_GATE_V0_1.md"
TRANSFER = ROOT / "TIR" / "foundations" / "TIR_GOLDEN_MEAN_TRANSFER_KAPPA_V0_1.md"
PRESSURE = ROOT / "TIR" / "foundations" / "TIR_GOLDEN_MEAN_PRESSURE_KAPPA_V0_1.md"

texts = {
    "theorem": THEOREM.read_text(encoding="utf-8"),
    "fractal": FRACTAL.read_text(encoding="utf-8"),
    "transfer": TRANSFER.read_text(encoding="utf-8"),
    "pressure": PRESSURE.read_text(encoding="utf-8"),
}
compact = {key: "".join(value.split()) for key, value in texts.items()}
checks: dict[str, bool] = {}

# Provenance receipts from the exact parent surfaces.
checks["upstream_fractal_language"] = "11\\not\\subsetw" in compact["fractal"]
checks["upstream_fractal_dimension"] = "\\dim_HK_C=\\frac{\\ln\\varphi}{\\ln2}" in compact["fractal"]
checks["upstream_transfer_matrix"] = "A=\\begin{pmatrix}1&1\\\\1&0\\end{pmatrix}" in compact["transfer"]
checks["upstream_pressure_family"] = "M(s)=2^{-s}A" in compact["pressure"]
checks["upstream_pressure_identity"] = "P(s)=h_{\\rmtop}-24\\pi\\kappa" in compact["pressure"]

# Exact adjacency / Lucas identities.
A = sp.Matrix([[1, 1], [1, 0]])
phi = (1 + sp.sqrt(5)) / 2
z = sp.symbols("z")
q = sp.symbols("q", positive=True)
I2 = sp.eye(2)

lam = sp.symbols("lam")
checks["transfer_charpoly"] = sp.expand(A.charpoly(lam).as_expr() - (lam**2 - lam - 1)) == 0
checks["phi_relation"] = sp.simplify(phi**2 - phi - 1) == 0


def lucas(n: int) -> int:
    if n == 0:
        return 2
    if n == 1:
        return 1
    a, b = 2, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def cyclic_no11(word: tuple[int, ...]) -> bool:
    n = len(word)
    return all(not (word[i] == 1 and word[(i + 1) % n] == 1) for i in range(n))


def periodic_binary_point(word: tuple[int, ...]) -> Fraction:
    n = len(word)
    numerator = sum(bit << (n - 1 - j) for j, bit in enumerate(word))
    return Fraction(numerator, (1 << n) - 1)


periodic_counts: dict[str, int] = {}
periodic_exact_match = True
periodic_points_fixed = True
for n in range(1, 13):
    words = [w for w in itertools.product((0, 1), repeat=n) if cyclic_no11(w)]
    periodic_counts[str(n)] = len(words)
    expected = int(sp.trace(A**n))
    periodic_exact_match = periodic_exact_match and len(words) == expected == lucas(n)
    pts = [periodic_binary_point(w) for w in words]
    periodic_points_fixed = periodic_points_fixed and len(set(pts)) == len(words)
    for x in pts:
        den = x.denominator
        image = Fraction(((1 << n) * x.numerator) % den, den)
        periodic_points_fixed = periodic_points_fixed and image == x

checks["cyclic_words_equal_trace_equal_lucas_n1_to_n12"] = periodic_exact_match
checks["periodic_binary_points_distinct_and_fixed_n1_to_n12"] = periodic_points_fixed

# Möbius inversion for exact-period point counts and primitive orbit integrality.
exact_period_counts: dict[str, int] = {}
primitive_orbit_counts: dict[str, int] = {}
mobius_ok = True
for n in range(1, 13):
    divisors = sp.divisors(n)
    exact_n = sum(int(sp.mobius(n // d)) * lucas(d) for d in divisors)
    exact_period_counts[str(n)] = exact_n
    primitive_orbit_counts[str(n)] = exact_n // n
    mobius_ok = mobius_ok and exact_n >= 0 and exact_n % n == 0
    mobius_ok = mobius_ok and sum(exact_period_counts[str(d)] for d in divisors) == lucas(n)
checks["mobius_exact_period_and_primitive_orbits"] = mobius_ok

# Finite-prefix witnesses for injective binary coding and exact conjugacy.
finite_coding_injective = True
finite_conjugacy = True
for n in range(1, 13):
    allowed = [w for w in itertools.product((0, 1), repeat=n) if all(not (w[i] == w[i + 1] == 1) for i in range(n - 1))]
    coded: list[Fraction] = []
    for word in allowed:
        x = sum((Fraction(bit, 1 << (j + 1)) for j, bit in enumerate(word)), Fraction(0, 1))
        coded.append(x)
        shifted = word[1:] + (0,)
        y = sum((Fraction(bit, 1 << (j + 1)) for j, bit in enumerate(shifted)), Fraction(0, 1))
        dx = Fraction((2 * x.numerator) % x.denominator, x.denominator) if x.denominator != 1 else Fraction(0, 1)
        finite_conjugacy = finite_conjugacy and dx == y
    finite_coding_injective = finite_coding_injective and len(set(coded)) == len(coded)
checks["finite_prefix_coding_injective_witness_n1_to_n12"] = finite_coding_injective
checks["finite_prefix_conjugacy_witness_n1_to_n12"] = finite_conjugacy

# Exact Artin-Mazur determinant and coefficient identity.
det_unweighted = sp.expand((I2 - z * A).det())
checks["artin_mazur_determinant"] = sp.expand(det_unweighted - (1 - z - z**2)) == 0
zeta_am = sp.cancel(1 / det_unweighted)
checks["artin_mazur_rational_form"] = sp.simplify(zeta_am - 1 / (1 - z - z**2)) == 0

log_derivative_series = sp.series(z * sp.diff(sp.log(zeta_am), z), z, 0, 13).removeO().expand()
trace_series = sum(sp.trace(A**n) * z**n for n in range(1, 13))
checks["zeta_log_derivative_coefficients_n1_to_n12"] = sp.expand(log_derivative_series - trace_series) == 0
checks["nearest_pole_inverse_phi"] = sp.simplify(1 - (1 / phi) - (1 / phi) ** 2) == 0
checks["other_pole_minus_phi"] = sp.simplify(1 + phi - phi**2) == 0

# Weighted determinant bridge to pressure.
M = q * A
det_weighted = sp.expand((I2 - z * M).det())
checks["weighted_determinant"] = sp.expand(det_weighted - (1 - q * z - q**2 * z**2)) == 0
z_c = sp.simplify(1 / (q * phi))
checks["weighted_positive_pole"] = sp.simplify(det_weighted.subs(z, z_c)) == 0
checks["critical_q_inverse_phi_gives_zc_one"] = sp.simplify(z_c.subs(q, 1 / phi) - 1) == 0

# Theorem-proof / type-firewall receipts.
theorem = texts["theorem"]
checks["injectivity_proof_receipt"] = "The golden-mean constraint removes binary ambiguity" in theorem
checks["homeomorphism_claim_receipt"] = "topological coding homeomorphism" in theorem
checks["conjugacy_claim_receipt"] = "D\\circ\\pi=\\pi\\circ\\sigma" in compact["theorem"]
checks["linear_intertwiner_type_firewall"] = "coding homeomorphism is a linear `E7,E8` intertwiner | `FALSE / TYPE_ERROR`" in theorem
checks["riemann_zeta_firewall"] = "Artin-Mazur zeta equals Riemann zeta | `NOT_DERIVED / NOT_CLAIMED`" in theorem
checks["rh_firewall"] = "implication for RH | `NONE`" in theorem
checks["physical_pole_firewall"] = "physical interpretation of dynamical zeta poles | `OPEN_NOT_CLAIMED`" in theorem

status = "PASS" if all(checks.values()) else "FAIL"
report = {
    "schema": "tir.golden-mean-coding-conjugacy/v0.1",
    "status": status,
    "coding": "pi(b)=sum b_k/2^(k+1)",
    "conjugacy": "D o pi = pi o sigma",
    "transfer_matrix": [[1, 1], [1, 0]],
    "fixed_point_formula": "#Fix(D^n|K_C)=tr(A^n)=L_n",
    "periodic_counts_n1_to_n12": periodic_counts,
    "exact_period_counts_n1_to_n12": exact_period_counts,
    "primitive_orbit_counts_n1_to_n12": primitive_orbit_counts,
    "artin_mazur_zeta": "1/(1-z-z^2)",
    "weighted_zeta": "1/(1-q*z-q^2*z^2), q=2^(-s)",
    "nearest_positive_weighted_pole": "z_c=1/(q*phi)=2^s/phi",
    "riemann_zeta_identification": "NOT_DERIVED",
    "rh_implication": "NONE",
    "checks": checks,
}
print(json.dumps(report, indent=2, sort_keys=True))
raise SystemExit(0 if status == "PASS" else 1)
