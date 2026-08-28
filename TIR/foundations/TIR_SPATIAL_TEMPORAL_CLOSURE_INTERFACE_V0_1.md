# TIR Spatial × Temporal Closure Interface v0.1

Status: `TIR_IDT_SPACETIME_INTERFACE_CANDIDATE`

Scope: TIR-owned interface contract describing how an admitted TIR spatial geometry can later join an independently derived scalar/tensor temporal sector from `Informational-Dynamics-of-Time`. This document defines the compatibility surface; temporal dynamics remain owned by the Time branch.

## 1. Two independently typed sectors

TIR spatial geometry exports

\[
\boxed{
\mathfrak S_X
=(\Sigma,h_{ij},D_i,{}^{(3)}R^{i}{}_{jkl}).
}
\]

The temporal branch is expected to export a packet of the form

\[
\boxed{
\mathfrak T
=(\Theta,N_\Theta,\mathcal K_{ij};\,\beta^i_{\rm match})
}
\]

where:

- `Theta` is the temporal scalar/order field;
- `N_Theta>0` is the scalar normalization between the temporal label and proper normal displacement;
- `K_ij=K_ji` is the temporal deformation tensor on spatial leaves;
- `beta^i_match` is an inter-leaf identification field used when a coordinate matching convention is required.

The first three entries are the scalar/tensor temporal content. The matching field is an interface coordinate choice.

## 2. Leaf picture

Let the temporal scalar label a family of spatial carriers

\[
\Sigma_\Theta.
\]

Each admitted leaf carries the TIR metric

\[
h_{ij}(\Theta,x).
\]

The combined object is therefore represented before full spacetime closure as

\[
\boxed{
\{\Sigma_\Theta,h_{ij}(\Theta)\}_{\Theta}
}
\]

with temporal change encoded by the temporal branch rather than built into the primitive TIR dependency relation.

## 3. Conditional ADM reconstruction

For an admitted three-dimensional spatial leaf, an admitted positive scalar `N_Theta`, and an admitted matching vector `beta^i`, define

\[
\boxed{
 ds^2
 =-N_\Theta^2 d\Theta^2
 +h_{ij}(dx^i+\beta^i d\Theta)(dx^j+\beta^j d\Theta).
}
\]

Equivalently,

\[
g_{00}=-N_\Theta^2+h_{ij}\beta^i\beta^j,
\]

\[
g_{0i}=h_{ij}\beta^j,
\qquad
g_{ij}=h_{ij}.
\]

Because `h_ij` is positive definite and `N_Theta>0`, the Schur complement of the spatial block is

\[
\boxed{
g_{00}-g_{0i}h^{ij}g_{0j}=-N_\Theta^2<0.
}
\]

Hence the reconstructed block metric has Lorentzian signature with one temporal sign and positive spatial block.

This is an exact conditional kinematic reconstruction from the declared interface data.

## 4. Temporal deformation tensor

The spatial metric and temporal deformation tensor meet through the standard ADM kinematic relation

\[
\boxed{
\mathcal K_{ij}
=\frac{1}{2N_\Theta}
\left(
D_i\beta_j+D_j\beta_i-\partial_\Theta h_{ij}
\right)
}
\]

for the corresponding sign convention.

This equation is the typed seam between:

```text
TIR:   h_ij, D_i
TIME:  Theta, N_Theta, K_ij
JOIN:  beta^i matching convention
```

The sign convention is stored as part of the closure contract and must remain consistent across every downstream equation.

## 5. Einstein closure test surface

Once the spatial and temporal sectors are joined, the standard Gauss--Codazzi/ADM constraints provide a precise closure test.

Let

\[
K=h^{ij}\mathcal K_{ij}.
\]

The Hamiltonian constraint is

\[
\boxed{
{}^{(3)}R+K^2-\mathcal K_{ij}\mathcal K^{ij}
=16\pi G\,\rho.
}
\]

The momentum constraint is

\[
\boxed{
D_j\left(\mathcal K^{ij}-h^{ij}K\right)
=8\pi G\,j^i.
}
\]

These equations define the first high-value compatibility target for the later TIR × Time × matter closure.

The dependency direction is

\[
\boxed{
\text{TIR spatial geometry}
+\text{Time scalar/tensor sector}
+\text{matter source packet}
\longrightarrow
\text{ADM closure tests}.
}
\]

## 6. Standard Model join

The Standard Model branch remains a sibling output of the primitive core. After the spatial-temporal closure is admitted, its matter/gauge sector can be coupled to the reconstructed spacetime carrier:

\[
\boxed{
\mathcal B_{\rm SM}
\otimes
\mathfrak M_{XT}
\longrightarrow
\mathfrak M_{XT+\rm matter}.
}
\]

This preserves the primitive ancestry:

```text
COMMON PRIMITIVE CORE
  |--> TIR spatial geometry
  |--> TIR Standard Model branch
  `--> Time scalar/tensor branch

TIR spatial geometry x Time
  --> spacetime closure

spacetime closure x Standard Model
  --> matter/field spacetime closure
```

## 7. Causal order and temporal order remain distinct

The TIR primitive relation

\[
X\prec Y
\]

continues to mean structural dependency. The temporal scalar `Theta` supplies temporal ordering only inside the temporal branch and its closure interface.

Thus the combined architecture has two typed orders:

\[
\boxed{\prec_{\rm dep}}
\quad\text{dependency order},
\]

and

\[
\boxed{\Theta}
\quad\text{temporal order field}.
\]

Their eventual compatibility becomes a theorem/closure condition rather than an identification by notation.

## 8. Export/import contract

### TIR export

```text
owner                = TIR
spatial_leaf         = Sigma
spatial_metric       = h_ij
spatial_connection   = D_i
spatial_curvature    = 3R^i_jkl
spatial_dimension    = n [specialize n=3 at ADM gate]
```

### Time import packet

```text
owner                = Informational-Dynamics-of-Time
temporal_scalar      = Theta
temporal_lapse       = N_Theta
temporal_deformation = K_ij
matching_vector      = beta^i [interface/gauge]
```

### Closure output

```text
spacetime_metric     = g_mu_nu
signature            = Lorentzian
closure_tests        = Hamiltonian + momentum + evolution sector
```

## 9. Claim classes

| Statement | Class |
|---|---|
| ADM block reconstruction from `(h,N,beta)` | STANDARD EXACT CONDITIONAL GEOMETRY |
| Schur complement equals `-N^2` | EXACT ALGEBRAIC |
| Lorentzian signature from positive-definite `h` and positive `N` | EXACT CONDITIONAL |
| `K_ij` kinematic relation | STANDARD ADM IDENTITY WITH DECLARED SIGN CONVENTION |
| Hamiltonian/momentum constraints | STANDARD GR CLOSURE CONDITIONS |
| TIR owns spatial geometry packet | PROJECT ARCHITECTURE CONTRACT |
| IDT owns temporal scalar/tensor packet | CROSS-REPOSITORY ARCHITECTURE CONTRACT |
| Einstein equations recovered as final closure | RESEARCH CLOSURE TARGET |
