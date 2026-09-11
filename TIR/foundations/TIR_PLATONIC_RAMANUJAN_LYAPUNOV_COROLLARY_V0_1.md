# TIR Platonic–Ramanujan Lyapunov Corollary v0.1

Status: `EXACT_CONDITIONAL_COROLLARY / PHASENAV_FULL_RUNTIME_BINDING_OPEN`

Parent: `TIR_PLATONIC_RAMANUJAN_SPECTRAL_CARRIER_V0_1`

Let the parent 36-node carrier be

\[
G_{36}=I_{12}\square K_3
\]

with adjacency \(A\), degree \(7\), and candidate phase regularizer

\[
\dot\phi_i=C_i^{PR}=-\frac{\beta}{7}\sum_jA_{ij}\sin(\phi_i-\phi_j),\qquad\beta\ge0.
\]

Define the disagreement potential

\[
\boxed{
V(\phi)=\sum_{(i,j)\in E(G_{36})}\left(1-\cos(\phi_i-\phi_j)\right).
}
\]

Because every undirected edge occurs once,

\[
\frac{\partial V}{\partial\phi_i}
=\sum_jA_{ij}\sin(\phi_i-\phi_j).
\]

Therefore

\[
\boxed{
\dot\phi=-\frac{\beta}{7}\nabla V.
}
\]

Along the isolated regularizer flow,

\[
\boxed{
\dot V
=\nabla V\cdot\dot\phi
=-\frac{\beta}{7}\|\nabla V\|_2^2
\le0.
}
\]

Thus the Platonic–Ramanujan candidate has an exact global Lyapunov monotonicity property as an isolated continuous-time subsystem.

Additional exact facts are

\[
0\le V(\phi)\le2|E|=252,
\]

\[
V(\phi+\alpha\mathbf1)=V(\phi),
\]

and

\[
\sum_iC_i^{PR}=0.
\]

Near the synchronized manifold, the parent spectral gap yields

\[
\dot\delta=-\frac{\beta}{7}L\delta+O(\|\delta\|^3)
\]

and mean-zero linear decay rate at least

\[
\boxed{
\beta\frac{5-\sqrt5}{7}.
}
\]

## Boundary

The corollary does **not** prove that every initial phase configuration converges to complete synchronization: the nonlinear graph potential can have other critical configurations. It also does not prove that \(V\) is monotone after adding the existing PhaseNav v0.32 frequency, adaptive-coupling, target-control, gravity/tau/flavour or QHTRI terms.

Therefore the exact status is:

```text
isolated candidate Lyapunov monotonicity = PROVED
local synchronized-manifold contraction rate = PROVED
full PNCS v0.32 + candidate stability = OPEN BENCHMARK
unique/global synchronization = NOT CLAIMED
physical stability claim = NOT CLAIMED
```

The corresponding PhaseNav implementation is kept non-actuating and disabled by default until comparative runtime validation.
