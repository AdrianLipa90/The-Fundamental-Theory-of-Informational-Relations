# TIR Minimal Isotropic Tetrahedral Cell v0.1

Status: `EXACT_CONDITIONAL_MINIMAL_LOCAL_CELL_THEOREM_CANDIDATE`

Scope: TIR-only local spatial theorem inside the already-derived real generator carrier `Herm_0(2) ~= R^3`. This gate asks for the smallest finite equal-weight relation set that has no preferred direction and has a full isotropic second moment.

## 1. Local relation directions

At a primitive locus `x`, let

\[
\mathbf n_1,\ldots,\mathbf n_m\in\mathbb R^3
\]

be equal-norm outgoing relational displacement directions in the local generator carrier.

Normalize them to

\[
|\mathbf n_a|=1.
\]

Define the first moment

\[
\boxed{
\mathbf M:=\sum_{a=1}^{m}\mathbf n_a
}
\]

and the second-moment tensor

\[
\boxed{
Q:=\sum_{a=1}^{m}\mathbf n_a\mathbf n_a^T.
}
\]

## 2. Primitive isotropy conditions

The finite local relation set is declared isotropic through two moment conditions.

### No preferred direction

\[
\boxed{\mathbf M=0.}
\]

### Isotropic quadratic response

Because `Tr(Q)=m`, full second-moment isotropy requires

\[
\boxed{
Q=\frac{m}{3}I_3.
}
\]

The second condition implies

\[
\operatorname{rank}Q=3
\]

for `m>0`, so the local relations span the full generator carrier.

These conditions are rotationally covariant and contain no external spatial axis.

## 3. Three relations cannot satisfy both conditions

Suppose `m=3` and

\[
\mathbf n_1+\mathbf n_2+\mathbf n_3=0.
\]

Then

\[
\mathbf n_3=-(\mathbf n_1+\mathbf n_2),
\]

so all three vectors lie in the span of two vectors. Hence

\[
\operatorname{rank}\{\mathbf n_1,\mathbf n_2,\mathbf n_3\}\le2.
\]

But second-moment isotropy requires `rank(Q)=3`.

Therefore

\[
\boxed{m\ne3.}
\]

The cases `m=1,2` are also rank-deficient. Thus every nonzero equal-weight local relation set satisfying both primitive isotropy conditions obeys

\[
\boxed{m\ge4.}
\]

## 4. Four relations force the regular tetrahedral Gram matrix

Now let `m=4`. Form the `3 x 4` matrix

\[
N=(\mathbf n_1\;\mathbf n_2\;\mathbf n_3\;\mathbf n_4).
\]

The isotropy equations become

\[
NN^T=\frac43 I_3
\]

and

\[
N\mathbf 1=0.
\]

Let

\[
G=N^TN
\]

be the `4 x 4` Gram matrix. Since `NN^T` has three eigenvalues `4/3`, `G` has eigenvalues

\[
\frac43,\frac43,\frac43,0.
\]

The zero-moment condition gives

\[
G\mathbf 1=0.
\]

Hence the orthogonal projector onto the three-dimensional subspace perpendicular to `1` is

\[
P=I_4-\frac14\mathbf 1\mathbf 1^T
\]

and therefore

\[
\boxed{
G=\frac43P
=\frac43I_4-\frac13\mathbf 1\mathbf 1^T.
}
\]

Its diagonal entries are `1` and every off-diagonal entry is

\[
\boxed{
\mathbf n_a\cdot\mathbf n_b=-\frac13,
\qquad a\ne b.
}
\]

This is exactly the Gram matrix of the four radius vectors from the center of a regular tetrahedron to its vertices.

### Theorem — minimal isotropic relation cell

For equal-weight unit local relation directions in the TIR three-dimensional generator carrier, the conditions

\[
\sum_a\mathbf n_a=0
\]

and

\[
\sum_a\mathbf n_a\mathbf n_a^T=\frac m3I_3
\]

have no solution with fewer than four directions. At `m=4`, the Gram matrix is forced to be the regular tetrahedral one.

Thus

\[
\boxed{
\text{minimal finite full isotropy}
\Longrightarrow
\text{regular tetrahedral local relation cell}.
}
\]

## 5. Exact integer realization

An unnormalized exact realization is

\[
\mathbf v_1=(1,1,1),
\quad
\mathbf v_2=(1,-1,-1),
\]

\[
\mathbf v_3=(-1,1,-1),
\quad
\mathbf v_4=(-1,-1,1).
\]

Then

\[
\sum_{a=1}^{4}\mathbf v_a=0,
\]

\[
\mathbf v_a\cdot\mathbf v_a=3,
\]

\[
\mathbf v_a\cdot\mathbf v_b=-1
\quad(a\ne b),
\]

and

\[
\boxed{
\sum_{a=1}^{4}\mathbf v_a\mathbf v_a^T=4I_3.
}
\]

After division by `sqrt(3)`, this is precisely the normalized theorem above.

## 6. Relation to the rank-3 theorem

The tetrahedral theorem provides a finite local mechanism realizing the full-rank isotropy condition.

For its four edge generators,

\[
\operatorname{rank}\{\mathbf n_a\}=3
\]

and

\[
Q\propto I_3.
\]

Therefore the local cell does not merely span `R^3`; its quadratic relational response is direction-independent.

This strengthens the earlier chain

\[
\operatorname{Herm}_0(2)
\xrightarrow{SO(3)\text{ isotropy}}
\text{rank }3
\]

with a concrete minimal finite realization.

## 7. Defect functional

The theorem suggests an executable primitive spatial defect at every locus:

\[
\boxed{
\mathcal D_x
=
\alpha\left|\sum_a\mathbf n_a\right|^2
+
\beta\left\|
Q-\frac{\operatorname{Tr}Q}{3}I_3
\right\|_F^2,
\qquad \alpha,\beta>0.
}
\]

Then

\[
\mathcal D_x\ge0
\]

and

\[
\mathcal D_x=0
\]

exactly when the declared first- and second-moment isotropy conditions hold.

For equal-weight unit vectors and minimal valence, the zero-defect cell is tetrahedral.

This functional is a candidate **stability diagnostic**, not yet a fundamental action postulate.

## 8. Coupling to endpoint closure

The local isotropy defect can be paired with the endpoint-composition defect

\[
\mathcal C_{xyz}
\]

from `TIR_RELATIONAL_ENDPOINT_CLOSURE_V0_1`.

A discrete spatial regularity diagnostic is therefore

\[
\boxed{
\mathcal D_{\rm spatial}
=
\sum_x\mathcal D_x
+
\gamma\sum_{\triangle xyz}
\|\mathcal C_{xyz}\|^2,
\qquad\gamma>0.
}
\]

Its zero set simultaneously enforces local moment isotropy and triangular endpoint closure on the sampled cells.

A future TIR law may derive, minimize, or otherwise stabilize this defect. That dynamical/variational choice is still open.

## 9. Axiom crosswalk

- **A2** supplies the binary complex carrier whose traceless Hermitian generators form `R^3`.
- **A4** converges with the unit directional locus `S^2` and motivates isotropic local sampling.
- **A5** measures the geometry through dot products, Gram matrices, rank and moment invariants.
- **A7** supplies the no-preferred-direction/full-isotropy requirement.
- **A8** can act on non-closing local relational compositions through the separately defined endpoint-closure defect.

## 10. Claim classes

| Statement | TIR class |
|---|---|
| `m<4` cannot satisfy zero mean plus full isotropic second moment in `R^3` | EXACT LINEAR ALGEBRA |
| at `m=4` the Gram matrix has off-diagonal `-1/3` | EXACT |
| minimal equal-weight unit isotropic cell is regular tetrahedral | EXACT CONDITIONAL THEOREM |
| tetrahedral integer realization above | EXACT |
| local defect `D_x` is nonnegative and vanishes on declared isotropy conditions | EXACT |
| `D_spatial` is the fundamental physical action | OPEN TIR LAW CANDIDATE |
| tetrahedral cells admit a regular manifold continuum under arbitrary gluing | OPEN CONTINUUM GATE |

## 11. Next frontier

The next primitive question is now narrower:

\[
\boxed{
\text{Can the TIR axioms select the zero-defect isotropy/closure sector}
\quad
\mathcal D_{\rm spatial}=0
\quad
\text{without adding an independent free dynamical law?}
}
\]

That is the natural point to test A4, A7 and A8 together.