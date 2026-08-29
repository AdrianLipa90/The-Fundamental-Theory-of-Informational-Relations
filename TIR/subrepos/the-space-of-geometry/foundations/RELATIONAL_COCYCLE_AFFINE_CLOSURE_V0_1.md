# Relational Cocycle to Affine Geometry v0.1

Status: `EXACT_LOCAL_AFFINE_RECONSTRUCTION_THEOREM_CANDIDATE`

Scope: derive local affine coordinates and additive displacement composition from the relational endpoint-closure law once relational displacements take values in the promoted local real carrier.

## 1. Relational displacement data

Let `X` be a contractible local set of relational loci and let

\[
\mathcal E_{xy}\in V
\]

be the displacement assigned to the oriented relation `x -> y`, where

\[
V\cong\operatorname{Herm}_0(2)\cong\mathbb R^3
\]

under the spatial-realization gate.

Work first in one local frame. Require

\[
\boxed{\mathcal E_{xx}=0,}
\]

\[
\boxed{\mathcal E_{yx}=-\mathcal E_{xy},}
\]

and triangular endpoint closure

\[
\boxed{
\mathcal E_{xy}+\mathcal E_{yz}+\mathcal E_{zx}=0
}
\]

for admitted local triples.

The last equation is exactly the zero endpoint-composition defect in a single trivialized frame.

## 2. Affine reconstruction theorem

Choose any reference locus `o in X` and define

\[
\boxed{r_o(x):=\mathcal E_{ox}.}
\]

Apply closure to the triangle `o -> x -> y -> o`:

\[
\mathcal E_{ox}+\mathcal E_{xy}+\mathcal E_{yo}=0.
\]

Using

\[
\mathcal E_{yo}=-\mathcal E_{oy},
\]

we obtain

\[
\boxed{
\mathcal E_{xy}
=\mathcal E_{oy}-\mathcal E_{ox}
=r_o(y)-r_o(x).
}
\]

### Theorem — local relational cocycle closure

If a local `V`-valued oriented relation map satisfies reversal and triangular endpoint closure, then it is an exact 1-cocycle: after choosing one reference locus,

\[
\boxed{
\mathcal E_{xy}=r(y)-r(x).
}
\]

Thus local affine coordinates are reconstructed from relations rather than introduced independently.

Changing the reference locus from `o` to `o'` adds the same constant vector to every coordinate:

\[
r_{o'}(x)=r_o(x)-r_o(o'),
\]

so relational displacements are origin-independent.

## 3. Additive endpoint composition

The coordinate representation immediately gives

\[
\begin{aligned}
\mathcal E_{xy}+\mathcal E_{yz}
&=[r(y)-r(x)]+[r(z)-r(y)]\\
&=r(z)-r(x)\\
&=\mathcal E_{xz}.
\end{aligned}
\]

Hence

\[
\boxed{
\mathcal E_{xz}
=\mathcal E_{xy}+\mathcal E_{yz}.
}
\]

The additive displacement law is therefore equivalent to local endpoint closure.

## 4. Metric reconstruction

Let the carrier have the positive inner product

\[
\langle A,B\rangle
=\frac12\operatorname{Tr}(AB).
\]

Define

\[
\boxed{
d(x,y):=\|\mathcal E_{xy}\|
=\|r(y)-r(x)\|.
}
\]

Then:

\[
d(x,y)\ge0,
\]

\[
d(x,y)=d(y,x),
\]

and from vector-norm subadditivity,

\[
\boxed{
d(x,z)\le d(x,y)+d(y,z).}
\]

On a nondegenerate local relation set where `E_xy=0` implies `x=y`, this is a metric.

Thus the metric-space structure follows from the same relational displacement data.

## 5. Angle and Pythagoras

For consecutive displacements

\[
A=\mathcal E_{xy},
\qquad
B=\mathcal E_{yz},
\]

we have

\[
\mathcal E_{xz}=A+B.
\]

Therefore

\[
\|\mathcal E_{xz}\|^2
=\|A\|^2+\|B\|^2+2\langle A,B\rangle.
\]

When

\[
\langle A,B\rangle=0,
\]

this becomes

\[
\boxed{
d(x,z)^2=d(x,y)^2+d(y,z)^2.}
\]

So the Pythagorean endpoint is now tied directly to relational endpoint closure.

## 6. Covariant version

With varying local frames, neighboring generators are first compared by the `SU(2)` transporter. The endpoint law is

\[
\boxed{
\mathcal E_{xz}
=
\mathcal E_{xy}
+
\operatorname{Ad}(U_{xy})\mathcal E_{yz}.
}
\]

In a local parallel trivialization this reduces to the affine theorem above. Nontrivial loop holonomy belongs to the downstream curvature layer.

## 7. A8 closure crosswalk

The endpoint defect

\[
\mathcal C_{xyz}
=
\mathcal E_{xz}
-
(\mathcal E_{xy}+\mathcal E_{yz})
\]

measures disagreement between direct and composed descriptions of the same endpoint relation.

The closure sector

\[
\boxed{\mathcal C_{xyz}=0}
\]

is precisely the sector in which local affine coordinates exist by the theorem above. This supplies a direct mathematical role for the previously registered A8 closure crosswalk.

## 8. Claim classes

| Statement | Class |
|---|---|
| reversal + triangular closure imply `E_xy=r(y)-r(x)` | EXACT ALGEBRAIC THEOREM |
| reference-point change is a global translation | EXACT |
| endpoint closure implies additive displacement composition | EXACT |
| positive carrier norm induces local metric under nondegeneracy | EXACT CONDITIONAL |
| orthogonal consecutive displacements give Pythagoras | EXACT |
| covariant transported closure reduces locally to the affine theorem | STANDARD LOCAL FRAME STATEMENT |
| A8 selects/stabilizes the zero-defect closure sector | TIR CROSSLINK CANDIDATE |
