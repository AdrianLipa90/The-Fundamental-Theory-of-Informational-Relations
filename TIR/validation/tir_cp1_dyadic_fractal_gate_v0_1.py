#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
import itertools
import json
import math
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
checks["unreduced_collatz_upstream"] = "3n+1" in phase_text and "n/2" in phase_text
checks["cp1_upstream"] = "\\mathbb CP^1" in phase_text or "\\mathbb{CP}^1" in phase_text
checks["five_one_two_upstream"] = "\\boxed{8=5+1+2}" in decomp_text


def C(n: int) -> int:
    return n // 2 if n % 2 == 0 else 3 * n + 1


def T(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def parity_prefix(f, n: int, k: int) -> str:
    bits: list[str] = []
    for _ in range(k):
        bits.append(str(n & 1))
        n = f(n)
    return "".join(bits)


# Exact local grammar: an odd C-state always maps to an even state.
checks["odd_forces_even"] = all(C(n) % 2 == 0 for n in range(1, 1000, 2))

# Fibonacci language counts and finite-prefix realizability witness.
def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def parse_C_word_to_T_word(w: str) -> str:
    # Append the forced zero if a requested finite prefix ends in 1.
    extended = w + ("0" if w.endswith("1") else "")
    out: list[str] = []
    i = 0
    while i < len(extended):
        if extended[i] == "0":
            out.append("0")
            i += 1
        else:
            assert i + 1 < len(extended) and extended[i : i + 2] == "10"
            out.append("1")
            i += 2
    return "".join(out)


language_counts: dict[str, int] = {}
finite_realizability_ok = True
T_bijection_ok = True
for k in range(1, 11):
    allowed = [
        "".join(bits)
        for bits in itertools.product("01", repeat=k)
        if "11" not in "".join(bits)
    ]
    language_counts[str(k)] = len(allowed)
    finite_realizability_ok = finite_realizability_ok and len(allowed) == fib(k + 2)

    for w in allowed:
        tw = parse_C_word_to_T_word(w)
        m = len(tw)
        modulus = 2**m
        table: dict[str, int] = {}
        for r in range(modulus):
            table[parity_prefix(T, r, m)] = r
        T_bijection_ok = T_bijection_ok and len(table) == modulus
        if tw not in table:
            finite_realizability_ok = False
            continue
        r = table[tw]
        n = r if r > 0 else modulus
        if parity_prefix(C, n, k) != w:
            finite_realizability_ok = False

checks["fibonacci_language_counts"] = all(language_counts[str(k)] == fib(k + 2) for k in range(1, 11))
checks["accelerated_parity_vector_bijection_witness"] = T_bijection_ok
checks["all_tested_11_free_prefixes_realized"] = finite_realizability_ok

# Golden-mean self-similar envelope K = f0(K) union f10(K).
def f0(x: Fraction) -> Fraction:
    return x / 2


def f10(x: Fraction) -> Fraction:
    return Fraction(1, 2) + x / 4

max_k = Fraction(2, 3)
checks["max_admissible_phase_two_thirds"] = f10(max_k) == max_k
checks["f0_hull"] = (f0(Fraction(0)), f0(max_k)) == (Fraction(0), Fraction(1, 3))
checks["f10_hull"] = (f10(Fraction(0)), f10(max_k)) == (Fraction(1, 2), Fraction(2, 3))
checks["strong_separation_gap"] = f0(max_k) < f10(Fraction(0))

# Similarity dimension: x=2^-d solves x+x^2=1, x=1/phi.
phi = (1.0 + math.sqrt(5.0)) / 2.0
dim = math.log(phi, 2.0)
x = 2.0 ** (-dim)
checks["golden_mean_dimension_equation"] = abs((x + x * x) - 1.0) < 1e-14
checks["dimension_noninteger"] = 0.69 < dim < 0.70

# Full degree-two circle covering remains distinct from the admissible subshift.
q_star = Fraction(1, 7)
full_preimage_counts = {}
for k in range(1, 11):
    vals = {((q_star + m) / (2**k)) % 1 for m in range(2**k)}
    full_preimage_counts[str(k)] = len(vals)
checks["full_circle_two_power_k_preimages"] = all(
    full_preimage_counts[str(k)] == 2**k for k in range(1, 11)
)

# Claim firewall tokens.
checks["branch_labels_not_E7E8"] = "not identified with the coordinate basis vectors `E7,E8`" in theorem_text
checks["terminal_closure_kept_open"] = "closure of terminal-reaching phase points equals `K_C` | `OPEN`" in theorem_text
checks["archival_dimension_not_imported"] = "archival number is **not imported**" in theorem_text
checks["physical_fractal_open"] = "physical/cosmological fractal binding | `OPEN`" in theorem_text
checks["golden_mean_dimension_claim_present"] = "log_2\\varphi" in theorem_text

status = "PASS" if all(checks.values()) else "FAIL"
report = {
    "schema": "tir.cp1-dyadic-collatz-fractal-gate/v0.1",
    "status": status,
    "canonical_circle_map": "zeta -> zeta^2",
    "unreduced_collatz_forbidden_word": "11",
    "language_counts_k1_to_k10": language_counts,
    "full_circle_preimage_counts": full_preimage_counts,
    "admissible_ifs": ["x/2", "1/2+x/4"],
    "admissible_hull": ["0", "2/3"],
    "strong_separation_gap": ["1/3", "1/2"],
    "hausdorff_dimension_formula": "log(phi)/log(2)",
    "hausdorff_dimension_numeric": dim,
    "terminal_phase_closure_equals_symbolic_envelope": "OPEN",
    "physical_fractal_binding": "OPEN",
    "checks": checks,
}
print(json.dumps(report, indent=2, sort_keys=True))
raise SystemExit(0 if status == "PASS" else 1)
