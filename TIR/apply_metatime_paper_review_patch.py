#!/usr/bin/env python3
"""Idempotently synchronize the live short Metatime/TIR paper with current κ provenance."""
from __future__ import annotations

import re
from pathlib import Path
from textwrap import dedent

PAPER = Path(__file__).with_name("metatime_paper.tex")

ABSTRACT = dedent(r"""
\begin{abstract}
Metatime/TIR is presented as a relational and information-geometric research
programme linking binary information, quantum-state geometry, flavour mixing,
and particle-sector observables. The information normalization
$\kappa=\ln2/(24\pi)$ is carried by an explicit internal dependency: the
balanced binary relation supplies $H_2(1/2)=\ln2$; the three-flavour carrier
$V_F\cong\mathbb C^3$ has mixing algebra
$\dim\mathfrak{su}(3)_F=3^2-1=8$; eight mixing directions across three flavours
give $N_{\rm mix}=24$; and the primitive half-turn contributes the angular unit
$\pi$. Hence the mixing-phase measure is $24\pi$ and
$\kappa=\ln2/[3(3^2-1)\pi]$.

With angular rate $\omega=2\pi f$ and the TIR information-phase law
$d\mathcal I=\kappa\,d\phi$, the exact consequence is
$\Gamma_{\mathcal I}=\kappa\omega=(\ln2/12)f$. Sector formulae, diagnostics,
empirical residuals, and prospective predictions retain their individual
evidence classes and validation receipts.
\end{abstract}
""").strip()

INTRO_BRIDGE = dedent(r"""
The Metatime/TIR framework organizes these quantities around the derived
information normalization $\kappa=\ln2/(24\pi)$ and a set of separately tracked
sector structures. The normalization is derived in Sec.~\ref{sec:constants}
from the three-flavour $SU(3)_F$ mixing carrier and the primitive half-turn phase;
its exact phase-rate consequence is Eq.~\eqref{eq:kappa_phase_rate_paper}.
""").strip()

INFO_SECTION = dedent(r"""
\subsection{The information constant $\kappa$}

The balanced binary relation supplies
\begin{equation}
I_\star=H_2(1/2)=\ln2.
\end{equation}
The TIR family carrier is three-flavour,
\begin{equation}
V_F\cong\mathbb C^3,
\qquad U_F\in SU(3)_F,
\end{equation}
and therefore
\begin{equation}
\dim_{\mathbb R}\mathfrak{su}(3)_F=3^2-1=8.
\end{equation}
The generator--flavour incidence count is
\begin{equation}
N_{\rm mix}=3\cdot8=24.
\end{equation}
The primitive half coordinate gives the half-turn angular unit
\begin{equation}
\Delta\phi_{1/2}=\frac12(2\pi)=\pi,
\end{equation}
so the total mixing-phase measure is
\begin{equation}
\Phi_{\rm mix}=N_{\rm mix}\Delta\phi_{1/2}=24\pi.
\end{equation}
The information normalization follows as
\begin{equation}
\boxed{
\kappa
=\frac{I_\star}{\Phi_{\rm mix}}
=\frac{\ln2}{3(3^2-1)\pi}
=\frac{\ln2}{24\pi}
}
\approx9.19315\times10^{-3}.
\label{eq:oi}
\end{equation}
The same integer has an independent spatial crosscheck through the regular
$3$-simplex automorphism group $\operatorname{Aut}(\Delta^3)\cong S_4$, whose
order is $24$.

For a spin-$1/2$ state the standard Berry relation is
$\gamma=-\Omega/2$ modulo $2\pi$. A hemisphere gives phase magnitude $\pi$ and
a full sphere gives $2\pi$; the half-turn $\pi$ used above is fixed directly by
the primitive half coordinate applied to the full angular closure.

If $\phi$ is an angular phase coordinate,
\begin{equation}
\omega\equiv\frac{d\phi}{dt}=2\pi f,
\end{equation}
and
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
One complete angular cycle carries
$\Delta\mathcal I_{\rm cycle}=\ln2/12$.
""").strip()


def replace_once(text: str, pattern: str, replacement: str, label: str) -> str:
    updated, count = re.subn(pattern, lambda _m: replacement, text, count=1, flags=re.S)
    if count != 1:
        raise SystemExit(f"{label}: expected exactly one match, found {count}")
    return updated


def patch_introduction(text: str) -> str:
    start = "The Metatime framework organizes these quantities around"
    stop = "The paper is organized as follows."
    if start in text and stop in text:
        start_i = text.index(start)
        stop_i = text.index(stop, start_i)
        return text[:start_i] + INTRO_BRIDGE + "\n\n" + text[stop_i:]
    return text


def normalize_literal_newlines(text: str) -> str:
    slash_n = chr(92) + "n"
    known = {
        "structural" + slash_n + "normalization": "structural\nnormalization",
        "the" + slash_n + "publication-candidate": "the\npublication-candidate",
        "independent" + slash_n + "predictions": "independent\npredictions",
    }
    for broken, repaired in known.items():
        text = text.replace(broken, repaired)
    return text


def assert_single_labels(text: str) -> None:
    for label in ("eq:oi", "eq:kappa_phase_rate_paper"):
        count = text.count(f"\\label{{{label}}}")
        if count != 1:
            raise SystemExit(f"{label}: expected one label after patch, found {count}")


def main() -> None:
    text = normalize_literal_newlines(PAPER.read_text(encoding="utf-8"))

    text = replace_once(
        text,
        r"\\begin\{abstract\}.*?\\end\{abstract\}",
        ABSTRACT,
        "abstract",
    )

    text = replace_once(
        text,
        r"\\subsection\{The information constant \$\\kappa\$\}.*?(?=\\subsection\{The L-constants\})",
        INFO_SECTION + "\n\n",
        "information constant section",
    )

    text = patch_introduction(text)

    # Remove any surviving duplicate historical eq:oi block outside the canonical
    # constants section by retaining exactly the first canonical label occurrence.
    if text.count(r"\label{eq:oi}") > 1:
        first = text.index(r"\label{eq:oi}")
        tail = text[first + len(r"\label{eq:oi}"):].replace(r"\label{eq:oi}", "", 1)
        text = text[:first + len(r"\label{eq:oi}")] + tail

    assert_single_labels(text)
    PAPER.write_text(text, encoding="utf-8")
    print("UPDATED: TIR/metatime_paper.tex with flavour-mixing κ provenance")


if __name__ == "__main__":
    main()
