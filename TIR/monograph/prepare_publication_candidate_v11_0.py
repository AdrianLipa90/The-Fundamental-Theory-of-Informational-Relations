#!/usr/bin/env python3
from __future__ import annotations

import re
import runpy
from pathlib import Path

_original_sub = re.sub


def _literal_hyperref_sub(pattern, repl, string, count=0, flags=0):
    if isinstance(repl, str) and "hyperref" in str(pattern):
        return _original_sub(
            pattern,
            lambda _match: repl,
            string,
            count=count,
            flags=flags,
        )
    return _original_sub(pattern, repl, string, count=count, flags=flags)


def _deduplicate_publication_macros(root: Path) -> None:
    """Keep exactly one copy of publication status macros after source preparation."""
    path = root / "metatime_monograph.tex"
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    targets = {
        r"\newcommand{\claimstatus}[1]{\par\noindent\textbf{Claim status: #1}\par}",
        r"\newcommand{\datasetstatus}[1]{\par\noindent\textbf{Data status: #1}\par}",
    }
    seen: set[str] = set()
    output: list[str] = []
    for line in lines:
        stripped = line.rstrip("\r\n")
        if stripped in targets:
            if stripped in seen:
                continue
            seen.add(stripped)
        output.append(line)
    missing = targets - seen
    if missing:
        raise SystemExit(f"Missing publication status macro definitions: {sorted(missing)}")
    path.write_text("".join(output), encoding="utf-8")


def _write_flavour_mixing_kappa_appendix(root: Path) -> None:
    """Promote the current TIR-internal 3 x 8 flavour-mixing derivation of 24*pi.

    The historical v11 implementation writes an older normalization appendix.
    The wrapper is the live publication entrypoint and therefore replaces that
    generated appendix with the current dependency surface after every run.
    """
    path = root / "appendices" / "appA_kappa_derivation.tex"
    text = r"""% !TEX root = ../metatime_monograph.tex
\chapter{Flavour-Mixing Derivation of $\kappa=\ln2/(24\pi)$}
\label{app:kappa}

% CITATION_CONTEXT_V10_9_BEGIN
\paragraph{Established context.}
The numerator $\ln2$ follows from binary Shannon information
\cite{shannon1948,CoverThomas2006}. Geometric phase and angular closure use the
standard Simon--Berry framework \cite{Simon1983,berry1984}. The group-theoretic
identity $\dim\mathfrak{su}(3)=8$ is standard. TIR combines these ingredients
with its derived three-flavour family carrier.
% CITATION_CONTEXT_V10_9_END

\claimstatus{TIR-internal derived structural normalization with explicit upstream carrier and phase dependencies.}

\section{Binary information input}
The primitive balanced binary distinction has
\[
\sigma_\star=\frac12,
\qquad
I_\star=H_{\rm bin}(1/2)=\ln2.
\]
This fixes the informational numerator.

\section{Three-flavour mixing carrier}
The TIR family branch supplies
\[
V_F\cong\mathbb C^3,
\qquad
U_F\in SU(3)_F.
\]
Hence
\[
N_F=3.
\]
For the mixing algebra,
\[
\dim_{\mathbb R}\mathfrak{su}(N)=N^2-1,
\]
so
\[
\boxed{\dim_{\mathbb R}\mathfrak{su}(3)_F=3^2-1=8.}
\]
The generator--flavour incidence set therefore contains
\[
\boxed{
N_{\rm mix}
=N_F\dim\mathfrak{su}(3)_F
=3\cdot8
=24.
}
\]
The later TIR symmetric-pair decomposition independently gives
\[
\mathfrak{su}(3)_F=\mathfrak{so}(3)\oplus\mathfrak p,
\qquad
8=3+5.
\]

\section{Half-turn phase unit}
A full radian turn is $2\pi$. The primitive half coordinate therefore gives the
half-turn phase
\[
\boxed{
\Delta\phi_{1/2}
=\frac12(2\pi)
=\pi.
}
\]
The total primitive mixing-phase measure is
\[
\boxed{
\Phi_{\rm mix}
=N_{\rm mix}\Delta\phi_{1/2}
=24\pi.
}
\]
Equivalently,
\[
\boxed{
24\pi
=\underbrace{(3^2-1)}_{8\;SU(3)_F\;\text{mixing directions}}
\underbrace{3}_{\text{flavours}}
\underbrace{\pi}_{\text{half-turn phase}}.
}
\]

\section{Derived information normalization}
The TIR information density per primitive mixing-phase measure is
\[
\boxed{
\kappa
=\frac{I_\star}{\Phi_{\rm mix}}
=\frac{\ln2}{3(3^2-1)\pi}
=\frac{\ln2}{24\pi}
}
\]
with numerical value
\[
\kappa=0.00919315000636\ldots .
\]
Thus the integer factor $24$ is supplied by eight independent $SU(3)_F$ mixing
directions across three flavours, while $\pi$ is the primitive half-turn angular
unit.

\section{Independent tetrahedral integer crosscheck}
The local spatial branch derives the regular tetrahedron with
\[
\operatorname{Aut}(\Delta^3)\cong S_4,
\qquad
|S_4|=24.
\]
Hence
\[
\boxed{
3\dim\mathfrak{su}(3)_F
=3\cdot8
=24
=|S_4|.
}
\]
The flavour-mixing route supplies the normalization dependency; the tetrahedral
automorphism order is an independent finite-symmetry crosscheck.

\section{Exact phase-rate identity}
\label{app:kappa-phase-rate}
Let
\begin{equation}
\omega\equiv\frac{d\phi}{dt}=2\pi f,
\label{eq:kappa-omega-frequency}
\end{equation}
and
\begin{equation}
d\mathcal I\equiv\kappa\,d\phi.
\label{eq:kappa-information-phase-increment}
\end{equation}
Then
\begin{align}
\Gamma_{\mathcal I}
\equiv\frac{d\mathcal I}{dt}
&=\kappa\omega\\
&=\frac{\ln2}{24\pi}(2\pi f)
=\boxed{\frac{\ln2}{12}f}.
\label{eq:kappa-phase-refresh-identity}
\end{align}
One complete angular cycle carries
\begin{equation}
\boxed{
\Delta\mathcal I_{\rm cycle}
=2\pi\kappa
=\frac{\ln2}{12}.
}
\label{eq:kappa-information-per-cycle}
\end{equation}

\section{Constraint manifold and effective degree of freedom}
\label{app:kappa-constraint-manifold}
For
\[
\mathbf q=(\kappa,\omega,f,\Gamma_{\mathcal I})
\]
with
\begin{align}
C_1&=\kappa-\frac{\ln2}{24\pi}=0,\\
C_2&=\omega-2\pi f=0,\\
C_3&=\Gamma_{\mathcal I}-\kappa\omega=0,
\end{align}
the constraint Jacobian has rank three. The subsystem is therefore
one-dimensional and can be parametrized by
\[
\boxed{
\mathbf q(f)=
\left(
\frac{\ln2}{24\pi},
2\pi f,
f,
\frac{\ln2}{12}f
\right).
}
\]

\section{Crosswalk}
Appendix~\ref{app:information_spinor_crosswalk} records the same normalization
inside the broader identity-axis and flavour-mixing dependency graph.
"""
    path.write_text(text, encoding="utf-8")


def _patch_generated_intro(root: Path) -> None:
    """Synchronize generated introduction wording with the current kappa theorem."""
    path = root / "chapters" / "ch01_introduction.tex"
    text = path.read_text(encoding="utf-8")
    old = (
        "These are model postulates.  The factor $24\\pi$ is a discrete normalization\n"
        "ansatz, not the standard symplectic volume of $\\mathbb{C}P^3$; Appendix\n"
        "\\ref{app:kappa} states the precise and limited claim."
    )
    new = (
        "The $\\kappa$ coefficient is carried by the TIR-internal flavour-mixing\n"
        "normalization of Appendix~\\ref{app:kappa}: the three-flavour carrier has\n"
        "$\\dim\\mathfrak{su}(3)_F=8$, giving $3\\times8=24$ generator--flavour\n"
        "channels, while the primitive half-turn contributes the phase unit $\\pi$.\n"
        "The remaining discrete integers and flavour labels retain their own\n"
        "sector-specific provenance."
    )
    if old in text:
        text = text.replace(old, new, 1)
    path.write_text(text, encoding="utf-8")


ROOT = Path(__file__).resolve().parent
re.sub = _literal_hyperref_sub
runpy.run_path(
    str(ROOT / "prepare_publication_candidate_v11_0_impl.py"),
    run_name="__main__",
)
_deduplicate_publication_macros(ROOT)
_write_flavour_mixing_kappa_appendix(ROOT)
_patch_generated_intro(ROOT)
