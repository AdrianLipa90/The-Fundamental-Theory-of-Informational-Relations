# TIR 36 -> 20 + 6 + 10 Gravity-Relevance Split v0.1

Status: EXACT_LINEAR_GEOMETRIC_DECOMPOSITION / PHYSICAL_DYNAMICS_OPEN  
Date: 2026-09-24

## 1. Input from the bivector gate

The moire/bivector bridge supplies the exact local decomposition

\[
\operatorname{Mat}_6
=
\mathfrak{co}(3,3)\oplus\mathcal Q,
\]

with

\[
36=16+20.
\]

The 20-dimensional \(\mathcal Q\) sector is the non-tetradic/simplicity-defect sector.

The 16-dimensional geometric sector is locally identified through the exterior-square representation with

\[
\mathfrak{gl}(4).
\]

This note decomposes that 16-dimensional sector into frame gauge and metric-changing directions.

## 2. Metric adjoint

Let \(g\) be the admitted nondegenerate local metric. For a frame generator

\[
H\in\mathfrak{gl}(4),
\]

define the metric adjoint

\[
H^{\dagger_g}=g^{-1}H^Tg.
\]

Then define

\[
\boxed{
H_{\rm L}
=
\frac12(H-H^{\dagger_g})
}
\]

and

\[
\boxed{
H_{\rm M}
=
\frac12(H+H^{\dagger_g}).
}
\]

They satisfy

\[
H=H_{\rm L}+H_{\rm M},
\]

\[
H_{\rm L}^{\dagger_g}=-H_{\rm L},
\qquad
H_{\rm M}^{\dagger_g}=H_{\rm M}.
\]

For Lorentzian signature,

\[
\dim H_{\rm L}=6,
\qquad
\dim H_{\rm M}=10.
\]

Therefore

\[
\boxed{
16=6+10.
}
\]

Together with the 20-dimensional bivector simplicity defect,

\[
\boxed{
36
=
20_{\rm defect}
+
6_{\rm Lorentz\ gauge}
+
10_{\rm metric}.
}
\]

## 3. First metric variation

Let the vector frame transform infinitesimally as

\[
E\mapsto (I+\varepsilon H)E.
\]

The corresponding metric changes to first order by

\[
\boxed{
\delta g
=
-\left(H^Tg+gH\right).
}
\]

Using the metric-adjoint split,

\[
\boxed{
\delta g
=
-2gH_{\rm M}.
}
\]

Hence

\[
\delta g[H_{\rm L}]=0.
\]

The six metric-antisymmetric directions are local Lorentz frame gauge at this linear level. Only the ten metric-symmetric directions can change the local metric.

This is the gravity-relevance firewall:

- 20D defect: not an admitted tetrad deformation;
- 6D Lorentz sector: admitted frame motion but metric-invisible locally;
- 10D symmetric sector: admitted metric deformation.

## 4. Canonical tetra-frame metric

For the rational tetrahedral null-frame chart,

\[
g_T
=
\operatorname{diag}
\left(
1,-\frac13,-\frac13,-\frac13
\right).
\]

The validator constructs an exact rational boost generator satisfying

\[
H_{\rm boost}^Tg_T+g_TH_{\rm boost}=0
\]

and verifies

\[
\delta g=0.
\]

It separately constructs a diagonal strain and verifies a nonzero metric variation.

A generic rational \(H\) is reconstructed exactly from the two sectors, and its first metric variation is reproduced entirely by \(H_{\rm M}\).

## 5. Relation to moire hyperlayers

The local chain is now

\[
\boxed{
M_{36}
\to
(Q_{20},H_{16})
\to
(Q_{20},H_{\rm L}^{(6)},H_{\rm M}^{(10)}).
}
\]

Only after the 20D defect is admitted/rejected and the 6D frame gauge is quotiented does the 10D metric-changing sector remain as a candidate gravitational variable.

This does not yet give Einstein dynamics. It isolates the correct local degrees on which any source/dynamics law must act.

## 6. Next gate

The remaining problem is no longer "how does 36D become a metric?" at the linear representation level.

It is:

\[
\boxed{
\text{TIR/moire source law}
\longrightarrow
H_{\rm M}^{(10)}(x)
\longrightarrow
g_{\mu\nu}(x)
\longrightarrow
R[g].
}
\]

A physical theory must specify:

1. the evolution/source equation for the 10D metric-changing field;
2. constraints/conservation laws;
3. dimensional normalization including \(G\);
4. equivalence with or deviations from Einstein dynamics;
5. held-out phenomenology.

## 7. Promotion ledger

- Mat6 = co(3,3) + 20D defect: PASS EXACT (upstream)
- gl(4) metric-adjoint split: PASS EXACT
- 16 = 6 + 10: PASS EXACT
- 36 = 20 + 6 + 10: PASS EXACT
- Lorentz-sector first metric variation = 0: PASS EXACT
- symmetric-sector carries full first metric variation: PASS EXACT
- metric dynamics/source equation: OPEN
- Einstein equations derived from pre-geometric law: OPEN
- physical normalization/G: OPEN
