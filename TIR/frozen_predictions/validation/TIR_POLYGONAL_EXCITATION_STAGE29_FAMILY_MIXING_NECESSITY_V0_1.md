# TIR Polygonal Excitation — Stage 29 Family Mixing Necessity v0.1

Status: `STAGE_29_NONTRIVIAL_MIXING_REQUIRES_SECTOR_MISALIGNMENT_PASS`

## Family carrier

Stage 25 separates the family factor from color. Let the three-dimensional family space be

```math
V_F\cong\mathbb C^3.
```

Let `U_u` and `U_d` denote orthonormal family bases selected by the up-type and down-type quark sector operators. The relative mixing operator is

```math
V_{ud}=U_u^\dagger U_d.
```

## Exact necessity theorem

If the two sector operators select the same ordered family basis up to diagonal rephasings,

```math
U_d=U_uD,
\qquad D=\operatorname{diag}(e^{i\alpha_1},e^{i\alpha_2},e^{i\alpha_3}),
```

then

```math
V_{ud}=D.
```

After independent field rephasing this carries zero nontrivial family mixing. In particular, identical bases give

```math
\boxed{U_u=U_d\implies V_{ud}=I_3.}
```

Therefore nontrivial three-family mixing requires a genuine relative orientation of the up and down family-sector bases.

## Relation to existing TIR pre-mass orientation

TIR v3.4 constructs mass-free structural up/down frames from CP1 pole, chirality, color depth, hypercharge, Collatz phase, Ramanujan coordinate, zeta-Heisenberg coordinate, and the fixed information quantum. Its output is explicitly named `up_down_basis_overlap_not_CKM`.

This existing object can therefore be tested as a sector-misalignment witness without promoting it to a physical mixing matrix.

## Result

Stage 29 establishes the exact algebraic requirement that any TIR CKM-like derivation must satisfy: a nontrivial mixing operator can arise only after sector-dependent family orientation has been derived. No CKM data or masses enter this theorem.

## Next gate

Test the frozen v3.4 cross-Gram for rank, singular values, unitarity and canonical polar decomposition while preserving its pre-CKM status.
