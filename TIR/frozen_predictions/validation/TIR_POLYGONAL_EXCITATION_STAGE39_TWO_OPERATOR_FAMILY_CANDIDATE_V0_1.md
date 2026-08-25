# TIR Polygonal Excitation — Stage 39 Frozen Two-Operator Family Candidate v0.1

Status: `STAGE_39_STRUCTURAL_CANDIDATE_FROZEN`

## Scope

This stage freezes a minimal two-operator family candidate before any target-matrix comparison in this gate.

The construction uses only structures already present on the polygonal/McKay branch:

1. the local geometry coordinates `c3,c4,c5`;
2. the canonical `C3` character matrix `F3` from Stage 38;
3. the endpoint ratios `a=2/7` and `b=2/9` recorded in Stage 33.

No observed CKM entries, observed masses, or fitted coefficients are read by the executable.

The candidate is retained as a structural freeze. Its physical sector assignment remains open and both assignments are preserved.

## Primary family axis

Use the Stage 1 / Stage 13 local geometric values

```math
D=\operatorname{diag}\left(-\frac13,0,\frac1{\sqrt5}\right).
```

Let

```math
C=F_3 D F_3^\dagger.
```

The operators `D` and `C` are Hermitian and do not commute.

## Endpoint weights

Stage 33 supplies the frozen endpoint ratios

```math
a=\frac27,
\qquad
b=\frac29.
```

Define the lowest-order affine Hermitian family candidate

```math
\boxed{
H(\alpha)=D+\alpha C.
}
```

Both sector assignments are retained:

```text
A: alpha_u=a, alpha_d=b
B: alpha_u=b, alpha_d=a
```

No assignment is selected by comparison to a target matrix.

## Primary output

For assignment A,

```math
H_u=H(a),
\qquad
H_d=H(b),
```

and

```text
max |[H_u,H_d]| = 0.011206297974936162.
```

The relative eigenbasis transformation is unitary with

```text
max |V^dagger V-I| = 4.44e-16
|det(V)-1| = 1.04e-17.
```

Its magnitude matrix is frozen as

```math
|V_A|\approx
\begin{pmatrix}
0.999154&0.037478&0.016961\\
0.037354&0.998774&0.032476\\
0.017232&0.032332&0.999329
\end{pmatrix}.
```

The family CP invariant is

```math
\boxed{J_A=-2.0174220730068447\times10^{-5}.}
```

For assignment B the magnitude matrix is transposed at the displayed precision and

```math
\boxed{J_B=+2.0174220730068325\times10^{-5}.}
```

Thus the assignment exchange reverses the orientation sign while preserving the mixing scale.

## Robustness controls

Two additional already frozen family axes are evaluated without target selection:

```text
D_N = diag(3,4,5)
D_ADE = diag(7,8,9)
```

The latter differs from the former by an additive identity shift and therefore has the same eigenvectors. Both give

```math
|J|\approx2.0366945594\times10^{-5}
```

and the same magnitude matrix to numerical precision:

```math
|V|\approx
\begin{pmatrix}
0.999259&0.034407&0.017227\\
0.034407&0.998815&0.034407\\
0.017227&0.034407&0.999259
\end{pmatrix}.
```

The non-zero CP invariant and near-identity hierarchy therefore do not depend on the irrational `c5=1/sqrt(5)` coordinate alone.

## Evidential status

```text
candidate frozen before target comparison in this gate: YES
non-commuting Hermitian pair: YES
unitary relative transformation: YES
non-zero family CP invariant: YES
continuous fitted coefficient: NONE
physical up/down assignment: OPEN
predictive status: FROZEN STRUCTURAL CANDIDATE IN POSTDICTION CONTEXT
```

The last status reflects the existing project history: CKM observables were already known elsewhere in TIR before this branch was constructed.

## Reproducibility

Executable:

`TIR/frozen_predictions/validation/scripts/two_operator_family_candidate_stage39_v01.py`

Receipt:

`TIR/frozen_predictions/validation/results/TIR_POLYGONAL_STAGE39_TWO_OPERATOR_FAMILY_CANDIDATE_RECEIPT_V0_1.json`

## Next gate

After preserving this freeze unchanged, compare the Stage 39 output to the existing CKM construction only as a retrospective diagnostic. Retain all disagreements. The comparison must separately score the three mixing magnitudes, the full matrix shape, and the CP invariant rather than selecting between assignments or axes by best fit.
