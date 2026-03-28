"""Repository object-state extraction to objects_state.csv and couplings.csv."""

from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path
from typing import Iterable

import numpy as np

from src.ciel_foundations.solvers.object_state_energy_solver import (
    amplitudes_from_normalized_energy,
    normalize_energies,
    phase_from_seed_text,
    raw_energy_linear,
)

TEXT_EXTENSIONS = {".md", ".tex", ".py", ".yaml", ".yml", ".json", ".csv", ".txt"}


def discover_repository_files(repo_root: str | Path) -> list[str]:
    root = Path(repo_root)
    files: list[str] = []
    for path in root.rglob("*"):
        if path.is_dir():
            continue
        if ".git" in path.parts or "__pycache__" in path.parts:
            continue
        files.append(str(path.relative_to(root)).replace("\\", "/"))
    return sorted(files)


def _read_text_if_possible(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        try:
            return path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            return None


def _content_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _file_type(rel_path: str) -> str:
    name = Path(rel_path).name
    if name == "README.md":
        return "readme"
    if name in {"INDEX.md", "index.md"}:
        return "index"
    if name == "AGENT.md":
        return "agent"
    if name == "GLOSSARY.md":
        return "glossary"
    if rel_path.startswith("definitions/"):
        return "definition"
    if rel_path.startswith("derivations/"):
        return "derivation"
    if rel_path.startswith("interfaces/"):
        return "interface"
    if rel_path.startswith("tests/"):
        return "test"
    if rel_path.startswith("Simulations/code/"):
        return "simulation_code"
    if rel_path.startswith("Simulations/results/"):
        return "simulation_result"
    if rel_path.startswith("provenance/"):
        return "provenance"
    if rel_path.startswith("falsification/"):
        return "falsification"
    if rel_path.startswith("whitepapers/"):
        return "whitepaper"
    if rel_path.startswith("LaTeX/sections/"):
        return "latex_section"
    if rel_path.startswith("LaTeX/appendices/"):
        return "latex_appendix"
    if rel_path.startswith("registries/"):
        return "registry"
    if rel_path.startswith("schemas/"):
        return "schema"
    if rel_path.startswith("systems/"):
        return "orchestrator"
    if rel_path.startswith("bibliography/"):
        return "bibliography"
    if rel_path.startswith("src/"):
        return "solver" if "solver" in name else "source"
    return "support"


def _layer(rel_path: str) -> str:
    parts = Path(rel_path).parts
    return parts[0] if parts else "root"


def _pressure(file_type: str) -> float:
    return {
        "index": 1.0,
        "orchestrator": 1.0,
        "readme": 0.9,
        "agent": 0.9,
        "registry": 0.9,
        "interface": 0.9,
        "schema": 0.9,
        "glossary": 0.85,
        "definition": 0.75,
        "derivation": 0.75,
        "solver": 0.6,
        "source": 0.55,
        "whitepaper": 0.55,
        "latex_section": 0.5,
        "latex_appendix": 0.45,
        "simulation_code": 0.4,
        "test": 0.35,
        "simulation_result": 0.2,
        "provenance": 0.2,
        "falsification": 0.25,
        "bibliography": 0.3,
        "support": 0.3,
    }.get(file_type, 0.3)


def _weight(file_type: str) -> float:
    return {
        "definition": 1.0,
        "derivation": 0.95,
        "interface": 0.9,
        "registry": 0.9,
        "schema": 0.9,
        "solver": 0.85,
        "source": 0.8,
        "readme": 0.8,
        "index": 0.8,
        "agent": 0.8,
        "orchestrator": 0.85,
        "glossary": 0.75,
        "whitepaper": 0.7,
        "latex_section": 0.7,
        "latex_appendix": 0.65,
        "simulation_code": 0.6,
        "test": 0.5,
        "simulation_result": 0.4,
        "provenance": 0.35,
        "falsification": 0.35,
        "bibliography": 0.3,
        "support": 0.3,
    }.get(file_type, 0.3)


def _character(rel_path: str, file_type: str) -> str:
    if file_type in {"readme", "index", "agent", "glossary", "definition", "derivation", "registry", "schema"}:
        return "canonical"
    if file_type == "orchestrator":
        return "bridge"
    if rel_path.startswith("Simulations/"):
        return "report"
    if rel_path.startswith("tests/"):
        return "test"
    if rel_path.startswith("LaTeX/") or rel_path.startswith("whitepapers/") or rel_path.startswith("bibliography/"):
        return "support"
    return "support"


def _chi_value(character: str) -> float:
    return {
        "canonical": 1.0,
        "bridge": 0.8,
        "orbital": 0.7,
        "support": 0.5,
        "report": 0.3,
        "test": 0.2,
        "archive": 0.1,
        "transitional": 0.4,
    }.get(character, 0.4)


def _local_mass(text: str | None, rel_path: str) -> float:
    if text is None:
        return 0.0
    if rel_path.endswith(".py"):
        count = 0
        for line in text.splitlines():
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            count += 1
        return float(count)
    return float(len(re.findall(r"[A-Za-z0-9_]+", text)))


def build_repository_couplings(repo_root: str | Path, rel_paths: Iterable[str] | None = None) -> list[dict[str, object]]:
    root = Path(repo_root)
    files = list(rel_paths) if rel_paths is not None else discover_repository_files(root)
    texts = {rel: _read_text_if_possible(root / rel) for rel in files}
    couplings: list[dict[str, object]] = []
    for source in files:
        text = texts[source]
        if not text:
            continue
        for target in files:
            if source == target:
                continue
            count = text.count(target)
            if count > 0:
                couplings.append(
                    {
                        "source": source,
                        "target": target,
                        "relation_type": "registry_reference" if source.startswith("registries/") else "path_mention",
                        "coupling_weight": float(count),
                        "phase_offset": 0.0,
                        "metadata": "exact_path_count",
                    }
                )
    return couplings


def extract_repository_object_states(repo_root: str | Path) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    root = Path(repo_root)
    files = discover_repository_files(root)
    couplings = build_repository_couplings(root, files)

    crossref_in = {rel: 0.0 for rel in files}
    crossref_out = {rel: 0.0 for rel in files}
    for row in couplings:
        source = str(row["source"])
        target = str(row["target"])
        w = float(row["coupling_weight"])
        crossref_out[source] += w
        crossref_in[target] += w

    rows: list[dict[str, object]] = []
    raw_energies: list[float] = []
    for rel in files:
        path = root / rel
        text = _read_text_if_possible(path)
        file_type = _file_type(rel)
        local_mass = _local_mass(text, rel)
        c_in = crossref_in[rel]
        c_out = crossref_out[rel]
        pressure = _pressure(file_type)
        weight = _weight(file_type)
        frequency = 0.0
        character = _character(rel, file_type)
        chi_value = _chi_value(character)
        density = local_mass + c_in + c_out
        neighborhood_norm = c_in + c_out
        state_vector = [local_mass, c_in, c_out, pressure, weight, frequency]
        state_norm = float(np.linalg.norm(np.array(state_vector, dtype=float)))
        raw_energy = raw_energy_linear(density, pressure, weight, frequency, state_norm, chi_value, neighborhood_norm)
        rows.append(
            {
                "id": rel,
                "path": rel,
                "type": file_type,
                "layer": _layer(rel),
                "content_hash": _content_hash(path),
                "size_bytes": path.stat().st_size,
                "local_mass": float(local_mass),
                "crossref_in": float(c_in),
                "crossref_out": float(c_out),
                "pressure": float(pressure),
                "density": float(density),
                "weight": float(weight),
                "frequency": float(frequency),
                "state_vector": json.dumps(state_vector),
                "character": character,
                "_state_norm": float(state_norm),
                "_chi_value": float(chi_value),
                "_neighborhood_norm": float(neighborhood_norm),
                "raw_energy": float(raw_energy),
            }
        )
        raw_energies.append(float(raw_energy))

    norm = normalize_energies(raw_energies)
    amps = amplitudes_from_normalized_energy(norm)
    for row, norm_energy, amp in zip(rows, norm, amps):
        seed_text = "|".join(
            [
                str(row["path"]),
                str(row["content_hash"]),
                f"{row['density']:.12f}",
                f"{row['pressure']:.12f}",
                f"{row['weight']:.12f}",
                f"{row['frequency']:.12f}",
                str(row["state_vector"]),
                str(row["character"]),
                f"{row['_neighborhood_norm']:.12f}",
            ]
        )
        seed = hashlib.sha256(seed_text.encode("utf-8")).hexdigest()
        phi = phase_from_seed_text(seed_text)
        state_re = float(amp * np.cos(phi))
        state_im = float(amp * np.sin(phi))
        row["norm_energy"] = float(norm_energy)
        row["amplitude"] = float(amp)
        row["phase"] = float(phi)
        row["state_signature"] = f"({state_re:.12f},{state_im:.12f})"
        row["seed"] = seed
        del row["_state_norm"]
        del row["_chi_value"]
        del row["_neighborhood_norm"]

    return rows, couplings


def write_repository_state_exports(repo_root: str | Path, objects_csv_path: str | Path, couplings_csv_path: str | Path) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    rows, couplings = extract_repository_object_states(repo_root)
    objects_csv = Path(objects_csv_path)
    couplings_csv = Path(couplings_csv_path)
    objects_csv.parent.mkdir(parents=True, exist_ok=True)
    couplings_csv.parent.mkdir(parents=True, exist_ok=True)

    object_fields = [
        "id",
        "path",
        "type",
        "layer",
        "content_hash",
        "size_bytes",
        "local_mass",
        "crossref_in",
        "crossref_out",
        "pressure",
        "density",
        "weight",
        "frequency",
        "state_vector",
        "character",
        "raw_energy",
        "norm_energy",
        "amplitude",
        "phase",
        "state_signature",
        "seed",
    ]
    with open(objects_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=object_fields)
        writer.writeheader()
        writer.writerows(rows)

    coupling_fields = ["source", "target", "relation_type", "coupling_weight", "phase_offset", "metadata"]
    with open(couplings_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=coupling_fields)
        writer.writeheader()
        writer.writerows(couplings)

    return rows, couplings
