# Physical Length-Scale Calibration v0.1

Status: `EXACT_ONE_PARAMETER_EUCLIDEAN_LENGTH_CALIBRATION_THEOREM_CANDIDATE`

Scope: determine exactly what remains after the local TIR spatial carrier, Euclidean inner product, physical chord domain, and Pythagorean closure have been fixed. The result isolates the single positive calibration parameter that converts the dimensionless local relation norm into a physical length.

## 1. Established dimensionless local metric

The local relation carrier is

\[
V=\operatorname{Herm}_0(2)\cong\mathbb R^3,
\]

with canonical invariant inner product

\[
\boxed{
g_0(A,B):=\frac12\operatorname{Tr}(AB).
}
\]

For a relation

\[
\mathcal E=\mathbf d\cdot\boldsymbol\sigma,
\]

its dimensionless squared norm is

\[
\boxed{
q_0(\mathcal E)=g_0(\mathcal E,\mathcal E)
=\frac12\operatorname{Tr}(\mathcal E^2)
=|\mathbf d|^2.
}
\]

## 2. The scale family

Let `L_* > 0` carry physical length dimension. Define

\[
\boxed{
g_{\rm phys}:=L_*^2 g_0.}
\]

Then the physical length of a local relation is

\[
\boxed{
\ell_{\rm phys}(\mathcal E)
=L_*\sqrt{\frac12\operatorname{Tr}(\mathcal E^2)}.
}
\]

Because the real defining representation of `SO(3)` on `V` is irreducible, every positive `SO(3)`-invariant inner product on `V` is a positive scalar multiple of `g_0`. Therefore every physical Euclidean metric that preserves the already-derived local rotational structure belongs to the one-parameter family

\[
\boxed{
g_{\rm phys}=L_*^2 g_0,\qquad L_*>0.}
\]

Thus the local Euclidean geometry determines shape and relative length completely, while dimensional calibration is represented by one positive scalar.

## 3. Calibration from one typed physical datum

Let a nonzero reference relation `E_ref` have dimensionless squared norm

\[
q_{\rm ref}=\frac12\operatorname{Tr}(\mathcal E_{\rm ref}^2)>0
\]

and assigned or measured physical length `ell_ref`. Then

\[
\ell_{\rm ref}=L_*\sqrt{q_{\rm ref}},
\]

so the calibration parameter is uniquely fixed by

\[
\boxed{
L_*=\frac{\ell_{\rm ref}}{\sqrt{q_{\rm ref}}}.
}
\]

One typed length datum therefore selects one representative of the scale family.

## 4. Physical chord diameter

For physical binary density-state endpoints, the exact coefficient-vector relation domain is

\[
|\mathbf d|\le2.
\]

Therefore the calibrated single-edge physical domain satisfies

\[
\boxed{
0\le\ell_{\rm phys}\le2L_*.
}
\]

Its physical diameter scale is consequently

\[
\boxed{D_{\rm edge}=2L_*.}
\]

Conversely, a physically fixed single-edge diameter `D_edge` determines

\[
\boxed{L_*=D_{\rm edge}/2.}
\]

## 5. Scale-independent geometric invariants

For `A,B != 0`, the calibrated angle is

\[
\cos\theta
=\frac{g_{\rm phys}(A,B)}{\sqrt{g_{\rm phys}(A,A)g_{\rm phys}(B,B)}}
=\frac{g_0(A,B)}{\sqrt{g_0(A,A)g_0(B,B)}}.
\]

Hence angle and orthogonality are independent of `L_*`.

For two lengths,

\[
\frac{\ell_{\rm phys}(A)}{\ell_{\rm phys}(B)}
=\frac{\|A\|_0}{\|B\|_0}.
\]

The Pythagorean relation is covariant under the same calibration:

\[
\|A+B\|_0^2=\|A\|_0^2+\|B\|_0^2
\]

implies

\[
\boxed{
\ell_{\rm phys}(A+B)^2
=\ell_{\rm phys}(A)^2+\ell_{\rm phys}(B)^2.
}
\]

The regular tetrahedral Gram value

\[
n_a\cdot n_b=-\frac13
\]

is likewise scale-independent after normalization.

## 6. Dimensional source typing

The existing local structural constants used in this branch -- rational numbers, group dimensions, `ln 2`, `kappa`, Gram coefficients, and representation-theoretic normalization factors -- are dimensionless quantities. They may determine dimensionless coefficients multiplying a calibrated scale.

The physical length unit is supplied by a typed datum carrying length dimension, or by a later bridge whose dimensional inputs combine to length. Any proposed source for `L_*` is therefore admitted through an explicit dimensional-type check

\[
\boxed{[L_*]=L.}
\]

This provides a clean gate for later TIR, matter-sector, temporal, or empirical scale-binding proposals.

## 7. Dependency result

The calibrated local chain is

\[
\boxed{
\operatorname{Herm}_0(2)
\xrightarrow{g_0}
\text{dimensionless Euclidean geometry}
\xrightarrow{L_*>0}
\text{physical Euclidean length geometry}.
}
\]

with

\[
\boxed{
\ell_{\rm phys}(\mathcal E)
=L_*\sqrt{\frac12\operatorname{Tr}(\mathcal E^2)}.
}
\]

The current frontier is therefore reduced to a sharply typed source problem:

\[
\boxed{\text{derive or bind the physical source of }L_*.}
\]

## 8. Claim classes

| Statement | Class |
|---|---|
| `g_0(A,B)=Tr(AB)/2` | ESTABLISHED LOCAL CARRIER METRIC |
| every positive `SO(3)`-invariant Euclidean metric is a positive scalar multiple of `g_0` | EXACT REPRESENTATION THEORY |
| `g_phys=L_*^2 g_0` | EXACT ONE-PARAMETER CALIBRATION FAMILY |
| `ell_phys(E)=L_* sqrt(Tr(E^2)/2)` | EXACT GIVEN CALIBRATION |
| one nonzero physical reference length fixes `L_*` uniquely | EXACT |
| physical one-edge radius is `2L_*` | EXACT GIVEN THE PHYSICAL CHORD THEOREM |
| angles, ratios, orthogonality and Pythagorean closure are scale-independent/covariant | EXACT |
| a candidate source for `L_*` must carry physical length dimension after all bridges are applied | DIMENSIONAL-TYPE GATE |
