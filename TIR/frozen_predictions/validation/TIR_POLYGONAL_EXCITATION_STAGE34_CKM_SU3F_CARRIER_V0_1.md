# TIR Polygonal Excitation — Stage 34 CKM as an SU(3)_F Carrier Transformation v0.1

Status: `STAGE_34_CKM_SU3F_REPRESENTATION_PASS`

## Family carrier

Stages 21, 24 and 25 establish an ordered three-dimensional family-label space

```math
V_F\cong\mathbb C^3
```

identified at label level with

```math
(s_1,s_2,s_3)=((3,5),(5,7),(11,13)).
```

The color factor `SU(3)_C` acts independently.

## Generic CKM parameterization

For arbitrary real angles `theta12, theta23, theta13` and phase `delta`, define

```math
R_{12}=\begin{pmatrix}
c_{12}&s_{12}&0\\
-s_{12}&c_{12}&0\\
0&0&1
\end{pmatrix},
```

```math
R_{13}(\delta)=\begin{pmatrix}
c_{13}&0&s_{13}e^{-i\delta}\\
0&1&0\\
-s_{13}e^{i\delta}&0&c_{13}
\end{pmatrix},
```

and

```math
R_{23}=\begin{pmatrix}
1&0&0\\
0&c_{23}&s_{23}\\
0&-s_{23}&c_{23}
\end{pmatrix}.
```

Each factor obeys

```math
R_{ij}^\dagger R_{ij}=I_3,
\qquad
\det R_{ij}=1.
```

Therefore

```math
\boxed{
V_F=R_{23}R_{13}(\delta)R_{12}\in SU(3)_F.
}
```

This statement is independent of the numerical choice of mixing angles.

## Seed-label representation

Let `M_s` be the Stage 24 map from the ordered TIR seed basis to the exceptional family-triplet basis. The same transformation on the seed labels is

```math
V_{seed}=M_s^\dagger V_F M_s.
```

With the current ordered-basis convention `M_s=I_3`, so `V_seed=V_F`.

## Independence from color

On a color-family product carrier,

```math
V_C\otimes V_F,
```

a color transformation and family mixing act as

```math
G_C\otimes I_F,
\qquad
I_C\otimes V_F.
```

Hence

```math
\boxed{[G_C\otimes I_F,I_C\otimes V_F]=0}
```

for every `G_C in SU(3)_C` and every CKM-form `V_F in SU(3)_F`.

## Existing structural candidate

Using the Stage 33 endpoint dictionary

```math
a=\frac27,\qquad b=\frac29,\qquad c=\frac25,
```

with

```math
\lambda=b+a\kappa,
\qquad
|V_{cb}|=\frac{a^2}{2},
\qquad
|V_{ub}|=\frac{a^2bc}{2},
\qquad
\delta=\arccos c,
```

the numerical carrier has

```text
max unitarity residual = 2.220446049250313e-16
|det(V)-1| = 2.220446049522218e-16
color-family commutator residual = 0.0
```

so the candidate lies on the derived family carrier to numerical precision and commutes with the independent color action.

## Result

The exceptional threefold carrier supplies an explicit representation space for quark-family mixing. CKM-type transformations live in `SU(3)_F` and are mathematically independent of the `SU(3)_C` holonomic gluon action.

Stage 32 continues to govern the predictive status of the existing angle formulas; Stage 34 establishes their group-theoretic home.

## Reproducibility closure

Executable:

`TIR/frozen_predictions/validation/scripts/ckm_su3f_stage34_v01.py`

Append-only receipt:

`TIR/frozen_predictions/validation/results/TIR_POLYGONAL_STAGE34_CKM_SU3F_CARRIER_RECEIPT_V0_1.json`

The exact committed source was replayed in the assistant-local Python environment with return code `0`. The receipt records the input invariants, the `SU(3)_F` unitarity and determinant checks, and the exact zero commutator for the deterministic color-cycle witness.
