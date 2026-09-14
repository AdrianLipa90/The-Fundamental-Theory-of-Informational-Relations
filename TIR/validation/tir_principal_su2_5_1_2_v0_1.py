#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp

I = sp.I
SQRT2 = sp.sqrt(2)
SQRT3 = sp.sqrt(3)
Z3 = sp.zeros(3)


def mm(rows):
    return sp.Matrix(rows)


# Standard Hermitian Gell-Mann matrices.
l1 = mm([[0, 1, 0], [1, 0, 0], [0, 0, 0]])
l2 = mm([[0, -I, 0], [I, 0, 0], [0, 0, 0]])
l3 = mm([[1, 0, 0], [0, -1, 0], [0, 0, 0]])
l4 = mm([[0, 0, 1], [0, 0, 0], [1, 0, 0]])
l5 = mm([[0, 0, -I], [0, 0, 0], [I, 0, 0]])
l6 = mm([[0, 0, 0], [0, 0, 1], [0, 1, 0]])
l7 = mm([[0, 0, 0], [0, 0, -I], [0, I, 0]])
l8 = mm([[1, 0, 0], [0, 1, 0], [0, 0, -2]]) / SQRT3
LAM = [l1, l2, l3, l4, l5, l6, l7, l8]


def comm(a: sp.Matrix, b: sp.Matrix) -> sp.Matrix:
    return sp.simplify(a * b - b * a)


def inner(a: sp.Matrix, b: sp.Matrix):
    return sp.simplify(sp.trace(a * b) / 2)


def is_zero_matrix(m: sp.Matrix) -> bool:
    return all(sp.simplify(x) == 0 for x in m)


def equal(a: sp.Matrix, b: sp.Matrix) -> bool:
    return is_zero_matrix(sp.simplify(a - b))


# Principal spin-1 SU(2) embedding.
J1 = (l1 + l6) / SQRT2
J2 = (l2 + l7) / SQRT2
J3 = (l3 + SQRT3 * l8) / 2
J = [J1, J2, J3]

# Orthogonal spin-2 complement.
Q1 = (l1 - l6) / SQRT2
Q2 = (l2 - l7) / SQRT2
Q3 = l4
Q4 = l5
Q5 = (SQRT3 * l3 - l8) / 2
Q = [Q1, Q2, Q3, Q4, Q5]

# Orthonormal decomposition basis p5 + h3.
B = Q + J

# Mnemonic adapted basis 12345|6|78.
E = [Q5, Q1, Q2, Q3, Q4, J3, J1, J2]


def support_of_hermitian(m: sp.Matrix, basis: list[sp.Matrix]) -> set[int]:
    coeffs = [sp.simplify(inner(b, m)) for b in basis]
    residual = sp.simplify(m - sum((c * b for c, b in zip(coeffs, basis)), sp.zeros(3)))
    if not is_zero_matrix(residual):
        raise AssertionError(f"basis decomposition residual is nonzero: {residual}")
    return {i for i, c in enumerate(coeffs) if sp.simplify(c) != 0}


checks: dict[str, bool] = {}

# Gell-Mann normalization.
gram_lam = sp.Matrix([[inner(a, b) for b in LAM] for a in LAM])
checks["gell_mann_orthonormal"] = gram_lam == sp.eye(8)

# Principal SU(2) commutators and spin-1 Casimir.
checks["J12_iJ3"] = equal(comm(J1, J2), I * J3)
checks["J23_iJ1"] = equal(comm(J2, J3), I * J1)
checks["J31_iJ2"] = equal(comm(J3, J1), I * J2)
casimir = sp.simplify(J1 * J1 + J2 * J2 + J3 * J3)
checks["spin1_casimir_2I"] = equal(casimir, 2 * sp.eye(3))

# Full 5+3 adapted Gram matrix.
gram_B = sp.Matrix([[inner(a, b) for b in B] for a in B])
checks["adapted_basis_orthonormal"] = gram_B == sp.eye(8)

# Symmetric-pair support rules.  comm/i is Hermitian and can be expanded in B.
hh_ok = True
hp_ok = True
pp_ok = True
for a in range(5, 8):
    for b in range(a + 1, 8):
        supp = support_of_hermitian(sp.simplify(comm(B[a], B[b]) / I), B)
        hh_ok = hh_ok and supp.issubset({5, 6, 7})
for a in range(5, 8):
    for b in range(0, 5):
        supp = support_of_hermitian(sp.simplify(comm(B[a], B[b]) / I), B)
        hp_ok = hp_ok and supp.issubset({0, 1, 2, 3, 4})
for a in range(0, 5):
    for b in range(a + 1, 5):
        supp = support_of_hermitian(sp.simplify(comm(B[a], B[b]) / I), B)
        pp_ok = pp_ok and supp.issubset({5, 6, 7})
checks["symmetric_pair_hh_to_h"] = hh_ok
checks["symmetric_pair_hp_to_p"] = hp_ok
checks["symmetric_pair_pp_to_h"] = pp_ok

# Explicit 12345|6|78 commutators.
checks["E6E7_iE8"] = equal(comm(E[5], E[6]), I * E[7])
checks["E6E8_minus_iE7"] = equal(comm(E[5], E[7]), -I * E[6])
checks["E7E8_iE6"] = equal(comm(E[6], E[7]), I * E[5])
checks["E2E3_iE6"] = equal(comm(E[1], E[2]), I * E[5])
checks["E4E5_2iE6"] = equal(comm(E[3], E[4]), 2 * I * E[5])
checks["E2E4_iE8"] = equal(comm(E[1], E[3]), I * E[7])
checks["E2E5_minus_iE7"] = equal(comm(E[1], E[4]), -I * E[6])
checks["E3E4_iE7"] = equal(comm(E[2], E[3]), I * E[6])
checks["E3E5_iE8"] = equal(comm(E[2], E[4]), I * E[7])

# Negative control against an absolute 5|6|78 barrier.
direct_5_to_78 = (
    not is_zero_matrix(comm(E[1], E[3]))
    and not is_zero_matrix(comm(E[1], E[4]))
)
checks["absolute_barrier_negative_control"] = direct_5_to_78

# Complexified adjoint spectrum of raw ad(E6).
# Coefficients are complex because [Hermitian,Hermitian] is anti-Hermitian.
ad6 = sp.Matrix(
    [[sp.simplify(inner(B[r], comm(E[5], B[c]))) for c in range(8)] for r in range(8)]
)
x = sp.symbols("x")
char_ad6 = sp.factor(ad6.charpoly(x).as_expr())
expected_ad6 = sp.expand(x**2 * (x**2 - 1) ** 2 * (x**2 - 4))
checks["adE6_characteristic_polynomial"] = sp.expand(char_ad6 - expected_ad6) == 0
checks["adE6_weights"] = ad6.eigenvals() == {
    sp.Integer(-2): 1,
    sp.Integer(-1): 2,
    sp.Integer(0): 2,
    sp.Integer(1): 2,
    sp.Integer(2): 1,
}

# Differently typed real-Hermitian representation -i ad(E6).
rot6 = sp.simplify(-I * ad6)
char_rot6 = sp.factor(rot6.charpoly(x).as_expr())
expected_rot6 = sp.expand(x**2 * (x**2 + 1) ** 2 * (x**2 + 4))
checks["minus_i_adE6_rotation_spectrum"] = sp.expand(char_rot6 - expected_rot6) == 0

# Upstream provenance tokens: DII axis and CP1 two-pole carrier already exist.
root = Path(__file__).resolve().parents[2]
dii_path = root / "TIR" / "foundations" / "TIR_DYNAMIC_IDENTITY_INVARIANT_V0_1.md"
cp1_path = root / "TIR" / "frozen_predictions" / "validation" / "TIR_POLYGONAL_EXCITATION_STAGE23_CHIRALITY_INTERTWINER_V0_1.md"
theorem_path = root / "TIR" / "foundations" / "TIR_PRINCIPAL_SU2_5_1_2_DECOMPOSITION_V0_1.md"

dii_text = dii_path.read_text(encoding="utf-8")
cp1_text = cp1_path.read_text(encoding="utf-8")
theorem_text = theorem_path.read_text(encoding="utf-8")
checks["upstream_dii_axis_present"] = "Sigma_i" in dii_text and "Pauli" in dii_text
checks["upstream_cp1_two_pole_present"] = "CP1/Bloch two-pole selector" in cp1_text
checks["theorem_keeps_fractal_open"] = "fractal dynamics on the `78` carrier | `OPEN`" in theorem_text
checks["theorem_rejects_physical_horizon_claim"] = "physical horizon identification | `NOT_CLAIMED`" in theorem_text

status = "PASS" if all(checks.values()) else "FAIL"
report = {
    "schema": "tir.principal-su2-5-1-2/v0.1",
    "status": status,
    "base_decomposition": "8=5+3=5+1+2",
    "complexified_adE6_charpoly": str(char_ad6),
    "real_basis_minus_i_adE6_charpoly": str(char_rot6),
    "absolute_barrier_hypothesis": "FAIL" if direct_5_to_78 else "UNRESOLVED",
    "physical_horizon_binding": "NOT_CLAIMED",
    "fractal_dynamics": "OPEN",
    "checks": checks,
}
print(json.dumps(report, indent=2, sort_keys=True))
raise SystemExit(0 if status == "PASS" else 1)
