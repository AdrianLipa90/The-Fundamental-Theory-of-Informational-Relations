#!/usr/bin/env python3
from __future__ import annotations
import json, re, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
MASTER=ROOT/"TIR/monograph/tir_monograph_v12.tex"
GRAPH=ROOT/"DEPENDENCY_EXPORT.json"

def fail(msg:str)->None:
    raise SystemExit("FAIL: "+msg)

def tex_closure(master:Path):
    base=master.parent
    seen={}
    queue=[master]
    inc=re.compile(r"\\(?:input|include)\{([^}]+)\}")
    while queue:
        p=queue.pop(0).resolve()
        if p in seen: continue
        if not p.is_file(): fail(f"missing TeX source: {p}")
        s=p.read_text(encoding="utf-8")
        seen[p]=s
        for rel in inc.findall(s):
            q=(base/(rel if Path(rel).suffix else rel+".tex")).resolve()
            if q not in seen: queue.append(q)
    return seen

files=tex_closure(MASTER)
full="\n".join(files.values())
labels=re.findall(r"\\label\{([^}]+)\}",full)
refs=re.findall(r"\\(?:ref|eqref|pageref|autoref|cref|Cref|nameref)\{([^}]+)\}",full)
refs+=re.findall(r"\\hyperref\[([^]]+)\]",full)
cites=[k.strip() for m in re.findall(r"\\cite[a-zA-Z*]*\{([^}]+)\}",full) for k in m.split(",") if k.strip()]
bib=re.findall(r"\\bibitem(?:\[[^]]*\])?\{([^}]+)\}",full)
for name,seq in (("label",labels),("bibitem",bib)):
    d={x for x in seq if seq.count(x)>1}
    if d: fail(f"duplicate {name}s: {sorted(d)}")
missing_refs=sorted(set(refs)-set(labels))
missing_cites=sorted(set(cites)-set(bib))
if missing_refs: fail(f"missing refs: {missing_refs}")
if missing_cites: fail(f"missing cites: {missing_cites}")
if "Version 12.4 Relational Zero and Graph Reconciliation" not in MASTER.read_text(encoding="utf-8"):
    fail("master is not v12.4")
required_tex=[
    r"\mathfrak Z_{\rm rel}=(\varnothing,\varnothing)",
    "minimal nontrivial distinction",
    r"\Pi_1=\{N,S\}",
    "binarity is not inferred from an order-two involution",
]
for token in required_tex:
    if token not in full: fail(f"missing foundational TeX token: {token}")

g=json.loads(GRAPH.read_text(encoding="utf-8"))
claims=g.get("claims",[])
ids=[c["claim_id"] for c in claims]
if len(ids)!=len(set(ids)): fail("duplicate graph claim_id")
idset=set(ids)
edges=g.get("local_edges",[])
orph=[e for e in edges if e.get("from") not in idset or e.get("to") not in idset]
if orph: fail(f"orphan graph edges: {orph}")
by={c["claim_id"]:c for c in claims}
for cid in ["TIR.PRIMITIVE.ZERO","TIR.PRIMITIVE.POINT","TIR.PRIMITIVE.FIRST_DISTINCTION","TIR.PRIMITIVE.POLES_NS","TIR.KAPPA.NORMALIZATION","TIR.FLAVOUR.THREE_STATE_CARRIER"]:
    if cid not in by: fail(f"missing graph claim: {cid}")
if "EMPTY_SUPPORT_AND_RELATION" not in by["TIR.PRIMITIVE.ZERO"].get("status",""):
    fail("relational zero typing missing")
parents={e["from"] for e in edges if e.get("to")=="TIR.KAPPA.NORMALIZATION" and e.get("authority")=="CANONICAL"}
expected={"TIR.FOUNDATION.HALF","TIR.FOUNDATION.LN2","TIR.FLAVOUR.THREE_STATE_CARRIER"}
if parents!=expected: fail(f"kappa parents drift: {sorted(parents)} != {sorted(expected)}")
print(json.dumps({
 "schema":"TIR_MANUSCRIPT_RELEASE_GATE_V0_1",
 "status":"PASS",
 "tex_files":len(files),
 "labels":len(set(labels)),
 "refs":len(refs),
 "citations":len(cites),
 "bibitems":len(set(bib)),
 "graph_claims":len(ids),
 "graph_edges":len(edges),
 "kappa_parents":sorted(parents),
},indent=2,sort_keys=True))
