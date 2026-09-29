# Relational State-Difference Uniqueness v0.2

Status: `ZERO_AXIOM_RELATIONAL_DIFFERENCE_UNIQUENESS_THEOREM_CANDIDATE`

Scope: zero-axiom successor to v0.1. The older file is retained as provenance for the former A2/A3/A5/A7/A8 crosswalk.

## 1. Derived projective/Hilbert carrier

The upstream chain is

\[
\boxed{
R
\to
\{N,S\}
\to
S^2
\cong
\mathbb{CP}^1
\to
P(\mathbb C^2).
}
\]

The normalized two-state affine hull is

\[
\mathcal A_2=\frac12 I+V,
\qquad
V=\operatorname{Herm}_0(2)\cong\mathbb R^3.
\]

No quantum-point axiom is used.

## 2. Endpoint closure

Let

\[
D:\mathcal A_2\times\mathcal A_2\to V
\]

satisfy endpoint composition

\[
D(\rho,\tau)=D(\rho,\sigma)+D(\sigma,\tau).
\]

Fixing \(\rho_*\) and defining

\[
f(\rho)=D(\rho_*,\rho)
\]

gives

\[
\boxed{
D(\rho,\sigma)=f(\sigma)-f(\rho).
}
\]

This is the local zero-defect relation. It is the exact structural content formerly assigned to legacy A8.

## 3. Affine compatibility

Writing

\[
\rho=\rho_*+v,
\]

require the centered map to respect admitted affine combinations,

\[
L(av+bw)=aL(v)+bL(w).
\]

Hence

\[
L:V\to V
\]

is real linear and

\[
\boxed{
D(\rho,\sigma)=L(\sigma-\rho).
}
\]

This is the arithmetic/geometric compatibility formerly labelled A5.

## 4. Derived symmetry covariance

The projective/Hilbert carrier with Euler phase closure yields the standard unitary/projective symmetry action and

\[
PSU(2)\cong SO(3).
\]

Require common-frame covariance,

\[
D(U\rho U^\dagger,U\sigma U^\dagger)
=
U D(\rho,\sigma)U^\dagger.
\]

Thus

\[
L(\operatorname{Ad}_U v)
=
\operatorname{Ad}_U L(v).
\]

The defining real \(SO(3)\) representation on \(V\) is irreducible, so its commutant is

\[
\boxed{\operatorname{Comm}_{SO(3)}(V)=\mathbb R I.}
\]

Therefore

\[
\boxed{L=\lambda I.}
\]

## 5. Distinction preservation

The value \(\lambda=0\) collapses every distinguishable pair to the same relation value. This contradicts the admitted nontrivial relation.

Hence

\[
\boxed{\lambda\ne0.}
\]

Therefore

\[
\boxed{
D(\rho_x,\rho_y)
=
\lambda(\rho_y-\rho_x),
\qquad
\lambda\ne0.
}
\]

With Pauli/Bloch normalization,

\[
\boxed{\lambda=2.}
\]

## 6. Dependency audit

```text
RELATION
 -> RELATIONAL SPHERE
 -> CP1 = P(C2)
 -> AFFINE STATE HULL
 -> ENDPOINT ZERO-DEFECT COCYCLE
 -> LINEAR DIFFERENCE MAP
 -> HILBERT/EULER SO(3) COVARIANCE
 -> SCALAR COMMUTANT
 -> DISTINCTION PRESERVATION
 -> D(rho_x,rho_y)=lambda(rho_y-rho_x), lambda != 0
```

No legacy A1--A8 label is an independent parent.

## 7. Claim classes

| Statement | Class |
|---|---|
| endpoint cocycle gives a difference representation | EXACT |
| affine compatibility makes the centered map linear | EXACT |
| \(SO(3)\)-equivariant endomorphism is scalar | EXACT REPRESENTATION THEORY |
| nontrivial distinction implies \(\lambda\ne0\) | EXACT CONDITIONAL |
| relation law is unique up to global scale/orientation | EXACT CONDITIONAL |
| physical identification of the affine relation with spatial displacement | DOWNSTREAM PHYSICAL BINDING |

\[
\boxed{
N_{\rm nonlogical\ axioms}=0.
}
\]
