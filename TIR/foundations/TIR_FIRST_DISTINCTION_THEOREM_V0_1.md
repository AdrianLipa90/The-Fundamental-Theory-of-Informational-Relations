# TIR First Distinction Theorem v0.1

Status: `EXACT_CONDITIONAL_FOUNDATION_CANDIDATE`

Scope: TIR-only derivation of the first non-zero informational distinction from the declared minimal-carrier, information-primacy, and symmetry axioms. The quantum axiom enters only after the binary distinction is established, when the two alternatives are lifted into a Hilbert carrier.

## 1. Primitive quantities

Let

\[
\nu(X)\in\mathbb N_{\ge 1}
\]

denote the number of mutually distinguishable relational alternatives available in a carrier description \(X\).

Define the distinction number

\[
\boxed{D(X)=\nu(X)-1.}
\]

For the A1 minimal point carrier \(\mathcal P\),

\[
\nu(\mathcal P)=1,
\qquad
D(\mathcal P)=0.
\]

This is the undivided state.

## 2. First non-zero distinction

A non-zero distinction requires

\[
D(X)>0,
\]

hence

\[
\nu(X)>1.
\]

Because \(\nu\) is natural-valued, the smallest admissible value is uniquely

\[
\boxed{\nu_1=2.}
\]

Therefore the minimal distinction operator is

\[
\boxed{
\Delta_1:\nu=1\longmapsto\nu=2.
}
\]

Equivalently,

\[
\boxed{
\mathcal P\xrightarrow{\Delta_1}\{N,S\},
}
\]

where `N` and `S` are merely labels for the two first distinguishable relational alternatives.

### Theorem 1 — Minimal Binary Distinction

Given:

1. a non-empty undivided carrier with \(\nu=1\);
2. distinction count \(D=\nu-1\);
3. discrete alternative count \(\nu\in\mathbb N_{\ge1}\);
4. the requirement that the first distinction be the smallest possible state with \(D>0\);

then

\[
\boxed{\nu_1=2}
\]

is unique.

The binary carrier is therefore not inserted as an arbitrary multiplicity: it is the smallest nontrivial distinguishability class.

## 3. Symmetry of the first distinction

Let the A7 symmetry of the first unresolved distinction act by the transposition

\[
J:N\leftrightarrow S,
\qquad
J^2=\mathrm{id}.
\]

Let the probability vector be

\[
\mathbf p=(p_N,p_S),
\qquad
p_N+p_S=1.
\]

Invariance under pole exchange requires

\[
J\mathbf p=\mathbf p,
\]

so

\[
(p_S,p_N)=(p_N,p_S).
\]

Hence

\[
p_N=p_S.
\]

Together with normalization,

\[
2p_N=1,
\]

and therefore

\[
\boxed{
p_N=p_S=\frac12.
}
\]

### Theorem 2 — Unique Symmetric Binary Prior

The only normalized probability vector on two alternatives invariant under the full exchange symmetry \(S_2\) is

\[
\boxed{\left(\frac12,\frac12\right).}
\]

## 4. First information quantum

For binary Shannon entropy

\[
H_2(p)=-p\ln p-(1-p)\ln(1-p),
\]

substitution of the unique symmetric first distinction gives

\[
H_2\!\left(\frac12\right)
=-2\left(\frac12\ln\frac12\right)
=\boxed{\ln2}.
\]

Thus the exact conditional chain is

\[
\boxed{
D=0
\xrightarrow{\text{minimal }D>0}
\nu=2
\xrightarrow{S_2\text{ invariance}}
\left(\frac12,\frac12\right)
\xrightarrow{H_2}
\ln2.
}
\]

This is the first closed derivation frontier of the TIR axiomatic kernel.

## 5. Half-seam equivalence

Parameterize the binary shares by

\[
\mathbf p(u)=(1-u,u),
\qquad
u=2.
\]

Pole exchange acts as

\[
J(u)=1-u.
\]

The invariant probability vector occurs at the fixed point

\[
J(u_\star)=u_\star,
\]

so

\[
\boxed{u_\star=\frac12.}
\]

Therefore the symmetry derivation and the relational half-seam are the same binary object in two coordinate languages:

\[
\boxed{
S_2\text{-invariant prior}
\Longleftrightarrow
\operatorname{Fix}(u\mapsto1-u)
\Longleftrightarrow
u=2,\;p=1/2.
}
\]

This binds directly to

`TIR/integration/TIR_RELATIONAL_HALF_SEAM_CROSSLINK_V0_1.md`.

## 6. Quantum lift

A2 states that the minimal carrier is quantum. Once \(\Delta_1\) has produced two distinguishable alternatives, the minimal complex Hilbert carrier capable of representing both as orthogonal pure alternatives has dimension two:

\[
\boxed{\mathcal H_2\cong\mathbb C^2.}
\]

Choose

\[
|N\rangle=\begin{pmatrix}1\\0\end{pmatrix},
\qquad
|S\rangle=\begin{pmatrix}0\\1\end{pmatrix}.
\]

The equal-share coherent family is

\[
\boxed{
|\psi_{1/2}(\varphi)\rangle
=\frac{1}{\sqrt2}
\left(|N\rangle+e^{i\varphi}|S\rangle\right).
}
\]

The probability symmetry fixes the moduli but leaves one relative phase degree of freedom:

\[
|\alpha|^2=|\beta|^2=\frac12,
\qquad
\varphi=\arg\beta-\arg\alpha.
\]

This relative phase is the first additional coordinate that appears after the informational half-seam is coherently lifted.

## 7. Dependency separation

The information-theoretic theorem uses

\[
\boxed{A1+A3+A7+\text{minimality definition of first distinction}.}
\]

The quantum lift additionally uses

\[
\boxed{A2.}
\]

Therefore the dependency graph is

```text
A1 POINT MINIMALITY
A3 INFORMATION PRIMACY
A7 SYMMETRY
  -> minimal non-zero distinction
  -> two alternatives
  -> unique S2-invariant prior (1/2,1/2)
  -> Shannon information ln2
  -> relational half-seam

A2 QUANTUM POINT
  + binary distinction
  -> C^2
  -> equal-modulus coherent half family
  -> relative phase phi
```

## 8. Claim classes

| Statement | TIR class |
|---|---|
| smallest natural-valued \(\nu>1\) is \(2\) | EXACT ARITHMETIC |
| minimal non-zero distinction has two alternatives | EXACT CONDITIONAL ON DECLARED DISTINCTION COUNT |
| unique normalized \(S_2\)-invariant binary prior is \((1/2,1/2)\) | EXACT |
| \(H_2(1/2)=\ln2\) | EXACT INFORMATION-THEORETIC |
| symmetric prior equals half-seam fixed point | EXACT COORDINATE EQUIVALENCE |
| minimal Hilbert span of two orthogonal alternatives is \(\mathbb C^2\) | EXACT LINEAR-ALGEBRAIC |
| equal-modulus coherent family retains relative phase | EXACT |
| physical realization of the axioms | TIR FOUNDATIONAL POSTULATE LAYER |

## 9. Immediate next gate

The first distinction is now reduced to a precise discrete minimality theorem. The next foundation gate is to determine which additional TIR principle fixes the status and dynamics of the relative phase \(\varphi\) after the coherent lift:

\[
\boxed{
\left(\frac12,\frac12\right)
\longrightarrow
|\psi_{1/2}(\varphi)\rangle
\longrightarrow
\text{phase law}.
}
\]

That gate is the clean entry point toward the later unitary/Schrödinger branch, without importing temporal dynamics prematurely.
