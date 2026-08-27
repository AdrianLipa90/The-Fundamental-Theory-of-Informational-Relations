#!/usr/bin/env python3
from __future__ import annotations
import json
import numpy as np

W=np.array([
 [0.40923698590418567,0.42125751604075806,0.24721654499317047],
 [0.24273860188209057,0.2361961887844993,0.41544523219348306],
 [0.2653425764457501,0.26957519099026234,0.3763372596224964],
],dtype=float)
U,s,Vh=np.linalg.svd(W)
R=U@Vh
I=np.eye(3)
rank=int(np.linalg.matrix_rank(W))
unitarity=float(np.max(np.abs(W.T@W-I)))
polar_orth=float(np.max(np.abs(R.T@R-I)))
polar_dist=float(np.linalg.norm(W-R,ord='fro'))
detW=float(np.linalg.det(W))
detR=float(np.linalg.det(R))
checks={
    "full_rank_numerically":rank==3,
    "small_third_singular_direction":float(np.min(s))<0.01,
    "raw_open_holonomy_not_unitary":unitarity>1e-3,
    "polar_factor_available":float(np.min(s))>1e-12,
    "polar_factor_orthogonal":polar_orth<1e-12,
    "polar_factor_orientation_reversing":detR<0,
}
report={
    "schema":"tir.polygonal.stage31.white-thread-unitarity/v0.1",
    "status":"PASS_BLOCKED" if all(checks.values()) else "FAIL",
    "checks":checks,
    "singular_values":s.tolist(),
    "rank":rank,
    "det_raw":detW,
    "raw_unitarity_max_abs_residual":unitarity,
    "polar_det":detR,
    "polar_orthogonality_max_abs_residual":polar_orth,
    "raw_to_polar_frobenius_distance":polar_dist,
    "direct_physical_mixing_promotion":"BLOCKED",
    "observed_CKM_used":False,
    "observed_masses_used":False,
}
print(json.dumps(report,indent=2,sort_keys=True))
raise SystemExit(0 if report["status"]=="PASS_BLOCKED" else 1)
