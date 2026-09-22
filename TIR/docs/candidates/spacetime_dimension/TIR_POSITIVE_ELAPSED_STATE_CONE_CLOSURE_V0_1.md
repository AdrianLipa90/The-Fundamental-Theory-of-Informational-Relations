# TIR Positive Elapsed-State Cone Closure v0.1

Status: CANDIDATE_ONLY / EXACT_POSITIVE_CONE_EQUIVALENCE / FORWARD_COMPOSITION_SEMIGROUP_EXACT / PSD_CONE_NOT_INDEPENDENT_CHOICE / PHYSICAL_CLOCK_CALIBRATION_OPEN / CANON_ALLOWED_FALSE

Date: 2026-09-19

## 1. Purpose

The causal 3+1 pair theorem uses the positive-semidefinite cone

\[
\mathcal C_+=\operatorname{PSD}(2)
\]

as the future relation cone.

TIR already independently admits the trace-recovery lift

\[
X=\ell\rho,
\]

where

\[
\ell>0
\]

is a positive elapsed scale and

\[
\rho\succeq0,
\qquad
\operatorname{Tr}\rho=1
\]

is a normalized binary state.

This note proves that these are not two separate structures.

The nonzero PSD cone is exactly the image of positive elapsed scale times normalized binary state.

## 2. Normalized binary state space

Define

\[
\mathcal D_2
=
\{
\rho\in\operatorname{Herm}(2):
\rho\succeq0,\ 
\operatorname{Tr}\rho=1
\}.
\]

Every such state has Bloch form

\[
\boxed{
\rho
=
\frac12
\left(
I+\mathbf r\cdot\boldsymbol\sigma
\right),
\qquad
|\mathbf r|\le1.
}
\]

Pure states satisfy

\[
|\mathbf r|=1,
\]

and mixed interior states satisfy

\[
|\mathbf r|<1.
\]

## 3. Positive elapsed-state lift

Define

\[
\Phi:
\mathbb R_{>0}\times\mathcal D_2
\longrightarrow
\operatorname{PSD}(2)\setminus\{0\}
\]

by

\[
\boxed{
\Phi(\ell,\rho)=\ell\rho.
}
\]

Because

\[
\ell>0
\]

and

\[
\rho\succeq0,
\]

one has

\[
\ell\rho\succeq0.
\]

Since

\[
\operatorname{Tr}(\ell\rho)=\ell>0,
\]

the image is nonzero.

## 4. Exact inverse

Let

\[
X\in\operatorname{PSD}(2)\setminus\{0\}.
\]

Every nonzero PSD matrix has strictly positive trace, so define

\[
\boxed{
\ell=\operatorname{Tr}X
}
\]

and

\[
\boxed{
\rho=\frac{X}{\operatorname{Tr}X}.
}
\]

Then

\[
\rho\succeq0
\]

and

\[
\operatorname{Tr}\rho=1.
\]

Therefore

\[
\rho\in\mathcal D_2
\]

and

\[
X=\ell\rho.
\]

The inverse is unique because the trace fixes \(\ell\), after which \(\rho=X/\ell\).

Hence

\[
\boxed{
\mathbb R_{>0}\times\mathcal D_2
\cong
\operatorname{PSD}(2)\setminus\{0\}.
}
\]

If the zero-apex is included by identifying all formal pairs with \(\ell=0\), one obtains the full closed cone.

## 5. Pauli-coordinate form

Write

\[
\rho
=
\frac12
\left(
I+\mathbf r\cdot\boldsymbol\sigma
\right).
\]

Then

\[
X
=
\ell\rho
=
\frac{\ell}{2}I
+
\frac{\ell}{2}\mathbf r\cdot\boldsymbol\sigma.
\]

Thus the causal-theorem coordinates are

\[
\boxed{
t=\frac{\ell}{2},
\qquad
\mathbf x=\frac{\ell}{2}\mathbf r.
}
\]

The determinant is

\[
\boxed{
\det X
=
\frac{\ell^2}{4}
\left(
1-|\mathbf r|^2
\right).
}
\]

Therefore:

\[
|\mathbf r|<1
\Longleftrightarrow
\det X>0
\]

gives the timelike interior,

\[
|\mathbf r|=1
\Longleftrightarrow
\det X=0
\]

gives the null boundary.

The Bloch ball and the future determinant cone are the same carrier in different coordinates.

## 6. Future-cone inequality

Because

\[
|\mathbf r|\le1,
\]

one has

\[
|\mathbf x|
=
\frac{\ell}{2}|\mathbf r|
\le
\frac{\ell}{2}
=
t.
\]

Hence

\[
\boxed{
t\ge|\mathbf x|.
}
\]

Conversely, for any nonzero pair

\[
t\ge|\mathbf x|,
\qquad
t>0,
\]

define

\[
\ell=2t,
\qquad
\mathbf r=\frac{\mathbf x}{t}.
\]

Then

\[
|\mathbf r|\le1
\]

and

\[
X=\ell\rho.
\]

Thus the positive elapsed-state lift is exactly the causal future cone.

## 7. Exact forward composition

Take two forward packets

\[
X_1=\ell_1\rho_1,
\qquad
X_2=\ell_2\rho_2,
\]

with

\[
\ell_1,\ell_2>0,
\qquad
\rho_1,\rho_2\in\mathcal D_2.
\]

Then

\[
X_1+X_2
=
\ell_1\rho_1+\ell_2\rho_2.
\]

Define

\[
\boxed{
\ell_{12}
=
\ell_1+\ell_2
}
\]

and

\[
\boxed{
\rho_{12}
=
\frac{
\ell_1\rho_1+\ell_2\rho_2
}{
\ell_1+\ell_2
}.
}
\]

The weights

\[
\frac{\ell_1}{\ell_1+\ell_2},
\qquad
\frac{\ell_2}{\ell_1+\ell_2}
\]

are positive and sum to one.

Since the density-state set is convex,

\[
\rho_{12}\in\mathcal D_2.
\]

Therefore

\[
\boxed{
X_1+X_2
=
\ell_{12}\rho_{12}.
}
\]

Forward composition is exactly:

- addition of elapsed scales;
- elapsed-scale-weighted convex composition of normalized relational states.

No separate cone-closure axiom is required.

## 8. Pointedness and causal orientation

Suppose

\[
X\succeq0
\]

and

\[
-X\succeq0.
\]

Then

\[
\operatorname{Tr}X\ge0
\]

and

\[
-\operatorname{Tr}X\ge0.
\]

Hence

\[
\operatorname{Tr}X=0.
\]

A PSD matrix with zero trace has all eigenvalues zero, so

\[
X=0.
\]

Therefore

\[
\boxed{
\mathcal C_+\cap(-\mathcal C_+)=\{0\}.
}
\]

The sign of the elapsed scale supplies the orientation separating future from past.

## 9. Relation to the causal 3+1 pair theorem

The causal theorem had the explicit assumption:

\[
\text{future relation}=\operatorname{PSD}(2)\text{ cone order}.
\]

The present theorem shows that, once the already-admitted TIR/IDT lift

\[
X=\ell\rho
\]

is used with

\[
\ell>0
\]

and a valid normalized positive state \(\rho\), the PSD future cone is not an independent arbitrary choice.

It is exactly the image of the admissible positive elapsed-state domain.

Thus the previous physical gate

\[
\text{why PSD?}
\]

reduces to the narrower question

\[
\boxed{
\text{why is the physical forward displacement represented by }
(\ell>0,\rho\in\mathcal D_2)?
}
\]

TIR already supplies the binary normalized-state carrier.
IDT/RFC supplies the positive elapsed-scale candidate.

The remaining physical binding is primarily the calibrated identification of the event trace scale with the physical clock interval.

## 10. Relation to the SP3 finite witness

For the frozen SP3 pairs,

\[
\ell=c\Delta t
\]

and

\[
\mathbf r
=
\frac{\Delta\mathbf x}{c\Delta t}
=
\frac{\boldsymbol\beta}{c}.
\]

The already-validated bound

\[
|\mathbf r|<1
\]

gives the normalized state

\[
\boxed{
\rho_s
=
\frac12
\left(
I+\mathbf r_s\cdot\boldsymbol\sigma
\right)
\in\mathcal D_2.
}
\]

Then the observed half-difference carrier is

\[
\boxed{
H_s=\ell\rho_s.
}
\]

Thus the finite SP3 source does not merely lie numerically inside the cone.
It supplies explicit admissible elapsed-state coordinates for five nonzero cone elements.

This remains a finite compatibility witness, not universal physical confirmation.

## 11. Main theorem

### Theorem — positive elapsed-state cone equivalence

For the normalized binary state space \(\mathcal D_2\), the map

\[
\Phi(\ell,\rho)=\ell\rho
\]

is a bijection

\[
\boxed{
\mathbb R_{>0}\times\mathcal D_2
\longleftrightarrow
\operatorname{PSD}(2)\setminus\{0\}.
}
\]

Under this bijection:

\[
\boxed{
\ell=\operatorname{Tr}X,
\qquad
\rho=\frac{X}{\operatorname{Tr}X};
}
\]

\[
\boxed{
\det X
=
\frac{\ell^2}{4}(1-|\mathbf r|^2);
}
\]

\[
\boxed{
\text{mixed states}
\leftrightarrow
\text{timelike interior};
}
\]

\[
\boxed{
\text{pure states}
\leftrightarrow
\text{null boundary};
}
\]

and forward composition obeys

\[
\boxed{
(\ell_1,\rho_1)\oplus(\ell_2,\rho_2)
=
\left(
\ell_1+\ell_2,
\frac{\ell_1\rho_1+\ell_2\rho_2}{\ell_1+\ell_2}
\right).
}
\]

Therefore the causal PSD cone and its additive composition law arise exactly from positive elapsed scale plus valid normalized binary state.

## 12. Evidence boundary

Exact:

- cone bijection;
- inverse by trace normalization;
- Pauli/Minkowski determinant relation;
- pure/null correspondence;
- mixed/timelike correspondence;
- additive closure;
- weighted-state composition;
- pointedness.

Already admitted upstream:

- primitive binary normalized-state carrier;
- canonical trace-recovery lift candidate;
- positive elapsed-scale coordinate candidate.

Still physical:

- calibrated event-scale identification
  \[
  \ell=c\,\Delta t
  \]
  for the intended physical clock;
- universal physical interpretation of every forward local event displacement by this elapsed-state packet.

No claim is made that positivity alone proves the complete global spacetime theory.
