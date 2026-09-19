# TIR SP3 Delta Herm(2) Half-Lift Bridge v0.1

Status: CANDIDATE_ONLY / EXACT_CENTERED_HALF_DISPLACEMENT_INTERTWINER / RFC_SHIFT_MATCH_EXACT / PHYSICAL_PRODUCTION_CLAIM_FALSE / CANON_ALLOWED_FALSE

Date: 2026-09-19

## 1. Purpose

This candidate tests whether the already-observed two-epoch SP3 source admits an exact finite-event realization of the TIR trace-normalized Hermitian lift without identifying the raw SP3 clock-correction column with the TIR event trace scale.

The raw clock-correction column fails that direct interpretation and is therefore not used as the temporal event coordinate.

Instead the source-owned epoch separation supplies

\[
\Delta x^0=c\,\Delta t,
\]

while the observed spatial displacement supplies

\[
\Delta\mathbf x
=
\mathbf x^{(2)}-\mathbf x^{(1)}.
\]

For the frozen SP3 source,

\[
\Delta t=120\,\mathrm{s}.
\]

## 2. Existing TIR lift

TIR already defines

\[
\rho
=
\frac12
\left(
I+\mathbf r\cdot\boldsymbol\sigma
\right),
\qquad
X=\ell\rho.
\]

The exact candidate binding is

\[
\boxed{
\ell=c\Delta t,
\qquad
\mathbf r
=
\frac{\Delta\mathbf x}{c\Delta t}
=
\frac{\boldsymbol\beta}{c}.
}
\]

Therefore

\[
\boxed{
X
=
\frac12
\left(
c\Delta t\,I
+
\Delta\mathbf x\cdot\boldsymbol\sigma
\right).
}
\]

In coefficient form,

\[
\boxed{
x^0=\frac{c\Delta t}{2},
\qquad
x^i=\frac{\Delta x^i}{2}.
}
\]

Thus the TIR Hermitian object is the exact centered half-displacement operator for the two-epoch source.

## 3. Trace recovery

Because

\[
\operatorname{Tr}I=2,
\qquad
\operatorname{Tr}\sigma_i=0,
\qquad
\operatorname{Tr}(\sigma_i\sigma_j)=2\delta_{ij},
\]

the source displacement is recovered exactly:

\[
\boxed{
\operatorname{Tr}X=c\Delta t
}
\]

and

\[
\boxed{
\operatorname{Tr}(X\sigma_i)=\Delta x^i.
}
\]

Hence the map from the centered \(3+1\) displacement to \(X\in\operatorname{Herm}(2)\) is lossless.

## 4. Midpoint association

Let

\[
\bar{\mathbf x}
=
\frac{
\mathbf x^{(1)}+\mathbf x^{(2)}
}{2}.
\]

Then

\[
\mathbf x^{(1)}
=
\bar{\mathbf x}-\frac{\Delta\mathbf x}{2},
\qquad
\mathbf x^{(2)}
=
\bar{\mathbf x}+\frac{\Delta\mathbf x}{2}.
\]

The Pauli coefficients of \(X\) are exactly the spatial half-increments \(\Delta\mathbf x/2\).

Likewise, in a centered temporal chart,

\[
t^{(1)}=-\frac{\Delta t}{2},
\qquad
t^{(2)}=+\frac{\Delta t}{2},
\]

and the identity coefficient of \(X\) is exactly \(c\Delta t/2\).

Therefore

\[
\boxed{
\text{two source events}
\Longleftrightarrow
\text{midpoint}
+
\text{Hermitian half-displacement}.
}
\]

This is the exact algebraic meaning of the factor one-half association in this candidate.

## 5. RFC shift equality

The existing RFC/SP3 matching construction defines

\[
\boldsymbol\beta
=
\frac{\Delta\mathbf x}{\Delta t}
\]

and exports

\[
\mathbf b
=
\frac{\boldsymbol\beta}{c}.
\]

Therefore

\[
\boxed{
\mathbf r=\mathbf b
}
\]

exactly at the candidate source level.

No additional direction variable is introduced: the normalized Bloch/Pauli vector used by the TIR lift is numerically the already-existing RF-E8 shift.

## 6. Positive-cone condition

The eigenvalues of \(X\) are

\[
\lambda_\pm
=
\frac{c\Delta t}{2}
\left(
1\pm|\mathbf r|
\right)
=
\frac{
c\Delta t\pm|\Delta\mathbf x|
}{2}.
\]

Thus

\[
X>0
\quad\Longleftrightarrow\quad
|\boldsymbol\beta|<c.
\]

For every frozen SP3 satellite segment this inequality is satisfied by a very large margin.

Equivalently,

\[
\det X
=
\frac14
\left[
(c\Delta t)^2
-
|\Delta\mathbf x|^2
\right]
>0.
\]

This places every two-epoch displacement witness strictly inside the TIR future determinant cone.

## 7. Important no-go: raw SP3 clock correction

The SP3 clock-correction column is not the same object as the elapsed epoch separation.

If the midpoint clock correction is naively converted to a length and used as the Hermitian temporal coefficient, all five source tuples fail the future-cone condition.

Therefore

\[
\boxed{
\text{raw SP3 clock correction}
\neq
\text{TIR event trace scale}.
}
\]

The candidate bridge uses the source epoch separation \(\Delta t\), not the clock-correction value.

## 8. Relation to the 3+1 mnemonic

The finite source contains:

1. a \(3+1\) displacement \((c\Delta t,\Delta\mathbf x)\);
2. exact association by the factor \(1/2\);
3. an invertible midpoint/half-displacement decomposition;
4. the same normalized vector \(\mathbf r=\boldsymbol\beta/c\) already exported as RF-E8 shift.

This gives a mathematically exact candidate interpretation of the mnemonic

\[
3+1
\longrightarrow
/2
\longrightarrow
\text{association}.
\]

The separate Collatz branch

\[
n\mapsto3n+1,
\qquad
n\mapsto n/2
\]

remains an independent structural layer. This candidate does not assert an intertwiner between the integer Collatz map and the two-epoch Hermitian displacement map.

## 9. Evidence boundary

This candidate establishes only a finite observationally anchored source witness.

It does not establish:

- a global physical spacetime identification;
- that every physical event pair uses this finite SP3 construction;
- a physical-production promotion of the TIR spatial or matching captures;
- a Collatz-to-spacetime dynamical law.

Current classification:

external two-epoch source: PRESENT
delta x0 = c delta t: SOURCE-OWNED
delta spatial displacement: SOURCE-OWNED
r = beta/c = RFC shift: EXACT
Herm(2) half-displacement lift: EXACT
trace recovery: EXACT
positive-cone witness: PASS ON FROZEN SOURCE
raw SP3 clock -> event trace scale: REFUTED
global physical carrier binding: OPEN
physical production claim: FALSE
canon allowed: FALSE
