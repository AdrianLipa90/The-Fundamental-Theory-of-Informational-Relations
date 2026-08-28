# TIR Relational Endpoint Closure v0.1

Status: `EXACT_CONDITIONAL_TORSION_CLOSURE_CANDIDATE`

Scope: TIR-only derivation gate connecting the discrete solder construction to a torsion-free spatial continuum. The central primitive object is not a temporal trajectory but consistency of relational composition between the same endpoints.

## 1. Parent discrete geometry

For every oriented relational edge

\[
x\to y
\]

TIR assigns a displacement generator

\[
\mathcal E_{xy}\in\operatorname{Herm}_0(2)
\]

and a frame transporter

\[
U_{xy}\in SU(2).
\]

A generator at `y` is represented in the frame at `x` by

\[
\operatorname{Ad}_{U_{xy}}(A_y)
=U_{xy}A_yU_{xy}^\dagger.
\]

## 2. Two descriptions of the same endpoint relation

Consider three loci `x,y,z` and two admitted descriptions of the displacement from `x` to `z`.

The direct relation is

\[
\mathcal E_{xz}.
\]

The composed relation through `y`, expressed in the frame at `x`, is

\[
\boxed{
\mathcal E_{xy}
+
U_{xy}\mathcal E_{yz}U_{xy}^\dagger.
}
\]

Define the endpoint-composition defect

\[
\boxed{
\mathcal C_{xyz}
:=
\mathcal E_{xz}
-
\left(
\mathcal E_{xy}
+U_{xy}\mathcal E_{yz}U_{xy}^\dagger
\right).
}
\]

## 3. Primitive endpoint closure law candidate

The primitive closure condition is

\[
\boxed{
\mathcal C_{xyz}=0
}
\]

whenever the direct edge and the composed path are declared to encode the same relational endpoint displacement in the same comparison frame.

This is not temporal path independence. It is equality of two structural compositions in the primitive dependency geometry.

The condition can be written

\[
\boxed{
\mathcal E_{xz}
=
\mathcal E_{xy}
+U_{xy}\mathcal E_{yz}U_{xy}^\dagger.
}
\]

## 4. Equivalence with triangular torsion defect

Using the reverse-edge convention

\[
\mathcal E_{zx}
=-U_{zx}\mathcal E_{xz}U_{zx}^\dagger,
\]

the triangle closure defect from the discrete solder construction is

\[
\mathcal T_{xyz}
=
\mathcal E_{xy}
+U_{xy}\mathcal E_{yz}U_{xy}^\dagger
+U_{xz}\mathcal E_{zx}U_{xz}^\dagger.
\]

With `U_zx=U_xz^{-1}`,

\[
U_{xz}\mathcal E_{zx}U_{xz}^\dagger=-\mathcal E_{xz}.
\]

Therefore

\[
\boxed{
\mathcal T_{xyz}=-\mathcal C_{xyz}.
}
\]

Hence

\[
\boxed{
\mathcal C_{xyz}=0
\Longleftrightarrow
\mathcal T_{xyz}=0.
}
\]

So endpoint-composition consistency is exactly the discrete torsion-free closure condition for a triangular relational cell.

## 5. A8 closure crosswalk

A8 acts when two admitted relational descriptions cannot be represented consistently in the current closure surface.

Here the two valid descriptions are

```text
DIRECT:   x -> z
COMPOSED: x -> y -> z
```

The mismatch is measured by `C_xyz`.

The TIR closure candidate is therefore

\[
\boxed{
A8:\quad
(\mathcal E_{xz},
\mathcal E_{xy}\oplus\mathcal E_{yz})
\mapsto
\mathcal C_{xyz}=0
}
\]

for primitive contractible endpoint comparisons.

This is a concrete mathematical realization candidate for “paradox as stabilizer”: incompatible path descriptions expose a closure defect; the closure surface is admitted only when the defect is resolved.

A8 itself does not replace the equation. The equation is the explicit consistency law being tested.

## 6. Continuum limit

Assume a regular refinement in which

\[
\mathcal E_{xy}
=e^a{}_i\Delta x^i\sigma_a+O(|\Delta x|^2)
\]

and the discrete transport converges to a smooth metric-compatible connection `omega^a_b`.

For infinitesimal contractible loops, the leading translational closure defect converges to Cartan torsion

\[
\boxed{
T^a
=de^a+\omega^a{}_b\wedge e^b.
}
\]

Therefore, if endpoint closure holds throughout a refining family with controlled error tending to zero,

\[
\boxed{
\mathcal C_{xyz}\to0
\Longrightarrow
T^a=0
}
\]

in the smooth limit.

This is an exact conditional continuum target under the declared regularity and convergence assumptions.

## 7. Levi-Civita closure

The `SU(2)/SO(3)` transporter construction preserves the Hilbert--Schmidt metric on the generator carrier, so its real frame connection is metric-compatible.

On a smooth spatial manifold, the fundamental theorem of Riemannian geometry states that there is a unique connection satisfying

\[
D h=0
\]

and

\[
T=0.
\]

Therefore, once the solder map is regular and endpoint closure yields zero torsion,

\[
\boxed{
\text{metric compatibility}+\text{endpoint closure}
\Longrightarrow
D=D^{\rm LC}.
}
\]

The spatial Levi-Civita connection is then selected rather than separately postulated.

## 8. Curvature remains holonomy

The rotational loop product

\[
\mathcal H_\gamma
=\prod_{e\in\gamma}U_e
\]

may remain nontrivial even when the translational closure defect vanishes.

Thus

\[
T=0
\]

does not force

\[
R=0.
\]

This cleanly separates the two primitive defects:

```text
translational endpoint mismatch -> torsion
rotational frame holonomy       -> curvature
```

A torsion-free curved spatial geometry is therefore naturally admitted.

## 9. Updated primitive spatial chain

With the rank-3 isotropy theorem and endpoint closure gate, the TIR spatial programme becomes

\[
\boxed{
\mathbb C^2
\to
\operatorname{Herm}_0(2)
\xrightarrow{\text{full isotropy}}
W_x\cong\mathbb R^3
\to
\mathcal E_{xy}
\xrightarrow{\text{endpoint closure}}
T=0
\to
D^{\rm LC}
\to
R.
}
\]

The remaining high-value issue is now the continuum existence/stability theorem for a refining relational family.

## 10. Claim classes

| Statement | TIR class |
|---|---|
| endpoint defect `C_xyz` definition | EXACT DEFINITION |
| `T_xyz=-C_xyz` under reverse-edge convention | EXACT ALGEBRAIC |
| endpoint closure iff triangular discrete torsion closure | EXACT |
| full local `SO(3)` transport is metric-preserving | EXACT FROM GENERATOR REPRESENTATION |
| regular endpoint-closed refinement gives `T^a=0` continuum target | EXACT CONDITIONAL LIMIT STATEMENT |
| metric compatibility + zero torsion selects Levi-Civita connection | STANDARD EXACT RIEMANNIAN THEOREM |
| A8 selects endpoint closure as primitive law | TIR CLOSURE-LAW CANDIDATE |
| existence of a regular refining family | OPEN TIR CONTINUUM GATE |

## 11. Next frontier

The next TIR question is now sharply reduced to stability:

\[
\boxed{
\text{Which primitive local relation rule guarantees}
\quad
r_x=3,
\quad
\|\mathcal C_{xyz}\|\to0,
\quad
\text{and a regular continuum limit?}
}
\]

The first two quantities are now explicit observables of the discrete relational geometry.