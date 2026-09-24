#!/usr/bin/env python3
"""Deterministic control gate for TIR fractal-orbital gravity derivation v0.1."""
from __future__ import annotations
import json, math
from pathlib import Path

TOL=5e-12

def mm(a,b): return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)) for i in range(3))
def ms(a,b): return tuple(tuple(a[i][j]-b[i][j] for j in range(3)) for i in range(3))
def smul(s,a): return tuple(tuple(s*a[i][j] for j in range(3)) for i in range(3))
def maxm(a,b): return max(abs(a[i][j]-b[i][j]) for i in range(3) for j in range(3))
def comm(a,b): return ms(mm(a,b),mm(b,a))

def main():
    checks=[]
    kappa=math.log(2.0)/(24.0*math.pi)
    checks.append({"name":"canonical_kappa_numeric","pass":abs(kappa-0.009193150006360484)<1e-16,"value":kappa})

    eb=es=ec=0.0
    for chi in [-4.0,-1.75,-0.2,0.0,0.3,1.2,3.5]:
        q=math.tanh(chi/2.0)
        beta=math.tanh(chi); beta2=2*q/(1+q*q)
        sech=1/math.cosh(chi); sech2=(1-q*q)/(1+q*q)
        eb=max(eb,abs(beta-beta2)); es=max(es,abs(sech-sech2))
        ec=max(ec,abs(beta*beta+sech*sech-1))
    checks += [
        {"name":"poincare_half_rapidity_beta_identity","pass":eb<TOL,"max_error":eb},
        {"name":"poincare_half_rapidity_sech_identity","pass":es<TOL,"max_error":es},
        {"name":"beta_sech_unit_identity","pass":ec<TOL,"max_error":ec},
    ]

    kx=((0.,1.,0.),(1.,0.,0.),(0.,0.,0.))
    ky=((0.,0.,1.),(0.,0.,0.),(1.,0.,0.))
    jz=((0.,0.,0.),(0.,0.,-1.),(0.,1.,0.))
    le=maxm(comm(kx,ky),smul(-1.,jz))
    checks.append({"name":"noncommuting_boosts_generate_rotation","pass":le<TOL,"max_error":le})

    G=6.67430e-11; c=299792458.0
    pe=ne=0.0
    for M in [1e20,1e25,1e30]:
        rs=2*G*M/(c*c)
        for factor in [1.2,2.,10.,1e4]:
            R=factor*rs; v=math.sqrt(2*G*M/R)
            gf=-c*c+v*v
            gs=-(1-2*G*M/(c*c*R))*c*c
            pe=max(pe,abs(gf-gs)/(c*c))
            chi=math.atanh(v/c)
            phi=-.5*c*c*math.tanh(chi)**2
            ne=max(ne,abs(phi+G*M/R)/max(1.,abs(G*M/R)))
    checks += [
        {"name":"schwarzschild_pg_gtt_control","pass":pe<2e-15,"max_relative_error":pe},
        {"name":"schwarzschild_control_newton_potential","pass":ne<2e-15,"max_relative_error":ne},
    ]

    fe=ae=0.0
    for a,H,Hdot,R,dt,dR in [
        (.7,.03,-.002,2.,.1,.004),(1.,.10,.005,5.,-.2,.02),(2.4,.008,-.00002,100.,.7,.13)
    ]:
        dr=(dR-H*R*dt)/a
        fe=max(fe,abs(a*a*dr*dr-(dR-H*R*dt)**2))
        material=Hdot*R+(H*R)*H
        ae=max(ae,abs(material-(Hdot+H*H)*R))
    checks += [
        {"name":"flat_flrw_physical_radius_flow_identity","pass":fe<TOL,"max_error":fe},
        {"name":"hubble_flow_material_acceleration_identity","pass":ae<TOL,"max_error":ae},
    ]

    root=Path(__file__).resolve().parents[3]
    doc=(root/"TIR/foundations/TIR_FRACTAL_ORBITAL_INFORMATIONAL_HOLONOMIC_GRAVITY_V0_1.md").read_text(encoding="utf-8")
    cur=(root/"TIR/CURRENT_STATUS.md").read_text(encoding="utf-8")
    markers=[
        "PURE_LOCAL_LORENTZ_RELABELING_AS_GRAVITY" in doc,
        "T^a(\\omega_{\\rm LC})=0" in doc,
        "R^a{}_b(\\omega_{\\rm TP})=0" in doc,
        "SOURCE_TO_DIMENSIONLESS_RAPIDITY_BINDING = OPEN" in doc,
        "FRACTAL_ORBITAL_GRAVITY" in cur,
    ]
    checks.append({"name":"claim_firewalls_and_status_markers","pass":all(markers),"markers":markers})

    passed=all(x["pass"] for x in checks)
    receipt={
        "schema":"TIR_FRACTAL_ORBITAL_INFORMATIONAL_HOLONOMIC_GRAVITY_VALIDATION_V0_1",
        "technical_status":"PASS" if passed else "FAIL",
        "verdict":"PASS_EXACT_CONTROLS_PHYSICAL_BINDING_OPEN" if passed else "FAIL_CONTROL_GATE",
        "canon_allowed":False,
        "exact_controls":{"hyperbolic_rapidity":"PASS","lorentz_lie_commutator":"PASS","schwarzschild_pg":"PASS","flat_flrw_flow":"PASS"} if passed else {},
        "open_gates":[
            "SOURCE_TO_DIMENSIONLESS_RAPIDITY_BINDING",
            "ORBITAL_RECURSION_TO_UNIQUE_PHYSICAL_COFRAME",
            "DYNAMICAL_FIELD_EQUATION_FOR_V_FO",
            "LATE_TIME_ACCELERATION_WITHOUT_RETUNING",
            "LOCAL_PPN_LENSING_GW_VALIDATION_AFTER_BINDING",
        ],
        "checks":checks,
    }
    print(json.dumps(receipt,indent=2,sort_keys=True))
    if not passed: raise SystemExit(1)

if __name__=="__main__": main()
