# TIR × IDT cross-review — information, area and inverse-square curvature typing

Date: 2026-08-27

Status: `CROSS_REVIEW_PASS_CANDIDATE / PHYSICAL_LENGTH_CALIBRATION_OPEN`

## Result

The dimensional chain is now typed as

\[
\boxed{
\text{dimensionless information}
\rightarrow
\text{dimensionless CP1/FS area}
\rightarrow
\text{length-calibrated relational area }L^2
\rightarrow
\text{information-area scalar }L^{-2}.
}
\]

For the CP1 reference geometry,

\[
da_{FS}=\frac14\sin\theta\,d\theta\wedge d\varphi,
\qquad
\mathcal F_B=\pm2da_{FS}.
\]

With a positive length calibration `ell_R`,

\[
\mathcal A_{\rm rel}=\ell_R^2 a_{FS}.
\]

The IDT 01K scalar is therefore

\[
\boxed{
\Xi_I
=\frac{(\ln2)\mathcal I_\pi}{\mathcal A_{\rm rel}}
=\frac{24\pi\kappa\mathcal I_\pi}{\mathcal A_{\rm rel}},
\qquad
[\Xi_I]=L^{-2}.
}
\]

## Dependency ownership

- TIR owns `a_FS`, Berry/FS geometric typing, `kappa`, and the `A_rel = ell_R^2 a_FS` calibration interface.
- IDT owns the temporal evolution of `I_pi`, `A_rel`, and `Xi_I` through internal elapsed activity and clock calibration.
- RFC owns the later field-level statement relating `Xi_I` to the dynamic `Lambda0` scalar.

## Evidence

Reference test:

`TIR/validation/information_area_curvature_v0_1.py`

Result: `6 passed`.

Receipt:

`TIR/validation/INFORMATION_AREA_CURVATURE_V0_1.json`

This cross-review preserves the current TIR claim hierarchy while exporting a dimensionally explicit interface to IDT and RFC.
