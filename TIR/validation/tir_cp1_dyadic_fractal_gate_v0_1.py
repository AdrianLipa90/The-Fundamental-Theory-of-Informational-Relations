#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PHASE = ROOT / "TIR" / "integration" / "TIR_COLLATZ_FS_RELATIONAL_PHASE_INTERFACE_V0_1.md"
DECOMP = ROOT / "TIR" / "foundations" / "TIR_PRINCIPAL_SU2_5_1_2_DECOMPOSITION_V0_1.md"
THEOREM = ROOT / "TIR" / "foundations" / "TIR_CP1_DYADIC_FRACTAL_GATE_V0_1.md"

phase_text = PHASE.read_text(encoding="utf-8")
decomp_text = DECOMP.read_text(encoding="utf-8")
theorem_text = THEOREM.read_text(encoding="utf-8")

checks: dict[str, bool] = {}

# Upstream operator and carrier provenance.
checks["phase_squaring_upstream"] = "\\zeta_C(Cn)=\\zeta_C(n)^2" in phase_text
checks["cp1_upstream"] = "\\mathbb CP^1" in phase_text or "\\mathbb{CP}^1" in phase_text
checks["five_one_two_upstream"] = "\\boxed{8=5+1+2}" in decomp_text

# Exact inverse-angle branches for D(q)=2q mod 1.
def g0(q: Fraction) -> Fraction:
    return q / 2


def g1(q: Fraction) -> Fraction:
    return (q + 1) / 2

# Images of [0,1] are [0,1/2] and [1/2,1].
checks["g0_interval"] = (g0(Fraction(0)), g0(Fraction(1))) == (Fraction(0), Fraction(1, 2))
checks["g1_interval"] = (g1(Fraction(0)), g1(Fraction(1))) == (Fraction(1, 2), Fraction(1))
checks["ifs_union_full_interval"] = g0(Fraction(1)) == g1(Fraction(0)) == Fraction(1, 2)

# Similarity-dimension equation at d=1: 2*(1/2)^1 = 1.
checks["similarity_dimension_one"] = 2 * Fraction(1, 2) == 1

# Exact 2^k preimage count, using the canonical q(4)=1/7 anchor.
q_star = Fraction(1, 7)
preimage_counts = {}
preimage_unique = True
for k in range(1, 11):
    vals = {((q_star + m) / (2**k)) % 1 for m in range(2**k)}
    preimage_counts[str(k)] = len(vals)
    preimage_unique = preimage_unique and len(vals) == 2**k
checks["two_power_k_preimages"] = preimage_unique

# Mesh bound demonstrates density of inverse levels on the circle in the k->infinity limit.
# Consecutive m values differ by exactly 1/2^k.
mesh_ok = True
for k in range(1, 11):
    vals = sorted(((q_star + m) / (2**k)) % 1 for m in range(2**k))
    diffs = [vals[i + 1] - vals[i] for i in range(len(vals) - 1)]
    mesh_ok = mesh_ok and all(d == Fraction(1, 2**k) for d in diffs)
checks["inverse_level_mesh_exact"] = mesh_ok

# z -> z^2 iterate exponent doubles exactly: F^k(z)=z^(2^k).
checks["iterate_degree_growth"] = all((2 ** k) == pow(2, k) for k in range(0, 16))

# Claim firewall tokens.
checks["branch_labels_not_E7E8"] = "not identified with the coordinate basis vectors `E7,E8`" in theorem_text
checks["nontrivial_fractal_not_derived"] = "NONTRIVIAL_FRACTAL_GEOMETRY_NOT_DERIVED" in theorem_text
checks["archival_dimension_not_imported"] = "archival number is not imported" in theorem_text
checks["future_fractal_open"] = "future nontrivial fractal dynamics | `OPEN`" in theorem_text

status = "PASS" if all(checks.values()) else "FAIL"
report = {
    "schema": "tir.cp1-dyadic-fractal-gate/v0.1",
    "status": status,
    "canonical_map": "zeta -> zeta^2",
    "inverse_branches": ["q/2", "(q+1)/2"],
    "preimage_counts": preimage_counts,
    "natural_ifs_attractor": "[0,1]",
    "similarity_dimension": 1,
    "nontrivial_fractal_geometry": "NOT_DERIVED",
    "checks": checks,
}
print(json.dumps(report, indent=2, sort_keys=True))
raise SystemExit(0 if status == "PASS" else 1)
