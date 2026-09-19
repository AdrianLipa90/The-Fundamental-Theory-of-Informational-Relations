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
    coefficient_orientation = (
        ROOT
        / "TIR/foundations/TIR_COEFFICIENT_ROLE_ORIENTATION_FORCING_V0_1.md"
    ).read_text(encoding="utf-8")
    sm_reconciliation = (
        ROOT
        / "TIR/standard_model/TIR_SM_RECONCILIATION_LEDGER_V0_1.md"
    ).read_text(encoding="utf-8")
    wij_crosswalk = (
        ROOT
        / "TIR/foundations/TIR_WIJ_HOLONOMY_CROSSWALK_V0_1.md"
    ).read_text(encoding="utf-8")
    idt_c3_crosswalk_doc = (
        ROOT
        / "TIR/integration/TIR_IDT_MOD6PI_C3_PAULI_CROSSWALK_V0_1.md"
    ).read_text(encoding="utf-8")
    collatz_fs_phase_interface = (
        ROOT
        / "TIR/integration/TIR_COLLATZ_FS_RELATIONAL_PHASE_INTERFACE_V0_1.md"
    ).read_text(encoding="utf-8")
    hexahedral_bloch = (
        ROOT
        / "TIR/integration/TIR_HEXAHEDRAL_BLOCH_DUAL_FRAME_V0_1.md"
    ).read_text(encoding="utf-8")
    gremlin_overlay = (
        ROOT
        / "TIR/integration/GREMLIN_CROSS_REPO_DEPENDENCY_OVERLAY_V0_1.md"
    ).read_text(encoding="utf-8")
    hexahedral_bloch = (
        ROOT
        / "TIR/integration/TIR_HEXAHEDRAL_BLOCH_DUAL_FRAME_V0_1.md"
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
    stage35 = (
        ROOT
        / "TIR/frozen_predictions/validation/"
        "TIR_POLYGONAL_EXCITATION_STAGE35_HERMITIAN_FAMILY_PAIR_V0_1.md"
    ).read_text(encoding="utf-8")
    stage36 = (
        ROOT
        / "TIR/frozen_predictions/validation/"
        "TIR_POLYGONAL_EXCITATION_STAGE36_COMPLEX_HOLONOMY_CP_V0_1.md"
    ).read_text(encoding="utf-8")
    stage37 = (
        ROOT
        / "TIR/frozen_predictions/validation/"
        "TIR_POLYGONAL_EXCITATION_STAGE37_COMMON_FAMILY_AXIS_NOGO_V0_1.md"
    ).read_text(encoding="utf-8")
    stage38 = (
        ROOT
        / "TIR/frozen_predictions/validation/"
        "TIR_POLYGONAL_EXCITATION_STAGE38_C3_CHARACTER_BASIS_CP_V0_1.md"
    ).read_text(encoding="utf-8")
    stage33_receipt = json.loads(
        (
            ROOT
            / "TIR/frozen_predictions/validation/results/"
            "TIR_POLYGONAL_STAGE33_MCKAY_ENDPOINT_CKM_DICTIONARY_RECEIPT_V0_1.json"
        ).read_text(encoding="utf-8")
    )
    stage39 = (
        ROOT
        / "TIR/frozen_predictions/validation/"
        "TIR_POLYGONAL_EXCITATION_STAGE39_TWO_OPERATOR_FAMILY_CANDIDATE_V0_1.md"
    ).read_text(encoding="utf-8")
    stage40 = (
        ROOT
        / "TIR/frozen_predictions/validation/"
        "TIR_POLYGONAL_EXCITATION_STAGE40_STAGE39_CKM_RETROSPECTIVE_V0_1.md"
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

    # The C3 label basis and its character eigenbasis form two exact
    # projective frames with overlap matrix F3.
    label_frame = [
        np.array([1.0, 0.0, 0.0], dtype=complex),
        np.array([0.0, 1.0, 0.0], dtype=complex),
        np.array([0.0, 0.0, 1.0], dtype=complex),
    ]
    character_frame = [F3[:, j] for j in range(3)]
    F3_overlap = np.array(
        [[np.vdot(s, chi) for chi in character_frame] for s in label_frame],
        dtype=complex,
    )
    f3_overlap_residual = float(np.max(np.abs(F3_overlap - F3)))

    f3_plaquette = (
        F3_overlap[0, 0]
        * np.conj(F3_overlap[1, 0])
        * F3_overlap[1, 1]
        * np.conj(F3_overlap[0, 1])
    )
    f3_bargmann = (
        np.vdot(label_frame[0], character_frame[0])
        * np.vdot(character_frame[0], label_frame[1])
        * np.vdot(label_frame[1], character_frame[1])
        * np.vdot(character_frame[1], label_frame[0])
    )
    f3_bargmann_residual = abs(f3_plaquette - f3_bargmann)
    f3_bargmann_phase = math.atan2(
        float(np.imag(f3_bargmann)),
        float(np.real(f3_bargmann)),
    )
    f3_bargmann_phase_expected = 2.0 * math.pi / 3.0
    f3_bargmann_phase_residual = abs(
        f3_bargmann_phase - f3_bargmann_phase_expected
    )

    J = jarlskog(F3)
    J_exact = 1.0 / (6.0 * math.sqrt(3.0))
    f3_plaquette_j_residual = abs(float(np.imag(f3_plaquette)) - J_exact)

    # Stage-42 family Lie closure and its pullback through M_tf.
    D_family = np.diag(
        [-1.0 / 3.0, 0.0, 1.0 / math.sqrt(5.0)]
    ).astype(complex)
    C_family = F3 @ D_family @ F3.conj().T
    D_temporal = M_tf.conj().T @ D_family @ M_tf
    C_temporal = M_tf.conj().T @ C_family @ M_tf

    # D and C=F3 D F3^dagger are unitarily conjugate.  Therefore no
    # single-generator spectral invariant can break the E/O <-> D/C Z2.
    dc_spectral_eigen_residual = float(
        np.max(
            np.abs(
                np.sort(np.linalg.eigvalsh(D_family))
                - np.sort(np.linalg.eigvalsh(C_family))
            )
        )
    )
    dc_trace_power_residual = max(
        abs(
            complex(np.trace(np.linalg.matrix_power(D_family, p)))
            - complex(np.trace(np.linalg.matrix_power(C_family, p)))
        )
        for p in (1, 2, 3)
    )
    dc_frobenius_residual = abs(
        float(np.linalg.norm(D_family, "fro"))
        - float(np.linalg.norm(C_family, "fro"))
    )

    # Stage-55 symmetric-pair projection in the exact spin-one basis used
    # by the canonical validator.
    r2_stage55 = math.sqrt(2.0)
    Jx_stage55 = np.array(
        [[0, 1, 0], [1, 0, 1], [0, 1, 0]], dtype=complex
    ) / r2_stage55
    Jy_stage55 = np.array(
        [[0, -1j, 0], [1j, 0, -1j], [0, 1j, 0]], dtype=complex
    ) / r2_stage55
    Jz_stage55 = np.diag([1.0, 0.0, -1.0]).astype(complex)
    Js_stage55 = [Jx_stage55, Jy_stage55, Jz_stage55]

    def stage55_casimir(X: np.ndarray) -> np.ndarray:
        out = np.zeros_like(X, dtype=complex)
        for J55 in Js_stage55:
            K55 = J55 @ X - X @ J55
            out += J55 @ K55 - K55 @ J55
        return out

    def stage55_Pk(X: np.ndarray) -> np.ndarray:
        return (6.0 * X - stage55_casimir(X)) / 4.0

    def stage55_Pp(X: np.ndarray) -> np.ndarray:
        return (stage55_casimir(X) - 2.0 * X) / 4.0

    D0_family = D_family - np.trace(D_family) / 3.0 * np.eye(3)
    C0_family = C_family - np.trace(C_family) / 3.0 * np.eye(3)
    D0_k = stage55_Pk(D0_family)
    D0_p = stage55_Pp(D0_family)
    C0_k = stage55_Pk(C0_family)
    C0_p = stage55_Pp(C0_family)
    D0_k_norm2 = float(np.linalg.norm(D0_k, "fro") ** 2)
    D0_p_norm2 = float(np.linalg.norm(D0_p, "fro") ** 2)
    C0_k_norm2 = float(np.linalg.norm(C0_k, "fro") ** 2)
    C0_p_norm2 = float(np.linalg.norm(C0_p, "fro") ** 2)
    D0_stage55_reconstruction_residual = float(
        np.max(np.abs(D0_k + D0_p - D0_family))
    )
    C0_stage55_reconstruction_residual = float(
        np.max(np.abs(C0_k + C0_p - C0_family))
    )

    D0_k_norm2_exact = math.sqrt(5.0) / 15.0 + 7.0 / 45.0
    D0_p_norm2_exact = 7.0 / 135.0 - math.sqrt(5.0) / 45.0
    C0_k_norm2_exact = 4.0 * math.sqrt(5.0) / 135.0 + 56.0 / 405.0
    C0_p_norm2_exact = 2.0 * math.sqrt(5.0) / 135.0 + 28.0 / 405.0
    stage55_dc_norm_formula_residual = max(
        abs(D0_k_norm2 - D0_k_norm2_exact),
        abs(D0_p_norm2 - D0_p_norm2_exact),
        abs(C0_k_norm2 - C0_k_norm2_exact),
        abs(C0_p_norm2 - C0_p_norm2_exact),
    )

    # Stage-39 two-sector structural candidate, frozen before target comparison.
    alpha_a = 2.0 / 7.0
    alpha_b = 2.0 / 9.0

    def stage39_relative(alpha_u: float, alpha_d: float):
        H_u = D_family + alpha_u * C_family
        H_d = D_family + alpha_d * C_family
        _, U_u = np.linalg.eigh(H_u)
        _, U_d = np.linalg.eigh(H_d)
        V_raw = U_u.conj().T @ U_d
        V = V_raw * np.exp(-1j * np.angle(np.linalg.det(V_raw)) / 3.0)
        comm = H_u @ H_d - H_d @ H_u
        return {
            "H_u": H_u,
            "H_d": H_d,
            "V": V,
            "J": jarlskog(V),
            "commutator_max_abs": float(np.max(np.abs(comm))),
            "unitarity_residual": float(
                np.max(np.abs(V.conj().T @ V - np.eye(3)))
            ),
            "determinant_residual": float(abs(np.linalg.det(V) - 1.0)),
            "absV": np.abs(V),
        }

    stage39_A = stage39_relative(alpha_a, alpha_b)
    stage39_B = stage39_relative(alpha_b, alpha_a)
    stage39_J_expected = 2.0174220730068447e-5
    stage39_J_A_abs_residual = abs(abs(stage39_A["J"]) - stage39_J_expected)
    stage39_J_B_abs_residual = abs(abs(stage39_B["J"]) - stage39_J_expected)
    stage39_J_sign_flip_residual = abs(stage39_A["J"] + stage39_B["J"])
    stage39_abs_transpose_residual = float(
        np.max(np.abs(stage39_A["absV"] - stage39_B["absV"].T))
    )

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

    # Exact CP no-go for any family phase matrix built only as a separable
    # vertex potential from the scalar IDT q_C values.  For
    # phi_ij = 2*pi*(alpha_i-beta_j), every rephasing-invariant plaquette
    # exponent alpha_i-beta_k+alpha_j-beta_l-alpha_i+beta_l-alpha_j+beta_k
    # cancels exactly.  The concrete q_C-difference law is one such case.
    q_vertices = (q1, q2, q3)
    qc_pair_phase_turns = tuple(
        tuple(q_vertices[i] - q_vertices[j] for j in range(3))
        for i in range(3)
    )
    qc_plaquette_turns = []
    for i in range(3):
        for j in range(i + 1, 3):
            for k in range(3):
                for l in range(k + 1, 3):
                    qc_plaquette_turns.append(
                        qc_pair_phase_turns[i][k]
                        + qc_pair_phase_turns[j][l]
                        - qc_pair_phase_turns[i][l]
                        - qc_pair_phase_turns[j][k]
                    )
    qc_all_plaquette_turns_zero = all(x == 0 for x in qc_plaquette_turns)
    qc_pair_phase_antisymmetric = all(
        qc_pair_phase_turns[i][j] == -qc_pair_phase_turns[j][i]
        for i in range(3)
        for j in range(3)
    )
    qc_pair_phase_diagonal_zero = all(
        qc_pair_phase_turns[i][i] == 0 for i in range(3)
    )

    # Equatorial CP1/Bargmann no-go for scalar q_C alone.
    # For |psi(q)>=(|0>+exp(2*pi*i*q)|1>)/sqrt(2),
    # <psi_i|psi_j>=exp(i*pi*(q_j-q_i))*cos(pi*(q_j-q_i)).
    # The three overlap phases telescope exactly around a closed triple.
    qc_bargmann_turn_sum = (
        (q2 - q1) + (q3 - q2) + (q1 - q3)
    )
    qc_pair_distances = (
        abs(q2 - q1),
        abs(q3 - q2),
        abs(q1 - q3),
    )
    qc_pair_distances_lt_half = all(
        d < Fraction(1, 2) for d in qc_pair_distances
    )
    qc_equatorial_states = []
    for q in q_vertices:
        theta = 2.0 * math.pi * float(q)
        qc_equatorial_states.append(
            np.array([1.0, np.exp(1j * theta)], dtype=complex) / math.sqrt(2.0)
        )
    qc_bargmann = (
        np.vdot(qc_equatorial_states[0], qc_equatorial_states[1])
        * np.vdot(qc_equatorial_states[1], qc_equatorial_states[2])
        * np.vdot(qc_equatorial_states[2], qc_equatorial_states[0])
    )
    qc_bargmann_imag_residual = abs(float(np.imag(qc_bargmann)))
    qc_bargmann_real = float(np.real(qc_bargmann))
    qc_bargmann_phase = math.atan2(
        float(np.imag(qc_bargmann)),
        float(np.real(qc_bargmann)),
    )

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

    # Orientation-reflection extension of C3.  This Z2 acts by inversion,
    # unlike the commuting weak Weyl Z2 used in the six-state C6 product.
    R_orient = np.array(
        [[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]],
        dtype=complex,
    )
    orientation_reflection_involution_residual = float(
        np.max(np.abs(R_orient @ R_orient - np.eye(3)))
    )
    orientation_inversion_action_residual = float(
        np.max(
            np.abs(
                R_orient @ P_family @ R_orient
                - np.linalg.matrix_power(P_family, 2)
            )
        )
    )
    orientation_extension_noncommutativity = float(
        np.max(np.abs(R_orient @ P_family - P_family @ R_orient))
    )

    d3_elements = [
        np.eye(3, dtype=complex),
        P_family,
        np.linalg.matrix_power(P_family, 2),
        R_orient,
        R_orient @ P_family,
        R_orient @ np.linalg.matrix_power(P_family, 2),
    ]
    d3_element_keys = {
        tuple(np.rint(np.real(M)).astype(int).reshape(-1).tolist())
        for M in d3_elements
    }
    d3_unique_element_count = len(d3_element_keys)

    weak_family_c3 = np.kron(P_family, np.eye(2, dtype=complex))
    weak_family_z2 = np.kron(np.eye(3, dtype=complex), J_weak)
    weak_family_commutator_residual = float(
        np.max(
            np.abs(
                weak_family_c3 @ weak_family_z2
                - weak_family_z2 @ weak_family_c3
            )
        )
    )

    G6_rotation = weak_family_c3 @ weak_family_z2
    R6_orientation = np.kron(
        R_orient, np.eye(2, dtype=complex)
    )
    G6_order6_residual = float(
        np.max(
            np.abs(
                np.linalg.matrix_power(G6_rotation, 6)
                - np.eye(6)
            )
        )
    )
    G6_lower_power_nonidentity = min(
        float(
            np.max(
                np.abs(
                    np.linalg.matrix_power(G6_rotation, k)
                    - np.eye(6)
                )
            )
        )
        for k in range(1, 6)
    )
    R6_involution_residual = float(
        np.max(
            np.abs(
                R6_orientation @ R6_orientation
                - np.eye(6)
            )
        )
    )
    D6_inversion_relation_residual = float(
        np.max(
            np.abs(
                R6_orientation @ G6_rotation @ R6_orientation
                - np.linalg.matrix_power(G6_rotation, 5)
            )
        )
    )
    D6_elements = [
        np.linalg.matrix_power(G6_rotation, k)
        for k in range(6)
    ] + [
        R6_orientation @ np.linalg.matrix_power(G6_rotation, k)
        for k in range(6)
    ]
    D6_element_keys = {
        tuple(np.rint(np.real(M)).astype(int).reshape(-1).tolist())
        for M in D6_elements
    }
    D6_unique_element_count = len(D6_element_keys)

    # Real permutation representation decomposition R^3 = 1 + 2 for D3/S3.
    d3_singlet = np.ones(3, dtype=float) / math.sqrt(3.0)
    d3_plane_basis = np.column_stack(
        [
            np.array([1.0, -1.0, 0.0], dtype=float) / math.sqrt(2.0),
            np.array([1.0, 1.0, -2.0], dtype=float) / math.sqrt(6.0),
        ]
    )
    d3_plane_orthonormal_residual = float(
        np.max(
            np.abs(
                d3_plane_basis.T @ d3_plane_basis
                - np.eye(2)
            )
        )
    )
    d3_singlet_plane_residual = float(
        np.max(np.abs(d3_plane_basis.T @ d3_singlet))
    )
    d3_singlet_P_residual = float(
        np.max(
            np.abs(
                np.real(P_family) @ d3_singlet - d3_singlet
            )
        )
    )
    d3_singlet_R_residual = float(
        np.max(
            np.abs(
                np.real(R_orient) @ d3_singlet - d3_singlet
            )
        )
    )
    P_d3_plane = d3_plane_basis.T @ np.real(P_family) @ d3_plane_basis
    R_d3_plane = d3_plane_basis.T @ np.real(R_orient) @ d3_plane_basis
    d3_plane_rotation_order3_residual = float(
        np.max(
            np.abs(
                np.linalg.matrix_power(P_d3_plane, 3)
                - np.eye(2)
            )
        )
    )
    d3_plane_rotation_trace_residual = abs(
        float(np.trace(P_d3_plane)) + 1.0
    )
    d3_plane_rotation_det_residual = abs(
        float(np.linalg.det(P_d3_plane)) - 1.0
    )
    d3_plane_reflection_involution_residual = float(
        np.max(
            np.abs(
                R_d3_plane @ R_d3_plane - np.eye(2)
            )
        )
    )
    d3_plane_reflection_det_residual = abs(
        float(np.linalg.det(R_d3_plane)) + 1.0
    )
    d3_plane_dihedral_relation_residual = float(
        np.max(
            np.abs(
                R_d3_plane @ P_d3_plane @ R_d3_plane
                - np.linalg.matrix_power(P_d3_plane, 2)
            )
        )
    )

    f3_trivial_character_residual = float(
        np.max(np.abs(F3[:, 0] - d3_singlet.astype(complex)))
    )
    f3_nontrivial_character_conjugacy_residual = float(
        np.max(np.abs(F3[:, 2] - np.conj(F3[:, 1])))
    )
    d3_real_plane_projector = d3_plane_basis @ d3_plane_basis.T
    f3_nontrivial_projector = (
        np.outer(F3[:, 1], np.conj(F3[:, 1]))
        + np.outer(F3[:, 2], np.conj(F3[:, 2]))
    )
    f3_character_plane_projector_residual = float(
        np.max(
            np.abs(
                f3_nontrivial_projector
                - d3_real_plane_projector.astype(complex)
            )
        )
    )

    # Rank-two Cartan plane of the compact symmetric space SU(3)/SO(3).
    # The family zero-sum plane x1+x2+x3=0 maps explicitly to diagonal
    # real-symmetric traceless Hermitian matrices H(x)=diag(x).
    su3so3_cartan_basis = [
        np.diag(d3_plane_basis[:, j]).astype(complex)
        for j in range(2)
    ]
    su3so3_cartan_gram = np.array(
        [
            [
                float(np.real(np.trace(A.conj().T @ B)))
                for B in su3so3_cartan_basis
            ]
            for A in su3so3_cartan_basis
        ],
        dtype=float,
    )
    su3so3_cartan_orthonormal_residual = float(
        np.max(np.abs(su3so3_cartan_gram - np.eye(2)))
    )
    su3so3_cartan_commutator_residual = float(
        np.max(
            np.abs(
                su3so3_cartan_basis[0] @ su3so3_cartan_basis[1]
                - su3so3_cartan_basis[1] @ su3so3_cartan_basis[0]
            )
        )
    )

    def cartan_action_coeffs(M: np.ndarray) -> np.ndarray:
        out = np.zeros((2, 2), dtype=float)
        Mr = np.real(M)
        for j, H in enumerate(su3so3_cartan_basis):
            Ht = Mr @ H @ Mr.T
            for i, B in enumerate(su3so3_cartan_basis):
                out[i, j] = float(np.real(np.trace(B.conj().T @ Ht)))
        return out

    P_cartan_plane = cartan_action_coeffs(P_family)
    R_cartan_plane = cartan_action_coeffs(R_orient)
    family_to_cartan_P_intertwiner_residual = float(
        np.max(np.abs(P_cartan_plane - P_d3_plane))
    )
    family_to_cartan_R_intertwiner_residual = float(
        np.max(np.abs(R_cartan_plane - R_d3_plane))
    )

    e1_root = np.array([1.0, 0.0, 0.0])
    e2_root = np.array([0.0, 1.0, 0.0])
    e3_root = np.array([0.0, 0.0, 1.0])
    alpha12 = d3_plane_basis.T @ (e1_root - e2_root)
    alpha23 = d3_plane_basis.T @ (e2_root - e3_root)
    alpha13 = d3_plane_basis.T @ (e1_root - e3_root)
    a2_root_sum_residual = float(
        np.max(np.abs(alpha12 + alpha23 - alpha13))
    )
    a2_root_norm_residual = max(
        abs(float(alpha12 @ alpha12) - 2.0),
        abs(float(alpha23 @ alpha23) - 2.0),
        abs(float(alpha13 @ alpha13) - 2.0),
    )
    a2_cartan_offdiag_12_23 = (
        2.0 * float(alpha12 @ alpha23) / float(alpha23 @ alpha23)
    )
    a2_cartan_offdiag_23_12 = (
        2.0 * float(alpha23 @ alpha12) / float(alpha12 @ alpha12)
    )
    a2_cartan_matrix_residual = max(
        abs(a2_cartan_offdiag_12_23 + 1.0),
        abs(a2_cartan_offdiag_23_12 + 1.0),
    )

    # Compact SU(3) Weyl alcove in the same rank-two Cartan plane.
    # Chamber: theta1>=theta2>=theta3, theta1-theta3<=2*pi,
    # theta1+theta2+theta3=0.
    alcove_vertices_x = np.array(
        [
            [0.0, 0.0, 0.0],
            [2.0 * math.pi / 3.0, 2.0 * math.pi / 3.0, -4.0 * math.pi / 3.0],
            [4.0 * math.pi / 3.0, -2.0 * math.pi / 3.0, -2.0 * math.pi / 3.0],
        ],
        dtype=float,
    )
    alcove_vertices_q = np.array(
        [d3_plane_basis.T @ x for x in alcove_vertices_x],
        dtype=float,
    )
    alcove_side_lengths = [
        float(
            np.linalg.norm(
                alcove_vertices_q[(i + 1) % 3] - alcove_vertices_q[i]
            )
        )
        for i in range(3)
    ]
    alcove_side_exact = 2.0 * math.pi * math.sqrt(2.0 / 3.0)
    alcove_equilateral_residual = max(
        abs(s - alcove_side_exact) for s in alcove_side_lengths
    )
    alcove_area = abs(
        float(
            np.linalg.det(
                np.column_stack(
                    [
                        alcove_vertices_q[1] - alcove_vertices_q[0],
                        alcove_vertices_q[2] - alcove_vertices_q[0],
                    ]
                )
            )
        )
    ) / 2.0
    alcove_area_exact = 2.0 * math.pi * math.pi / math.sqrt(3.0)
    alcove_area_residual = abs(alcove_area - alcove_area_exact)

    omega3 = np.exp(2j * math.pi / 3.0)
    alcove_vertex_traces = np.array(
        [
            np.sum(np.exp(1j * x))
            for x in alcove_vertices_x
        ],
        dtype=complex,
    )
    alcove_expected_cusps = np.array(
        [3.0 + 0.0j, 3.0 * omega3, 3.0 * np.conj(omega3)],
        dtype=complex,
    )
    alcove_cusp_residual = float(
        np.max(np.abs(alcove_vertex_traces - alcove_expected_cusps))
    )

    # The edge theta1=theta2 has trace 2 e^{it}+e^{-2it},
    # i.e. exactly one deltoid boundary arc.
    alcove_edge_t = np.linspace(0.0, 2.0 * math.pi / 3.0, 241)
    alcove_edge_trace = (
        2.0 * np.exp(1j * alcove_edge_t)
        + np.exp(-2j * alcove_edge_t)
    )
    alcove_edge_deltoid_residual = float(
        np.max(
            np.abs(
                alcove_edge_trace
                - (
                    2.0 * np.exp(1j * alcove_edge_t)
                    + np.exp(-2j * alcove_edge_t)
                )
            )
        )
    )

    # Trace is invariant under the D3/S3 Weyl permutations.
    alcove_probe_x = np.array([0.7, 0.1, -0.8], dtype=float)
    alcove_probe_trace = np.sum(np.exp(1j * alcove_probe_x))
    alcove_weyl_trace_residual = max(
        abs(
            np.sum(np.exp(1j * (np.real(M) @ alcove_probe_x)))
            - alcove_probe_trace
        )
        for M in d3_elements
    )

    # On the rank-two diagonal Cartan flat, choose g=exp(iH/2), so Phi=exp(iH).
    H_cartan_probe = np.diag(alcove_probe_x).astype(complex)
    g_cartan_probe = np.diag(np.exp(0.5j * alcove_probe_x))
    S_cartan_probe = g_cartan_probe @ g_cartan_probe.T
    exp_iH_probe = np.diag(np.exp(1j * alcove_probe_x))
    cartan_embedding_flat_exp_residual = float(
        np.max(np.abs(S_cartan_probe - exp_iH_probe))
    )
    cartan_embedding_flat_trace_residual = abs(
        np.trace(S_cartan_probe) - alcove_probe_trace
    )

    # Six-state C6 character spectrum from C3 x Z2.
    F2 = np.array(
        [[1.0, 1.0], [1.0, -1.0]],
        dtype=complex,
    ) / math.sqrt(2.0)
    F6_tensor = np.kron(F3, F2)
    G6_character = F6_tensor.conj().T @ G6_rotation @ F6_tensor
    G6_character_offdiag_residual = float(
        np.max(
            np.abs(
                G6_character
                - np.diag(np.diag(G6_character))
            )
        )
    )
    G6_character_eigenvalues = np.diag(G6_character)
    sixth_roots = np.array(
        [
            np.exp(2.0j * math.pi * k / 6.0)
            for k in range(6)
        ],
        dtype=complex,
    )
    unmatched = list(sixth_roots)
    G6_sixth_root_match_residuals = []
    for z in G6_character_eigenvalues:
        j = min(range(len(unmatched)), key=lambda q: abs(z - unmatched[q]))
        G6_sixth_root_match_residuals.append(abs(z - unmatched[j]))
        unmatched.pop(j)
    G6_sixth_root_match_residual = max(G6_sixth_root_match_residuals)

    G6_real_eigenvalue_count = sum(
        abs(float(np.imag(z))) < TOL for z in G6_character_eigenvalues
    )
    G6_nonreal_eigenvalue_count = 6 - G6_real_eigenvalue_count
    G6_conjugate_pair_residual = max(
        min(abs(np.conj(z) - w) for w in G6_character_eigenvalues)
        for z in G6_character_eigenvalues
    )
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

    # Real-Lie homomorphism no-go: sl(2,R) is simple noncompact.
    # In the standard H,E,F basis its Killing form has signature (2,1).
    sl2_killing = np.array(
        [[8.0, 0.0, 0.0], [0.0, 0.0, 4.0], [0.0, 4.0, 0.0]],
        dtype=float,
    )
    sl2_killing_eigenvalues = np.linalg.eigvalsh(sl2_killing)
    sl2_killing_negative = int(np.sum(sl2_killing_eigenvalues < -TOL))
    sl2_killing_positive = int(np.sum(sl2_killing_eigenvalues > TOL))
    sl2_killing_zero = int(np.sum(np.abs(sl2_killing_eigenvalues) <= TOL))

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

    # Full Stage-66 C3 orbit as a source-derived family-generator set.
    # Any pair closes only a 3D subalgebra, while all three orbit members
    # generate the full 8D su(3)_F algebra.
    selector_pair_dims = {}
    selector_pair_residuals = {}
    for ia, ib in ((0, 1), (1, 2), (2, 0)):
        dim_pair, res_pair = lie_closure_dimension(
            [selector_orbit[ia], selector_orbit[ib]]
        )
        selector_pair_dims[f"{ia}{ib}"] = dim_pair
        selector_pair_residuals[f"{ia}{ib}"] = res_pair

    selector_orbit_lie_dim, selector_orbit_lie_residual = lie_closure_dimension(
        selector_orbit
    )

    selector_orbit_kp = []
    for A in selector_orbit:
        Ak = stage55_Pk(A)
        Ap = stage55_Pp(A)
        selector_orbit_kp.append(
            {
                "k_norm2": float(np.linalg.norm(Ak, "fro") ** 2),
                "p_norm2": float(np.linalg.norm(Ap, "fro") ** 2),
                "reconstruction_residual": float(np.max(np.abs(Ak + Ap - A))),
            }
        )

    selector_orbit_kp_expected = [
        {"k_norm2": 0.25, "p_norm2": 0.25},
        {"k_norm2": 0.25, "p_norm2": 0.25},
        {"k_norm2": 0.0, "p_norm2": 0.5},
    ]
    selector_orbit_kp_residual = max(
        abs(selector_orbit_kp[i][key] - selector_orbit_kp_expected[i][key])
        for i in range(3)
        for key in ("k_norm2", "p_norm2")
    )
    selector_orbit_kp_reconstruction_residual = max(
        x["reconstruction_residual"] for x in selector_orbit_kp
    )

    selector_forward_A1 = selector_orbit[1]
    selector_forward_A2 = selector_orbit[2]
    selector_forward_commutator = (
        selector_forward_A1 @ selector_forward_A2
        - selector_forward_A2 @ selector_forward_A1
    )
    selector_forward_commutator_max = float(
        np.max(np.abs(selector_forward_commutator))
    )
    selector_forward_commutator_norm2 = float(
        np.linalg.norm(selector_forward_commutator, "fro") ** 2
    )

    # Exact Collatz-state -> temporal C3 frame index on the finite-stopping basin.
    # Anchor n=1 at frame 0 and define r_C(n)=-L(n) mod 3.  One Collatz
    # step advances the frame by +1 mod 3, including the terminal 1->4 step.
    collatz_c3_tested = 10000
    collatz_c3_failures = []
    collatz_c3_frame_counts = [0, 0, 0]
    for n in range(1, collatz_c3_tested + 1):
        Ln = collatz_depth_to_one(n)
        Lnext = collatz_depth_to_one(collatz_step(n))
        rn = (-Ln) % 3
        rnext = (-Lnext) % 3
        collatz_c3_frame_counts[rn] += 1
        if rnext != (rn + 1) % 3:
            collatz_c3_failures.append(
                {
                    "n": n,
                    "L": Ln,
                    "L_next": Lnext,
                    "r": rn,
                    "r_next": rnext,
                }
            )

    terminal_cycle_states = [1, 4, 2]
    terminal_cycle_depths = [collatz_depth_to_one(n) for n in terminal_cycle_states]
    terminal_cycle_frames = [(-x) % 3 for x in terminal_cycle_depths]
    terminal_cycle_qc = [q_c(n) for n in terminal_cycle_states]
    terminal_cycle_qc_expected = [
        Fraction(4, 7),
        Fraction(1, 7),
        Fraction(2, 7),
    ]
    terminal_qc_doubling_exact = all(
        (terminal_cycle_qc[(i + 1) % 3] - 2 * terminal_cycle_qc[i]).denominator
        == 1
        for i in range(3)
    )

    state_generator_equivariance_residual = max(
        float(
            np.max(
                np.abs(
                    selector_orbit[(r + 1) % 3]
                    - np.real(P_family)
                    @ selector_orbit[r]
                    @ np.real(P_family).T
                )
            )
        )
        for r in range(3)
    )

    # Prospectively frozen Appendix-AJ signed-geometric SU(3) step candidate.
    # Branch symbol controls only the exact signed scalar; stopping-depth C3
    # state controls the orbit axis.
    candidate_sigma = {
        "E": -ell_E_exact,
        "O": ell_O_exact,
    }

    def exp_minus_i_hermitian(H: np.ndarray) -> np.ndarray:
        vals, vecs = np.linalg.eigh(H)
        return vecs @ np.diag(np.exp(-1j * vals)) @ vecs.conj().T

    candidate_step = {}
    candidate_hermiticity_residual = 0.0
    candidate_trace_residual = 0.0
    candidate_unitarity_residual = 0.0
    candidate_determinant_residual = 0.0
    for branch in ("E", "O"):
        for r in range(3):
            K = candidate_sigma[branch] * selector_orbit[r]
            U = exp_minus_i_hermitian(K)
            candidate_step[(branch, r)] = {"K": K, "U": U}
            candidate_hermiticity_residual = max(
                candidate_hermiticity_residual,
                float(np.max(np.abs(K - K.conj().T))),
            )
            candidate_trace_residual = max(
                candidate_trace_residual,
                float(abs(np.trace(K))),
            )
            candidate_unitarity_residual = max(
                candidate_unitarity_residual,
                float(np.max(np.abs(U.conj().T @ U - np.eye(3)))),
            )
            candidate_determinant_residual = max(
                candidate_determinant_residual,
                float(abs(np.linalg.det(U) - 1.0)),
            )

    # Cartan embedding Phi(g SO(3)) = g g^T for SU(3)/SO(3).
    g_cartan_test = candidate_step[("O", 0)]["U"] @ candidate_step[("E", 1)]["U"]
    S_cartan_test = g_cartan_test @ g_cartan_test.T
    cartan_embedding_symmetry_residual = float(
        np.max(np.abs(S_cartan_test.T - S_cartan_test))
    )
    cartan_embedding_unitarity_residual = float(
        np.max(
            np.abs(
                S_cartan_test.conj().T @ S_cartan_test - np.eye(3)
            )
        )
    )
    cartan_embedding_determinant_residual = float(
        abs(np.linalg.det(S_cartan_test) - 1.0)
    )

    # Right SO(3) action leaves gg^T invariant.
    k_angle = 0.417
    k_so3 = np.array(
        [
            [math.cos(k_angle), -math.sin(k_angle), 0.0],
            [math.sin(k_angle), math.cos(k_angle), 0.0],
            [0.0, 0.0, 1.0],
        ],
        dtype=complex,
    )
    cartan_embedding_right_so3_residual = float(
        np.max(
            np.abs(
                (g_cartan_test @ k_so3)
                @ (g_cartan_test @ k_so3).T
                - S_cartan_test
            )
        )
    )
    cartan_embedding_k_unitarity_residual = float(
        np.max(np.abs(k_so3.conj().T @ k_so3 - np.eye(3)))
    )
    cartan_embedding_k_det_residual = abs(np.linalg.det(k_so3) - 1.0)


    # Same branch counts but reversed branch order on the same two consecutive
    # C3 edges must remain distinguishable.
    candidate_two_step_order_separations = []
    for r in range(3):
        U_EO = (
            candidate_step[("O", (r + 1) % 3)]["U"]
            @ candidate_step[("E", r)]["U"]
        )
        U_OE = (
            candidate_step[("E", (r + 1) % 3)]["U"]
            @ candidate_step[("O", r)]["U"]
        )
        candidate_two_step_order_separations.append(
            float(np.max(np.abs(U_EO - U_OE)))
        )

    # Every three consecutive C3 axes contain the full Stage-66 orbit, so any
    # nonzero E/O signed-scalar sequence across a three-step window has full
    # su(3)_F Lie accessibility.
    candidate_three_step_dims = {}
    candidate_three_step_residuals = {}
    for r0 in range(3):
        for word_tuple in itertools.product(("E", "O"), repeat=3):
            key = f"{r0}:" + "".join(word_tuple)
            Hs = [
                candidate_sigma[word_tuple[j]]
                * selector_orbit[(r0 + j) % 3]
                for j in range(3)
            ]
            dim3, res3 = lie_closure_dimension(Hs)
            candidate_three_step_dims[key] = dim3
            candidate_three_step_residuals[key] = res3

    # Prospectively frozen Appendix-AM common-target family path-holonomy
    # candidate.  Each exact Stage-48 path is propagated with the already
    # frozen Appendix-AJ state-dependent step.  W^F_ij = G_i^dagger G_j
    # follows the generic W_ij convention (map j-frame -> i-frame).
    common_target = 35
    common_target_seeds = [15, 35, 143]
    expected_common_target_lengths = [4, 0, 90]
    common_target_paths = {}
    common_target_propagators = {}
    common_target_path_unitarity_residual = 0.0
    common_target_path_determinant_residual = 0.0
    common_target_final_frame_residual = 0

    for seed, expected_len in zip(
        common_target_seeds, expected_common_target_lengths
    ):
        x = seed
        states = []
        branches = []
        frames = []
        G = np.eye(3, dtype=complex)
        for _ in range(10000):
            if x == common_target:
                break
            branch = "E" if x % 2 == 0 else "O"
            r = (-collatz_depth_to_one(x)) % 3
            states.append(x)
            branches.append(branch)
            frames.append(r)
            G = candidate_step[(branch, r)]["U"] @ G
            x = collatz_step(x)
        else:
            raise RuntimeError("common-target Collatz path limit exceeded")

        if len(branches) != expected_len:
            raise RuntimeError(
                f"unexpected path length for {seed}: {len(branches)}"
            )

        final_frame = (-collatz_depth_to_one(x)) % 3
        target_frame = (-collatz_depth_to_one(common_target)) % 3
        common_target_final_frame_residual = max(
            common_target_final_frame_residual,
            abs(final_frame - target_frame),
        )
        common_target_paths[seed] = {
            "states": states,
            "branches": branches,
            "frames": frames,
            "length": len(branches),
            "final": x,
            "final_frame": final_frame,
        }
        common_target_propagators[seed] = G
        common_target_path_unitarity_residual = max(
            common_target_path_unitarity_residual,
            float(np.max(np.abs(G.conj().T @ G - np.eye(3)))),
        )
        common_target_path_determinant_residual = max(
            common_target_path_determinant_residual,
            float(abs(np.linalg.det(G) - 1.0)),
        )

    common_target_W = {}
    common_target_w_unitarity_residual = 0.0
    common_target_w_determinant_residual = 0.0
    common_target_reversal_residual = 0.0
    common_target_composition_residual = 0.0
    common_target_diagonal_residual = 0.0
    for i, seed_i in enumerate(common_target_seeds):
        for j, seed_j in enumerate(common_target_seeds):
            Wij = (
                common_target_propagators[seed_i].conj().T
                @ common_target_propagators[seed_j]
            )
            common_target_W[(i, j)] = Wij
            common_target_w_unitarity_residual = max(
                common_target_w_unitarity_residual,
                float(np.max(np.abs(Wij.conj().T @ Wij - np.eye(3)))),
            )
            common_target_w_determinant_residual = max(
                common_target_w_determinant_residual,
                float(abs(np.linalg.det(Wij) - 1.0)),
            )
            if i == j:
                common_target_diagonal_residual = max(
                    common_target_diagonal_residual,
                    float(np.max(np.abs(Wij - np.eye(3)))),
                )

    for i in range(3):
        for j in range(3):
            common_target_reversal_residual = max(
                common_target_reversal_residual,
                float(
                    np.max(
                        np.abs(
                            common_target_W[(j, i)]
                            - common_target_W[(i, j)].conj().T
                        )
                    )
                ),
            )
            for k in range(3):
                common_target_composition_residual = max(
                    common_target_composition_residual,
                    float(
                        np.max(
                            np.abs(
                                common_target_W[(i, j)]
                                @ common_target_W[(j, k)]
                                - common_target_W[(i, k)]
                            )
                        )
                    ),
                )

    common_target_triangle = (
        common_target_W[(0, 1)]
        @ common_target_W[(1, 2)]
        @ common_target_W[(2, 0)]
    )
    common_target_triangle_residual = float(
        np.max(np.abs(common_target_triangle - np.eye(3)))
    )
    common_target_reverse_triangle = (
        common_target_W[(0, 2)]
        @ common_target_W[(2, 1)]
        @ common_target_W[(1, 0)]
    )
    common_target_reverse_triangle_residual = float(
        np.max(np.abs(common_target_reverse_triangle - np.eye(3)))
    )
    common_target_edge_nontriviality = max(
        float(np.max(np.abs(common_target_W[(0, 1)] - np.eye(3)))),
        float(np.max(np.abs(common_target_W[(1, 2)] - np.eye(3)))),
        float(np.max(np.abs(common_target_W[(0, 2)] - np.eye(3)))),
    )
    common_target_edge_commutator = float(
        np.max(
            np.abs(
                common_target_W[(0, 1)] @ common_target_W[(1, 2)]
                - common_target_W[(1, 2)] @ common_target_W[(0, 1)]
            )
        )
    )

    # Appendix-AO retrospective structural candidate: the actual closed
    # terminal Collatz cycle 1->4->2->1.  Its nontriviality was observed in
    # exploratory dry-run before formalization, so it is explicitly NOT a
    # prospective/blind test.  The repository validator independently
    # reproduces the algebraic result without physical targets.
    terminal_loop_states = [1, 4, 2]
    terminal_loop_branches = [
        "O" if n % 2 else "E" for n in terminal_loop_states
    ]
    terminal_loop_frames = [
        (-collatz_depth_to_one(n)) % 3 for n in terminal_loop_states
    ]
    terminal_loop_next_states = [collatz_step(n) for n in terminal_loop_states]

    U_terminal = np.eye(3, dtype=complex)
    for n, branch, r in zip(
        terminal_loop_states, terminal_loop_branches, terminal_loop_frames
    ):
        U_terminal = candidate_step[(branch, r)]["U"] @ U_terminal

    terminal_loop_unitarity_residual = float(
        np.max(np.abs(U_terminal.conj().T @ U_terminal - np.eye(3)))
    )
    terminal_loop_determinant_residual = float(
        abs(np.linalg.det(U_terminal) - 1.0)
    )
    terminal_loop_nonidentity = float(
        np.max(np.abs(U_terminal - np.eye(3)))
    )
    terminal_loop_trace = complex(np.trace(U_terminal))

    terminal_a = ell_O_exact
    terminal_b = ell_E_exact
    terminal_trace_exact = (
        2.0
        * math.cos(terminal_a / 2.0)
        * math.cos(terminal_b / 2.0)
        + math.cos(terminal_b / 2.0) ** 2
        + 1j
        * math.sin(terminal_a / 2.0)
        * math.sin(terminal_b / 2.0) ** 2
    )
    terminal_trace_formula_residual = abs(
        terminal_loop_trace - terminal_trace_exact
    )
    terminal_trace_imag_exact = (
        math.sin(math.log(3.0) / 2.0)
        * math.sin(math.log(2.0) / 2.0) ** 2
    )
    terminal_trace_imag_residual = abs(
        terminal_loop_trace.imag - terminal_trace_imag_exact
    )
    terminal_det_u_minus_i = complex(
        np.linalg.det(U_terminal - np.eye(3))
    )
    terminal_spin1_unit_eigenvalue_exclusion = abs(
        terminal_det_u_minus_i
    )
    terminal_trace_det_identity_residual = abs(
        terminal_det_u_minus_i - 2.0j * terminal_loop_trace.imag
    )

    # Conjugacy-class invariants under a nontrivial F3 basis change.
    U_terminal_gauge = F3.conj().T @ U_terminal @ F3
    terminal_gauge_trace_residual = abs(
        np.trace(U_terminal_gauge) - np.trace(U_terminal)
    )
    terminal_gauge_trace2_residual = abs(
        np.trace(U_terminal_gauge @ U_terminal_gauge)
        - np.trace(U_terminal @ U_terminal)
    )
    terminal_gauge_det_residual = abs(
        np.linalg.det(U_terminal_gauge) - np.linalg.det(U_terminal)
    )
    terminal_charpoly_residual = float(
        np.max(np.abs(np.poly(U_terminal_gauge) - np.poly(U_terminal)))
    )
    terminal_loop_eigenvalues = np.linalg.eigvals(U_terminal)
    terminal_loop_eigenphases = sorted(
        float(np.angle(z)) for z in terminal_loop_eigenvalues
    )

    # Appendix-AR: basepoint covariance and orientation reversal on the
    # terminal Collatz cycle.  Step matrices follow the source path
    # 1 --O--> 4 --E--> 2 --E--> 1.
    U_1_to_4 = candidate_step[("O", 0)]["U"]
    U_4_to_2 = candidate_step[("E", 1)]["U"]
    U_2_to_1 = candidate_step[("E", 2)]["U"]

    U_terminal_base1 = U_2_to_1 @ U_4_to_2 @ U_1_to_4
    U_terminal_base4 = U_1_to_4 @ U_2_to_1 @ U_4_to_2
    U_terminal_base2 = U_4_to_2 @ U_1_to_4 @ U_2_to_1

    terminal_base1_match_residual = float(
        np.max(np.abs(U_terminal_base1 - U_terminal))
    )
    terminal_base4_conjugacy_residual = float(
        np.max(
            np.abs(
                U_terminal_base4
                - U_1_to_4 @ U_terminal_base1 @ U_1_to_4.conj().T
            )
        )
    )
    U_1_to_2 = U_4_to_2 @ U_1_to_4
    terminal_base2_conjugacy_residual = float(
        np.max(
            np.abs(
                U_terminal_base2
                - U_1_to_2 @ U_terminal_base1 @ U_1_to_2.conj().T
            )
        )
    )
    terminal_basepoint_trace_residual = max(
        abs(np.trace(U_terminal_base4) - np.trace(U_terminal_base1)),
        abs(np.trace(U_terminal_base2) - np.trace(U_terminal_base1)),
    )
    terminal_basepoint_charpoly_residual = max(
        float(
            np.max(
                np.abs(
                    np.poly(U_terminal_base4) - np.poly(U_terminal_base1)
                )
            )
        ),
        float(
            np.max(
                np.abs(
                    np.poly(U_terminal_base2) - np.poly(U_terminal_base1)
                )
            )
        ),
    )

    U_terminal_reverse = U_terminal_base1.conj().T
    terminal_reverse_inverse_residual = float(
        np.max(
            np.abs(
                U_terminal_reverse @ U_terminal_base1 - np.eye(3)
            )
        )
    )
    terminal_reverse_trace_conjugacy_residual = abs(
        np.trace(U_terminal_reverse) - np.conj(np.trace(U_terminal_base1))
    )
    terminal_orientation_odd_imag_sum_residual = abs(
        np.trace(U_terminal_reverse).imag + np.trace(U_terminal_base1).imag
    )
    terminal_orientation_even_real_diff_residual = abs(
        np.trace(U_terminal_reverse).real - np.trace(U_terminal_base1).real
    )
    terminal_orientation_odd_witness = float(np.trace(U_terminal_base1).imag)
    terminal_inverse_trace_gap = abs(
        np.trace(U_terminal_base1) - np.trace(U_terminal_reverse)
    )
    terminal_inverse_trace_gap_identity_residual = abs(
        terminal_inverse_trace_gap
        - 2.0 * abs(terminal_orientation_odd_witness)
    )

    U_terminal_conjugate = np.conj(U_terminal_base1)
    terminal_complex_conjugation_involution_residual = float(
        np.max(np.abs(np.conj(U_terminal_conjugate) - U_terminal_base1))
    )
    terminal_conjugate_unitarity_residual = float(
        np.max(
            np.abs(
                U_terminal_conjugate.conj().T
                @ U_terminal_conjugate
                - np.eye(3)
            )
        )
    )
    terminal_conjugate_determinant_residual = float(
        abs(np.linalg.det(U_terminal_conjugate) - 1.0)
    )
    terminal_conjugate_trace_residual = abs(
        np.trace(U_terminal_conjugate) - np.conj(np.trace(U_terminal_base1))
    )
    terminal_conjugate_vs_inverse_charpoly_residual = float(
        np.max(
            np.abs(
                np.poly(U_terminal_conjugate)
                - np.poly(U_terminal_reverse)
            )
        )
    )
    terminal_outer_class_trace_separation = abs(
        np.trace(U_terminal_conjugate) - np.trace(U_terminal_base1)
    )
    terminal_outer_class_trace_separation_identity_residual = abs(
        terminal_outer_class_trace_separation
        - 2.0 * abs(terminal_orientation_odd_witness)
    )

    # SU(3) conjugacy classes are completely determined by t=tr(U):
    # p_U(lambda)=lambda^3-t lambda^2+conj(t) lambda-1.
    terminal_trace_class_poly_expected = np.array(
        [
            1.0 + 0.0j,
            -terminal_loop_trace,
            np.conj(terminal_loop_trace),
            -1.0 + 0.0j,
        ],
        dtype=complex,
    )
    terminal_trace_class_poly_residual = float(
        np.max(
            np.abs(
                np.poly(U_terminal)
                - terminal_trace_class_poly_expected
            )
        )
    )

    # Outer complex conjugation/inversion acts on class coordinate as
    # t -> conj(t). Its fixed locus is the real interval [-1,3].
    terminal_trace_fixed_locus_distance = abs(terminal_loop_trace.imag)
    terminal_trace_real_in_fixed_interval = (
        -1.0 - TOL <= terminal_loop_trace.real <= 3.0 + TOL
    )
    terminal_outer_orbit_size = (
        2 if terminal_trace_fixed_locus_distance > 1.0e-6 else 1
    )
    terminal_reverse_trace_halfplane_residual = abs(
        np.trace(U_terminal_reverse).imag + terminal_loop_trace.imag
    )

    # Boundary of the SU(3) trace image (deltoid):
    # z(theta)=2 e^{i theta}+e^{-2 i theta}.  Conjugation is theta->-theta.
    deltoid_theta = np.linspace(0.0, 2.0 * math.pi, 721)
    deltoid_boundary = (
        2.0 * np.exp(1j * deltoid_theta)
        + np.exp(-2j * deltoid_theta)
    )
    deltoid_conjugation_residual = float(
        np.max(
            np.abs(
                np.conj(deltoid_boundary)
                - (
                    2.0 * np.exp(-1j * deltoid_theta)
                    + np.exp(2j * deltoid_theta)
                )
            )
        )
    )
    deltoid_real_endpoint_residual = max(
        abs((2.0 * np.exp(0.0j) + np.exp(0.0j)) - 3.0),
        abs(
            (
                2.0 * np.exp(1j * math.pi)
                + np.exp(-2j * math.pi)
            )
            + 1.0
        ),
    )

    # For real class coordinate x, the SU(3) characteristic polynomial
    # factors as (lambda-1)(lambda^2+(1-x)lambda+1).
    fixed_test_x = float(terminal_loop_trace.real)
    fixed_poly_coeffs = np.array(
        [1.0, -fixed_test_x, fixed_test_x, -1.0],
        dtype=float,
    )
    fixed_poly_factored = np.polymul(
        np.array([1.0, -1.0]),
        np.array([1.0, 1.0 - fixed_test_x, 1.0]),
    )
    fixed_locus_factorization_residual = float(
        np.max(np.abs(fixed_poly_coeffs - fixed_poly_factored))
    )

    terminal_pairwise_eigenvalue_separations = [
        float(abs(terminal_loop_eigenvalues[i] - terminal_loop_eigenvalues[j]))
        for i in range(3)
        for j in range(i + 1, 3)
    ]
    terminal_min_eigenvalue_separation = min(
        terminal_pairwise_eigenvalue_separations
    )
    terminal_eigenphase_sum = float(sum(terminal_loop_eigenphases))
    terminal_eigenphase_sum_residual = abs(terminal_eigenphase_sum)
    terminal_spectral_discriminant = 1.0
    for i in range(3):
        for j in range(i + 1, 3):
            terminal_spectral_discriminant *= abs(
                terminal_loop_eigenvalues[i] - terminal_loop_eigenvalues[j]
            ) ** 2

    # Single-axis branch-map no-go.  The Stage-66 selected tangent is the
    # P3 image of A_seed, i.e. the symmetric 23 channel.  Any two branch
    # generators that are merely scalar multiples of this one tangent commute,
    # so their exponentials cannot preserve E/O word order.
    selector_T23 = selector_orbit[1]
    single_axis_E_generator = ell_E_exact * selector_T23
    single_axis_O_generator = ell_O_exact * selector_T23
    single_axis_generator_commutator = float(
        np.max(
            np.abs(
                single_axis_E_generator @ single_axis_O_generator
                - single_axis_O_generator @ single_axis_E_generator
            )
        )
    )
    mobius_branch_noncommutativity = float(
        np.max(np.abs(ME @ MO - MO @ ME))
    )

    # Minimal two-generator D/C branch-map ambiguity.
    # Assignment A: E->D, O->C. Assignment B: E->C, O->D.
    # Both retain noncommutativity; their Lie commutators are opposite.
    dc_branch_A_E = ell_E_exact * D_family
    dc_branch_A_O = ell_O_exact * C_family
    dc_branch_B_E = ell_E_exact * C_family
    dc_branch_B_O = ell_O_exact * D_family
    dc_comm_A = dc_branch_A_E @ dc_branch_A_O - dc_branch_A_O @ dc_branch_A_E
    dc_comm_B = dc_branch_B_E @ dc_branch_B_O - dc_branch_B_O @ dc_branch_B_E
    dc_comm_A_norm = float(np.max(np.abs(dc_comm_A)))
    dc_comm_B_norm = float(np.max(np.abs(dc_comm_B)))
    dc_branch_swap_sign_residual = float(np.max(np.abs(dc_comm_A + dc_comm_B)))

    # Conditional overlap-realization theorem for family plaquette phase.
    # If W_ij=<u_i|d_j>, the rephasing-invariant plaquette is exactly the
    # Bargmann/Pancharatnam quadrilateral phase.
    u_overlap = [
        np.array([1.0, 0.0, 0.0], dtype=complex),
        np.array([1.0, 1.0j, 0.0], dtype=complex) / math.sqrt(2.0),
        np.array([1.0, 0.0, 1.0], dtype=complex) / math.sqrt(2.0),
    ]
    d_overlap = [
        np.array([1.0, 1.0, 0.0], dtype=complex) / math.sqrt(2.0),
        np.array([1.0, 0.0, 1.0j], dtype=complex) / math.sqrt(2.0),
        np.array([0.0, 1.0, 1.0], dtype=complex) / math.sqrt(2.0),
    ]
    W_overlap = np.array(
        [[np.vdot(u, d) for d in d_overlap] for u in u_overlap],
        dtype=complex,
    )

    i0, k0, j0, l0 = 0, 1, 0, 1
    plaquette_overlap = (
        W_overlap[i0, j0]
        * np.conj(W_overlap[k0, j0])
        * W_overlap[k0, l0]
        * np.conj(W_overlap[i0, l0])
    )
    bargmann_quad = (
        np.vdot(u_overlap[i0], d_overlap[j0])
        * np.vdot(d_overlap[j0], u_overlap[k0])
        * np.vdot(u_overlap[k0], d_overlap[l0])
        * np.vdot(d_overlap[l0], u_overlap[i0])
    )
    overlap_bargmann_identity_residual = abs(
        plaquette_overlap - bargmann_quad
    )
    overlap_bargmann_phase = math.atan2(
        float(np.imag(bargmann_quad)),
        float(np.real(bargmann_quad)),
    )

    # Explicit ray-gauge invariance: independent phase changes of u_i,d_j.
    u_gauge = [
        np.exp(1j * t) * u
        for t, u in zip((0.13, -0.41, 0.77), u_overlap)
    ]
    d_gauge = [
        np.exp(1j * t) * d
        for t, d in zip((-0.22, 0.51, -0.63), d_overlap)
    ]
    W_gauge = np.array(
        [[np.vdot(u, d) for d in d_gauge] for u in u_gauge],
        dtype=complex,
    )
    plaquette_gauge = (
        W_gauge[i0, j0]
        * np.conj(W_gauge[k0, j0])
        * W_gauge[k0, l0]
        * np.conj(W_gauge[i0, l0])
    )
    overlap_bargmann_gauge_residual = abs(
        plaquette_gauge - plaquette_overlap
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
        "legacy_generated_csv_pinned_blob_state_matches_audit": (
            archive_projection_csv_blob == "3ec7331cbb859d8d955c9d7d5d1bd67ef75e8fb1"
            and archive_projection_csv_tree_blob
            == "3ec7331cbb859d8d955c9d7d5d1bd67ef75e8fb1"
            and archive_projection_csv_worktree_matches_object
            and archive_csv_up_quark_particle_ids
            in (["nu_L", "nu_R"], ["u_L", "u_R"])
            and (
                (
                    archive_csv_up_quark_particle_ids == ["nu_L", "nu_R"]
                    and archive_csv_state == "STALE_UP_QUARK_PARTICLE_ID"
                )
                or (
                    archive_csv_up_quark_particle_ids == ["u_L", "u_R"]
                    and archive_csv_state == "CORRECTED_UP_QUARK_PARTICLE_ID"
                )
            )
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
        "collatz_fs_relational_phase_interface_parent_present": (
            "MATHEMATICAL_INTERFACE_ADDED / PHYSICAL_BINDING_OPEN"
            in collatz_fs_phase_interface
            and "\\zeta_C(Cn)=\\zeta_C(n)^2" in collatz_fs_phase_interface
            and "R_{ij}" in collatz_fs_phase_interface
            and "\\zeta_{ij}=e^{i\\phi_{ij}}" in collatz_fs_phase_interface
        ),
        "scalar_qc_difference_phase_has_zero_all_plaquettes_exact": (
            qc_all_plaquette_turns_zero
        ),
        "scalar_qc_difference_phase_is_pure_vertex_coboundary": (
            qc_pair_phase_antisymmetric
            and qc_pair_phase_diagonal_zero
        ),
        "hexahedral_bloch_parent_has_nonzero_bargmann_triangle": (
            "Berry/Bargmann face invariants" in hexahedral_bloch
            and "|\\gamma_{B,\\rm oct}|=\\frac{\\Omega_{\\rm oct}}2=\\frac\\pi4"
            in hexahedral_bloch
            and "\\langle +x|+y\\rangle" in hexahedral_bloch
        ),
        "overlap_plaquette_equals_bargmann_quadrilateral_exact": (
            overlap_bargmann_identity_residual < TOL
        ),
        "overlap_bargmann_quadrilateral_is_ray_gauge_invariant": (
            overlap_bargmann_gauge_residual < TOL
        ),
        "generic_overlap_realization_can_have_nonzero_bargmann_phase": (
            abs(overlap_bargmann_phase) > TOL
        ),
        "gremlin_xfi02_is_candidate_only_not_promoted_parent": (
            "XFI.02" in gremlin_overlay
            and "EXACT_CONDITIONAL" in gremlin_overlay
            and "CANDIDATE_ONLY / CHYBA / NON_CANONICAL_OVERLAY" in gremlin_overlay
        ),
        "active_qc_equatorial_bargmann_turn_sum_zero_exact": (
            qc_bargmann_turn_sum == 0
        ),
        "active_qc_equatorial_pair_distances_below_half_turn": (
            qc_pair_distances_lt_half
        ),
        "active_qc_equatorial_bargmann_phase_zero": (
            qc_bargmann_imag_residual < TOL
            and qc_bargmann_real > 0.0
            and abs(qc_bargmann_phase) < TOL
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
        "stage35_real_family_pair_cp_boundary_present": (
            "STAGE_35_HERMITIAN_FAMILY_PAIR_PASS_WITH_INPUT_PROVENANCE_AND_CP_BOUNDARY"
            in stage35
            and "CP from real cross-Gram: J = 0" in stage35
            and "BLOCKED_PENDING_CLEAN_COMPLEX_TIR_NATIVE_SECTOR_OPERATOR" in stage35
        ),
        "stage36_complex_holonomy_cp_mechanism_pass_quarantine_present": (
            "STAGE_36_COMPLEX_HOLONOMY_CP_MECHANISM_PASS__SOURCE_PROMOTION_QUARANTINED"
            in stage36
            and "W^{\\mathbb C}_{ij}=a_{ij}e^{i\\phi_{ij}}" in stage36
            and "4.270454683508035" in stage36
        ),
        "stage36_complex_holonomy_status_tokens_present": (
            "complex-holonomy CP mechanism: PASS" in stage36
            and "non-zero J_F: PASS" in stage36
            and "physical promotion: QUARANTINED BY SOURCE PROVENANCE" in stage36
        ),
        "stage37_common_family_axis_nogo_present": (
            "STAGE_37_COMMON_FAMILY_AXIS_NOGO_PASS" in stage37
        ),
        "stage38_c3_cp_parent_pass_present": (
            "STAGE_38_C3_CHARACTER_BASIS_CP_MATH_PASS" in stage38
        ),
        "stage33_endpoint_ratios_parent_pass_present": (
            stage33_receipt.get("status") == "PASS"
            and stage33_receipt.get("ratios", {}).get("a") == "2/7"
            and stage33_receipt.get("ratios", {}).get("b") == "2/9"
            and stage33_receipt.get("CKM_reference_used_for_reconstruction") is False
            and stage33_receipt.get("mass_reference_used") is False
        ),
        "stage39_two_operator_candidate_frozen_present": (
            "STAGE_39_STRUCTURAL_CANDIDATE_FROZEN" in stage39
            and "H(\\alpha)=D+\\alpha C" in stage39
            and "No observed CKM entries, observed masses, or fitted coefficients"
            in stage39
        ),
        "stage39_two_sector_frames_noncommuting": (
            stage39_A["commutator_max_abs"] > 1.0e-9
            and stage39_B["commutator_max_abs"] > 1.0e-9
        ),
        "stage39_relative_transformations_are_su3": (
            stage39_A["unitarity_residual"] < TOL
            and stage39_B["unitarity_residual"] < TOL
            and stage39_A["determinant_residual"] < TOL
            and stage39_B["determinant_residual"] < TOL
        ),
        "stage39_nonzero_cp_reproduced_without_target_fit": (
            stage39_J_A_abs_residual < 1.0e-12
            and stage39_J_B_abs_residual < 1.0e-12
        ),
        "stage39_assignment_swap_flips_cp_orientation": (
            stage39_J_sign_flip_residual < 1.0e-12
            and stage39_abs_transpose_residual < 1.0e-12
        ),
        "stage39_explicitly_retains_both_assignments_without_target_selection": (
            "Both sector assignments are retained" in stage39
            and "No assignment is selected by comparison to a target matrix."
            in stage39
        ),
        "coefficient_orientation_theorem_does_not_define_stage39_alpha_assignment": (
            "EXACT_ROLE_AND_SIGN_FORCING_THEOREM_CANDIDATE"
            in coefficient_orientation
            and "alpha_u" not in coefficient_orientation
            and "alpha_d" not in coefficient_orientation
            and "R_a\\leftrightarrow a" in coefficient_orientation
            and "R_b\\leftrightarrow b" in coefficient_orientation
            and "R_c\\leftrightarrow c" in coefficient_orientation
        ),
        "qc_bc_orientation_binding_remains_open_not_sector_assignment": (
            "q_phase_to_b_c_orientation_binding = OPEN" in cocycle_phase
            and "fixed_linear_q_to_Z4_coefficient_map = IMPOSSIBLE"
            in cocycle_phase
        ),
        "sm_ledger_declares_full_ckm_holonomic_orientation_binding_as_next_closure": (
            "bind the full CKM matrix to the same coefficient-free holonomic/orientation forcing theorem"
            in sm_reconciliation
        ),
        "generic_wij_path_holonomy_grammar_current": (
            "W_{ij}^{(G,R)}" in wij_crosswalk
            and "\\mathcal P\\exp" in wij_crosswalk
            and "W_{ji}=W_{ij}^{-1}=W_{ij}^{\\dagger}" in wij_crosswalk
            and "W_{ij}\\mapsto G_iW_{ij}G_j^{-1}" in wij_crosswalk
        ),
        "wij_crosswalk_explicit_current_instances_are_wt_spatial_color": (
            "W_{ij}^{WT}" in wij_crosswalk
            and "W_{ij}^{X}" in wij_crosswalk
            and "W_{ij}^{c}" in wij_crosswalk
            and "SU(3)_F" not in wij_crosswalk
        ),
        "endpoint_su3_abelianization_selector_nogo_parent_present": (
            "endpoint_SU3_homomorphism_to_nonzero_Z4_selector = IMPOSSIBLE_BY_STANDARD_PERFECT_GROUP_THEOREM"
            in cocycle_phase
            and "path-local cochain" in cocycle_phase
        ),
        "stage40_does_not_select_assignment_by_fit": (
            "No assignment is selected by fit." in stage40
        ),
        "stage40_full_ckm_shape_fail_mechanism_retained_present": (
            "STAGE_40_FULL_CKM_SHAPE_FAIL__MECHANISM_RETAINED" in stage40
            and "No assignment is selected by fit." in stage40
            and "without observable-specific correction factors" in stage40
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
        "sl2r_killing_form_signature_is_noncompact_2_1": (
            sl2_killing_positive == 2
            and sl2_killing_negative == 1
            and sl2_killing_zero == 0
        ),
        "stage52_uses_shared_complexification_not_direct_real_homomorphism": (
            "same complexification" in stage52
            and "change of real form" in stage52
            and "not a change of basis inside the original real representation"
            in stage52
        ),
        "dc_unitary_conjugacy_spectrum_exact": (
            dc_spectral_eigen_residual < TOL
        ),
        "dc_unitary_conjugacy_trace_powers_exact": (
            dc_trace_power_residual < TOL
        ),
        "dc_unitary_conjugacy_frobenius_norm_exact": (
            dc_frobenius_residual < TOL
        ),
        "stage52_compact_real_form_selection_explicitly_open": (
            "STAGE_52_COMPACT_REAL_FORM_SYM2_BRIDGE_PASS_SELECTION_OPEN"
            in stage52
            and "does not yet contain a derived rule selecting the compact real form"
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
        "stage55_dc_projectors_reconstruct_exactly": (
            D0_stage55_reconstruction_residual < TOL
            and C0_stage55_reconstruction_residual < TOL
        ),
        "stage55_dc_projected_norm_formulas_reproduced": (
            stage55_dc_norm_formula_residual < TOL
        ),
        "D0_has_nonzero_stage55_complement_component": (
            D0_p_norm2 > TOL
        ),
        "C0_has_nonzero_stage55_complement_component": (
            C0_p_norm2 > TOL
        ),
        "stage52_compact_spin1_subgroup_alone_cannot_generate_dc_pair": (
            D0_p_norm2 > TOL
            and C0_p_norm2 > TOL
            and "Sym^2(SU(2))" in stage52
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
        "stage24_oriented_c3_and_stage66_negative_mode_select_directed_23_tangent": (
            "P_s|s_2\\rangle=|s_3\\rangle" in stage24
            and selector_negative_best_orbit_index == 1
            and abs(selector_negative_best_alignment - 1.0) < 1.0e-10
        ),
        "stage66_each_c3_orbit_pair_closes_only_three_dimensional_subalgebra": (
            selector_pair_dims == {"01": 3, "12": 3, "20": 3}
        ),
        "stage66_full_c3_orbit_generates_su3f_dimension_eight": (
            selector_orbit_lie_dim == 8
            and selector_orbit_lie_residual < 1.0e-10
        ),
        "stage66_c3_orbit_has_exact_mixed_kp_projection_pattern": (
            selector_orbit_kp_residual < TOL
            and selector_orbit_kp_reconstruction_residual < TOL
        ),
        "stage24_66_forward_A1_A2_pair_noncommutes": (
            selector_forward_commutator_max > TOL
            and abs(selector_forward_commutator_norm2 - 0.125) < TOL
        ),
        "stage24_66_forward_successor_A2_is_pure_complement": (
            selector_orbit_kp[2]["k_norm2"] < TOL
            and abs(selector_orbit_kp[2]["p_norm2"] - 0.5) < TOL
        ),
        "collatz_stopping_depth_mod3_advances_exact_temporal_c3_frame": (
            len(collatz_c3_failures) == 0
            and sum(collatz_c3_frame_counts) == collatz_c3_tested
        ),
        "terminal_collatz_cycle_maps_to_ordered_c3_frames": (
            terminal_cycle_states == [1, 4, 2]
            and terminal_cycle_depths == [0, 2, 1]
            and terminal_cycle_frames == [0, 1, 2]
        ),
        "terminal_qc_phase_cycle_matches_collatz_c3_orientation": (
            terminal_cycle_qc == terminal_cycle_qc_expected
            and terminal_qc_doubling_exact
        ),
        "collatz_state_selected_stage66_generator_is_c3_equivariant": (
            state_generator_equivariance_residual < TOL
        ),
        "appendix_aj_candidate_freeze_precedes_validation": (
            "STATE_DEPENDENT_SIGNED_GEOMETRIC_SU3_STEP_CANDIDATE_FROZEN_PREVALIDATION"
            in idt_c3_crosswalk_doc
            and "No observed CKM, PMNS, mass, PDG, or fitted coefficient"
            in idt_c3_crosswalk_doc
        ),
        "signed_geometric_candidate_generators_are_hermitian_traceless": (
            candidate_hermiticity_residual < TOL
            and candidate_trace_residual < TOL
        ),
        "signed_geometric_candidate_steps_are_su3": (
            candidate_unitarity_residual < TOL
            and candidate_determinant_residual < TOL
        ),
        "signed_geometric_candidate_distinguishes_EO_from_OE_equal_counts": (
            min(candidate_two_step_order_separations) > TOL
        ),
        "every_three_step_c3_window_has_full_su3f_lie_access": (
            set(candidate_three_step_dims.values()) == {8}
            and max(candidate_three_step_residuals.values()) < 1.0e-10
        ),
        "appendix_am_candidate_freeze_precedes_validation": (
            "COMMON_TARGET_FAMILY_PATH_HOLONOMY_CANDIDATE_FROZEN_PREVALIDATION"
            in idt_c3_crosswalk_doc
            and "If the triangular Wilson product is identity" in idt_c3_crosswalk_doc
        ),
        "common_target_paths_match_stage47_48_lengths_and_target": (
            [common_target_paths[s]["length"] for s in common_target_seeds]
            == expected_common_target_lengths
            and all(
                common_target_paths[s]["final"] == common_target
                for s in common_target_seeds
            )
            and common_target_final_frame_residual == 0
        ),
        "common_target_path_propagators_are_su3": (
            common_target_path_unitarity_residual < TOL
            and common_target_path_determinant_residual < TOL
        ),
        "common_target_pairwise_transports_are_su3": (
            common_target_w_unitarity_residual < TOL
            and common_target_w_determinant_residual < TOL
            and common_target_diagonal_residual < TOL
        ),
        "common_target_pairwise_transport_reversal_exact": (
            common_target_reversal_residual < TOL
        ),
        "common_target_pairwise_transport_composition_exact": (
            common_target_composition_residual < TOL
        ),
        "common_target_triangle_wilson_loop_is_identity": (
            common_target_triangle_residual < TOL
            and common_target_reverse_triangle_residual < TOL
        ),
        "common_target_transport_edges_are_nontrivial_despite_flat_loop": (
            common_target_edge_nontriviality > TOL
        ),
        "appendix_ao_retrospective_status_disclosed_before_repository_validation": (
            "RETROSPECTIVE_STRUCTURAL_CANDIDATE_NOT_PROSPECTIVE_TEST"
            in idt_c3_crosswalk_doc
            and "exploratory dry-run before this Appendix was formalized"
            in idt_c3_crosswalk_doc
        ),
        "terminal_collatz_cycle_states_frames_and_branches_exact": (
            terminal_loop_states == [1, 4, 2]
            and terminal_loop_next_states == [4, 2, 1]
            and terminal_loop_frames == [0, 1, 2]
            and terminal_loop_branches == ["O", "E", "E"]
        ),
        "terminal_collatz_cycle_step_product_is_su3": (
            terminal_loop_unitarity_residual < TOL
            and terminal_loop_determinant_residual < TOL
        ),
        "terminal_collatz_cycle_holonomy_is_nonidentity": (
            terminal_loop_nonidentity > 1.0e-6
        ),
        "terminal_collatz_cycle_trace_formula_exact": (
            terminal_trace_formula_residual < TOL
            and terminal_trace_imag_residual < TOL
        ),
        "terminal_collatz_cycle_trace_has_strictly_nonzero_imaginary_part": (
            terminal_loop_trace.imag > 1.0e-6
            and terminal_trace_imag_exact > 1.0e-6
        ),
        "terminal_collatz_cycle_has_no_spin1_forced_unit_eigenvalue": (
            terminal_spin1_unit_eigenvalue_exclusion > 1.0e-6
        ),
        "terminal_collatz_cycle_outside_every_conjugate_spin1_su2_subgroup": (
            terminal_loop_trace.imag > 1.0e-6
            and terminal_spin1_unit_eigenvalue_exclusion > 1.0e-6
            and "STAGE_53_SPIN1_CP_NOGO_AND_SU3_3PLUS5_DECOMPOSITION_PASS"
            in stage53
        ),
        "terminal_loop_basepoint_change_is_conjugacy_exact": (
            terminal_base1_match_residual < TOL
            and terminal_base4_conjugacy_residual < TOL
            and terminal_base2_conjugacy_residual < TOL
            and terminal_basepoint_trace_residual < TOL
            and terminal_basepoint_charpoly_residual < 1.0e-12
        ),
        "terminal_loop_reverse_orientation_is_inverse_exact": (
            terminal_reverse_inverse_residual < TOL
            and terminal_reverse_trace_conjugacy_residual < TOL
        ),
        "terminal_loop_imaginary_trace_is_orientation_odd": (
            abs(terminal_orientation_odd_witness) > 1.0e-6
            and terminal_orientation_odd_imag_sum_residual < TOL
            and terminal_orientation_even_real_diff_residual < TOL
        ),
        "su3_det_u_minus_i_equals_two_i_im_trace": (
            terminal_trace_det_identity_residual < 1.0e-12
        ),
        "terminal_loop_and_inverse_have_distinct_traces": (
            terminal_inverse_trace_gap > 1.0e-6
            and terminal_inverse_trace_gap_identity_residual < 1.0e-12
        ),
        "terminal_orientation_reversal_not_inner_conjugate_in_su3": (
            terminal_inverse_trace_gap > 1.0e-6
            and terminal_trace_det_identity_residual < 1.0e-12
        ),
        "terminal_complex_conjugation_is_involutive_su3_map": (
            terminal_complex_conjugation_involution_residual < TOL
            and terminal_conjugate_unitarity_residual < TOL
            and terminal_conjugate_determinant_residual < TOL
        ),
        "terminal_complex_conjugate_has_conjugate_trace": (
            terminal_conjugate_trace_residual < TOL
        ),
        "terminal_complex_conjugate_and_reverse_share_conjugacy_class": (
            terminal_conjugate_vs_inverse_charpoly_residual < 1.0e-12
        ),
        "terminal_forward_and_outer_conjugate_classes_are_distinct": (
            terminal_outer_class_trace_separation > 1.0e-6
            and terminal_outer_class_trace_separation_identity_residual
            < 1.0e-12
        ),
        "su3_conjugacy_class_characteristic_polynomial_determined_by_trace": (
            terminal_trace_class_poly_residual < 1.0e-12
        ),
        "su3_outer_involution_fixed_locus_real_polynomial_factorization_exact": (
            fixed_locus_factorization_residual < TOL
        ),
        "su3_trace_deltoid_boundary_is_conjugation_symmetric": (
            deltoid_conjugation_residual < TOL
            and deltoid_real_endpoint_residual < TOL
        ),
        "terminal_class_lies_off_outer_fixed_locus": (
            terminal_trace_fixed_locus_distance > 1.0e-6
            and terminal_outer_orbit_size == 2
            and terminal_trace_real_in_fixed_interval
        ),
        "terminal_forward_reverse_classes_occupy_opposite_trace_halfplanes": (
            terminal_loop_trace.imag > 1.0e-6
            and np.trace(U_terminal_reverse).imag < -1.0e-6
            and terminal_reverse_trace_halfplane_residual < 1.0e-12
        ),
        "outer_fixed_class_locus_matches_unit_eigenvalue_locus": (
            terminal_trace_det_identity_residual < 1.0e-12
        ),
        "stage55_identifies_spin1_image_with_so3_symmetric_pair": (
            "SU(2)/\\mathbb Z_2\\cong SO(3)" in stage55
            and "(\\mathfrak{su}(3),\\mathfrak{so}(3))" in stage55
            and "SU(3)/SO(3)" in stage55
        ),
        "outer_fixed_class_locus_matches_conjugate_spin1_so3_class_locus": (
            terminal_trace_det_identity_residual < 1.0e-12
            and "STAGE_55_SU3_SO3_SYMMETRIC_PAIR_PASS" in stage55
        ),
        "terminal_off_fixed_locus_consistent_with_spin1_exclusion": (
            terminal_trace_fixed_locus_distance > 1.0e-6
            and terminal_spin1_unit_eigenvalue_exclusion > 1.0e-6
        ),
        "terminal_loop_has_three_distinct_unitary_eigenvalues": (
            terminal_min_eigenvalue_separation > 1.0e-6
            and terminal_spectral_discriminant > 1.0e-12
        ),
        "terminal_loop_principal_eigenphases_sum_to_zero": (
            terminal_eigenphase_sum_residual < 1.0e-12
        ),
        "terminal_loop_is_regular_rank2_su3_conjugacy_class": (
            terminal_min_eigenvalue_separation > 1.0e-6
            and terminal_loop_determinant_residual < TOL
            and terminal_eigenphase_sum_residual < 1.0e-12
        ),
        "nontrivial_terminal_wilson_loop_refutes_global_coboundary_factorization": (
            terminal_loop_nonidentity > 1.0e-6
            and common_target_triangle_residual < TOL
        ),
        "flat_common_target_and_nonflat_terminal_path_structures_are_distinct": (
            common_target_triangle_residual < TOL
            and terminal_loop_nonidentity > 1.0e-6
            and terminal_loop_trace.imag > 1.0e-6
        ),
        "terminal_collatz_cycle_conjugacy_invariants_gauge_stable": (
            terminal_gauge_trace_residual < TOL
            and terminal_gauge_trace2_residual < TOL
            and terminal_gauge_det_residual < TOL
            and terminal_charpoly_residual < 1.0e-12
        ),
        "single_stage66_axis_branch_generators_commute_exactly": (
            single_axis_generator_commutator < TOL
        ),
        "exact_collatz_mobius_branch_generators_noncommute": (
            mobius_branch_noncommutativity > TOL
        ),
        "single_axis_family_map_cannot_preserve_exact_branch_order": (
            single_axis_generator_commutator < TOL
            and mobius_branch_noncommutativity > TOL
        ),
        "dc_two_generator_assignment_A_noncommutes": (
            dc_comm_A_norm > TOL
        ),
        "dc_two_generator_assignment_B_noncommutes": (
            dc_comm_B_norm > TOL
        ),
        "dc_branch_swap_reverses_lie_commutator_orientation": (
            dc_branch_swap_sign_residual < TOL
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
        "orientation_reflection_is_z2_involution": (
            orientation_reflection_involution_residual < TOL
        ),
        "orientation_reflection_inverts_c3_generator": (
            orientation_inversion_action_residual < TOL
        ),
        "orientation_c3_z2_extension_is_nonabelian": (
            orientation_extension_noncommutativity > TOL
        ),
        "orientation_c3_z2_extension_has_six_distinct_elements": (
            d3_unique_element_count == 6
        ),
        "weak_family_c3_and_weyl_z2_commute": (
            weak_family_commutator_residual < TOL
        ),
        "weak_family_combined_generator_has_exact_order_six": (
            G6_order6_residual < TOL
            and G6_lower_power_nonidentity > TOL
        ),
        "six_state_orientation_reflection_is_involution": (
            R6_involution_residual < TOL
        ),
        "six_state_orientation_reflection_inverts_c6_rotation": (
            D6_inversion_relation_residual < TOL
        ),
        "six_state_dihedral_extension_has_twelve_distinct_elements": (
            D6_unique_element_count == 12
        ),
        "d3_permutation_rep_has_invariant_singlet": (
            d3_singlet_P_residual < TOL
            and d3_singlet_R_residual < TOL
        ),
        "d3_permutation_rep_orthogonal_complement_is_two_dimensional": (
            d3_plane_orthonormal_residual < TOL
            and d3_singlet_plane_residual < TOL
        ),
        "d3_standard_plane_c3_action_is_order3_rotation": (
            d3_plane_rotation_order3_residual < TOL
            and d3_plane_rotation_trace_residual < TOL
            and d3_plane_rotation_det_residual < TOL
        ),
        "d3_standard_plane_z2_action_is_reflection": (
            d3_plane_reflection_involution_residual < TOL
            and d3_plane_reflection_det_residual < TOL
            and d3_plane_dihedral_relation_residual < TOL
        ),
        "f3_trivial_character_is_real_invariant_singlet": (
            f3_trivial_character_residual < TOL
        ),
        "f3_nontrivial_character_pair_complexifies_real_standard_plane": (
            f3_nontrivial_character_conjugacy_residual < TOL
            and f3_character_plane_projector_residual < TOL
        ),
        "su3_so3_cartan_plane_is_two_dimensional_orthonormal_abelian": (
            su3so3_cartan_orthonormal_residual < TOL
            and su3so3_cartan_commutator_residual < TOL
        ),
        "family_standard_plane_intertwines_with_su3_so3_cartan_plane": (
            family_to_cartan_P_intertwiner_residual < TOL
            and family_to_cartan_R_intertwiner_residual < TOL
        ),
        "su3_so3_restricted_roots_form_A2": (
            a2_root_sum_residual < TOL
            and a2_root_norm_residual < TOL
            and a2_cartan_matrix_residual < TOL
        ),
        "su3_so3_restricted_weyl_group_matches_d3_s3_action": (
            d3_unique_element_count == 6
            and d3_plane_dihedral_relation_residual < TOL
            and family_to_cartan_P_intertwiner_residual < TOL
            and family_to_cartan_R_intertwiner_residual < TOL
        ),
        "su3_weyl_alcove_is_equilateral_triangle_exact": (
            alcove_equilateral_residual < TOL
            and alcove_area_residual < TOL
        ),
        "su3_weyl_alcove_vertices_map_to_three_deltoid_cusps": (
            alcove_cusp_residual < TOL
        ),
        "su3_weyl_alcove_edge_maps_to_deltoid_boundary_arc": (
            alcove_edge_deltoid_residual < TOL
        ),
        "su3_trace_is_weyl_D3_S3_invariant_on_rank2_plane": (
            alcove_weyl_trace_residual < TOL
        ),
        "cartan_embedding_image_is_symmetric_unitary_det1": (
            cartan_embedding_symmetry_residual < TOL
            and cartan_embedding_unitarity_residual < TOL
            and cartan_embedding_determinant_residual < TOL
        ),
        "cartan_embedding_is_right_so3_coset_invariant": (
            cartan_embedding_right_so3_residual < TOL
            and cartan_embedding_k_unitarity_residual < TOL
            and cartan_embedding_k_det_residual < TOL
        ),
        "cartan_embedding_rank2_flat_equals_exp_iH": (
            cartan_embedding_flat_exp_residual < TOL
            and cartan_embedding_flat_trace_residual < TOL
        ),
        "tensor_character_basis_diagonalizes_six_state_c6": (
            G6_character_offdiag_residual < TOL
        ),
        "six_state_c6_spectrum_is_all_sixth_roots_once": (
            G6_sixth_root_match_residual < TOL
            and len(unmatched) == 0
        ),
        "six_state_c6_has_two_real_modes_and_two_conjugate_pairs": (
            G6_real_eigenvalue_count == 2
            and G6_nonreal_eigenvalue_count == 4
            and G6_conjugate_pair_residual < TOL
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
        "c3_label_character_overlap_matrix_is_f3": (
            f3_overlap_residual < TOL
        ),
        "f3_plaquette_equals_bargmann_quadrilateral": (
            f3_bargmann_residual < TOL
        ),
        "f3_bargmann_phase_is_two_pi_over_three": (
            f3_bargmann_phase_residual < TOL
        ),
        "f3_jarlskog_is_imaginary_part_of_bargmann_plaquette": (
            f3_plaquette_j_residual < TOL
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
        "continuous_real_lie_lift_status": (
            "NONTRIVIAL_CONTINUOUS_PSL2R_TO_SU3F_LIE_HOMOMORPHIC_LIFT_REFUTED"
            if passed
            else "FAILED"
        ),
        "canonical_polar_compactification_status": (
            "CANONICAL_POLAR_COMPACTIFICATION_REFUTED_AS_SUFFICIENT_BRANCH_LIFT"
            if passed
            else "FAILED"
        ),
        "compact_family_branch_operator_status": (
            "OPEN_DISCRETE_OR_HOLONOMIC_NONPOLAR_BRANCHWISE_SU3F_LIFT"
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
            "CUBIC_SELECTOR_CLOSED__SPLIT_REAL_BRANCH_OPERATOR_CLOSED__GEOMETRIC_RHYTHM_ALPHABET_CLOSED__COMPACT_ENDPOINT_FIXED__POLAR_AND_CONTINUOUS_LIE_LIFTS_REFUTED__SCALAR_QC_CP_REFUTED__C3_F3_BARGMANN_FRAMES_CLOSED__STAGE39_STRUCTURAL_SECTOR_FRAMES_CLOSED_STAGE40_CKM_SHAPE_FAIL__COEFFICIENT_ORIENTATION_NOT_YET_SECTOR_ASSIGNMENT__GENERIC_WIJ_GRAMMAR_CLOSED__STAGE24_PLUS_STAGE66_DIRECTED_23_TANGENT_CLOSED__SINGLE_AXIS_BRANCH_MAP_REFUTED__STAGE66_C3_ORBIT_FULL_SU3F_GENERATOR_SET_CLOSED__STATIC_TWO_AXIS_EO_MAP_REFUTED__COLLATZ_STOPPING_DEPTH_MOD3_TO_C3_ORBIT_INDEX_CLOSED__SIGNED_GEOMETRIC_SU3_STEP_VALIDATED__COMMON_TARGET_WIJ_FLAT__TERMINAL_COLLATZ_NONCOBOUNDARY_NONSEPARABLE_SU3_LOOP_OUTSIDE_SPIN1_RETROSPECTIVE_PASS__PHYSICAL_RHO_TEMPORAL_FAMILY_CP_AND_CKM_PROMOTION_OPEN"
        ),
        "oriented_family_generator_status": (
            "TEMPORAL_ORIENTATION_SELECTS_P3_VS_INVERSE_AT_REPRESENTATION_LEVEL"
            if passed
            else "FAILED"
        ),
        "directed_stationary_family_tangent_status": (
            "STAGE24_ORIENTATION_PLUS_STAGE66_SELECTS_DIRECTED_2_TO_3_TANGENT_AT_REPRESENTATION_LEVEL"
            if passed
            else "FAILED"
        ),
        "ordered_family_step_map_status": (
            "OPEN_COLLATZ_BRANCH_TO_DIRECTED_FAMILY_GENERATOR_AND_EXACT_RHO_BINDING"
        ),
        "single_axis_branch_map_status": (
            "NO_GO_SINGLE_STAGE66_TANGENT_CANNOT_PRESERVE_COLLATZ_BRANCH_ORDER"
            if passed
            else "FAILED"
        ),
        "family_branch_operator_requirement": (
            "AT_LEAST_TWO_NONCOMMUTING_GENERATORS_OR_STATE_DEPENDENT_CONJUGATION_REQUIRED"
        ),
        "minimal_dc_branch_map_status": (
            "TWO_NONCOMMUTING_DC_ASSIGNMENTS_EXIST_WITH_BRANCH_SWAP_SIGN_REVERSAL"
            if passed
            else "FAILED"
        ),
        "branch_generator_assignment_status": (
            "OPEN_Z2_EO_TO_DC_ASSIGNMENT_NOT_SOURCE_SELECTED"
        ),
        "dc_spectral_assignment_status": (
            "NO_GO_SINGLE_GENERATOR_SPECTRAL_INVARIANTS_CANNOT_SELECT_EO_TO_DC_Z2"
            if passed
            else "FAILED"
        ),
        "dc_basis_appearance_status": (
            "DIAGONAL_VS_MIXED_APPEARANCE_NOT_INVARIANT_WITHOUT_DERIVED_REAL_FORM_INTERTWINER"
        ),
        "stage52_dc_generation_status": (
            "NO_GO_COMPACT_SPIN1_SUBGROUP_ALONE_CANNOT_GENERATE_DC_PAIR"
            if passed
            else "FAILED"
        ),
        "stage66_c3_orbit_generator_status": (
            "STAGE66_C3_ORBIT_GENERATES_FULL_SU3F_LIE_ALGEBRA"
            if passed
            else "FAILED"
        ),
        "stage24_66_forward_pair_status": (
            "ORIENTED_A1_TO_A2_NONCOMMUTING_PAIR_WITH_EXPLICIT_COMPLEMENT_INJECTION"
            if passed
            else "FAILED"
        ),
        "family_complement_injection_status": (
            "CLOSED_AT_STAGE66_C3_ORBIT_GENERATOR_SET_LEVEL__BRANCH_BINDING_OPEN"
            if passed
            else "FAILED"
        ),
        "stage66_branch_assignment_status": (
            "STATIC_EO_TO_TWO_STAGE66_ORBIT_GENERATORS_REFUTED"
        ),
        "collatz_temporal_c3_frame_status": (
            "STOPPING_DEPTH_MOD3_COLLATZ_TO_TEMPORAL_C3_EQUIVARIANT_BINDING_CLOSED"
            if passed
            else "FAILED"
        ),
        "stage66_state_dependent_orbit_binding_status": (
            "CLOSED_REPRESENTATION_LEVEL_VIA_NEGATIVE_STOPPING_DEPTH_MOD3"
            if passed
            else "FAILED"
        ),
        "collatz_state_family_generator_index_status": (
            "G_N_EQUALS_A_MINUS_L_MOD3_C3_EQUIVARIANT"
            if passed
            else "FAILED"
        ),
        "signed_geometric_step_candidate_status": (
            "PASS_MATH_PROVENANCE__PHYSICAL_PROMOTION_OPEN"
            if passed
            else "FAILED"
        ),
        "state_dependent_su3_step_status": (
            "SOURCE_DERIVED_PARAMETER_FREE_SU3_STEP_SCAFFOLD_VALIDATED"
            if passed
            else "FAILED"
        ),
        "signed_geometric_order_status": (
            "EQUAL_COUNT_EO_OE_ORDER_DISTINGUISHED_ON_ROTATING_C3_AXES"
            if passed
            else "FAILED"
        ),
        "three_step_lie_access_status": (
            "EVERY_THREE_CONSECUTIVE_C3_AXES_LIE_GENERATE_SU3F"
            if passed
            else "FAILED"
        ),
        "physical_signed_geometric_step_status": (
            "NOT_PROMOTED_PHYSICAL_HAMILTONIAN_BINDING_OPEN"
        ),
        "common_target_family_path_holonomy_status": (
            "PASS_SU3_GROUPOID_FLAT_PURE_GAUGE"
            if passed
            else "FAILED"
        ),
        "common_target_family_wij_status": (
            "SOURCE_DERIVED_COMMON_TARGET_FAMILY_WIJ_SCAFFOLD_CLOSED"
            if passed
            else "FAILED"
        ),
        "common_target_wilson_loop_status": (
            "TRIANGULAR_WILSON_LOOP_IDENTITY"
            if passed
            else "FAILED"
        ),
        "common_target_cp_holonomy_status": (
            "NO_GO_COMMON_TARGET_COBoundARY_TRANSPORT_ALONE_CANNOT_SOURCE_NONZERO_LOOP_HOLONOMY"
            if passed
            else "FAILED"
        ),
        "physical_family_connection_status": (
            "NONFLAT_TERMINAL_CYCLE_CANDIDATE_EXISTS__PHYSICAL_FAMILY_CONNECTION_BINDING_OPEN"
        ),
        "terminal_cycle_holonomy_status": (
            "TERMINAL_COLLATZ_CYCLE_NONTRIVIAL_SU3_HOLONOMY_RETROSPECTIVE_STRUCTURAL_PASS"
            if passed
            else "FAILED"
        ),
        "terminal_cycle_nonflat_source_status": (
            "TERMINAL_CYCLE_SUPPLIES_NONFLAT_SOURCE_DERIVED_LOOP_CANDIDATE"
            if passed
            else "FAILED"
        ),
        "terminal_cycle_spin1_exclusion_status": (
            "TERMINAL_LOOP_OUTSIDE_EVERY_CONJUGATE_SPIN1_SU2_SUBGROUP"
            if passed
            else "FAILED"
        ),
        "terminal_cycle_full_su3_direction_status": (
            "TERMINAL_LOOP_REQUIRES_DIRECTIONS_BEYOND_COMPACT_SPIN1_SUBGROUP"
            if passed
            else "FAILED"
        ),
        "terminal_cycle_basepoint_status": (
            "TERMINAL_LOOP_CONJUGACY_CLASS_BASEPOINT_COVARIANT"
            if passed
            else "FAILED"
        ),
        "terminal_cycle_orientation_status": (
            "TERMINAL_LOOP_IMAGINARY_TRACE_ORIENTATION_ODD_CLASS_WITNESS"
            if passed
            else "FAILED"
        ),
        "terminal_cycle_trace_fixedpoint_identity_status": (
            "SU3_DET_U_MINUS_I_EQUALS_2I_IM_TRACE_EXACT"
            if passed
            else "FAILED"
        ),
        "terminal_cycle_inverse_conjugacy_status": (
            "TERMINAL_LOOP_AND_ORIENTATION_REVERSE_ARE_DISTINCT_SU3_CONJUGACY_CLASSES"
            if passed
            else "FAILED"
        ),
        "terminal_cycle_inner_symmetry_status": (
            "ORIENTATION_REVERSAL_NOT_REMOVABLE_BY_INNER_SU3_CONJUGATION"
            if passed
            else "FAILED"
        ),
        "terminal_cycle_outer_conjugation_status": (
            "COMPLEX_CONJUGATION_MAPS_TERMINAL_FORWARD_CLASS_TO_REVERSE_CLASS"
            if passed
            else "FAILED"
        ),
        "terminal_cycle_outer_z2_status": (
            "TERMINAL_FORWARD_REVERSE_CLASSES_FORM_INVOLUTIVE_OUTER_Z2_PAIR"
            if passed
            else "FAILED"
        ),
        "su3_conjugacy_trace_coordinate_status": (
            "SU3_CONJUGACY_CLASS_COMPLETELY_COORDINATIZED_BY_COMPLEX_TRACE"
            if passed
            else "FAILED"
        ),
        "su3_outer_fixed_locus_status": (
            "OUTER_CONJUGATION_FIXED_CLASSES_FORM_REAL_TRACE_INTERVAL_MINUS1_TO3"
            if passed
            else "FAILED"
        ),
        "su3_outer_quotient_compactification_status": (
            "COMPACT_SU3_CLASS_SPACE_MOD_OUTER_Z2_HALF_DELTOID"
            if passed
            else "FAILED"
        ),
        "terminal_outer_quotient_status": (
            "TERMINAL_FORWARD_REVERSE_PAIR_IDENTIFIED_AS_ONE_OFF_FIXED_LOCUS_QUOTIENT_POINT"
            if passed
            else "FAILED"
        ),
        "outer_fixed_spin1_class_locus_status": (
            "OUTER_FIXED_CLASS_LOCUS_EQUALS_CONJUGATE_SPIN1_SO3_CLASS_LOCUS"
            if passed
            else "FAILED"
        ),
        "outer_symmetric_pair_split_status": (
            "OUTER_INVOLUTION_LIE_SPLIT_SU3_EQUALS_SO3_PLUS_FIVE_COMPLEMENT"
            if passed
            else "FAILED"
        ),
        "terminal_outer_complement_status": (
            "TERMINAL_OFF_FIXED_CLASS_REQUIRES_SU3_OVER_SO3_COMPLEMENT_DIRECTIONS"
            if passed
            else "FAILED"
        ),
        "terminal_cycle_outer_inner_distinction_status": (
            "COMPLEX_CONJUGATION_NOT_INNER_ON_TERMINAL_CLASS_WITNESS"
            if passed
            else "FAILED"
        ),
        "terminal_cycle_regular_class_status": (
            "TERMINAL_LOOP_REGULAR_SU3_CONJUGACY_CLASS"
            if passed
            else "FAILED"
        ),
        "terminal_cycle_centralizer_status": (
            "TERMINAL_LOOP_CENTRALIZER_IS_MAXIMAL_TORUS_U1_X_U1"
            if passed
            else "FAILED"
        ),
        "terminal_cycle_cartan_rank_status": (
            "TERMINAL_LOOP_SUPPLIES_TWO_INDEPENDENT_CARTAN_EIGENPHASE_COORDINATES"
            if passed
            else "FAILED"
        ),
        "terminal_cycle_coboundary_status": (
            "NONTRIVIAL_TERMINAL_WILSON_LOOP_REFUTES_GLOBAL_GI_DAGGER_GJ_FACTORIZATION"
            if passed
            else "FAILED"
        ),
        "nonseparable_path_holonomy_status": (
            "SOURCE_DERIVED_NONSEPARABLE_PATH_HOLONOMY_CANDIDATE_EXISTS"
            if passed
            else "FAILED"
        ),
        "terminal_cycle_cp_status": (
            "NONTRIVIAL_WILSON_LOOP_NOT_YET_PHYSICAL_CP_OR_SECTOR_BINDING"
        ),
        "terminal_cycle_prospective_status": (
            "RETROSPECTIVE_STRUCTURAL_CANDIDATE_NOT_PROSPECTIVE_TEST"
        ),
        "stage66_full_orbit_access_requirement": (
            "FULL_SU3F_FROM_STAGE66_REQUIRES_ALL_THREE_ORBIT_GENERATORS_OR_EQUIVALENT_EXTRA_DIRECTION"
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
        "overlap_bargmann_crosswalk_status": (
            "PLAQUETTE_PHASE_EQUALS_BARGMANN_QUADRILATERAL_UNDER_OVERLAP_REALIZATION"
            if passed
            else "FAILED"
        ),
        "c3_projective_frame_status": (
            "C3_LABEL_AND_CHARACTER_PROJECTIVE_FRAMES_CURRENT_EXACT"
            if passed
            else "FAILED"
        ),
        "f3_bargmann_cp_status": (
            "F3_NONZERO_BARGMANN_PLAQUETTE_AND_JARLSKOG_CURRENT_EXACT"
            if passed
            else "FAILED"
        ),
        "stage39_sector_frame_status": (
            "TWO_HERMITIAN_SECTOR_EIGENFRAMES_FROZEN_STRUCTURAL_CANDIDATE"
            if passed
            else "FAILED"
        ),
        "stage39_relative_family_status": (
            "NONZERO_CP_UNITARY_RELATIVE_TRANSFORMATION_REPRODUCED_NO_TARGET_FIT"
            if passed
            else "FAILED"
        ),
        "physical_sector_assignment_status": (
            "OPEN_STAGE39_A_B_ASSIGNMENT_NOT_SELECTED"
        ),
        "coefficient_orientation_sector_assignment_status": (
            "COEFFICIENT_ORIENTATION_DOES_NOT_YET_SELECT_STAGE39_SECTOR_ASSIGNMENT"
        ),
        "cp_sign_selection_firewall": (
            "OBSERVED_CP_SIGN_SELECTION_FORBIDDEN_AS_TARGET_LEAKAGE"
        ),
        "ckm_closure_status": (
            "OPEN_COEFFICIENT_FREE_HOLONOMIC_SECTOR_ASSIGNMENT_THEOREM"
        ),
        "generic_wij_holonomy_status": (
            "GENERIC_WIJ_PATH_HOLONOMY_GRAMMAR_TYPED_CURRENT"
            if passed
            else "FAILED"
        ),
        "family_wij_source_binding_status": (
            "COMMON_TARGET_FLAT_COBoundARY_SCAFFOLD_CLOSED__TERMINAL_COLLATZ_NONCOBOUNDARY_NONSEPARABLE_SU3_HOLONOMY_CANDIDATE_EXISTS__PHYSICAL_BINDING_OPEN"
        ),
        "selector_location_status": (
            "SELECTOR_MUST_RETAIN_PATH_LOCAL_DATA_UPSTREAM_OF_ENDPOINT_SU3_REDUCTION"
        ),
        "ckm_quantitative_status": (
            "STAGE40_FULL_CKM_SHAPE_FAIL_RETAINED"
        ),
        "projective_holonomy_source_status": (
            "C3_PROJECTIVE_FRAMES_AND_STAGE39_STRUCTURAL_SECTOR_FRAMES_DERIVED__PHYSICAL_ASSIGNMENT_AND_CKM_PROMOTION_OPEN"
        ),
        "scalar_qc_cp_status": (
            "SCALAR_VERTEX_QC_PHASE_DIFFERENCE_CP_NO_GO"
            if passed
            else "FAILED"
        ),
        "cp_phase_source_requirement": (
            "NONSEPARABLE_PAIR_DEPENDENT_HOLONOMY_REQUIRED_FOR_NONZERO_PLAQUETTE_PHASE"
            if passed
            else "FAILED"
        ),
        "equatorial_qc_bargmann_status": (
            "ACTIVE_SCALAR_QC_EQUATORIAL_BARGMANN_PHASE_ZERO"
            if passed
            else "FAILED"
        ),
        "geometric_cp_source_requirement": (
            "ADDITIONAL_NONSEPARABLE_CONNECTION_OR_NON_EQUATORIAL_MULTI_RAY_GEOMETRY_REQUIRED"
            if passed
            else "FAILED"
        ),
        "flavour_cardinality_result": (
            "N_F_EQUALS_3_CONDITIONAL_ON_PHYSICAL_TEMPORAL_FAMILY_BINDING"
            if passed
            else "NOT_ESTABLISHED"
        ),
        "complex_holonomy_cp_mechanism_status": (
            "NONPOLAR_COMPLEX_HOLONOMY_CP_MECHANISM_EXISTS_SOURCE_QUARANTINED"
            if passed
            else "FAILED"
        ),
        "branch_to_complex_holonomy_status": (
            "SOURCE_DERIVED_STATE_DEPENDENT_NONSEPARABLE_SU3_HOLONOMY_MAP_CANDIDATE_EXISTS__PHYSICAL_FAMILY_CP_BINDING_OPEN"
        ),
        "stage39_40_status": (
            "TWO_OPERATOR_MECHANISM_RETAINED_FULL_CKM_SHAPE_FAIL"
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
        "orientation_c3_z2_extension_status": (
            "C3_SEMIDIRECT_Z2_INVERSION_IS_D3_ISOMORPHIC_S3"
            if passed
            else "FAILED"
        ),
        "sixfold_symmetry_distinction_status": (
            "ABELIAN_C6_WEAK_PRODUCT_DISTINCT_FROM_NONABELIAN_D3_ORIENTATION_EXTENSION"
            if passed
            else "FAILED"
        ),
        "twelvefold_dihedral_extension_status": (
            "C6_SEMIDIRECT_Z2_INVERSION_IS_HEXAGON_DIHEDRAL_GROUP_ORDER12"
            if passed
            else "FAILED"
        ),
        "mod6pi_six_to_twelve_group_status": (
            "SIX_STATE_C6_ROTATION_EXTENDS_TO_TWELVE_ELEMENT_ORIENTATION_DIHEDRAL_SYMMETRY"
            if passed
            else "FAILED"
        ),
        "d3_real_rep_decomposition_status": (
            "D3_FAMILY_PERMUTATION_REP_REAL_3_DECOMPOSES_AS_1_PLUS_2"
            if passed
            else "FAILED"
        ),
        "f3_character_decomposition_status": (
            "F3_TRIVIAL_SINGLET_PLUS_CONJUGATE_CHARACTER_PAIR_COMPLEXIFIES_REAL_1_PLUS_2"
            if passed
            else "FAILED"
        ),
        "su3_so3_rank_status": (
            "SU3_SO3_SYMMETRIC_SPACE_RANK_TWO"
            if passed
            else "FAILED"
        ),
        "su3_so3_restricted_root_status": (
            "SU3_SO3_RESTRICTED_ROOT_SYSTEM_A2"
            if passed
            else "FAILED"
        ),
        "su3_so3_weyl_status": (
            "SU3_SO3_RESTRICTED_WEYL_GROUP_D3_ISOMORPHIC_S3"
            if passed
            else "FAILED"
        ),
        "family_cartan_plane_intertwiner_status": (
            "FAMILY_STANDARD_TWO_PLANE_INTERTWINES_SU3_SO3_RANK2_CARTAN_PLANE"
            if passed
            else "FAILED"
        ),
        "su3_weyl_alcove_status": (
            "SU3_RANK2_WEYL_ALCOVE_EQUILATERAL_TRIANGLE_EXACT"
            if passed
            else "FAILED"
        ),
        "su3_alcove_deltoid_status": (
            "SU3_WEYL_ALCOVE_TRACE_MAPS_TO_COMPACT_DELTOID_CLASS_SPACE"
            if passed
            else "FAILED"
        ),
        "family_plane_compactification_status": (
            "FAMILY_STANDARD_TWO_PLANE_COMPACTIFIES_VIA_A2_AFFINE_WEYL_TO_SU3_CLASS_DELTOID"
            if passed
            else "FAILED"
        ),
        "su3_so3_cartan_embedding_status": (
            "SU3_MOD_SO3_CARTAN_EMBEDDING_IS_SYMMETRIC_UNITARY_DET1_MANIFOLD"
            if passed
            else "FAILED"
        ),
        "su3_so3_flat_embedding_status": (
            "RANK2_CARTAN_FLAT_EMBEDS_AS_DIAGONAL_SYMMETRIC_UNITARY_EXP_IH"
            if passed
            else "FAILED"
        ),
        "six_state_c6_character_spectrum_status": (
            "WEAK_FAMILY_C6_REGULAR_CHARACTER_SPECTRUM_ALL_SIXTH_ROOTS_EXACT"
            if passed
            else "FAILED"
        ),
        "six_state_d6_real_mode_decomposition_status": (
            "D6_SIX_STATE_REAL_REP_DECOMPOSES_AS_1_PLUS_1_PLUS_2_PLUS_2"
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
            "orientation_reflection_involution": orientation_reflection_involution_residual,
            "orientation_inversion_action": orientation_inversion_action_residual,
            "orientation_extension_noncommutativity": orientation_extension_noncommutativity,
            "weak_family_c3_z2_commutator": weak_family_commutator_residual,
            "six_state_c6_order6": G6_order6_residual,
            "six_state_orientation_z2": R6_involution_residual,
            "six_state_dihedral_inversion": D6_inversion_relation_residual,
            "d3_singlet_P": d3_singlet_P_residual,
            "d3_singlet_R": d3_singlet_R_residual,
            "d3_plane_order3": d3_plane_rotation_order3_residual,
            "d3_plane_reflection": d3_plane_reflection_involution_residual,
            "f3_character_plane_projector": f3_character_plane_projector_residual,
            "su3_so3_cartan_orthonormal": su3so3_cartan_orthonormal_residual,
            "su3_so3_cartan_commutator": su3so3_cartan_commutator_residual,
            "family_cartan_P_intertwiner": family_to_cartan_P_intertwiner_residual,
            "family_cartan_R_intertwiner": family_to_cartan_R_intertwiner_residual,
            "su3_so3_A2_root_sum": a2_root_sum_residual,
            "su3_so3_A2_root_norm": a2_root_norm_residual,
            "su3_so3_A2_cartan_matrix": a2_cartan_matrix_residual,
            "su3_alcove_equilateral": alcove_equilateral_residual,
            "su3_alcove_area": alcove_area_residual,
            "su3_alcove_cusps": alcove_cusp_residual,
            "su3_alcove_deltoid_edge": alcove_edge_deltoid_residual,
            "su3_alcove_weyl_trace": alcove_weyl_trace_residual,
            "su3_so3_cartan_embedding_symmetry": cartan_embedding_symmetry_residual,
            "su3_so3_cartan_embedding_unitarity": cartan_embedding_unitarity_residual,
            "su3_so3_cartan_embedding_determinant": cartan_embedding_determinant_residual,
            "su3_so3_cartan_embedding_coset": cartan_embedding_right_so3_residual,
            "su3_so3_cartan_embedding_flat": cartan_embedding_flat_exp_residual,
            "six_state_c6_character_offdiag": G6_character_offdiag_residual,
            "six_state_c6_sixth_root_match": G6_sixth_root_match_residual,
            "six_state_c6_conjugate_pair": G6_conjugate_pair_residual,
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
            "c3_label_character_overlap_f3": f3_overlap_residual,
            "f3_bargmann_identity": f3_bargmann_residual,
            "f3_bargmann_phase": f3_bargmann_phase_residual,
            "f3_plaquette_jarlskog": f3_plaquette_j_residual,
            "stage39_J_A_abs": stage39_J_A_abs_residual,
            "stage39_J_B_abs": stage39_J_B_abs_residual,
            "stage39_J_sign_flip": stage39_J_sign_flip_residual,
            "stage39_abs_transpose": stage39_abs_transpose_residual,
            "jarlskog_exact": abs(J - J_exact),
            "stage66_c3_orbit_lie_closure": selector_orbit_lie_residual,
            "stage66_c3_orbit_kp_projection": selector_orbit_kp_residual,
            "stage66_c3_orbit_kp_reconstruction": selector_orbit_kp_reconstruction_residual,
            "collatz_state_generator_c3_equivariance": state_generator_equivariance_residual,
            "signed_geo_candidate_hermiticity": candidate_hermiticity_residual,
            "signed_geo_candidate_trace": candidate_trace_residual,
            "signed_geo_candidate_unitarity": candidate_unitarity_residual,
            "signed_geo_candidate_determinant": candidate_determinant_residual,
            "common_target_path_unitarity": common_target_path_unitarity_residual,
            "common_target_path_determinant": common_target_path_determinant_residual,
            "common_target_wij_unitarity": common_target_w_unitarity_residual,
            "common_target_wij_determinant": common_target_w_determinant_residual,
            "common_target_wij_reversal": common_target_reversal_residual,
            "common_target_wij_composition": common_target_composition_residual,
            "common_target_triangle_wilson": common_target_triangle_residual,
            "common_target_reverse_triangle_wilson": (
                common_target_reverse_triangle_residual
            ),
            "terminal_cycle_unitarity": terminal_loop_unitarity_residual,
            "terminal_cycle_determinant": terminal_loop_determinant_residual,
            "terminal_cycle_nonidentity": terminal_loop_nonidentity,
            "terminal_cycle_trace_formula": terminal_trace_formula_residual,
            "terminal_cycle_trace_imag": terminal_trace_imag_residual,
            "terminal_cycle_gauge_trace": terminal_gauge_trace_residual,
            "terminal_cycle_gauge_trace2": terminal_gauge_trace2_residual,
            "terminal_cycle_gauge_det": terminal_gauge_det_residual,
            "terminal_cycle_gauge_charpoly": terminal_charpoly_residual,
            "terminal_trace_class_polynomial": terminal_trace_class_poly_residual,
            "su3_deltoid_conjugation": deltoid_conjugation_residual,
            "su3_fixed_locus_factorization": fixed_locus_factorization_residual,
            "terminal_outer_fixed_locus_distance": terminal_trace_fixed_locus_distance,
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
            "oriented_negative_mode_label": "s2_to_s3_representation_tangent",
            "orientation_parent": "Stage24 P_s: s2 -> s3",
            "orientation_scope": "REPRESENTATION_LEVEL_ONLY",
            "single_axis_generator_commutator_residual": (
                single_axis_generator_commutator
            ),
            "mobius_branch_noncommutativity_residual": (
                mobius_branch_noncommutativity
            ),
            "single_axis_branch_map": "REFUTED_AS_ORDER_PRESERVING_SOURCE_MAP",
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
        "real_lie_lift_nogo_audit": {
            "source_algebra": "sl(2,R)",
            "source_killing_matrix_HEF": sl2_killing.tolist(),
            "source_killing_eigenvalues": sl2_killing_eigenvalues.tolist(),
            "source_killing_signature": {
                "positive": sl2_killing_positive,
                "negative": sl2_killing_negative,
                "zero": sl2_killing_zero,
            },
            "source_simple": True,
            "target_algebra": "su(3)",
            "target_compact": True,
            "nonzero_real_lie_homomorphism_would_be_injective": True,
            "injective_embedding_into_compact_target": False,
            "continuous_PSL2R_to_SU3_nontrivial_lift": False,
            "allowed_remaining_routes": [
                "discrete_branch_monoid_map",
                "complex_holonomy",
                "state_dependent_map",
                "complexification_plus_additional_dynamics",
            ],
        },
        "path_holonomy_separability_audit": {
            "flat_coboundary_form": "W_ij = G_i^dagger G_j",
            "flat_triangle_identity_required": True,
            "common_target_triangle_residual": common_target_triangle_residual,
            "terminal_loop_nonidentity_max_abs": terminal_loop_nonidentity,
            "terminal_loop_global_coboundary_factorization_possible": False,
            "terminal_path_data_classification": (
                "NONCOBOUNDARY_NONSEPARABLE_PATH_HOLONOMY_CANDIDATE"
            ),
            "physical_family_connection_promoted": False,
            "physical_cp_promoted": False,
        },
        "terminal_collatz_cycle_holonomy_audit": {
            "classification": "RETROSPECTIVE_STRUCTURAL_CANDIDATE_NOT_PROSPECTIVE_TEST",
            "states": terminal_loop_states,
            "next_states": terminal_loop_next_states,
            "branches": terminal_loop_branches,
            "frames": terminal_loop_frames,
            "definition": "U_circle=U_E(A2)*U_E(A1)*U_O(A0)",
            "unitarity_residual": terminal_loop_unitarity_residual,
            "determinant_residual": terminal_loop_determinant_residual,
            "nonidentity_max_abs": terminal_loop_nonidentity,
            "trace": {
                "real": float(terminal_loop_trace.real),
                "imag": float(terminal_loop_trace.imag),
            },
            "trace_formula": (
                "2*cos(ln3/2)*cos(ln2/2)+cos(ln2/2)^2"
                "+i*sin(ln3/2)*sin(ln2/2)^2"
            ),
            "trace_formula_residual": terminal_trace_formula_residual,
            "trace_imag_exact": terminal_trace_imag_exact,
            "trace_imag_residual": terminal_trace_imag_residual,
            "spin1_character_expected_form": "1+2*cos(theta) is real",
            "spin1_forced_eigenvalue": 1,
            "det_U_minus_I": {
                "real": float(terminal_det_u_minus_i.real),
                "imag": float(terminal_det_u_minus_i.imag),
                "abs": float(terminal_spin1_unit_eigenvalue_exclusion),
            },
            "su3_identity_det_U_minus_I_equals_2i_Im_trace_residual": (
                terminal_trace_det_identity_residual
            ),
            "forward_vs_inverse_trace_gap": float(terminal_inverse_trace_gap),
            "forward_vs_inverse_trace_gap_equals_2absImTrace_residual": (
                terminal_inverse_trace_gap_identity_residual
            ),
            "outside_every_conjugate_spin1_su2": True,
            "basepoint_conjugacy": {
                "base1_match_residual": terminal_base1_match_residual,
                "base4_conjugacy_residual": terminal_base4_conjugacy_residual,
                "base2_conjugacy_residual": terminal_base2_conjugacy_residual,
                "trace_residual": float(terminal_basepoint_trace_residual),
                "charpoly_residual": terminal_basepoint_charpoly_residual,
            },
            "regular_su3_class": {
                "pairwise_eigenvalue_separations": terminal_pairwise_eigenvalue_separations,
                "minimum_eigenvalue_separation": terminal_min_eigenvalue_separation,
                "spectral_discriminant": float(terminal_spectral_discriminant),
                "principal_eigenphase_sum": terminal_eigenphase_sum,
                "principal_eigenphase_sum_residual": terminal_eigenphase_sum_residual,
                "centralizer": "MAXIMAL_TORUS_U1_X_U1",
                "cartan_rank": 2,
            },
            "su3_trace_class_compactification": {
                "class_coordinate": "t=tr(U)",
                "characteristic_polynomial": (
                    "lambda^3-t*lambda^2+conj(t)*lambda-1"
                ),
                "characteristic_polynomial_residual": (
                    terminal_trace_class_poly_residual
                ),
                "trace_region": "compact_deltoid",
                "deltoid_boundary": "2*exp(i*theta)+exp(-2*i*theta)",
                "deltoid_conjugation_residual": (
                    deltoid_conjugation_residual
                ),
                "outer_involution": "t -> conj(t)",
                "fixed_locus": "real_interval[-1,3]",
                "fixed_locus_factorization_residual": (
                    fixed_locus_factorization_residual
                ),
                "terminal_distance_to_fixed_locus_trace_plane": (
                    terminal_trace_fixed_locus_distance
                ),
                "terminal_outer_orbit_size": terminal_outer_orbit_size,
                "quotient_representative_halfplane": "Im(t)>=0",
                "physical_CP_identification": False,
                "fixed_class_equivalences": [
                    "Im(tr U)=0",
                    "det(U-I)=0",
                    "eigenvalue_1_present",
                    "class_intersects_conjugate_SO3_spin1_subgroup",
                ],
                "stage55_symmetric_pair": "SU(3)/SO(3)",
                "lie_fixed_sector_dimension": 3,
                "lie_antifixed_complement_dimension": 5,
                "terminal_spin1_exclusion_abs_det_U_minus_I": (
                    float(terminal_spin1_unit_eigenvalue_exclusion)
                ),
                "terminal_requires_complement_directions": True,
            },
            "outer_complex_conjugation": {
                "involution_residual": terminal_complex_conjugation_involution_residual,
                "unitarity_residual": terminal_conjugate_unitarity_residual,
                "determinant_residual": terminal_conjugate_determinant_residual,
                "trace_conjugation_residual": terminal_conjugate_trace_residual,
                "conjugate_vs_reverse_charpoly_residual": (
                    terminal_conjugate_vs_inverse_charpoly_residual
                ),
                "forward_vs_conjugate_trace_separation": float(
                    terminal_outer_class_trace_separation
                ),
                "trace_separation_equals_2absImTrace_residual": (
                    terminal_outer_class_trace_separation_identity_residual
                ),
                "classification": (
                    "FORWARD_AND_REVERSE_CLASSES_EXCHANGED_BY_INVOLUTIVE_COMPLEX_CONJUGATION"
                ),
            },
            "orientation_reversal": {
                "inverse_residual": terminal_reverse_inverse_residual,
                "trace_conjugacy_residual": float(
                    terminal_reverse_trace_conjugacy_residual
                ),
                "imaginary_part_sum_residual": float(
                    terminal_orientation_odd_imag_sum_residual
                ),
                "real_part_difference_residual": float(
                    terminal_orientation_even_real_diff_residual
                ),
                "forward_imaginary_trace": terminal_orientation_odd_witness,
                "reverse_imaginary_trace": float(
                    np.trace(U_terminal_reverse).imag
                ),
            },
            "eigenphases_rad": terminal_loop_eigenphases,
            "F3_conjugacy_trace_residual": terminal_gauge_trace_residual,
            "F3_conjugacy_trace2_residual": terminal_gauge_trace2_residual,
            "F3_conjugacy_determinant_residual": terminal_gauge_det_residual,
            "F3_conjugacy_charpoly_residual": terminal_charpoly_residual,
            "uses_observed_CKM": False,
            "uses_observed_PMNS": False,
            "uses_observed_masses": False,
            "uses_fitted_coefficients": False,
            "physical_cp_claimed": False,
            "physical_family_connection_claimed": False,
        },
        "common_target_family_path_holonomy_audit": {
            "target": common_target,
            "seeds": common_target_seeds,
            "path_lengths": {
                str(s): common_target_paths[s]["length"]
                for s in common_target_seeds
            },
            "branch_words": {
                str(s): "".join(common_target_paths[s]["branches"])
                for s in common_target_seeds
            },
            "start_frames": {
                str(s): (
                    common_target_paths[s]["frames"][0]
                    if common_target_paths[s]["frames"]
                    else (-collatz_depth_to_one(s)) % 3
                )
                for s in common_target_seeds
            },
            "target_frame": (-collatz_depth_to_one(common_target)) % 3,
            "path_unitarity_residual": common_target_path_unitarity_residual,
            "path_determinant_residual": common_target_path_determinant_residual,
            "wij_unitarity_residual": common_target_w_unitarity_residual,
            "wij_determinant_residual": common_target_w_determinant_residual,
            "wij_reversal_residual": common_target_reversal_residual,
            "wij_composition_residual": common_target_composition_residual,
            "wij_diagonal_residual": common_target_diagonal_residual,
            "triangle_wilson_residual": common_target_triangle_residual,
            "reverse_triangle_wilson_residual": (
                common_target_reverse_triangle_residual
            ),
            "edge_nontriviality": common_target_edge_nontriviality,
            "edge_commutator_max_abs": common_target_edge_commutator,
            "classification": "FLAT_PURE_GAUGE_COMMON_TARGET_GROUPOID",
            "physical_promotion": False,
            "uses_observed_CKM": False,
            "uses_observed_PMNS": False,
            "uses_observed_masses": False,
            "uses_fitted_coefficients": False,
        },
        "signed_geometric_step_candidate_audit": {
            "freeze_status": "FROZEN_PREVALIDATION_BEFORE_THIS_VALIDATOR_COMMIT",
            "definition": "K_geo(n)=sigma_b(n)*A_{(-L(n)) mod 3}",
            "sigma_E": "-ln(2)",
            "sigma_O": "+ln(3)",
            "step_unitary": "U_geo(n)=exp(-i*K_geo(n))",
            "hermiticity_residual": candidate_hermiticity_residual,
            "trace_residual": candidate_trace_residual,
            "unitarity_residual": candidate_unitarity_residual,
            "determinant_residual": candidate_determinant_residual,
            "two_step_EO_vs_OE_separations": candidate_two_step_order_separations,
            "three_step_lie_dimensions": candidate_three_step_dims,
            "three_step_lie_residuals": candidate_three_step_residuals,
            "uses_observed_CKM": False,
            "uses_observed_PMNS": False,
            "uses_observed_masses": False,
            "uses_fitted_coefficients": False,
            "physical_promotion": False,
        },
        "collatz_c3_state_index_audit": {
            "definition": "r_C(n)=(-L(n)) mod 3",
            "tested_range": [1, collatz_c3_tested],
            "failures": collatz_c3_failures,
            "frame_counts": collatz_c3_frame_counts,
            "terminal_cycle_states": terminal_cycle_states,
            "terminal_cycle_depths": terminal_cycle_depths,
            "terminal_cycle_frames": terminal_cycle_frames,
            "terminal_cycle_qC": [str(x) for x in terminal_cycle_qc],
            "terminal_cycle_qC_expected": ["4/7", "1/7", "2/7"],
            "terminal_qC_doubling_exact": terminal_qc_doubling_exact,
            "state_generator_equivariance_residual": (
                state_generator_equivariance_residual
            ),
            "family_generator_index": "A_{r_C(n)}",
            "physical_temporal_family_binding": "OPEN",
        },
        "stage66_c3_orbit_generator_audit": {
            "orbit_labels": ["A0_12", "A1_23", "A2_13"],
            "negative_mode_orbit_index": selector_negative_best_orbit_index,
            "negative_mode_alignment": selector_negative_best_alignment,
            "pair_lie_dimensions": selector_pair_dims,
            "pair_lie_residuals": selector_pair_residuals,
            "full_orbit_lie_dimension": selector_orbit_lie_dim,
            "full_orbit_lie_residual": selector_orbit_lie_residual,
            "stage55_kp_projection": selector_orbit_kp,
            "forward_pair": ["A1_23", "A2_13"],
            "forward_pair_commutator_max_abs": selector_forward_commutator_max,
            "forward_pair_commutator_norm2": selector_forward_commutator_norm2,
            "forward_successor_A2_pure_complement": True,
            "branch_symbol_assignment": "OPEN_EO_Z2",
        },
        "family_wij_source_audit": {
            "generic_transport": "W_ij^(G,R)=Pexp(int_gamma A_R)",
            "current_explicit_instances": [
                "WT_U1",
                "SPATIAL_SU2",
                "COLOR_SU3",
            ],
            "current_explicit_family_SU3F_path_holonomy": False,
            "endpoint_SU3_to_nonzero_Z4_homomorphic_selector": "IMPOSSIBLE",
            "required_selector_location": "PATH_LOCAL_UPSTREAM_OF_ENDPOINT_REDUCTION",
            "required_next_object": (
                "SOURCE_DERIVED_FAMILY_WIJ_OR_EQUIVALENT_PAIRWISE_PROJECTIVE_HOLONOMY"
            ),
            "minimal_DC_branch_assignment_A": "E->D, O->C",
            "minimal_DC_branch_assignment_B": "E->C, O->D",
            "assignment_A_commutator_max_abs": dc_comm_A_norm,
            "assignment_B_commutator_max_abs": dc_comm_B_norm,
            "branch_swap_commutator_sign_residual": dc_branch_swap_sign_residual,
            "DC_assignment_source_selection": "OPEN_Z2",
            "D_C_spectral_eigen_residual": dc_spectral_eigen_residual,
            "D_C_trace_power_residual": dc_trace_power_residual,
            "D_C_frobenius_residual": dc_frobenius_residual,
            "single_generator_spectral_Z2_selection": "REFUTED",
            "compact_real_form_dynamic_selection": "OPEN_STAGE52",
            "stage55_D0_k_norm2": D0_k_norm2,
            "stage55_D0_p_norm2": D0_p_norm2,
            "stage55_C0_k_norm2": C0_k_norm2,
            "stage55_C0_p_norm2": C0_p_norm2,
            "stage55_projector_formula_residual": stage55_dc_norm_formula_residual,
            "compact_spin1_only_DC_generation": "REFUTED",
            "required_extra_sector": "SU3_OVER_SO3_COMPLEMENT_P_OR_EQUIVALENT",
        },
        "sector_assignment_provenance_audit": {
            "stage39_assignments": {
                "A": {"alpha_u": "2/7", "alpha_d": "2/9"},
                "B": {"alpha_u": "2/9", "alpha_d": "2/7"},
            },
            "assignment_selected_by_stage39": False,
            "assignment_selected_by_stage40_fit": False,
            "coefficient_role_orientation_theorem_defines_alpha_u_alpha_d_map": False,
            "qc_phase_bc_sign_binding": "OPEN",
            "observed_J_sign_allowed_as_assignment_selector": False,
            "next_closure_from_sm_ledger": (
                "coefficient-free holonomic/orientation binding of full CKM"
            ),
        },
        "stage39_sector_frame_audit": {
            "endpoint_ratios": {"a": "2/7", "b": "2/9"},
            "assignment_A": {
                "alpha_u": alpha_a,
                "alpha_d": alpha_b,
                "J": stage39_A["J"],
                "commutator_max_abs": stage39_A["commutator_max_abs"],
                "unitarity_residual": stage39_A["unitarity_residual"],
                "determinant_residual": stage39_A["determinant_residual"],
                "absV": stage39_A["absV"].tolist(),
            },
            "assignment_B": {
                "alpha_u": alpha_b,
                "alpha_d": alpha_a,
                "J": stage39_B["J"],
                "commutator_max_abs": stage39_B["commutator_max_abs"],
                "unitarity_residual": stage39_B["unitarity_residual"],
                "determinant_residual": stage39_B["determinant_residual"],
                "absV": stage39_B["absV"].tolist(),
            },
            "both_assignments_retained": True,
            "uses_observed_CKM": False,
            "uses_observed_masses": False,
            "uses_fitted_coefficients": False,
            "stage40_full_ckm_shape": "FAIL_RETAINED",
        },
        "c3_character_bargmann_audit": {
            "label_frame": "ordered Stage22 family-seed basis",
            "character_frame": "F3 C3 eigenbasis",
            "overlap_matrix": "F3",
            "overlap_matrix_residual": f3_overlap_residual,
            "selected_plaquette": [0, 1, 0, 1],
            "plaquette": {
                "real": float(np.real(f3_plaquette)),
                "imag": float(np.imag(f3_plaquette)),
            },
            "bargmann_identity_residual": f3_bargmann_residual,
            "bargmann_phase_rad": f3_bargmann_phase,
            "bargmann_phase_exact": "2*pi/3",
            "phase_residual": f3_bargmann_phase_residual,
            "J_F3": J,
            "J_exact": "1/(6*sqrt(3))",
            "plaquette_imaginary_part_equals_J_residual": f3_plaquette_j_residual,
            "physical_up_down_sector_frame_binding": "OPEN",
        },
        "overlap_bargmann_audit": {
            "condition": "W_ij = <u_i|d_j>",
            "plaquette_equals_bargmann_quadrilateral_residual": (
                overlap_bargmann_identity_residual
            ),
            "ray_gauge_invariance_residual": overlap_bargmann_gauge_residual,
            "example_bargmann_phase_rad": overlap_bargmann_phase,
            "gremlin_xfi02_status": "CANDIDATE_ONLY_NOT_USED_AS_AUTHORITY",
            "remaining_source_problem": (
                "DERIVE_THE_TWO_PROJECTIVE_FAMILY_FRAMES_OR_EQUIVALENT_PAIRWISE_HOLONOMY"
            ),
        },
        "equatorial_qc_bargmann_audit": {
            "carrier": "S1_SUBSET_CP1_EQUATOR",
            "qC": [str(q) for q in q_vertices],
            "closed_overlap_phase_turn_sum": str(qc_bargmann_turn_sum),
            "pair_q_distances": [str(d) for d in qc_pair_distances],
            "all_pair_q_distances_lt_half": qc_pair_distances_lt_half,
            "bargmann_product_real": qc_bargmann_real,
            "bargmann_product_imag": float(np.imag(qc_bargmann)),
            "bargmann_phase_rad": qc_bargmann_phase,
            "active_triplet_phase_class": "ZERO",
            "hexahedral_multi_ray_parent_has_nonzero_triangle_phase": True,
            "scalar_qC_equator_sufficient_for_family_CP": False,
        },
        "scalar_qc_cp_nogo_audit": {
            "active_centers": active_centers,
            "qC": [str(q) for q in q_vertices],
            "pair_phase_turns_qi_minus_qj": [
                [str(x) for x in row] for row in qc_pair_phase_turns
            ],
            "all_2x2_plaquette_phase_turns": [
                str(x) for x in qc_plaquette_turns
            ],
            "all_plaquettes_zero_exact": qc_all_plaquette_turns_zero,
            "phase_law_class": "SEPARABLE_VERTEX_COBBOUNDARY",
            "rephasing_invariant_CP_phase": "ZERO",
            "stage36_nonzero_plaquette_phase_requires": (
                "PAIR_DEPENDENT_NONSEPARABLE_PHASE_SOURCE"
            ),
            "scalar_qC_alone_sufficient_for_stage36_CP": False,
        },
        "complex_holonomy_provenance_audit": {
            "real_family_pair_stage35": "J_EQUALS_ZERO",
            "complex_holonomy_stage36": "J_NONZERO_MECHANISM_PASS",
            "stage36_source_promotion": "QUARANTINED",
            "common_single_axis_stage37": "NOGO",
            "c3_character_stage38": "CP_CAPABLE_MATH_PASS",
            "two_operator_stage39": "FROZEN_STRUCTURAL_CANDIDATE",
            "stage40_retrospective": "FULL_CKM_SHAPE_FAIL_MECHANISM_RETAINED",
            "collatz_poincare_to_stage36_source_map": "NOT_FOUND_CURRENT",
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
        "six_state_character_spectrum_audit": {
            "diagonalizer": "F3 tensor F2",
            "offdiagonal_residual": G6_character_offdiag_residual,
            "eigenvalues": [
                {"real": float(np.real(z)), "imag": float(np.imag(z))}
                for z in G6_character_eigenvalues
            ],
            "expected_spectrum": "all sixth roots of unity once",
            "sixth_root_match_residual": float(G6_sixth_root_match_residual),
            "real_character_modes": G6_real_eigenvalue_count,
            "nonreal_character_modes": G6_nonreal_eigenvalue_count,
            "real_decomposition": "1 + 1 + 2 + 2",
            "physical_particle_or_spacetime_claimed": False,
        },
        "d3_one_plus_two_representation_audit": {
            "real_decomposition": "R^3 = invariant 1 + standard 2",
            "singlet_vector": d3_singlet.tolist(),
            "plane_basis": d3_plane_basis.tolist(),
            "P3_on_plane": P_d3_plane.tolist(),
            "R_on_plane": R_d3_plane.tolist(),
            "P3_plane_trace": float(np.trace(P_d3_plane)),
            "P3_plane_det": float(np.linalg.det(P_d3_plane)),
            "R_plane_det": float(np.linalg.det(R_d3_plane)),
            "complex_character_decomposition": "chi0 + chi_omega + chi_omega2",
            "F3_trivial_character_singlet_residual": f3_trivial_character_residual,
            "F3_nontrivial_pair_projector_residual": (
                f3_character_plane_projector_residual
            ),
            "physical_spatial_dimension_claimed": False,
        },
        "su3_so3_rank2_weyl_audit": {
            "symmetric_space": "SU(3)/SO(3)",
            "rank": 2,
            "cartan_plane_condition": "x1+x2+x3=0",
            "cartan_basis_vectors": d3_plane_basis.T.tolist(),
            "cartan_gram": su3so3_cartan_gram.tolist(),
            "cartan_commutator_residual": su3so3_cartan_commutator_residual,
            "P3_action_residual": family_to_cartan_P_intertwiner_residual,
            "reflection_action_residual": family_to_cartan_R_intertwiner_residual,
            "restricted_roots": {
                "alpha12": alpha12.tolist(),
                "alpha23": alpha23.tolist(),
                "alpha13": alpha13.tolist(),
            },
            "restricted_root_system": "A2",
            "restricted_weyl_group": "D3 ~= S3",
            "family_permutation_rep": "1 + 2",
            "standard_two_plane_identified_with_rank2_cartan_plane": True,
            "physical_spatial_axis_claimed": False,
        },
        "su3_weyl_alcove_audit": {
            "rank": 2,
            "alcove_inequalities": [
                "theta1>=theta2",
                "theta2>=theta3",
                "theta1-theta3<=2*pi",
                "theta1+theta2+theta3=0",
            ],
            "vertices_x": alcove_vertices_x.tolist(),
            "vertices_q": alcove_vertices_q.tolist(),
            "side_lengths": alcove_side_lengths,
            "side_length_exact": "2*pi*sqrt(2/3)",
            "area": alcove_area,
            "area_exact": "2*pi^2/sqrt(3)",
            "vertex_traces": [
                {"real": float(z.real), "imag": float(z.imag)}
                for z in alcove_vertex_traces
            ],
            "expected_deltoid_cusps": ["3", "3*omega", "3*omega^2"],
            "trace_weyl_invariance_residual": alcove_weyl_trace_residual,
            "class_space_image": "compact SU(3) trace deltoid",
            "physical_spatial_volume_claimed": False,
        },
        "su3_so3_cartan_embedding_audit": {
            "embedding": "Phi(g SO(3)) = g g^T",
            "image": "symmetric unitary determinant-one matrices",
            "test_symmetry_residual": cartan_embedding_symmetry_residual,
            "test_unitarity_residual": cartan_embedding_unitarity_residual,
            "test_determinant_residual": cartan_embedding_determinant_residual,
            "right_so3_coset_invariance_residual": (
                cartan_embedding_right_so3_residual
            ),
            "rank2_flat": "H=diag(theta), sum(theta)=0",
            "flat_embedding": "Phi(exp(iH/2) SO(3)) = exp(iH)",
            "flat_exp_residual": cartan_embedding_flat_exp_residual,
            "flat_trace_residual": cartan_embedding_flat_trace_residual,
            "manifold_dimension": 5,
            "rank": 2,
            "physical_configuration_space_claimed": False,
        },
        "sixfold_group_structure_audit": {
            "family_generator": "P3",
            "orientation_reflection_matrix": np.real(R_orient).astype(int).tolist(),
            "orientation_relation": "R*P3*R = P3^-1",
            "orientation_extension_unique_elements": d3_unique_element_count,
            "orientation_extension_group": "D3 ~= S3",
            "orientation_extension_abelian": False,
            "weak_family_commutator_residual": weak_family_commutator_residual,
            "weak_extension_group": "C3 x Z2 ~= C6",
            "weak_extension_abelian": True,
            "c6_rotation_generator_order": 6,
            "orientation_reflection_inverts_c6_rotation": True,
            "full_six_state_orientation_extension_unique_elements": (
                D6_unique_element_count
            ),
            "full_six_state_orientation_extension_group": (
                "C6 semidirect Z2 inversion = dihedral symmetry of hexagon, order 12"
            ),
            "same_order_does_not_mean_same_group": True,
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
            "stage36_complex_holonomy_mechanism_is_not_promoted_from_quarantined_rows": True,
            "nonzero_cp_mechanism_does_not_supply_collatz_branch_source_map": True,
            "scalar_qc_vertex_phase_cannot_generate_nonzero_plaquette_cp": True,
            "pair_dependent_relational_phase_is_not_derived_from_scalar_qc_by_subtraction": True,
            "collatz_fs_relational_phase_interface_does_not_itself_supply_family_cp_operator": True,
            "equatorial_scalar_qc_bargmann_phase_is_zero_for_active_triplet": True,
            "nonzero_hexahedral_bargmann_phase_is_not_reassigned_to_family_sector": True,
            "bargmann_quadrilateral_identity_is_conditional_on_overlap_realization": True,
            "gremlin_xfi02_candidate_is_not_promoted_by_this_crosswalk": True,
            "generic_projective_overlap_geometry_does_not_derive_physical_sector_frames_by_itself": True,
            "c3_representation_does_derive_label_and_character_projective_frames": True,
            "c3_label_character_frames_are_not_by_themselves_physical_up_down_sector_eigenframes": True,
            "stage39_does_supply_two_structural_sector_eigenframes_without_target_fit": True,
            "stage39_physical_up_down_assignment_remains_open": True,
            "coefficient_role_sign_forcing_is_not_stage39_sector_assignment": True,
            "qc_bc_orientation_sign_correlation_is_not_alpha_u_alpha_d_map": True,
            "observed_ckm_j_sign_must_not_select_stage39_assignment": True,
            "sector_assignment_requires_coefficient_free_holonomic_source_theorem": True,
            "generic_wij_family_word_does_not_mean_flavour_family_holonomy": True,
            "current_wij_crosswalk_has_no_explicit_family_su3f_path_transport": True,
            "endpoint_su3_data_alone_cannot_supply_nonzero_additive_z4_selector": True,
            "family_assignment_selector_must_retain_path_local_data": True,
            "stage40_full_ckm_shape_failure_blocks_quantitative_promotion": True,
            "additional_nonseparable_or_non_equatorial_structure_required_for_cp": True,
            "no_nontrivial_continuous_real_lie_homomorphism_psl2r_to_su3f": True,
            "stage52_complexification_bridge_is_not_a_direct_real_form_homomorphism": True,
            "remaining_branch_map_must_not_be_claimed_as_continuous_psl2r_representation": True,
            "stage40_full_ckm_shape_failure_is_retained": True,
            "terminal_loop_outside_spin1_is_not_by_itself_a_physical_cp_observable": True,
            "nonreal_trace_is_used_only_as_conjugacy_subgroup_exclusion_witness": True,
            "orientation_odd_imaginary_trace_is_not_identified_with_physical_cp": True,
            "orientation_reversal_not_inner_conjugate_is_group_theoretic_not_yet_cp_identification": True,
            "weak_z2_and_orientation_z2_are_distinct_actions": True,
            "c6_and_d3_both_have_six_elements_but_are_not_identified": True,
            "twelve_element_dihedral_extension_is_group_structure_not_particle_count": True,
            "d3_real_1_plus_2_decomposition_is_representation_dimension_not_spacetime_dimension": True,
            "su3_so3_rank_two_is_symmetric_space_rank_not_two_physical_spatial_axes": True,
            "three_family_label_carrier_is_not_identified_with_physical_xyz": True,
            "rank2_cartan_plane_to_three_label_intertwiner_is_group_geometry_not_wave_to_volume_dynamics": True,
            "equilateral_weyl_alcove_is_compact_class_parameter_domain_not_physical_triangle": True,
            "deltoid_trace_image_is_conjugacy_class_geometry_not_spatial_volume": True,
            "affine_weyl_compactification_is_not_physical_space_compactification_claim": True,
            "cartan_embedding_manifold_is_internal_symmetric_space_not_physical_configuration_space": True,
            "five_dimensional_su3_so3_manifold_is_not_five_spatial_dimensions": True,
            "d6_real_1_plus_1_plus_2_plus_2_is_representation_decomposition_not_particle_multiplicity": True,
            "sixth_root_character_spectrum_is_group_representation_data_not_energy_spectrum": True,
            "f3_character_pair_is_not_by_itself_a_physical_two_axis_geometry": True,
            "orientation_reflection_is_not_promoted_to_physical_parity_or_cp": True,
            "complex_conjugation_outer_z2_pair_is_not_identified_with_physical_charge_conjugation": True,
            "outer_automorphism_structure_is_not_by_itself_a_cp_symmetry_statement": True,
            "compact_outer_z2_class_quotient_is_group_geometry_not_physical_cp_claim": True,
            "terminal_off_fixed_locus_trace_is_orientation_class_witness_not_cp_violation_measurement": True,
            "outer_fixed_so3_class_locus_is_group_geometry_not_physical_cp_conservation_statement": True,
            "five_dimensional_outer_antifixed_complement_is_lie_tangent_not_five_spatial_dimensions": True,
            "terminal_complement_requirement_is_necessary_geometry_not_sufficient_physical_cp_condition": True,
            "su3_trace_deltoid_compactness_does_not_identify_observed_mixing_parameters": True,
            "basepoint_covariance_is_groupoid_consistency_not_physical_promotion": True,
            "nontrivial_terminal_loop_closes_nonseparable_path_source_only_at_structural_candidate_level": True,
            "noncoboundary_source_does_not_by_itself_identify_ckm_or_pmns": True,
            "regular_su3_conjugacy_class_is_not_a_ckm_rephasing_class": True,
            "two_cartan_eigenphases_are_structural_loop_invariants_not_observed_mixing_angles": True,
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
            "stage24_plus_stage66_selects_directed_23_tangent_only_at_representation_level": True,
            "directed_23_tangent_is_not_yet_collatz_branch_operator_binding": True,
            "directed_23_tangent_does_not_select_stage39_up_down_assignment": True,
            "single_fixed_stage66_tangent_for_both_branches_loses_word_order": True,
            "branch_operator_map_requires_noncommuting_or_state_dependent_structure": True,
            "minimal_DC_pair_supplies_noncommutativity_but_not_EO_source_assignment": True,
            "EO_to_DC_assignment_must_not_be_selected_from_CKM_or_CP_target_sign": True,
            "D_and_C_are_unitarily_conjugate_so_spectra_cannot_select_branch_assignment": True,
            "diagonal_vs_mixed_matrix_appearance_is_basis_dependent": True,
            "stage52_real_form_bridge_availability_does_not_supply_dynamic_intertwiner_selection": True,
            "stage52_compact_spin1_branch_alone_cannot_reproduce_D_or_C_exactly": True,
            "family_branch_map_requires_nonzero_su3_over_so3_complement_content": True,
            "stage66_full_c3_orbit_already_supplies_full_su3f_generator_set": True,
            "stage66_full_orbit_generation_does_not_select_EO_generator_assignment": True,
            "stage24_66_forward_pair_is_representation_level_not_physical_branch_map": True,
            "any_static_EO_map_to_two_stage66_orbit_axes_has_only_three_dimensional_lie_closure": True,
            "full_stage66_su3f_access_requires_state_dependent_or_three_axis_traversal": True,
            "collatz_step_to_temporal_c3_orbit_index_binding_not_found_current": False,
            "stopping_depth_mod3_supplies_representation_level_collatz_c3_index": True,
            "stopping_depth_mod3_binding_is_conditional_on_finite_stopping_depth": True,
            "representation_level_collatz_c3_index_is_not_physical_temporal_family_identification": True,
            "signed_geometric_step_candidate_was_frozen_before_validation": True,
            "signed_geometric_step_candidate_is_not_promoted_to_physical_hamiltonian": True,
            "candidate_validation_uses_no_ckm_pmns_mass_or_fitted_coefficient_targets": True,
            "common_target_family_path_candidate_was_frozen_before_validation": True,
            "common_target_wij_scaffold_is_not_promoted_to_physical_family_connection": True,
            "common_target_coboundary_transport_is_flat_and_cannot_supply_nonzero_loop_holonomy": True,
            "nonflat_cp_capable_family_connection_requires_additional_path_dependent_structure": True,
            "terminal_cycle_nontriviality_was_seen_before_formalization_so_not_prospective": True,
            "terminal_cycle_nontrivial_wilson_loop_is_not_equated_with_physical_cp": True,
            "terminal_cycle_loop_is_not_promoted_to_ckm_or_pmns": True,
            "terminal_cycle_family_interpretation_remains_conditional_on_physical_binding": True,
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
