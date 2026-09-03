from __future__ import annotations

import hashlib, json
from dataclasses import asdict
from typing import Any

from tir_production_realization_binding_v0_2 import PhysicalRealizationBundleCertificateV02

RECEIPT_SCHEMA="TIR_PHYSICAL_REALIZATION_SOURCE_BUNDLE_CERTIFICATE_V0_2"

def _sha(obj: Any) -> str:
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def physical_realization_bundle_receipt(cert: PhysicalRealizationBundleCertificateV02) -> dict[str,Any]:
    if not isinstance(cert,PhysicalRealizationBundleCertificateV02):
        raise TypeError("PhysicalRealizationBundleCertificateV02 required")
    payload={"schema":RECEIPT_SCHEMA,"authority":"SOURCE_CONTRACT","physical_production_claim":False,**asdict(cert)}
    payload["receipt_sha256"]=_sha(payload)
    return payload
