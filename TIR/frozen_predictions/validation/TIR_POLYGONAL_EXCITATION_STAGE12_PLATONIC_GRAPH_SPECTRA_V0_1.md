# TIR Polygonal Excitation — Stage 12: Parameter-Free Graph Spectra for N=4 and N=5

Status: `STAGE_12_PLATONIC_GRAPH_SPECTRA_PASS`

Scope: pure geometry and graph spectral mathematics, with a canonical exchange-matrix normalization prepared for later QHTRI replay.

## 1. Canonical edge graphs

Stage 10 identifies the finite closures

\[
N=4\to\{3,4\}\quad\text{octahedron},
\qquad
N=5\to\{3,5\}\quad\text{icosahedron}.
\]

Define the unweighted adjacency matrices directly from geometric nearest-neighbour edges:

\[
(A_N)_{ij}=1
\]

exactly when vertices i and j share a polyhedral edge, and zero otherwise.

The octahedral graph is 4-regular on 6 vertices. The icosahedral graph is 5-regular on 12 vertices.

## 2. Octahedral spectrum

The adjacency spectrum is

\[
\operatorname{spec}(A_4)=\{4,-2,-2,0,0,0\}.
\]

Therefore

\[
\boxed{\chi_{A_4}(\lambda)=\lambda^3(\lambda-4)(\lambda+2)^2}.
\]

The graph Laplacian L_4=4I-A_4 has spectrum

\[
\{0,4,4,4,6,6\}.
\]

## 3. Icosahedral spectrum

The adjacency spectrum is

\[
\operatorname{spec}(A_5)
=
\{5,(\sqrt5)^{\times3},(-\sqrt5)^{\times3},(-1)^{\times5}\}.
\]

Therefore

\[
\boxed{
\chi_{A_5}(\lambda)
=(\lambda-5)(\lambda+1)^5(\lambda^2-5)^3
}.
\]

The graph Laplacian L_5=5I-A_5 has spectrum

\[
\{0,(5-\sqrt5)^{\times3},6^{\times5},(5+\sqrt5)^{\times3}\}.
\]

## 4. Canonical exchange normalization

For each connected positive d-regular adjacency matrix above, the spectral radius equals d. Hence the parameter-free normalized exchange matrices are

\[
\boxed{H_4=A_4/4},
\qquad
\boxed{H_5=A_5/5}.
\]

They are real symmetric Hermitian matrices with unit spectral radius.

Their spectra are

\[
\operatorname{spec}(H_4)
=\{1,-1/2,-1/2,0,0,0\},
\]

and

\[
\operatorname{spec}(H_5)
=
\{1,(1/\sqrt5)^{\times3},(-1/\sqrt5)^{\times3},(-1/5)^{\times5}\}.
\]

## 5. Computational audit

The audit constructs the vertices from exact regular-polyhedron coordinates, infers edges by the unique minimum nonzero pair distance, constructs A_N, and diagonalizes the resulting symmetric matrices.

Maximum adjacency-spectrum residuals:

\[
N=4:\ 4.44\times10^{-16},
\qquad
N=5:\ 1.78\times10^{-15}.
\]

Both normalized exchange matrices have Hermiticity residual zero and spectral radius one to floating-point precision.

## 6. Verdict

`STAGE_12_PLATONIC_GRAPH_SPECTRA_PASS`

The next gate tests whether the Stage 1 latitude c_N is itself the eigenvalue carried by the three-dimensional geometric coordinate subspace of H_N.