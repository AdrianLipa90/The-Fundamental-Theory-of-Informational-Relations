# TIR Polygonal Excitation — Stage 36 Complex Open-Holonomy CP Mechanism v0.1

Status: `STAGE_36_COMPLEX_HOLONOMY_CP_MECHANISM_PASS__SOURCE_PROMOTION_QUARANTINED`

## Scope

This gate tests whether a pre-existing complex phase carried by the archived TIR family-sector holonomy is sufficient to generate a non-zero rephasing-invariant CP measure on the three-dimensional family carrier.

No observed CKM entries, observed masses, PMNS entries, or fitted White-Thread values are used as construction inputs.

The gate is mechanism-level. The archived heavy-family source rows retain their existing quarantine status, so physical promotion remains blocked.

## Frozen source objects

The archived v3.5 pre-CKM module records for each up/down family pair

- `oriented_open_holonomy_overlap = a_ij`,
- `phase_gap_rad = phi_ij`,
- `uses_observed_mass = False`,
- `uses_observed_CKM = False`,
- `uses_observed_PMNS = False`,
- `uses_fitted_white_thread_values = False`.

The v3.5 source explicitly describes `phase_gap_rad` as an open-holonomy phase-displacement proxy derived from the angle between normalized sector-basis vectors.

Stage 36 therefore uses the minimal coefficient-free complex lift

```math
\boxed{
W^{\mathbb C}_{ij}=a_{ij}e^{i\phi_{ij}}.
}
```

No additional phase, continuous coefficient, normalization parameter, or CKM target is introduced.

## Hermitian family pair

Define

```math
H_u=WW^\dagger,
\qquad
H_d=W^\dagger W.
```

The numerical replay gives

```text
max |H_u-H_u^dagger| = 8.38e-18
max |H_d-H_d^dagger| = 8.66e-18
```

and

```math
\boxed{[H_u,H_d]\neq0}
```

with

```text
max |[H_u,H_d]| = 0.06454341101125786.
```

The two operators share the singular-value spectrum, as required by their construction:

```text
1.665876898e-05
0.0510640026211
0.926980773026
```

up to floating-point ordering residuals.

## Relative family transformation

Let

```math
U_u^\dagger H_u U_u=D_u,
\qquad
U_d^\dagger H_d U_d=D_d.
```

The relative transformation is

```math
V_F=U_u^\dagger U_d.
```

After removal of the irrelevant global determinant phase, the representative lies in `SU(3)_F` with

```text
max |V_F^dagger V_F-I| = 8.88e-16
|det(V_F)-1| = 7.71e-16.
```

Its magnitude matrix is

```math
|V_F|\approx
\begin{pmatrix}
0.296811&0.953971&0.042928\\
0.951639&0.292111&0.095158\\
0.079293&0.067900&0.994536
\end{pmatrix}.
```

This matrix is retained as the direct output of the structural gate. No target matrix is used to alter it.

## Rephasing-invariant complex phase

For row pair `(i,j)` and column pair `(k,l)`, define the plaquette product

```math
P_{ij;kl}
=
W_{ik}W_{jl}W_{il}^*W_{jk}^*.
```

Its phase is invariant under independent row and column rephasings.

The largest absolute plaquette phase in the archived v3.5 lift is

```math
\boxed{
\max |\arg P_{ij;kl}|
=0.37125283033244827\ \mathrm{rad}.
}
```

Therefore the phase matrix is not reducible to a pure row-phase plus column-phase convention.

## CP invariant

Using the relative unitary family transformation,

```math
J_F=
\operatorname{Im}
\left(
V_{11}V_{22}V_{12}^*V_{21}^*
\right),
```

the replay gives

```math
\boxed{
J_F=-4.270454683508035\times10^{-4}.
}
```

Thus the complex open-holonomy lift generates a non-zero basis-invariant CP quantity without inserting a CKM phase as an input.

## Provenance boundary

The v3.4 source rows for `c`, `t`, and `b` retain the status

`old_doc_bridge_ansatz_quarantined`.

The source rows for `u`, `d`, and `s` retain `definition_plus_old_doc_bridge_ansatz`.

Accordingly:

```text
complex-holonomy CP mechanism: PASS
non-commuting Hermitian family pair: PASS
rephasing-invariant phase: PASS
non-zero J_F: PASS
physical promotion: QUARANTINED BY SOURCE PROVENANCE
```

The numerical result is not promoted to an independently validated CKM prediction.

## Reproducibility

Executable:

`TIR/frozen_predictions/validation/scripts/complex_holonomy_cp_stage36_v01.py`

Receipt:

`TIR/frozen_predictions/validation/results/TIR_POLYGONAL_STAGE36_COMPLEX_HOLONOMY_CP_RECEIPT_V0_1.json`

## Next gate

Replace the quarantined heavy-family source rows with a family operator derived only from the already frozen polygonal/McKay/seed geometry. The next admissible test is whether the same complex-holonomy construction produces non-zero rephasing-invariant phase and non-zero `J_F` when the three family states are generated directly from the new `N=3,4,5 -> E6,E7,E8` chain rather than inherited heavy-family bridge ansatz rows.
