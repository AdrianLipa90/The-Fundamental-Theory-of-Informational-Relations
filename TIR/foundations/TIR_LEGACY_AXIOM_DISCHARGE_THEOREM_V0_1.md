# TIR Legacy Axiom Discharge Theorem v0.1

Status: `LEGACY_A1_A8_DISCHARGED__CANONICAL_PARENT_TIR_CANONICAL_DERIVATION_SPINE_V0_1`

Scope: provenance/discharge map for the historical labels A1--A8. The canonical foundation owner is `TIR_CANONICAL_DERIVATION_SPINE_V0_1.md`.

\[
\boxed{N_{\rm nonlogical\ axioms}=0.}
\]

## 1. Root typing

Absolute nothing is defined by absence of relation,

\[
\mathsf N:=\neg\exists R,
\]

and cannot itself be realized as existing under relational existence typing.

TIR distinguishes two minima:

\[
\boxed{
\min(\text{object})=P,
\qquad
\min(\text{nontrivial structure})=R.
}
\]

The number/value \(0\) is not ontic nothing; it is typed relational nullity.

## 2. A1--A4 discharge

### A1 — point minimality

A point is the minimum non-empty object carrier (singleton / zero-dimensional locus). It is not the minimum nontrivial structure; that role belongs to relation.

Therefore A1 is no longer an independent ontological postulate:

\[
\boxed{A1:\ \min(\text{object})=P\quad\text{DERIVED/TYPED}.}
\]

### A2 — quantum point / two-state projective carrier

The first nontrivial relation supplies two orientation roles \(\{N,S\}\). Their normalized coherent extension carries relative phase \(U(1)\cong S^1\):

\[
|\psi(u,\varphi)\rangle
=
\sqrt{1-u}|N\rangle
+
e^{i\varphi}\sqrt u|S\rangle.
\]

The endpoint phase circles collapse at \(u=0,1\), so

\[
(S^1\times[0,1])/\partial
\cong
\Sigma S^1
\cong
S^2.
\]

The same state is a normalized vector in \(\mathbb C^2\); quotienting global phase gives

\[
S^3/U(1)
=
\mathbb{CP}^1
\cong
S^2.
\]

Canonical source:

`TIR/foundations/TIR_LAGRANGIAN_BLOCH_SELECTION_V0_1.md`.

Thus the structural two-state projective/quantum representation is downstream of the point--relation--phase geometry rather than an independent A2 postulate. Empirical universality remains a separate physical claim.

### A3 — information primacy

For normalized exchange-invariant relational shares,

\[
(w_N,w_S)=\left(\frac12,\frac12\right),
\]

and

\[
\boxed{H_2(1/2)=\ln2.}
\]

Information is therefore measured on relational distinction; it is not inserted as an independent substance.

### A4 — spherical realization and efficiency

The sphere is supplied without assuming \(SO(3)\):

\[
\boxed{
S^1+\{N,S\}
\to
\Sigma S^1
\cong S^2
\cong\mathbb{CP}^1.
}
\]

Euler-characteristic closure gives

\[
\chi(S^1)=0,
\qquad
\chi(\Sigma S^1)=2.
\]

The Fubini--Study metric realizes the round projective metric. Separately, once a three-dimensional Euclidean fixed-volume/minimal-boundary problem is admitted, the standard isoperimetric theorem selects the sphere as equality case. These two statements must not be conflated.

## 3. A5--A6 discharge

For closed relational phase transport,

\[
e^{i\Delta\phi}=1
\iff
\Delta\phi=2\pi n,
\qquad n\in\mathbb Z.
\]

Hence

\[
\boxed{
n=\frac1{2\pi}\oint d\phi\in\mathbb Z
}
\]

is the winding/degree invariant, with positive magnitude giving the corresponding natural-number closure index.

Thus A5 and A6 are downstream of relational zero plus the already-derived \(U(1)\) phase carrier.

## 4. A7 discharge

After

\[
\mathbb{CP}^1=P(\mathbb C^2),
\]

projective Hilbert-frame symmetry gives the unitary/projective action, with

\[
SU(2)/\{\pm I\}\cong SO(3).
\]

The Berry connection plus the nontrivial Euler projective sign yields the minimal spin sector

\[
\boxed{s=\frac12}
\]

on the formal-symbolic gate already present in the repository. The exact spin lift satisfies

\[
2\pi\mapsto-I,
\qquad
4\pi\mapsto+I.
\]

Therefore the precise structural symmetry content is downstream; the historical phrase “universal symmetry” is retired as an axiom.

## 5. A8 discharge

If a projection erases a context coordinate, distinct relational states may collapse to an apparent contradiction. The lost distinction lies in the projection kernel. The TIR repair retains the context-bearing lift instead of interpreting zeroed information as ontic identity:

\[
(P,C_1;\neg P,C_2)
\mapsto
\widetilde X(C_1,C_2).
\]

This is the structural context-closure content formerly labelled A8. Physical realization of any particular paradox sector remains separately gated.

## 6. Circularity firewall

The canonical order is

\[
\boxed{
P
\to
R
\to
\{N,S\}
\to
\left\{
\begin{array}{l}
\frac12\to\ln2,\\
U(1)\cong S^1
\end{array}
\right.
\to
S^2\cong\mathbb{CP}^1
\to
(g_{FS},F_B)
\to
s=\frac12
\to
SU(2)/\{\pm I\}\cong SO(3).
}
\]

Prohibited foundation cycles include

\[
SO(3)\to S^2\to SU(2)\to SO(3)
\]

and

\[
\text{quantum axiom}\to\text{Bloch sphere}\to\text{proof of quantum axiom}.
\]

Spin-pole agreement with the upstream relational poles is a closure check, not a dependency edge.

## 7. Discharge table

| Legacy | Historical content | Current parent | Status |
|---|---|---|---|
| A1 | point minimality | singleton/0D object minimum | DERIVED/TYPED |
| A2 | quantum point | relation + coherent phase + projective/Bloch theorem | STRUCTURALLY DERIVED; PHYSICAL UNIVERSALITY SEPARATE |
| A3 | information primacy | relational distinction + normalized measure | DERIVED/DEFINITIONAL |
| A4 | sphere efficiency | S1 suspension/projective sphere + isoperimetric theorem | DERIVED WITH EXPLICIT HYPOTHESES |
| A5 | arithmetic measures geometry | relational-zero phase closure / winding | DERIVED |
| A6 | naturals from complex phase closure | winding/degree integer | DERIVED |
| A7 | universal symmetry | projective Hilbert + Berry/Euler + spin lift | PRECISE STRUCTURAL VERSION DERIVED |
| A8 | paradox stabilization | zero/kernel awareness + context-preserving lift | STRUCTURAL CLOSURE VERSION DERIVED |

Therefore

\[
\boxed{
N_{\rm legacy\ labels}=8,
\qquad
N_{\rm legacy\ independent\ axioms}=0.
}
\]

Validator:

`TIR/validation/tir_legacy_axiom_discharge_v0_1.py`.
