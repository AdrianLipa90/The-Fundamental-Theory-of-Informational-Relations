#!/usr/bin/env python3
"""Deterministic v12 audit for Chapter 7 holonomy / SE(3) / torsion chain."""
from __future__ import annotations
import json, math

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
def mv(A,v): return [sum(A[i][j]*v[j] for j in range(3)) for i in range(3)]
def mt(A): return [list(x) for x in zip(*A)]
def vadd(a,b): return [x+y for x,y in zip(a,b)]
def vsub(a,b): return [x-y for x,y in zip(a,b)]
def vscale(c,a): return [c*x for x in a]
def eye(): return [[1,0,0],[0,1,0],[0,0,1]]
def close_vec(a,b,tol=1e-12): return all(abs(x-y)<tol for x,y in zip(a,b))
def close_mat(A,B,tol=1e-12): return all(abs(A[i][j]-B[i][j])<tol for i in range(3) for j in range(3))
def norm(v): return math.sqrt(sum(x*x for x in v))
def compose(g1,g2):
    R1,t1=g1; R2,t2=g2
    return (matmul(R1,R2), vadd(t1,mv(R1,t2)))
def inv(g):
    R,t=g; Rt=mt(R)
    return (Rt,vscale(-1,mv(Rt,t)))

Q_a=eye()
Q_b=[[0,-1,0],[1,0,0],[0,0,1]]
Q_c=[[1,0,0],[0,0,-1],[0,1,0]]
r_a=[1,2,3]; r_b=[-2,1,4]; r_c=[0,-3,2]

def atlas(Q_src,r_src,Q_dst,r_dst):
    Qt=mt(Q_dst)
    return (matmul(Qt,Q_src), mv(Qt,vsub(r_src,r_dst)))

G_ba=atlas(Q_a,r_a,Q_b,r_b)
G_cb=atlas(Q_b,r_b,Q_c,r_c)
G_ca=atlas(Q_a,r_a,Q_c,r_c)
cocycle=compose(G_cb,G_ba)
atlas_cocycle=close_mat(cocycle[0],G_ca[0]) and close_vec(cocycle[1],G_ca[1])
atlas_inverse=close_mat(compose(inv(G_ba),G_ba)[0],eye()) and close_vec(compose(inv(G_ba),G_ba)[1],[0,0,0])
atlas_loop=compose(inv(G_ca),compose(G_cb,G_ba))
pure_atlas_loop=close_mat(atlas_loop[0],eye()) and close_vec(atlas_loop[1],[0,0,0])

Rxy=Q_b
Ryz=[[1,0,0],[0,-1,0],[0,0,-1]]
Rxz=matmul(Rxy,Ryz)
exy=[1,2,0]
eyz=[-1,1,3]
exz=[4,-2,1]
c=vsub(exz,vadd(exy,mv(Rxy,eyz)))

Gxy=(Rxy,exy); Gyz=(Ryz,eyz); Gxz=(Rxz,exz)
GC=compose(compose(Gxy,Gyz),inv(Gxz))
rot_closed=close_mat(GC[0],eye())
loop_translation=GC[1]
loop_defect=close_vec(loop_translation,vscale(-1,c))

T=vsub(vadd(exy,mv(Rxy,eyz)),exz)
solder_identity=close_vec(T,vscale(-1,c))
torsion_loop_identity=close_vec(T,loop_translation)
norm_identity=abs(norm(T)-norm(c))<1e-12 and abs(norm(T)-norm(loop_translation))<1e-12

Qx=Q_c
cprime=mv(Qx,c)
Tprime=mv(Qx,T)
covariance=abs(norm(cprime)-norm(c))<1e-12 and abs(norm(Tprime)-norm(T))<1e-12 and close_vec(Tprime,vscale(-1,cprime))

checks={
 "atlas_three_chart_cocycle":atlas_cocycle,
 "atlas_pair_inverse":atlas_inverse,
 "pure_atlas_loop_identity":pure_atlas_loop,
 "rotationally_consistent_connection_loop":rot_closed,
 "loop_translation_equals_minus_endpoint_defect":loop_defect,
 "discrete_solder_equals_minus_endpoint_defect":solder_identity,
 "loop_translation_equals_solder_torsion_vector":torsion_loop_identity,
 "torsion_norm_identity":norm_identity,
 "local_frame_covariance_of_scalar_witness":covariance,
}
passed=all(checks.values())
payload={
 "schema":"TIR_V12_CH07_HOLONOMY_SE3_TORSION_V0_1",
 "technical_status":"PASS" if passed else "FAIL",
 "atlas_firewall":"pure atlas cocycle => identity closed loop",
 "connection_lift":"G_xy^nabla=(R_xy,e_xy)",
 "torsion_crosswalk":"vec(T_xyz)=t_C=-c_xyz",
 "continuum_gate":"refining-family convergence to Cartan torsion/curvature",
 "checks":checks,
}
print(json.dumps(payload,indent=2,sort_keys=True))
raise SystemExit(0 if passed else 1)
