#!/usr/bin/env python3
"""Idempotently restore the reviewed κ phase-rate section after source generation.

The publication-candidate generator still emits the canonical v11.0 Appendix A
skeleton.  This patch applies the reviewed 2026-08-07 TIR/Metatime additions
without changing the generator's historical snapshot or any archived source.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent
APPENDIX = ROOT / "appendices" / "appA_kappa_derivation.tex"

PHASE_RATE_SECTION = r"""
\section{Exact phase-rate identity}
\label{app:kappa-phase-rate}
Let $\phi(t)$ denote a phase coordinate and define its angular rate in the
standard way,
\begin{equation}
  \omega\equiv\frac{d\phi}{dt}=2\pi f,
  \label{eq:kappa-omega-frequency}
\end{equation}
where $f$ is the cyclic frequency.  If informational accumulation is measured
per unit phase by
\begin{equation}
  d\mathcal I\equiv\kappa\,d\phi,
  \label{eq:kappa-information-phase-increment}
\end{equation}
then its rate is fixed algebraically:
\begin{align}
  \Gamma_{\mathcal I}
  \equiv\frac{d\mathcal I}{dt}
  &=\kappa\frac{d\phi}{dt}
    =\kappa\omega \\
  &=\frac{\ln2}{24\pi}(2\pi f)
    =\boxed{\frac{\ln2}{12}\,f}.
  \label{eq:kappa-phase-refresh-identity}
\end{align}
Equivalently, one complete phase cycle $\Delta\phi=2\pi$ carries the fixed
increment
\begin{equation}
  \Delta\mathcal I_{\rm cycle}=2\pi\kappa=\frac{\ln2}{12},
  \label{eq:kappa-information-per-cycle}
\end{equation}
so that $f$ cycles per unit time yield
$\Gamma_{\mathcal I}=f\,\Delta\mathcal I_{\rm cycle}$.

\section{Constraint manifold and effective degree of freedom}
\label{app:kappa-constraint-manifold}
Introduce
\[
  \mathbf q=(\kappa,\omega,f,\Gamma_{\mathcal I})\in\mathbb R^4
\]
with
\begin{align}
  C_1(\mathbf q)&=\kappa-\frac{\ln2}{24\pi}=0,\\
  C_2(\mathbf q)&=\omega-2\pi f=0,\\
  C_3(\mathbf q)&=\Gamma_{\mathcal I}-\kappa\omega=0.
\end{align}
The Jacobian
\[
  J_C=
  \begin{pmatrix}
    1 & 0 & 0 & 0\\
    0 & 1 & -2\pi & 0\\
    -\omega & -\kappa & 0 & 1
  \end{pmatrix}
\]
has rank three everywhere.  Hence the regular constraint set is
one-dimensional and may be parametrized globally by $f$:
\[
  \boxed{
  \mathbf q(f)=
  \left(
    \frac{\ln2}{24\pi},
    2\pi f,
    f,
    \frac{\ln2}{12}f
  \right)}.
\]
Conditional on the Metatime normalization and on
$d\mathcal I=\kappa\,d\phi$, this subsystem therefore has one continuous
degree of freedom.  Choosing $f$ fixes $\omega$ and
$\Gamma_{\mathcal I}$, while $\kappa$ is fixed by definition.

\paragraph{Claim boundary.}
The phase-rate identity and the dimension-one constraint statement are exact
consequences of the stated definitions.  Identifying
$\Gamma_{\mathcal I}$ with a physical ``surface-refresh rate'' remains an
additional Metatime/TIR interpretation requiring an operational observable.
""".strip()


def main() -> None:
    text = APPENDIX.read_text(encoding="utf-8")
    if "\\label{app:kappa-constraint-manifold}" in text:
        print("SKIP: κ phase-rate patch already present")
        return

    marker = "\\section{Mnemonic decompositions}"
    if marker not in text:
        raise SystemExit("Appendix A marker not found; refusing non-local rewrite")

    patched = text.replace(marker, PHASE_RATE_SECTION + "\n\n" + marker, 1)
    APPENDIX.write_text(patched, encoding="utf-8")
    print("UPDATED: appendices/appA_kappa_derivation.tex")


if __name__ == "__main__":
    main()
