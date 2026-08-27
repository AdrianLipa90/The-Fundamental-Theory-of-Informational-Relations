# TIR Polygonal Excitation — Stage 66 Stationary Selector Derivation v0.1

Status: `STAGE_66_UNIQUE_STATIONARY_SELECTOR_PASS_WITH_SADDLE_CLASSIFICATION`

Parent freeze: `TIR_POLYGONAL_STAGE65_STATIONARY_ORDERED_AXIS_CUBIC_SELECTOR_FREEZE_V0_1.md`

## Purpose

Stage 65 froze, before validation, the projectively normalized cubic family functional

```math
\mathcal F_\eta(S)=I_{iso}(S)+\eta I_{A5}(S)
```

with the constrained-stationarity condition

```math
\nabla\mathcal F_\eta(D_0)=\lambda D_0.
```

Stage 66 solves that frozen condition, classifies the constrained Hessian, and only afterwards compares its eigendirections with the independently frozen `C3` orbit of `A_seed`.

No CKM entries, observed masses, or fitted coefficients are used.

## 1. Unique selector coefficient

Solving the three diagonal stationarity equations for the two unknowns `eta` and `lambda` gives the unique real solution

```math
\boxed{
\eta_*
=-\frac{75(59+21\sqrt5)}{638}
}
```

and

```math
\boxed{
\lambda_*
=-\frac{8765+4758\sqrt5}{4785}.
}
```

Numerically,

```text
eta_*    = -12.4558104460222...
lambda_* =  -4.05521660124222...
```

The stationarity residual is at floating-point order `1e-15`.

## 2. Constrained Hessian

Use the unique quadratic invariant as the norm constraint. The constrained second variation is the Hessian of

```math
\mathcal L(S)
=\mathcal F_{\eta_*}(S)
-\frac{\lambda_*}{2}\operatorname{tr}(S^2)
```

restricted to the four-dimensional tangent space

```math
\operatorname{tr}(D_0X)=0.
```

In the natural decomposition into one diagonal tangent direction and the three symmetric off-diagonal channels, the exact eigenvalues are:

### `12` channel — proportional to `A_seed`

```math
\boxed{
\mu_{12}
=\frac{6(1415+628\sqrt5)}{1595}
>0
}
```

### `13` channel

```math
\boxed{
\mu_{13}
=\frac{3(710+323\sqrt5)}{319}
>0
}
```

### `23` channel

```math
\boxed{
\mu_{23}
=-\frac{2075+771\sqrt5}{319}
<0
}
```

### diagonal tangent channel

```math
\boxed{
\mu_{diag}
=\frac{8765+4758\sqrt5}{1595}
>0.
}
```

Numerically the ordered tangent spectrum is

```text
-11.9091172748
 10.6053317487
 12.1656498037
 13.4694353298
```

Therefore

```math
\boxed{\operatorname{signature}(\operatorname{Hess}_{T}\mathcal L)=(-,+,+,+).}
```

The frozen stationary point is a saddle.

## 3. Independent C3-orbit check

The Stage-65 selector equation deliberately excluded `A_seed` as an input.

After solving and classifying the Hessian, compare the three frozen `C3` images

```math
A_0=A_{seed},
\qquad
A_1=P_3A_{seed}P_3^T,
\qquad
A_2=P_3^2A_{seed}(P_3^T)^2.
```

They are proportional respectively to the symmetric `12`, `23`, and `13` tangent directions.

The Hessian eigendirection alignment is exact:

```text
A_0 -> positive eigenmode mu_12
A_1 -> unique negative eigenmode mu_23
A_2 -> positive eigenmode mu_13
```

Hence

```math
\boxed{
v_-\parallel P_3A_{seed}P_3^T.
}
```

The alignment is an external structural check because the `A_seed` orbit was excluded from the Stage-65 coefficient-selection equation.

## 4. Result

The frozen stationary ordered-axis ansatz produces:

```text
unique eta: PASS
constrained stationarity: PASS
local-minimum classification: SADDLE
Hessian signature: (-,+,+,+)
unique negative mode: exact C3 image of frozen A_seed
CKM input: NONE
mass input: NONE
continuous fitted parameters: NONE
```

The saddle classification is retained as part of the result and is not repaired by coefficient retuning.

## Boundary

This stage establishes a mathematical stationary selector for the frozen cubic ansatz and an exact relation between its Hessian eigendirections and the pre-existing `C3` seed-incidence orbit. Physical assignment of the saddle direction requires a separate gate.

## Reproducibility

Executable:

`TIR/frozen_predictions/validation/scripts/stationary_selector_stage66_v01.py`

Receipt:

`TIR/frozen_predictions/validation/results/TIR_POLYGONAL_STAGE66_STATIONARY_SELECTOR_RECEIPT_V0_1.json`
