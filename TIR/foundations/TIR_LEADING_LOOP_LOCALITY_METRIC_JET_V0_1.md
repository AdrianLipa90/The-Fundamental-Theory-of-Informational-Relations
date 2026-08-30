# TIR Leading-Loop Locality and Metric-Jet Selection v0.1

Status: `EXACT_LEADING_SMALL_LOOP_SCALING / LEADING_REFINEMENT_CARRIER_SELECTION_CONDITIONAL / SECOND_ORDER_METRIC_JET_BOUND_PASS_ON_SELECTION / HIGHER_JET_SECTORS_RETAINED`

Date: 2026-08-30

## 1. Purpose

Gate A2 separated Cartan torsion from rotational curvature in the controlled small-loop limit. Gate A3 selected the local torsion-free, metric-compatible Levi-Civita spatial-GR sector. Gate A4 asks the next question needed by RFC RF-E21:

\[
\boxed{\text{Which differential order is carried by the primitive local continuum geometry?}}
\]

The answer is split into two layers:

1. an exact smooth-small-loop scaling theorem;
2. a TIR leading-refinement selection rule that promotes the lowest finite nonzero covariant loop coefficient as the primitive local continuum carrier.

Higher-jet data remain available as typed extended/correction sectors.

## 2. Parent curvature expansion

For a regular shrinking contractible loop `C_epsilon` with characteristic edge scale `epsilon`, Gate A2 supplies

\[
A_C=\Theta(\epsilon^2)
\]

and the smooth connection-holonomy expansion

\[
\boxed{
R_C
=I+A_C\,\Omega(u,v)+O(\epsilon^3).
}
\]

Equivalently,

\[
\boxed{
\frac{R_C-I}{A_C}
=\Omega(u,v)+O(\epsilon).
}
\]

Therefore

\[
\boxed{
\lim_{\epsilon\to0}
\frac{R_C-I}{A_C}
=\Omega(u,v).
}
\]

The curvature two-form is the leading finite nonzero rotational loop coefficient after area normalization.

## 3. Higher-jet scaling

For a smooth connection, variation of curvature across the loop enters at one additional edge power. Schematically,

\[
R_C
=I
+A_C\Omega
+O(\epsilon A_C\nabla\Omega)
+O(A_C^2\Omega^2)
+\cdots.
\]

Since `A_C=Theta(epsilon^2)`, the first derivative-of-curvature contribution is

\[
O(\epsilon^3),
\]

and after area normalization it is

\[
\boxed{O(\epsilon)\to0.}
\]

A second derivative of curvature enters at still higher order. Thus the hierarchy is

```text
area-normalized leading loop coefficient     -> Omega
next edge order                              -> nabla Omega
higher edge orders                           -> higher curvature jets
```

The normalized refinement limit separates the curvature carrier from its higher jets by scaling order.

## 4. Leading Refinement Rule

Gate A4 introduces the following typed TIR selection rule.

### LRR — Leading Refinement Rule

For a local geometric observable defined by a regular shrinking relational loop family, the primitive continuum carrier is the lowest normalization order that yields a finite, nonzero, frame-covariant refinement limit.

For rotational connection transport this gives

\[
\boxed{
\mathcal J_0(u,v)
:=\lim_{\epsilon\to0}\frac{R_C-I}{A_C}
=\Omega(u,v).
}
\]

Data that vanish under this normalization but become finite only after an additional inverse power of `epsilon` are typed as higher-jet/extended carriers.

The LRR is the TIR selection step. Its mathematical scaling consequences are exact once the regular smooth refinement hypotheses hold.

## 5. Relation to TIR minimality

A1 supplies point minimality and A3 types physical structure through informational relations. The established spatial branch then builds local geometry from the smallest nontrivial relation loops and their refinement limits.

The LRR is the differential-geometric continuation of that minimal-carrier programme:

```text
primitive point/relation
 -> smallest contractible relation loop
 -> lowest finite covariant normalized loop coefficient
 -> primitive continuum geometric carrier
```

This inheritance is recorded as a TIR structural selection rule. The independent mathematical statement remains the small-loop scaling theorem above.

## 6. Levi-Civita metric-jet consequence

Gate A3 selects, on the regular endpoint-compatible spatial-GR sector,

\[
T^a=0,
\qquad
Dh=0,
\qquad
D=D^{LC}.
\]

The Levi-Civita coefficients are

\[
\Gamma^k{}_{ij}
=\frac12h^{k\ell}
(\partial_i h_{j\ell}+\partial_j h_{i\ell}-\partial_\ell h_{ij}),
\]

so the connection is first order in the metric. Its curvature is

\[
\Omega=d\omega+\omega\wedge\omega,
\]

hence depends locally on

\[
\boxed{h,\partial h,\partial^2 h.}
\]

Under LRR, the primitive local geometric data are therefore the metric/coframe plus curvature, with no independent `nabla Omega` carrier at leading refinement order.

Thus the primitive local metric operator class is bounded to second metric jet order:

\[
\boxed{
\mathcal E_{\mu\nu}
=\mathcal E_{\mu\nu}(g,\partial g,\partial^2g)
}
\]

for the leading GR-selection sector.

## 7. Curvature powers and the Lovelock firewall

LRR by itself selects the differential jet order. It does not by itself choose a unique rank-two tensor from all algebraic contractions of `g` and curvature.

That remaining selection is exactly the role of RFC RF-E21:

```text
4D Lorentzian metric carrier
+ natural symmetric rank-2 operator
+ dependence through metric jets up to order two
+ covariant divergence-free selection
 -> 4D Lovelock tensor classification
 -> A G_mn + B g_mn
```

Thus Gate A4 supplies the project-owned second-order/locality premise while RF-E21 supplies the standard uniqueness theorem.

## 8. Higher-jet sector retention

Higher refinement coefficients remain typed as extended geometric data:

\[
\nabla\Omega,
\quad
\nabla^2\Omega,
\quad\ldots
\]

and may support finite-scale, effective or ultraviolet correction sectors when separately sourced.

The leading GR branch is selected by LRR through the lowest finite nonzero normalized carrier.

This gives the hierarchy

```text
leading continuum geometry       -> g, Omega
higher refinement corrections    -> nabla Omega, nabla^2 Omega, ...
```

without conflating the two levels.

## 9. Four-dimensional transfer

RFC RF-G0 and RF-E8 combine the TIR spatial carrier with IDT temporal orientation/lapse into a local Lorentzian four-metric. Once the global smooth join is admitted, the same local jet argument applies to the four-dimensional Levi-Civita curvature:

\[
\boxed{
\Omega^{AB}
=d\omega^{AB}+\omega^A{}_C\wedge\omega^{CB}
}
\]

and the leading metric-side operator remains a natural second-order metric-jet object.

The global smooth-refinement/gluing existence gate remains separately tracked.

## 10. Claim ledger

| Claim | Status |
|---|---|
| `R_C=I+A_C Omega+O(epsilon^3)` on smooth regular loop family | `STANDARD SMALL-LOOP EXPANSION / A2 PARENT` |
| `(R_C-I)/A_C -> Omega` | `PASS EXACT CONDITIONAL LIMIT` |
| first curvature-derivative correction is area-normalized `O(epsilon)` | `PASS SMOOTH SCALING` |
| higher curvature jets occupy higher refinement orders | `PASS SMOOTH JET EXPANSION` |
| LRR selects lowest finite nonzero covariant refinement coefficient | `TIR STRUCTURAL SELECTION RULE` |
| LRR selects `Omega` as primitive rotational continuum carrier | `PASS ON LRR` |
| A3 Levi-Civita curvature uses metric jets through order two | `STANDARD EXACT DIFFERENTIAL GEOMETRY` |
| leading GR metric operator class is second metric jet order | `PASS ON LRR + A3` |
| higher-jet sectors remain typed extended carriers | `RETAINED` |
| unique 4D divergence-free rank-two tensor form | `RFC RF-E21 THEOREM GATE` |
| global four-dimensional smooth refinement/gluing | `OPEN CROSS-REPOSITORY GATE` |

## 11. Updated GR dependency line

```text
TIR affine relation
 -> Cartan refinement                                      PASS A2
 -> zero torsion + Levi-Civita                            PASS A3
 -> leading loop / area -> curvature Omega               PASS A4 MATH
 -> LRR minimal refinement selection                     TIR SELECTION
 -> metric jet order <= 2                                PASS ON LRR
 + IDT temporal carrier
 -> local 4D Lorentzian metric
 -> RFC RF-E21 Lovelock uniqueness
 -> divergence-free operator binding
 -> Einstein tensor form
 -> RF-E3 coupling normalization
```

## 12. Validation authority

Deterministic validator:

`TIR/foundations/validation/tir_leading_loop_locality_metric_jet_v0_1.py`

Static receipt:

`TIR/foundations/validation/TIR_LEADING_LOOP_LOCALITY_METRIC_JET_V0_1.json`

Hosted workflow:

`.github/workflows/tir-leading-loop-locality-metric-jet.yml`

Verdict target:

`PASS_TIR_LEADING_LOOP_LOCALITY_METRIC_JET_SELECTION`.
