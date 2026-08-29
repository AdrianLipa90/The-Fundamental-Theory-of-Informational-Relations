# TIR SE(3) Global Gluing and Affine Holonomy v0.1

Status: `CANDIDATE_THEOREM / GREMLIN_PROMOTION_GATE`

Source state:

```text
TIR main integration frontier: 2026-08-29
GREMLIN role: candidate discovery only
runtime_execution_authority = false
canon_write_authority = false
```

## 1. Problem

The local spatial branch supplies a three-real-dimensional affine translation carrier

\[
V=\operatorname{Herm}_0(2)\cong\mathbb R^3
\]

and a local regular tetrahedral cell. Existing TIR transport links `W_ij` carry rotational/projective frame information through `SO(3)` or its `SU(2)` lift.

For global gluing, a transition between two local affine carriers must transport both:

1. orientation / frame basis;
2. affine origin / displacement.

A rotational link alone therefore does not contain the full affine gluing datum.

## 2. Minimal affine transport carrier

Let a transition from local frame `a` to local frame `b` be

\[
\boxed{G_{ba}=(R_{ba},t_{ba})\in SE(3)=\mathbb R^3\rtimes SO(3),}
\]

acting on local coordinates by

\[
\boxed{x_b=R_{ba}x_a+t_{ba}.}
\]

The rotational component is the `SO(3)` image of the admitted TIR `SU(2)` transport when such a lift is used:

\[
W_{ba}^{X}\in SU(2)
\xrightarrow{\operatorname{Ad}}
R_{ba}\in SO(3).
\]

The affine component `t_ba` is an additional typed carrier sourced by endpoint displacement/gluing data.

## 3. Exact semidirect-product composition

For

\[
G_1=(R_1,t_1),\qquad G_2=(R_2,t_2),
\]

successive transport gives

\[
G_2\circ G_1
=
\boxed{(R_2R_1,\;R_2t_1+t_2)}.
\]

The inverse is

\[
\boxed{G^{-1}=(R^{-1},-R^{-1}t).}
\]

These relations are exact consequences of affine-map composition.

## 4. Path and loop holonomy

For an oriented path

\[
\gamma:a_0\to a_1\to\cdots\to a_n,
\]

define

\[
\boxed{G_\gamma
=G_{a_na_{n-1}}\cdots G_{a_2a_1}G_{a_1a_0}.}
\]

For a closed loop `C` based at `a_0`,

\[
\boxed{G_C=(R_C,t_C)\in SE(3).}
\]

Exact affine closure is

\[
\boxed{G_C=e_{SE(3)}\iff R_C=I\ \text{and}\ t_C=0.}
\]

Thus the universal loop has two separately typed closure channels:

```text
rotational closure defect     R_C != I
translational closure defect  t_C != 0
```

## 5. Gauge/frame covariance

Let each local affine frame be changed by

\[
H_a=(Q_a,s_a)\in SE(3).
\]

Then transition functions transform as

\[
\boxed{G'_{ba}=H_bG_{ba}H_a^{-1}.}
\]

For a loop based at `a_0`, all internal frame changes telescope:

\[
\boxed{G'_C=H_{a_0}G_CH_{a_0}^{-1}.}
\]

Therefore the statement

\[
G_C=e_{SE(3)}
\]

is frame invariant.

The rotational loop datum transforms by conjugation,

\[
R'_C=Q_{a_0}R_CQ_{a_0}^{-1},
\]

so its conjugacy class and rotation angle are invariant.

## 6. Pure translational-holonomy sector

When

\[
\boxed{R_C=I,}
\]

the loop is a pure translation

\[
G_C=(I,t_C).
\]

Under an arbitrary base-frame change,

\[
t'_C=Q_{a_0}t_C,
\]

hence

\[
\boxed{\|t'_C\|=\|t_C\|.}
\]

Therefore the nonzero scalar

\[
\boxed{\tau_C:=\|t_C\|}
\]

is a base-frame-invariant affine closure defect in the rotationally closed sector.

This is the clean candidate carrier for a discrete torsion witness. Physical promotion as torsion requires an explicit TIR coframe/source binding and a continuum/discrete correspondence validator.

## 7. Rotational-only insufficiency theorem

Suppose only the rotational links `R_ba` (equivalently the `SO(3)` shadows of `W_ba`) are retained.

Choose a loop with

\[
R_{ba}=I
\]

on every edge. Then all rotational Wilson products are identical:

\[
R_C=I.
\]

Yet two affine realizations may have

\[
\sum_C t_e=0
\]

or

\[
\sum_C t_e\ne0.
\]

Both realizations have exactly the same rotational transport data but different affine loop holonomy.

Hence

\[
\boxed{
\{R_{ba}\}\ \text{alone does not determine}\ G_C\in SE(3).
}
\]

In particular, a translational closure defect cannot be reconstructed from rotational `W_ij` data alone.

This forces an additional affine displacement/coframe carrier into any TIR global-gluing programme that aims to resolve translational loop closure.

## 8. GREMLIN dependency refinement

The earlier candidate chain

```text
Delta3 -> E_ij -> W_ij -> W_loop -> closure defect -> curvature/torsion
```

is refined to the typed graph

```text
Delta3
 -> E_ij local affine displacement
 -> [R_ij , t_ij]
 -> G_ij in SE(3)
 -> G_loop = (R_loop,t_loop)
 -> rotational conjugacy class                [curvature candidate]
 -> pure-translation norm when R_loop = I     [torsion candidate]
```

with

```text
W_ij^X -> Ad(W_ij^X)=R_ij
E_ij / gluing displacement -> t_ij
```

The two source channels must be validated independently before joint promotion.

## 9. Claim ledger

| Statement | Status |
|---|---|
| `SE(3)=R^3 rtimes SO(3)` affine transport | STANDARD EXACT |
| composition `(R2R1,R2 t1+t2)` | EXACT |
| inverse `(R^-1,-R^-1 t)` | EXACT |
| loop closure iff `R_C=I` and `t_C=0` | EXACT |
| local-frame changes act by loop conjugation | EXACT |
| `||t_C||` invariant when `R_C=I` | EXACT |
| rotational links alone cannot determine affine loop closure | EXACT INSUFFICIENCY THEOREM |
| `R_C` as TIR discrete curvature realization | CANDIDATE / REQUIRES PHYSICAL BINDING |
| `||t_C||` as TIR discrete torsion realization | CANDIDATE / REQUIRES COFRAME BINDING |
| continuum Einstein-Cartan correspondence | OPEN DOWNSTREAM GATE |

## 10. Promotion gate

Promotion requires all of:

1. deterministic verification of `SE(3)` composition and inverse;
2. loop identity closure test;
3. local-frame conjugation test;
4. pure-translation norm invariance test;
5. explicit rotational-only insufficiency counterexample;
6. source binding `W_ij -> R_ij` and `E_ij/gluing -> t_ij`;
7. a separate physical theorem before the words curvature/torsion are promoted from candidate carriers to TIR physical results.

Verdict target:

`PASS_TIR_SE3_AFFINE_HOLONOMY_ALGEBRAIC_GATE`.
