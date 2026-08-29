# TIR SE(3) Anchor-Source Binding v0.1

Status: `CANDIDATE_THEOREM / GREMLIN_SOURCE_BINDING_GATE`

## 1. Parent carrier

The local TIR geometry uses the real affine translation carrier

\[
V=\operatorname{Herm}_0(2)\cong\mathbb R^3
\]

with Pauli-coordinate endpoint relation

\[
\mathcal E_{xy}
=(\mathbf r_y-\mathbf r_x)\cdot\boldsymbol\sigma.
\]

RF/TIR global gluing has now introduced affine transport

\[
G_{ba}=(R_{ba},t_{ba})\in SE(3).
\]

This gate asks when the translational component `t_ba` is fixed directly by ordinary overlapping affine charts.

## 2. Anchored local frames

Let chart `a` be specified by:

- an anchor Bloch/Pauli coordinate `r_a`;
- an orthonormal frame matrix `Q_a in SO(3)`.

For a common carrier point with Pauli coordinate `r`, define chart coordinates

\[
\boxed{x_a:=Q_a^T(\mathbf r-\mathbf r_a).}
\]

Likewise,

\[
\boxed{x_b:=Q_b^T(\mathbf r-\mathbf r_b).}
\]

Eliminating `r` gives

\[
\boxed{
x_b
=Q_b^TQ_a x_a
+Q_b^T(\mathbf r_a-\mathbf r_b).
}
\]

Therefore the exact overlap transition is

\[
\boxed{
R_{ba}=Q_b^TQ_a,
\qquad
t_{ba}=Q_b^T(\mathbf r_a-\mathbf r_b).
}
\]

The translational carrier is thus source-bound to the TIR endpoint relation between the two chart anchors, expressed in the target chart frame.

## 3. Relation crosswalk

The anchor relation is

\[
\mathcal E_{ba}
=(\mathbf r_a-\mathbf r_b)\cdot\boldsymbol\sigma.
\]

If `vec` denotes extraction of the Pauli coefficient vector, then

\[
\boxed{
t_{ba}=Q_b^T\operatorname{vec}(\mathcal E_{ba}).}
\]

Thus the source map is typed

```text
TIR endpoint relation E_ba
 + target local frame Q_b
 -> affine translation t_ba.
```

No independent translational degree of freedom is needed for a pure chart change on one common affine carrier.

## 4. Exact cocycle theorem

For three anchored frames `a,b,c`,

\[
R_{cb}R_{ba}
=Q_c^TQ_bQ_b^TQ_a
=Q_c^TQ_a
=R_{ca}.
\]

For the translation,

\[
\begin{aligned}
R_{cb}t_{ba}+t_{cb}
&=Q_c^TQ_bQ_b^T(\mathbf r_a-\mathbf r_b)
+Q_c^T(\mathbf r_b-\mathbf r_c)\\
&=Q_c^T(\mathbf r_a-\mathbf r_c)\\
&=t_{ca}.
\end{aligned}
\]

Hence

\[
\boxed{G_{cb}G_{ba}=G_{ca}.}
\]

This is the exact `SE(3)` Čech/atlas cocycle on an ordinary common affine overlap.

## 5. Inverse theorem

Exchanging the two charts gives

\[
R_{ab}=R_{ba}^{-1},
\]

and

\[
t_{ab}=-R_{ba}^{-1}t_{ba}.
\]

Therefore

\[
\boxed{G_{ab}=G_{ba}^{-1}.}
\]

## 6. Pure-atlas loop firewall

For a closed sequence of exact overlap transitions on one common affine carrier,

\[
a_0\to a_1\to\cdots\to a_n=a_0,
\]

repeated cocycle composition gives

\[
\boxed{G_C=G_{a_0a_0}=e_{SE(3)}.}
\]

Therefore ordinary coordinate re-expression of one common affine carrier has trivial affine loop holonomy.

This yields the firewall

\[
\boxed{
\text{PURE ATLAS GLUING}
\Longrightarrow
G_C=e_{SE(3)}.
}
\]

A nontrivial loop witness

\[
G_C\ne e_{SE(3)}
\]

must therefore enter through an additional path-dependent connection/transport structure, a nontrivial gluing obstruction, or another explicitly source-bound departure from the pure-atlas hypothesis.

## 7. GREMLIN XFI.01 crosslink

GREMLIN candidate XFI.01 identifies the exact-coboundary/trivial-holonomy pattern. The present TIR source binding realizes the same structural firewall in the affine `SE(3)` chart sector:

```text
anchor difference = exact affine coboundary
 -> transition translation t_ba
 -> cocycle composition
 -> trivial closed pure-atlas holonomy.
```

The correspondence is used as a theorem-organizing crosslink; its promotion here rests on the direct affine derivation above rather than on GREMLIN authority.

## 8. Connection-holonomy frontier

The TIR global geometry programme therefore separates two transport layers:

```text
ATLAS TRANSITION
  G_ba^atlas=(Q_b^TQ_a, Q_b^T(r_a-r_b))
  -> exact cocycle
  -> trivial loop holonomy

CONNECTION TRANSPORT
  U_ba[path]
  -> path composition
  -> potentially nontrivial loop holonomy
  -> curvature/torsion candidate carriers
```

This prevents coordinate-frame mismatch from being counted as physical curvature.

## 9. Infinitesimal affine-frame rate and ADM shift candidate

Consider a smooth one-parameter family of anchored affine frames with

\[
Q(x^0+dx^0)^TQ(x^0)
=I+\Omega\,dx^0+O((dx^0)^2),
\]

where `Omega` is antisymmetric, and

\[
t(x^0+dx^0,x^0)
=v\,dx^0+O((dx^0)^2).
\]

Then the infinitesimal coordinate identification is

\[
\boxed{
\frac{dx^i}{dx^0}
=v^i+\Omega^i{}_j x^j.
}
\]

This supplies a precise candidate affine contribution to an ADM shift field,

\[
\boxed{
b^i_{\rm affine}(x)=v^i+\Omega^i{}_j x^j,}
\]

on a local affine frame patch.

Its use as the physical/canonical RFC shift source remains a separate cross-repository realization gate because general ADM shift freedom extends beyond rigid affine-frame transport.

## 10. Claim ledger

| Statement | Status |
|---|---|
| anchored chart transition formula | EXACT AFFINE ALGEBRA |
| `t_ba=Q_b^T vec(E_ba)` | EXACT TIR SOURCE BINDING ON COMMON CARRIER |
| `G_cb G_ba=G_ca` | EXACT COCYCLE |
| `G_ab=G_ba^-1` | EXACT |
| pure-atlas closed loop is identity | EXACT |
| nontrivial holonomy requires departure from pure-atlas transition | EXACT CONDITIONAL FIREWALL |
| XFI.01 structural crosslink | GREMLIN-SUGGESTED / DIRECTLY RE-DERIVED HERE |
| infinitesimal rigid-affine rate `v+Omega x` | EXACT LOCAL KINEMATICS |
| identification with full RFC ADM shift | CROSS-REPO CANDIDATE / GATED |
| curvature/torsion physical realization | DOWNSTREAM GATE |

## 11. Validation target

The deterministic gate must verify:

1. exact anchored coordinate transformation;
2. pair inverse;
3. three-chart cocycle;
4. arbitrary finite pure-atlas loop identity;
5. randomized anchor/frame tests;
6. infinitesimal affine generator finite-difference convergence;
7. explicit firewall showing a manually added non-coboundary translation breaks the pure-atlas loop identity.

Verdict target:

`PASS_TIR_SE3_ANCHOR_SOURCE_BINDING`.
