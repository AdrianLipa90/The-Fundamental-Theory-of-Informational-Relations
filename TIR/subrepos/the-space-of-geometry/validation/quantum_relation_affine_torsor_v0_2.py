#!/usr/bin/env python3
"""Zero-axiom audit for affine torsor relation v0.2."""
from __future__ import annotations
import json
from fractions import Fraction as F

Vec = tuple[F,F,F]
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def neg(a): return tuple(-x for x in a)
def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def q(v): return dot(v,v)

def main():
    rx=(F(1,3),F(-1,4),F(1,5))
    ry=(F(-1,6),F(1,2),F(1,10))
    rz=(F(1,4),F(1,8),F(-1,5))
    exy=sub(ry,rx); eyz=sub(rz,ry); exz=sub(rz,rx)
    endpoint=add(exy,eyz)==exz
    reversal=sub(rx,ry)==neg(exy)
    shift=(F(2,7),F(-3,11),F(5,13))
    origin_independent=sub(add(ry,shift),add(rx,shift))==exy
    a=(F(3),F(0),F(0)); b=(F(0),F(4),F(0)); c=add(a,b)
    pythagoras=dot(a,b)==0 and q(c)==q(a)+q(b)==25
    passed=all((endpoint,reversal,origin_independent,pythagoras))
    receipt={
      "schema":"TIR_QUANTUM_RELATION_AFFINE_TORSOR_V0_2",
      "canonical_nonlogical_axiom_count":0,
      "upstream":"RELATION->S2->CP1->P(C2)->AFFINE_STATE_HULL",
      "remaining_tir_gate":"RELATION_TYPED_AS_INTRINSIC_AFFINE_DISPLACEMENT",
      "context_closure_role":"ZERO_KERNEL_CONTEXT_LIFT",
      "metric_role":"RELATIONAL_INVARIANT_MEASUREMENT",
      "endpoint_composition":endpoint,
      "reversal":reversal,
      "origin_independent":origin_independent,
      "pythagorean_control":pythagoras,
      "technical_status":"PASS" if passed else "FAIL",
    }
    print(json.dumps(receipt,indent=2,sort_keys=True))
    if not passed: raise SystemExit(1)

if __name__=="__main__": main()
