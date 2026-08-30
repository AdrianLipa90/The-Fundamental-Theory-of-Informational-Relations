# TIR Zero-Torsion and Levi-Civita Selection v0.1

Status: `EXACT_PRIMITIVE_ENDPOINT_SELECTION / ZERO_TORSION_REGULAR_REFINEMENT_PASS / LEVI_CIVITA_UNIQUENESS_PASS / GLOBAL_CONTINUUM_EXISTENCE_OPEN / BROADER_CARTAN_TORSION_SECTOR_RETAINED`

Date: 2026-08-30

## 1. Purpose

Gate A2 identifies the continuum Cartan torsion and curvature coordinates and proves that the leading translational torsion coefficient is not contaminated by rotational curvature. Gate A3 now selects the spatial GR connection sector from existing TIR parent structures.

The selection is deliberately typed as a sector theorem.

TIR carries both:

```text
primitive same-endpoint relation sector
context-lifted connection sector
```

The spatial GR route uses the first whenever two descriptions are admitted as representations of the same primitive endpoint relation. Context-bearing departures remain available to the broader Cartan branch.

## 2. Parent 1 — unique intrinsic affine relation

The quantum relation affine-torsor theorem supplies

\[
\mathcal E_{xy}=2(\rho_y-\rho_x)
\in\operatorname{Herm}_0(2),
\]

with exact composition in one affine carrier,

\[
\boxed{
\mathcal E_{xz}
=\mathcal E_{xy}+\mathcal E_{yz}.
}
\]

More strongly, once a physical primitive relation is typed as the actual affine translation taking the first normalized state to the second, that displacement is unique.

Thus two admitted primitive descriptions of the same ordered endpoint pair `(x,z)` cannot represent two different intrinsic affine displacement vectors in the same comparison frame.

## 3. Parent 2 — local frame covariance

Let local orthonormal relation frames be `Q_x,Q_y in SO(3)`. Represent the intrinsic displacement in the target local frame by

\[
\mathbf e_{xy}^{(x)}
=Q_x^T(\mathbf r_y-\mathbf r_x).
\]

The exact frame comparison is

\[
\boxed{
R_{xy}=Q_x^TQ_y\in SO(3).
}
\]

Then

\[
\begin{aligned}
\mathbf e_{xy}^{(x)}
+R_{xy}\mathbf e_{yz}^{(y)}
&=Q_x^T(\mathbf r_y-\mathbf r_x)
+Q_x^TQ_yQ_y^T(\mathbf r_z-\mathbf r_y)\\
&=Q_x^T(\mathbf r_z-\mathbf r_x)\\
&=\mathbf e_{xz}^{(x)}.
\end{aligned}
\]

Hence pure local-frame re-expression preserves endpoint closure exactly.

This is the already validated pure-atlas baseline. Physical connection holonomy is admitted downstream and can carry rotational curvature.

## 4. Primitive same-endpoint admissibility condition

For a physical connection transporter `U_xy`, define

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

The existing relational endpoint-closure theorem gives the exact algebraic equivalence

\[
\boxed{
\mathcal T_{xyz}=-\mathcal C_{xyz}.
}
\]

Gate A3 applies the primitive relation typing as follows:

> If the direct relation `x -> z` and the connection-composed description `x -> y -> z` are admitted as two representations of the same primitive ordered endpoint relation in the same comparison frame, intrinsic affine displacement uniqueness selects equality of the two representations.

Therefore on this admitted sector

\[
\boxed{
\mathcal C_{xyz}=0
}
\]

and consequently

\[
\boxed{
\mathcal T_{xyz}=0.
}
\]

This is the discrete zero-torsion selection rule for primitive contractible endpoint comparisons.

## 5. A8 context firewall

A nonzero endpoint defect

\[
\mathcal C_{xyz}\ne0
\]

is not erased by Gate A3. It indicates that the composed connection description and direct primitive relation cannot both remain identified inside the same primitive comparison surface.

A8 provides the TIR context-lift route:

```text
same primitive endpoint representation
 -> C_xyz = 0
 -> spatial GR torsion-free sector

context-bearing mismatch
 -> C_xyz retained as typed defect
 -> broader Cartan/torsional sector
```

Thus Gate A3 selects the GR branch while preserving the already source-bound torsion observable for other admitted relational sectors.

## 6. Gate A2 continuum transfer

Gate A2 established, for a regular shrinking triangle family,

\[
\boxed{
\mathbf t_C
=\operatorname{vec}(\mathcal T_{xyz})
+(I-R_C)\mathbf e_{xz},
}
\]

with

\[
\mathbf e_{xz}=O(\epsilon),
\qquad
R_C-I=O(\epsilon^2),
\qquad
A_C=\Theta(\epsilon^2).
\]

Therefore the curvature correction to the translational loop is `O(epsilon^3)` and

\[
\boxed{
\frac{\mathbf t_C}{A_C}
-
\frac{\operatorname{vec}(\mathcal T_{xyz})}{A_C}
\to0.
}
\]

On an endpoint-compatible refining family,

\[
\mathcal T_{xyz}=o(A_C),
\]

so

\[
\boxed{
T^a=de^a+\omega^a{}_b\wedge e^b=0.
}
\]

This is the continuum zero-torsion transfer.

## 7. Metric compatibility

The local relational frame transport is induced by

\[
SU(2)\xrightarrow{\operatorname{Ad}}SO(3).
\]

For

\[
R\in SO(3),
\]

one has

\[
R^TR=I.
\]

Therefore the Hilbert--Schmidt / Euclidean relation metric is preserved under the real frame transport.

After the already established solder/tangent binding, the continuum spatial connection is metric-compatible:

\[
\boxed{D h=0}.
\]

## 8. Levi-Civita uniqueness

The fundamental theorem of Riemannian geometry states that on a smooth nondegenerate Riemannian metric carrier there exists a unique connection satisfying

\[
Dh=0
\]

and

\[
T=0.
\]

Gate A3 supplies these two conditions on the regular endpoint-compatible spatial refinement sector. Therefore

\[
\boxed{
D=D^{\rm LC}.
}
\]

Equivalently, in coordinates,

\[
\boxed{
\Gamma^k{}_{ij}
=\frac12 h^{k\ell}
\left(
\partial_i h_{j\ell}
+\partial_j h_{i\ell}
-\partial_\ell h_{ij}
\right).
}
\]

The connection is selected from the metric/coframe plus endpoint-compatibility conditions rather than introduced as an independent spatial GR object.

## 9. Zero torsion does not remove curvature

Gate A2 gives the required firewall. On the zero-torsion refinement sector it remains possible that

\[
\boxed{
\frac{R_C-I}{A_C}
\to\Omega(u,v)\ne0.
}
\]

Hence

\[
\boxed{
T^a=0,
\qquad
\Omega^a{}_b\ne0
}
\]

is an admitted and explicitly validated scaling regime.

At finite loop scale the translational loop may contain the curvature-suppressed term

\[
\mathbf t_C=(I-R_C)\mathbf e_{xz}=O(\epsilon^3),
\]

whose area-normalized contribution vanishes as the loop shrinks.

Therefore zero torsion does not remove curvature.

## 10. Global continuum existence firewall

Gate A3 proves selection on a declared regular refining family. The existence and global stability of such a family across the full TIR spatial complex remain separately typed.

The remaining global question is

\[
\boxed{
\text{Does the full relational cell complex admit a globally compatible smooth refinement carrying the selected local }D^{LC}?
}
\]

This is a topology/refinement existence problem, not a local torsion-selection problem.

Status:

`GLOBAL_CONTINUUM_EXISTENCE_OPEN`.

## 11. Updated spatial GR chain

\[
\boxed{
\begin{aligned}
&\mathbb C^2
\to\operatorname{Herm}_0(2)\cong\mathbb R^3
\to\mathcal E_{xy}
\to e^a
\to h\\
&\to W_{ij}^X / R_{ij}
\to \mathcal T_{xyz}
\to \text{Gate A2 Cartan limit}\\
&\to \text{primitive endpoint-compatible sector}
\to T^a=0
\to D^{LC}
\to \Omega^a{}_b / R^i{}_{jkl}.
\end{aligned}
}
\]

The next relativistic bridge is then

```text
local/refining Levi-Civita spatial GR sector
 + IDT temporal orientation/lapse
 -> four-dimensional Lorentzian/ADM carrier
 -> global continuum/covariance gate
 -> RFC RF-E21 Einstein-form selection
```

## 12. Claim ledger

| Claim | Status |
|---|---|
| affine endpoint displacement uniqueness | `EXACT PARENT TORSOR THEOREM` |
| same-frame affine endpoint composition | `EXACT PARENT` |
| local SO(3) frame re-expression preserves endpoint closure | `EXACT` |
| `T_xyz=-C_xyz` | `EXACT PARENT` |
| same primitive endpoint admissibility selects `C_xyz=0` | `EXACT CONDITIONAL SELECTION` |
| endpoint-compatible discrete sector has `T_xyz=0` | `EXACT` |
| Gate A2 carries area-normalized discrete torsion to Cartan `T^a` | `PASS CONDITIONAL REFINEMENT THEOREM` |
| endpoint-compatible regular refinement gives `T^a=0` | `PASS CONDITIONAL` |
| SO(3) transport preserves spatial metric | `EXACT` |
| metric compatibility + zero torsion selects Levi-Civita | `STANDARD EXACT THEOREM` |
| zero torsion retains possible nonzero curvature | `PASS FIREWALL` |
| global smooth refinement existence/stability | `OPEN` |
| broader context-lifted torsional Cartan sector | `RETAINED TYPED BRANCH` |

## 13. Validation authority

Reference validator:

`TIR/foundations/validation/tir_zero_torsion_levi_civita_selection_v0_1.py`

Static receipt:

`TIR/foundations/validation/TIR_ZERO_TORSION_LEVI_CIVITA_SELECTION_V0_1.json`

Hosted gate:

`.github/workflows/tir-spatial-gr-levi-civita.yml`

The hosted gate reruns both Gate A2 and Gate A3 on the same exact PR head.

Verdict target:

`PASS_TIR_ZERO_TORSION_LEVI_CIVITA_SELECTION`.
