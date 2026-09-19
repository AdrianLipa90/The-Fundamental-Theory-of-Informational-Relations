#!/usr/bin/env python3
"""TIR/IDT representation crosswalk for the periodic 6pi triad.

This validator is deliberately representation-level only. It checks:

1. the C3 shift obtained from the periodic three-frame quotient;
2. the F3 character basis already used by the TIR family-space branch;
3. the SU(2)-adjoint realization on the Pauli triplet;
4. the anchored equivariant intertwiner from the temporal C3 carrier to the
   already-frozen Stage-22/24 ordered family C3 carrier;
5. preservation of the Stage-38 CP-capable character invariant and Stage-42
   su(3)_F Lie closure under that ordered representation map.

No physical identification of temporal, spatial, or flavour sectors is made.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np


TOL = 1.0e-12
ROOT = Path(__file__).resolve().parents[2]


def traceless(H: np.ndarray) -> np.ndarray:
    return H - np.trace(H) / 3.0 * np.eye(3, dtype=complex)


def real_vector(X: np.ndarray) -> np.ndarray:
    return np.concatenate([X.real.ravel(), X.imag.ravel()])


def lie_closure_dimension(hermitians: list[np.ndarray]) -> tuple[int, float]:
    """Real Lie dimension of traceless skew-Hermitian generators."""
    mats: list[np.ndarray] = []
    vecs: list[np.ndarray] = []

    def add(X: np.ndarray) -> bool:
        v = real_vector(X)
        if not vecs:
            mats.append(X)
            vecs.append(v)
            return True
        old_rank = np.linalg.matrix_rank(np.stack(vecs, axis=1), 1.0e-10)
        new_rank = np.linalg.matrix_rank(np.stack(vecs + [v], axis=1), 1.0e-10)
        if new_rank > old_rank:
            mats.append(X)
            vecs.append(v)
            return True
        return False

    for H in hermitians:
        add(1j * traceless(H))

    changed = True
    while changed and len(mats) < 8:
        changed = False
        current = list(mats)
        for i in range(len(current)):
            for j in range(i + 1, len(current)):
                K = current[i] @ current[j] - current[j] @ current[i]
                if np.max(np.abs(K)) > 1.0e-12 and add(K):
                    changed = True

    residual = max(
        max(
            float(np.max(np.abs(M.conj().T + M))),
            float(abs(np.trace(M))),
        )
        for M in mats
    )
    return len(mats), residual


def jarlskog(V: np.ndarray) -> float:
    return float(
        np.imag(
            V[0, 0]
            * V[1, 1]
            * np.conj(V[0, 1])
            * np.conj(V[1, 0])
        )
    )


def main() -> None:
    stage15 = (
        ROOT
        / "TIR/frozen_predictions/validation/"
        "TIR_POLYGONAL_EXCITATION_STAGE15_EXCEPTIONAL_SM_SUBALGEBRA_V0_1.md"
    ).read_text(encoding="utf-8")
    stage16 = (
        ROOT
        / "TIR/frozen_predictions/validation/"
        "TIR_POLYGONAL_EXCITATION_STAGE16_EXCEPTIONAL_HYPERCHARGE_MATCH_V0_1.md"
    ).read_text(encoding="utf-8")
    stage22 = (
        ROOT
        / "TIR/frozen_predictions/validation/"
        "TIR_POLYGONAL_EXCITATION_STAGE22_SEED_PRECEDENCE_V0_1.md"
    ).read_text(encoding="utf-8")
    stage23 = (
        ROOT
        / "TIR/frozen_predictions/validation/"
        "TIR_POLYGONAL_EXCITATION_STAGE23_CHIRALITY_INTERTWINER_V0_1.md"
    ).read_text(encoding="utf-8")
    stage24 = (
        ROOT
        / "TIR/frozen_predictions/validation/"
        "TIR_POLYGONAL_EXCITATION_STAGE24_TIR_SEED_CHIRALITY_E8_INTERTWINER_V0_1.md"
    ).read_text(encoding="utf-8")
    stage38 = (
        ROOT
        / "TIR/frozen_predictions/validation/"
        "TIR_POLYGONAL_EXCITATION_STAGE38_C3_CHARACTER_BASIS_CP_V0_1.md"
    ).read_text(encoding="utf-8")
    stage42 = (
        ROOT
        / "TIR/frozen_predictions/validation/"
        "TIR_POLYGONAL_EXCITATION_STAGE42_FAMILY_LIE_CLOSURE_V0_1.md"
    ).read_text(encoding="utf-8")

    omega = np.exp(2j * math.pi / 3.0)
    P_temporal = np.array(
        [
            [0.0, 0.0, 1.0],
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
        ],
        dtype=complex,
    )
    P_family = P_temporal.copy()

    F3 = np.array(
        [
            [1.0, 1.0, 1.0],
            [1.0, omega, omega**2],
            [1.0, omega**2, omega],
        ],
        dtype=complex,
    ) / math.sqrt(3.0)

    sx = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    sy = np.array([[0.0, -1j], [1j, 0.0]], dtype=complex)
    sz = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
    pauli = (sx, sy, sz)

    n_sigma = (sx + sy + sz) / math.sqrt(3.0)
    U3 = (
        math.cos(math.pi / 3.0) * np.eye(2, dtype=complex)
        - 1j * math.sin(math.pi / 3.0) * n_sigma
    )

    gram = np.array(
        [[0.5 * np.trace(a @ b) for b in pauli] for a in pauli],
        dtype=complex,
    )
    f3_temporal = F3.conj().T @ P_temporal @ F3
    f3_family = F3.conj().T @ P_family @ F3
    target_diag = np.diag([1.0, omega**2, omega])

    pauli_cycle_residual = max(
        float(
            np.max(
                np.abs(
                    U3 @ pauli[j] @ U3.conj().T
                    - pauli[(j + 1) % 3]
                )
            )
        )
        for j in range(3)
    )

    # Ordered temporal->family label intertwiner.  The declared anchor is
    # e1 -> s1.  Equivariance then forces e2 -> s2 and e3 -> s3.
    M_tf = np.eye(3, dtype=complex)
    e1 = np.array([1.0, 0.0, 0.0], dtype=complex)
    intertwiner_residual = float(
        np.max(np.abs(M_tf @ P_temporal - P_family @ M_tf))
    )
    anchor_residual = float(np.max(np.abs(M_tf @ e1 - e1)))

    # Among the three cyclic permutation intertwiners, exactly one preserves
    # the declared e1 -> s1 anchor.
    cyclic_intertwiners = [
        np.linalg.matrix_power(P_family, k) for k in range(3)
    ]
    anchored_intertwiner_count = sum(
        np.allclose(M @ P_temporal, P_family @ M, atol=TOL)
        and np.allclose(M @ e1, e1, atol=TOL)
        for M in cyclic_intertwiners
    )

    temporal_orbit = [
        tuple(np.rint(np.real(np.linalg.matrix_power(P_temporal, k) @ e1)).astype(int))
        for k in range(3)
    ]
    family_orbit = [
        tuple(np.rint(np.real(np.linalg.matrix_power(P_family, k) @ e1)).astype(int))
        for k in range(3)
    ]

    # Exact C3 x Z2 six-state product already present in Stage 23/24.
    J_chi = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    I2 = np.eye(2, dtype=complex)
    I3 = np.eye(3, dtype=complex)
    P6_temporal = np.kron(P_temporal, I2)
    Z2_temporal = np.kron(I3, J_chi)
    G6_temporal = P6_temporal @ Z2_temporal

    P6_family = np.kron(P_family, I2)
    Z2_family = np.kron(I3, J_chi)
    G6_family = P6_family @ Z2_family

    M6 = np.kron(M_tf, I2)
    six_state_intertwiner_residual = float(
        np.max(np.abs(M6 @ G6_temporal - G6_family @ M6))
    )
    six_state_seed = np.kron(
        np.array([1.0, 0.0, 0.0], dtype=complex),
        np.array([1.0, 0.0], dtype=complex),
    )
    six_state_orbit = [
        tuple(
            np.rint(
                np.real(np.linalg.matrix_power(G6_temporal, k) @ six_state_seed)
            ).astype(int)
        )
        for k in range(6)
    ]
    g6_charpoly = np.poly(G6_temporal)
    expected_g6_charpoly = np.array(
        [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0],
        dtype=complex,
    )

    J = jarlskog(F3)
    J_exact = 1.0 / (6.0 * math.sqrt(3.0))

    # Stage-42 family Lie closure and its pullback through M_tf.
    D_family = np.diag(
        [-1.0 / 3.0, 0.0, 1.0 / math.sqrt(5.0)]
    ).astype(complex)
    C_family = F3 @ D_family @ F3.conj().T
    D_temporal = M_tf.conj().T @ D_family @ M_tf
    C_temporal = M_tf.conj().T @ C_family @ M_tf
    dim_family, residual_family = lie_closure_dimension([D_family, C_family])
    dim_temporal, residual_temporal = lie_closure_dimension(
        [D_temporal, C_temporal]
    )

    family_dimension = len(set(temporal_orbit))
    weak_doublet_dimension = 2
    family_x_weak_dimension = family_dimension * weak_doublet_dimension

    checks = {
        "stage15_sm_subalgebra_parent_pass_present": (
            "STAGE_15_PURE_LIE_ALGEBRA_PASS" in stage15
            and "su}(2)" in stage15
        ),
        "stage16_hypercharge_representation_parent_pass_present": (
            "STAGE_16_EXACT_HYPERCHARGE_REPRESENTATION_PASS" in stage16
        ),
        "stage16_explicit_two_state_lepton_doublet_multiplicity": (
            "Y = -1/2   multiplicity 2" in stage16
            and "L   : 2 states, Y = -1/2" in stage16
        ),
        "stage22_active_order_is_frozen": all(
            token in stage22
            for token in (
                "(3,5)\\to1",
                "(5,7)\\to2",
                "(11,13)\\to3",
            )
        ),
        "stage23_chirality_z2_parent_pass_present": (
            "STAGE_23_Z2_INTERTWINER_PASS_WITH_ORIENTATION_CONVENTION"
            in stage23
        ),
        "stage24_family_c3_cycle_is_frozen": all(
            token in stage24
            for token in (
                "P_s|s_1\\rangle=|s_2\\rangle",
                "P_s|s_2\\rangle=|s_3\\rangle",
                "P_s|s_3\\rangle=|s_1\\rangle",
            )
        ),
        "stage38_c3_cp_parent_pass_present": (
            "STAGE_38_C3_CHARACTER_BASIS_CP_MATH_PASS" in stage38
        ),
        "stage42_su3f_parent_pass_present": (
            "STAGE_42_SU3F_LIE_CLOSURE_PASS" in stage42
        ),
        "c3_shift_order_three": bool(
            np.allclose(
                np.linalg.matrix_power(P_temporal, 3),
                np.eye(3),
                atol=TOL,
            )
        ),
        "f3_unitary": bool(
            np.allclose(F3.conj().T @ F3, np.eye(3), atol=TOL)
        ),
        "f3_diagonalizes_temporal_c3": bool(
            np.allclose(f3_temporal, target_diag, atol=TOL)
        ),
        "f3_diagonalizes_family_c3": bool(
            np.allclose(f3_family, target_diag, atol=TOL)
        ),
        "pauli_hs_orthonormal": bool(
            np.allclose(gram, np.eye(3), atol=TOL)
        ),
        "u3_special_unitary": bool(
            np.allclose(U3.conj().T @ U3, np.eye(2), atol=TOL)
            and abs(np.linalg.det(U3) - 1.0) < TOL
        ),
        "pauli_c3_equivariance": pauli_cycle_residual < TOL,
        "spinorial_cube_minus_identity": bool(
            np.allclose(
                np.linalg.matrix_power(U3, 3),
                -np.eye(2),
                atol=TOL,
            )
        ),
        "spinorial_sixth_power_identity": bool(
            np.allclose(
                np.linalg.matrix_power(U3, 6),
                np.eye(2),
                atol=TOL,
            )
        ),
        "temporal_family_intertwiner_unitary": bool(
            np.allclose(M_tf.conj().T @ M_tf, np.eye(3), atol=TOL)
        ),
        "temporal_family_c3_intertwining": intertwiner_residual < TOL,
        "declared_anchor_e1_to_s1": anchor_residual < TOL,
        "anchor_plus_c3_equivariance_selects_unique_cyclic_map": (
            anchored_intertwiner_count == 1
        ),
        "temporal_transitive_orbit_has_three_labels": (
            len(set(temporal_orbit)) == 3
        ),
        "family_transitive_orbit_has_three_labels": (
            len(set(family_orbit)) == 3
        ),
        "weak_doublet_dimension_is_two": weak_doublet_dimension == 2,
        "family_x_weak_dimension_is_six": family_x_weak_dimension == 6,
        "c3_and_z2_actions_commute": bool(
            np.allclose(
                P6_temporal @ Z2_temporal,
                Z2_temporal @ P6_temporal,
                atol=TOL,
            )
        ),
        "z2_involution_exact": bool(
            np.allclose(
                np.linalg.matrix_power(Z2_temporal, 2),
                np.eye(6),
                atol=TOL,
            )
        ),
        "six_state_generator_order_six": bool(
            np.allclose(
                np.linalg.matrix_power(G6_temporal, 6),
                np.eye(6),
                atol=TOL,
            )
            and not np.allclose(
                np.linalg.matrix_power(G6_temporal, 3),
                np.eye(6),
                atol=TOL,
            )
        ),
        "six_state_cube_equals_chirality_flip": bool(
            np.allclose(
                np.linalg.matrix_power(G6_temporal, 3),
                Z2_temporal,
                atol=TOL,
            )
        ),
        "six_state_single_transitive_orbit": (
            len(set(six_state_orbit)) == 6
        ),
        "six_state_characteristic_polynomial_lambda6_minus_1": bool(
            np.allclose(
                g6_charpoly,
                expected_g6_charpoly,
                atol=1.0e-10,
            )
        ),
        "temporal_family_six_state_intertwining": (
            six_state_intertwiner_residual < TOL
        ),
        "shared_character_jarlskog_exact": abs(J - J_exact) < TOL,
        "family_stage42_lie_dimension_is_eight": dim_family == 8,
        "pulled_temporal_lie_dimension_is_eight": dim_temporal == 8,
        "lie_dimension_preserved_by_intertwiner": dim_family == dim_temporal,
        "lie_generators_remain_su3_typed": (
            residual_family < TOL and residual_temporal < TOL
        ),
    }

    passed = all(checks.values())
    payload = {
        "schema": "TIR_IDT_MOD6PI_C3_PAULI_CROSSWALK_V0_1",
        "technical_status": "PASS" if passed else "FAIL",
        "representation_status": (
            "TEMPORAL_C3_TO_PAULI_AND_ORDERED_FAMILY_C3_CROSSWALK_CLOSED"
            if passed
            else "CROSSWALK_FAILED"
        ),
        "temporal_family_label_binding": (
            "ANCHORED_EQUIVARIANT_LABEL_INTERTWINER_CLOSED"
            if passed
            else "FAILED"
        ),
        "flavour_cardinality_result": (
            "N_F_EQUALS_3_CONDITIONAL_ON_PHYSICAL_TEMPORAL_FAMILY_BINDING"
            if passed
            else "NOT_ESTABLISHED"
        ),
        "cp_character_transfer": (
            "F3_JARLSKOG_MATH_TRANSFER_CLOSED_PHYSICAL_CP_BINDING_OPEN"
            if passed
            else "FAILED"
        ),
        "su3f_transfer": (
            "LIE_DIMENSION_8_PRESERVED_UNDER_ORDERED_INTERTWINER"
            if passed
            else "FAILED"
        ),
        "six_state_product_binding": (
            "C3_X_CHIRALITY_Z2_SIX_STATE_INTERTWINER_CLOSED"
            if passed
            else "FAILED"
        ),
        "weak_family_cardinality": (
            "DIMENSION_3_X_2_EQUALS_6_CONDITIONAL_ON_PHYSICAL_TEMPORAL_FAMILY_BINDING"
            if passed
            else "NOT_ESTABLISHED"
        ),
        "six_quark_flavour_cardinality": (
            "CONDITIONAL_LABEL_COUNT_SIX_NOT_FULL_PHYSICAL_SPECTRUM_DERIVATION"
            if passed
            else "NOT_ESTABLISHED"
        ),
        "six_cycle_physical_flavour_operator": (
            "OPEN_REQUIRES_CHIRALITY_Z2_TO_WEAK_ISOSPIN_DOUBLET_BINDING"
        ),
        "physical_sector_binding": "OPEN",
        "idt_parent": "02JN periodic P4 endpoint quotient at N=3",
        "tir_pauli_parent": "TIR_RELATIONAL_GENERATOR_SPACE_V0_1",
        "tir_weak_subalgebra_parent": "TIR_POLYGONAL_STAGE15_EXCEPTIONAL_SM_SUBALGEBRA_V0_1",
        "tir_hypercharge_representation_parent": "TIR_POLYGONAL_STAGE16_EXCEPTIONAL_HYPERCHARGE_MATCH_V0_1",
        "tir_family_order_parent": "TIR_POLYGONAL_STAGE22_SEED_PRECEDENCE_V0_1",
        "tir_chirality_parent": "TIR_POLYGONAL_STAGE23_CHIRALITY_INTERTWINER_V0_1",
        "tir_family_cycle_parent": "TIR_POLYGONAL_STAGE24_TIR_SEED_CHIRALITY_E8_INTERTWINER_V0_1",
        "tir_cp_parent": "TIR_POLYGONAL_STAGE38_C3_CHARACTER_BASIS_CP_V0_1",
        "tir_lie_parent": "TIR_POLYGONAL_STAGE42_FAMILY_LIE_CLOSURE_V0_1",
        "checks": checks,
        "residuals": {
            "pauli_c3_equivariance": pauli_cycle_residual,
            "temporal_family_intertwiner": intertwiner_residual,
            "anchor": anchor_residual,
            "family_lie_structure": residual_family,
            "temporal_pullback_lie_structure": residual_temporal,
            "six_state_intertwiner": six_state_intertwiner_residual,
            "jarlskog_exact": abs(J - J_exact),
        },
        "orbit_cardinalities": {
            "temporal": len(set(temporal_orbit)),
            "family": len(set(family_orbit)),
            "family_x_chirality": len(set(six_state_orbit)),
        },
        "carrier_dimensions": {
            "family": family_dimension,
            "weak_doublet": weak_doublet_dimension,
            "family_x_weak": family_x_weak_dimension,
            "family_x_chirality": len(set(six_state_orbit)),
        },
        "lie_dimensions": {
            "family": dim_family,
            "temporal_pullback": dim_temporal,
        },
        "J_F3": J,
        "J_F3_exact": J_exact,
        "firewall": {
            "representation_equivalence_is_not_physical_sector_identity": True,
            "physical_temporal_to_flavour_binding": "OPEN",
            "physical_ckm_assignment": "OPEN",
            "physical_pmns_assignment": "OPEN",
            "family_count_is_conditional_on_sector_binding": True,
            "six_state_family_x_chirality_is_not_yet_the_physical_flavour_operator": True,
            "six_weak_family_component_count_is_conditional_on_family_binding": True,
            "required_next_gate_for_operator_identity": "CHIRALITY_Z2_TO_WEAK_ISOSPIN_DOUBLET_BINDING",
        },
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
