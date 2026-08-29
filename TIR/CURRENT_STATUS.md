# CURRENT STATUS — TIR

**Status line:** 2026-08-29 foundational-completion audit  
**Author:** Adrian Lipa  
**Active branch:** `feat/tir-relational-half-seam-v0.1`  
**Pull request:** #96 — `TIR: build primitive causal and spatial geometry foundation`  
**Promotion:** feature branch; `main` unchanged pending explicit merge order

This file is the current TIR status surface. Historical review states remain available through repository history and archival publication surfaces.

## 1. Foundational status

The current primitive dependency spine is

\[
\boxed{
0
\to P
\to \text{FIRST DISTINCTION}
\to \{N,S\}
\to \frac12
\to \ln2
\to \mathbb C^2.
}
\]

The spatial branch now continues through

\[
\boxed{
\mathbb C^2
\to \rho_x
\to \mathcal A_2
\to \delta(\rho_x,\rho_y)
\to \operatorname{Herm}_0(2)\cong\mathbb R^3.
}
\]

From this common carrier, the local geometry forks into

\[
\boxed{
\operatorname{Herm}_0(2)
\to
\begin{cases}
\text{Euclidean inner-product branch}\to a^2+b^2=c^2,\\
\text{minimal finite-cell branch}\to\Delta^3\xrightarrow{A5+A7}\text{regular tetrahedron}.
\end{cases}}
\]

The dedicated publication surface is

`TIR/subrepos/the-space-of-geometry/paper/THE_SPACE_OF_GEOMETRY_V1_0.tex`.

Current classification:

```text
TIR_FOUNDATIONAL_CORE = CLOSED
TIR_LOCAL_SPATIAL_GEOMETRY = CLOSED
TIR_GLOBAL_GEOMETRY_PROGRAMME = DOWNSTREAM
TIR_STANDARD_MODEL_PROGRAMME = ACTIVE
TIR_TIME_JOIN = SIBLING_INTERFACE
```

## 2. κ normalization — flavour-mixing derivation

The denominator in

\[
\boxed{
\kappa=\frac{\ln2}{24\pi}
}
\]

is now carried by the explicit TIR flavour-mixing derivation in

`TIR/foundations/TIR_KAPPA_FLAVOUR_MIXING_NORMALIZATION_V0_1.md`.

The flavour carrier is

\[
V_F\cong\mathbb C^3,
\qquad
U_F\in SU(3)_F.
\]

Thus

\[
N_F=3
\]

and

\[
\dim_{\mathbb R}\mathfrak{su}(3)_F
=3^2-1
=8.
\]

The generator-flavour incidence count is therefore

\[
\boxed{
N_{\rm mix}
=N_F\dim\mathfrak{su}(3)_F
=3\cdot8
=24.
}
\]

The primitive half coordinate supplies the half-turn phase unit

\[
\Delta\phi_{1/2}
=\frac12(2\pi)
=\pi.
\]

Hence the total primitive mixing-phase measure is

\[
\boxed{
\Phi_{\rm mix}
=N_{\rm mix}\Delta\phi_{1/2}
=24\pi.
}
\]

With the balanced binary information quantum

\[
I_\star=H_2(1/2)=\ln2,
\]

the TIR information-per-mixing-phase normalization gives

\[
\boxed{
\kappa
=\frac{I_\star}{\Phi_{\rm mix}}
=\frac{\ln2}{3(3^2-1)\pi}
=\frac{\ln2}{24\pi}.
}
\]

This is classified as a **TIR-internal derived structural normalization**. Its upstream ingredients are the binary-information theorem, the half-turn angular unit, and the three-flavour `SU(3)_F` mixing carrier.

An independent finite-symmetry crosscheck is supplied by the spatial branch:

\[
\operatorname{Aut}(\Delta^3)\cong S_4,
\qquad
|S_4|=24.
\]

Thus

\[
\boxed{
3\dim\mathfrak{su}(3)_F
=3\cdot8
=24
=|S_4|.
}
\]

## 3. Exact κ phase-rate closure

For

\[
\omega=2\pi f
\]

and

\[
d\mathcal I=\kappa\,d\phi,
\]

the exact consequence remains

\[
\boxed{
\Gamma_{\mathcal I}
=\frac{d\mathcal I}{dt}
=\kappa\omega
=\frac{\ln2}{12}f.
}
\]

One complete angular cycle carries

\[
\boxed{
\Delta\mathcal I_{\rm cycle}
=2\pi\kappa
=\frac{\ln2}{12}.
}
\]

The exact implementation checks are

- `TIR/validation/tir_kappa_flavour_mixing_normalization_v0_1.py`;
- `TIR/validation/kappa_phase_rate_identity_v11_1.py`.

Both are part of the integrated TIR verification workflow.

## 4. Mixing carrier provenance

The three-flavour carrier and full family mixing transformation are established in the polygonal-excitation validation line:

\[
V_F\cong\mathbb C^3,
\qquad
V_F^{\rm mix}=R_{23}R_{13}(\delta)R_{12}\in SU(3)_F.
\]

The later symmetric-pair closure gives

\[
\mathfrak{su}(3)_F
=\mathfrak{so}(3)\oplus\mathfrak p,
\qquad
\dim\mathfrak{so}(3)=3,
\qquad
\dim\mathfrak p=5,
\]

so

\[
8=3+5
\]

independently certifies the eight-dimensional mixing algebra.

Canonical provenance surfaces:

- `TIR/frozen_predictions/validation/TIR_POLYGONAL_EXCITATION_STAGE34_CKM_SU3F_CARRIER_V0_1.md`;
- `TIR/frozen_predictions/validation/TIR_POLYGONAL_EXCITATION_STAGE55_SU3_SO3_SYMMETRIC_PAIR_V0_1.md`;
- `TIR/monograph/appendices/appP_information_spinor_crosswalk.tex`.

## 5. TIR ↔ Secret-of-a-Half interface

The current typed chain is

\[
\boxed{
\frac12
\xrightarrow{H_2}
\ln2
\xrightarrow{\text{flavour-mixing normalization}}
\kappa
\xrightarrow{d\mathcal I=\kappa d\phi}
\Gamma_{\mathcal I}.
}
\]

The exact half theorem supplies the numerator. The flavour-mixing carrier, mixing-algebra dimension, flavour multiplicity and half-turn phase supply the denominator.

## 6. Spatial publication state

`The Space of Geometry: From First Distinction to Pythagoras` is the current local spatial-geometry release candidate.

Its theorem split is:

```text
Theorem E — local Euclidean/Pythagorean closure
Theorem T1 — minimal finite full-dimensional support
Theorem T2 — regular tetrahedron from A5+A7 edge-orbit invariance
Theorem Q — independent tetrahedral qubit-SIC convergence
```

The same local carrier therefore supports both

\[
a^2+b^2=c^2
\]

and

\[
n_a\cdot n_b=-\frac13\quad(a\ne b)
\]

as parallel consequences.

## 7. Active physical frontier

The remaining work is concentrated above the foundational layer:

1. sector-by-sector Standard Model derivation and empirical audit;
2. operational calibration of information-rate observables;
3. global spatial refinement, curvature and holonomy;
4. TIR spatial geometry × Time scalar/tensor closure;
5. completion of any still-open Secret-of-a-Half / zeta proof dependencies;
6. preservation of frozen prospective tests and explicit empirical failure receipts.

## 8. Reproducibility invariant

Every PASS belongs to the exact commit tested. Claim promotion follows the evidence class of the specific theorem or observable.

The integrated workflow is

`.github/workflows/tir-integrated-kappa-critical-axis.yml`.

It now audits the flavour-mixing derivation of the κ denominator in addition to the existing phase-rate, primitive-foundation, spatial and critical-axis gates.
