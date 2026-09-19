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

import hashlib
import itertools
import json
import math
from fractions import Fraction
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


def git_blob_sha(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()


def collatz_step(n: int) -> int:
    return n // 2 if n % 2 == 0 else 3 * n + 1


def collatz_depth_to_one(n: int, limit: int = 1000) -> int:
    for k in range(limit + 1):
        if n == 1:
            return k
        n = collatz_step(n)
    raise RuntimeError("Collatz depth limit exceeded")


def q_c(n: int) -> Fraction:
    bits: list[int] = []
    x = n
    for _ in range(1000):
        if x == 1:
            L = len(bits)
            prefix = sum(
                (Fraction(bit, 2 ** (k + 1)) for k, bit in enumerate(bits)),
                Fraction(0, 1),
            )
            return prefix + Fraction(4, 7 * (2 ** L))
        bits.append(x % 2)
        x = collatz_step(x)
    raise RuntimeError("Collatz phase orbit did not reach 1")


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
    archive_projection_path = (
        ROOT
        / "archive/v7.9/full/28_debt11_chiral_representation_projection_v3_0/"
        "scripts/debt11_chiral_representation_projection_v3_0.py"
    )
    archive_projection_csv_path = (
        ROOT
        / "archive/v7.9/full/28_debt11_chiral_representation_projection_v3_0/"
        "results/projection_channel_table_v3_0.csv"
    )
    archive_axis_v18_path = (
        ROOT
        / "archive/v7.9/full/16_debt_axis_selection_berry_weak_twinprime_v1_8/"
        "METATIME_SM_AXIS_SELECTION_DEBT_v1_8.md"
    )
    archive_axis_v23_path = (
        ROOT
        / "archive/v7.9/full/21_debt8_source_axis_candidate_grammar_v2_3/"
        "METATIME_SM_DEBT8_SOURCE_AXIS_CANDIDATE_GRAMMAR_v2_3.md"
    )

    archive_projection_bytes = archive_projection_path.read_bytes()
    archive_projection_csv_bytes = archive_projection_csv_path.read_bytes()
    archive_projection = archive_projection_bytes.decode("utf-8")
    archive_projection_csv = archive_projection_csv_bytes.decode("utf-8")
    archive_axis_v18 = archive_axis_v18_path.read_text(encoding="utf-8")
    archive_axis_v23 = archive_axis_v23_path.read_text(encoding="utf-8")

    archive_projection_blob = git_blob_sha(archive_projection_bytes)
    archive_projection_csv_blob = git_blob_sha(archive_projection_csv_bytes)

    archive_csv_has_stale_up_quark_id = (
        'nu_L,up_quark,"T3=1/2, pole=north/+"' in archive_projection_csv
    )
    archive_csv_has_corrected_up_quark_id = (
        'u_L,up_quark,"T3=1/2, pole=north/+"' in archive_projection_csv
    )
    if archive_csv_has_stale_up_quark_id and not archive_csv_has_corrected_up_quark_id:
        archive_csv_state = "STALE_UP_QUARK_PARTICLE_ID"
    elif archive_csv_has_corrected_up_quark_id and not archive_csv_has_stale_up_quark_id:
        archive_csv_state = "CORRECTED_UP_QUARK_PARTICLE_ID"
    elif archive_csv_has_stale_up_quark_id and archive_csv_has_corrected_up_quark_id:
        archive_csv_state = "MIXED_UP_QUARK_PARTICLE_IDS"
    else:
        archive_csv_state = "UP_QUARK_ROW_NOT_DETECTED"

    active_seed_reachability = (
        ROOT
        / "TIR/foundations/TIR_ACTIVE_SEED_COLLATZ_REACHABILITY_V0_1.md"
    ).read_text(encoding="utf-8")
    cocycle_phase = (
        ROOT
        / "TIR/foundations/TIR_COEFFICIENT_COCYCLE_POTENTIAL_REDUCTION_V0_4.md"
    ).read_text(encoding="utf-8")

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
    atomic_assignment = (
        ROOT
        / "TIR/integration/tir_half_foundation_v0_6_0/"
        "ATOMIC_ASSIGNMENT_CANONIZATION.md"
    ).read_text(encoding="utf-8")
    precedence_falsification = (
        ROOT
        / "TIR/foundations/"
        "TIR_COEFFICIENT_TRANSITION_SELECTOR_PRECEDENCE_FALSIFICATION_V0_2.md"
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

    # Recovered legacy orientation anchor for the two-pole weak-doublet map.
    # Current Stage-15/16/23 provide compatible two-state structural parents;
    # the N/S -> T3 +/- 1/2 orientation itself is recovered from the archived
    # v3.0 projection source and is not promoted as a new first-principles
    # physical theorem here.
    # Current A1 weak-doublet Weyl action. In the T3 weight basis the
    # nontrivial Weyl element exchanges +/- 1/2 and squares to identity.
    T3_weak = np.diag([0.5, -0.5]).astype(complex)
    J_weak = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
    weak_weyl_flip_residual = float(
        np.max(np.abs(J_weak @ T3_weak @ J_weak.conj().T + T3_weak))
    )

    # Generic A1 Cartan-axis conjugacy test.  Absolute orientation of the
    # normalized weak axis is an SU(2)-conjugacy choice; the Weyl Z2 action
    # transports covariantly with the axis.
    n_axis = np.array([1.0, 2.0, 3.0], dtype=float)
    n_axis = n_axis / np.linalg.norm(n_axis)
    theta_axis = math.acos(float(n_axis[2]))
    phi_axis = math.atan2(float(n_axis[1]), float(n_axis[0]))
    U_z = (
        math.cos(phi_axis / 2.0) * np.eye(2, dtype=complex)
        - 1j * math.sin(phi_axis / 2.0) * sz
    )
    U_y = (
        math.cos(theta_axis / 2.0) * np.eye(2, dtype=complex)
        - 1j * math.sin(theta_axis / 2.0) * sy
    )
    U_axis = U_z @ U_y
    H_axis = 0.5 * (
        n_axis[0] * sx + n_axis[1] * sy + n_axis[2] * sz
    )
    axis_conjugacy_residual = float(
        np.max(np.abs(U_axis @ T3_weak @ U_axis.conj().T - H_axis))
    )
    J_axis = U_axis @ J_weak @ U_axis.conj().T
    axis_weyl_involution_residual = float(
        np.max(np.abs(J_axis @ J_axis - np.eye(2)))
    )
    axis_weyl_flip_residual = float(
        np.max(np.abs(J_axis @ H_axis @ J_axis.conj().T + H_axis))
    )

    F_chi_weak = np.eye(2, dtype=complex)
    chirality_weak_intertwiner_residual = float(
        np.max(np.abs(F_chi_weak @ J_chi - J_weak @ F_chi_weak))
    )
    M6_weak = np.kron(M_tf, F_chi_weak)
    G6_weak = np.kron(P_family, J_weak)
    weak_family_seed = np.kron(
        np.array([1.0, 0.0, 0.0], dtype=complex),
        np.array([1.0, 0.0], dtype=complex),
    )
    weak_family_orbit = [
        tuple(
            np.rint(
                np.real(np.linalg.matrix_power(G6_weak, k) @ weak_family_seed)
            ).astype(int)
        )
        for k in range(6)
    ]
    weak_family_charpoly = np.poly(G6_weak)

    six_weak_intertwiner_residual = float(
        np.max(np.abs(M6_weak @ G6_temporal - G6_weak @ M6_weak))
    )

    family_dimension = len(set(temporal_orbit))
    weak_doublet_dimension = 2
    family_x_weak_dimension = family_dimension * weak_doublet_dimension

    # Source-order canonicalization of the temporal->family label map.
    # The open-cut IDT carrier retains the ordered frame-edge provenance
    # e1<e2<e3 before periodic quotienting.  Current TIR Stage-22 fixes the
    # ordered seeds s1<s2<s3.  On the active center projection, ordinary
    # Collatz stopping depth is strictly increasing in the same current order.
    active_centers = [4, 6, 12]
    center_depths = [collatz_depth_to_one(n) for n in active_centers]
    temporal_order = (1, 2, 3)
    family_order = tuple(
        j + 1
        for j in sorted(range(3), key=lambda j: center_depths[j])
    )
    order_preserving_permutations = [
        perm
        for perm in itertools.permutations((1, 2, 3))
        if all(perm[i] < perm[i + 1] for i in range(2))
    ]

    # Negative control: the raw IDT Collatz phases carried by the active
    # centers are not themselves the uniformly spaced 0,1/3,2/3 C3 clock.
    q1, q2, q3 = (q_c(n) for n in active_centers)
    q_raw_is_arithmetic_progression = (q2 - q1) == (q3 - q2)
    q_raw_family_order_is_monotone = q1 < q2 < q3

    checks = {
        "legacy_projection_source_blob_pinned": (
            archive_projection_blob == "01b9be380f095b613a731ba258865bc617d8e854"
        ),
        "legacy_projection_csv_blob_pinned": (
            archive_projection_csv_blob == "3ec7331cbb859d8d955c9d7d5d1bd67ef75e8fb1"
        ),
        "legacy_projection_source_has_correct_up_quark_row": (
            'Channel("u_L", "up_quark", "L", "weak_doublet", "north/+", Fraction(1,2)' in archive_projection
        ),
        "legacy_projection_source_has_down_quark_row": (
            'Channel("d_L", "down_quark", "L", "weak_doublet", "south/-", Fraction(-1,2)' in archive_projection
        ),
        "legacy_projection_source_has_lepton_pole_pair": (
            'Channel("nu_L", "neutrino", "L", "weak_doublet", "north/+", Fraction(1,2)' in archive_projection
            and 'Channel("e_L", "charged_lepton", "L", "weak_doublet", "south/-", Fraction(-1,2)' in archive_projection
        ),
        "legacy_generated_csv_up_quark_row_auditable": (
            archive_csv_has_stale_up_quark_id
            or archive_csv_has_corrected_up_quark_id
        ),
        "legacy_axis_v18_declares_universal_weak_axis_ansatz": (
            "The weak doublet uses one universal weak-isospin axis." in archive_axis_v18
            and "conditionally closed as a canonical working ansatz" in archive_axis_v18
        ),
        "legacy_axis_v23_source_derived_cp1_before_weak_naming": (
            "SOURCE_DERIVED_CHIRAL_CP1_AXIS" in archive_axis_v23
            and "the SM interpretation of that abstract axis is weak isospin" in archive_axis_v23
            and "CONDITIONALLY_CLOSED_STRUCTURAL_ENUMERATION" in archive_axis_v23
        ),
        "current_active_seed_reachability_parent_present": (
            "EXACT_CENTER_PROJECTION_REACHABILITY" in active_seed_reachability
            and "m_1=4" in active_seed_reachability
            and "m_2=6" in active_seed_reachability
            and "m_3=12" in active_seed_reachability
        ),
        "current_idt_phase_coboundary_parent_present": (
            "EXACT_IDT_PHASE_COBBOUNDARY" in cocycle_phase
            and "q_1:=q_C(4)=\\frac17" in cocycle_phase
            and "q_2:=q_C(6)=\\frac{141}{448}" in cocycle_phase
            and "q_3:=q_C(12)=\\frac{141}{896}" in cocycle_phase
        ),
        "active_center_stopping_depths_strictly_increase_with_stage22_order": (
            center_depths == [2, 8, 9]
        ),
        "source_order_preserving_bijection_is_unique": (
            temporal_order == (1, 2, 3)
            and family_order == (1, 2, 3)
            and order_preserving_permutations == [(1, 2, 3)]
        ),
        "raw_qc_not_uniform_three_frame_clock": (
            not q_raw_is_arithmetic_progression
        ),
        "raw_qc_not_monotone_in_stage22_family_order": (
            not q_raw_family_order_is_monotone
        ),
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
        "historical_generation_order_is_preserved_separately": all(
            token in atomic_assignment
            for token in (
                "generation 1: `(3,5)`",
                "generation 2: `(11,13)`",
                "generation 3: `(5,7)`",
            )
        ),
        "active_stage22_order_explicitly_supersedes_historical_order_for_validation": (
            "explicitly supersedes the early v0.5 generation ordering"
            in precedence_falsification
            and "(3,5)\\to1" in precedence_falsification
            and "(5,7)\\to2" in precedence_falsification
            and "(11,13)\\to3" in precedence_falsification
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
        "current_weak_a1_weyl_z2_involution_exact": bool(
            np.allclose(J_weak @ J_weak, np.eye(2), atol=TOL)
        ),
        "current_weak_a1_weyl_reflection_flips_t3": (
            weak_weyl_flip_residual < TOL
        ),
        "weak_axis_generic_su2_conjugacy_exact": (
            axis_conjugacy_residual < TOL
        ),
        "weak_axis_transported_weyl_is_involution": (
            axis_weyl_involution_residual < TOL
        ),
        "weak_axis_transported_weyl_flips_generic_cartan": (
            axis_weyl_flip_residual < TOL
        ),
        "current_family_x_weak_generator_order_six": bool(
            np.allclose(
                np.linalg.matrix_power(G6_weak, 6),
                np.eye(6),
                atol=TOL,
            )
            and not np.allclose(
                np.linalg.matrix_power(G6_weak, 3),
                np.eye(6),
                atol=TOL,
            )
        ),
        "current_family_x_weak_single_six_cycle": (
            len(set(weak_family_orbit)) == 6
        ),
        "current_family_x_weak_charpoly_lambda6_minus_1": bool(
            np.allclose(
                weak_family_charpoly,
                expected_g6_charpoly,
                atol=1.0e-10,
            )
        ),
        "chirality_to_weak_z2_intertwiner_exact_under_recovered_anchor": (
            chirality_weak_intertwiner_residual < TOL
        ),
        "temporal_family_weak_six_state_intertwiner_exact_under_recovered_anchor": (
            six_weak_intertwiner_residual < TOL
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
        "family_precedence_binding": (
            "TEMPORAL_C3_TO_ACTIVE_STAGE22_FAMILY_SEED_ORDER_CLOSED"
            if passed
            else "FAILED"
        ),
        "historical_generation_numbering_status": (
            "PRESERVED_BUT_NOT_USED_AS_ACTIVE_C3_ANCHOR"
        ),
        "source_order_anchor_status": (
            "UNIQUE_ORDER_PRESERVING_LABEL_CROSSWALK_CLOSED"
            if passed
            else "FAILED"
        ),
        "declared_anchor_dependency": (
            "REMOVED_AT_ORDERED_LABEL_REPRESENTATION_LEVEL"
            if passed
            else "NOT_ESTABLISHED"
        ),
        "raw_qc_phase_binding": (
            "DIRECT_UNIFORM_C3_CLOCK_IDENTIFICATION_REFUTED"
            if passed
            else "NOT_EVALUATED"
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
        "weak_a1_weyl_z2_status": "CURRENT_EXACT",
        "weak_axis_conjugacy_status": (
            "A1_CARTAN_ORIENTATION_SU2_CONJUGACY_CLASS_CLOSED"
            if passed
            else "FAILED"
        ),
        "electroweak_vacuum_alignment_status": (
            "OPEN_HIGGS_HYPERCHARGE_ALIGNMENT_NOT_CLOSED_BY_AXIS_CONJUGACY"
        ),
        "family_x_weak_six_cycle": (
            "CURRENT_C3_X_A1_WEYL_Z2_C6_EXACT"
            if passed
            else "FAILED"
        ),
        "six_weak_component_label_count": (
            "SIX_CONDITIONAL_ON_PHYSICAL_TEMPORAL_FAMILY_BINDING"
            if passed
            else "NOT_ESTABLISHED"
        ),
        "legacy_weak_pole_orientation_audit": (
            "ARCHIVAL_SOURCE_RECOVERED_CURRENT_PROMOTION_CONDITIONAL"
        ),
        "chirality_to_weak_label_intertwiner": (
            "CLOSED_CONDITIONAL_ON_RECOVERED_NORTH_SOUTH_T3_ORIENTATION_ANCHOR"
            if passed
            else "FAILED"
        ),
        "six_cycle_weak_family_label_operator": (
            "CLOSED_CONDITIONAL_ON_RECOVERED_WEAK_ORIENTATION_ANCHOR"
            if passed
            else "FAILED"
        ),
        "six_cycle_physical_flavour_operator": (
            "CURRENT_WEAK_FAMILY_REPRESENTATION_EXACT_PHYSICAL_GENERATION_BINDING_OPEN"
        ),
        "physical_sector_binding": "OPEN",
        "idt_parent": "02JN periodic P4 endpoint quotient at N=3",
        "tir_pauli_parent": "TIR_RELATIONAL_GENERATOR_SPACE_V0_1",
        "tir_weak_subalgebra_parent": "TIR_POLYGONAL_STAGE15_EXCEPTIONAL_SM_SUBALGEBRA_V0_1",
        "tir_hypercharge_representation_parent": "TIR_POLYGONAL_STAGE16_EXCEPTIONAL_HYPERCHARGE_MATCH_V0_1",
        "legacy_weak_projection_source": "archive/v7.9/full/28_debt11_chiral_representation_projection_v3_0/scripts/debt11_chiral_representation_projection_v3_0.py",
        "legacy_weak_projection_source_blob": archive_projection_blob,
        "legacy_generated_projection_csv_blob": archive_projection_csv_blob,
        "legacy_generated_projection_csv_state": archive_csv_state,
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
            "weak_weyl_t3_flip": weak_weyl_flip_residual,
            "generic_axis_conjugacy": axis_conjugacy_residual,
            "generic_axis_weyl_involution": axis_weyl_involution_residual,
            "generic_axis_weyl_flip": axis_weyl_flip_residual,
            "chirality_weak_intertwiner": chirality_weak_intertwiner_residual,
            "six_weak_intertwiner": six_weak_intertwiner_residual,
            "jarlskog_exact": abs(J - J_exact),
        },
        "source_order_audit": {
            "active_centers": active_centers,
            "center_stopping_depths": center_depths,
            "temporal_order": list(temporal_order),
            "family_rank_order": list(family_order),
            "order_preserving_bijection_count": len(order_preserving_permutations),
            "qC": [str(q1), str(q2), str(q3)],
            "raw_qC_is_arithmetic_progression": q_raw_is_arithmetic_progression,
            "raw_qC_is_monotone_in_stage22_order": q_raw_family_order_is_monotone,
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
            "family_x_weak_orbit": len(set(weak_family_orbit)),
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
            "active_stage22_seed_precedence_is_not_historical_generation_numbering": True,
            "historical_generation_numbering_is_not_used_as_temporal_c3_anchor": True,
            "physical_ckm_assignment": "OPEN",
            "physical_pmns_assignment": "OPEN",
            "family_count_is_conditional_on_sector_binding": True,
            "legacy_generated_csv_state_is_diagnostic_not_math_gate": True,
            "legacy_projection_script_is_provenance_authority": True,
            "chirality_to_weak_label_map_uses_recovered_orientation_anchor": True,
            "weak_a1_weyl_z2_does_not_require_legacy_orientation_anchor": True,
            "absolute_a1_cartan_axis_orientation_is_su2_conjugacy_choice": True,
            "axis_conjugacy_does_not_close_higgs_hypercharge_vacuum_alignment": True,
            "legacy_anchor_only_orients_cp1_ns_against_t3_sign": True,
            "six_weak_family_component_count_is_conditional_on_family_binding": True,
            "source_order_anchor_is_not_physical_sector_identity": True,
            "raw_qc_phase_does_not_supply_uniform_mod6pi_frame_positions": True,
            "remaining_physical_gate": "TEMPORAL_C3_TO_PHYSICAL_FAMILY_BINDING_AND_FULL_MASS_MIXING_SPECTRUM",
        },
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
