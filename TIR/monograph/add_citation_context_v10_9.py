#!/usr/bin/env python3
"""Integrate local scientific citations and audit coverage for the Metatime monograph.

The script is deterministic and idempotent. It inserts one clearly delimited
"Established context" paragraph into every monograph chapter and appendix,
validates all cited bibliography keys, and writes Markdown/JSON coverage reports.
The inserted citations establish external context only; they do not promote or
validate original TIR/Metatime claims.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parent
BIBLIOGRAPHY = ROOT / "references_expanded_v10_8.tex"
REPORT_MD = ROOT / "CITATION_COVERAGE_v11_0.md"
REPORT_JSON = ROOT / "citation_coverage_v11_0.json"
BEGIN = "% CITATION_CONTEXT_V10_9_BEGIN"
END = "% CITATION_CONTEXT_V10_9_END"

CONTEXTS: Dict[str, str] = {
    "chapters/ch01_introduction.tex": r"""\paragraph{Established context.}
The conventional particle-physics reference values used for comparison are those
of the Particle Data Group, while the information-theoretic and geometric-phase
background begins with Shannon's communication theory and the Berry-phase
literature \cite{PDG2024,shannon1948,Simon1983,berry1984}.  The criteria used here
to distinguish an exploratory ansatz from an empirically established result follow
the falsifiability and reproducibility literature \cite{Popper1959,Munafo2017}.
These sources establish external context only; the TIR/Metatime identifications
and formulae developed below are original hypotheses unless explicitly stated
otherwise.""",
    "chapters/ch02_metatime_framework.tex": r"""\paragraph{Established context.}
The standard geometric ingredients behind phase holonomy, quantum-state metrics,
and cyclic evolution are described by Pancharatnam, Simon, Berry,
Aharonov--Anandan, and Provost--Vall\'ee
\cite{Pancharatnam1956,Simon1983,berry1984,AharonovAnandan1987,ProvostVallee1980}.
Connections to information geometry are conventional in the sense of Fisher,
Rao, and Amari--Nagaoka \cite{Fisher1925,Rao1945,AmariNagaoka2000}; the specific
Metatime synthesis and its operator assignments are the construction tested in
this monograph.""",
    "chapters/ch03_l_constants.tex": r"""\paragraph{Established context.}
The number-theoretic vocabulary used in defining the discrete $L$-constants is
standard and may be compared with classical analytic number theory and
Ramanujan's work \cite{Apostol1976,HardyWright2008,Ramanujan1918,HardyRamanujan1918}.
No cited source derives the particular values or physical assignments proposed
here; those assignments remain internal TIR hypotheses.""",
    "chapters/ch04_quark_primes.tex": r"""\paragraph{Established context.}
Prime-number structure, bounded prime gaps, and asymptotic prime-pair reasoning
are established mathematical subjects \cite{HardyLittlewood1923,Zhang2014,Polymath2014,Maynard2015,HardyWright2008}.
The conventional quark classification originates in the Gell-Mann and Zweig
models and is summarized in modern reference data \cite{GellMann1964,Zweig1964,PDG2024}.
The association of particular prime seeds with quark sectors is original to the
present ansatz.""",
    "chapters/ch05_electron_action.tex": r"""\paragraph{Established context.}
The relativistic electron, chiral spinor structure, electroweak interactions, and
mass generation are conventionally grounded in the work of Dirac, Weyl,
Glashow, Weinberg, Salam, and Higgs
\cite{Dirac1928,Weyl1929,Glashow1961,Weinberg1967,Salam1968,Higgs1964}.
Numerical comparisons use the Particle Data Group \cite{PDG2024}; the geometric
action assigned to the electron below is not a result of those references.""",
    "chapters/ch06_generation_release.tex": r"""\paragraph{Established context.}
The $3n+1$ map and its stopping-time statistics are reviewed by Terras, Lagarias,
Wirsching, and Tao \cite{Terras1976,Lagarias1985,Wirsching1998,Tao2022Collatz}.
Ramanujan and Hardy--Ramanujan provide the classical analytic background for the
release terms used here \cite{Ramanujan1918,HardyRamanujan1918}; their physical
interpretation as generation release is specific to TIR.""",
    "chapters/ch07_lepton_spectrum.tex": r"""\paragraph{Established context.}
Charged-lepton masses and Standard Model conventions are taken from current
reference data \cite{PDG2024}.  The conventional Higgs mechanism and its
experimental discovery are documented in the foundational and LHC literature
\cite{EnglertBrout1964,Higgs1964,GHK1964,ATLAS2012Higgs,CMS2012Higgs}.
The low-parameter spectral relations tested below are independent hypotheses and
are not implied by those sources.""",
    "chapters/ch08_gmo_formula.tex": r"""\paragraph{Established context.}
The hadronic classification and mass relations used as the comparison baseline
are the Gell-Mann--Okubo framework
\cite{gellmann1961,GellMann1962,okubo1962}, with numerical masses taken from the
Particle Data Group \cite{PDG2024}.  The replacement of fitted coefficients by
Metatime expressions is the novel step evaluated in this chapter.""",
    "chapters/ch09_octet_m0.tex": r"""\paragraph{Established context.}
Baryon-octet organization follows the established SU(3) classification of
Gell-Mann, Ne'eman, and Okubo \cite{gellmann1961,Neeman1961,GellMann1962,okubo1962}.
Modern hadron masses are taken from the Particle Data Group \cite{PDG2024}; the
proposed derivation of $M_0$ is a TIR construction rather than a standard QCD
result.""",
    "chapters/ch10_octet_coefficients.tex": r"""\paragraph{Established context.}
The coefficients compared here belong to the conventional Gell-Mann--Okubo mass
organization \cite{GellMann1962,okubo1962}.  QCD supplies the accepted microscopic
framework for strong interactions \cite{GrossWilczek1973,Politzer1973,Wilson1974},
while the coefficient identities below are phenomenological Metatime proposals
benchmarked against PDG data \cite{PDG2024}.""",
    "chapters/ch11_octet_predictions.tex": r"""\paragraph{Established context.}
The octet assignments and empirical targets are fixed by SU(3) flavor
classification and Particle Data Group masses
\cite{GellMann1962,okubo1962,PDG2024}.  Agreement or disagreement of the tabulated
predictions is therefore an empirical test of the present ansatz, not evidence
supplied by the cited classification itself.""",
    "chapters/ch12_decuplet_m0prime.tex": r"""\paragraph{Established context.}
The baryon decuplet is part of the established SU(3) flavor scheme
\cite{gellmann1961,GellMann1962,Neeman1961}, and its measured masses are reported
by the Particle Data Group \cite{PDG2024}.  The expression for $M'_0$ proposed
below is specific to the Metatime construction.""",
    "chapters/ch13_decuplet_predictions.tex": r"""\paragraph{Established context.}
The decuplet multiplet and equal-spacing phenomenology arise from the established
SU(3) program \cite{GellMann1962,okubo1962}; numerical comparison uses PDG masses
\cite{PDG2024}.  The predictions in this chapter are consequently judged against
external data while retaining their status as model-dependent TIR outputs.""",
    "chapters/ch14_pseudoscalar_mesons.tex": r"""\paragraph{Established context.}
Meson flavor assignments follow the quark model and SU(3) classification
\cite{GellMann1962,GellMann1964,Zweig1964}.  The accepted strong-interaction
framework is QCD \cite{GrossWilczek1973,Politzer1973,Wilson1974}, and empirical
masses are taken from the Particle Data Group \cite{PDG2024}.  The numerical
mass map developed below is an additional ansatz.""",
    "chapters/ch15_heavy_mesons.tex": r"""\paragraph{Established context.}
Heavy-meson identities and masses are conventional quark-model and PDG data
\cite{GellMann1964,Zweig1964,PDG2024}, interpreted within QCD
\cite{GrossWilczek1973,Politzer1973,Wilson1974}.  The prime-seed and Metatime
relations assigned to these states are original model hypotheses.""",
    "chapters/ch16_pmns_mixing.tex": r"""\paragraph{Established context.}
Lepton mixing originates in the Pontecorvo and Maki--Nakagawa--Sakata framework
\cite{Pontecorvo1957,Maki1962}.  Matter effects and decisive oscillation evidence
are documented by Wolfenstein, Mikheyev--Smirnov, Super-Kamiokande, SNO, KamLAND,
and Daya Bay
\cite{Wolfenstein1978,MikheyevSmirnov1985,SuperK1998,SNO2002,KamLAND2003,DayaBay2012}.
The angle formulae below are TIR predictions compared with the modern PDG summary
\cite{PDG2024}.""",
    "chapters/ch17_neutrino_masses.tex": r"""\paragraph{Established context.}
Nonzero neutrino mass is established through oscillation observations
\cite{SuperK1998,SNO2002,KamLAND2003,DayaBay2012}, while absolute and cosmological
constraints are summarized by the Particle Data Group and Planck
\cite{PDG2024,Planck2018}.  The absolute hierarchy and scale generated below are
model outputs; oscillation experiments do not by themselves establish this
specific spectrum.""",
    "chapters/ch18_ckm_matrix.tex": r"""\paragraph{Established context.}
Quark mixing is conventionally described by the Cabibbo and
Kobayashi--Maskawa framework, often expressed through the Wolfenstein
parameterization \cite{Cabibbo1963,kobayashi1973,Wolfenstein1983}.  Empirical
matrix elements are taken from the Particle Data Group \cite{PDG2024}; the
Metatime construction of those entries is the claim under test.""",
    "chapters/ch19_ckm_cp_violation.tex": r"""\paragraph{Established context.}
CP violation in the three-generation quark sector is encoded by the
Kobayashi--Maskawa phase and the basis-invariant Jarlskog measure
\cite{kobayashi1973,Jarlskog1985,Wolfenstein1983}.  Numerical reference values are
those of the Particle Data Group \cite{PDG2024}; the geometric explanation
proposed below is not contained in the standard formalism.""",
    "chapters/ch20_higgs_vev.tex": r"""\paragraph{Established context.}
Spontaneous electroweak symmetry breaking and gauge-boson mass generation are
established by the Brout--Englert, Higgs, and Guralnik--Hagen--Kibble mechanisms
\cite{EnglertBrout1964,Higgs1964,GHK1964}.  Electroweak normalization follows
Glashow--Weinberg--Salam and modern reference data
\cite{Glashow1961,Weinberg1967,Salam1968,PDG2024,CODATA2022}; the Metatime
expression for the vacuum expectation value is an additional derivation claim.""",
    "chapters/ch21_weinberg_angle.tex": r"""\paragraph{Established context.}
The weak mixing angle belongs to the Glashow--Weinberg--Salam electroweak theory
\cite{Glashow1961,Weinberg1967,Salam1968}.  Experimental conventions and values
are taken from the Particle Data Group \cite{PDG2024}; the discrete geometric
formula proposed here is evaluated against, rather than derived from, that
standard reference.""",
    "chapters/ch22_fine_structure.tex": r"""\paragraph{Established context.}
The fine-structure constant and associated precision values are taken from
CODATA and the Particle Data Group \cite{CODATA2022,PDG2024}.  The accepted QED
framework is represented by Dirac, Tomonaga, Schwinger, Feynman, and Dyson
\cite{Dirac1928,Tomonaga1946,Schwinger1948,Feynman1949,Dyson1949}; the informational
formula below is a separate low-parameter ansatz.""",
    "chapters/ch23_gauge_bosons.tex": r"""\paragraph{Established context.}
Non-Abelian gauge theory and electroweak unification originate with Yang--Mills
and Glashow--Weinberg--Salam \cite{YangMills1954,Glashow1961,Weinberg1967,Salam1968}.
Mass generation uses the established symmetry-breaking mechanism
\cite{EnglertBrout1964,Higgs1964,GHK1964}, and numerical boson properties are
benchmarked against PDG data \cite{PDG2024}.""",
    "chapters/ch24_higgs_mass.tex": r"""\paragraph{Established context.}
The scalar mechanism is founded on the 1964 symmetry-breaking papers
\cite{EnglertBrout1964,Higgs1964,GHK1964}, and the observed Higgs-like boson was
reported by ATLAS and CMS \cite{ATLAS2012Higgs,CMS2012Higgs}.  The current mass
reference is the Particle Data Group \cite{PDG2024}; the discrete mass relation
below is a model prediction rather than part of the discovery analyses.""",
    "chapters/ch25_strong_cp_angle.tex": r"""\paragraph{Established context.}
The strong-CP problem is tied to nonperturbative gauge topology and the QCD
vacuum, with standard discussions including 't Hooft, Peccei--Quinn, Weinberg,
and Wilczek \cite{tHooft1976,PecceiQuinn1977,Weinberg1978Axion,Wilczek1978Axion}.
Phenomenological consequences are reviewed by Crewther and Pospelov--Ritz
\cite{crewther1979,pospelov2005}; the value derived here is the distinct TIR
proposal.""",
    "chapters/ch26_neutron_edm.tex": r"""\paragraph{Established context.}
The link between a QCD CP phase and the neutron electric dipole moment follows
the chiral and effective-field-theory literature
\cite{crewther1979,pospelov2005}.  The experimental bound is represented by the
modern neutron-EDM measurement \cite{Abel2020nEDM}.  The numerical mapping from
the Metatime angle to $d_n$ is therefore directly falsifiable against external
data.""",
    "chapters/ch27_hypercharge.tex": r"""\paragraph{Established context.}
Hypercharge assignments and electroweak representations belong to the
Glashow--Weinberg--Salam model \cite{Glashow1961,Weinberg1967,Salam1968}, with
modern conventions summarized by the Particle Data Group \cite{PDG2024}.
Consistency is constrained by gauge and global anomaly structure
\cite{Adler1969,BellJackiw1969,witten1982}; the discrete derivation attempted
below is an additional claim.""",
    "chapters/ch28_anomaly_cancellation.tex": r"""\paragraph{Established context.}
Local chiral anomalies are described by Adler, Bell--Jackiw, and 't Hooft
\cite{Adler1969,BellJackiw1969,tHooft1976}, while the global SU(2) obstruction is
Witten's anomaly \cite{witten1982}.  Standard Model charge assignments provide
the accepted cancellation pattern \cite{Weinberg1967,PDG2024}; the TIR account
seeks a geometric origin for that established consistency condition.""",
    "chapters/ch29_dark_energy.tex": r"""\paragraph{Established context.}
Relativistic cosmology is based on Einstein, Friedmann, and Lema\^itre
\cite{Einstein1915,Friedmann1922,Lemaitre1927}.  Late-time acceleration is
established by supernova observations and constrained by Planck and DESI
\cite{Riess1998,Perlmutter1999,Planck2018,DESI2024}.  The cosmological-constant
problem and information-related gravitational ideas provide context
\cite{Weinberg1989CC,Carroll2001,Bekenstein1973,Hawking1975,Jacobson1995}; the
specific Metatime density formula remains an original ansatz.""",
    "chapters/ch30_parameter_summary.tex": r"""\paragraph{Established context.}
The summary tables compare model outputs with external reference compilations and
major measurements, principally PDG, CODATA, Planck, and the Higgs and neutrino
experiments \cite{PDG2024,CODATA2022,Planck2018,ATLAS2012Higgs,CMS2012Higgs,SuperK1998,SNO2002}.
A close numerical match is treated as a retrospective comparison unless a
prediction and decision rule were frozen before inspection of the relevant data.""",
    "chapters/ch31_open_problems.tex": r"""\paragraph{Established context.}
The open-problem ledger follows falsifiability, preregistration, and reproducible
computational practice \cite{Popper1959,Lakatos1978,Sandve2013,Wilson2014,Munafo2017,Nosek2018,Stark2018}.
Prospective Higgs-coupling gates are anchored to direct experimental searches and
current reference data \cite{ATLAS2022Charm,PDG2024}.  A failed frozen test is to
be retained as a failure rather than repaired by post-hoc parameter changes.""",
    "appendices/appA_kappa_derivation.tex": r"""\paragraph{Established context.}
The informational and thermodynamic vocabulary surrounding $\ln 2$ is grounded
in Shannon, Landauer, Bennett, and modern information theory
\cite{shannon1948,Landauer1961,Bennett1982,CoverThomas2006}.  Geometric-phase
normalization is compared with Berry and Simon \cite{Simon1983,berry1984}; the
specific coefficient $\ln 2/(24\pi)$ is the monograph's own proposed invariant.""",
    "appendices/appB_collatz_tables.tex": r"""\paragraph{Established context.}
The tabulated $3n+1$ trajectories should be read against the mathematical Collatz
literature \cite{Terras1976,Lagarias1985,Wirsching1998,Tao2022Collatz}.  Exhaustive
finite tables verify only the stated computational range and do not constitute a
proof of the Collatz conjecture.""",
    "appendices/appC_su3_primer.tex": r"""\paragraph{Established context.}
The SU(3) flavor primer follows the historical classification of Gell-Mann,
Ne'eman, and Okubo \cite{gellmann1961,Neeman1961,GellMann1962,okubo1962}, while
QCD is the accepted gauge theory of strong interactions
\cite{GrossWilczek1973,Politzer1973,Wilson1974}.""",
    "appendices/appD_poincare_disk.tex": r"""\paragraph{Established context.}
The differential-geometric and topological language used for disk geometry,
connections, curvature, and bundles follows standard references
\cite{KobayashiNomizu1963,BottTu1982,Nakahara2003}.  The embedding of the
Metatime state construction into this geometry is specific to the present model.""",
    "appendices/appE_tetrahedron_algebra.tex": r"""\paragraph{Established context.}
The bundle, characteristic-class, and quantum-state geometric background is
represented by Hopf, Chern, Bott--Tu, Nakahara, and Bengtsson--Zyczkowski
\cite{Hopf1931,Chern1946,BottTu1982,Nakahara2003,BengtssonZyczkowski2006}.
The tetrahedral algebra and its physical labels are original TIR structures.""",
    "appendices/appF_baryon_calculations.tex": r"""\paragraph{Established context.}
The calculation tables implement the Gell-Mann--Okubo classification
\cite{GellMann1962,okubo1962} and compare with Particle Data Group masses
\cite{PDG2024}.  Arithmetic reproduction of the displayed formulae is distinct
from establishing their physical derivation.""",
    "appendices/appG_meson_calculations.tex": r"""\paragraph{Established context.}
Meson assignments follow the quark model and SU(3) literature
\cite{GellMann1962,GellMann1964,Zweig1964}, and measured masses are taken from the
Particle Data Group \cite{PDG2024}.  The appendix records the model's numerical
trace rather than a standard QCD calculation.""",
    "appendices/appH_pdg_tables.tex": r"""\paragraph{Established context.}
The numerical reference tables are sourced from the Particle Data Group, CODATA,
and cosmological parameter compilations where applicable
\cite{PDG2024,CODATA2022,Planck2018}.  Version and scheme dependence must be
retained whenever values are updated.""",
    "appendices/appI_source_code.tex": r"""\paragraph{Established context.}
The source-code appendix is governed by reproducible-research and scientific
computing practices \cite{Sandve2013,Wilson2014,Munafo2017,Stark2018}.  Executable
agreement with a formula establishes technical reproducibility, not empirical
truth of the underlying physical model.""",
    "appendices/appJ_collatz_quarter_power_scaling.tex": r"""\paragraph{Established context.}
The accelerated Collatz map and stopping-time background follow Terras, Lagarias,
Wirsching, and Tao \cite{Terras1976,Lagarias1985,Wirsching1998,Tao2022Collatz}.
Ramanujan and Hardy--Ramanujan supply the analytic-number-theory layer
\cite{Ramanujan1918,HardyRamanujan1918}; the quarter-power mass bridge is the
specific hypothesis audited in this appendix.""",
    "appendices/appK_sector_holonomy_release.tex": r"""\paragraph{Established context.}
Holonomy and geometric phase are established by Simon, Berry, and Wilczek--Zee
\cite{Simon1983,berry1984,WilczekZee1984}, while the generation coordinate uses
the Collatz and Ramanujan context
\cite{Lagarias1985,Tao2022Collatz,Ramanujan1918}.  The sector-holonomy candidate
is retrospective and must not be read as a consequence of those sources.""",
    "appendices/appL_up_sector_common_baseline_no_go.tex": r"""\paragraph{Established context.}
The no-go result is an internal algebraic theorem for the frozen v10.2 trace.
Its scientific handling follows falsification and preproducibility principles
\cite{Popper1959,Lakatos1978,Nosek2018,Stark2018}: an excluded architecture is
retained as excluded rather than rescued by an unregistered correction.""",
    "appendices/appM_prospective_observable_identifiability.tex": r"""\paragraph{Established context.}
Observable selection and cancellation tests are governed by preregistration and
reproducibility principles \cite{Nosek2018,Munafo2017,Stark2018}.  Experimental
anchoring uses direct Higgs--charm constraints and current particle reference data
\cite{ATLAS2022Charm,PDG2024}; the assigned future ratios remain frozen model
predictions.""",
    "appendices/appN_separable_candidate_family.tex": r"""\paragraph{Established context.}
The candidate-family freeze follows falsifiability, preregistration, and
multiplicity-aware interpretation \cite{Popper1959,Nosek2018,Munafo2017}.  Its
geometric and arithmetic ingredients are externally contextualized by Berry,
Collatz, and Ramanujan literature
\cite{berry1984,Lagarias1985,Tao2022Collatz,Ramanujan1918}, while the three
specific maps and their Yukawa-ratio predictions are original TIR candidates.""",
    "appendices/appO_publication_protocol.tex": r"""\paragraph{Established context.}
Model comparison, likelihood inference, preregistration, and reproducible
computation are grounded in the statistical and methodological literature
\cite{Akaike1974,Schwarz1978,Wilks1938,Cowan2011,Nosek2018,Sandve2013}.
The protocol below applies those norms to interpretation of this monograph.""",
}


def bibliography_keys() -> set[str]:
    """
    Extract all bibliography entry keys from the configured bibliography file.
    
    Returns:
    	set[str]: The bibliography keys found in `\\bibitem{...}` entries.
    """
    text = BIBLIOGRAPHY.read_text(encoding="utf-8")
    return set(re.findall(r"\\bibitem\{([^}]+)\}", text))


def cited_keys(text: str) -> List[str]:
    """
    Extract citation keys from LaTeX citation commands.
    
    Parameters:
        text (str): LaTeX source text containing citation commands.
    
    Returns:
        List[str]: Citation keys in their order of appearance.
    """
    keys: List[str] = []
    for group in re.findall(r"\\cite\{([^}]+)\}", text):
        keys.extend(k.strip() for k in group.split(",") if k.strip())
    return keys


def insert_after_heading(text: str, block: str) -> str:
    """
    Insert a marked context block after the first chapter heading.
    
    Parameters:
        text (str): LaTeX document content.
        block (str): Context text to insert.
    
    Returns:
        str: The document content with the marked block inserted.
    
    Raises:
        ValueError: If the document contains no chapter command.
    """
    lines = text.splitlines(keepends=True)
    chapter_idx = next(
        (i for i, line in enumerate(lines) if line.lstrip().startswith("\\chapter")),
        None,
    )
    if chapter_idx is None:
        raise ValueError("No \\chapter command found")
    insert_at = chapter_idx + 1
    while insert_at < len(lines):
        stripped = lines[insert_at].strip()
        if not stripped or stripped.startswith("\\label{"):
            insert_at += 1
            continue
        break
    lines.insert(insert_at, "\n" + BEGIN + "\n" + block.strip() + "\n" + END + "\n\n")
    return "".join(lines)


def apply_context(path: Path, block: str) -> bool:
    """
    Apply a delimited context block to a LaTeX file when it has not already been inserted.
    
    Parameters:
    	path (Path): The target LaTeX file.
    	block (str): The context paragraph to insert.
    
    Returns:
    	bool: `True` if the context was inserted, `False` if the file already contains it.
    """
    text = path.read_text(encoding="utf-8")
    if BEGIN in text:
        return False
    path.write_text(insert_after_heading(text, block), encoding="utf-8")
    return True


def update_version() -> None:
    """
    Update the monograph's first version line to the publication candidate version.
    """
    root = ROOT / "metatime_monograph.tex"
    text = root.read_text(encoding="utf-8")
    text = re.sub(
        r"%% Version [^\n]+",
        "%% Version 11.0 - Publication Candidate",
        text,
        count=1,
    )
    root.write_text(text, encoding="utf-8")


def write_reports(rows: List[dict], bib_count: int, unique_cited: set[str]) -> None:
    """
    Write JSON and Markdown citation coverage reports from the audit results.
    
    Parameters:
        rows (List[dict]): Per-file audit records containing citation counts, unique key counts, and context status.
        bib_count (int): Number of entries in the expanded bibliography.
        unique_cited (set[str]): Bibliography keys cited across all audited files.
    """
    zero = [row["path"] for row in rows if row["citation_commands"] == 0]
    payload = {
        "version": "v11.0",
        "bibliography_entries": bib_count,
        "covered_files": len(rows),
        "files_without_citations": zero,
        "unique_cited_keys": len(unique_cited),
        "rows": rows,
    }
    REPORT_JSON.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    lines = [
        "# Citation Coverage Audit v11.0",
        "",
        "Status: `PASS` if every listed chapter and appendix contains at least one local citation and every citation key resolves to the expanded bibliography.",
        "",
        f"- Bibliography entries: **{bib_count}**",
        f"- Audited chapters and appendices: **{len(rows)}**",
        f"- Files with zero local citations: **{len(zero)}**",
        f"- Unique bibliography keys cited locally: **{len(unique_cited)}**",
        "",
        "The inserted paragraphs establish external scientific context only. They do not assert that cited authors endorse TIR/Metatime or that original model claims follow from the cited work.",
        "",
        "| File | Citation commands | Unique keys | local context |",
        "|---|---:|---:|---|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['path']}` | {row['citation_commands']} | {row['unique_keys']} | "
            f"{'inserted' if row['context_present'] else 'missing'} |"
        )
    if zero:
        lines.extend(["", "## FAIL: files without local citations", ""])
        lines.extend(f"- `{path}`" for path in zero)
    else:
        lines.extend(["", "## Result", "", "`TECHNICAL PASS - LOCAL CITATION COVERAGE COMPLETE`"])
    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """
    Audit mapped monograph files, update citation context and version metadata, and generate coverage reports.
    
    Raises:
        SystemExit: If the bibliography is empty, mapped files or citation keys are invalid,
            or an audited file has no local citations.
    """
    bib = bibliography_keys()
    if not bib:
        raise SystemExit("No bibliography keys found")
    changed: List[str] = []
    missing_files: List[str] = []
    for rel, block in CONTEXTS.items():
        path = ROOT / rel
        if not path.exists():
            missing_files.append(rel)
            continue
        missing_keys = sorted(set(cited_keys(block)) - bib)
        if missing_keys:
            raise SystemExit(f"Unknown bibliography keys in {rel}: {missing_keys}")
        if apply_context(path, block):
            changed.append(rel)
    if missing_files:
        raise SystemExit(f"Mapped files do not exist: {missing_files}")
    update_version()
    rows: List[dict] = []
    unique_cited: set[str] = set()
    unresolved: Dict[str, List[str]] = {}
    for rel in sorted(CONTEXTS):
        text = (ROOT / rel).read_text(encoding="utf-8")
        keys = cited_keys(text)
        unique = set(keys)
        unique_cited.update(unique)
        bad = sorted(unique - bib)
        if bad:
            unresolved[rel] = bad
        rows.append({
            "path": rel,
            "citation_commands": len(re.findall(r"\\cite\{", text)),
            "unique_keys": len(unique),
            "context_present": BEGIN in text and END in text,
        })
    if unresolved:
        raise SystemExit(f"Unresolved citation keys: {unresolved}")
    write_reports(rows, len(bib), unique_cited)
    zero = [row["path"] for row in rows if row["citation_commands"] == 0]
    print(f"Citation contexts inserted in {len(changed)} files.")
    print(f"Audited {len(rows)} files against {len(bib)} bibliography entries.")
    print(f"Unique locally cited keys: {len(unique_cited)}.")
    if zero:
        raise SystemExit(f"Files without local citations: {zero}")
    print("TECHNICAL PASS - LOCAL CITATION COVERAGE COMPLETE")


if __name__ == "__main__":
    main()
