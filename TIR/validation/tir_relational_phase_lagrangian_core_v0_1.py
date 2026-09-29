#!/usr/bin/env python3
"""Structural checks for TIR relational phase Lagrangian core v0.1."""
from __future__ import annotations
import json, math, cmath

def main():
    phases=(0.0,0.3,math.pi,5.2)
    closure=[]
    ok=True
    for x in phases:
        residual=abs(cmath.exp(1j*(x+2*math.pi))-cmath.exp(1j*x))
        good=residual<1e-12
        ok &= good
        closure.append({"chi":x,"residual":residual,"pass":good})

    # finite gauge-covariance control:
    # chi' = chi-lambda(q), A' = A + d lambda
    qdot=1.7; chidot=-0.4; A=0.6; dlambda=0.23
    original=chidot+A*qdot
    transformed=(chidot-dlambda*qdot)+(A+dlambda)*qdot
    gauge=abs(original-transformed)<1e-15
    ok &= gauge

    Iphi=2.3; J0=-0.2
    J=Iphi*original+J0
    inverse=(J-J0)/Iphi
    momentum=abs(inverse-original)<1e-15
    ok &= momentum

    receipt={
      "schema":"TIR_RELATIONAL_PHASE_LAGRANGIAN_CORE_V0_1",
      "canonical_nonlogical_axiom_count":0,
      "phase_carrier":"U(1) ~= S1",
      "closure_rows":closure,
      "gauge_covariant_velocity":gauge,
      "phase_momentum_inversion":momentum,
      "physical_time_binding":"SEPARATE",
      "physical_connection_binding":"SEPARATE",
      "technical_status":"PASS" if ok else "FAIL",
    }
    print(json.dumps(receipt,indent=2,sort_keys=True))
    if not ok: raise SystemExit(1)

if __name__=="__main__": main()
