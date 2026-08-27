#!/usr/bin/env python3
"""Stage 35: derive a Hermitian up/down family pair from the archived pre-CKM cross-Gram."""
import json
import numpy as np

SOURCE_BLOB_SHA = "9394ca738bc41ab78b084cd03202016fa0c9bb05"
O_UD = np.array([
    [ 0.4135652625510,  0.1727254809150, -0.0920240308652],
    [-0.1786581699140, -0.4072018579720,  0.8597118285350],
    [ 0.0375262746218,  0.2427361855910,  0.1373170397680],
], dtype=float)

H_U = O_UD @ O_UD.T
H_D = O_UD.T @ O_UD

def oriented_eigh(h):
    vals, vecs = np.linalg.eigh(h)
    order = np.argsort(vals)[::-1]
    vals = vals[order]
    vecs = vecs[:, order]
    for j in range(vecs.shape[1]):
        pivot = int(np.argmax(np.abs(vecs[:, j])))
        if vecs[pivot, j] < 0:
            vecs[:, j] *= -1
    if np.linalg.det(vecs) < 0:
        vecs[:, -1] *= -1
    return vals, vecs

eval_u, U_U = oriented_eigh(H_U)
eval_d, U_D = oriented_eigh(H_D)
V_REL = U_U.T @ U_D

hermitian_u_res = float(np.max(np.abs(H_U - H_U.T)))
hermitian_d_res = float(np.max(np.abs(H_D - H_D.T)))
commutator = H_U @ H_D - H_D @ H_U
commutator_inf = float(np.linalg.norm(commutator, ord=np.inf))
spectral_match = float(np.max(np.abs(eval_u - eval_d)))
unitarity_res = float(np.max(np.abs(V_REL.T @ V_REL - np.eye(3))))
det_res = float(abs(np.linalg.det(V_REL) - 1.0))
jarlskog_real = float(np.imag(
    V_REL[0,0] * V_REL[1,1] * np.conj(V_REL[0,1]) * np.conj(V_REL[1,0])
))

tol = 1e-12
mechanism_pass = (
    hermitian_u_res < tol
    and hermitian_d_res < tol
    and commutator_inf > tol
    and spectral_match < tol
    and unitarity_res < tol
    and det_res < tol
)
status = "PASS_WITH_INPUT_PROVENANCE_AND_CP_BOUNDARY" if mechanism_pass else "FAIL"

out = {
    "schema": "TIR_POLYGONAL_STAGE35_HERMITIAN_FAMILY_PAIR_V0_1",
    "status": status,
    "source_matrix_blob_sha": SOURCE_BLOB_SHA,
    "source_label": "up_down_basis_overlap_not_CKM",
    "operators": {
        "definition_H_u": "O_ud O_ud^T",
        "definition_H_d": "O_ud^T O_ud",
        "eigenvalues_H_u": eval_u.tolist(),
        "eigenvalues_H_d": eval_d.tolist(),
    },
    "checks": {
        "H_u_hermitian_residual": hermitian_u_res,
        "H_d_hermitian_residual": hermitian_d_res,
        "commutator_inf_norm": commutator_inf,
        "shared_spectrum_residual": spectral_match,
        "relative_diagonalizer_unitarity_residual": unitarity_res,
        "relative_diagonalizer_det_minus_one_abs": det_res,
        "relative_diagonalizer": V_REL.tolist(),
        "jarlskog_of_real_relative_diagonalizer": jarlskog_real,
    },
    "provenance_boundary": {
        "uses_observed_mass_in_source": False,
        "uses_observed_mixing_in_source": False,
        "heavy_quark_orientation_rows": "old_doc_bridge_ansatz_quarantined",
        "physical_promotion": "BLOCKED_PENDING_CLEAN_SECTOR_OPERATOR",
    },
    "cp_boundary": "The archived cross-Gram is real, so this construction yields an SO(3) subset of SU(3)_F and J=0. A complex TIR-native holonomy is required for CP violation.",
}
print(json.dumps(out, indent=2, sort_keys=True))
raise SystemExit(0 if mechanism_pass else 1)
