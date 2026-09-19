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

import csv
import hashlib
import io
import itertools
import json
import math
import subprocess
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


def git_head_blob(path: Path) -> tuple[str, bytes]:
    rel = path.resolve().relative_to(ROOT.resolve()).as_posix()
    listing = subprocess.run(
        ["git", "-C", str(ROOT), "ls-tree", "HEAD", "--", rel],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    if not listing:
        raise RuntimeError(f"HEAD does not contain required provenance path: {rel}")
    meta, listed_path = listing.split("\t", 1)
    mode, obj_type, blob_sha = meta.split()
    if listed_path != rel or obj_type != "blob":
        raise RuntimeError(
            f"Unexpected HEAD tree entry for {rel}: {mode} {obj_type} {blob_sha} {listed_path}"
        )
    data = subprocess.run(
        ["git", "-C", str(ROOT), "cat-file", "blob", blob_sha],
        check=True,
        capture_output=True,
    ).stdout
    if git_blob_sha(data) != blob_sha:
        raise RuntimeError(f"Git object self-hash mismatch for {rel}")
    return blob_sha, data


def json_default(value):
    if isinstance(value, np.generic):
        return value.item()
    raise TypeError(
        f"Unsupported JSON payload type: {type(value).__module__}.{type(value).__qualname__}"
    )


def collatz_step(n: int) -> int:
    return n // 2 if n % 2 == 0 else 3 * n + 1


def collatz_depth_to_one(n: int, limit: int = 1000) -> int:
    for k in range(limit + 1):
        if n == 1:
            return k
        n = collatz_step(n)
    raise RuntimeError("Collatz depth limit exceeded")


def collatz_first_hit(start: int, target: int, limit: int = 10000) -> int | None:
    x = start
    seen: set[int] = set()
    for k in range(limit + 1):
        if x == target:
            return k
        if x in seen:
            return None
        seen.add(x)
        x = collatz_step(x)
    raise RuntimeError("Collatz first-hit limit exceeded")


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

    # Provenance is read from the immutable HEAD git object, not inferred only
    # from the checked-out working-tree representation.
    archive_projection_csv_tree_blob, archive_projection_csv_object_bytes = (
        git_head_blob(archive_projection_csv_path)
    )
    archive_projection_csv_worktree_matches_object = (
        archive_projection_csv_bytes == archive_projection_csv_object_bytes
    )
    archive_projection_csv_object = archive_projection_csv_object_bytes.decode("utf-8")
    archive_csv_rows = list(csv.reader(io.StringIO(archive_projection_csv_object)))
    archive_csv_data_rows = archive_csv_rows[1:]
    archive_csv_up_quark_particle_ids = [
        row[0]
        for row in archive_csv_data_rows
        if len(row) >= 2 and row[1] == "up_quark"
    ]
    archive_csv_has_stale_up_quark_id = "nu_L" in archive_csv_up_quark_particle_ids
    archive_csv_has_corrected_up_quark_id = "u_L" in archive_csv_up_quark_particle_ids
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
    stage21 = (
        ROOT
        / "TIR/frozen_predictions/validation/"
        "TIR_POLYGONAL_EXCITATION_STAGE21_E8_THREEFOLD_SM_CARRIER_V0_1.md"
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
    stage25 = (
        ROOT
        / "TIR/frozen_predictions/validation/"
        "TIR_POLYGONAL_EXCITATION_STAGE25_COLOR_FAMILY_FACTORISATION_V0_1.md"
    ).read_text(encoding="utf-8")
    stage30 = (
        ROOT
        / "TIR/frozen_predictions/validation/"
        "TIR_POLYGONAL_EXCITATION_STAGE30_PRECKM_CROSS_GRAM_AUDIT_V0_1.md"
    ).read_text(encoding="utf-8")
    flavour_normalization = (
        ROOT
        / "TIR/foundations/TIR_KAPPA_FLAVOUR_MIXING_NORMALIZATION_V0_1.md"
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
    stage43 = (
        ROOT
        / "TIR/frozen_predictions/validation/"
        "TIR_POLYGONAL_EXCITATION_STAGE43_FAMILY_ORDERING_PROVENANCE_V0_1.md"
    ).read_text(encoding="utf-8")
    legacy_collatz_phase_sim = (
        ROOT
        / "archive/v7.9/full/01_foundational_formal_notes/"
        "phase_hamiltonian_english_derivations/scripts/collatz_phase_sim.py"
    ).read_text(encoding="utf-8")
    stage44 = (
        ROOT
        / "TIR/frozen_predictions/validation/"
        "TIR_POLYGONAL_EXCITATION_STAGE44_COLLATZ_PRODUCT_SEED_INTERSECTION_V0_1.md"
    ).read_text(encoding="utf-8")
    stage45 = (
        ROOT
        / "TIR/frozen_predictions/validation/"
        "TIR_POLYGONAL_EXCITATION_STAGE45_DISTANCE_AMPLITUDE_PROVENANCE_V0_1.md"
    ).read_text(encoding="utf-8")
    stage48 = (
        ROOT
        / "TIR/frozen_predictions/validation/"
        "TIR_POLYGONAL_EXCITATION_STAGE48_COLLATZ_BRANCH_WORD_OPERATOR_INTERFACE_V0_1.md"
    ).read_text(encoding="utf-8")
    stage49 = (
        ROOT
        / "TIR/frozen_predictions/validation/"
        "TIR_POLYGONAL_EXCITATION_STAGE49_COLLATZ_MOBIUS_POINCARE_LIFT_V0_1.md"
    ).read_text(encoding="utf-8")
    stage50 = (
        ROOT
        / "TIR/frozen_predictions/validation/"
        "TIR_POLYGONAL_EXCITATION_STAGE50_SYM2_POLYNOMIAL_THREE_CARRIER_V0_1.md"
    ).read_text(encoding="utf-8")
    stage51 = (
        ROOT
        / "TIR/frozen_predictions/validation/"
        "TIR_POLYGONAL_EXCITATION_STAGE51_SYM2_UNITARIZATION_NO_GO_V0_1.md"
    ).read_text(encoding="utf-8")
    stage52 = (
        ROOT
        / "TIR/frozen_predictions/validation/"
        "TIR_POLYGONAL_EXCITATION_STAGE52_COMPACT_REAL_FORM_SYM2_SU2_SU3_BRIDGE_V0_1.md"
    ).read_text(encoding="utf-8")
    stage53 = (
        ROOT
        / "TIR/frozen_predictions/validation/"
        "TIR_POLYGONAL_EXCITATION_STAGE53_SPIN1_SUBGROUP_CP_NOGO_3PLUS5_V0_1.md"
    ).read_text(encoding="utf-8")
    stage55 = (
        ROOT
        / "TIR/frozen_predictions/validation/"
        "TIR_POLYGONAL_EXCITATION_STAGE55_SU3_SO3_SYMMETRIC_PAIR_V0_1.md"
    ).read_text(encoding="utf-8")
    stage56 = (
        ROOT
        / "TIR/frozen_predictions/validation/"
        "TIR_POLYGONAL_EXCITATION_STAGE56_PLATONIC_SPIN2_RESTRICTION_V0_1.md"
    ).read_text(encoding="utf-8")
    stage57 = (
        ROOT
        / "TIR/frozen_predictions/validation/"
        "TIR_POLYGONAL_EXCITATION_STAGE57_PLATONIC_TRIPLET_TENSOR_SQUARE_V0_1.md"
    ).read_text(encoding="utf-8")
    stage58 = (
        ROOT
        / "TIR/frozen_predictions/validation/"
        "TIR_POLYGONAL_EXCITATION_STAGE58_ICOSAHEDRAL_QUADRUPOLE_SU3_GENERATION_V0_1.md"
    ).read_text(encoding="utf-8")
    stage64 = (
        ROOT
        / "TIR/frozen_predictions/validation/"
        "TIR_POLYGONAL_EXCITATION_STAGE64_SELECTOR_PROVENANCE_GATE_V0_1.md"
    ).read_text(encoding="utf-8")
    stage65 = (
        ROOT
        / "TIR/frozen_predictions/"
        "TIR_POLYGONAL_STAGE65_STATIONARY_ORDERED_AXIS_CUBIC_SELECTOR_FREEZE_V0_1.md"
    ).read_text(encoding="utf-8")
    stage66 = (
        ROOT
        / "TIR/frozen_predictions/validation/"
        "TIR_POLYGONAL_EXCITATION_STAGE66_STATIONARY_SELECTOR_DERIVATION_V0_1.md"
    ).read_text(encoding="utf-8")
    stage61 = (
        ROOT
        / "TIR/frozen_predictions/validation/"
        "TIR_POLYGONAL_EXCITATION_STAGE61_C3_ICOSAHEDRAL_FAMILY_INTERTWINER_V0_1.md"
    ).read_text(encoding="utf-8")
    stage62 = (
        ROOT
        / "TIR/frozen_predictions/validation/"
        "TIR_POLYGONAL_EXCITATION_STAGE62_FAMILY_ICOSAHEDRAL_EMBEDDING_RIGIDITY_V0_1.md"
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

    # Raw product-seed Collatz dynamics: exact directed reachability among
    # n=(15,35,143).  This is a negative control for deriving the Stage-24 C3
    # cycle directly from ordinary Collatz dynamics.
    product_seeds = [15, 35, 143]
    product_reachability = np.array(
        [
            [
                0 if i == j else (
                    -1
                    if collatz_first_hit(a, b) is None
                    else collatz_first_hit(a, b)
                )
                for j, b in enumerate(product_seeds)
            ]
            for i, a in enumerate(product_seeds)
        ],
        dtype=int,
    )
    product_directed_cycle_exists = (
        product_reachability[0, 1] > 0
        and product_reachability[1, 2] > 0
        and product_reachability[2, 0] > 0
    ) or (
        product_reachability[0, 2] > 0
        and product_reachability[2, 1] > 0
        and product_reachability[1, 0] > 0
    )

    # The oriented temporal generator distinguishes the two nontrivial
    # orientation-preserving order-3 permutation generators P3 and P3^{-1}.
    P_forward = P_temporal
    P_reverse = np.linalg.matrix_power(P_temporal, 2)
    temporal_forward_edge = tuple(
        np.rint(np.real(P_forward @ e1)).astype(int)
    )
    temporal_reverse_edge = tuple(
        np.rint(np.real(P_reverse @ e1)).astype(int)
    )
    e2_tuple = (0, 1, 0)
    e3_tuple = (0, 0, 1)
    oriented_generator_residual = float(
        np.max(np.abs(M_tf @ P_forward - P_family @ M_tf))
    )
    inverse_generator_separation = float(
        np.max(np.abs(P_forward - P_reverse))
    )

    # Canonical 2->3 Sym^2 carrier audit from Stage 49/50.
    ME = np.array(
        [[1.0 / math.sqrt(2.0), 0.0], [0.0, math.sqrt(2.0)]],
        dtype=float,
    )
    MO = np.array(
        [[math.sqrt(3.0), 1.0 / math.sqrt(3.0)], [0.0, 1.0 / math.sqrt(3.0)]],
        dtype=float,
    )

    def sym2(M: np.ndarray) -> np.ndarray:
        a, b = M[0, 0], M[0, 1]
        cc, d = M[1, 0], M[1, 1]
        return np.array(
            [
                [a * a, 2.0 * a * b, b * b],
                [a * cc, a * d + b * cc, b * d],
                [cc * cc, 2.0 * cc * d, d * d],
            ],
            dtype=float,
        )

    RE = sym2(ME)
    RO = sym2(MO)
    sym2_homomorphism_residual = max(
        float(np.max(np.abs(sym2(ME @ MO) - RE @ RO))),
        float(np.max(np.abs(sym2(MO @ ME) - RO @ RE))),
    )
    split_branch_noncommutativity = float(np.max(np.abs(RE @ RO - RO @ RE)))

    # Canonical hyperbolic translation-length / log-Jacobian alphabet for
    # the exact Stage-49 PSL(2,R) branch generators, in the standard
    # curvature -1 Poincare normalization.
    ell_E = 2.0 * math.acosh(abs(float(np.trace(ME))) / 2.0)
    ell_O = 2.0 * math.acosh(abs(float(np.trace(MO))) / 2.0)
    ell_E_exact = math.log(2.0)
    ell_O_exact = math.log(3.0)
    ell_E_residual = abs(ell_E - ell_E_exact)
    ell_O_residual = abs(ell_O - ell_O_exact)

    signed_log_jacobian_E = math.log(0.5)
    signed_log_jacobian_O = math.log(3.0)
    signed_scale_residual = max(
        abs(signed_log_jacobian_E + ell_E_exact),
        abs(signed_log_jacobian_O - ell_O_exact),
    )

    kappa_canonical = math.log(2.0) / (24.0 * math.pi)
    kappa_length_residual = abs(
        kappa_canonical - ell_E_exact / (24.0 * math.pi)
    )

    # Exact abelianized slope cocycle checks for the frozen branch words.
    w1_signed_scale = (
        2.0 * signed_log_jacobian_O
        + 2.0 * signed_log_jacobian_E
    )
    w1_slope_residual = abs(w1_signed_scale - math.log(9.0 / 4.0))
    w3_signed_scale = (
        34.0 * signed_log_jacobian_O
        + 56.0 * signed_log_jacobian_E
    )
    w3_slope_residual = abs(
        w3_signed_scale
        - math.log((3.0 ** 34) / (2.0 ** 56))
    )

    # Canonical 2x2 positive-determinant polar compact factor.
    def polar_so2(M: np.ndarray) -> np.ndarray:
        a, b = float(M[0, 0]), float(M[0, 1])
        cc, d = float(M[1, 0]), float(M[1, 1])
        norm = math.hypot(a + d, cc - b)
        return np.array(
            [[a + d, b - cc], [cc - b, a + d]],
            dtype=float,
        ) / norm

    QE = polar_so2(ME)
    QO = polar_so2(MO)
    QO_exact = np.array([[4.0, 1.0], [-1.0, 4.0]]) / math.sqrt(17.0)
    polar_QE_identity_residual = float(np.max(np.abs(QE - np.eye(2))))
    polar_QO_exact_residual = float(np.max(np.abs(QO - QO_exact)))
    polar_QO_orthogonality_residual = float(
        np.max(np.abs(QO.T @ QO - np.eye(2)))
    )

    # Generator-wise compact-factor assignment loses E positions because QE=I.
    generator_polar_EO = QE @ QO
    generator_polar_OE = QO @ QE
    generator_polar_order_separation = float(
        np.max(np.abs(generator_polar_EO - generator_polar_OE))
    )

    # Word-wise polar factor retains order but is not a monoid homomorphism.
    Q_EO_word = polar_so2(ME @ MO)
    Q_OE_word = polar_so2(MO @ ME)
    word_polar_order_separation = float(
        np.max(np.abs(Q_EO_word - Q_OE_word))
    )
    word_polar_homomorphism_residual = max(
        float(np.max(np.abs(Q_EO_word - QE @ QO))),
        float(np.max(np.abs(Q_OE_word - QO @ QE))),
    )

    J_split = np.array(
        [[0.0, 0.0, 0.5], [0.0, -1.0, 0.0], [0.5, 0.0, 0.0]],
        dtype=float,
    )
    split_invariant_residual = max(
        float(np.max(np.abs(RE.T @ J_split @ RE - J_split))),
        float(np.max(np.abs(RO.T @ J_split @ RO - J_split))),
    )
    sym2_dimension = 2 * (2 + 1) // 2
    re_eigen_moduli = sorted(abs(x) for x in np.linalg.eigvals(RE))

    # Independent Stage-65/66 stationary cubic-selector reproduction.
    phi = (1.0 + math.sqrt(5.0)) / 2.0
    ico_vertices: list[np.ndarray] = []
    for s1 in (-1.0, 1.0):
        for s2 in (-1.0, 1.0):
            ico_vertices.extend(
                [
                    np.array([0.0, s1, s2 * phi]),
                    np.array([s1, s2 * phi, 0.0]),
                    np.array([s2 * phi, 0.0, s1]),
                ]
            )
    ico_norm = float(np.linalg.norm(ico_vertices[0]))
    ico_axes: list[np.ndarray] = []
    for v in ico_vertices:
        u = v / ico_norm
        for value in u:
            if abs(value) > TOL:
                if value < 0:
                    u = -u
                break
        if not any(np.max(np.abs(u - a)) < TOL for a in ico_axes):
            ico_axes.append(u)
    ico_quadrupoles = [np.outer(u, u) - np.eye(3) / 3.0 for u in ico_axes]

    def proj0_real(M: np.ndarray) -> np.ndarray:
        return 0.5 * (M + M.T) - np.trace(M) / 3.0 * np.eye(3)

    def grad_iso(S: np.ndarray) -> np.ndarray:
        return 3.0 * proj0_real(S @ S)

    def grad_a5(S: np.ndarray) -> np.ndarray:
        return 3.0 * sum(
            (np.trace(S @ Q) ** 2) * Q for Q in ico_quadrupoles
        )

    def hess_iso_action(S: np.ndarray, X: np.ndarray) -> np.ndarray:
        return 3.0 * proj0_real(S @ X + X @ S)

    def hess_a5_action(S: np.ndarray, X: np.ndarray) -> np.ndarray:
        return 6.0 * sum(
            np.trace(S @ Q) * np.trace(X @ Q) * Q
            for Q in ico_quadrupoles
        )

    D_selector = np.diag([-1.0 / 3.0, 0.0, 1.0 / math.sqrt(5.0)])
    D0_selector = D_selector - np.trace(D_selector) / 3.0 * np.eye(3)
    g0_selector = grad_iso(D0_selector)
    g1_selector = grad_a5(D0_selector)
    selector_linear = np.column_stack(
        [np.diag(g1_selector), -np.diag(D0_selector)]
    )
    selector_rhs = -np.diag(g0_selector)
    eta_selector, lambda_selector = np.linalg.lstsq(
        selector_linear, selector_rhs, rcond=None
    )[0]
    eta_selector_exact = -75.0 * (59.0 + 21.0 * math.sqrt(5.0)) / 638.0
    lambda_selector_exact = -(8765.0 + 4758.0 * math.sqrt(5.0)) / 4785.0
    eta_selector_residual = abs(float(eta_selector) - eta_selector_exact)
    lambda_selector_residual = abs(float(lambda_selector) - lambda_selector_exact)
    selector_stationarity_residual = float(
        np.max(
            np.abs(
                g0_selector
                + eta_selector * g1_selector
                - lambda_selector * D0_selector
            )
        )
    )

    selector_basis: list[np.ndarray] = [
        np.diag([1.0, -1.0, 0.0]) / math.sqrt(2.0),
        np.diag([1.0, 1.0, -2.0]) / math.sqrt(6.0),
    ]
    for i, j in ((0, 1), (0, 2), (1, 2)):
        M = np.zeros((3, 3))
        M[i, j] = M[j, i] = 1.0 / math.sqrt(2.0)
        selector_basis.append(M)

    selector_H = np.zeros((5, 5), dtype=float)
    for i, X in enumerate(selector_basis):
        Y = (
            hess_iso_action(D0_selector, X)
            + eta_selector * hess_a5_action(D0_selector, X)
        )
        for j, B in enumerate(selector_basis):
            selector_H[j, i] = np.trace(B @ Y)

    selector_d = np.array(
        [np.trace(B @ D0_selector) for B in selector_basis], dtype=float
    )
    selector_d /= np.linalg.norm(selector_d)
    _, _, selector_vh = np.linalg.svd(selector_d.reshape(1, -1))
    selector_tangent = selector_vh[1:].T
    selector_constrained = selector_tangent.T @ (
        selector_H - lambda_selector * np.eye(5)
    ) @ selector_tangent
    selector_constrained = 0.5 * (
        selector_constrained + selector_constrained.T
    )
    selector_eigenvalues, selector_eigenvectors_tangent = np.linalg.eigh(
        selector_constrained
    )
    selector_eigenvectors_full = (
        selector_tangent @ selector_eigenvectors_tangent
    )

    selector_Aseed = np.zeros((3, 3))
    selector_Aseed[0, 1] = selector_Aseed[1, 0] = 0.5
    selector_orbit = [selector_Aseed]
    for _ in range(2):
        selector_orbit.append(
            np.real(P_family) @ selector_orbit[-1] @ np.real(P_family).T
        )
    selector_orbit_vectors = []
    for A in selector_orbit:
        v = np.array([np.trace(B @ A) for B in selector_basis], dtype=float)
        selector_orbit_vectors.append(v / np.linalg.norm(v))
    selector_orbit_vectors = np.stack(selector_orbit_vectors, axis=0)
    selector_alignment = np.abs(
        selector_orbit_vectors @ selector_eigenvectors_full
    )
    selector_negative_indices = np.where(selector_eigenvalues < -1.0e-9)[0]
    selector_positive_indices = np.where(selector_eigenvalues > 1.0e-9)[0]
    selector_zero_indices = np.where(np.abs(selector_eigenvalues) <= 1.0e-9)[0]
    selector_neg_index = (
        int(selector_negative_indices[0])
        if len(selector_negative_indices) == 1
        else -1
    )
    selector_negative_best_orbit_index = (
        int(np.argmax(selector_alignment[:, selector_neg_index]))
        if selector_neg_index >= 0
        else -1
    )
    selector_negative_best_alignment = (
        float(np.max(selector_alignment[:, selector_neg_index]))
        if selector_neg_index >= 0
        else 0.0
    )

    checks = {
        "legacy_projection_source_blob_pinned": (
            archive_projection_blob == "01b9be380f095b613a731ba258865bc617d8e854"
        ),
        "legacy_projection_csv_blob_pinned": (
            archive_projection_csv_blob == "3ec7331cbb859d8d955c9d7d5d1bd67ef75e8fb1"
        ),
        "legacy_projection_csv_head_tree_blob_pinned": (
            archive_projection_csv_tree_blob == "3ec7331cbb859d8d955c9d7d5d1bd67ef75e8fb1"
        ),
        "legacy_projection_csv_worktree_matches_head_object": (
            archive_projection_csv_worktree_matches_object
            and archive_projection_csv_blob == archive_projection_csv_tree_blob
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
        "legacy_generated_csv_pinned_blob_has_corrected_up_quark_ids": (
            archive_projection_csv_blob == "3ec7331cbb859d8d955c9d7d5d1bd67ef75e8fb1"
            and archive_projection_csv_tree_blob
            == "3ec7331cbb859d8d955c9d7d5d1bd67ef75e8fb1"
            and archive_projection_csv_worktree_matches_object
            and archive_csv_up_quark_particle_ids == ["u_L", "u_R"]
            and archive_csv_has_corrected_up_quark_id
            and not archive_csv_has_stale_up_quark_id
            and archive_csv_state == "CORRECTED_UP_QUARK_PARTICLE_ID"
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
        "stage21_e8_threefold_family_multiplicity_pass_present": (
            "STAGE_21_THREEFOLD_HYPERCHARGE_CARRIER_PASS" in stage21
            and "16\\cdot3=48" in stage21
            and "multiplicity factor of three" in stage21
        ),
        "stage21_declares_seed_triplet_bijection_as_next_gate": (
            "bijection between the three SU(3) triplet weights"
            in stage21
            and "three previously frozen TIR structural generation channels/seeds"
            in stage21
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
            and "s_1=(3,5)" in precedence_falsification
            and "s_2=(5,7)" in precedence_falsification
            and "s_3=(11,13)" in precedence_falsification
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
        "stage24_seed_to_exceptional_triplet_intertwiner_pass_present": (
            "STAGE_24_SIX_STATE_LABEL_INTERTWINER_PASS" in stage24
            and "M_sP_s=P_3M_s" in stage24
        ),
        "stage25_color_family_factorisation_pass_present": (
            "STAGE_25_COLOR_FAMILY_FACTORISATION_PASS" in stage25
            and "SU(3)_F" in stage25
            and "two independent commuting SU(3) factors" in stage25
        ),
        "current_family_carrier_is_complex_three_and_special_unitary": (
            "V_F\\cong\\mathbb C^3" in flavour_normalization
            and "U_F\\in SU(3)_F" in flavour_normalization
            and "EXACT_TIR_INTERNAL_FLAVOUR_MIXING_NORMALIZATION_DERIVATION"
            in flavour_normalization
        ),
        "stage25_family_action_is_explicit_su3f_endpoint": (
            "U_F\\in SU(3)_F" in stage25
            and "I_3\\otimes I_2\\otimes U_F" in stage25
        ),
        "stage30_canonical_polar_diagnostic_parent_present": (
            "STAGE_30_SECTOR_MISALIGNMENT_PASS__DIRECT_MIXING_PROMOTION_OPEN"
            in stage30
            and "Canonical polar factor" in stage30
            and "requires an independently derived TIR rule" in stage30
        ),
        "stage38_c3_cp_parent_pass_present": (
            "STAGE_38_C3_CHARACTER_BASIS_CP_MATH_PASS" in stage38
        ),
        "stage42_su3f_parent_pass_present": (
            "STAGE_42_SU3F_LIE_CLOSURE_PASS" in stage42
        ),
        "stage43_ordering_principle_parent_pass_present": (
            "STAGE_43_ORDERING_PRINCIPLE_FOUND__EXACT_WEIGHT_MAP_OPEN" in stage43
            and "exact rho_s(k) formula: OPEN DERIVATION DEBT" in stage43
            and "reference eta=0.35: MODEL-CHOICE INPUT" in stage43
        ),
        "legacy_bounded_rhythm_declares_model_choice": (
            "The exact rhythm map is a model choice" in legacy_collatz_phase_sim
            and "eta: float = 0.35" in legacy_collatz_phase_sim
        ),
        "stage44_product_seed_parent_pass_present": (
            "STAGE_44_COLLATZ_PRODUCT_SEED_INTERSECTION_PASS" in stage44
            and "n_1=15" in stage44
            and "n_2=35" in stage44
            and "n_3=143" in stage44
        ),
        "stage45_distance_to_amplitude_provenance_nogo_present": (
            "STAGE_45_CANONICAL_DISTANCE_TO_AMPLITUDE_MAP_NOT_FOUND__PROVENANCE_NOGO_PASS"
            in stage45
            and "canonical distance/path-cost -> amplitude rule: NOT FOUND"
            in stage45
        ),
        "stage48_branch_word_interface_parent_pass_present": (
            "STAGE_48_BRANCH_WORD_INTERFACE_PASS_OPERATOR_ASSIGNMENT_OPEN" in stage48
            and "branch symbol -> family-space operator" in stage48
            and "exact per-step rhythm/weight" in stage48
        ),
        "stage49_collatz_mobius_poincare_lift_pass_present": (
            "STAGE_49_COLLATZ_MOBIUS_POINCARE_LIFT_PASS" in stage49
            and "\\{E,O\\}^*" in stage49
            and "PSL(2,\\mathbb R)" in stage49
        ),
        "stage50_sym2_three_carrier_pass_present": (
            "STAGE_50_SYM2_POLYNOMIAL_THREE_CARRIER_PASS_WITH_SIGNATURE_SEPARATION"
            in stage50
            and "SL(2,\\mathbb R)" in stage50
            and "SL(3,\\mathbb R)" in stage50
        ),
        "stage51_direct_unitarization_nogo_present": (
            "STAGE_51_POSITIVE_HERMITIAN_UNITARIZATION_NO_GO_PASS" in stage51
            and "cannot be conjugated into `SU(3)`" in stage51
        ),
        "stage52_compact_real_form_bridge_pass_selection_open": (
            "STAGE_52_COMPACT_REAL_FORM_SYM2_BRIDGE_PASS_SELECTION_OPEN" in stage52
            and "Sym^2(SU(2))" in stage52
            and "current TIR branch does not yet contain a derived rule selecting the compact real form"
            in stage52
        ),
        "stage53_spin1_cp_nogo_and_3plus5_parent_pass": (
            "STAGE_53_SPIN1_CP_NOGO_AND_SU3_3PLUS5_DECOMPOSITION_PASS" in stage53
            and "\\boxed{J=0}" in stage53
            and "\\mathbf 3\\oplus\\mathbf 5" in stage53
        ),
        "stage55_su3_so3_symmetric_pair_pass_present": (
            "STAGE_55_SU3_SO3_SYMMETRIC_PAIR_PASS" in stage55
            and "SU(3)/SO(3)" in stage55
            and "\\dim\\mathfrak p=5" in stage55
        ),
        "stage56_n5_icosahedral_spin2_irreducibility_pass_present": (
            "STAGE_56_N5_ICOSAHEDRAL_SPIN2_IRREDUCIBILITY_PASS" in stage56
            and "\\mathbf5\\downarrow A_5=\\mathbf5_{\\rm irr}" in stage56
        ),
        "stage57_icosahedral_triplet_tensor_square_match_pass_present": (
            "STAGE_57_ICOSAHEDRAL_TRIPLET_TENSOR_SQUARE_MATCH_PASS" in stage57
            and "\\mathbf3\\otimes\\mathbf3" in stage57
            and "\\mathbf1\\oplus\\mathbf3\\oplus\\mathbf5" in stage57
        ),
        "stage58_icosahedral_quadrupole_su3_generation_pass_present": (
            "STAGE_58_ICOSAHEDRAL_QUADRUPOLE_SU3_GENERATION_PASS" in stage58
            and "\\operatorname{rank}\\{Q_a\\}=5" in stage58
            and "Lie-closure dimension `8`" in stage58
        ),
        "stage64_selector_provenance_open_parent_present": (
            "STAGE_64_CANONICAL_SCALAR_SELECTOR_REMAINS_OPEN_PASS" in stage64
            and "branch symbol -> family-space operator" in stage64
            and "canonical_scalar_selector_status: OPEN" in stage64
        ),
        "stage65_stationary_selector_prevalidation_freeze_present": (
            "STAGE_65_STATIONARY_ORDERED_AXIS_SELECTOR_FROZEN_PREVALIDATION"
            in stage65
            and "CKM entries" in stage65
            and "`A_seed` is deliberately excluded from the selector equation"
            in stage65
        ),
        "stage66_unique_stationary_selector_parent_pass_present": (
            "STAGE_66_UNIQUE_STATIONARY_SELECTOR_PASS_WITH_SADDLE_CLASSIFICATION"
            in stage66
            and "eta_*" in stage66
            and "signature" in stage66
            and "A_seed" in stage66
        ),
        "stage66_selector_eta_exact_reproduced": eta_selector_residual < 1.0e-10,
        "stage66_selector_lambda_exact_reproduced": (
            lambda_selector_residual < 1.0e-10
        ),
        "stage66_stationarity_residual_reproduced": (
            selector_stationarity_residual < 1.0e-10
        ),
        "stage66_selector_hessian_signature_minus_plus_plus_plus": (
            len(selector_negative_indices) == 1
            and len(selector_positive_indices) == 3
            and len(selector_zero_indices) == 0
        ),
        "stage66_negative_mode_is_p3_Aseed_orbit_image": (
            selector_negative_best_orbit_index == 1
            and abs(selector_negative_best_alignment - 1.0) < 1.0e-10
        ),
        "sym2_binary_to_three_dimension_exact": sym2_dimension == 3,
        "split_real_branch_operator_homomorphism_exact": (
            sym2_homomorphism_residual < TOL
        ),
        "split_real_branch_operators_noncommute": (
            split_branch_noncommutativity > TOL
        ),
        "poincare_even_branch_translation_length_is_ln2": (
            ell_E_residual < TOL
        ),
        "poincare_odd_branch_translation_length_is_ln3": (
            ell_O_residual < TOL
        ),
        "branch_signed_log_jacobian_matches_translation_lengths": (
            signed_scale_residual < TOL
        ),
        "kappa_equals_even_branch_length_over_24pi": (
            kappa_length_residual < TOL
        ),
        "frozen_branch_word_signed_scale_cocycle_exact": (
            w1_slope_residual < TOL
            and w3_slope_residual < 1.0e-12
        ),
        "polar_even_compact_factor_is_identity": (
            polar_QE_identity_residual < TOL
        ),
        "polar_odd_compact_factor_exact": (
            polar_QO_exact_residual < TOL
            and polar_QO_orthogonality_residual < TOL
        ),
        "generatorwise_polar_compactification_loses_E_order": (
            generator_polar_order_separation < TOL
        ),
        "wordwise_polar_factor_detects_EO_vs_OE_order": (
            word_polar_order_separation > TOL
        ),
        "wordwise_polar_factor_is_not_branch_homomorphism": (
            word_polar_homomorphism_residual > TOL
        ),
        "sym2_branch_generators_have_det_one": bool(
            abs(np.linalg.det(RE) - 1.0) < TOL
            and abs(np.linalg.det(RO) - 1.0) < TOL
        ),
        "sym2_split_real_invariant_preserved": split_invariant_residual < TOL,
        "split_real_even_generator_not_unitary_spectrum": bool(
            abs(re_eigen_moduli[0] - 0.5) < TOL
            and abs(re_eigen_moduli[1] - 1.0) < TOL
            and abs(re_eigen_moduli[2] - 2.0) < TOL
        ),
        "stage61_c3_icosahedral_parent_pass_present": (
            "STAGE_61_C3_ICOSAHEDRAL_FAMILY_INTERTWINER_PASS" in stage61
            and "P3 acts as icosahedral order-3 symmetry: PASS" in stage61
        ),
        "stage62_embedding_rigidity_parent_pass_present": (
            "STAGE_62_FAMILY_ICOSAHEDRAL_EMBEDDING_RIGIDITY_PASS" in stage62
            and "residual C3 label freedom after fixed A_seed: NONE" in stage62
        ),
        "raw_product_seed_collatz_c3_cycle_refuted": (
            not product_directed_cycle_exists
            and product_reachability.tolist()
            == [[0, 4, -1], [-1, 0, -1], [-1, 90, 0]]
        ),
        "temporal_forward_generator_maps_e1_to_e2": (
            temporal_forward_edge == e2_tuple
        ),
        "temporal_inverse_generator_maps_e1_to_e3": (
            temporal_reverse_edge == e3_tuple
        ),
        "forward_and_inverse_c3_generators_are_distinct": (
            inverse_generator_separation > 0.0
        ),
        "oriented_temporal_c3_selects_family_p3_equivariantly": (
            oriented_generator_residual < TOL
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
        "independent_family_multiplicity_status": (
            "STAGE21_E8_THREEFOLD_MULTIPLICITY_3_CURRENT_PASS"
            if passed
            else "FAILED"
        ),
        "seed_exceptional_triplet_binding_status": (
            "STAGE24_ORDERED_SEED_TO_E8_TRIPLET_INTERTWINER_CURRENT_PASS"
            if passed
            else "FAILED"
        ),
        "temporal_c3_family_role": (
            "INDEPENDENT_C3_CROSSWALK_TO_EXISTING_MULTIPLICITY3_FAMILY_CARRIER"
            if passed
            else "FAILED"
        ),
        "raw_product_seed_cycle_status": (
            "ORDINARY_PRODUCT_SEED_COLLATZ_C3_CYCLE_REFUTED"
            if passed
            else "NOT_ESTABLISHED"
        ),
        "distance_amplitude_status": (
            "CANONICAL_PATH_COST_TO_AMPLITUDE_RULE_NOT_FOUND"
            if passed
            else "NOT_ESTABLISHED"
        ),
        "collatz_poincare_operator_chain_status": (
            "BRANCH_WORD_TO_PSL2R_TO_SYM2_THREE_CARRIER_CURRENT_EXACT"
            if passed
            else "FAILED"
        ),
        "branch_symbol_split_real_operator_status": (
            "BRANCH_SYMBOL_TO_SPLIT_REAL_THREE_OPERATOR_CLOSED"
            if passed
            else "FAILED"
        ),
        "legacy_rhythm_status": (
            "LEGACY_BOUNDED_RHYTHM_MODEL_CHOICE_NOT_PROMOTED"
        ),
        "poincare_branch_translation_length_status": (
            "POINCARE_BRANCH_TRANSLATION_LENGTH_ALPHABET_CLOSED"
            if passed
            else "FAILED"
        ),
        "branch_scale_cocycle_status": (
            "SIGNED_LOG_JACOBIAN_COCYCLE_CLOSED"
            if passed
            else "FAILED"
        ),
        "geometric_rhythm_alphabet_status": (
            "CANONICAL_GEOMETRIC_RHYTHM_ALPHABET_AVAILABLE"
            if passed
            else "FAILED"
        ),
        "exact_rhythm_status": (
            "EXACT_GEOMETRIC_BRANCH_LENGTH_ALPHABET_CLOSED__HAMILTONIAN_RHO_BINDING_OPEN"
        ),
        "family_endpoint_class_status": (
            "CURRENT_FAMILY_ENDPOINT_COMPACT_SU3F_REQUIRED"
            if passed
            else "FAILED"
        ),
        "real_form_endpoint_status": (
            "COMPACT_ENDPOINT_CLASS_FIXED__DYNAMICAL_BRANCHWISE_LIFT_OPEN"
            if passed
            else "FAILED"
        ),
        "canonical_polar_compactification_status": (
            "CANONICAL_POLAR_COMPACTIFICATION_REFUTED_AS_SUFFICIENT_BRANCH_LIFT"
            if passed
            else "FAILED"
        ),
        "compact_family_branch_operator_status": (
            "OPEN_NONPOLAR_BRANCHWISE_SPLIT_REAL_TO_COMPACT_SU3F_LIFT"
        ),
        "binary_to_three_carrier_status": (
            "SYM2_TWO_TO_THREE_CARRIER_CLOSED"
            if passed
            else "FAILED"
        ),
        "split_real_to_family_unitary_status": (
            "DIRECT_UNITARIZATION_REFUTED__COMPACT_SU3F_ENDPOINT_REQUIRED__BRANCHWISE_REALFORM_LIFT_OPEN"
            if passed
            else "FAILED"
        ),
        "spin1_cp_status": (
            "COMPACT_SPIN1_SUBGROUP_JARLSKOG_ZERO_FULL_SU3_COMPLEMENT_REQUIRED"
            if passed
            else "FAILED"
        ),
        "su3_so3_complement_status": (
            "FIVE_DIMENSIONAL_SU3_OVER_SO3_SPIN2_COMPLEMENT_CURRENT_EXACT"
            if passed
            else "FAILED"
        ),
        "n5_icosahedral_complement_status": (
            "N5_A5_IRREDUCIBLE_FIVE_CARRIER_CURRENT_EXACT"
            if passed
            else "FAILED"
        ),
        "icosahedral_su3_generation_status": (
            "SIX_ICOSAHEDRAL_QUADRUPOLES_GENERATE_FULL_SU3_CURRENT_EXACT"
            if passed
            else "FAILED"
        ),
        "cubic_complement_selector_status": (
            "STAGE66_UNIQUE_STATIONARY_CUBIC_SELECTOR_CLOSED_SADDLE"
            if passed
            else "FAILED"
        ),
        "cubic_complement_selector_eta_exact": (
            "-75*(59+21*sqrt(5))/638"
        ),
        "family_dynamics_selector_status": (
            "CUBIC_SELECTOR_CLOSED__SPLIT_REAL_BRANCH_OPERATOR_CLOSED__GEOMETRIC_RHYTHM_ALPHABET_CLOSED__COMPACT_ENDPOINT_CLASS_FIXED__CANONICAL_POLAR_LIFT_REFUTED__RHO_BINDING_AND_NONPOLAR_COMPACT_LIFT_OPEN"
        ),
        "oriented_family_generator_status": (
            "TEMPORAL_ORIENTATION_SELECTS_P3_VS_INVERSE_AT_REPRESENTATION_LEVEL"
            if passed
            else "FAILED"
        ),
        "icosahedral_family_embedding_status": (
            "STAGE61_62_C3_COMPATIBLE_RIGID_EMBEDDING_CURRENT_PASS"
            if passed
            else "FAILED"
        ),
        "seed_dynamical_cycle_status": (
            "OPEN_RICHER_POINCARE_HOLONOMY_OPERATOR_REQUIRED"
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
        "legacy_generated_projection_csv_tree_blob": archive_projection_csv_tree_blob,
        "legacy_generated_projection_csv_worktree_matches_head_object": (
            archive_projection_csv_worktree_matches_object
        ),
        "legacy_generated_projection_csv_up_quark_particle_ids": (
            archive_csv_up_quark_particle_ids
        ),
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
            "oriented_temporal_generator": oriented_generator_residual,
            "forward_inverse_generator_separation": inverse_generator_separation,
            "sym2_branch_homomorphism": sym2_homomorphism_residual,
            "split_branch_noncommutativity": split_branch_noncommutativity,
            "poincare_length_E_ln2": ell_E_residual,
            "poincare_length_O_ln3": ell_O_residual,
            "branch_signed_scale": signed_scale_residual,
            "kappa_even_branch_length": kappa_length_residual,
            "polar_QE_identity": polar_QE_identity_residual,
            "polar_QO_exact": polar_QO_exact_residual,
            "polar_generator_order_separation": generator_polar_order_separation,
            "polar_word_order_separation": word_polar_order_separation,
            "polar_word_homomorphism": word_polar_homomorphism_residual,
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
        "stationary_cubic_selector_audit": {
            "eta": float(eta_selector),
            "eta_exact": "-75*(59+21*sqrt(5))/638",
            "eta_residual": eta_selector_residual,
            "lambda": float(lambda_selector),
            "lambda_exact": "-(8765+4758*sqrt(5))/4785",
            "lambda_residual": lambda_selector_residual,
            "stationarity_residual": selector_stationarity_residual,
            "hessian_eigenvalues": selector_eigenvalues.tolist(),
            "hessian_signature": {
                "negative": int(len(selector_negative_indices)),
                "zero": int(len(selector_zero_indices)),
                "positive": int(len(selector_positive_indices)),
            },
            "classification": "SADDLE",
            "negative_mode_best_Aseed_orbit_index": (
                selector_negative_best_orbit_index
            ),
            "negative_mode_best_alignment": selector_negative_best_alignment,
            "Aseed_used_to_solve_eta": False,
            "uses_observed_CKM": False,
            "uses_observed_masses": False,
            "uses_fitted_coefficients": False,
        },
        "icosahedral_su3_complement_audit": {
            "compact_subgroup_dimension": 3,
            "symmetric_space_tangent_dimension": 5,
            "full_su3_dimension": 8,
            "symmetric_pair": "SU(3)/SO(3)",
            "n5_rotation_group": "A5",
            "n5_spin2_restriction": "irreducible_5",
            "icosahedral_axes_unoriented": 6,
            "quadrupole_span_dimension": 5,
            "commutator_span_dimension": 3,
            "lie_closure_dimension": 8,
            "physical_family_dynamics_selector": "OPEN",
        },
        "polar_compactification_audit": {
            "QE": QE.tolist(),
            "QO": QO.tolist(),
            "QO_exact": "1/sqrt(17)*[[4,1],[-1,4]]",
            "QE_identity_residual": polar_QE_identity_residual,
            "QO_exact_residual": polar_QO_exact_residual,
            "QO_orthogonality_residual": polar_QO_orthogonality_residual,
            "generatorwise_EO_vs_OE_separation": generator_polar_order_separation,
            "wordwise_EO_vs_OE_separation": word_polar_order_separation,
            "wordwise_polar_homomorphism_residual": word_polar_homomorphism_residual,
            "generatorwise_conclusion": "ORDER_INFORMATION_LOST_BECAUSE_QE_IS_IDENTITY",
            "wordwise_conclusion": "ORDER_RETAINED_BUT_NOT_A_MONOID_REPRESENTATION",
            "sufficient_family_lift": False,
        },
        "compact_family_endpoint_audit": {
            "family_carrier": "C^3",
            "family_group": "SU(3)_F",
            "positive_definite_unitary_endpoint": True,
            "direct_split_real_similarity_unitarization": "REFUTED",
            "complexification_real_form_bridge": "AVAILABLE",
            "compact_endpoint_class": "FIXED_BY_CURRENT_FAMILY_CARRIER",
            "branchwise_split_real_to_compact_lift": "OPEN",
        },
        "branch_operator_rhythm_audit": {
            "split_real_E_operator": RE.tolist(),
            "split_real_O_operator": RO.tolist(),
            "sym2_homomorphism_residual": sym2_homomorphism_residual,
            "branch_operator_noncommutativity_residual": split_branch_noncommutativity,
            "poincare_translation_length_E": ell_E,
            "poincare_translation_length_O": ell_O,
            "poincare_translation_length_E_exact": "ln(2)",
            "poincare_translation_length_O_exact": "ln(3)",
            "normalized_length_ratio_O_over_E": ell_O / ell_E,
            "normalized_length_ratio_exact": "ln(3)/ln(2)",
            "signed_log_jacobian_E": signed_log_jacobian_E,
            "signed_log_jacobian_O": signed_log_jacobian_O,
            "kappa_equals_ell_E_over_24pi_residual": kappa_length_residual,
            "w1_signed_scale_log_slope_residual": w1_slope_residual,
            "w3_signed_scale_log_slope_residual": w3_slope_residual,
            "split_real_branch_operator": "CLOSED",
            "compact_family_endpoint_class": "SU3F_REQUIRED",
            "compact_family_branch_operator": "OPEN_BRANCHWISE_LIFT",
            "legacy_bounded_rhythm_eta": 0.35,
            "legacy_bounded_rhythm_classification": "MODEL_CHOICE_NOT_PROMOTED",
            "exact_rho_s": "OPEN_DERIVATION_DEBT",
        },
        "collatz_poincare_three_carrier_audit": {
            "input_carrier_dimension": 2,
            "sym2_carrier_dimension": sym2_dimension,
            "RE": RE.tolist(),
            "RO": RO.tolist(),
            "split_invariant_signature": "(1,2) up to overall sign convention",
            "split_invariant_residual": split_invariant_residual,
            "RE_eigenvalue_moduli": re_eigen_moduli,
            "direct_fixed_similarity_to_SU3": "REFUTED",
            "compact_real_form_bridge": "AVAILABLE_SELECTION_OPEN",
            "spin1_subgroup_CP": "J_EQUALS_ZERO",
            "full_su3_complement": "3_PLUS_5",
        },
        "dynamical_cycle_audit": {
            "product_seeds": product_seeds,
            "directed_first_hit_matrix_minus1_for_absent": product_reachability.tolist(),
            "ordinary_product_seed_collatz_c3_cycle_exists": product_directed_cycle_exists,
            "stage45_canonical_path_cost_to_amplitude_rule": "NOT_FOUND",
            "temporal_forward_e1_image": temporal_forward_edge,
            "temporal_inverse_e1_image": temporal_reverse_edge,
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
            "family_multiplicity_three_already_has_independent_e8_parent": True,
            "temporal_c3_is_not_claimed_as_the_sole_origin_of_family_multiplicity": True,
            "ordinary_center_collatz_does_not_generate_stage24_cycle": True,
            "ordinary_product_seed_collatz_does_not_generate_stage24_cycle": True,
            "stage44_distance_geometry_is_not_converted_to_amplitude_without_new_law": True,
            "sym2_two_to_three_is_representation_carrier_not_physical_xyz_claim": True,
            "split_real_three_carrier_is_not_identified_directly_with_SU3F": True,
            "compact_real_form_bridge_availability_is_not_dynamical_selection": True,
            "current_family_unitarity_fixes_endpoint_class_not_branchwise_lift": True,
            "su3f_endpoint_requirement_does_not_override_stage51_similarity_nogo": True,
            "branchwise_realform_lift_requires_additional_dynamics": True,
            "generatorwise_polar_compactification_is_order_blind_for_even_steps": True,
            "wordwise_polar_factor_is_not_a_branch_monoid_homomorphism": True,
            "polar_compact_factor_is_diagnostic_not_physical_family_operator": True,
            "branch_symbol_to_split_real_operator_is_closed_but_not_physical_family_map": True,
            "legacy_eta_0_35_rhythm_is_model_choice_not_current_input": True,
            "exact_geometric_branch_length_alphabet_is_closed": True,
            "translation_length_equals_hamiltonian_rho_is_not_yet_promoted": True,
            "standard_poincare_curvature_minus_one_normalization_used_for_lengths": True,
            "exact_rho_s_remains_open_as_hamiltonian_binding": True,
            "spin1_compact_subgroup_alone_cannot_supply_nonzero_CP": True,
            "five_dimensional_complement_is_lie_tangent_not_five_physical_spatial_dimensions": True,
            "a5_icosahedral_five_carrier_is_not_equated_with_su3f_without_dynamics": True,
            "icosahedral_quadrupole_lie_generation_does_not_close_physical_family_selector": True,
            "stage64_selector_open_status_is_superseded_by_frozen_stage65_66_selector": True,
            "stage66_stationary_selector_is_mathematical_not_full_physical_dynamics": True,
            "stage66_saddle_classification_is_retained_not_repaired": True,
            "Aseed_was_not_used_to_fit_eta": True,
            "temporal_orientation_selection_is_representation_level_not_seed_dynamics": True,
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
    print(
        json.dumps(
            payload,
            indent=2,
            sort_keys=True,
            default=json_default,
        )
    )
    raise SystemExit(0 if passed else 1)


if __name__ == "__main__":
    main()
