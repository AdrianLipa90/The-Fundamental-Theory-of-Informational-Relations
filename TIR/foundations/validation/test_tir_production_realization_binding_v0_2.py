from copy import deepcopy

from tir_interleaf_matching_field_input_contract_v0_1 import reference_dataset as matching_reference
from tir_production_realization_binding_v0_2 import (
    BUNDLE_SCHEMA,
    MATCHING_SCHEMA,
    SPATIAL_SCHEMA,
    ProductionRealizationBindingError,
    certify_physical_realization_bundle_v02,
    certify_spatial_capture_v02,
)

H="a"*64

def spatial_reference():
    cells=[]
    vertices=["0","1","2","3","4"]
    for omitted in range(5):
        cells.append({"cell_id":f"tet-{omitted}","vertices":[v for i,v in enumerate(vertices) if i!=omitted]})
    return {"schema":SPATIAL_SCHEMA,"physical_realization_id":"physical:reference-R1","physical_realization_receipt_sha256":H,"capture_id":"reference-boundary-4-simplex","source":{"source_id":"REFERENCE_CONTROL","source_class":"REFERENCE_CONTROL","immutable_ref":"REFERENCE_CONTROL_NOT_PRODUCTION"},"tetrahedral_cells":cells}

def matching_reference_v02():
    data=matching_reference(production=False,c_scale=10.0)
    data["schema"]=MATCHING_SCHEMA
    data["physical_realization_id"]="physical:reference-R1"
    data["physical_realization_receipt_sha256"]=H
    return data

def bundle():
    return {"schema":BUNDLE_SCHEMA,"spatial_capture":spatial_reference(),"matching_input":matching_reference_v02()}

def test_reference_bundle_executes_original_gsc1_a5_and_matching_but_cannot_promote():
    cert=certify_physical_realization_bundle_v02(bundle())
    assert cert.same_physical_realization and cert.same_realization_receipt
    assert not cert.spatial_ready and not cert.matching_ready
    assert not cert.promotion_review_eligible and not cert.canon_allowed
    assert "TIR_GSC1_PRODUCTION_SPATIAL_CAPTURE" in cert.blockers
    assert "TIR_INTERLEAF_PRODUCTION_MATCHING_CAPTURE" in cert.blockers

def test_physical_realization_mismatch_fails_bundle_gate():
    data=bundle(); data["matching_input"]["physical_realization_id"]="physical:reference-R2"
    cert=certify_physical_realization_bundle_v02(data)
    assert not cert.same_physical_realization
    assert "SAME_PHYSICAL_REALIZATION_ID" in cert.blockers

def test_realization_receipt_mismatch_fails_bundle_gate():
    data=bundle(); data["matching_input"]["physical_realization_receipt_sha256"]="b"*64
    cert=certify_physical_realization_bundle_v02(data)
    assert not cert.same_realization_receipt
    assert "SAME_PHYSICAL_REALIZATION_RECEIPT" in cert.blockers

def test_pncs_phase_realization_cannot_be_used_as_physical_realization():
    data=spatial_reference(); data["physical_realization_id"]="pncs:realization36:sha256:"+"c"*64
    try:
        certify_spatial_capture_v02(data)
    except ProductionRealizationBindingError as exc:
        assert "not a PNCS Phase36 realization id" in str(exc)
        return
    raise AssertionError("PNCS realization id must not alias physical realization id")
