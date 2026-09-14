#!/usr/bin/env python3
"""Deterministic witness for TIR coefficient-selector precedence falsification v0.2."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]

stage22 = (ROOT / "TIR/frozen_predictions/validation/TIR_POLYGONAL_EXCITATION_STAGE22_SEED_PRECEDENCE_V0_1.md").read_text()
old_atomic = (ROOT / "TIR/integration/tir_half_foundation_v0_6_0/ATOMIC_ASSIGNMENT_CANONIZATION.md").read_text()
parents = (ROOT / "TIR/foundations/TIR_COEFFICIENT_MAGNITUDE_PARENT_EVALUATION_V0_1.md").read_text()
dii = (ROOT / "TIR/foundations/TIR_DYNAMIC_IDENTITY_INVARIANT_V0_2.md").read_text()


def collatz_stopping_length(n: int) -> int:
    steps = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
        if steps > 10000:
            raise RuntimeError("unexpected nontermination in finite witness")
    return steps


active_seeds = [(3, 5), (5, 7), (11, 13)]
centers = [(a + b) // 2 for a, b in active_seeds]
ells = [collatz_stopping_length(c) for c in centers]

# Historical curvature magnitudes/signs are read only after their source tokens are verified.
historical_c_magnitudes = [8, 7]
historical_c_signs = [1, -1]
predicted_c_magnitudes = [ells[1] - 1, ells[2] - 1]
predicted_c_signs = [1 if ells[1] > ells[0] else -1 if ells[1] < ells[0] else 0,
                     1 if ells[2] > ells[1] else -1 if ells[2] < ells[1] else 0]

checks = {
    "stage22_pass": "STAGE_22_SEED_PRECEDENCE_PASS" in stage22,
    "active_precedence_tokens": all(t in stage22 for t in ("(3,5)\\to1", "(5,7)\\to2", "(11,13)\\to3")),
    "older_order_is_preserved_as_historical": all(t in old_atomic for t in ("generation 1: `(3,5)`", "generation 2: `(11,13)`", "generation 3: `(5,7)`")),
    "active_order_differs_from_old_atomic_order": active_seeds != [(3, 5), (11, 13), (5, 7)],
    "active_centers": centers == [4, 6, 12],
    "active_stopping_lengths": ells == [2, 8, 9],
    "historical_parent_packets_present": all(t in parents for t in ("P_{e\\mu}=(0,X_5,X_4,X_3+I)", "P_{\\mu\\tau}=(0,F,I,X_3)")),
    "historical_signed_release_tuples_present": all(t in parents for t in ("(0,+5,+2,+8)", "(0,+3,-1,-7)")),
    "magnitude_rule_fails_both": predicted_c_magnitudes == [7, 8] and predicted_c_magnitudes != historical_c_magnitudes,
    "sign_rule_fails_second": predicted_c_signs == [1, 1] and predicted_c_signs[1] != historical_c_signs[1],
    "dii_tetra_half_turn_present": "q_n=\\frac12\\iff n=3" in dii or "q_n=\frac12\iff n=3" in dii,
}

passed = all(checks.values())
payload = {
    "schema": "TIR_COEFFICIENT_TRANSITION_SELECTOR_PRECEDENCE_FALSIFICATION_V0_2",
    "technical_status": "PASS" if passed else "FAIL",
    "active_seeds": active_seeds,
    "centers": centers,
    "stopping_lengths": ells,
    "predicted_c_magnitudes_under_falsified_rule": predicted_c_magnitudes,
    "historical_c_magnitudes": historical_c_magnitudes,
    "predicted_c_signs_under_falsified_rule": predicted_c_signs,
    "historical_c_signs": historical_c_signs,
    "claim_scope": {
        "stopping_length_magnitude_rule": "FALSIFIED_UNDER_ACTIVE_PRECEDENCE",
        "stopping_length_sign_rule": "FALSIFIED_FOR_SECOND_ACTIVE_TRANSITION",
        "transition_parent_selector": "OPEN",
        "physical_binding": "NOT_CLAIMED",
    },
    "checks": checks,
}
print(json.dumps(payload, indent=2, sort_keys=True))
raise SystemExit(0 if passed else 1)
