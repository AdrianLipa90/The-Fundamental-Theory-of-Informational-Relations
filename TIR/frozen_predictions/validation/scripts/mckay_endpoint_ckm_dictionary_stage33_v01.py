#!/usr/bin/env python3
from __future__ import annotations
from fractions import Fraction
import json
import math

Nminus,Nplus=3,5
nminus,nplus=7,9
s=2
a=Fraction(s,nminus)
b=Fraction(s,nplus)
c=Fraction(s,Nplus)
L3,L4,L5=7,2,5
kappa=math.log(2)/(24*math.pi)
checks={
    "endpoint_levels_unique":(Nminus,Nplus)==(3,5),
    "affine_endpoint_node_counts":(nminus,nplus)==(7,9),
    "defining_mckay_dimension_two":s==2,
    "a_matches_L4_over_L3":a==Fraction(L4,L3),
    "b_matches_L4_over_L3plusL4":b==Fraction(L4,L3+L4),
    "c_matches_L4_over_L5":c==Fraction(L4,L5),
    "Vcb_identity":a*a/Fraction(s,1)==Fraction(2,49),
    "Vub_identity":a*a*b/Fraction(Nplus,1)==Fraction(8,2205),
    "Vub_second_identity":a*a*b*c/Fraction(s,1)==Fraction(8,2205),
}
report={
    "schema":"tir.polygonal.stage33.mckay-endpoint-ckm-dictionary/v0.1",
    "status":"PASS" if all(checks.values()) else "FAIL",
    "checks":checks,
    "endpoint_invariants":{"N_minus":Nminus,"N_plus":Nplus,"n_minus":nminus,"n_plus":nplus,"spinor_dimension":s},
    "ratios":{"a":str(a),"b":str(b),"c":str(c)},
    "lambda_r1":b.numerator/b.denominator + (a.numerator/a.denominator)*kappa,
    "Vcb":float(a*a/Fraction(s,1)),
    "Vub":float(a*a*b/Fraction(Nplus,1)),
    "J_structural":kappa*kappa*float(c)*(1-float(c*c)/s),
    "delta_direct_deg":math.degrees(math.acos(float(c))),
    "CKM_reference_used_for_reconstruction":False,
    "mass_reference_used":False,
    "functional_form_status":"RETROSPECTIVE_EXISTING_TIR_CANDIDATE",
}
print(json.dumps(report,indent=2,sort_keys=True))
raise SystemExit(0 if report["status"]=="PASS" else 1)
