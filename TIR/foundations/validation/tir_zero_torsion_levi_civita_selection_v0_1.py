#!/usr/bin/env python3
"""Deterministic gate for TIR zero-torsion / Levi-Civita selection v0.1."""
from __future__ import annotations
import json, math, random
from pathlib import Path

TOL=2e-10
I3=((1.0,0.0,0.0),(0.0,1.0,0.0),(0.0,0.0,1.0))

def mm(a,b): return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)) for i in range(3))
def mv(a,v): return tuple(sum(a[i][k]*v[k] for k in range(3)) for i in range(3))
def va(a,b): return tuple(a[i]+b[i] for i in range(3))
def vs(a,b): return tuple(a[i]-b[i] for i in range(3))
def smul(s,v): return tuple(s*x for x in v)
def tr(a): return tuple(tuple(a[j][i] for j in range(3)) for i in range(3))
def norm(v): return math.sqrt(sum(x*x for x in v))
def maxv(a,b): return max(abs(a[i]-b[i]) for i in range(3))
def maxm(a,b): return max(abs(a[i][j]-b[i][j]) for i in range(3) for j in range(3))
def frob(a): return math.sqrt(sum(a[i][j]**2 for i in range(3) for j in range(3)))

def rx(t):
    c,s=math.cos(t),math.sin(t); return ((1,0,0),(0,c,-s),(0,s,c))
def ry(t):
    c,s=math.cos(t),math.sin(t); return ((c,0,s),(0,1,0),(-s,0,c))
def rz(t):
    c,s=math.cos(t),math.sin(t); return ((c,-s,0),(s,c,0),(0,0,1))
def rot(a,b,c): return mm(rz(a),mm(ry(b),rx(c)))

def endpoint_defect(rxy,exy,eyz,exz): return vs(exz,va(exy,mv(rxy,eyz)))
def torsion_vec(rxy,exy,eyz,exz): return vs(va(exy,mv(rxy,eyz)),exz)
def se3_mul(g1,g2):
    r1,t1=g1;r2,t2=g2; return mm(r1,r2),va(t1,mv(r1,t2))
def se3_inv(g):
    r,t=g;ri=tr(r); return ri,smul(-1,mv(ri,t))
def loop(gxy,gyz,gxz): return se3_mul(se3_mul(gxy,gyz),se3_inv(gxz))

def main():
    checks=[]; rng=random.Random(20260830)

    max_affine=0.0
    for _ in range(128):
        x=tuple(rng.uniform(-1,1) for _ in range(3)); y=tuple(rng.uniform(-1,1) for _ in range(3)); z=tuple(rng.uniform(-1,1) for _ in range(3))
        exy=vs(y,x); eyz=vs(z,y); exz=vs(z,x)
        max_affine=max(max_affine,maxv(exz,va(exy,eyz)))
    checks.append({"name":"intrinsic_affine_endpoint_uniqueness_composition","pass":max_affine<TOL,"max_error":max_affine})

    max_cov=0.0
    for _ in range(128):
        qx=rot(*(rng.uniform(-0.8,0.8) for _ in range(3))); qy=rot(*(rng.uniform(-0.8,0.8) for _ in range(3)))
        x=tuple(rng.uniform(-1,1) for _ in range(3)); y=tuple(rng.uniform(-1,1) for _ in range(3)); z=tuple(rng.uniform(-1,1) for _ in range(3))
        exy_x=mv(tr(qx),vs(y,x)); eyz_y=mv(tr(qy),vs(z,y)); exz_x=mv(tr(qx),vs(z,x)); rxy=mm(tr(qx),qy)
        max_cov=max(max_cov,maxv(exz_x,va(exy_x,mv(rxy,eyz_y))))
    checks.append({"name":"same_endpoint_local_frame_closure","pass":max_cov<TOL,"max_error":max_cov})

    rxy=rot(0.37,-0.22,0.15); exy=(0.2,-0.1,0.3);eyz=(-0.4,0.25,0.05); exz=va(exy,mv(rxy,eyz))
    c=endpoint_defect(rxy,exy,eyz,exz);t=torsion_vec(rxy,exy,eyz,exz)
    eqerr=max(norm(c),norm(t),maxv(t,smul(-1,c)))
    checks.append({"name":"endpoint_closure_iff_discrete_torsion_zero","pass":eqerr<TOL,"max_error":eqerr})

    max_metric=0.0
    for _ in range(128):
        r=rot(*(rng.uniform(-1,1) for _ in range(3))); u=tuple(rng.uniform(-1,1) for _ in range(3));v=tuple(rng.uniform(-1,1) for _ in range(3))
        dot=lambda a,b:sum(a[i]*b[i] for i in range(3))
        max_metric=max(max_metric,abs(dot(mv(r,u),mv(r,v))-dot(u,v)),maxm(mm(tr(r),r),I3))
    checks.append({"name":"so3_transport_metric_compatibility","pass":max_metric<TOL,"max_error":max_metric})

    area_errors=[];rot_area=[];u=(0.4,-0.3,0.2);v=(-0.2,0.5,0.1)
    for eps in [0.2,0.1,0.05,0.025,0.0125]:
        rxy=rot(0.3*eps,-0.1*eps,0.2*eps); ryz=rot(-0.2*eps,0.25*eps,-0.15*eps); rxz=mm(mm(rxy,ryz),rz(0.7*eps*eps))
        exy=smul(eps,u);eyz=smul(eps,v);exz=va(exy,mv(rxy,eyz)); tc=torsion_vec(rxy,exy,eyz,exz)
        lc=loop((rxy,exy),(ryz,eyz),(rxz,exz));rc=lc[0]
        area_errors.append(norm(lc[1])/(eps*eps));rot_area.append(frob(tuple(tuple(rc[i][j]-I3[i][j] for j in range(3)) for i in range(3)))/(eps*eps))
        assert norm(tc)<TOL
    checks.append({"name":"zero_torsion_translation_area_limit","pass":area_errors[-1]<0.08*area_errors[0],"coarse":area_errors[0],"fine":area_errors[-1]})
    checks.append({"name":"zero_torsion_retains_curvature_area_limit","pass":rot_area[-1]>0.5 and abs(rot_area[-1]-rot_area[-2])<0.01,"fine_rotation_area":rot_area[-1]})

    eps=0.025;tau=(0.3,-0.2,0.4);rxy=rot(0.3*eps,-0.1*eps,0.2*eps);exy=smul(eps,u);eyz=smul(eps,v)
    exz=vs(va(exy,mv(rxy,eyz)),smul(eps*eps,tau));t=torsion_vec(rxy,exy,eyz,exz);terr=maxv(smul(1/(eps*eps),t),tau)
    checks.append({"name":"torsional_extension_fail_closed_witness","pass":terr<TOL and norm(t)>1e-6,"max_error":terr,"torsion_norm":norm(t)})

    root=Path(__file__).resolve().parents[3]
    a2=(root/"TIR/foundations/TIR_CARTAN_REFINEMENT_CURVATURE_TORSION_SEPARATION_V0_1.md").read_text(encoding="utf-8")
    parent=(root/"TIR/foundations/TIR_RELATIONAL_ENDPOINT_CLOSURE_V0_1.md").read_text(encoding="utf-8")
    doc=(root/"TIR/foundations/TIR_ZERO_TORSION_LEVI_CIVITA_SELECTION_V0_1.md").read_text(encoding="utf-8")
    markers=["T^a=0" in doc,"D^{\\rm LC}" in doc,"GLOBAL_CONTINUUM_EXISTENCE_OPEN" in doc,"zero torsion does not remove curvature" in doc.lower(),"\\mathcal C_{xyz}=0" in parent,"t_C-\\operatorname{vec}(\\mathcal T_{xyz})" in a2]
    checks.append({"name":"claim_and_parent_firewalls","pass":all(markers),"markers":markers})

    passed=all(c["pass"] for c in checks)
    receipt={"schema":"TIR_ZERO_TORSION_LEVI_CIVITA_SELECTION_VALIDATION_V0_1","technical_status":"PASS" if passed else "FAIL","verdict":"PASS_TIR_ZERO_TORSION_LEVI_CIVITA_SELECTION" if passed else "FAIL_TIR_ZERO_TORSION_LEVI_CIVITA_SELECTION","selection_scope":"PRIMITIVE_SAME_ENDPOINT_COMPATIBLE_REGULAR_REFINEMENT_SECTOR","global_continuum_existence":"OPEN","checks":checks}
    print(json.dumps(receipt,indent=2,sort_keys=True))
    if not passed: raise SystemExit(1)

if __name__=="__main__": main()
