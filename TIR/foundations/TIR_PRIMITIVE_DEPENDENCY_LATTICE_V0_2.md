# TIR Primitive Dependency Lattice v0.2

Status: `ZERO_AXIOM_NONCIRCULAR_DEPENDENCY_LATTICE`

Scope: current primitive dependency graph after discharge of historical A1--A8. The v0.1 lattice is legacy provenance.

## 1. Root

\[
\boxed{N_{\rm nonlogical\ axioms}=0,\qquad \min(\mathrm{TIR})=R.}
\]

A nontrivial relation has orientation reversal

\[
J^2=\mathrm{id},
\qquad
\mathcal O_J=\{N,S\}.
\]

No global symmetry axiom is required to obtain this minimal two-role orbit.

## 2. Scalar branch

Normalize relational shares,

\[
w_N+w_S=1.
\]

Exchange of the two orientation roles fixes

\[
\boxed{w_N=w_S=\frac12},
\]

and therefore

\[
\boxed{H_2(1/2)=\ln2.}
\]

Dependency:

\[
\boxed{R\to\{N,S\}\to\frac12\to\ln2.}
\]

## 3. Sphere before quantum

The complete normalized orientation orbit is

\[
\boxed{SO(3)/SO(2)\cong S^2.}
\]

This is the abstract relational sphere. Next,

\[
\boxed{S^2\cong\mathbb{CP}^1},
\]

and

\[
\mathbb{CP}^1=P(\mathbb C^2)
\]

is the space of complex rays of a two-state Hilbert carrier.

Hence the canonical order is

\[
\boxed{
R
\to
\{N,S\}
\to
S^2
\to
\mathbb{CP}^1
\to
P(\mathbb C^2)
\to
\text{two-state quantum representation}.
}
\]

The prohibited circular order is

\[
\text{quantum axiom}\to\text{Bloch sphere}\to\text{quantum proof}.
\]

## 4. Zero-to-arithmetic branch

Closed relational return is typed by

\[
\Delta_R(\gamma)=0.
\]

For a phase lift,

\[
e^{i\Delta\phi}=1
\iff
\Delta\phi=2\pi n,
\qquad
n\in\mathbb Z.
\]

Thus

\[
\boxed{
0_R
\to
\text{closed phase relation}
\to
\frac1{2\pi}\oint d\phi=n\in\mathbb Z
\to
|n|\in\mathbb N.
}
\]

This discharges the old A5/A6 pair downstream of relational zero.

## 5. Hilbert--Euler symmetry branch

Once the projective Hilbert carrier exists, norm-preserving frame changes are unitary. Modulo global phase the action is projective unitary; the determinant-one lift yields the standard

\[
SU(2)\to SO(3).
\]

Euler phase closure gives

\[
e^{i(\phi+2\pi)}=e^{i\phi}.
\]

Hence the precise old-A7 content is downstream:

\[
\boxed{
\mathbb{CP}^1/P(\mathbb C^2)
+
\text{Euler closure}
\to
\text{unitary/projective symmetry}.
}
\]

## 6. Zero-to-context-closure branch

If a projection forgets a context coordinate, two distinct relational states can be mapped to an untyped apparent contradiction. The erased difference lies in the kernel of the projection. TIR therefore retains the context-bearing lift rather than interpreting the zeroed coordinate as ontic identity:

\[
\boxed{
(P,C_1;\neg P,C_2)
\to
\widetilde X(C_1,C_2).
}
\]

This is the structural discharge of old A8.

## 7. Canonical DAG

```text
RELATION
  |-- orientation reversal --> {N,S}
  |       |-- normalized exchange --> 1/2 --> ln2
  |       `-- orientation closure --> S2 --> CP1 --> P(C2) --> quantum carrier
  |                                               `--> Hilbert/Euler symmetry
  |
  `-- relational zero / closed return --> winding --> Z --> N
                                           `--> kernel awareness --> context lift
```

There are no A1--A8 nodes upstream of their own discharge.

## 8. Status

\[
\boxed{
N_{\rm legacy\ labels}=8,
\qquad
N_{\rm legacy\ independent\ axioms}=0.
}
\]

Canonical detailed proof surface:

`TIR/foundations/TIR_LEGACY_AXIOM_DISCHARGE_THEOREM_V0_1.md`.
