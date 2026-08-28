# TIR × IDT — Phase–Clock Physicalization of Information-Area Curvature

Status: `EXACT_DIMENSIONAL_CLOSURE / PHASE_CLOCK_SCALE_BINDING_CANDIDATE / RFC_COUPLING_DOWNSTREAM`

Source pin:

- TIR integration branch: `feat/main-sync-phase-clock-hexahedral-v0.1`
- IDT `main`: `3ac1f53af5223d16f8818dba99a63a6af2ba9498`
- IDT gates: `formalism/01K_temporal_information_curvature_interface.md`, `formalism/05B_phase_clock_length_scale.md`

## 1. Dimensional closure theorem

The projective quantities used by the TIR/Bloch layer are dimensionless:

\[
a_{FS},\quad
\int\mathcal F_B,\quad
|\langle\psi_a|\psi_b\rangle|^2,\quad
\arg\Delta_{abc},\quad
\kappa.
\]

Accordingly, functions built solely from these invariants carry dimension `L^0`. A physical metric or area therefore requires one admitted `L`-typed carrier.

IDT 05B supplies such a carrier directly from the calibrated temporal phase flow,

\[
\boxed{
\ell_\varphi
=\frac{c}{|\omega_t|}
=c\left|\frac{dt}{d\varphi}\right|
=\frac{\hbar c}{E}.
}
\]

This separates two roles cleanly:

- TIR/CP1/polyhedral geometry fixes dimensionless shape, relative metric, area and Berry flux;
- IDT phase-clock dynamics fixes the local physical conversion scale.

## 2. Physicalized Fubini--Study metric candidate

For the CP1 reference metric

\[
ds^2_{FS}
=\frac14\left(d\theta^2+\sin^2\theta\,d\varphi^2\right),
\]

define the phase-clock physicalization candidate

\[
\boxed{
 ds^2_{\rm rel}
 :=\ell_\varphi^2 ds^2_{FS}.
}
\]

Hence

\[
\boxed{
 ds^2_{\rm rel}
 =\frac{c^2}{\omega_t^2}ds^2_{FS}
 =\left(\frac{\hbar c}{E}\right)^2ds^2_{FS}.
}
\]

The conformal scale is therefore local whenever the calibrated phase rate or energy is local.

## 3. Physicalized area and Berry relation

The dimensionless FS area form is

\[
 da_{FS}
 =\frac14\sin\theta\,d\theta\wedge d\varphi,
\]

and the spin-1/2 Berry curvature satisfies

\[
\boxed{
\mathcal F_B=\pm2\,da_{FS}.
}
\]

The local physical relational area element is

\[
\boxed{
 d\mathcal A_{\rm rel}
 :=\ell_\varphi^2da_{FS}
 =\frac{c^2}{\omega_t^2}da_{FS}.
}
\]

Equivalently, with orientation tracked explicitly,

\[
\boxed{
 d\mathcal A_{\rm rel}
 =\pm\frac{\ell_\varphi^2}{2}\mathcal F_B.
}
\]

Thus Berry curvature fixes the dimensionless oriented-area content while temporal phase rate supplies the physical square-length scale.

## 4. Polyhedral and hexahedral cell form

Let `P` be a CP1 polyhedral cell complex with faces `f`. For a piecewise-constant calibrated phase rate on each face,

\[
\boxed{
\mathcal A_{\rm rel}^{(P)}
=\sum_f
\frac{c^2}{\omega_f^2}\,a_{FS}(f).
}
\]

For a common cell rate `omega_P`,

\[
\boxed{
\mathcal A_{\rm rel}^{(P)}
=\frac{c^2}{\omega_P^2}
a_{FS}^{(P)},
\qquad
 a_{FS}^{(P)}:=\sum_f a_{FS}(f).
}
\]

Define the dimensionless refinement ratio

\[
\boxed{
\mathcal R_P:=\frac{a_{FS}^{(P)}}{\pi}.
}
\]

Then

\[
\boxed{
\mathcal A_{\rm rel}^{(P)}
=\pi\mathcal R_P\ell_\varphi^2.
}
\]

A full oriented covering of CP1 has `R_P = 1`. Hexahedral and higher refinements can therefore change the discrete decomposition while preserving the integrated full-sphere area and Berry flux.

For a continuously varying nonzero rate,

\[
\boxed{
\mathcal A_{\rm rel}^{(P)}
=\int_P\frac{c^2}{\omega_t(x)^2}\,da_{FS}(x).
}
\]

## 5. Information-area curvature with the scale eliminated

Let

\[
\mathcal J_\pi=(\ln2)\mathcal I_\pi
=24\pi\kappa\,\mathcal I_\pi.
\]

For a constant-rate cell,

\[
\Xi_I^{(P)}
=\frac{\mathcal J_\pi}{\mathcal A_{\rm rel}^{(P)}}.
\]

Using the phase-clock area expression,

\[
\boxed{
\Xi_I^{(P)}
=\frac{\mathcal J_\pi}{a_{FS}^{(P)}}
\left(\frac{\omega_P}{c}\right)^2
}
\]

or equivalently

\[
\boxed{
\Xi_I^{(P)}
=\frac{\mathcal J_\pi}{a_{FS}^{(P)}}
\left(\frac{E_P}{\hbar c}\right)^2.
}
\]

In canonical TIR form,

\[
\boxed{
\Xi_I^{(P)}
=\frac{24\pi\kappa}{a_{FS}^{(P)}}
\mathcal I_\pi
\left(\frac{\omega_P}{c}\right)^2.
}
\]

For the full CP1/Bloch sphere, `a_FS = pi`, hence

\[
\boxed{
\Xi_I^{(S^2)}
=24\kappa\,\mathcal I_\pi
\left(\frac{\omega}{c}\right)^2.
}
\]

The formerly free area scale `ell_R` is therefore replaced, under the phase-clock binding, by the local dynamical quantity

\[
\boxed{
\ell_R(x)\equiv\ell_\varphi(x)=\frac{c}{|\omega_t(x)|}.
}
\]

## 6. Projective and spinorial cycle scales

IDT 05B also gives

\[
L_{2\pi}=2\pi\ell_\varphi,
\qquad
L_{4\pi}=4\pi\ell_\varphi,
\]

so

\[
\boxed{
\frac{L_{2\pi}}{L_{4\pi}}=\frac12.
}
\]

The projective/Berry `2pi` cycle and spinorial `4pi` cycle remain distinct carriers linked by the exact half ratio.

## 7. Refinement invariant target

For a sequence of polyhedral refinements `P_n`, the field-scale interface requires convergence of the weighted physical area,

\[
\boxed{
\mathcal A_{\rm rel}^{(P_n)}
=\sum_{f\in P_n}\ell_{\varphi,f}^2 a_{FS}(f)
\longrightarrow
\mathcal A_{\rm rel}.
}
\]

The uniform-rate sector reduces this requirement to convergence of the FS/Berry area invariant already present in the projective geometry.

## 8. Export contract to RFC

TIR × IDT export:

```text
phase_clock_length            = ell_phi = c/|omega_t| = hbar*c/E
physicalized_metric           = ds_rel^2 = ell_phi^2 ds_FS^2
physicalized_area_element     = dA_rel = ell_phi^2 da_FS
berry_area_relation           = F_B = ±2 da_FS
polyhedral_area               = sum_f ell_phi,f^2 a_FS(f)
constant_cell_Xi              = (J_pi/a_FS)(omega/c)^2
full_CP1_Xi                   = 24 kappa I_pi (omega/c)^2
projective_spinor_scale_ratio = L_2pi/L_4pi = 1/2
```

RFC owns the binding of `Xi_I` to dynamic `Lambda0`, the action-level metric variation and the Einstein/Newton closure tests.

## 9. Claim typing

Exact within the declared conventions:

- dimensional closure separating dimensionless projective invariants from the IDT length carrier;
- `ell_phi = c/|omega| = hbar*c/E`;
- phase-clock physicalized FS metric and area type signatures;
- constant-rate cell reduction for `A_rel` and `Xi_I`;
- full-CP1 simplification;
- projective/spinorial cycle ratio.

Open physical gates:

- promotion of `ds_rel^2 = ell_phi^2 ds_FS^2` from scale-binding candidate to physical metric calibration;
- behavior at phase-rate zeros;
- spatially varying phase-rate refinement convergence;
- hexahedral rank-three spatial metric binding;
- RFC `Xi_I -> Lambda0` coefficient and field equations.
