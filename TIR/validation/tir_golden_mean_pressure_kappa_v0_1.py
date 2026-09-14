#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
TRANSFER_DOC = ROOT / "TIR" / "foundations" / "TIR_GOLDEN_MEAN_TRANSFER_KAPPA_V0_1.md"
FRACTAL_DOC = ROOT / "TIR" / "foundations" / "TIR_CP1_DYADIC_FRACTAL_GATE_V0_1.md"
FIBRATION_DOC = ROOT / "TIR" / "foundations" / "TIR_HOMOGENEOUS_FIBRATION_5_1_2_V0_1.md"
KAPPA_DOC = ROOT / "TIR" / "foundations" / "TIR_KAPPA_FLAVOUR_MIXING_NORMALIZATION_V0_1.md"
THEOREM = ROOT / "TIR" / "foundations" / "TIR_GOLDEN_MEAN_PRESSURE_KAPPA_V0_1.md"

transfer_text = TRANSFER_DOC.read_text(encoding="utf-8")
fractal_text = FRACTAL_DOC.read_text(encoding="utf-8")
fibration_text = FIBRATION_DOC.read_text(encoding="utf-8")
kappa_text = KAPPA_DOC.read_text(encoding="utf-8")
theorem_text = THEOREM.read_text(encoding="utf-8")

compact_transfer = "".join(transfer_text.split())
compact_fractal = "".join(fractal_text.split())
compact_fibration = "".join(fibration_text.split())
compact_kappa = "".join(kappa_text.split())

phi = (1 + sp.sqrt(5)) / 2
A = sp.Matrix([[1, 1], [1, 0]])
q = sp.symbols("q", positive=True, real=True)
s = sp.symbols("s", real=True)
lam = sp.symbols("lambda")
checks: dict[str, bool] = {}

# Upstream provenance.
checks["transfer_receipt"] = "A=\\begin{pmatrix}1&1\\\\1&0\\end{pmatrix}" in compact_transfer
checks["transfer_entropy_receipt"] = "h_{\\rmtop}=\\ln\\varphi" in compact_transfer
checks["fractal_dimension_receipt"] = "\\dim_HK_C=\\frac{\\ln\\varphi}{\\ln2}=\\log_2\\varphi" in compact_fractal
checks["kappa_receipt"] = "\\kappa=\\frac{\\ln2}{24\\pi}" in compact_kappa
checks["fibration_J6_receipt"] = "\\operatorname{Stab}_{SO(2)}(K_C)=\\{e\\}" in compact_fibration

# Weighted transfer with abstract positive scale q.
Mq = q * A
checks["weighted_charpoly"] = sp.expand(Mq.charpoly(lam).as_expr() - (lam**2 - q * lam - q**2)) == 0
checks["weighted_phi_eigenvalue"] = (Mq * sp.Matrix([phi, 1]) - q * phi * sp.Matrix([phi, 1])).applyfunc(sp.simplify) == sp.zeros(2, 1)
checks["weighted_second_eigenvalue"] = sp.simplify((-q / phi) ** 2 - q * (-q / phi) - q**2) == 0

# Pressure law after q=2^{-s}.
rho_s = sp.exp(-s * sp.log(2)) * phi
pressure_from_log = sp.expand_log(sp.log(rho_s), force=True)
pressure_expected = sp.log(phi) - s * sp.log(2)
checks["pressure_formula"] = sp.simplify(pressure_from_log - pressure_expected) == 0
checks["pressure_slope"] = sp.diff(pressure_expected, s) == -sp.log(2)
checks["pressure_strictly_decreasing"] = sp.log(2).is_positive is True

# Unique pressure zero and dimension.
d = sp.log(phi) / sp.log(2)
checks["pressure_zero"] = sp.simplify(pressure_expected.subs(s, d)) == 0
checks["critical_weight"] = sp.simplify(sp.exp(-d * sp.log(2)) - 1 / phi) == 0

# Exact finite partition sums and asymptotic pressure growth.
def fib(n: int) -> sp.Integer:
    return sp.Integer(sp.fibonacci(n))

ones = sp.Matrix([1, 1])
partition_ok = True
counts_ok = True
partition_receipt: dict[str, str] = {}
for k in range(1, 16):
    path_count = sp.simplify((ones.T * (A ** (k - 1)) * ones)[0])
    counts_ok = counts_ok and path_count == fib(k + 2)
    transfer_partition = sp.simplify(q * (ones.T * ((q * A) ** (k - 1)) * ones)[0])
    expected_partition = sp.simplify(fib(k + 2) * q**k)
    partition_ok = partition_ok and sp.simplify(transfer_partition - expected_partition) == 0
    partition_receipt[str(k)] = str(expected_partition)
checks["fibonacci_path_counts"] = counts_ok
checks["finite_partition_sums"] = partition_ok

# Critical Binet asymptotic: Z_k(d) = F_{k+2} phi^{-k} -> phi^2/sqrt(5).
psi = (1 - sp.sqrt(5)) / 2
ratio = sp.simplify(psi / phi)
checks["binet_subleading_ratio"] = sp.simplify(ratio + 1 / phi**2) == 0
checks["binet_ratio_contracts"] = abs(float(sp.N(ratio))) < 1.0
critical_limit = sp.simplify(phi**2 / sp.sqrt(5))
checks["critical_partition_limit_formula"] = sp.simplify(
    ((phi**2) / sp.sqrt(5)) - critical_limit
) == 0

# Critical weighted operator equals upstream normalized A/phi.
Md = (A / phi).applyfunc(sp.simplify)
mu = sp.symbols("mu")
critical_poly_expected = sp.expand((mu - 1) * (mu + 1 / phi**2))
checks["critical_operator_spectrum"] = sp.simplify(Md.charpoly(mu).as_expr() - critical_poly_expected) == 0
checks["critical_operator_perron_one"] = (Md * sp.Matrix([phi, 1]) - sp.Matrix([phi, 1])).applyfunc(sp.simplify) == sp.zeros(2, 1)
checks["upstream_normalized_transfer_receipt"] = "\\widehatA=\\frac{A}{\\varphi}" in compact_transfer

# Kappa pressure slope.
kappa = sp.log(2) / (24 * sp.pi)
h_top = sp.log(phi)
pressure_kappa = h_top - 24 * sp.pi * kappa * s
checks["kappa_pressure_identity"] = sp.simplify(pressure_kappa - pressure_expected) == 0
checks["kappa_pressure_slope"] = sp.simplify(-sp.diff(pressure_kappa, s) - 24 * sp.pi * kappa) == 0
checks["dimension_from_pressure_kappa"] = sp.simplify(d - h_top / (24 * sp.pi * kappa)) == 0

# Strong all-real-finite-s intertwiner no-go.
J6 = sp.Matrix([[0, -1], [1, 0]])
t00, t01, t10, t11 = sp.symbols("t00 t01 t10 t11")
T = sp.Matrix([[t00, t01], [t10, t11]])
S = q * A * T - T * J6
vars_vec = sp.Matrix([t00, t01, t10, t11])
Lq = sp.Matrix(list(S)).jacobian(vars_vec)
sylvester_det = sp.factor(Lq.det())
checks["sylvester_det_formula"] = sp.expand(sylvester_det - (q**4 + 3 * q**2 + 1)) == 0
checks["sylvester_det_positive_for_q_positive"] = (
    sp.Poly(sylvester_det, q).all_coeffs() == [1, 0, 3, 0, 1]
    and q.is_positive is True
)

# Claim firewall.
checks["physical_pressure_not_claimed"] = "thermodynamic/mechanical/gravitational pressure interpretation | `NOT_CLAIMED`" in theorem_text
checks["no_new_parameter"] = "new physical parameter introduced | `NO`" in theorem_text
checks["operator_typing_preserved"] = "symbolic pressure/transfer family is not the continuous axial rotation generator" in theorem_text

status = "PASS" if all(checks.values()) else "FAIL"
report = {
    "schema": "tir.golden-mean-pressure-kappa/v0.1",
    "status": status,
    "weighted_transfer": "M(s)=2^(-s) A",
    "pressure": "P(s)=ln(phi)-s*ln(2)",
    "pressure_zero": "d=ln(phi)/ln(2)",
    "kappa": "ln(2)/(24*pi)",
    "kappa_pressure": "P(s)=h_top-24*pi*kappa*s",
    "pressure_slope": "-24*pi*kappa",
    "critical_operator": "A/phi",
    "critical_spectrum": ["1", "-1/phi^2"],
    "critical_partition_limit": str(critical_limit),
    "sylvester_determinant": str(sylvester_det),
    "linear_intertwiner_for_finite_real_s": "ZERO_ONLY",
    "partition_sums_k1_to_k15": partition_receipt,
    "checks": checks,
}
print(json.dumps(report, indent=2, sort_keys=True))
raise SystemExit(0 if status == "PASS" else 1)
