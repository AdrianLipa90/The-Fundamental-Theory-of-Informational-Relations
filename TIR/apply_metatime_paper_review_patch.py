#!/usr/bin/env python3
"""Idempotent review patch for the live short Metatime paper.

The long publication-candidate monograph has a stricter claim taxonomy than the
older REVTeX paper.  This patch synchronizes the paper's front matter and κ
section with the reviewed 2026-08-07 state without touching archived copies.
It also repairs two representation defects found during review: literal ``\\n``
text inserted by an earlier patch and a duplicate ``eq:oi`` label in the
introduction.
"""
from __future__ import annotations

import re
from pathlib import Path
from textwrap import dedent

PAPER = Path(__file__).with_name("metatime_paper.tex")

ABSTRACT = dedent(r"""
\begin{abstract}
Metatime/TIR is presented here as an exploratory low-parameter arithmetic and
phase-geometry ansatz for patterns across particle, flavour, hadronic, and
cosmological observables.  Its structural normalization is
$\kappa=\ln2/(24\pi)$ together with discrete constants
$(L_3,L_4,L_5)=(7,2,5)$ and prime-valued flavour labels.  The coefficient
$\kappa$ is a TIR model definition with structural motivation; it is not claimed
to be independently derived by standard quantum mechanics or the Standard
Model.  With angular phase rate $\omega=2\pi f$ and the TIR definition
$d\mathcal I=\kappa\,d\phi$, the information-rate identity
$\Gamma_{\mathcal I}=\kappa\omega=(\ln2/12)f$ follows exactly and carries no
additional continuous coefficient.

The numerical sector relations remain heterogeneous in evidential status:
several are retrospective assignments or anchored constructions, while named
future tests are treated separately as prospective.  The publication record
retains material failures rather than absorbing them into a global accuracy
score.  In particular, the fixed gauge-boson relations remain approximately
$4.5\%$--$5.0\%$ high, and the frozen strong-CP-to-neutron-EDM mapping used in
the current audit gives $d_n\simeq5.33\times10^{-26}\,e\,\mathrm{cm}$, about
$2.96$ times the $1.8\times10^{-26}\,e\,\mathrm{cm}$ bound used by the
publication snapshot.  The framework is therefore reported as a falsifiable
phenomenological programme, not as an experimentally established derivation of
all Standard Model parameters from first principles.
\end{abstract}
""").strip()

INTRO_BRIDGE = dedent(r"""
The Metatime framework organizes these quantities around a declared structural
normalization and a small set of discrete assignments.  The normalization
$\kappa=\ln2/(24\pi)$ is defined and audited in
Sec.~\ref{sec:constants}; its exact phase-rate consequence is given in
Eq.~\eqref{eq:kappa_phase_rate_paper}.  The remaining constants and flavour
labels are model assignments whose evidential status is evaluated sector by
sector rather than inferred from the normalization alone.
""").strip()

INFO_SECTION = dedent(r"""
\subsection{The information constant $\kappa$}

TIR defines
\begin{equation}
\kappa \equiv \frac{\ln 2}{24\pi}
\approx 9.19315 \times 10^{-3}.
\label{eq:oi}
\end{equation}
The numerator $\ln2$ is the Shannon entropy of a binary equiprobable choice.
The denominator is a TIR discrete normalization
$24\pi=2|A_4|\pi$, with $|A_4|=12$, combining an orientation factor, the
rotational tetrahedral group order, and a reference spinorial/geometric phase
scale $\pi$.  This is a model postulate with structural motivation, not a
standard invariant derived from the cited ingredients.

For a spin-$1/2$ state, the standard Berry phase is
$\gamma=-\Omega/2$ modulo $2\pi$, where $\Omega$ is the enclosed Bloch-sphere
solid angle.  Thus a hemisphere ($|\Omega|=2\pi$) yields phase magnitude $\pi$,
whereas a full-sphere solid angle $4\pi$ yields magnitude $2\pi$, trivial modulo
$2\pi$.  The reference $\pi$ in the TIR normalization must therefore not be
justified by claiming that a full-sphere cycle produces Berry phase $\pi$.

If $\phi$ is an angular phase coordinate,
\begin{equation}
\omega\equiv\frac{d\phi}{dt}=2\pi f,
\end{equation}
and TIR defines informational accumulation per unit phase by
\begin{equation}
d\mathcal I\equiv\kappa\,d\phi,
\end{equation}
then
\begin{equation}
\boxed{
\Gamma_{\mathcal I}
\equiv\frac{d\mathcal I}{dt}
=\kappa\omega
=\frac{\ln2}{12}f
}.
\label{eq:kappa_phase_rate_paper}
\end{equation}
One complete phase cycle consequently carries
$\Delta\mathcal I_{\rm cycle}=\ln2/12$.  Conditional on these definitions, the
four quantities $(\kappa,\omega,f,\Gamma_{\mathcal I})$ obey three independent
constraints and hence form a one-dimensional regular constraint manifold,
parametrized by $f$.  A physical interpretation of
$\Gamma_{\mathcal I}$ as a surface-refresh observable remains an additional,
operationally open hypothesis.
""").strip()

EXTERNAL_SCALES_TAIL = dedent(r"""
Additional external anchors and conversion inputs are declared explicitly in
the publication-candidate monograph; results depending on them are not
independent predictions of those anchors.
""").strip()


def replace_once(text: str, pattern: str, replacement: str, label: str) -> str:
    updated, count = re.subn(pattern, lambda _m: replacement, text, count=1, flags=re.S)
    if count != 1:
        raise SystemExit(f"{label}: expected exactly one match, found {count}")
    return updated


def normalize_literal_newlines(text: str) -> str:
    """Repair only known prose-level literal backslash-n artifacts."""
    slash_n = chr(92) + "n"
    known = {
        "structural" + slash_n + "normalization": "structural\nnormalization",
        "the" + slash_n + "publication-candidate": "the\npublication-candidate",
        "independent" + slash_n + "predictions": "independent\npredictions",
    }
    for broken, repaired in known.items():
        text = text.replace(broken, repaired)
    return text


def patch_introduction(text: str) -> str:
    """Replace the old κ mini-derivation in the introduction by one cross-link.

    This removes the second ``eq:oi`` definition and makes the constants section
    the single source of the κ equation in the short paper.
    """
    start = "The Metatime framework organizes these quantities around"
    stop = "The paper is organized as follows."
    if start not in text:
        return text
    start_i = text.index(start)
    stop_i = text.index(stop, start_i)
    return text[:start_i] + INTRO_BRIDGE + "\n\n" + text[stop_i:]


def assert_single_labels(text: str) -> None:
    for label in ("eq:oi", "eq:kappa_phase_rate_paper"):
        count = text.count(f"\\label{{{label}}}")
        if count != 1:
            raise SystemExit(f"{label}: expected one label after patch, found {count}")


def main() -> None:
    text = PAPER.read_text(encoding="utf-8")
    original = text

    text = normalize_literal_newlines(text)

    if "current audit gives $d_n\\simeq5.33" not in text:
        text = replace_once(
            text,
            r"\\begin\{abstract\}.*?\\end\{abstract\}",
            ABSTRACT,
            "abstract",
        )

    if "\\label{eq:kappa_phase_rate_paper}" not in text:
        text = replace_once(
            text,
            r"\\subsection\{The information constant \$\\kappa\$\}.*?(?=\\subsection\{The L-constants\})",
            INFO_SECTION + "\n\n",
            "information constant section",
        )

    text = patch_introduction(text)

    literal_old = "No other experimental" + chr(92) + "ndata are used."
    text = text.replace(literal_old, EXTERNAL_SCALES_TAIL)
    text = text.replace("No other experimental data are used.", EXTERNAL_SCALES_TAIL)

    text = text.replace(
        "eliminating all continuous free parameters.",
        "eliminating those particular continuous baryon scales while leaving the "
        "model's discrete structural complexity explicit.",
    )

    # Remove the strongest stale κ-origin sentence if it survives an older source
    # layout not caught by patch_introduction().
    text = text.replace(
        "The Metatime framework proposes that all of these parameters arise from a\n"
        "single information-theoretic constant---the Berry phase accumulated by a\n"
        "quantum system on the Poincar\\'{e} disk:",
        INTRO_BRIDGE,
    )

    assert_single_labels(text)

    if text != original:
        PAPER.write_text(text, encoding="utf-8")
        print("UPDATED: TIR/metatime_paper.tex")
    else:
        print("SKIP: TIR/metatime_paper.tex already carries review patch")


if __name__ == "__main__":
    main()
