#!/usr/bin/env python3
"""Deterministic gate for TIR Cartan refinement / curvature-torsion separation v0.1."""
from __future__ import annotations

import json
import math
import random

TOL = 2e-10
I3 = ((1.0,0.0,0.0),(0.0,1.0,0.0),(0.0,0.0,1.0))


def mm(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)) for i in range(3))

def mv(a,v): return tuple(sum(a[i][k]*v[k] for k in range(3)) for i in range(3))
def va(a,b): return tuple(a[i]+b[i] for i in range(3))
def vs(a,b): return tuple(a[i]-b[i] for i in range(3))
def vn(a): return tuple(-x for x in a)
def smul(s,v): return tuple(s*x for x in v)
def transpose(a): return tuple(tuple(a[j][i] for j in range(3)) for i in range(3))
def norm(v): return math.sqrt(sum(x*x for x in v))
def maxv(a,b): return max(abs(a[i]-b[i]) for i in range(3))
def maxm(a,b): return max(abs(a[i][j]-b[i][j]) for i in range(3) for j in range(3))
def frob(a): return math.sqrt(sum(a[i][j]*a[i][j] for i in range(3) for j in range(3)))


def rx(t):
    c,s=math.cos(t),math.sin(t)
    return ((1.0,0.0,0.0),(0.0,c,-s),(0.0,s,c))
def ry(t):
    c,s=math.cos(t),math.sin(t)
    return ((c,0.0,s),(0.0,1.0,0.0),(-s,0.0,c))
def rz(t):
    c,s=math.cos(t),math.sin(t)
    return ((c,-s,0.0),(s,c,0.0),(0.0,0.0,1.0))
def rotation(a,b,c): return mm(rz(a),mm(ry(b),rx(c)))


def se3_mul(g_left,g_right):
    rl,tl=g_left; rr,tr=g_right
    return mm(rl,rr),va(tl,mv(rl,tr))

def se3_inverse(g):
    r,t=g; ri=transpose(r)
    return ri,vn(mv(ri,t))

def triangle_loop(gxy,gyz,gxz): return se3_mul(se3_mul(gxy,gyz),se3_inverse(gxz))

def discrete_solder_vector(rxy,exy,eyz,exz):
    return vs(va(exy,mv(rxy,eyz)),exz)

def rotational_loop(rxy,ryz,rxz): return mm(mm(rxy,ryz),transpose(rxz))

def curvature_correction(rxy,ryz,rxz,exz):
    h=rotational_loop(rxy,ryz,rxz)
    return mv(tuple(tuple(I3[i][j]-h[i][j] for j in range(3)) for i in range(3)),exz)

def slope(xs,ys):
    lx=[math.log(x) for x in xs]; ly=[math.log(y) for y in ys]
    mx=sum(lx)/len(lx); my=sum(ly)/len(ly)
    return sum((x-mx)*(y-my) for x,y in zip(lx,ly))/sum((x-mx)**2 for x in lx)


def main():
    checks=[]
    rng=random.Random(20260830)
    max_identity=0.0
    for _ in range(128):
        ang=[rng.uniform(-0.8,0.8) for _ in range(9)]
        rxy=rotation(*ang[:3]); ryz=rotation(*ang[3:6]); rxz=rotation(*ang[6:9])
        exy=tuple(rng.uniform(-1,1) for _ in range(3))
        eyz=tuple(rng.uniform(-1,1) for _ in range(3))
        exz=tuple(rng.uniform(-1,1) for _ in range(3))
        loop=triangle_loop((rxy,exy),(ryz,eyz),(rxz,exz))
        tors=discrete_solder_vector(rxy,exy,eyz,exz)
        corr=curvature_correction(rxy,ryz,rxz,exz)
        max_identity=max(max_identity,maxv(vs(loop[1],tors),corr))
    checks.append({"name":"general_loop_translation_decomposition","pass":max_identity<TOL,"max_error":max_identity})

    rxy=rotation(0.31,-0.17,0.09); ryz=rotation(-0.22,0.41,-0.13); rxz=mm(rxy,ryz)
    exy=(0.2,-0.3,0.4); eyz=(-0.1,0.25,0.35); exz=(0.5,-0.2,0.1)
    loop=triangle_loop((rxy,exy),(ryz,eyz),(rxz,exz)); tors=discrete_solder_vector(rxy,exy,eyz,exz)
    closed_error=max(maxm(loop[0],I3),maxv(loop[1],tors))
    checks.append({"name":"gate_a_rotational_closure_roundtrip","pass":closed_error<TOL,"max_error":closed_error})

    eps_values=[0.2,0.1,0.05,0.025,0.0125]
    tau0=(0.3,-0.2,0.4); u=(0.4,-0.3,0.2); v=(-0.2,0.5,0.1)
    torsion_errors=[]; correction_norms=[]; rotation_defects=[]; area_loop_errors=[]; decomp_errors=[]
    for eps in eps_values:
        rxy=rotation(0.30*eps,-0.10*eps,0.20*eps)
        ryz=rotation(-0.20*eps,0.25*eps,-0.15*eps)
        rxz=mm(mm(rxy,ryz),rz(0.70*eps*eps))
        exy=smul(eps,u); eyz=smul(eps,v)
        exz=vs(va(exy,mv(rxy,eyz)),smul(eps*eps,tau0))
        tors=discrete_solder_vector(rxy,exy,eyz,exz)
        loop=triangle_loop((rxy,exy),(ryz,eyz),(rxz,exz))
        h=rotational_loop(rxy,ryz,rxz); corr=curvature_correction(rxy,ryz,rxz,exz)
        torsion_errors.append(maxv(smul(1.0/(eps*eps),tors),tau0))
        correction_norms.append(norm(vs(loop[1],tors)))
        rotation_defects.append(frob(tuple(tuple(h[i][j]-I3[i][j] for j in range(3)) for i in range(3))))
        area_loop_errors.append(maxv(smul(1.0/(eps*eps),loop[1]),tau0))
        decomp_errors.append(maxv(vs(loop[1],tors),corr))

    max_tau=max(torsion_errors)
    checks.append({"name":"discrete_torsion_area_coefficient_frozen","pass":max_tau<TOL,"max_error":max_tau})
    max_decomp=max(decomp_errors)
    checks.append({"name":"curvature_correction_exact_on_refining_family","pass":max_decomp<TOL,"max_error":max_decomp})
    corr_slope=slope(eps_values,correction_norms)
    checks.append({"name":"curvature_contamination_is_third_order","pass":2.75<corr_slope<3.25,"observed_loglog_slope":corr_slope})
    rot_slope=slope(eps_values,rotation_defects)
    checks.append({"name":"rotational_holonomy_is_second_order","pass":1.85<rot_slope<2.15,"observed_loglog_slope":rot_slope})
    ratio=area_loop_errors[-1]/area_loop_errors[0]
    checks.append({"name":"translation_area_limit_matches_cartan_torsion_coefficient","pass":area_loop_errors[-1]<0.08*area_loop_errors[0],"coarse_error":area_loop_errors[0],"fine_error":area_loop_errors[-1],"fine_to_coarse_ratio":ratio})

    eps=0.025
    rxy=rotation(0.30*eps,-0.10*eps,0.20*eps); ryz=rotation(-0.20*eps,0.25*eps,-0.15*eps)
    rxz=mm(mm(rxy,ryz),rz(0.70*eps*eps)); exy=smul(eps,u); eyz=smul(eps,v); exz=va(exy,mv(rxy,eyz))
    tors=discrete_solder_vector(rxy,exy,eyz,exz); loop=triangle_loop((rxy,exy),(ryz,eyz),(rxz,exz)); h=rotational_loop(rxy,ryz,rxz)
    rot_nonzero=frob(tuple(tuple(h[i][j]-I3[i][j] for j in range(3)) for i in range(3)))
    checks.append({"name":"zero_torsion_does_not_force_zero_curvature","pass":norm(tors)<TOL and rot_nonzero>1e-6 and norm(loop[1])>0.0,"torsion_norm":norm(tors),"rotation_defect":rot_nonzero,"finite_loop_translation_from_curvature_order3":norm(loop[1])})

    qa=rotation(0.1,-0.2,0.3); qb=rotation(-0.3,0.4,-0.1); qc=rotation(0.2,0.1,-0.4)
    ra=(0.2,-0.1,0.4); rb=(-0.3,0.25,0.05); rc=(0.15,0.5,-0.2)
    def atlas(qt,rt,qs,rs): return mm(transpose(qt),qs),mv(transpose(qt),vs(rs,rt))
    gab=atlas(qa,ra,qb,rb); gbc=atlas(qb,rb,qc,rc); gac=atlas(qa,ra,qc,rc)
    atlas_loop=triangle_loop(gab,gbc,gac); atlas_err=max(maxm(atlas_loop[0],I3),norm(atlas_loop[1]))
    checks.append({"name":"pure_atlas_exact_zero_baseline","pass":atlas_err<TOL,"max_error":atlas_err})

    passed=all(c["pass"] for c in checks)
    receipt={
        "schema":"TIR_CARTAN_REFINEMENT_CURVATURE_TORSION_SEPARATION_VALIDATION_V0_1",
        "technical_status":"PASS" if passed else "FAIL",
        "verdict":"PASS_TIR_CARTAN_REFINEMENT_CURVATURE_TORSION_SEPARATION" if passed else "FAIL_TIR_CARTAN_REFINEMENT_CURVATURE_TORSION_SEPARATION",
        "exact_identity":"t_C = vec(T_triangle) + (I - R_C) e_xz",
        "small_loop_scaling":{"edge":"O(epsilon)","rotation_defect":"O(epsilon^2)","curvature_correction_to_translation":"O(epsilon^3)","discrete_torsion":"O(epsilon^2)","area_normalized_translation_limit":"same as discrete torsion limit"},
        "zero_torsion_selection":"DOWNSTREAM_GATE",
        "checks":checks,
    }
    print(json.dumps(receipt,indent=2,sort_keys=True))
    if not passed: raise SystemExit(1)

if __name__=="__main__": main()
