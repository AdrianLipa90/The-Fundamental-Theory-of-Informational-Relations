# TIR — Tetrahedral FS / Spatial Shape Crosswalk v0.1

Status: `EXACT_DUAL_SHAPE_MEASURE / CONDITIONAL_SHARED_TETRAHEDRAL_CARRIER / PHYSICAL_SCALE_BINDING_OPEN`

This gate compares two independently typed dimensionless measures carried by the same regular tetrahedral Bloch vertex set when that shared realization is explicitly admitted:

1. the Euclidean three-volume of the tetrahedron in the Bloch/Pauli coefficient carrier `Herm_0(2) ~= R^3`;
2. the Fubini--Study area of the geodesic CP1 tetrahedral cell determined by the same four Bloch directions.

The existing TIR firewall remains active: informational tetrahedral SIC data and physical spatial adjacency are separate types until their promotion gate passes. The crosswalk below is exact on the declared shared-vertex realization and does not perform that promotion by itself.

## 1. Canonical tetrahedral Bloch frame

Let four unit vectors satisfy

\[
\boxed{\mathbf n_a\cdot\mathbf n_b=-\frac13\quad(a\ne b),}
\qquad
\sum_{a=1}^4\mathbf n_a=0.
\]

A canonical realization is

\[
\mathbf n_1=\frac1{\sqrt3}(1,1,1),
\quad
\mathbf n_2=\frac1{\sqrt3}(1,-1,-1),
\]

\[
\mathbf n_3=\frac1{\sqrt3}(-1,1,-1),
\quad
\mathbf n_4=\frac1{\sqrt3}(-1,-1,1).
\]

These are simultaneously the standard regular tetrahedral Bloch directions used by the qubit SIC crosscheck and a regular tetrahedral frame in the real Pauli coefficient carrier.

## 2. Euclidean spatial shape volume

For any distinct pair,

\[
\|\mathbf n_a-\mathbf n_b\|^2
=2-2\left(-\frac13\right)
=\frac83.
\]

Hence the dimensionless edge length is

\[
\boxed{\hat a=\sqrt{\frac83}.}
\]

The volume of a regular tetrahedron of edge `a_hat` is

\[
\hat V_{\Delta^3}
=\frac{\hat a^3}{6\sqrt2}.
\]

Therefore

\[
\boxed{
\hat V_{\Delta^3}
=\frac{8}{9\sqrt3}.
}
\]

The hat marks a dimensionless shape measure in the normalized Bloch/Pauli carrier.

## 3. Projective FS tetrahedral area

For pure qubit states, the Bloch-sphere central angle `chi` between two tetrahedral vertices satisfies

\[
\boxed{\cos\chi=-\frac13.}
\]

Take one geodesic spherical face. It is equilateral with side `chi`. The spherical cosine law gives its interior angle `alpha`:

\[
\cos\chi
=\cos^2\chi+\sin^2\chi\cos\alpha.
\]

Thus

\[
\cos\alpha
=\frac{\cos\chi-\cos^2\chi}{\sin^2\chi}
=-\frac12,
\]

so

\[
\boxed{\alpha=\frac{2\pi}{3}.}
\]

On the unit Bloch sphere the spherical excess of one face is

\[
3\alpha-\pi=\pi.
\]

The qubit Fubini--Study metric is

\[
 ds_{FS}^2=\frac14 ds_{S^2}^2,
\]

so its area element is one quarter of the unit-sphere area element. Therefore one tetrahedral geodesic face carries

\[
\boxed{a_{FS}^{face}=\frac\pi4.}
\]

The four faces give

\[
\boxed{a_{FS}^{tet}=\pi.}
\]

This agrees with the full-CP1 area normalization already used in the TIR x IDT information-area interface.

## 4. Exact dual-shape coefficient

Define the dimensionless dual-shape coefficient

\[
\boxed{
C_{\Delta/FS}
:=\frac{\hat V_{\Delta^3}}{a_{FS}^{tet}}.
}
\]

Using the exact values above,

\[
\boxed{
C_{\Delta/FS}
=\frac{8}{9\sqrt3\,\pi}.
}
\]

Numerically,

\[
C_{\Delta/FS}\approx0.163356709754605.
\]

This number is a shape crosswalk between two differently typed normalized measures. It is not a physical length by itself.

## 5. Separate physical scales

Let the spatial Bloch/Pauli relation carrier receive an admitted physical length scale `ell_s`, while the projective FS carrier receives the IDT phase-clock scale

\[
\ell_\varphi=\frac{c}{|\omega|}.
\]

Then

\[
\boxed{
V_{\Delta^3}^{phys}
=\ell_s^3\hat V_{\Delta^3},
}
\]

while the TIR x IDT interface gives

\[
\boxed{
\mathcal A_{rel}^{tet}
=\ell_\varphi^2 a_{FS}^{tet}
=\pi\ell_\varphi^2.
}
\]

Therefore

\[
\boxed{
\frac{V_{\Delta^3}^{phys}}{\mathcal A_{rel}^{tet}}
=C_{\Delta/FS}
\frac{\ell_s^3}{\ell_\varphi^2}.
}
\]

Define the dimensionless scale ratio

\[
q_s:=\frac{\ell_s}{\ell_\varphi}>0.
\]

Then

\[
\boxed{
\frac{V_{\Delta^3}^{phys}}{\mathcal A_{rel}^{tet}}
=C_{\Delta/FS}\,q_s^3\,\ell_\varphi.
}
\]

If a downstream calibration independently establishes `ell_s=ell_phi`, this reduces to

\[
\boxed{
\frac{V}{\mathcal A_{rel}}
=C_{\Delta/FS}\ell_\varphi.
}
\]

The equality of the two physical length scales is an explicit downstream gate.

## 6. RF-E17 export

RF-E17 contains

\[
E_\star
=\frac{\alpha_{clk}}{\kappa_E}
\frac{V_{cell}}{\mathcal A_{rel}}.
\]

On the conditional shared tetrahedral carrier this becomes

\[
\boxed{
E_\star
=\frac{\alpha_{clk}}{\kappa_E}
C_{\Delta/FS}q_s^3\ell_\varphi.
}
\]

If the RF-L4A normalization `alpha_clk = kappa_E m_I^2` is separately source-bound to the clock-information scalar, then

\[
\boxed{
E_\star
=m_I^2 C_{\Delta/FS}q_s^3\ell_\varphi.
}
\]

Using the IDT phase-clock representation

\[
\ell_\varphi=\frac{\hbar c}{E_\varphi},
\]

one obtains

\[
\boxed{
E_\star
=C_{\Delta/FS}q_s^3
\frac{m_I^2\hbar c}{E_\varphi}
}
\]

with the usual natural-unit simplification when `hbar=c=1`.

This is an exact conditional scale decomposition. The identifications among `m_I`, `E_phi/c^2`, a measured rest mass and the spatial/projective calibration ratio remain separate physical gates.

## 7. Promotion ledger

Exact on the declared normalized shared tetrahedral realization:

- edge length `sqrt(8/3)`;
- Euclidean tetrahedral volume `8/(9 sqrt(3))`;
- spherical face angle `2pi/3`;
- FS face area `pi/4`;
- total tetrahedral CP1 area `pi`;
- shape coefficient `8/(9 sqrt(3) pi)`;
- two-scale `V/A` identity.

Promotion gates retained:

```text
TETRA_SIC_TO_SPATIAL_CELL       informational probe -> physical adjacency
SPATIAL_LENGTH_SCALE            Bloch/Pauli norm -> ell_s
PHASE_CLOCK_AREA_SCALE          FS area -> ell_phi^2 area
COMMON_SCALE                    ell_s = ell_phi, if derived
CLOCK_ALPHA_BINDING             alpha_clk -> RF-L4A alpha_I, if derived
MASS_PHASE_BINDING              m_I / E_phi / measured rest mass
```

Reference validator: `TIR/validation/tir_tetra_fs_spatial_shape_crosswalk_v0_1.py`.
