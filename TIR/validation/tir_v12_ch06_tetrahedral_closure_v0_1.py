#!/usr/bin/env python3
"""Deterministic v12 audit for Chapter 6 tetrahedral closure."""
from __future__ import annotations
import json, math

s=1/math.sqrt(3)
N=[
 ( s, s, s),
 ( s,-s,-s),
 (-s, s,-s),
 (-s,-s, s),
]
def dot(a,b): return sum(x*y for x,y in zip(a,b))
zero=tuple(sum(v[i] for v in N) for i in range(3))
first_moment=all(abs(x)<1e-12 for x in zero)
gram=[[dot(N[i],N[j]) for j in range(4)] for i in range(4)]
gram_ok=all(abs(gram[i][j]-(1.0 if i==j else -1/3))<1e-12 for i in range(4) for j in range(4))
Q=[[sum(v[i]*v[j] for v in N) for j in range(3)] for i in range(3)]
second_moment=all(abs(Q[i][j]-((4/3) if i==j else 0.0))<1e-12 for i in range(3) for j in range(3))

edge_vec=tuple(N[0][i]-N[1][i] for i in range(3))
edge2=dot(edge_vec,edge_vec)
edge_ok=abs(edge2-8/3)<1e-12
edge=math.sqrt(edge2)
volume=edge**3/(6*math.sqrt(2))
volume_ok=abs(volume-8/(9*math.sqrt(3)))<1e-12

r=(0.2,-0.3,0.4)
p=[0.25*(1+dot(r,n)) for n in N]
prob_norm=abs(sum(p)-1)<1e-12
recon=tuple(3*sum(p[a]*N[a][i] for a in range(4)) for i in range(3))
reconstruction=all(abs(recon[i]-r[i])<1e-12 for i in range(3))
pair_overlap=all(abs(0.5*(1+gram[i][j])-1/3)<1e-12 for i in range(4) for j in range(4) if i!=j)

cos_chi=-1/3
cos_alpha=(cos_chi-cos_chi*cos_chi)/(1-cos_chi*cos_chi)
alpha=math.acos(cos_alpha)
fs_face=(3*alpha-math.pi)/4
fs_ok=abs(fs_face-math.pi/4)<1e-12
shape=volume/(4*fs_face)
shape_ok=abs(shape-8/(9*math.sqrt(3)*math.pi))<1e-12

checks={
 "zero_first_moment":first_moment,
 "isotropic_second_moment":second_moment,
 "regular_tetrahedral_gram":gram_ok,
 "edge_squared_8_over_3":edge_ok,
 "volume_8_over_9sqrt3":volume_ok,
 "sic_probabilities_normalize":prob_norm,
 "sic_pair_overlap_1_over_3":pair_overlap,
 "sic_reconstructs_bloch_vector":reconstruction,
 "fs_face_area_pi_over_4":fs_ok,
 "dual_shape_coefficient":shape_ok,
}
passed=all(checks.values())
payload={
 "schema":"TIR_V12_CH06_TETRAHEDRAL_CLOSURE_V0_1",
 "technical_status":"PASS" if passed else "FAIL",
 "minimal_full_isotropy_valence":4,
 "gram_off_diagonal":"-1/3",
 "edge":"sqrt(8/3)",
 "euclidean_volume":"8/(9*sqrt(3))",
 "fs_total_area":"pi",
 "dual_shape_coefficient":"8/(9*sqrt(3)*pi)",
 "checks":checks,
}
print(json.dumps(payload,indent=2,sort_keys=True))
raise SystemExit(0 if passed else 1)
