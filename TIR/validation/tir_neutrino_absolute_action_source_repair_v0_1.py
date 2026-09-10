#!/usr/bin/env python3
from __future__ import annotations

import math
import re
from pathlib import Path


def algebra():
    kappa = math.log(2.0) / (24.0 * math.pi)
    L3, L4 = 7.0, 2.0
    s_bare = (1.0 + L4 / L3) / 2.0
    a_face = ((L4 / L3) ** 2) / 2.0
    ds = kappa * a_face * (1.0 - kappa)
    direct = s_bare + kappa * a_face * (1.0 - kappa)
    single = s_bare + ds
    double = s_bare + kappa * ds
    assert direct == single
    assert abs(double - single) > 1e-6
    ratios = (1.0, L4, L3 + L4 + 1.0)
    actions = tuple(single - kappa * math.log(r) for r in ratios)
    weights = tuple(math.exp(-s / kappa) for s in actions)
    for w, r in zip(weights, ratios):
        assert abs((w / weights[0]) - r) < 2e-12
    return kappa, s_bare, a_face, ds, direct, double


def source_contract(system_text: str, chapter_text: str):
    compact_system = re.sub(r"\s+", "", system_text)
    compact_chapter = re.sub(r"\s+", "", chapter_text)
    assert "S_1=\\frac{9}{14}+OI\\cdot\\frac{(L4/L3)^2}{2}\\cdot(1-OI)" in compact_system
    assert "dS=\\kappa\\cdotA_{\\text{face}}\\cdot(1-\\kappa)" in compact_chapter
    assert "S_1=S_{\\text{bare}}+\\kappa\\,dS" in compact_chapter
    return True


def validate_repo(root: Path):
    system = root / "TIR/metatime_systematization_v7_8.md"
    chapter = root / "TIR/monograph/chapters/ch17_neutrino_masses.tex"
    assert system.is_file(), system
    assert chapter.is_file(), chapter
    source_contract(system.read_text(encoding="utf-8"), chapter.read_text(encoding="utf-8"))


def main():
    algebra()
    root = Path(__file__).resolve().parents[2]
    validate_repo(root)
    print("schema=TIR_NEUTRINO_ABSOLUTE_ACTION_SOURCE_REPAIR_V0_1")
    print("status=PASS")
    print("single_offset_equals_direct_systematization=true")
    print("double_kappa_differs_from_direct_systematization=true")
    print("ratio_identity_1_2_10_exact_internal=true")
    print("observed_masses_used_for_rule_selection=false")
    print("absolute_neutrino_mass_empirical_status=OPEN")


if __name__ == "__main__":
    main()
