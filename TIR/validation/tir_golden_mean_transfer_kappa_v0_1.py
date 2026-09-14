#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
KAPPA_DOC = ROOT / "TIR" / "foundations" / "TIR_KAPPA_FLAVOUR_MIXING_NORMALIZATION_V0_1.md"
FRACTAL_DOC = ROOT / "TIR" / "foundations" / "TIR_CP1_DYADIC_FRACTAL_GATE_V0_1.md"
FIBRATION_DOC = ROOT / "TIR" / "foundations" / "TIR_HOMOGENEOUS_FIBRATION_5_1_2_V0_1.md"
THEOREM = ROOT / "TIR" / "foundations" / "TIR_GOLDEN_MEAN_TRANSFER_KAPPA_V0_1.md"

kappa_text = KAPPA_DOC.read_text(encoding="utf-8")
fractal_text = FRACTAL_DOC.read_text(encoding="utf-8")
fibration_text = FIBRATION_DOC.read_text(encoding="utf-8")
theorem_text = THEOREM.read_text(encoding="utf-8")

compact_kappa = "".join(kappa_text.split())
compact_fractal = "".join(fractal_text.split())
compact_fibration = "".join(fibration_text.split())

sqrt5 = sp.sqrt(5)
phi = (1 + sqrt5) / 2
A = sp.Matrix([[1, 1], [1, 0]])
checks: dict[str, bool] = {}

# Upstream provenance.
checks["canonical_kappa_receipt"] = "\\kappa=\\frac{\\ln2}{24\\pi}" in compact_kappa
checks["golden_fractal_dimension_receipt"] = (
    "\\dim_HK_C=\\frac{\\ln\\varphi}{\\ln2}=\\log_2\\varphi" in compact_fractal
)
checks["fibration_axial_stabilizer_receipt"] = (
    "\\operatorname{Stab}_{SO(2)}(K_C)=\\{e\\}" in compact_fibration
)

# Transfer matrix spectrum.
lam = sp.symbols("lambda")
charpoly = sp.expand(A.charpoly(lam).as_expr())
checks["transfer_charpoly"] = sp.expand(charpoly - (lam**2 - lam - 1)) == 0
checks["phi_root"] = sp.simplify(phi**2 - phi - 1) == 0
checks["second_root_minus_inverse_phi"] = sp.simplify((1 - sqrt5) / 2 + 1 / phi) == 0
perron_residual = (A * sp.Matrix([phi, 1]) - phi * sp.Matrix([phi, 1])).applyfunc(sp.simplify)
checks["perron_vector"] = perron_residual == sp.zeros(2, 1)

# Fibonacci power law and path counts.
def fib(n: int) -> sp.Integer:
    return sp.Integer(sp.fibonacci(n))

matrix_power_ok = True
word_count_ok = True
ones = sp.Matrix([1, 1])
word_counts: dict[str, int] = {}
for n in range(1, 16):
    expected = sp.Matrix([[fib(n + 1), fib(n)], [fib(n), fib(n - 1)]])
    matrix_power_ok = matrix_power_ok and (A**n == expected)
for k in range(1, 16):
    count = int((ones.T * (A ** (k - 1)) * ones)[0])
    word_counts[str(k)] = count
    word_count_ok = word_count_ok and count == int(fib(k + 2))
checks["fibonacci_matrix_power"] = matrix_power_ok
checks["fibonacci_word_count"] = word_count_ok

# Topological entropy / fractal dimension / kappa identity.
h_top = sp.log(phi)
d_h = sp.log(phi) / sp.log(2)
kappa = sp.log(2) / (24 * sp.pi)
kappa_phi = sp.simplify(kappa * d_h)
checks["dimension_entropy_crosswalk"] = sp.simplify(d_h - h_top / sp.log(2)) == 0
checks["kappa_identity"] = sp.simplify(h_top - 24 * sp.pi * kappa * d_h) == 0
checks["kappa_phi_identity"] = sp.simplify(kappa_phi - sp.log(phi) / (24 * sp.pi)) == 0

# Parry transition matrix and stationary distribution.
P = sp.Matrix([[1 / phi, 1 / phi**2], [1, 0]]).applyfunc(sp.simplify)
pi0 = sp.simplify(phi**2 / (phi**2 + 1))
pi1 = sp.simplify(1 / (phi**2 + 1))
pi_row = sp.Matrix([[pi0, pi1]])
checks["parry_row_stochastic"] = all(sp.simplify(sum(P[i, j] for j in range(2)) - 1) == 0 for i in range(2))
checks["parry_stationary"] = (pi_row * P - pi_row).applyfunc(sp.simplify) == sp.zeros(1, 2)
checks["stationary_normalized"] = sp.simplify(pi0 + pi1 - 1) == 0

# Entropy rate: log(phi) times an exact coefficient that must equal one.
entropy_coefficient = sp.simplify(pi0 * (1 / phi + 2 / phi**2))
checks["parry_entropy_coefficient_one"] = sp.simplify(entropy_coefficient - 1) == 0
checks["parry_entropy_rate_ln_phi"] = checks["parry_entropy_coefficient_one"]

# Normalized transfer spectrum.
Ahat = (A / phi).applyfunc(sp.simplify)
mu = sp.symbols("mu")
expected_ahat_poly = sp.expand((mu - 1) * (mu + 1 / phi**2))
checks["normalized_transfer_spectrum"] = sp.simplify(Ahat.charpoly(mu).as_expr() - expected_ahat_poly) == 0

# Reconstruct E6/E7/E8 from the parent principal embedding.
I = sp.I
sqrt = sp.sqrt
l1 = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])
l2 = sp.Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]])
l3 = sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]])
l6 = sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]])
l7 = sp.Matrix([[0, 0, 0], [0, 0, -I], [0, I, 0]])
l8 = (1 / sqrt(3)) * sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -2]])
E6 = (l3 + sqrt(3) * l8) / 2
E7 = (l1 + l6) / sqrt(2)
E8 = (l2 + l7) / sqrt(2)


def hbracket(x: sp.Matrix, y: sp.Matrix) -> sp.Matrix:
    return sp.simplify(-I * (x * y - y * x))


def inner(x: sp.Matrix, y: sp.Matrix) -> sp.Expr:
    return sp.simplify(sp.trace(x * y) / 2)

# Columns are the coordinates of J6(E7), J6(E8) in ordered basis (E7,E8).
J6 = sp.Matrix([
    [inner(E7, hbracket(E6, E7)), inner(E7, hbracket(E6, E8))],
    [inner(E8, hbracket(E6, E7)), inner(E8, hbracket(E6, E8))],
]).applyfunc(sp.simplify)
J6_expected = sp.Matrix([[0, -1], [1, 0]])
checks["J6_matrix"] = J6 == J6_expected
nu = sp.symbols("nu")
checks["J6_charpoly"] = sp.expand(J6.charpoly(nu).as_expr() - (nu**2 + 1)) == 0

# Disjoint spectra: neither +/-i solves the transfer characteristic polynomial.
checks["spectra_disjoint_plus_i"] = sp.simplify((I**2 - I - 1)) != 0
checks["spectra_disjoint_minus_i"] = sp.simplify(((-I)**2 - (-I) - 1)) != 0

# Strong Sylvester no-go: solve A*T - T*J6 = 0 over C.
t00, t01, t10, t11 = sp.symbols("t00 t01 t10 t11")
T = sp.Matrix([[t00, t01], [t10, t11]])
S = A * T - T * J6
eqs = list(S)
solution = sp.linsolve(eqs, (t00, t01, t10, t11))
checks["sylvester_only_zero"] = solution == sp.FiniteSet((0, 0, 0, 0))

# Claim-firewall tokens.
checks["no_physical_entropy_claim"] = "physical entropy/time/energy interpretation | `OPEN_NOT_CLAIMED`" in theorem_text
checks["intertwiner_fail_claim"] = "nonzero linear intertwiner `A T = T J6` | `FAIL`" in theorem_text
checks["state_basis_identification_not_derived"] = "literal identification of symbolic states with `E7,E8` | `NOT_DERIVED`" in theorem_text
checks["kappa_not_rederived_from_fractal"] = "does **not** derive `κ` from the golden-mean fractal" in theorem_text

status = "PASS" if all(checks.values()) else "FAIL"
report = {
    "schema": "tir.golden-mean-transfer-kappa/v0.1",
    "status": status,
    "transfer_matrix": [[1, 1], [1, 0]],
    "transfer_spectrum": ["phi", "-1/phi"],
    "spectral_radius": "phi",
    "topological_entropy": "ln(phi)",
    "hausdorff_dimension": "ln(phi)/ln(2)",
    "kappa": "ln(2)/(24*pi)",
    "normalization_identity": "h_top = 24*pi*kappa*dim_H(K_C)",
    "derived_kappa_phi": "ln(phi)/(24*pi)",
    "normalized_transfer_spectrum": ["1", "-1/phi^2"],
    "geometric_J6": [[0, -1], [1, 0]],
    "geometric_J6_spectrum": ["+i", "-i"],
    "linear_intertwiner": "ZERO_ONLY",
    "word_counts_k1_to_k15": word_counts,
    "checks": checks,
}
print(json.dumps(report, indent=2, sort_keys=True))
raise SystemExit(0 if status == "PASS" else 1)
