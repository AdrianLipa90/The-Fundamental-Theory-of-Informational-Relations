#!/usr/bin/env python3
"""Prepare the Metatime monograph v11.0 publication candidate.

The transformation is deterministic and idempotent. It corrects internal
numerical inconsistencies, replaces over-claims with explicit claim classes,
adds publication front matter and a data/statistics protocol, and writes a
machine-readable publication-readiness ledger.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from textwrap import dedent

ROOT = Path(__file__).resolve().parent


def write(rel: str, content: str) -> None:
    """
    Write normalized UTF-8 content to a path relative to the repository root.
    
    Parameters:
        rel (str): Relative path of the target file.
        content (str): Text to dedent and normalize before writing.
    """
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    normalized = dedent(content).lstrip("\n").rstrip() + "\n"
    if path.exists() and path.read_text(encoding="utf-8") == normalized:
        print(f"SKIP unchanged: {rel}")
        return
    path.write_text(normalized, encoding="utf-8")
    print(f"UPDATED: {rel}")


def patch_root() -> None:
    """
    Update the monograph root LaTeX file for the v11.0 publication candidate.
    
    The update is idempotent and preserves the file when all required content is already present.
    """
    path = ROOT / "metatime_monograph.tex"
    text = path.read_text(encoding="utf-8")
    original = text

    text = text.replace(
        "%% Complete derivations of all Standard Model parameters from\n"
        "%% the Metatime framework: κ = ln(2)/(24π), L₃=7, L₄=2, L₅=5",
        "%% Publication-candidate presentation of an exploratory low-parameter ansatz\n"
        "%% with explicit claim classes, data conventions, failures, and prospective gates",
    )
    text = re.sub(
        r"%% Version .*\n",
        "%% Version 11.0 - Publication Candidate\n",
        text,
        count=1,
    )

    if "\\usepackage{lmodern}" not in text:
        text = text.replace("\\usepackage[T1]{fontenc}\n", "\\usepackage[T1]{fontenc}\n\\usepackage{lmodern}\n", 1)

    text = re.sub(
        r"\\usepackage(?:\[[^\]]*\])?\{hyperref\}",
        dedent(r"""
        \usepackage[
          hidelinks,
          pdfpagelayout=TwoPageRight,
          pdftitle={Metatime: Publication Candidate of a Low-Parameter Phenomenological Ansatz},
          pdfauthor={Adrian Lipa},
          pdfsubject={Geometric-phase information structures and particle, flavor, hadronic, and cosmological observables},
          pdfkeywords={Metatime, TIR, geometric phase, information geometry, Standard Model phenomenology, Collatz, Ramanujan, falsifiability}
        ]{hyperref}
        """).strip(),
        text,
        count=1,
    )

    text = text.replace(
        "\\newtheorem{lemma}{Lemma}[chapter]\n",
        "\\newtheorem{lemma}{Lemma}[chapter]\n"
        "\\newcommand{\\claimstatus}[1]{\\par\\noindent\\textbf{Claim status: #1}\\par}\n"
        "\\newcommand{\\datasetstatus}[1]{\\par\\noindent\\textbf{Data status: #1}\\par}\n",
        1,
    )

    old_title = dedent(r"""
    \title{Metatime: A Low-Parameter Ansatz for Standard Model \\
           Parameters from Geometric Phase Information Theory}
    \author{Adrian Lipa}
    \date{Independent Researcher, Doncaster, UK\\\today}

    \maketitle

    \tableofcontents
    """).strip()
    new_title = dedent(r"""
    \title{Metatime: A Publication Candidate for an Exploratory\\
           Low-Parameter Phenomenological Ansatz}
    \author{Adrian Lipa}
    \date{Independent Researcher, Doncaster, UK\\Version 11.0 -- 29 July 2026}

    \maketitle
    \input{frontmatter/publication_frontmatter_v11_0}

    \tableofcontents
    """).strip()
    text = text.replace(old_title, new_title, 1)

    if "\\include{appendices/appO_publication_protocol}" not in text:
        text = text.replace(
            "\\include{appendices/appN_separable_candidate_family}\n",
            "\\include{appendices/appN_separable_candidate_family}\n"
            "\\include{appendices/appO_publication_protocol}\n",
            1,
        )

    if "\\raggedbottom" not in text:
        text = text.replace("\\begin{document}\n", "\\begin{document}\n\\raggedbottom\n", 1)

    if text != original:
        path.write_text(text, encoding="utf-8")
        print("UPDATED: metatime_monograph.tex")
    else:
        print("SKIP unchanged: metatime_monograph.tex")


def extend_bibliography() -> None:
    """
    Add model-selection and likelihood-method references to the expanded bibliography when they are absent.
    """
    path = ROOT / "references_expanded_v10_8.tex"
    text = path.read_text(encoding="utf-8")
    if "\\bibitem{Akaike1974}" in text:
        print("SKIP bibliography already extended for v11.0")
        return
    additions = dedent(r"""

    \item[]\textbf{K. Model selection, likelihoods, and reporting standards}

    \bibitem{Akaike1974}
    H.~Akaike,
    ``A new look at the statistical model identification,''
    IEEE Trans. Automat. Control \textbf{19}, 716--723 (1974).

    \bibitem{Schwarz1978}
    G.~Schwarz,
    ``Estimating the dimension of a model,''
    Ann. Stat. \textbf{6}, 461--464 (1978).

    \bibitem{Wilks1938}
    S.~S.~Wilks,
    ``The large-sample distribution of the likelihood ratio for testing composite
    hypotheses,'' Ann. Math. Stat. \textbf{9}, 60--62 (1938).

    \bibitem{Cowan2011}
    G.~Cowan, K.~Cranmer, E.~Gross, and O.~Vitells,
    ``Asymptotic formulae for likelihood-based tests of new physics,''
    Eur. Phys. J. C \textbf{71}, 1554 (2011).

    \bibitem{Humphreys1990}
    J.~E.~Humphreys,
    \emph{Reflection Groups and Coxeter Groups}
    (Cambridge University Press, Cambridge, 1990).
    """).rstrip()
    text = text.replace("\\end{thebibliography}", additions + "\n\n\\end{thebibliography}", 1)
    path.write_text(text, encoding="utf-8")
    print("UPDATED: references_expanded_v10_8.tex")


def patch_citation_audit() -> None:
    """
    Update the citation-audit helper for the v11.0 publication candidate.
    
    The update changes report paths and version metadata, adds citation context for the publication protocol when needed, and writes the helper only when its content changes.
    """
    path = ROOT / "add_citation_context_v10_9.py"
    text = path.read_text(encoding="utf-8")
    original = text
    text = text.replace(
        'REPORT_MD = ROOT / "CITATION_COVERAGE_v10_9.md"',
        'REPORT_MD = ROOT / "CITATION_COVERAGE_v11_0.md"',
    )
    text = text.replace(
        'REPORT_JSON = ROOT / "citation_coverage_v10_9.json"',
        'REPORT_JSON = ROOT / "citation_coverage_v11_0.json"',
    )
    if '"appendices/appO_publication_protocol.tex"' not in text:
        entry = (
            '    "appendices/appO_publication_protocol.tex": r"""\\paragraph{Established context.}\n'
            'Model comparison, likelihood inference, preregistration, and reproducible\n'
            'computation are grounded in the statistical and methodological literature\n'
            '\\cite{Akaike1974,Schwarz1978,Wilks1938,Cowan2011,Nosek2018,Sandve2013}.\n'
            'The protocol below applies those norms to interpretation of this monograph.""",\n'
        )
        text = text.replace('}\n\n\ndef bibliography_keys', entry + '}\n\n\ndef bibliography_keys', 1)
    text = text.replace(
        '"%% Version 10.9 - Citation-integrated monograph"',
        '"%% Version 11.0 - Publication Candidate"',
    )
    text = text.replace('"version": "v10.9"', '"version": "v11.0"')
    text = text.replace('# Citation Coverage Audit v10.9', '# Citation Coverage Audit v11.0')
    text = text.replace('| v10.9 context |', '| local context |')
    if text != original:
        path.write_text(text, encoding="utf-8")
        print("UPDATED: add_citation_context_v10_9.py for v11.0")
    else:
        print("SKIP citation audit already at v11.0")


def main() -> None:
    """
    Prepare the v11.0 publication-candidate source files and readiness artifacts.
    
    The process updates the monograph, bibliography, citation audit, publication
    content, and machine-readable readiness ledgers using deterministic, idempotent
    file operations.
    """
    patch_root()

    write("frontmatter/publication_frontmatter_v11_0.tex", r"""
    \chapter*{Abstract}
    \addcontentsline{toc}{chapter}{Abstract}

    This monograph presents Metatime/TIR as an exploratory, low-parameter
    phenomenological ansatz relating geometric-phase and information-theoretic
    structures to particle, flavor, hadronic, and cosmological observables.  The
    construction uses the defined information constant
    $\kappa=\ln 2/(24\pi)$, three discrete integers $(L_3,L_4,L_5)=(7,2,5)$,
    prime-valued flavor labels, and a small set of external physical anchors.
    The manuscript does not claim that these ingredients have been derived from
    an accepted microscopic theory.  Instead, it distinguishes established
    mathematics, model postulates, retrospective formula assignments, diagnostic
    no-go results, and prospectively frozen tests.

    The retrospective ledger contains close numerical matches in several sectors,
    but these matches are not combined into a single global accuracy score because
    the observables have different units, uncertainties, dependence structures,
    and degrees of post-selection.  Two failures are kept explicit: the quoted
    gauge-boson masses remain approximately $4.5$--$5.0\%$ high, and the fixed
    strong-CP-to-neutron-EDM mapping gives
    $d_n=5.33\times10^{-26}\,e\,\mathrm{cm}$, a factor $2.96$ above the current
    $90\%$ confidence upper bound used in this work.  The Collatz $3/4$ mass trace
    is also retained as an incomplete comparative signal rather than a closed mass
    derivation.  A restricted common-baseline repair is excluded by an explicit
    no-go theorem.  Three separable candidates are frozen for future direct
    Higgs-coupling likelihoods, with no candidate deletion or formula alteration
    permitted after inspection of the named data.

    The complete source, validation ledgers, and reproducible LaTeX build are
    available in the accompanying repository.

    \section*{Keywords}
    geometric phase; information geometry; phenomenological ansatz; flavor;
    Standard Model observables; Collatz dynamics; Ramanujan structure;
    preregistration; reproducibility.

    \section*{Claim and evidence taxonomy}
    \begin{description}
      \item[A -- established result:] a standard mathematical identity or external
      experimental result supported by the cited literature.
      \item[B -- model postulate:] a defining structural choice of Metatime/TIR.
      \item[C -- retrospective assignment:] a formula assessed after some or all of
      the comparison data were known.
      \item[D -- diagnostic or no-go:] an internal audit, failure, or restricted
      impossibility result.
      \item[E -- prospective prediction:] a frozen formula, observable, and decision
      rule specified before the named future dataset is inspected.
      \item[F -- external anchor:] a measured scale or coefficient supplied to the
      construction rather than predicted by it.
    \end{description}

    \section*{Availability and version status}
    This is Version 11.0, designated a \emph{Publication Candidate}.  It is suitable
    for circulation as a research monograph or preprint.  It is not presented as an
    experimentally established derivation of the Standard Model from first
    principles.  Source code, version history, machine-readable validation outputs,
    and the build workflow are maintained at
    \url{https://github.com/AdrianLipa90/The-Fundamental-Theory-of-Informational-Relations}.

    \section*{Declarations}
    This manuscript is an independent research work.  No external grant is
    identified in the repository record.  No competing interest is declared in
    this manuscript version.

    \cleardoublepage
    """)

    write("appendices/appO_publication_protocol.tex", r"""
    % !TEX root = ../metatime_monograph.tex
    \chapter{Publication Protocol, Data Provenance, and Statistical Interpretation}
    \label{app:publication_protocol}

    % CITATION_CONTEXT_V10_9_BEGIN
    \paragraph{Established context.}
    Model comparison, likelihood inference, preregistration, and reproducible
    computation are grounded in the statistical and methodological literature
    \cite{Akaike1974,Schwarz1978,Wilks1938,Cowan2011,Nosek2018,Sandve2013}.
    The protocol below applies those norms to interpretation of this monograph.
    % CITATION_CONTEXT_V10_9_END

    \claimstatus{Methodological protocol; it governs interpretation but is not a
    physical derivation.}

    \section{Purpose}
    This appendix fixes the publication-level interpretation of the numerical
    material in the monograph.  It prevents a close numerical match from being
    promoted to independent evidence when the corresponding formula was selected
    retrospectively, and it prevents quantities with incompatible statistical
    meanings from being merged into a single accuracy score.  The protocol follows
    standard concerns in model selection, likelihood inference, preregistration,
    and reproducible computation
    \cite{Akaike1974,Schwarz1978,Wilks1938,Cowan2011,Nosek2018,Sandve2013}.

    \section{Data snapshot and external inputs}
    The numerical comparison tables are a frozen audit snapshot dated 29 July 2026.
    Unless an entry explicitly states otherwise, a quoted reference value is the
    value used during development of the v10 series and is not asserted to be the
    latest global fit.  The principal external reference compilations are PDG,
    CODATA, and Planck \cite{PDG2024,CODATA2022,Planck2018}.

    External inputs include the Planck scale, the proton mass where used as a
    hadronic scale, $N_c=3$, the assigned lepton hypercharge, and the hadronic
    coefficient used to map $\theta_{\rm QCD}$ to the neutron EDM.  The electron is
    the sole dimensional anchor in the Collatz charged-fermion mass audit.  Results
    depending on an anchor are not independent predictions of that anchor.

    \section{Renormalization and scheme conventions}
    The current monograph does not derive renormalization-group running.  Therefore:
    \begin{enumerate}
      \item masses quoted for charged leptons, hadrons, and gauge bosons are compared
      with the reference mass conventions stated or implied by the cited source;
      \item $\sin^2\theta_W$, gauge couplings, quark masses, and Yukawa couplings are
      scheme- and scale-dependent and must not be compared at precision level unless
      the same scheme and scale are used;
      \item future ratios $y_c/y_\mu$ and $y_c/y_t$ must be taken from a common direct
      experimental likelihood or translated to a common scheme before testing the
      frozen candidates;
      \item no sub-percent claim is made for a cross-scheme comparison.
    \end{enumerate}

    \section{Residuals and aggregate summaries}
    For a positive observable $x$, the preferred scale-free residual is
    \[
      r=\ln\!\left(\frac{x_{\rm model}}{x_{\rm ref}}\right),
      \qquad
      f=\exp(|r|),
    \]
    where $f$ is the multiplicative error factor.  A normalized pull may be quoted
    only when a defensible model uncertainty and reference uncertainty are both
    available:
    \[
      z=\frac{x_{\rm model}-x_{\rm ref}}
      {\sqrt{\sigma_{\rm model}^2+\sigma_{\rm ref}^2}}.
    \]
    Circular variables such as phases require circular distance.  Upper limits such
    as the neutron EDM are pass/fail constraints and are excluded from mean-error
    calculations.  External anchors and values used to choose a formula are also
    excluded from prospective performance scores.

    The earlier statement of a mean error across ``26 SM parameters'' is withdrawn.
    The summary actually contains 36 heterogeneous observables and derived
    quantities, including hadron masses and cosmological quantities that are not
    independent parameters of the Standard Model Lagrangian.  Sector-level
    descriptive residuals may be reported, but no single global percentage is used
    as evidence.

    \section{Model complexity}
    ``Zero continuous fitted parameters'' does not mean zero model complexity.  The
    construction contains approximately fifty discrete structural choices,
    including integer assignments, prime labels, formula families, anchor choices,
    and sector mappings.  Interpretation must therefore account for discrete
    selection freedom and post-selection.  Information criteria such as AIC or BIC
    are not applied here because a complete likelihood and effective parameter count
    have not yet been defined; their absence is a declared limitation, not evidence
    in favor of the model.

    \section{Retrospective and prospective evidence}
    All numerical sector formulas developed with access to their target values are
    classified as retrospective assignments.  They may motivate structure but do
    not constitute independent confirmation.  The v10.7 candidate family is the
    principal prospective component because the three formulas, two orthogonal
    observables, post-29-July-2026 data gate, and no-refit rule are frozen in advance.
    Multiplicity-aware likelihood interpretation is mandatory.

    \section{Current physical failures}
    \begin{enumerate}
      \item The fixed gauge-boson relations overshoot the quoted $W$ and $Z$ masses
      by approximately $4.5\%$ and $5.0\%$.
      \item With $\kappa=\ln2/(24\pi)$ and exponent $14$, the strong-CP assignment
      gives $\theta_{\rm QCD}=2.2208\times10^{-10}$ and, with the fixed hadronic
      coefficient used here, $d_n=5.3299\times10^{-26}\,e\,\mathrm{cm}$.  This is a
      technical calculation PASS but a physical constraint FAIL against the
      $1.8\times10^{-26}\,e\,\mathrm{cm}$ bound used in the manuscript.
      \item The isolated Collatz $3/4$ mass trace has a geometric-mean multiplicative
      error of $9.967$ and is not a closed spectrum derivation.
    \end{enumerate}

    These failures are retained without hidden suppression factors, exponent changes,
    or candidate substitution.

    \section{Publication gate}
    A release is a publication candidate only if the build has no unresolved
    citations or references, no multiply defined labels, no overfull boxes, nonempty
    PDF metadata, embedded non-Type-3 fonts, a complete citation-coverage ledger, and
    a publication-readiness ledger recording the physical PASS/FAIL separation.
    """)

    write("appendices/appA_kappa_derivation.tex", r"""
    % !TEX root = ../metatime_monograph.tex
    \chapter{Definition and Structural Motivation of $\kappa=\ln2/(24\pi)$}
    \label{app:kappa}

    % CITATION_CONTEXT_V10_9_BEGIN
    \paragraph{Established context.}
    The informational and thermodynamic vocabulary surrounding $\ln2$ is grounded
    in Shannon, Landauer, Bennett, and modern information theory
    \cite{shannon1948,Landauer1961,Bennett1982,CoverThomas2006}.  Geometric-phase
    normalization is compared with Simon and Berry \cite{Simon1983,berry1984}.  The
    coefficient $\ln2/(24\pi)$ is a Metatime/TIR structural definition, not a
    standard invariant established by those sources.
    % CITATION_CONTEXT_V10_9_END

    \claimstatus{B -- model postulate with structural motivation.}

    \section{Established ingredients}
    A binary equiprobable choice has Shannon entropy $\ln2$ in natural units
    \cite{shannon1948}.  A cyclic quantum evolution may acquire a geometric phase
    determined by a connection and its holonomy \cite{Simon1983,berry1984}.  Pure
    states in a three-dimensional complex Hilbert space form $\mathbb{C}P^2$, not
    $\mathbb{C}P^3$; the normalization of any Fubini--Study or symplectic volume must
    be specified before assigning it a numerical value.

    \section{Metatime normalization postulate}
    The framework defines
    \[
      \boxed{\kappa\equiv\frac{\ln2}{24\pi}}
      =0.00919315000636\ldots .
    \]
    The denominator is motivated by the discrete normalization
    \[
      24\pi=2\,|A_4|\,\pi,
      \qquad |A_4|=12,
    \]
    combining a two-orientation factor, the order of the rotational tetrahedral
    group, and a reference phase scale $\pi$.  This is an ansatz internal to the
    framework.  It is not asserted to be the symplectic volume of
    $\mathbb{C}P^3$, a theorem about the Standard Model, or a Coxeter invariant of
    $A_4$.  Standard Coxeter-group terminology should not be conflated with the
    alternating group $A_4$ \cite{Humphreys1990}.

    \section{Mnemonic decompositions}
    Relations such as $24=8\times3$ may be used as mnemonics for gluon and color
    counts, but they are not independent derivations.  Likewise, appearances of the
    integer $24$ in modular forms or lattices do not establish a physical connection
    without an explicit map and theorem.

    \section{Parameter-counting statement}
    The numerical value of $\kappa$ is not obtained by a continuous fit.  It does,
    however, depend on discrete structural choices.  The appropriate publication
    claim is therefore ``no continuously fitted coefficient in the definition,''
    not ``derived uniquely from first principles.''  Its physical relevance must be
    tested by transfer to observables and by prospective predictions.
    """)

    write("chapters/ch01_introduction.tex", r"""
    % !TEX root = ../metatime_monograph.tex
    \chapter{Introduction}
    \label{ch:introduction}

    % CITATION_CONTEXT_V10_9_BEGIN
    \paragraph{Established context.}
    Conventional particle-physics reference values are taken principally from the
    Particle Data Group, while the information-theoretic and geometric-phase
    background begins with Shannon, Simon, Berry, and the geometry of quantum states
    \cite{PDG2024,shannon1948,Simon1983,berry1984,ProvostVallee1980}.  Criteria used
    to distinguish exploratory assignments from established results follow the
    falsifiability and reproducibility literature \cite{Popper1959,Munafo2017}.
    % CITATION_CONTEXT_V10_9_END

    \section{Motivation}
    The Standard Model contains measured masses, couplings, and mixing quantities
    whose numerical values are not fixed by the minimal Lagrangian.  The exact count
    depends on convention and on whether neutrino masses and phases are included;
    counts near 19 for the minimal model and near 26 with neutrino parameters are
    commonly quoted.  This motivates attempts to identify lower-dimensional
    structures behind the observed hierarchy.

    \section{Aim and scope}
    This monograph investigates whether a compact set of discrete
    information-geometric assignments can organize a broad collection of particle,
    flavor, hadronic, and cosmological observables.  It does not claim an accepted
    microscopic derivation of the Standard Model.  The appropriate status is an
    exploratory phenomenological ansatz with explicit internal audits and named
    prospective tests.

    The standard geometric background is the projective space of quantum rays,
    equipped with the Fubini--Study metric and Berry curvature
    \cite{ProvostVallee1980,Simon1983,berry1984}.  For a normalized state $|\psi\rangle$,
    the line element may be written
    \begin{equation}
      ds_{\rm FS}^2=\langle d\psi|d\psi\rangle
      -|\langle\psi|d\psi\rangle|^2.
      \label{eq:fubini_study}
    \end{equation}
    Metatime uses this established language as motivation; its discrete particle
    assignments are additional hypotheses.

    \section{Defining structural choices}
    The core model choices are
    \begin{equation}
      \kappa\equiv\frac{\ln2}{24\pi},
      \qquad (L_3,L_4,L_5)=(7,2,5),
      \label{eq:kappa_def}
    \end{equation}
    and the prime labels
    \begin{equation}
      (u,d,s,c,b,t)=(3,5,7,11,13,17).
      \label{eq:quark_primes_def}
    \end{equation}
    These are model postulates.  The factor $24\pi$ is a discrete normalization
    ansatz, not the standard symplectic volume of $\mathbb{C}P^3$; Appendix
    \ref{app:kappa} states the precise and limited claim.

    The construction also uses external physical anchors, including the Planck
    scale, the proton mass in hadronic sectors, $N_c=3$, assigned hypercharge data,
    and a hadronic coefficient in the neutron-EDM mapping.  The electron is the sole
    dimensional anchor in the Collatz charged-fermion audit.  Such anchored results
    are not independent predictions of the anchor itself.

    \section{Claim hierarchy}
    Every substantive result is to be read using the following hierarchy:
    \[
    \begin{array}{ll}
      \text{[A]} & \text{established mathematical or experimental result},\\
      \text{[B]} & \text{Metatime/TIR model postulate},\\
      \text{[C]} & \text{retrospective phenomenological assignment},\\
      \text{[D]} & \text{diagnostic, failure, or restricted no-go result},\\
      \text{[E]} & \text{prospectively frozen prediction},\\
      \text{[F]} & \text{external anchor or input}.
    \end{array}
    \]
    A numerical match in class [C] is descriptive and hypothesis-generating.  Only a
    class [E] result evaluated under its frozen rule can provide prospective support.

    \section{Current evidence balance}
    Several retrospective assignments reproduce their reference snapshot closely,
    but the manuscript deliberately retains material failures.  The quoted $W$ and
    $Z$ masses remain high by approximately $4.5\%$ and $5.0\%$.  The fixed
    strong-CP assignment maps to a neutron EDM above the current bound.  The isolated
    Collatz quarter-power mass trace is not a closed derivation, and a proposed
    common up-sector baseline is ruled out for the frozen trace.  Conversely, the
    v10.7 separable candidate family supplies two orthogonal prospective observables
    and an explicit no-refit rule.

    \section{Model complexity}
    The framework uses no continuously fitted coefficient in several defining
    relations, but it contains approximately fifty discrete structural choices.
    ``Zero continuous free parameters'' must therefore not be interpreted as zero
    effective model complexity.  Appendix \ref{app:publication_protocol} fixes the
    statistical and publication conventions.

    \section{Organization}
    Parts II--X develop the sector assignments; Part XI separates retrospective
    comparisons, failures, and future work.  Appendices J--N contain the Collatz
    audit, retrospective release, no-go theorem, identifiability result, and frozen
    candidate family.  Appendix \ref{app:publication_protocol} records data
    provenance, renormalization limitations, and the prospective evaluation rule.
    """)

    write("chapters/ch24_higgs_mass.tex", r"""
    % !TEX root = ../metatime_monograph.tex
    \chapter{Higgs Boson Mass}
    \label{ch:higgs_mass}

    % CITATION_CONTEXT_V10_9_BEGIN
    \paragraph{Established context.}
    The scalar mechanism is founded on the 1964 symmetry-breaking papers
    \cite{EnglertBrout1964,Higgs1964,GHK1964}, and the observed Higgs-like boson was
    reported by ATLAS and CMS \cite{ATLAS2012Higgs,CMS2012Higgs}.  The reference mass
    is taken from PDG \cite{PDG2024}; the discrete relation below is a Metatime
    assignment rather than part of the discovery analyses.
    % CITATION_CONTEXT_V10_9_END

    \claimstatus{C -- retrospective revised assignment.}

    \section{Revision history}
    An earlier tree-level quartic relation gave $M_H\approx6.3$~TeV and failed
    severely.  After that failure was known, the following replacement was proposed:
    \begin{equation}
      M_H=v\,\kappa\,(L_3^2+L_4+L_5).
      \label{eq:higgs_mass}
    \end{equation}
    Because the target mass was already known when the new functional form was
    adopted, the relation is retrospective and cannot be counted as an independent
    prediction.

    \section{Numerical evaluation}
    With the Metatime value $v=244.89$~GeV,
    \[
      M_H=244.89\times0.00919315\times56=126.07~\mathrm{GeV}.
    \]
    Relative to the reference $125.25\pm0.17$~GeV, the fractional offset is
    $+0.65\%$.  If the quoted experimental uncertainty alone is used, the central
    difference is approximately $4.8\sigma$; no model uncertainty has been derived,
    so the earlier statement that the value is within $2\sigma$ is withdrawn.

    Using $v=246.22$~GeV gives $126.76$~GeV, an offset of $+1.2\%$ and approximately
    $8.9\sigma$ relative to the same experimental uncertainty alone.

    \section{Interpretation}
    The combination $L_3^2+L_4+L_5=56$ is a model-motivated discrete assignment.
    Descriptions such as ``color-squared phase space'' are heuristic until an
    explicit field-theoretic map is supplied.  The relation remains useful as a
    compact retrospective pattern, but publication-level support requires an
    independently derived functional form or a prediction frozen before new data.
    """)

    write("chapters/ch25_strong_cp_angle.tex", r"""
    % !TEX root = ../metatime_monograph.tex
    \chapter{Strong CP Angle}
    \label{ch:strong_cp}

    % CITATION_CONTEXT_V10_9_BEGIN
    \paragraph{Established context.}
    The strong-CP problem is tied to nonperturbative gauge topology and the QCD
    vacuum, with standard discussions including 't Hooft, Peccei--Quinn, Weinberg,
    and Wilczek \cite{tHooft1976,PecceiQuinn1977,Weinberg1978Axion,Wilczek1978Axion}.
    Phenomenological EDM consequences are reviewed by Crewther and Pospelov--Ritz
    \cite{crewther1979,pospelov2005}; the value below is the distinct TIR proposal.
    % CITATION_CONTEXT_V10_9_END

    \claimstatus{B/C -- model assignment with a current physical constraint FAIL.}

    \section{Model assignment}
    The monograph assigns
    \begin{equation}
      \theta_{\rm QCD}=\kappa\left(\frac{L_4}{L_3}\right)^{14},
      \qquad 14=L_3+L_4+L_5.
      \label{eq:theta_qcd}
    \end{equation}
    The exponent and suppression rule are model postulates; they are not derived from
    QCD in this work.

    \section{Correct numerical evaluation}
    \[
    \left(\frac27\right)^{14}=2.4157243621\times10^{-8},
    \qquad
    \theta_{\rm QCD}=2.2208116435\times10^{-10}.
    \]
    The earlier value $7.57\times10^{-11}$ resulted from an arithmetic error in
    $(2/7)^{14}$ and is superseded.

    With the fixed coefficient used in this monograph,
    \[
      C=2.4\times10^{-16}\ e\,\mathrm{cm},
      \qquad
      d_n=\theta_{\rm QCD}C
      =5.3299\times10^{-26}\ e\,\mathrm{cm}.
    \]

    \section{Constraint status}
    The experimental result represented by Abel \emph{et al.} is
    $d_n=(0.0\pm1.1_{\rm stat}\pm0.2_{\rm sys})\times10^{-26}\,e\,\mathrm{cm}$,
    corresponding to the $90\%$ confidence upper bound
    $|d_n|<1.8\times10^{-26}\,e\,\mathrm{cm}$ used here
    \cite{Abel2020nEDM}.  The fixed model value is a factor
    \[
      \frac{5.3299}{1.8}=2.96
    \]
    above that bound.  Under the fixed coefficient and exponent, the calculation is
    a technical PASS and the physical constraint is a FAIL.

    Hadronic matching carries theory uncertainty, but no quantitative uncertainty
    model is supplied in this monograph.  A post-hoc exponent change or unidentified
    suppression factor is therefore not accepted as a repair.
    """)

    write("chapters/ch26_neutron_edm.tex", r"""
    % !TEX root = ../metatime_monograph.tex
    \chapter{Neutron Electric Dipole Moment: Constraint Audit}
    \label{ch:neutron_edm}

    % CITATION_CONTEXT_V10_9_BEGIN
    \paragraph{Established context.}
    The link between a QCD CP phase and the neutron electric dipole moment follows
    the chiral and effective-field-theory literature
    \cite{crewther1979,pospelov2005}.  The experimental constraint is represented by
    the modern neutron-EDM measurement \cite{Abel2020nEDM}.
    % CITATION_CONTEXT_V10_9_END

    \claimstatus{D -- falsification audit of the fixed strong-CP assignment.}

    \section{Fixed mapping}
    Using Chapter \ref{ch:strong_cp},
    \[
      \theta_{\rm QCD}=2.2208116435\times10^{-10},
      \qquad
      C=2.4\times10^{-16}\ e\,\mathrm{cm},
    \]
    and therefore
    \[
      \boxed{d_n^{\rm model}=5.3299\times10^{-26}\ e\,\mathrm{cm}}.
    \]

    \section{Experimental comparison}
    The bound used in this release is
    \[
      |d_n|<1.8\times10^{-26}\ e\,\mathrm{cm}\qquad(90\%\ \mathrm{CL}).
    \]
    The model value is $2.96$ times the bound.  The current fixed implementation
    therefore fails this constraint.  This result is not described as ``at the
    limit'' and is not deferred to a future experiment.

    \section{Allowed interpretation}
    The failure applies to the conjunction of the exponent $14$, the chosen
    $\kappa$, and the fixed coefficient $C$.  It does not by itself prove that every
    possible information-geometric strong-CP construction is excluded.  However,
    changing the exponent to $15$, adding a suppression factor, or selecting a new
    coefficient after seeing the bound would constitute a new model version and
    cannot be counted as confirmation of the frozen formula.

    \section{Relation to axion models}
    The minimal Metatime implementation contains no Peccei--Quinn axion.  Discovery
    of an axion would contradict the minimal claim that no additional strong-CP
    degree of freedom is required; it would not automatically falsify every other
    mathematical component of TIR.  Conversely, the absence of an axion is not
    positive evidence for the present nEDM formula.
    """)

    write("chapters/ch30_parameter_summary.tex", r"""
    % !TEX root = ../metatime_monograph.tex
    \chapter{Summary of Observables, Status, and Limitations}
    \label{ch:parameter_summary}

    % CITATION_CONTEXT_V10_9_BEGIN
    \paragraph{Established context.}
    The table preserves the reference snapshot used in the v10 development series,
    principally PDG, CODATA, Planck, and major Higgs and neutrino measurements
    \cite{PDG2024,CODATA2022,Planck2018,ATLAS2012Higgs,CMS2012Higgs,SuperK1998,SNO2002}.
    A close match is retrospective unless a formula and decision rule were frozen
    before inspection of the relevant data.
    % CITATION_CONTEXT_V10_9_END

    \datasetstatus{Frozen 29 July 2026 audit snapshot; not a claim that every entry
    is the latest global fit.}

    \section{Scope of the table}
    The table contains 36 heterogeneous observables and derived quantities.  They
    are not 36 independent parameters of the Standard Model Lagrangian: hadron
    masses, cosmological quantities, anchors, and upper limits have different
    theoretical and statistical meanings.  The earlier heading ``All 26 SM
    Parameters'' and the single mean-error claim are withdrawn.

    \begin{longtable}{p{0.29\textwidth}p{0.20\textwidth}p{0.20\textwidth}p{0.19\textwidth}}
    \toprule
    Observable & Model value & Reference snapshot & Publication status\\
    \midrule
    \endfirsthead
    \toprule
    Observable & Model value & Reference snapshot & Publication status\\
    \midrule
    \endhead
    $m_e$ (MeV) & 0.5107 & 0.5110 & retrospective\\
    $m_\mu$ (MeV) & 105.98 & 105.66 & retrospective\\
    $m_\tau$ (MeV) & 1781.5 & 1776.86 & retrospective\\
    \midrule
    $p/n$ (MeV) & 949.19 & 938.92 & anchor-linked retrospective\\
    $\Lambda$ (MeV) & 1115.72 & 1115.68 & retrospective\\
    $\Sigma$ (MeV) & 1193.18 & 1193.15 & retrospective\\
    $\Xi$ (MeV) & 1320.99 & 1318.29 & retrospective\\
    $\Delta$ (MeV) & 1227.18 & 1232.0 & retrospective\\
    $\Sigma^*$ (MeV) & 1378.13 & 1382.8 & retrospective\\
    $\Xi^*$ (MeV) & 1529.08 & 1531.8 & retrospective\\
    $\Omega$ (MeV) & 1680.03 & 1672.45 & retrospective\\
    \midrule
    $\pi$ (MeV) & 139.57 & 139.57 & retrospective\\
    $K$ (MeV) & 493.68 & 493.68 & retrospective\\
    $\eta$ (MeV) & 547.86 & 547.86 & retrospective\\
    $\eta'$ (MeV) & 957.78 & 957.78 & retrospective\\
    \midrule
    $\sin^2\theta_{12}$ & 0.304 & 0.307 & retrospective\\
    $\sin^2\theta_{23}$ & 0.541 & 0.545 & retrospective\\
    $\sin\theta_{13}$ & 0.143 & 0.148 & retrospective\\
    $\delta_{\rm CP}^{\rm PMNS}$ & $246.1^\circ$ & $244^\circ$ & retrospective\\
    $\Delta m_{21}^2$ (eV$^2$) & $7.50\times10^{-5}$ & $7.53\times10^{-5}$ & retrospective\\
    $\Delta m_{31}^2$ (eV$^2$) & $2.48\times10^{-3}$ & $2.45\times10^{-3}$ & retrospective\\
    \midrule
    $\lambda_{\rm CKM}$ & 0.22485 & 0.22500 & retrospective\\
    $|V_{cb}|$ & 0.04082 & 0.04182 & retrospective tension\\
    $|V_{ub}|$ & 0.00363 & 0.00369 & retrospective\\
    $J_{\rm CP}$ & $3.11\times10^{-5}$ & $3.08\times10^{-5}$ & retrospective\\
    $\delta_{\rm CP}^{\rm CKM}$ & $66.42^\circ$ & $65.6^\circ$ & retrospective revision\\
    \midrule
    $v$ (GeV) & 244.89 & 246.22 & retrospective\\
    $\sin^2\theta_W$ & 0.23142 & 0.23122 & scheme-sensitive\\
    $1/\alpha$ & 137.037 & 137.036 & retrospective\\
    $M_W$ (GeV) & 83.96 & 80.38 & physical tension\\
    $M_Z$ (GeV) & 95.77 & 91.19 & physical tension\\
    $M_H$ (GeV) & 126.07 & $125.25\pm0.17$ & retrospective revision\\
    \midrule
    $\theta_{\rm QCD}$ & $2.2208\times10^{-10}$ & constrained indirectly & model assignment\\
    $d_n$ ($e\,\mathrm{cm}$) & $5.3299\times10^{-26}$ & $<1.8\times10^{-26}$ & \textbf{FAIL}\\
    \midrule
    $\Omega_\Lambda$ & 0.685 & 0.685 & retrospective\\
    $\rho_\Lambda$ (GeV$^4$) & $3.3\times10^{-47}$ & $3.2\times10^{-47}$ & retrospective\\
    \bottomrule
    \end{longtable}

    \section{Assessment}
    No global mean percentage is reported.  Percent differences, circular phase
    residuals, likelihood pulls, anchors, and upper limits cannot be combined without
    a joint statistical model.  Sector-level comparisons remain descriptive.  The
    present publication-level conclusions are:
    \begin{enumerate}
      \item several compact retrospective assignments reproduce their frozen
      reference snapshot closely;
      \item the gauge-boson relations remain visibly inaccurate;
      \item the Higgs replacement is retrospective and differs from the quoted
      experimental central value by about $4.8\sigma$ if only experimental
      uncertainty is used;
      \item the neutron-EDM implementation fails the stated bound by a factor $2.96$;
      \item prospective evidential weight is reserved for the frozen v10.7
      candidate-family tests.
    \end{enumerate}
    """)

    write("chapters/ch31_open_problems.tex", r"""
    % !TEX root = ../metatime_monograph.tex
    \chapter{Open Problems and Falsification Ledger}
    \label{ch:open_problems}

    % CITATION_CONTEXT_V10_9_BEGIN
    \paragraph{Established context.}
    The ledger follows falsifiability, preregistration, and reproducible
    computational practice \cite{Popper1959,Lakatos1978,Sandve2013,Wilson2014,Munafo2017,Nosek2018,Stark2018}.
    Prospective Higgs-coupling gates are anchored to direct experimental searches
    and reference data \cite{ATLAS2022Charm,PDG2024}.  A failed frozen test is
    retained rather than repaired post hoc.
    % CITATION_CONTEXT_V10_9_END

    \section{Current physical status}
    \begin{description}
      \item[Gauge bosons -- OPEN TENSION.] The frozen relations overshoot the quoted
      $W$ and $Z$ masses by approximately $4.5\%$ and $5.0\%$.  No
      renormalization-group derivation is presently supplied.

      \item[Higgs mass -- RETROSPECTIVE REVISION.] The earlier $6.3$~TeV formula
      failed.  The replacement $M_H=v\kappa(L_3^2+L_4+L_5)$ was adopted after the
      target value was known.  Its small percentage offset is not prospective
      evidence, and the statement ``within $2\sigma$'' has been withdrawn.

      \item[Neutron EDM -- PHYSICAL FAIL.] Correct arithmetic gives
      $\theta_{\rm QCD}=2.2208\times10^{-10}$ and
      $d_n=5.3299\times10^{-26}\,e\,\mathrm{cm}$, a factor $2.96$ above the bound
      used in the manuscript.  The former value $1.82\times10^{-26}$ is superseded.

      \item[Collatz quarter-power bridge -- OPEN.] The $3/4$ exponent beats the
      declared fixed comparators but leaves a geometric-mean multiplicative error
      $9.967$ and is not a closed charged-fermion spectrum.

      \item[Common up-sector baseline -- RESTRICTED NO-GO.] A common additive shift
      cannot repair the frozen v10.2 up-sector residuals; the unavoidable worst
      multiplicative error is at least $4.7207104$.

      \item[Separable candidate family -- PROSPECTIVE.] Exactly three candidates and
      the orthogonal ratios $y_c/y_\mu$ and $y_c/y_t$ remain frozen for the first
      qualifying direct post-29-July-2026 likelihoods.  No fourth candidate, refit,
      or observable substitution is allowed.
    \end{description}

    \section{Methodological debts}
    \begin{enumerate}
      \item construct a common likelihood with uncertainties and covariance rather
      than a table of heterogeneous percentage errors;
      \item define an effective complexity penalty for the approximately fifty
      discrete structural choices;
      \item specify mass, coupling, and weak-mixing-angle renormalization schemes and
      scales before precision comparison;
      \item derive, rather than retrospectively select, the functional forms used in
      the Higgs, electroweak, and flavor sectors;
      \item preserve all failed formulae and superseded arithmetic in the version
      history.
    \end{enumerate}

    \section{Prospective program}
    \begin{enumerate}
      \item evaluate the three frozen v10.7 candidates on the named direct
      charm--muon and charm--top Higgs-coupling likelihoods using a
      multiplicity-aware rule;
      \item derive receiver-independent or externally reproducible tests for any
      additional TIR/NOEMA claims before using them as physical evidence;
      \item produce an RG-consistent electroweak comparison with matched schemes;
      \item preregister any new mass formula before comparing it with the target
      spectrum;
      \item treat the current neutron-EDM formula as failed unless a new version
      supplies an independently motivated uncertainty model or replacement before
      inspecting a new result.
    \end{enumerate}

    \vfill
    \noindent\small\textit{Repository:}
    \url{https://github.com/AdrianLipa90/The-Fundamental-Theory-of-Informational-Relations}
    """)

    extend_bibliography()
    patch_citation_audit()

    ledger = {
        "version": "11.0",
        "status": "PUBLICATION_CANDIDATE_PENDING_CI",
        "date": "2026-07-29",
        "required_files": [
            "frontmatter/publication_frontmatter_v11_0.tex",
            "appendices/appO_publication_protocol.tex",
            "PUBLICATION_READINESS_v11_0.md",
            "publication_readiness_v11_0.json",
        ],
        "corrected_inconsistencies": {
            "summary_count": {"old": 26, "actual": 36},
            "theta_qcd": {"old": 7.57e-11, "corrected": 2.2208116434538389e-10},
            "neutron_edm_e_cm": {"old": 1.82e-26, "corrected": 5.329947944289213e-26},
            "neutron_edm_bound_ratio": 2.961082191271785,
            "higgs_sigma_using_experimental_uncertainty_only": 4.823529411764707,
        },
        "physical_status": {
            "gauge_boson_masses": "OPEN_TENSION",
            "higgs_relation": "RETROSPECTIVE_REVISION",
            "neutron_edm": "FAIL",
            "collatz_quarter_power_mass_bridge": "OPEN_NOT_CLOSED",
            "common_up_sector_baseline": "RESTRICTED_NO_GO",
            "v10_7_candidate_family": "PROSPECTIVE_FROZEN",
        },
        "canonical_promotion": False,
    }
    write("publication_readiness_v11_0.json", json.dumps(ledger, indent=2, sort_keys=True))

    write("PUBLICATION_READINESS_v11_0.md", r"""
    # Publication Readiness Ledger v11.0

    Status before CI: `PUBLICATION_CANDIDATE_PENDING_CI`

    ## Corrections applied

    - Replaced the false heading "All 26 SM Parameters" with a 36-observable scope statement.
    - Withdrew the global 1.1% mean as statistically heterogeneous and post-selection sensitive.
    - Corrected `(2/7)^14` and the derived strong-CP value.
    - Corrected the neutron-EDM output to `5.3299e-26 e cm` and recorded a physical FAIL against the manuscript's `1.8e-26 e cm` bound.
    - Reclassified the revised Higgs formula as retrospective and withdrew the incorrect "within 2 sigma" statement.
    - Reframed `kappa = ln(2)/(24 pi)` as a model postulate with structural motivation, not a standard CP3 volume or first-principles theorem.
    - Added a renormalization, data-provenance, model-complexity, and statistical-interpretation protocol.
    - Added abstract, keywords, availability statement, claim taxonomy, PDF metadata, hidden link styling, and publication font preflight.

    ## Physical status

    - Gauge-boson relations: `OPEN_TENSION`
    - Higgs relation: `RETROSPECTIVE_REVISION`
    - Neutron EDM: `FAIL`
    - Collatz quarter-power mass bridge: `OPEN_NOT_CLOSED`
    - Common up-sector baseline: `RESTRICTED_NO_GO`
    - v10.7 candidate family: `PROSPECTIVE_FROZEN`
    - Canonical promotion: `DENIED`

    ## CI publication gates

    CI must confirm:

    - successful exact-head checkout and deterministic source integration;
    - zero unresolved citations and references;
    - zero multiply defined labels;
    - zero overfull boxes;
    - nonempty PDF title, author, subject, and keywords;
    - all fonts embedded and no Type 3 fonts;
    - citation coverage complete;
    - corrected neutron-EDM values present and superseded values absent from active monograph sources;
    - final PDF, checksum, preflight, and ledgers uploaded.
    """)


if __name__ == "__main__":
    main()
