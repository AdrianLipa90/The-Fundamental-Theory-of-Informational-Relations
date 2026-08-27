# TIR — Hexahedral Bloch Dual Frame and Rank-Three Projective Metric

Status: `EXACT_HEXAHEDRAL_DUAL_FRAME_THEOREM / LOCAL_SPATIAL_TRIAD_BINDING_CANDIDATE / GLOBAL_SPATIAL_INTEGRABILITY_OPEN`

Upstream base:

- TIR phase-clock area branch: `agent/phase-clock-area-scale-v0.2`
- base head at branch creation: `b69ba6055c0535c666e12dbba069ffb87238eee6`

## 1. Hexahedron on the Bloch sphere: dual representation

A regular hexahedral cell has six oriented faces. Represent the six outward face normals by the Bloch vectors

\[
\boxed{
\mathcal H^\star
=\{\mathbf n_{i,s}=s\,\mathbf e_i:\ i=1,2,3,\ s=\pm1\}
\subset S^2_{\rm Bloch}.
}
\]

The corresponding pure-state density matrices are

\[
\boxed{
\rho_{i,s}=\frac12\left(I+s\sigma_i\right).
}
\]

Thus the hexahedron is represented on the Bloch sphere by its six face normals. The six Bloch points form the octahedral dual complex. The original hexahedron has

\[
(V,E,F)=(8,12,6),
\]

while the dual spherical complex has

\[
(V^\star,E^\star,F^\star)=(6,12,8).
\]

Both satisfy the Euler invariant

\[
\boxed{\chi=V-E+F=2.}
\]

This dual typing removes an ambiguity: the physical combinatorial object is hexahedral, while the six Bloch representatives are its oriented face-normal rays.

## 2. Exact pair invariants

For pure qubit rays with unit Bloch vectors `n_a,n_b`,

\[
\boxed{
P_{ab}=|\langle\psi_a|\psi_b\rangle|^2
=\frac{1+\mathbf n_a\cdot\mathbf n_b}{2},
}
\]

and

\[
\boxed{
d_{FS}(a,b)
=\frac12\arccos(\mathbf n_a\cdot\mathbf n_b).
}
\]

For the hexahedral dual frame:

- identical normal: `P=1`, `d_FS=0`;
- opposite face pair: `P=0`, `d_FS=pi/2`;
- distinct orthogonal face normals: `P=1/2`, `d_FS=pi/4`.

Hence the six-state distance/transition fingerprint is fixed without choosing a Cartesian embedding beyond the relational orthogonal triad itself.

## 3. Weighted second moment

Assign equal weights

\[
w_{i,s}=\frac16.
\]

Define the Bloch second-moment tensor

\[
\boxed{
M_{\mathcal H}
:=\sum_{i,s}w_{i,s}\,\mathbf n_{i,s}\mathbf n_{i,s}^{\mathsf T}.
}
\]

Because each axis occurs with both orientations,

\[
\sum_{i,s}\mathbf n_{i,s}\mathbf n_{i,s}^{\mathsf T}=2I_3,
\]

therefore

\[
\boxed{M_{\mathcal H}=\frac13 I_3.}
\]

This is an exact isotropic second-moment invariant.

## 4. Aggregate Fubini--Study orbit metric

Let `xi,eta in R^3` be infinitesimal rotation generators of the full six-ray configuration. For each Bloch vector,

\[
\delta_\xi\mathbf n=\boldsymbol\xi\times\mathbf n.
\]

The qubit Fubini--Study line element is

\[
ds_{FS}^2=\frac14\,d\mathbf n\cdot d\mathbf n.
\]

Define the aggregate configuration-orbit bilinear form

\[
\boxed{
h_{\mathcal H}(\boldsymbol\xi,\boldsymbol\eta)
:=\frac14\sum_a w_a
(\boldsymbol\xi\times\mathbf n_a)\cdot
(\boldsymbol\eta\times\mathbf n_a).
}
\]

Using

\[
(\xi\times n)\cdot(\eta\times n)
=\xi\cdot\eta-(\xi\cdot n)(\eta\cdot n),
\]

one obtains for any normalized weighted Bloch configuration

\[
\boxed{
h_P
=\frac14\left(I_3-M_P\right),
\qquad
M_P:=\sum_a w_a n_an_a^{\mathsf T}.
}
\]

For the hexahedral dual frame,

\[
\boxed{
h_{\mathcal H}=\frac16 I_3.}
\]

Therefore

\[
\boxed{
\operatorname{rank}h_{\mathcal H}=3,
\qquad
\operatorname{Spec}(h_{\mathcal H})
=\left\{\frac16,\frac16,\frac16\right\},
}
\]

\[
\boxed{
\det h_{\mathcal H}=\frac1{216}>0,
\qquad
\operatorname{cond}(h_{\mathcal H})=1.
}
\]

The hexahedral face-normal frame therefore supplies an exact positive rank-three local projective metric with isotropic conditioning.

The rank-three result is a property of the multi-ray configuration. It does not contradict the rank-at-most-two pullback bound for a single `CP1` ray.

## 5. Isotropy extremum

For every normalized weighted unit-vector configuration,

\[
\operatorname{tr}M_P=1,
\]

hence

\[
\boxed{\operatorname{tr}h_P=\frac12.}
\]

Among positive three-eigenvalue metrics with fixed trace `1/2`, the determinant is maximal when all eigenvalues are equal. Therefore

\[
\boxed{
\det h_P\le\left(\frac16\right)^3=\frac1{216},
}
\]

with equality for an isotropic second moment `M_P=I/3`, including the regular hexahedral dual frame.

Thus the hexahedral frame is not merely rank three: it realizes the maximally isotropic determinant at fixed aggregate FS trace.

## 6. Berry/Bargmann face invariants

The six dual vertices partition the Bloch sphere into eight spherical octants, one for each vertex of the original hexahedron.

Each octant has solid angle

\[
\boxed{\Omega_{\rm oct}=\frac\pi2.}
\]

Because the spin-1/2 Fubini--Study area is one quarter of Bloch solid angle,

\[
\boxed{a_{FS,\rm oct}=\frac\pi8.}
\]

The corresponding oriented Berry/Pancharatnam triangle phase has magnitude

\[
\boxed{|\gamma_{B,\rm oct}|=\frac{\Omega_{\rm oct}}2=\frac\pi4.}
\]

For example, with the ordered rays `(+x,+y,+z)`,

\[
\arg\!\left(
\langle +x|+y\rangle
\langle +y|+z\rangle
\langle +z|+x\rangle
\right)
=+\frac\pi4
\]

in the stated orientation convention.

Summing the eight oriented octants gives

\[
\sum_f\Omega_f=4\pi,
\qquad
\sum_f a_{FS}(f)=\pi,
\]

and the full Berry flux is

\[
\boxed{
\int_{S^2}\mathcal F_B=\pm2\pi.
}
\]

Therefore the first Chern number is

\[
\boxed{
c_1=\frac1{2\pi}\int_{S^2}\mathcal F_B=\pm1.
}
\]

The Euler characteristic `chi=2`, total FS area `pi`, total Berry flux magnitude `2pi`, Chern number magnitude `1`, and the rank-three second-moment metric survive any refinement that preserves the corresponding integrated invariants and local rank gate.

## 7. Phase-clock physicalization

Import the IDT phase-clock length carrier from the pinned TIR×IDT interface,

\[
\ell_\varphi=\frac{c}{|\omega_t|}=\frac{\hbar c}{E}.
\]

For a common local phase rate over one hexahedral cell, define

\[
\boxed{
h_{\mathcal H}^{\rm phys}
:=\ell_\varphi^2 h_{\mathcal H}
=\frac{\ell_\varphi^2}{6}I_3
=\frac{c^2}{6\omega_t^2}I_3.
}
\]

Hence

\[
\boxed{[h_{\mathcal H}^{\rm phys}]=L^2}
\]

when evaluated on dimensionless local orientation coordinates.

Equivalently introduce the local coframe

\[
\boxed{
E^i:=\frac{\ell_\varphi}{\sqrt6}\,\vartheta^i,
}
\]

where `vartheta^i` is a dimensionless hexahedral orientation coframe. Then

\[
\boxed{
h_\perp=\sum_{i=1}^3E^i\otimes E^i}
\]

is positive and rank three.

## 8. Export to RFC

TIR exports the following exact local structural package:

```text
hexahedron_representation = six oriented face-normal rays {±ex, ±ey, ±ez}
second_moment              = I3 / 3
aggregate_FS_metric        = I3 / 6
metric_rank                = 3
metric_determinant         = 1 / 216
metric_condition_number    = 1
spherical_cells            = 8 octants
FS_area_per_octant         = pi / 8
Berry_phase_per_octant     = ± pi / 4
total_FS_area              = pi
total_Berry_flux           = ± 2 pi
first_Chern_number         = ± 1
Euler_characteristic       = 2
physical_scale_candidate   = ell_phi = c / |omega_t|
physical_local_metric      = ell_phi^2 I3 / 6
```

RFC may use this package as the positive rank-three prerequisite of its Lorentzian signature gate.

## 9. Remaining closure boundary

The local rank-three metric theorem is exact for the declared hexahedral dual-frame orbit geometry. Downstream work must still determine:

1. how the local orientation coframe `vartheta^i` binds to physical spatial displacement;
2. whether the coframe is integrable or carries torsion/connection curvature;
3. how neighboring hexahedral cells glue under refinement;
4. how anisotropic/local phase rates deform the spatial metric;
5. whether the resulting weak-field limit yields the Newtonian potential without importing Newton's law as a premise.
