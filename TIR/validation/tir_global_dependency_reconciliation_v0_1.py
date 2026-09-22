#!/usr/bin/env python3
from __future__ import annotations
import json
from collections import defaultdict, deque
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
EXPORT=ROOT/"DEPENDENCY_EXPORT.json"
CURRENT=ROOT/"TIR/CURRENT_STATUS.md"
EXPECTED={
"TIR.HALF_SEAM.PHASE_FIBER","TIR.HOLONOMY.SEMANTIC_U1",
"TIR.INFORMATION_AREA_CURVATURE.PHASE_CLOCK","TIR.PLATONIC.RAMANUJAN_SPECTRAL_CARRIER",
"TIR.PLATONIC.MCKAY_E8_600CELL","TIR.COEFFICIENT.ROLE_ORIENTATION",
"TIR.COEFFICIENT.SELECTOR_COMPOSITION_NOGO","TIR.SM.COEFFICIENT_TRANSITION_SELECTOR",
"TIR.CKM.JARLSKOG_CLOSURE","TIR.HYPERCHARGE.RELATIVE_UNIQUENESS",
"TIR.NEUTRINO.ABSOLUTE_ACTION_REPAIR","TIR.SM.CONTINUUM_GAUGE_NORMALIZATION",
"TIR.SM.ELECTROWEAK_SCHEME_SCALE","TIR.SM.HIGGS_SCALAR_ACTION_BINDING",
"TIR.SM.QUARK_MASS_MAP","TIR.SM.MESON_ABSOLUTE_ACTION_BASELINE",
"TIR.SM.STRONG_CP_HOLONOMIC_SOURCE","TIR.SM.COSMOLOGY_SCALE_RHOCRIT",
"TIR.CP1.DYADIC_FRACTAL_GATE","TIR.SPACE.HEXAHEDRAL_BLOCH_DUAL_FRAME",
"TIR.SPACE.TETRA_FS_CROSSWALK","TIR.QUANTUM.QUBIT_TETRAHEDRAL_IC",
"TIR.SPACE.DIMENSION_GATE","TIR.WHITE_THREAD.SPIN_LIFT","TIR.WHITE_THREAD.LYAPUNOV",
"TIR.SPACETIME.SP3_3PLUS1_BUNDLE_COMPATIBILITY_V01","TIR.SPACETIME.SP3_DELTA_HERM2_HALF_LIFT_V01",
"TIR.SPACETIME.CAUSAL_3PLUS1_PAIR_CLOSURE_V01","TIR.SPACETIME.SP3_CAUSAL_PAIR_INSTANTIATION_V01",
"TIR.SPACETIME.HERM2_LORENTZ_COVARIANCE_V01","TIR.SPACETIME.HERM2_RAPIDITY_SPEED_COMPOSITION_V01",
"TIR.SPACETIME.POSITIVE_ELAPSED_STATE_CONE_V01",
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
def main():
    dep=json.loads(EXPORT.read_text()); current=CURRENT.read_text()
    ids=[c["claim_id"] for c in dep["claims"]]; s=set(ids); edges=dep["local_edges"]
    checks={
      "schema":dep.get("schema")=="FPDG_DEPENDENCY_EXPORT_V0_1",
      "source_commit":dep.get("source_commit")=="8c781742b656871529a4783ce977c8c1b8d51de2",
      "unique":len(ids)==len(s),
      "expected":EXPECTED<=s,
      "endpoints":all(e["from"] in s and e["to"] in s for e in edges),
      "candidate_typed":all(e.get("promotion_required") is True and e.get("promotion_gate") for e in edges if e["authority"]=="CANDIDATE_ONLY"),
      "dag":dag(s,edges),
      "hypercharge_closed":"hypercharge relative uniqueness              CLOSED" in current,
      "neutrino_repair_closed":"neutrino absolute-action source repair       CLOSED" in current,
      "white_thread_exported":"TIR.WHITE_THREAD.SPIN_LIFT" in s and "TIR.WHITE_THREAD.LYAPUNOV" in s,
      "legacy_fail_scoped":"These receipts are not verdicts on later replacement constructions" in current,
    }
    status="PASS" if all(checks.values()) else "FAIL"
    print(json.dumps({"schema":"TIR_GLOBAL_DEPENDENCY_RECONCILIATION_V0_2","status":status,"claims":len(ids),"edges":len(edges),"checks":checks},indent=2,sort_keys=True))
    raise SystemExit(0 if status=="PASS" else 1)
if __name__=="__main__":main()
