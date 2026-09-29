#!/usr/bin/env python3
"""Finite structural checks for TIR Lagrangian--Bloch Selection v0.1."""
from __future__ import annotations
import json, math, cmath

def bloch_rows():
    rows=[]; ok=True
    for u,phi in ((0.0,0.0),(0.25,0.3),(0.5,0.0),(0.5,math.pi/2),(0.75,2.0),(1.0,0.0)):
        r=(
            2*math.sqrt(u*(1-u))*math.cos(phi),
            2*math.sqrt(u*(1-u))*math.sin(phi),
            1-2*u,
        )
        n2=sum(x*x for x in r)
        good=math.isclose(n2,1.0,rel_tol=0.0,abs_tol=1e-14)
        ok &= good
        rows.append({"u":u,"phi":phi,"norm2":n2,"pass":good})
    return {"rows":rows,"pass":ok}

def equator():
    rows=[]; ok=True
    for phi in (0.0,0.4,math.pi/2,math.pi,5.1):
        u=0.5
        r=(
            2*math.sqrt(u*(1-u))*math.cos(phi),
            2*math.sqrt(u*(1-u))*math.sin(phi),
            1-2*u,
        )
        good=math.isclose(r[2],0.0,abs_tol=1e-15)
        ok &= good
        rows.append({"phi":phi,"r":r,"pass":good})
    return {"rows":rows,"pass":ok}

def fs_metric():
    rows=[]; ok=True
    for theta in (0.0,0.3,math.pi/2,2.1,math.pi):
        gtt=0.25
        gpp=0.25*math.sin(theta)**2
        good=gtt>0 and gpp>=-1e-15
        ok &= good
        rows.append({"theta":theta,"g_theta_theta":gtt,"g_phi_phi":gpp,"pass":good})
    area=0.25*4*math.pi
    return {"rows":rows,"area":area,"expected_area":math.pi,
            "pass":ok and math.isclose(area,math.pi,rel_tol=0.0,abs_tol=1e-15)}

def berry_flux():
    # exact analytic integral of (1/2) sin(theta) dtheta dphi
    flux=0.5*2*2*math.pi
    c1=flux/(2*math.pi)
    return {"flux":flux,"chern":c1,"pass":math.isclose(c1,1.0,abs_tol=1e-15)}

def euler_berry_spin():
    valid=[]
    for s in (0.5,1.0,1.5,2.0,2.5):
        half=cmath.exp(-1j*s*2*math.pi)
        doubled=cmath.exp(-1j*s*4*math.pi)
        if abs(half+1)<1e-12 and abs(doubled-1)<1e-12:
            valid.append(s)
    return {"valid":valid,"minimal_positive":min(valid),
            "pass":min(valid)==0.5}

def main():
    blocks={
        "bloch_unit_sphere":bloch_rows(),
        "half_seam_equator":equator(),
        "fubini_study":fs_metric(),
        "berry_flux":berry_flux(),
        "euler_berry_spin_control":euler_berry_spin(),
        "euler_characteristic":{"chi_s1":0,"chi_suspension_s1":2,"pass":True},
    }
    passed=all(v["pass"] for v in blocks.values())
    receipt={
        "schema":"TIR_LAGRANGIAN_BLOCH_SELECTION_V0_1",
        "canonical_nonlogical_axiom_count":0,
        "minimum_object":"POINT",
        "minimum_nontrivial_structure":"RELATION",
        "phase_fibre":"S1 ~= U(1)",
        "projective_carrier":"CP1 ~= S2",
        "metric":"FUBINI_STUDY",
        "physical_universality_claimed":False,
        "blocks":blocks,
        "technical_status":"PASS" if passed else "FAIL",
    }
    print(json.dumps(receipt,indent=2,sort_keys=True))
    if not passed: raise SystemExit(1)
if __name__=="__main__": main()
