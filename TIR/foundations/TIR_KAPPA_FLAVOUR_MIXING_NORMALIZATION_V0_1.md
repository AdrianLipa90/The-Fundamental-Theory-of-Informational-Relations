# TIR κ Flavour-Mixing Normalization v0.1

Status: `EXACT_TIR_INTERNAL_FLAVOUR_MIXING_NORMALIZATION_DERIVATION`

## Purpose

This surface records the internal TIR derivation of the denominator in

\[
\kappa=\frac{\ln2}{24\pi}
\]

from the already established three-flavour mixing carrier together with the primitive half-turn phase unit.

The derivation replaces the older bookkeeping-only reading of

\[
24=8\cdot3
\]

with an explicit dependency chain from the flavour mixing matrix.

## 1. Three-flavour carrier

The TIR flavour-mixing branch establishes

\[
V_F\cong\mathbb C^3
\]

and a full mixing transformation

\[
U_F\in SU(3)_F.
\]

Hence the flavour multiplicity is

\[
\boxed{N_F=3.}
\]

## 2. Eight independent mixing directions

For the special unitary flavour group,

\[
\dim_{\mathbb R}\mathfrak{su}(N)=N^2-1.
\]

Therefore

\[
\boxed{
\dim_{\mathbb R}\mathfrak{su}(3)_F=3^2-1=8.
}
\]

Choose any basis of generators

\[
\{T_a\}_{a=1}^{8}
\]

for the mixing algebra. The number eight is basis-independent because it is the Lie-algebra dimension.

The Stage-55 decomposition gives the independent crosscheck

\[
8=3+5,
\]

through

\[
\mathfrak{su}(3)_F
=
\mathfrak{so}(3)\oplus\mathfrak p,
\qquad
\dim\mathfrak{so}(3)=3,
\qquad
\dim\mathfrak p=5.
\]

## 3. Mixing-channel multiplicity

Define the primitive mixing-channel label set by the Cartesian product

\[
\mathcal C_{\rm mix}
=
\{1,\ldots,8\}_{\rm generator}
\times
\{1,2,3\}_{\rm flavour}.
\]

Its cardinality is therefore

\[
\boxed{
N_{\rm mix}
=
\dim\mathfrak{su}(3)_F\,N_F
=8\cdot3
=24.
}
\]

Equivalently,

\[
\boxed{
N_{\rm mix}
=N_F(N_F^2-1)
=3(3^2-1)
=24.
}
\]

This is the exact source of the integer factor in the TIR normalization.

## 4. Half-turn phase unit

The primitive binary balance supplies the half coordinate

\[
\sigma_\star=\frac12.
\]

Under the standard angular closure of one full turn,

\[
\Delta\phi_{\rm full}=2\pi,
\]

the corresponding half-turn phase unit is

\[
\boxed{
\Delta\phi_{1/2}
=\frac12(2\pi)
=\pi.
}
\]

This is also the relative phase producing the sign reversal between the two orientations of the binary/spinorial relation.

## 5. Total primitive mixing-phase measure

One half-turn phase unit for each generator-flavour mixing channel gives

\[
\Phi_{\rm mix}
=N_{\rm mix}\,\Delta\phi_{1/2}.
\]

Therefore

\[
\boxed{
\Phi_{\rm mix}
=24\pi.
}
\]

The denominator thus factorizes as

\[
\boxed{
24\pi
=
\underbrace{(3^2-1)}_{8\ \mathrm{mixing\ directions}}
\underbrace{3}_{\mathrm{flavours}}
\underbrace{\pi}_{\mathrm{half\!\!-turn\ phase}}.
}
\]

## 6. κ

The primitive balanced binary distinction carries

\[
\boxed{
I_\star=H_2(1/2)=\ln2.
}
\]

The TIR information-per-mixing-phase normalization is therefore

\[
\kappa
=\frac{I_\star}{\Phi_{\rm mix}}
=\frac{\ln2}{N_F(N_F^2-1)\pi}.
\]

For the three-flavour carrier,

\[
\boxed{
\kappa
=\frac{\ln2}{3(3^2-1)\pi}
=\frac{\ln2}{24\pi}.
}
\]

Thus the coefficient is obtained internally from:

\[
\boxed{
\text{binary information}
\times
\text{half-turn phase}
\times
\text{three-flavour }SU(3)_F\text{ mixing geometry}.
}
\]

## 7. Independent 24 crosscheck from the spatial branch

The Space of Geometry independently gives the minimal regular tetrahedral cell with abstract automorphism group

\[
\operatorname{Aut}(\Delta^3)\cong S_4,
\]

and therefore

\[
|S_4|=24.
\]

Hence the same integer appears through two structurally distinct routes:

\[
\boxed{
3\,\dim\mathfrak{su}(3)_F
=3\cdot8
=24
=|S_4|.
}
\]

The flavour-mixing route is the normalization derivation recorded here; the tetrahedral order supplies an independent finite-symmetry crosscheck.

## 8. Dependency receipt

```text
binary_half = 1/2
binary_information = ln2
full_turn_phase = 2*pi
half_turn_phase = pi
flavour_carrier = C^3
mixing_group = SU(3)_F
mixing_algebra_dimension = 3^2 - 1 = 8
flavour_multiplicity = 3
mixing_channel_count = 8*3 = 24
total_mixing_phase_measure = 24*pi
kappa = ln2/(24*pi)
```

Canonical status:

`TIR_INTERNAL_DERIVED_NORMALIZATION_FROM_FLAVOUR_MIXING_GEOMETRY`
