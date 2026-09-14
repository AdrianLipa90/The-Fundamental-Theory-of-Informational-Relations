import json
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parents[1]
MANIFEST = MODULE_ROOT / "REPOSITORY_HOLONOMY_V1.json"


def test_repository_holonomy_contract_is_fail_closed() -> None:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))

    assert data["schema"] == "tir.soh-repository-holonomy/v1"
    assert data["status"] == "ACTIVE_BACKLINK_CONTRACT"
    assert data["relationship"] == "CROSS_REPOSITORY_HOLONOMY_BACKLINK"
    assert data["local_repository"] == (
        "AdrianLipa90/The-Fundamental-Theory-of-Informational-Relations"
    )
    assert data["local_branch"] == "main"
    assert data["local_path"] == "TIR/zeta_information_axis"
    assert data["dedicated_repository"] == "AdrianLipa90/secret-of-a-half"
    assert data["dedicated_branch"] == "main"
    assert data["embedded_source_preserved"] is True
    assert data["recursive_submodule"] is False
    assert data["physical_gitlink_direction"] == "secret-of-a-half -> TIR"
    assert data["scientific_claim_impact"] == "NONE"
    assert data["riemann_hypothesis_status"] == "OPEN"

    assert (MODULE_ROOT / "README.md").is_file()
    assert (MODULE_ROOT / "src").is_dir()
    assert len(data["invariants"]) >= 4
