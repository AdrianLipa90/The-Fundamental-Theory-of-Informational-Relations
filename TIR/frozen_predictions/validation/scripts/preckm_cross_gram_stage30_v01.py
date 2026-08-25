#!/usr/bin/env python3
from __future__ import annotations
import json
import numpy as np

O=np.array([
 [0.413565262551,0.172725480915,-0.0920240308652],
 [-0.178658169914,-0.407201857972,0.859711828535],
 [0.0375262746218,0.242736185591,0.137317039768],
],dtype=float)

U,s,Vh=np.linalg.svd(O)
R=U@Vh
I=np.eye(3)
rank=int(np.linalg.matrix_rank(O))
unitarity=float(np.max(np.abs(O.T@O-I)))
polar_orth=float(np.max(np.abs(R.T@R-I)))
polar_dist=float(np.linalg.norm(O-R,ord='fro'))
detO=float(np.linalg.det(O))
detR=float(np.linalg.det(R))
checks={
    "full_rank":rank==3,
    "nontrivial_sector_misalignment":float(np.min(s))<0.99,
    "raw_cross_gram_not_unitary":unitarity>1e-3,
    "unique_polar_factor_available":float(np.min(s))>1e-12,
    "polar_factor_orthogonal":polar_orth<1e-12,
    "polar_factor_orientation_reversing":detR<0,
}
report={
    "schema":"tir.polygonal.stage30.preckm-cross-gram/v0.1",
    "status":"PASS_OPEN" if all(checks.values()) else "FAIL",
    "checks":checks,
    "singular_values":s.tolist(),
    "rank":rank,
    "det_raw":detO,
    "raw_unitarity_max_abs_residual":unitarity,
    "polar_factor":R.tolist(),
    "polar_det":detR,
    "polar_orthogonality_max_abs_residual":polar_orth,
    "raw_to_polar_frobenius_distance":polar_dist,
    "physical_mixing_promotion":"OPEN",
    "observed_CKM_used":False,
    "observed_masses_used":False,
}
print(json.dumps(report,indent=2,sort_keys=True))
raise SystemExit(0 if report["status"]=="PASS_OPEN" else 1)
