from __future__ import annotations

import hashlib, json
from dataclasses import asdict
from typing import Any, Mapping

from tir_production_realization_binding_v0_2 import (
    BUNDLE_SCHEMA,
    ProductionRealizationBindingError,
    certify_physical_realization_bundle_v02,
)

RECEIPT_SCHEMA="TIR_PHYSICAL_REALIZATION_EVIDENCE_RECEIPT_V0_2"

def _sha(obj: Any) -> str:
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def certify_physical_realization_evidence_v02(bundle: Mapping[str,Any]) -> dict[str,Any]:
    if not isinstance(bundle,Mapping) or bundle.get("schema")!=BUNDLE_SCHEMA:
        raise ProductionRealizationBindingError(f"bundle schema must equal {BUNDLE_SCHEMA}")
    cert=certify_physical_realization_bundle_v02(bundle)
    spatial=bundle["spatial_capture"]; matching=bundle["matching_input"]
    sid=spatial.get("physical_realization_id"); mid=matching.get("physical_realization_id")
    sr=spatial.get("physical_realization_receipt_sha256"); mr=matching.get("physical_realization_receipt_sha256")
    if cert.same_physical_realization and sid!=mid:
        raise ProductionRealizationBindingError("internal same-realization inconsistency")
    if cert.same_realization_receipt and sr!=mr:
        raise ProductionRealizationBindingError("internal realization-receipt inconsistency")
    payload={"schema":RECEIPT_SCHEMA,"authority":"SOURCE_CONTRACT","physical_production_claim":False,"physical_realization_id":sid if cert.same_physical_realization else None,"physical_realization_receipt_sha256":sr if cert.same_realization_receipt else None,**asdict(cert)}
    payload["receipt_sha256"]=_sha(payload)
    return payload
