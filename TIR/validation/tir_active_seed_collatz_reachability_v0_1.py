#!/usr/bin/env python3
"""Deterministic validator for TIR active-seed Collatz reachability v0.1."""
from fractions import Fraction
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]

stage22 = (ROOT / "TIR/frozen_predictions/validation/TIR_POLYGONAL_EXCITATION_STAGE22_SEED_PRECEDENCE_V0_1.md").read_text()
stage24 = (ROOT / "TIR/frozen_predictions/validation/TIR_POLYGONAL_EXCITATION_STAGE24_TIR_SEED_CHIRALITY_E8_INTERTWINER_V0_1.md").read_text()
receipt = json.loads((ROOT / "TIR/validation/receipts/idt_collatz_fs_phase_source_v0_1.json").read_text())


def C(n: int) -> int:
    return n // 2 if n % 2 == 0 else 3 * n + 1


def first_hit_or_cycle(start: int, target: int):
    n = start
    seen = set()
    k = 0
    while n not in seen:
        if n == target:
            return k
        seen.add(n)
        n = C(n)
        k += 1
    return None


def corridor_word(start: int, target: int) -> str:
    d = first_hit_or_cycle(start, target)
    if d is None:
        raise ValueError(f"target {target} not reachable from {start}")
    bits = []
    n = start
    for _ in range(d):
        bits.append(str(n % 2))
        n = C(n)
    assert n == target
    return "".join(bits)


def to_one_data(start: int):
    n = start
    bits = []
    seen = set()
    while n != 1:
        if n in seen:
            raise ValueError(f"orbit from {start} repeated before reaching 1")
        seen.add(n)
        bits.append(n % 2)
        n = C(n)
    return bits


def q_from_terminal_orbit(start: int) -> Fraction:
    bits = to_one_data(start)
    L = len(bits)
    q = sum((Fraction(bit, 2 ** (k + 1)) for k, bit in enumerate(bits)), Fraction(0, 1))
    q += Fraction(4, 7 * (2 ** L))
    return q


def mod1(x: Fraction) -> Fraction:
    return Fraction(x.numerator % x.denominator, x.denominator)


active_seeds = [(3, 5), (5, 7), (11, 13)]
centers = [(a + b) // 2 for a, b in active_seeds]
assert centers == [4, 6, 12]

q4 = q_from_terminal_orbit(4)
q6 = q_from_terminal_orbit(6)
q12 = q_from_terminal_orbit(12)

fingerprint_6_to_4 = (first_hit_or_cycle(6, 4), corridor_word(6, 4), q6, q4)
fingerprint_12_to_6 = (first_hit_or_cycle(12, 6), corridor_word(12, 6), q12, q6)

checks = {
    "stage22_current_order_tokens": all(t in stage22 for t in ("(3,5)\\to1", "(5,7)\\to2", "(11,13)\\to3")),
    "stage24_cycle_present": all(t in stage24 for t in ("P_s|s_1\\rangle=|s_2\\rangle", "P_s|s_2\\rangle=|s_3\\rangle", "P_s|s_3\\rangle=|s_1\\rangle")),
    "stage24_dynamic_derivation_explicitly_separate": "dynamical derivation of that cycle from Collatz/Poincare seed evolution remains a separate validation gate" in stage24,
    "idt_source_commit_pinned": receipt.get("upstream_commit_sha") == "f670e60112b578756a90a7b29a4f574c37a8c03f",
    "idt_source_blob_pinned": receipt.get("source_blob_sha") == "727cbadf7bf86c7fdce26ac906d4febe0464b4bc",
    "active_centers": centers == [4, 6, 12],
    "distance_12_to_6": first_hit_or_cycle(12, 6) == 1,
    "distance_6_to_4": first_hit_or_cycle(6, 4) == 6,
    "distance_12_to_4": first_hit_or_cycle(12, 4) == 7,
    "no_upward_4_to_6": first_hit_or_cycle(4, 6) is None,
    "no_upward_4_to_12": first_hit_or_cycle(4, 12) is None,
    "no_upward_6_to_12": first_hit_or_cycle(6, 12) is None,
    "corridor_word_6_to_4": corridor_word(6, 4) == "010100",
    "corridor_word_12_to_6": corridor_word(12, 6) == "0",
    "q4_exact": q4 == Fraction(1, 7),
    "q6_exact": q6 == Fraction(141, 448),
    "q12_exact": q12 == Fraction(141, 896),
    "phase_12_to_6_doubling": mod1(2 * q12) == q6,
    "phase_6_to_4_six_steps": mod1((2 ** 6) * q6) == q4,
    "phase_12_to_4_seven_steps": mod1((2 ** 7) * q12) == q4,
    "label_cycle_not_raw_center_collatz": first_hit_or_cycle(4, 6) is None and first_hit_or_cycle(6, 12) is None,
    "corridor_fingerprints_distinct": fingerprint_6_to_4 != fingerprint_12_to_6,
}

passed = all(checks.values())
payload = {
    "schema": "TIR_ACTIVE_SEED_COLLATZ_REACHABILITY_V0_1",
    "technical_status": "PASS" if passed else "FAIL",
    "active_seeds": active_seeds,
    "centers": centers,
    "first_hit_distances": {"12_to_6": 1, "6_to_4": 6, "12_to_4": 7},
    "corridor_words": {"6_to_4": corridor_word(6, 4), "12_to_6": corridor_word(12, 6)},
    "q_exact": {"4": str(q4), "6": str(q6), "12": str(q12)},
    "claim_scope": {
        "center_reachability_chain": "EXACT_INTEGER_COMPUTATION",
        "stage24_cycle_from_raw_center_collatz": "REFUTED",
        "transition_corridor_fingerprint": "EXACT_COEFFICIENT_FREE_INPUT",
        "coefficient_parent_selector": "OPEN",
        "physical_binding": "NOT_CLAIMED",
    },
    "checks": checks,
}
print(json.dumps(payload, indent=2, sort_keys=True))
raise SystemExit(0 if passed else 1)
