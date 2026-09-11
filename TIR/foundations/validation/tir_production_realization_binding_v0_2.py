#!/usr/bin/env python3
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any, Mapping

from tir_global_spatial_complex_source_freeze_v0_1 import freeze_source_capture
from tir_global_spatial_complex_input_contract_v0_1 import validate_input_dataset as validate_spatial_input
from tir_interleaf_matching_field_input_contract_v0_1 import validate_input_dataset as validate_matching_input

SPATIAL_SCHEMA = "TIR_GLOBAL_RELATIONAL_COMPLEX_CAPTURE_V0_2"
MATCHING_SCHEMA = "TIR_INTERLEAF_MATCHING_FIELD_INPUT_V0_2"
BUNDLE_SCHEMA = "TIR_PHYSICAL_REALIZATION_SOURCE_BUNDLE_V0_2"
HEX64 = re.compile(r"^[0-9a-f]{64}$")

class ProductionRealizationBindingError(ValueError):
    pass

def _id(value: Any, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ProductionRealizationBindingError(f"{name} must be a non-empty string")
    out=value.strip()
    if out.startswith("pncs:realization36:"):
        raise ProductionRealizationBindingError(f"{name} must be a source-declared physical realization id, not a PNCS Phase36 realization id")
    return out

def _sha(value: Any, name: str) -> str:
    out=_id(value,name)
    if HEX64.fullmatch(out) is None:
        raise ProductionRealizationBindingError(f"{name} must be 64 lowercase hex")
    return out

@dataclass(frozen=True)
class SpatialRealizationCertificateV02:
    physical_realization_id: str
    physical_realization_receipt_sha256: str
    production_source_admitted: bool
    manifold_certified: bool
    promotion_review_eligible: bool
    capture_sha256: str
    incidence_sha256: str
    canon_allowed: bool=False

@dataclass(frozen=True)
class MatchingRealizationCertificateV02:
    physical_realization_id: str
    physical_realization_receipt_sha256: str
    production_input: bool
    handoff_compatible: bool
    promotion_review_eligible: bool
    payload_sha256: str
    rfe8_shift_packet: dict[str,Any]
    canon_allowed: bool=False

@dataclass(frozen=True)
class PhysicalRealizationBundleCertificateV02:
    same_physical_realization: bool
    same_realization_receipt: bool
    spatial_ready: bool
    matching_ready: bool
    promotion_review_eligible: bool
    canon_allowed: bool
    blockers: tuple[str,...]


def certify_spatial_capture_v02(capture: Mapping[str,Any]) -> SpatialRealizationCertificateV02:
    if not isinstance(capture,Mapping) or capture.get("schema")!=SPATIAL_SCHEMA:
        raise ProductionRealizationBindingError(f"spatial schema must equal {SPATIAL_SCHEMA}")
    rid=_id(capture.get("physical_realization_id"),"physical_realization_id")
    rsha=_sha(capture.get("physical_realization_receipt_sha256"),"physical_realization_receipt_sha256")
    v1={k:v for k,v in capture.items() if k not in {"physical_realization_id","physical_realization_receipt_sha256"}}
    v1["schema"]="TIR_GLOBAL_RELATIONAL_COMPLEX_CAPTURE_V0_1"
    frozen=freeze_source_capture(dict(v1))
    cert=validate_spatial_input(frozen.dataset)
    return SpatialRealizationCertificateV02(rid,rsha,bool(frozen.production_source_admitted),bool(cert.manifold_certified),bool(frozen.production_source_admitted and cert.manifold_certified),frozen.capture_sha256,cert.incidence_sha256,False)


def certify_matching_input_v02(data: Mapping[str,Any]) -> MatchingRealizationCertificateV02:
    if not isinstance(data,Mapping) or data.get("schema")!=MATCHING_SCHEMA:
        raise ProductionRealizationBindingError(f"matching schema must equal {MATCHING_SCHEMA}")
    rid=_id(data.get("physical_realization_id"),"physical_realization_id")
    rsha=_sha(data.get("physical_realization_receipt_sha256"),"physical_realization_receipt_sha256")
    v1={k:v for k,v in data.items() if k not in {"physical_realization_id","physical_realization_receipt_sha256"}}
    v1["schema"]="TIR_INTERLEAF_MATCHING_FIELD_INPUT_V0_1"
    cert=validate_matching_input(v1)
    return MatchingRealizationCertificateV02(rid,rsha,bool(cert.production_input),bool(cert.handoff_compatible),bool(cert.promotion_eligible),cert.payload_sha256,cert.rfe8_shift_packet,False)


def certify_physical_realization_bundle_v02(bundle: Mapping[str,Any]) -> PhysicalRealizationBundleCertificateV02:
    if not isinstance(bundle,Mapping) or bundle.get("schema")!=BUNDLE_SCHEMA:
        raise ProductionRealizationBindingError(f"bundle schema must equal {BUNDLE_SCHEMA}")
    spatial=certify_spatial_capture_v02(bundle.get("spatial_capture"))
    matching=certify_matching_input_v02(bundle.get("matching_input"))
    same_id=spatial.physical_realization_id==matching.physical_realization_id
    same_receipt=spatial.physical_realization_receipt_sha256==matching.physical_realization_receipt_sha256
    blockers=[]
    if not spatial.promotion_review_eligible: blockers.append("TIR_GSC1_PRODUCTION_SPATIAL_CAPTURE")
    if not matching.promotion_review_eligible: blockers.append("TIR_INTERLEAF_PRODUCTION_MATCHING_CAPTURE")
    if not same_id: blockers.append("SAME_PHYSICAL_REALIZATION_ID")
    if not same_receipt: blockers.append("SAME_PHYSICAL_REALIZATION_RECEIPT")
    ready=not blockers
    return PhysicalRealizationBundleCertificateV02(same_id,same_receipt,spatial.promotion_review_eligible,matching.promotion_review_eligible,ready,False,tuple(blockers))
