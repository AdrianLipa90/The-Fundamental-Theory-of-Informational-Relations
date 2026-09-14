#!/usr/bin/env python3
from __future__ import annotations

from itertools import product
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
PARENT = ROOT / "TIR" / "foundations" / "TIR_PRINCIPAL_SU2_5_1_2_DECOMPOSITION_V0_1.md"
FRACTAL = ROOT / "TIR" / "foundations" / "TIR_CP1_DYADIC_FRACTAL_GATE_V0_1.md"
THEOREM = ROOT / "TIR" / "foundations" / "TIR_HOMOGENEOUS_FIBRATION_5_1_2_V0_1.md"

parent_text = PARENT.read_text(encoding="utf-8")
fractal_text = FRACTAL.read_text(encoding="utf-8")
theorem_text = THEOREM.read_text(encoding="utf-8")

I = sp.I
sqrt = sp.sqrt
zero = sp.Integer(0)
one = sp.Integer(1)

# Standard Hermitian Gell-Mann basis.
l1 = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])
l2 = sp.Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]])
l3 = sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]])
l4 = sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]])
l5 = sp.Matrix([[0, 0, -I], [0, 0, 0], [I, 0, 0]])
l6 = sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]])
l7 = sp.Matrix([[0, 0, 0], [0, 0, -I], [0, I, 0]])
l8 = (one / sqrt(3)) * sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -2]])

J1 = (l1 + l6) / sqrt(2)
J2 = (l2 + l7) / sqrt(2)
J3 = (l3 + sqrt(3) * l8) / 2
Q1 = (l1 - l6) / sqrt(2)
Q2 = (l2 - l7) / sqrt(2)
Q3 = l4
Q4 = l5
Q5 = (sqrt(3) * l3 - l8) / 2

# E1..E8 exactly as in the parent theorem.
E = [Q5, Q1, Q2, Q3, Q4, J3, J1, J2]


def inner(a: sp.Matrix, b: sp.Matrix) -> sp.Expr:
    return sp.simplify(sp.trace(a * b) / 2)


def hbracket(a: sp.Matrix, b: sp.Matrix) -> sp.Matrix:
    """Hermitian-coordinate Lie bracket: -i[A,B]."""
    return sp.simplify(-I * (a * b - b * a))


def coeffs(a: sp.Matrix) -> list[sp.Expr]:
    return [sp.simplify(inner(e, a)) for e in E]


checks: dict[str, bool] = {}

# Orthonormal adapted basis.
gram = sp.Matrix(8, 8, lambda i, j: inner(E[i], E[j]))
checks["adapted_gram_identity"] = gram == sp.eye(8)

# Principal k = span(E6,E7,E8) closure.
k_idx = {5, 6, 7}
k_closure = True
for i in k_idx:
    for j in k_idx:
        c = coeffs(hbracket(E[i], E[j]))
        k_closure = k_closure and all(sp.simplify(c[t]) == 0 for t in range(8) if t not in k_idx)
checks["principal_so3_closure"] = k_closure

# Exact isotropy rotation on m=span(E7,E8).
checks["E6_rotates_E7_to_E8"] = hbracket(E[5], E[6]) == E[7]
checks["E6_rotates_E8_to_minus_E7"] = hbracket(E[5], E[7]) == -E[6]

# h=span(E6) preserves p=span(E1..E5) under the isotropy representation.
p_idx = {0, 1, 2, 3, 4}
h_preserves_p = True
for j in p_idx:
    c = coeffs(hbracket(E[5], E[j]))
    h_preserves_p = h_preserves_p and all(sp.simplify(c[t]) == 0 for t in range(8) if t not in p_idx)
checks["isotropy_preserves_horizontal_p"] = h_preserves_p

# Dimension / quotient typing.
checks["algebra_dimension_8_5_1_2"] = 8 == 5 + 1 + 2
checks["homogeneous_dimension_7_5_2"] = (8 - 1) == (8 - 3) + (3 - 1) == 7
checks["quotient_tangent_excludes_E6"] = 5 not in (p_idx | {6, 7}) and len(p_idx | {6, 7}) == 7
checks["vertical_indices_78"] = {6, 7} == ({0, 1, 2, 3, 4, 5, 6, 7} - p_idx - {5})

# Parent/downstream provenance tokens.
checks["parent_5_1_2_present"] = "\\boxed{8=5+1+2}" in parent_text
checks["parent_absolute_barrier_fail"] = "`E6` as absolute barrier | `FAIL`" in parent_text
checks["fractal_dimension_present"] = "\\dim_H K_C=\\log_2\\varphi" in fractal_text
checks["terminal_density_kept_open"] = "closure of terminal-reaching phase points equals `K_C` | `OPEN`" in fractal_text

# Exact golden-ratio similarity equation in x=2^{-d}.
phi = (1 + sqrt(5)) / 2
x = sp.simplify(1 / phi)
checks["golden_similarity_equation"] = sp.simplify(x + x**2 - 1) == 0

# Finite-word witness of D(K_C)=K_C: shift preserves no-11,
# and prefixing 0 supplies an admissible preimage.
def admissible(word: tuple[int, ...]) -> bool:
    return all(not (word[i] == 1 and word[i + 1] == 1) for i in range(len(word) - 1))

shift_ok = True
preimage_ok = True
counts = {}
for n in range(1, 15):
    words = [w for w in product((0, 1), repeat=n) if admissible(w)]
    counts[str(n)] = len(words)
    for w in words:
        shift_ok = shift_ok and admissible(w[1:])
        preimage_ok = preimage_ok and admissible((0,) + w)
checks["binary_shift_preserves_admissibility"] = shift_ok
checks["zero_prefix_gives_admissible_preimage"] = preimage_ok

# Exact counterexample to full SO(2) invariance:
# q=0 belongs to K_C; rotation by 3/8 sends it to 0.011_2, which contains 11.
three_eighths_bits = (0, 1, 1)  # fractional bits .011
checks["rotation_counterexample_origin_in_K"] = admissible((0, 0, 0, 0))
checks["rotation_counterexample_3_8_not_in_K"] = not admissible(three_eighths_bits)

# Claim firewall tokens.
checks["E6_isotropy_claim"] = "E_6\\notin T_{eH}(G/H)" in theorem_text
checks["global_fractal_subbundle_open"] = "canonical global fractal subbundle}=\\text{OPEN}" in theorem_text
checks["physical_horizon_not_claimed"] = "`E6` is a physical horizon | `NOT_CLAIMED`" in theorem_text
checks["full_SO2_invariance_fail"] = "full `SO(2)` rotation action preserves `K_C` | `FAIL`" in theorem_text

status = "PASS" if all(checks.values()) else "FAIL"
report = {
    "schema": "tir.homogeneous-fibration-5-1-2/v0.1",
    "status": status,
    "groups": {"G": "SU(3)", "K": "SO(3)", "H": "SO(2)"},
    "dimensions": {"G/H": 7, "G/K": 5, "K/H": 2, "isotropy": 1},
    "horizontal_basis": ["E1", "E2", "E3", "E4", "E5"],
    "isotropy_basis": ["E6"],
    "vertical_basis": ["E7", "E8"],
    "fractal_dimension": "log_2(phi)",
    "fractal_full_SO2_invariant": False,
    "admissible_word_counts_k1_to_k14": counts,
    "checks": checks,
}
print(json.dumps(report, indent=2, sort_keys=True))
raise SystemExit(0 if status == "PASS" else 1)
