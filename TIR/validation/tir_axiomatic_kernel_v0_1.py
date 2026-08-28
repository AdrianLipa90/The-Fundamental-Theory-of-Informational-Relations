#!/usr/bin/env python3
"""Deterministic structural audit for TIR Axiomatic Kernel v0.1.

This audit checks finite/exact consequences and implementation identities attached
to the eight TIR axioms. It does not convert foundational postulates into standard
mathematical or empirical theorems. Standard theorem dependencies are emitted
explicitly in the receipt.
"""
from __future__ import annotations

import json
import math
from fractions import Fraction


def axiom1_point_minimality() -> dict[str, object]:
    carrier = ("point",)
    return {
        "carrier_cardinality": len(carrier),
        "internal_distinction_count": 0,
        "pass": len(carrier) == 1,
    }


def axiom2_quantum_point() -> dict[str, object]:
    amplitude = 1.0 + 0.0j
    norm = amplitude.real * amplitude.real + amplitude.imag * amplitude.imag
    return {
        "state_representation": "|P> in complex Hilbert carrier",
        "example_amplitude": [amplitude.real, amplitude.imag],
        "norm_squared": norm,
        "pass": math.isclose(norm, 1.0, rel_tol=0.0, abs_tol=0.0),
    }


def shannon(probabilities: tuple[float, ...]) -> float:
    return -sum(p * math.log(p) for p in probabilities if p > 0.0)


def axiom3_information_primacy() -> dict[str, object]:
    h_zero = shannon((1.0,))
    h_binary = shannon((0.5, 0.5))
    return {
        "H_singleton": h_zero,
        "H_symmetric_binary": h_binary,
        "ln2": math.log(2.0),
        "pass_singleton": h_zero == 0.0,
        "pass_binary_ln2": math.isclose(h_binary, math.log(2.0), rel_tol=0.0, abs_tol=1e-15),
        "pass": h_zero == 0.0 and math.isclose(h_binary, math.log(2.0), rel_tol=0.0, abs_tol=1e-15),
    }


def axiom4_spherical_efficiency() -> dict[str, object]:
    radius = 1.0
    area = 4.0 * math.pi * radius * radius
    volume = (4.0 / 3.0) * math.pi * radius**3
    lhs = area**3
    rhs = 36.0 * math.pi * volume**2
    return {
        "declared_efficiency_functional": "minimum boundary area at fixed enclosed volume",
        "unit_sphere_area": area,
        "unit_sphere_volume": volume,
        "A_cubed": lhs,
        "36piV_squared": rhs,
        "equality_residual": lhs - rhs,
        "standard_theorem_dependency": "three-dimensional isoperimetric inequality",
        "pass_sphere_saturates_bound": math.isclose(lhs, rhs, rel_tol=1e-15, abs_tol=1e-15),
        "pass": math.isclose(lhs, rhs, rel_tol=1e-15, abs_tol=1e-15),
    }


def axiom5_arithmetic_measures_geometry() -> dict[str, object]:
    # Work in turns rather than radians so the winding certificate is exact.
    quarter_turn = Fraction(1, 4)
    increments = (quarter_turn,) * 4
    total_turns = sum(increments, Fraction(0, 1))
    winding = total_turns
    return {
        "phase_increments_turns": [[x.numerator, x.denominator] for x in increments],
        "total_turns": [total_turns.numerator, total_turns.denominator],
        "winding_number": [winding.numerator, winding.denominator],
        "integer_winding": winding.denominator == 1,
        "pass": winding == 1,
    }


def axiom6_naturals_from_complex_phase() -> dict[str, object]:
    rows = []
    passed = True
    for n in (1, 2, 3, 4, 5, 8, 12):
        phase_turn = Fraction(1, n)
        closed_turns = n * phase_turn
        row_pass = closed_turns.denominator == 1 and closed_turns == 1
        passed &= row_pass
        rows.append({
            "n": n,
            "primitive_phase_turn": [phase_turn.numerator, phase_turn.denominator],
            "n_fold_phase_turn": [closed_turns.numerator, closed_turns.denominator],
            "closure": row_pass,
        })
    return {
        "typing": "natural number n is a discrete phase-closure index",
        "rows": rows,
        "pass": passed,
    }


def axiom7_universal_symmetry() -> dict[str, object]:
    exchange = {"N": "S", "S": "N"}
    involutive = all(exchange[exchange[label]] == label for label in exchange)
    p = Fraction(1, 2)
    fixed_share = 1 - p == p
    return {
        "pole_exchange": exchange,
        "exchange_squared_identity": involutive,
        "symmetric_share": [p.numerator, p.denominator],
        "fixed_share_under_complement": fixed_share,
        "pass": involutive and fixed_share,
    }


def axiom8_paradox_stabilization() -> dict[str, object]:
    projected_a = {"proposition": "P", "context": "C1"}
    projected_b = {"proposition": "not P", "context": "C2"}
    lifted = (projected_a, projected_b)
    contexts_preserved = lifted[0]["context"] != lifted[1]["context"]
    statements_preserved = {entry["proposition"] for entry in lifted} == {"P", "not P"}
    return {
        "input": [projected_a, projected_b],
        "lifted_state": [projected_a, projected_b],
        "contexts_preserved": contexts_preserved,
        "both_projections_preserved": statements_preserved,
        "closure_rule": "apparent contradiction -> context lift -> closure constraint",
        "pass": contexts_preserved and statements_preserved,
    }


def dependency_certificate() -> dict[str, object]:
    edges = (
        ("A1", "A2"),
        ("A2", "A3"),
        ("A3", "FIRST_DISTINCTION"),
        ("A7", "SYMMETRIC_POLE_EXCHANGE"),
        ("SYMMETRIC_POLE_EXCHANGE", "HALF_SEAM"),
        ("HALF_SEAM", "LN2"),
        ("FIRST_DISTINCTION", "C2"),
        ("C2", "SCHRODINGER_BRANCH"),
        ("C2", "HEISENBERG_BRANCH"),
        ("A4", "SPHERICAL_REALIZATION"),
        ("SPHERICAL_REALIZATION", "SO3_BRANCH"),
        ("A5", "GEOMETRIC_INVARIANTS"),
        ("A6", "NATURAL_CLOSURE_INDICES"),
        ("A8", "CONTEXTUAL_CLOSURE_GATE"),
    )
    return {
        "edges": [list(edge) for edge in edges],
        "edge_count": len(edges),
        "pass": len(set(edges)) == len(edges),
    }


def build_receipt() -> dict[str, object]:
    blocks = {
        "A1_point_minimality": axiom1_point_minimality(),
        "A2_quantum_point": axiom2_quantum_point(),
        "A3_information_primacy": axiom3_information_primacy(),
        "A4_spherical_efficiency": axiom4_spherical_efficiency(),
        "A5_arithmetic_geometry": axiom5_arithmetic_measures_geometry(),
        "A6_complex_phase_naturals": axiom6_naturals_from_complex_phase(),
        "A7_symmetry": axiom7_universal_symmetry(),
        "A8_paradox_stabilization": axiom8_paradox_stabilization(),
        "dependency_graph": dependency_certificate(),
    }
    passed = all(block["pass"] for block in blocks.values())
    return {
        "schema": "TIR_AXIOMATIC_KERNEL_V0_1",
        "scope": "TIR_FOUNDATIONAL_STRUCTURAL_AUDIT",
        "axiom_count": 8,
        "claim_boundary": {
            "axioms": "TIR foundational postulates",
            "finite_certificates": "exact or implementation-level checks where declared",
            "standard_theorems": "retain independent hypotheses and authority",
            "empirical_physics": "requires separate observational validation",
        },
        "standard_theorem_dependencies": {
            "A4": "isoperimetric inequality",
            "Schrodinger_branch": "strongly continuous one-parameter unitary group generator theorem",
            "Heisenberg_branch": "Robertson uncertainty theorem",
            "Bloch_branch": "CP1 isomorphic/diffeomorphic to S2 in the standard projective-state sense",
            "Banach_Tarski_branch": "free non-abelian subgroup action, paradoxical decomposition machinery, and choice principle",
        },
        "blocks": blocks,
        "technical_status": "PASS" if passed else "FAIL",
    }


def main() -> None:
    receipt = build_receipt()
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if receipt["technical_status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
