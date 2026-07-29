# The Fundamental Theory of Informational Relations

https://www.researchgate.net/publication/408131825_Metatime_A_Low-Parameter_Ansatz_for_Standard_Model_Parameters_from_Geometric_Phase_Information_Theory

**Author:** Adrian Lipa — Independent Researcher, Doncaster, United Kingdom  
**Current monograph:** Metatime v11.0 Publication Candidate  
**Research status:** exploratory phenomenological programme; not a peer-reviewed confirmation of a final physical theory

## Overview

The **Fundamental Theory of Informational Relations (TIR)** is an exploratory research programme investigating whether geometric phase, information geometry, discrete arithmetic structure, holonomy, synchronization, and low-parameter relations can organize selected particle-physics, flavor, hadronic, and cosmological observables.

The current monograph develops the **Metatime** formulation around the informational preference quantum

\[
\kappa = \frac{\ln 2}{24\pi},
\]

which is treated in this repository as a **model postulate with structural motivation**, not as an established theorem of quantum field theory or differential geometry.

The programme includes:

- geometric-phase and information-geometric constructions;
- Bloch, Berry, Fubini–Study, holonomy, and spin-related structures;
- discrete prime, Ramanujan, and Collatz layers;
- charged-fermion mass and Yukawa audits;
- flavor, neutrino, hadronic, gauge, Higgs, strong-CP, and cosmological relations;
- explicit retrospective/prospective separation;
- reproducible numerical and publication-readiness audits;
- retained negative results and falsification gates.

## Scientific status

This repository deliberately separates technical correctness from physical success.

| Component | Current status | Interpretation |
|---|---|---|
| Publication build | **PASS** | The v11.0 monograph compiles reproducibly and passes citation, reference, layout, metadata, font, and PDF-integrity gates. |
| \(\kappa=\ln 2/(24\pi)\) | **MODEL POSTULATE** | Structurally motivated within TIR; not claimed as an established first-principles theorem. |
| Accelerated Collatz quarter-power layer | **TECHNICAL PASS** | The specified residue-class audit yields the expected multiplier \(\rho_C=3/4\). |
| Isolated Collatz mass bridge | **OPEN / PHYSICAL FAIL** | The frozen v10.1 trace retains a geometric-mean multiplicative error of approximately \(9.967\times\). |
| Retrospective sector-holonomy trace | **RETROSPECTIVE** | Useful as a diagnostic construction, but not independent confirmation. |
| Common up-sector baseline | **RESTRICTED NO-GO** | A common additive baseline cannot remove the frozen residual spread for the tested architecture. |
| v10.7 candidate family | **PROSPECTIVE FROZEN** | Three candidates and their future observables are fixed in advance under a no-refit rule. |
| Gauge-boson relations | **OPEN TENSION** | The active relations remain approximately 4.5% and 5.0% high. |
| Higgs relation | **RETROSPECTIVE REVISION** | The former precision claim has been withdrawn. |
| Neutron electric dipole moment | **PHYSICAL FAIL** | The active prediction is \(5.3299\times10^{-26}\,e\,\mathrm{cm}\), about \(2.96\times\) above the manuscript bound. |
| Full physical closure | **NOT CLAIMED** | Open derivational debts and empirical tensions remain. |
| Canonical promotion | **DENIED** | The framework is not presented as an experimentally established replacement for the Standard Model. |

## Frozen prospective candidate family

The v10.7 family uses

\[
\ln y_{f,g}=F(S_f)+D(G_g,R_g),
\]

with the same functions acting across the charged-lepton, down-quark, and up-quark sectors.

Exactly three candidates are retained:

```text
C1: F(S) = -S
    D(G,R) = -G + R

C2: F(S) = -S^(3/4)
    D(G,R) = -G^(3/4) + R

C3: F(S) = S^(-3/4)/(L3*kappa)
    D(G,R) = G^(-3/4)/(L3*kappa) + R
```

The orthogonal prospective observables are:

- `y_c / y_mu`, isolating the sector functional;
- `y_c / y_t`, isolating the generation-release operator.

Frozen predictions:

| Candidate | `y_c / y_mu` | `y_c / y_t` |
|---|---:|---:|
| C1 | 4.850346751338371 | 0.16766796647328305 |
| C2 | 2.3521800134268784 | 0.17147213462587316 |
| C3 | 6.858021228826222 | 2.8101955040512466e-11 |

No fourth candidate may be introduced, and no candidate, observable, or formula may be replaced after inspecting the assigned future likelihood.

## Publication candidate v11.0

The v11.0 revision adds a publication-level claim hierarchy and corrects several earlier overstatements.

Principal changes include:

- replacement of the inaccurate “26 Standard Model parameters” label with a 36-observable scope statement;
- withdrawal of a single heterogeneous global percentage-error claim;
- explicit separation of anchors, retrospective assignments, upper-limit tests, scheme-dependent quantities, and prospective predictions;
- renormalization-scale and scheme caveats for quark masses, Yukawa couplings, gauge couplings, and \(\sin^2\theta_W\);
- corrected strong-CP and neutron-EDM arithmetic;
- explicit retention of physical failures;
- a data-provenance and statistical-interpretation protocol;
- expanded bibliography and complete local citation coverage;
- PDF metadata, embedded publication fonts, hidden links, and automated preflight checks.

The numerical tables should be read as a **frozen audit snapshot dated 29 July 2026**, not as a continuously updated global-fit database.

## Repository structure

```text
.
├── README.md
├── .github/
│   └── workflows/
│       └── compile-metatime-monograph.yml
├── TIR/
│   └── monograph/
│       ├── metatime_monograph.tex
│       ├── frontmatter/
│       │   └── publication_frontmatter_v11_0.tex
│       ├── chapters/
│       ├── appendices/
│       │   └── appO_publication_protocol.tex
│       ├── references_expanded_v10_8.tex
│       ├── PUBLICATION_READINESS_v11_0.md
│       ├── publication_readiness_v11_0.json
│       ├── CITATION_COVERAGE_v11_0.md
│       ├── citation_coverage_v11_0.json
│       ├── normalize_build_sources.py
│       ├── prepare_publication_candidate_v11_0.py
│       ├── prepare_publication_candidate_v11_0_impl.py
│       └── add_citation_context_v10_9.py
└── archive/
    └── historical releases and audit material
```

## Build the monograph

### Dependencies

The GitHub Actions build uses:

- `latexmk`;
- `lmodern`;
- `texlive-latex-base`;
- `texlive-latex-recommended`;
- `texlive-latex-extra`;
- `texlive-fonts-recommended`;
- `texlive-science`;
- `poppler-utils`;
- `qpdf`.

On Debian or Ubuntu:

```bash
sudo apt-get update
sudo apt-get install -y \
  latexmk \
  lmodern \
  texlive-latex-base \
  texlive-latex-recommended \
  texlive-latex-extra \
  texlive-fonts-recommended \
  texlive-science \
  poppler-utils \
  qpdf
```

### Reproduce the source integration and PDF

```bash
cd TIR/monograph

python3 normalize_build_sources.py
PYTHONDONTWRITEBYTECODE=1 python3 prepare_publication_candidate_v11_0.py
PYTHONDONTWRITEBYTECODE=1 python3 add_citation_context_v10_9.py

latexmk -pdf \
  -interaction=nonstopmode \
  -halt-on-error \
  -file-line-error \
  metatime_monograph.tex
```

The resulting file is:

```text
TIR/monograph/metatime_monograph.pdf
```

## Automated publication gates

The workflow checks:

- exact-head checkout provenance;
- deterministic and idempotent source preparation;
- complete local citation coverage;
- zero unresolved citations and references;
- zero multiply defined labels;
- zero overfull boxes;
- nonempty PDF title, author, subject, and keywords;
- embedded fonts and absence of Type 3 fonts;
- `qpdf` syntax and stream integrity;
- corrected strong-CP and neutron-EDM values;
- explicit preservation of the neutron-EDM physical FAIL;
- absence of generated Python bytecode artifacts;
- artifact upload with checksums and audit ledgers.

## Evidence and interpretation policy

When reading or extending this repository:

1. **Do not treat retrospective numerical agreement as prospective confirmation.**
2. **Do not combine heterogeneous observables into a single accuracy percentage without a justified likelihood.**
3. **Do not compare scale-dependent quantities at precision level without a common renormalization scale and scheme.**
4. **Do not remove or suppress failed predictions after observing the result.**
5. **Do not modify the frozen prospective family after inspecting future data.**
6. **Preserve Ramanujan continuity in the scaling programme.**
7. **Keep technical PASS and physical PASS/FAIL separate.**

## Citation

Until a DOI-backed release is deposited, cite the repository and the exact commit used:

```bibtex
@misc{Lipa2026Metatime,
  author       = {Adrian Lipa},
  title        = {Metatime: A Publication Candidate for an Exploratory
                  Low-Parameter Phenomenological Ansatz},
  year         = {2026},
  howpublished = {The Fundamental Theory of Informational Relations repository},
  url          = {https://github.com/AdrianLipa90/The-Fundamental-Theory-of-Informational-Relations},
  note         = {Version 11.0; cite the exact Git commit used}
}
```

## Author and contact

**Adrian Lipa**  
Independent Researcher  
Doncaster, United Kingdom

For scientific discussion, reproducibility reports, or collaboration proposals, use the repository's GitHub issue or discussion channels where available.

## Disclaimer

This repository contains an independent exploratory research programme. It does not claim peer-reviewed validation, experimental confirmation of a final theory, or replacement of the Standard Model. Numerical proximity alone is not treated as proof, and all stated failures and open derivational debts remain part of the public record.
