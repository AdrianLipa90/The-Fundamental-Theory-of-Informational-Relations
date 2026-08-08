from __future__ import annotations
from dataclasses import dataclass, asdict
from .l_constants import L3, L4, L5
from .action_generator import COEFFICIENT_STATES

@dataclass(frozen=True)
class CoefficientLineage:
    gate: str
    slot: str
    value: int
    magnitude_parent: str
    magnitude_status: str
    sign_parent: str
    sign_status: str
    role_parent: str
    role_status: str
    provenance: tuple[str, ...]

LINEAGE = (
    CoefficientLineage("ELECTRON_ACTION","half_base",1,"HALF","EXACT","IDENTITY","EXACT_OPERATOR","spin-half base","PROJECT_IDENTIFICATION",("Metatime Ch.5.1","SOH/TIR half-axis")),
    CoefficientLineage("ELECTRON_ACTION","linear",-3,"GENERATION_COUNT_3","OBSERVATION_OR_PROJECT_PRIMITIVE","NEGATION","EXACT_OPERATOR","generation deficit lowers action","PROJECT_MODEL_ASSIGNMENT",("Metatime Ch.5.2","TIR v6.7")),
    CoefficientLineage("ELECTRON_ACTION","return_axis",+1,"IDENTITY","EXACT_INTEGER","POSITIVE_ORIENTATION","EXACT_OPERATOR_CLASS","Collatz return correction","PROJECT_MODEL_ASSIGNMENT",("Metatime Ch.5.3","TIR v6.7")),
    CoefficientLineage("ELECTRON_ACTION","curvature",-1,"IDENTITY","EXACT_INTEGER","NEGATION","EXACT_OPERATOR","leading Poincare curvature correction","PROJECT_MODEL_ASSIGNMENT",("Metatime Ch.5.4","TIR v6.7")),
    CoefficientLineage("E_TO_MU_RELEASE","linear",+L5,"L5","PROJECT_DEFINED_EXACT_ARITHMETIC","POSITIVE_ORIENTATION","EXACT_OPERATOR_CLASS","five-fold generation bridge / intention-space count","PROJECT_MODEL_ASSIGNMENT",("Metatime Ch.6.1.1","TIR v7.0")),
    CoefficientLineage("E_TO_MU_RELEASE","return_axis",+L4,"L4","PROJECT_DEFINED_EXACT_ARITHMETIC","POSITIVE_ORIENTATION","EXACT_OPERATOR_CLASS","Collatz channel correction","PROJECT_MODEL_ASSIGNMENT",("Metatime Ch.6.1.1","TIR v7.0")),
    CoefficientLineage("E_TO_MU_RELEASE","curvature",+(L3+1),"L3_PLUS_IDENTITY","EXACT_ARITHMETIC","POSITIVE_ORIENTATION","EXACT_OPERATOR_CLASS","positive second-order curvature count","PROJECT_MODEL_ASSIGNMENT",("Metatime Ch.6.1.1","TIR v7.0")),
    CoefficientLineage("MU_TO_TAU_RELEASE","linear",+3,"GENERATION_COUNT_3","OBSERVATION_OR_PROJECT_PRIMITIVE","POSITIVE_ORIENTATION","EXACT_OPERATOR_CLASS","three-generation release step","PROJECT_MODEL_ASSIGNMENT",("Metatime Ch.6.2.1","TIR v6.8")),
    CoefficientLineage("MU_TO_TAU_RELEASE","return_axis",-1,"IDENTITY","EXACT_INTEGER","NEGATION","EXACT_OPERATOR","negative Collatz correction near asymptotic scale","PROJECT_MODEL_ASSIGNMENT",("Metatime Ch.6.2.1","TIR v6.8")),
    CoefficientLineage("MU_TO_TAU_RELEASE","curvature",-L3,"L3","PROJECT_DEFINED_EXACT_ARITHMETIC","NEGATION","EXACT_OPERATOR","negative L3-weighted curvature correction","PROJECT_MODEL_ASSIGNMENT",("Metatime Ch.6.2.1","TIR v6.8")),
)

def audit_coefficients() -> dict[str, object]:
    rows=[asdict(x) for x in LINEAGE]
    no_magnitude_parent=[x for x in rows if not x["magnitude_parent"]]
    open_assignment=[x for x in rows if str(x["role_status"]).startswith("PROJECT_")]
    return {"schema":"TIR_HALF_COEFFICIENT_PARENT_AUDIT_V1","status":"PASS_WITH_OPEN_ASSIGNMENT_RULE","coefficient_count":len(rows),"magnitude_unparented_count":len(no_magnitude_parent),"magnitude_unparented":no_magnitude_parent,"assignment_open_count":len(open_assignment),"assignment_open":open_assignment,"conclusion":"Coefficient magnitudes are parented. The remaining non-canonical freedom is the rule assigning orientation/sign and semantic role to each generation transition."}
