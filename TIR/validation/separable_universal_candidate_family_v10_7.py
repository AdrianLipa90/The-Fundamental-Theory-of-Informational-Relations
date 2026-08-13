#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TIR v10.7 — separable universal candidate-family freeze.

Purpose
-------
Freeze exactly three mass-free candidate maps before inspecting any future
Higgs-coupling likelihood.  The architecture is deliberately separable:

    log y(f,g) = F(S_f) + D(G_g, R_g)

S_f is generation-invariant sector action, G_g is the shared generation action,
and R_g is the mandatory Ramanujan release.  The same F and D are applied to all
charged-fermion sectors.  No observed mass, CKM/PMNS value, or future likelihood
enters candidate construction.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

ROOT = Path(__file__).resolve().parents[2]
RESULTS = Path(__file__).resolve().parent / "results"
RESULTS.mkdir(parents=True, exist_ok=True)

KAPPA = math.log(2.0) / (24.0 * math.pi)
L3 = 7
ALPHA_COLLATZ = 0.75

ACTION_SOURCE = ROOT / (
    "archive/v7.9/full/10_standard_model_derivation_stages/"
    "11_metatime_sm_full_action_seed_arbitration_v1_0/results/"
    "charged_fermion_action_assembly_v1_0.csv"
)
REPRESENTATION_SOURCE = ROOT / (
    "archive/v7.9/full/10_standard_model_derivation_stages/"
    "11_metatime_sm_full_action_seed_arbitration_v1_0/results/"
    "representation_features_corrected_v1_0.csv"
)

SOURCE_GIT_BLOBS = {
    "charged_fermion_action_assembly_v1_0.csv": "afd4260e99880c6a4f01134c3dc8102404f1f245",
    "representation_features_corrected_v1_0.csv": "536dd830666e8100c00b046b625ce0028e424558",
    "ramanujan_seed_suppression_v2_1.py": "c8f708e2d9a81573b9c746ce5ecd717465b73a1d",
}

FORBIDDEN_OPERATOR_INPUTS = {
    "target_mass",
    "pdg_mass",
    "observed_mass",
    "CKM_observed",
    "PMNS_observed",
    "future_likelihood_value",
}

CANDIDATE_IDS = (
    "C1_LINEAR_SEPARABLE_ACTION",
    "C2_QUARTER_POWER_SEPARABLE_ACTION",
    "C3_INVERSE_QUARTER_INFORMATION_POTENTIAL",
)


def sha256_file(path: Path) -> str:
    """
    Compute the SHA-256 hexadecimal digest of a file.
    
    Parameters:
        path (Path): File to hash.
    
    Returns:
        str: SHA-256 hexadecimal digest of the file contents.
    """
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def collatz_orbit(n: int, max_steps: int = 512) -> List[int]:
    """
    Build the Collatz sequence from a starting integer until it reaches 1.
    
    Parameters:
    	n (int): Starting integer.
    	max_steps (int): Maximum number of values allowed in the sequence.
    
    Returns:
    	List[int]: The Collatz orbit, including the starting integer and 1.
    
    Raises:
    	RuntimeError: If the sequence does not reach 1 within the step limit.
    """
    out = [n]
    while out[-1] != 1 and len(out) < max_steps:
        x = out[-1]
        out.append(x // 2 if x % 2 == 0 else 3 * x + 1)
    if out[-1] != 1:
        raise RuntimeError(f"Collatz guard exceeded for {n}")
    return out


def ramanujan_sum(q: int, n: int) -> int:
    """
    Compute the integer-valued Ramanujan sum for a modulus and index.
    
    Parameters:
    	q (int): The modulus used to select coprime terms.
    	n (int): The index applied to each term.
    
    Returns:
    	int: The Ramanujan sum rounded to the nearest integer.
    """
    total = 0.0
    for a in range(1, q + 1):
        if math.gcd(a, q) == 1:
            total += math.cos(2.0 * math.pi * a * n / q)
    return int(round(total))


def hardy_ramanujan_entropy(n: int) -> float:
    """Compute the Hardy–Ramanujan entropy approximation for an integer.
    
    Parameters:
    	n (int): The integer used in the approximation.
    
    Returns:
    	float: The entropy value, using 1 when n is less than 1.
    """
    return math.pi * math.sqrt(2.0 * max(n, 1) / 3.0)


def ramanujan_release_unit(pair: Tuple[int, int]) -> float:
    """
    Compute the Ramanujan release unit for a pair of seed integers.
    
    Parameters:
        pair (Tuple[int, int]): Seed integers used to derive the release value.
    
    Returns:
        float: A non-negative release unit.
    """
    p, q = pair
    n = p * q
    ref = 11 * 13
    entropy = hardy_ramanujan_entropy(n) / hardy_ramanujan_entropy(ref)
    orbit_p = collatz_orbit(p)
    orbit_q = collatz_orbit(q)
    depth = 0.5 * (len(orbit_p) + len(orbit_q)) + math.log1p(
        max(max(orbit_p), max(orbit_q))
    )
    q_values: Iterable[int] = (3, 4, 5, 7, 11, 13)
    resonance = sum(
        abs(ramanujan_sum(modulus, n)) / modulus for modulus in q_values
    ) / 6.0
    return max(0.0, entropy * math.log1p(depth) - resonance)


def load_sources() -> Tuple[
    Dict[str, float], Dict[int, float], Dict[int, Tuple[int, int]], Dict[str, Tuple[str, int]]
]:
    """
    Load and validate the representation and charged-fermion source artifacts.
    
    Returns:
        A tuple containing sector action units, generation action units, generation
        seed pairs, and a mapping from fermion names to sector and generation.
    
    Raises:
        FileNotFoundError: If a required source artifact is missing.
        RuntimeError: If either source fails validation or is incomplete.
    """
    if not ACTION_SOURCE.exists() or not REPRESENTATION_SOURCE.exists():
        raise FileNotFoundError("required v1.0 source artifact is missing")

    with REPRESENTATION_SOURCE.open(newline="", encoding="utf-8") as handle:
        rep_rows = list(csv.DictReader(handle))
    if not rep_rows or any(row["status"] != "allowed" for row in rep_rows):
        raise RuntimeError("corrected v1.0 representation gate is not fully allowed")

    sector_rep = {
        row["class"]: float(row["rep_action_unit_v10"])
        for row in rep_rows
        if row["class"] in {"charged_lepton", "down_quark", "up_quark"}
    }
    if set(sector_rep) != {"charged_lepton", "down_quark", "up_quark"}:
        raise RuntimeError("incomplete corrected representation source")

    sector_action = {sector: rep_action + 2.0 for sector, rep_action in sector_rep.items()}
    generation_action: Dict[int, float] = {}
    generation_seed: Dict[int, Tuple[int, int]] = {}
    particle_map: Dict[str, Tuple[str, int]] = {}

    with ACTION_SOURCE.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        if row["uses_observed_mass_as_input"] != "False":
            raise RuntimeError("mass-contaminated v1.0 source row")
        generation = int(row["assigned_generation_v10"])
        generation_action.setdefault(generation, float(row["generation_damping_unit"]))
        generation_seed.setdefault(generation, (int(row["seed_p"]), int(row["seed_q"])))
        particle_map[row["fermion"]] = (row["class"], generation)

    if set(generation_action) != {1, 2, 3} or len(particle_map) != 9:
        raise RuntimeError("incomplete charged-fermion source table")
    return sector_action, generation_action, generation_seed, particle_map


def sector_potential(candidate_id: str, action: float) -> float:
    """
    Compute the sector potential for a candidate formulation and action value.
    
    Parameters:
    	candidate_id (str): Identifier of the candidate formulation.
    	action (float): Sector action unit.
    
    Returns:
    	float: The candidate-specific sector potential.
    
    Raises:
    	KeyError: If `candidate_id` is not recognized.
    """
    if candidate_id == "C1_LINEAR_SEPARABLE_ACTION":
        return -action
    if candidate_id == "C2_QUARTER_POWER_SEPARABLE_ACTION":
        return -(action ** ALPHA_COLLATZ)
    if candidate_id == "C3_INVERSE_QUARTER_INFORMATION_POTENTIAL":
        return action ** (-ALPHA_COLLATZ) / (L3 * KAPPA)
    raise KeyError(candidate_id)


def generation_release(
    candidate_id: str,
    generation_action_unit: float,
    ramanujan_unit: float,
) -> float:
    """
    Calculate the generation contribution for a candidate formulation, including the Ramanujan release.
    
    Parameters:
    	candidate_id (str): Identifier of the candidate formulation.
    	generation_action_unit (float): Generation action unit used to calculate the base contribution.
    	ramanujan_unit (float): Ramanujan release added to the base contribution.
    
    Returns:
    	float: The candidate-specific generation contribution including the Ramanujan release.
    
    Raises:
    	KeyError: If candidate_id is not a recognized candidate formulation.
    """
    if candidate_id == "C1_LINEAR_SEPARABLE_ACTION":
        base = -generation_action_unit
    elif candidate_id == "C2_QUARTER_POWER_SEPARABLE_ACTION":
        base = -(generation_action_unit ** ALPHA_COLLATZ)
    elif candidate_id == "C3_INVERSE_QUARTER_INFORMATION_POTENTIAL":
        base = generation_action_unit ** (-ALPHA_COLLATZ) / (L3 * KAPPA)
    else:
        raise KeyError(candidate_id)
    return base + ramanujan_unit


def ratio(log_coordinates: Dict[str, float], numerator: str, denominator: str) -> float:
    """
    Compute the ratio represented by two logarithmic coordinates.
    
    Parameters:
    	log_coordinates (Dict[str, float]): Mapping of names to logarithmic values.
    	numerator (str): Name of the numerator coordinate.
    	denominator (str): Name of the denominator coordinate.
    
    Returns:
    	float: Exponential ratio of the numerator coordinate to the denominator coordinate.
    """
    return math.exp(log_coordinates[numerator] - log_coordinates[denominator])


def main() -> None:
    """
    Freeze the candidate family and write its JSON and CSV artifacts.
    
    The generated candidates and ratio observables are computed from the pre-frozen
    source data without performing mass benchmarking or inspecting future
    likelihoods.
    """
    sector_action, generation_action, generation_seed, particle_map = load_sources()
    ramanujan_release = {
        generation: ramanujan_release_unit(pair)
        for generation, pair in generation_seed.items()
    }

    candidates: Dict[str, object] = {}
    csv_rows: List[Dict[str, object]] = []

    for candidate_id in CANDIDATE_IDS:
        sector_values = {
            sector: sector_potential(candidate_id, action)
            for sector, action in sector_action.items()
        }
        generation_values = {
            generation: generation_release(
                candidate_id,
                generation_action[generation],
                ramanujan_release[generation],
            )
            for generation in generation_action
        }
        log_coordinates = {
            particle: sector_values[sector] + generation_values[generation]
            for particle, (sector, generation) in particle_map.items()
        }
        frozen_ratios = {
            # Same generation, different sector: class-A baseline observable.
            "class_A_yc_over_ymu": ratio(log_coordinates, "c", "mu"),
            # Same sector, different generation: class-B release observable.
            "class_B_yc_over_yt": ratio(log_coordinates, "c", "t"),
            # Diagnostics and cross-transfer outputs; not used for candidate selection.
            "diagnostic_yc_over_ytau": ratio(log_coordinates, "c", "tau"),
            "cross_transfer_ys_over_ymu": ratio(log_coordinates, "s", "mu"),
            "cross_transfer_yu_over_ye": ratio(log_coordinates, "u", "e"),
            "generation_ymu_over_ye": ratio(log_coordinates, "mu", "e"),
            "generation_ytau_over_ymu": ratio(log_coordinates, "tau", "mu"),
            "generation_yc_over_yu": ratio(log_coordinates, "c", "u"),
            "generation_yt_over_yc": ratio(log_coordinates, "t", "c"),
        }
        candidates[candidate_id] = {
            "sector_potential": sector_values,
            "generation_release": {str(k): v for k, v in generation_values.items()},
            "particle_log_coordinates": log_coordinates,
            "frozen_ratios": frozen_ratios,
        }
        for observable, value in frozen_ratios.items():
            csv_rows.append(
                {
                    "candidate_id": candidate_id,
                    "observable": observable,
                    "frozen_ratio": value,
                    "uses_observed_mass": False,
                    "uses_future_likelihood": False,
                }
            )

    payload: Dict[str, object] = {
        "schema": "TIR_SEPARABLE_UNIVERSAL_CANDIDATE_FAMILY_V10_7",
        "created_date": "2026-07-29",
        "formula_count": len(CANDIDATE_IDS),
        "mass_benchmark_performed": False,
        "future_likelihood_inspected": False,
        "canonical_promotion_allowed": False,
        "constants": {
            "kappa_ln2_over_24pi": KAPPA,
            "L3": L3,
            "alpha_collatz": ALPHA_COLLATZ,
        },
        "architecture": (
            "log_y(f,g)=F(S_f)+D(G_g,R_g); F is sector-invariant and D is "
            "universal across charged families"
        ),
        "source_git_blobs": SOURCE_GIT_BLOBS,
        "source_file_sha256": {
            str(ACTION_SOURCE.relative_to(ROOT)): sha256_file(ACTION_SOURCE),
            str(REPRESENTATION_SOURCE.relative_to(ROOT)): sha256_file(REPRESENTATION_SOURCE),
        },
        "sector_action_units": sector_action,
        "generation_action_units": {str(k): v for k, v in generation_action.items()},
        "ramanujan_release_units": {str(k): v for k, v in ramanujan_release.items()},
        "candidates": candidates,
        "prospective_observables": {
            "class_A": (
                "direct charm-to-muon Higgs coupling ratio y_c/y_mu from the first "
                "qualifying post-2026-07-29 joint ATLAS/CMS likelihood"
            ),
            "class_B": (
                "direct charm-to-top Higgs coupling ratio y_c/y_t from the first "
                "qualifying post-2026-07-29 joint ATLAS/CMS likelihood"
            ),
        },
        "method_status": "PROSPECTIVE_CANDIDATE_FAMILY_FROZEN_NO_SELECTION",
        "forbidden_operator_inputs": sorted(FORBIDDEN_OPERATOR_INPUTS),
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["candidate_family_fingerprint_sha256"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()

    json_path = RESULTS / "separable_universal_candidate_family_v10_7.json"
    json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    csv_path = RESULTS / "separable_universal_candidate_predictions_v10_7.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(csv_rows[0].keys()))
        writer.writeheader()
        writer.writerows(csv_rows)

    print(json.dumps({
        "status": "PASS",
        "formula_count": len(CANDIDATE_IDS),
        "fingerprint": payload["candidate_family_fingerprint_sha256"],
        "json": str(json_path),
        "csv": str(csv_path),
    }, indent=2))


if __name__ == "__main__":
    main()
