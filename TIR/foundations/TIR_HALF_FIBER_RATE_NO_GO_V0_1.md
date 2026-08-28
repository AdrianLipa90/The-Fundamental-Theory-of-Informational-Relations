# TIR Half-Fiber Phase-Rate No-Go v0.1

Status: `EXACT_CONDITIONAL_UNDERDETERMINATION_CANDIDATE`

Scope: TIR-only boundary theorem. The eight-axiom kernel and the half-seam phase-fiber construction determine the binary carrier, its symmetric half-point, the `U(1)` relative-phase fiber, and the admissible continuous unitary orbit structure. They do not select a unique non-zero phase rate without an additional dynamical or temporal input.

## 1. Static half-fiber already fixed

The current foundation chain supplies

\[
\boxed{
\nu=2,
\qquad
p_N=p_S=\frac12,
\qquad
H_2=\ln2,
\qquad
\mathcal H_2\cong\mathbb C^2.
}
\]

The coherent half family is

\[
\boxed{
|\psi_{1/2}(\varphi)\rangle
=\frac{|N\rangle+e^{i\varphi}|S\rangle}{\sqrt2},
\qquad
\varphi\in U(1).
}
\]

Thus the static structure fixes the phase domain but not a phase velocity.

## 2. Continuous phase-flow family

Introduce an external continuous parameter \(\tau\) only as a group parameter. For every real constant \(\omega\), define

\[
\varphi_\omega(\tau)=\varphi_0+\omega\tau
\]

and

\[
|\psi_\omega(\tau)\rangle
=\frac{|N\rangle+e^{i(\varphi_0+\omega\tau)}|S\rangle}{\sqrt2}.
\]

Each \(\omega\in\mathbb R\) defines a strongly continuous one-parameter unitary orbit preserving

\[
|\alpha|^2=|\beta|^2=\frac12.
\]

Therefore all values of \(\omega\) preserve the exact binary half-seam probabilities and entropy.

## 3. Reparameterization degeneracy

Let

\[
\tau'=a\tau,
\qquad a>0.
\]

Then

\[
\varphi_0+\omega\tau
=
\varphi_0+\frac{\omega}{a}\tau'.
\]

Hence the same geometric phase orbit can be described with

\[
\boxed{\omega' = \frac{\omega}{a}.}
\]

The static orbit geometry is invariant under this positive rescaling of the group parameter.

Consequently, no statement involving only the static carrier, half probabilities, `U(1)` topology, Bloch geometry, winding class, or pole-exchange symmetry can determine the absolute numerical value of \(\omega\).

## 4. Phase-rate underdetermination theorem

### Theorem

Let the TIR half-fiber satisfy:

1. binary equal probabilities \((1/2,1/2)\);
2. coherent relative phase \(\varphi\in U(1)\);
3. continuous unitary evolution in a parameter \(\tau\);
4. no independent physical normalization of \(\tau\).

Then the absolute phase rate

\[
\omega=\frac{d\varphi}{d\tau}
\]

is underdetermined up to positive rescaling of \(\tau\).

Equivalently,

\[
\boxed{
\text{static half-fiber structure}
\not\Rightarrow
\text{unique absolute }\omega.
}
\]

The remaining free continuous coordinate is exactly the generator/rate scale.

## 5. Relation to the existing TIR phase-information identity

TIR defines

\[
\kappa=\frac{\ln2}{24\pi}
\]

and

\[
d\mathcal I=\kappa\,d\varphi.
\]

Therefore

\[
\boxed{
\Gamma_{\mathcal I}
=\frac{d\mathcal I}{d\tau}
=\kappa\omega.
}
\]

If \(\omega=2\pi f\), then

\[
\boxed{
\Gamma_{\mathcal I}=\frac{\ln2}{12}f.
}
\]

The already-reviewed TIR constraint subsystem

\[
(\kappa,\omega,f,\Gamma_{\mathcal I})
\]

has one continuous degree of freedom after its three defining constraints are imposed. The half-fiber analysis identifies the geometric location of that surviving degree of freedom: it is the unfixed phase-rate scale along the `U(1)` fiber.

## 6. What TIR has now fixed before temporal dynamics

The foundation closes the following structure:

\[
\boxed{
\text{POINT}
\rightarrow
\text{FIRST DISTINCTION}
\rightarrow
2
\rightarrow
\frac12
\rightarrow
\ln2
\rightarrow
\mathbb C^2
\rightarrow
U(1)_{\rm half}
\rightarrow
\omega\;\text{free}.
}
\]

The final free rate is not a defect in the derivation. It is the exact boundary between static relational structure and temporal/dynamical normalization.

## 7. Typed crosslink to Informational Dynamics of Time

TIR can now export a sharper packet:

```text
binary_carrier       = C^2
probability_seam     = (1/2, 1/2)
information_seam     = ln2
phase_fiber          = U(1) ~= S1
bloch_fiber          = equator z=0
phase_coordinate     = phi
phase_rate           = omega = dphi/dtau
information_rate     = Gamma_I = kappa * omega
rate_status          = FREE_CONTINUOUS_COORDINATE
normalization_needed = temporal/dynamical input
```

The sibling temporal programme may supply the missing normalization at its `TIR -> Temporal Primitive` boundary. TIR retains authority over the static relational packet and the underdetermination theorem.

## 8. Schrödinger boundary

For a strongly continuous unitary flow there is a self-adjoint generator `G` with

\[
U(\tau)=e^{-iG\tau/\hbar}.
\]

The corresponding generator equation is

\[
\boxed{
i\hbar\frac{d}{d\tau}|\psi\rangle=G|\psi\rangle.
}
\]

The theorem above shows that the static axioms determine the admissible carrier and phase orbit while leaving the generator scale tied to the normalization of \(\tau\). A physical-time/Hamiltonian identification is therefore a genuinely new dynamical input rather than a hidden consequence of the static half construction.

## 9. Claim classes

| Statement | TIR class |
|---|---|
| half-fiber is `U(1)` | EXACT GEOMETRIC LIFT |
| every constant `omega` gives an equal-probability unitary phase orbit | EXACT |
| `tau -> a tau` implies `omega -> omega/a` for the same phase path | EXACT |
| static half structure does not select an absolute phase-rate scale | EXACT CONDITIONAL UNDER DECLARED PARAMETER FREEDOM |
| `Gamma_I=kappa omega` | EXISTING EXACT CONDITIONAL TIR IDENTITY |
| one continuous degree remains in `(kappa,omega,f,Gamma_I)` | EXISTING EXACT CONDITIONAL CONSTRAINT RESULT |
| temporal normalization of the free rate | CROSSLINK INPUT TO DYNAMICS OF TIME |

## 10. Next TIR question

The next TIR-only question is no longer “what is the phase fiber?” or “does a generator exist?”. It is:

\[
\boxed{
\text{Can any existing TIR invariant fix a dimensionless ratio of phase rates without importing time?}
}
\]

Absolute temporal normalization remains outside this static foundation gate.
