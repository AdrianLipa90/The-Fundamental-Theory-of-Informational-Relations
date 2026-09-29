#!/usr/bin/env python3
from __future__ import annotations
import json
from collections import defaultdict, deque
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
EXPORT=ROOT/"DEPENDENCY_EXPORT.json"
CURRENT=ROOT/"TIR/CURRENT_STATUS.md"

EXPECTED={
"TIR.PRIMITIVE.NOTHING_NONREALIZABLE",
"TIR.PRIMITIVE.POINT",
"TIR.PRIMITIVE.RELATION",
"TIR.PRIMITIVE.FIRST_DISTINCTION",
"TIR.PRIMITIVE.POLES_NS",
"TIR.FOUNDATION.HALF",
"TIR.FOUNDATION.LN2",
"TIR.FOUNDATION.PHASE_LAGRANGIAN",
"TIR.FOUNDATION.PHASE_S1",
"TIR.FOUNDATION.LAGRANGIAN_BLOCH_SELECTION",
"TIR.FOUNDATION.SPHERE_S2",
"TIR.FOUNDATION.C2",
"TIR.FOUNDATION.CP1",
"TIR.FOUNDATION.BERRY_FS",
"TIR.FOUNDATION.SPIN_HALF",
"TIR.HALF_SEAM.PHASE_FIBER",
"TIR.HOLONOMY.SEMANTIC_U1",
"TIR.INFORMATION_AREA_CURVATURE.PHASE_CLOCK",
"TIR.PLATONIC.RAMANUJAN_SPECTRAL_CARRIER",
"TIR.PLATONIC.MCKAY_E8_600CELL",
"TIR.COEFFICIENT.ROLE_ORIENTATION",
"TIR.COEFFICIENT.SELECTOR_COMPOSITION_NOGO",
"TIR.SM.COEFFICIENT_TRANSITION_SELECTOR",
"TIR.CKM.JARLSKOG_CLOSURE",
"TIR.HYPERCHARGE.RELATIVE_UNIQUENESS",
"TIR.NEUTRINO.ABSOLUTE_ACTION_REPAIR",
"TIR.SM.CONTINUUM_GAUGE_NORMALIZATION",
"TIR.SM.ELECTROWEAK_SCHEME_SCALE",
"TIR.SM.HIGGS_SCALAR_ACTION_BINDING",
"TIR.SM.QUARK_MASS_MAP",
"TIR.SM.MESON_ABSOLUTE_ACTION_BASELINE",
"TIR.SM.STRONG_CP_HOLONOMIC_SOURCE",
"TIR.SM.COSMOLOGY_SCALE_RHOCRIT",
"TIR.CP1.DYADIC_FRACTAL_GATE",
"TIR.SPACE.HEXAHEDRAL_BLOCH_DUAL_FRAME",
"TIR.SPACE.TETRA_FS_CROSSWALK",
"TIR.QUANTUM.QUBIT_TETRAHEDRAL_IC",
"TIR.SPACE.DIMENSION_GATE",
"TIR.WHITE_THREAD.SPIN_LIFT",
"TIR.WHITE_THREAD.LYAPUNOV",
"TIR.SPACETIME.SP3_3PLUS1_BUNDLE_COMPATIBILITY_V01",
"TIR.SPACETIME.SP3_DELTA_HERM2_HALF_LIFT_V01",
"TIR.SPACETIME.CAUSAL_3PLUS1_PAIR_CLOSURE_V01",
"TIR.SPACETIME.SP3_CAUSAL_PAIR_INSTANTIATION_V01",
"TIR.SPACETIME.HERM2_LORENTZ_COVARIANCE_V01",
"TIR.SPACETIME.HERM2_RAPIDITY_SPEED_COMPOSITION_V01",
"TIR.SPACETIME.POSITIVE_ELAPSED_STATE_CONE_V01",
}

REQUIRED_EDGES={
("TIR.PRIMITIVE.NOTHING_NONREALIZABLE","TIR.PRIMITIVE.POINT"),
("TIR.PRIMITIVE.POINT","TIR.PRIMITIVE.RELATION"),
("TIR.PRIMITIVE.RELATION","TIR.PRIMITIVE.FIRST_DISTINCTION"),
("TIR.PRIMITIVE.FIRST_DISTINCTION","TIR.PRIMITIVE.POLES_NS"),
("TIR.PRIMITIVE.POLES_NS","TIR.FOUNDATION.HALF"),
("TIR.PRIMITIVE.RELATION","TIR.FOUNDATION.PHASE_LAGRANGIAN"),
("TIR.FOUNDATION.PHASE_LAGRANGIAN","TIR.FOUNDATION.PHASE_S1"),
("TIR.FOUNDATION.PHASE_S1","TIR.FOUNDATION.LAGRANGIAN_BLOCH_SELECTION"),
("TIR.PRIMITIVE.FIRST_DISTINCTION","TIR.FOUNDATION.LAGRANGIAN_BLOCH_SELECTION"),
("TIR.PRIMITIVE.POLES_NS","TIR.FOUNDATION.LAGRANGIAN_BLOCH_SELECTION"),
("TIR.FOUNDATION.LAGRANGIAN_BLOCH_SELECTION","TIR.FOUNDATION.SPHERE_S2"),
("TIR.FOUNDATION.C2","TIR.FOUNDATION.CP1"),
("TIR.FOUNDATION.LAGRANGIAN_BLOCH_SELECTION","TIR.FOUNDATION.C2"),
("TIR.FOUNDATION.SPHERE_S2","TIR.FOUNDATION.CP1"),
("TIR.FOUNDATION.CP1","TIR.FOUNDATION.BERRY_FS"),
("TIR.FOUNDATION.BERRY_FS","TIR.FOUNDATION.SPIN_HALF"),
("TIR.FLAVOUR.STAGE66_SU3F_GENERATION","TIR.KAPPA.NORMALIZATION"),
}

def dag(nodes,edges):
    indeg={n:0 for n in nodes}; adj=defaultdict(list)
    for e in edges:
        if e["authority"]=="CANDIDATE_ONLY": continue
        adj[e["from"]].append(e["to"]); indeg[e["to"]]+=1
    q=deque(n for n,d in indeg.items() if d==0); seen=0
    while q:
        n=q.popleft(); seen+=1
        for m in adj[n]:
            indeg[m]-=1
            if indeg[m]==0:q.append(m)
    return seen==len(nodes)

def ancestors(target,nodes,edges):
    rev=defaultdict(set)
    for e in edges:
        if e["authority"]=="CANDIDATE_ONLY": continue
        rev[e["to"]].add(e["from"])
    seen=set(); todo=list(rev[target])
    while todo:
        x=todo.pop()
        if x in seen: continue
        seen.add(x)
        todo.extend(rev[x]-seen)
    return seen

def main():
    dep=json.loads(EXPORT.read_text()); current=CURRENT.read_text()
    ids=[c["claim_id"] for c in dep["claims"]]; s=set(ids); edges=dep["local_edges"]
    edge_pairs={(e["from"],e["to"]) for e in edges if e["authority"]!="CANDIDATE_ONLY"}

    spin_anc=ancestors("TIR.FOUNDATION.SPIN_HALF",s,edges)
    sphere_anc=ancestors("TIR.FOUNDATION.SPHERE_S2",s,edges)
    kappa_anc=ancestors("TIR.KAPPA.NORMALIZATION",s,edges)

    checks={
      "schema":dep.get("schema")=="FPDG_DEPENDENCY_EXPORT_V0_1",
      "source_ref":dep.get("source_ref")=="feat/zero-axiom-relational-foundation-20260928",
      "source_commit_present":isinstance(dep.get("source_commit"),str) and len(dep["source_commit"])==40,
      "zero_nonlogical_axioms":dep.get("canonical_nonlogical_axiom_count")==0,
      "foundation_owner":dep.get("foundation_owner")=="TIR/foundations/TIR_CANONICAL_DERIVATION_SPINE_V0_1.md",
      "unique":len(ids)==len(s),
      "expected":EXPECTED<=s,
      "endpoints":all(e["from"] in s and e["to"] in s for e in edges),
      "candidate_typed":all(e.get("promotion_required") is True and e.get("promotion_gate") for e in edges if e["authority"]=="CANDIDATE_ONLY"),
      "required_edges":REQUIRED_EDGES<=edge_pairs,
      "dag":dag(s,edges),
      "no_so3_parent_of_sphere":not any("SO3" in x or "SO(3)" in x for x in sphere_anc),
      "berry_upstream_of_spin":"TIR.FOUNDATION.BERRY_FS" in spin_anc,
      "sphere_upstream_of_spin":"TIR.FOUNDATION.SPHERE_S2" in spin_anc,
      "su3f_upstream_of_kappa":"TIR.FLAVOUR.STAGE66_SU3F_GENERATION" in kappa_anc,
      "hypercharge_closed":"hypercharge relative uniqueness            CLOSED" in current,
      "neutrino_repair_closed":"neutrino absolute-action source repair       CLOSED" in current,
      "foundation_reconciled":"Foundation source reconciliation — 2026-09-28" in current,
    }
    status="PASS" if all(checks.values()) else "FAIL"
    print(json.dumps({
      "schema":"TIR_GLOBAL_DEPENDENCY_RECONCILIATION_V0_3",
      "status":status,
      "claims":len(ids),
      "edges":len(edges),
      "checks":checks
    },indent=2,sort_keys=True))
    raise SystemExit(0 if status=="PASS" else 1)

if __name__=="__main__":
    main()
