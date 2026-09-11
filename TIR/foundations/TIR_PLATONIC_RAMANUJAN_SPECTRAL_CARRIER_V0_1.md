# TIR Platonic–Ramanujan Spectral Carrier v0.1

Status: `EXACT_GRAPH_THEOREM / TIR_STRUCTURAL_CANDIDATE / PHYSICAL_BINDING_OPEN`  
Date: 2026-09-11  
Parent: `TIR_PLATONIC_L_CONSTANTS_CLOSURE_V0_1`

## 1. Scope and terminology

This module introduces a finite spectral carrier that links the Platonic branch of TIR to Ramanujan **graph** geometry.

It deliberately distinguishes two different uses of the name Ramanujan already present in the project:

1. arithmetic Ramanujan sums used in earlier Standard-Model diagnostic modules;
2. the Ramanujan spectral bound for regular graphs used here.

No equivalence between those two constructions is assumed.

This document also does **not** identify a finite Platonic graph with a continuous hyperbolic Ramanujan surface. The finite graph statement is exact on its own. Continuous-surface or Ramanujan-complex lifts remain a separate future bridge.

## 2. Platonic skeletons are Ramanujan graphs

For a connected \(k\)-regular graph \(G\), let \(A_G\) be its adjacency matrix. A finite graph is Ramanujan when every nontrivial adjacency eigenvalue obeys

\[
|\lambda|\le 2\sqrt{k-1},
\]

with both \(\pm k\) removed from the trivial spectrum in the bipartite case.

The five Platonic skeleton graphs have spectra

\[
\operatorname{Spec}(T)=\{3^{(1)},(-1)^{(3)}\},
\]

\[
\operatorname{Spec}(C)=\{3^{(1)},1^{(3)},(-1)^{(3)},(-3)^{(1)}\},
\]

\[
\operatorname{Spec}(O)=\{4^{(1)},0^{(3)},(-2)^{(2)}\},
\]

\[
\operatorname{Spec}(D)=\{3^{(1)},(\sqrt5)^{(3)},1^{(5)},0^{(4)},(-2)^{(4)},(-\sqrt5)^{(3)}\},
\]

and

\[
\operatorname{Spec}(I)=\{5^{(1)},(\sqrt5)^{(3)},(-1)^{(5)},(-\sqrt5)^{(3)}\}.
\]

The deterministic validator constructs all five graphs and verifies the corresponding Ramanujan inequalities. Thus

\[
\boxed{T,C,O,D,I\text{ are all finite Ramanujan graphs.}}
\]

This is a graph-spectral statement, not a physical postulate.

## 3. The 36-node carrier

The current PhaseNav runtime uses an exact 36-component state. Its implementation groups the lanes as twelve ordered blocks of three. TIR therefore considers the cross-repository candidate carrier

\[
\boxed{G_{36}:=I_{12}\square K_3},
\]

where \(I_{12}\) is the 12-vertex icosahedral graph, \(K_3\) is the complete three-vertex local lane graph, and \(\square\) denotes the Cartesian graph product.

The adjacency operator is

\[
\boxed{A_{36}=A_I\otimes I_3+I_{12}\otimes A_{K_3}}.
\]

This construction preserves the existing ordered \(12\times3\) lane decomposition; it does not assign new semantic meanings to the 36 axes.

The degree is

\[
\deg(G_{36})=\deg(I_{12})+\deg(K_3)=5+2=7.
\]

Using the already-closed TIR constants

\[
(L_3,L_4,L_5)=(7,2,5),
\]

the degree identity becomes

\[
\boxed{\deg(G_{36})=L_5+L_4=L_3}.
\]

This is an independent structural crosscheck of the \(7=5+2\) closure in a 36-node spectral carrier. It is not used retroactively to derive the L-constants.

## 4. Exact product spectrum

For a Cartesian product of graphs, adjacency eigenvalues add. Since

\[
\operatorname{Spec}(I_{12})=\{5^{(1)},(\sqrt5)^{(3)},(-1)^{(5)},(-\sqrt5)^{(3)}\}
\]

and

\[
\operatorname{Spec}(K_3)=\{2^{(1)},(-1)^{(2)}\},
\]

the 36-node carrier has spectrum

\[
\boxed{
\begin{aligned}
\operatorname{Spec}(G_{36})=\{&7^{(1)},(2+\sqrt5)^{(3)},4^{(2)},\\
&(\sqrt5-1)^{(6)},1^{(5)},(2-\sqrt5)^{(3)},\\
&(-2)^{(10)},(-1-\sqrt5)^{(6)}\}.
\end{aligned}}
\]

The largest nontrivial absolute eigenvalue is

\[
\rho_{\rm nt}=2+\sqrt5.
\]

Because \(G_{36}\) is 7-regular, its Ramanujan bound is \(2\sqrt6\). Numerically,

\[
2+\sqrt5\approx4.2360679775<2\sqrt6\approx4.8989794856.
\]

Therefore

\[
\boxed{G_{36}\text{ is a Ramanujan graph.}}
\]

The graph has

\[
|V|=36,\qquad |E|=\frac{36\cdot7}{2}=126.
\]

A complete 36-node graph would have 630 undirected edges, so the carrier uses exactly one fifth as many undirected support edges. This is a combinatorial sparsity ratio only; it is not yet a measured runtime speedup.

## 5. Spectral gap

Let

\[
\mathcal L_{\rm norm}=I-\frac17A_{36}
\]

be the normalized graph Laplacian. The second-largest adjacency eigenvalue is \(2+\sqrt5\), so

\[
\boxed{\gamma_{36}=1-\frac{2+\sqrt5}{7}=\frac{5-\sqrt5}{7}\approx0.3948474318}.
\]

The gap is strictly positive because the carrier is connected. This gives a quantitative mixing/regularization scale without inventing a semantic metric on the 36 axes.

## 6. Candidate PhaseNav stability operator

Define an explicitly separate candidate regularizer

\[
\boxed{C_i^{\rm PR}(\phi)=-\frac{\beta}{7}\sum_j(A_{36})_{ij}\sin(\phi_i-\phi_j),\qquad\beta\ge0.}
\]

This term is **not** a replacement for the existing PhaseNav/HTRI coupling law. It is a candidate additive spectral regularizer.

Around a synchronized state \(\phi_i=\bar\phi+\delta_i\),

\[
\sin(\phi_i-\phi_j)=\delta_i-\delta_j+O(\|\delta\|^3),
\]

hence

\[
\dot\delta=-\frac{\beta}{7}L_{36}\delta+O(\|\delta\|^3),\qquad L_{36}=7I-A_{36}.
\]

On the mean-zero subspace the slowest linear mode therefore decays at rate at least

\[
\boxed{r_{\min}=\beta\gamma_{36}=\beta\frac{5-\sqrt5}{7}}.
\]

This is an exact **local linearized** stability bound for the declared candidate term. It is not a proof of global nonlinear synchronization, not a proof of stability after coupling to every existing PhaseNav term, and not a physical laboratory claim.

Two exact invariants follow from antisymmetry:

\[
\sum_i C_i^{\rm PR}=0,
\qquad
C^{\rm PR}(\phi+\alpha\mathbf1)=C^{\rm PR}(\phi).
\]

Thus the candidate preserves global phase covariance and does not inject a net common phase drift.

## 7. Orbital bridge

The icosahedral factor has multiplicity blocks \(1,3,5,3\); the first three match the dimensions of the \(s,p,d\) angular sectors, \(2\ell+1=1,3,5\) for \(\ell=0,1,2\). This motivates—but does not yet prove—a common finite angular/spectral carrier for orbital angular quadrature, PhaseNav channel transport, sparse HTRI/QHTRI support, and later Ramanujan lifts for larger angular bandwidth.

The radial orbital Hamiltonian is not modified by this module.

## 8. Evidence and claim classification

Exact finite statements: Platonic graph constructions and spectra, Ramanujan inequalities, Cartesian-product spectrum, 7-regularity, 126 edges, \(\rho_{\rm nt}=2+\sqrt5\), \(\gamma_{36}=(5-\sqrt5)/7\), and the local linearized decay bound for the explicitly declared regularizer.

TIR structural candidate: the identification

\[
G_{36}=I_{12}\square K_3
\]

as a bridge between current 36D PhaseNav runtime topology and the closed Platonic L-constant structure.

Open gates remain: full-runtime stability benefit, justified \(\beta\), sparse masking of adaptive coupling, measured latency/conditioning gains, Wigner/Gaunt orbital equivalence, continuous hyperbolic/Ramanujan-surface lift, and physical interpretation.

## 9. Validator

Reference validator:

`TIR/validation/tir_platonic_ramanujan_spectral_carrier_v0_1.py`

It constructs the five Platonic graphs directly, constructs the dodecahedral graph as the dual of the icosahedron, validates their spectra and Ramanujan bounds, builds \(G_{36}\), and checks connectivity, degree, edge count, spectrum, normalized gap, and the \(L_3=L_4+L_5\) degree identity.

Expected verdict:

```text
status = PASS
all_five_platonic_graphs_ramanujan = PASS
G36_degree = 7
G36_edges = 126
G36_rho_nontrivial = 2 + sqrt(5)
G36_ramanujan_bound = 2*sqrt(6)
G36_normalized_gap = (5 - sqrt(5))/7
physical_claim = false
```
