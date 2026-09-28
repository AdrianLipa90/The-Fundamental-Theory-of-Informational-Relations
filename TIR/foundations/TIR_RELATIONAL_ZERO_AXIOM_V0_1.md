# TIR Relational Zero Axiom v0.1

Status: `FOUNDATIONAL_DEFINITIONAL_THEOREM / RELATIONAL_ZERO_CLOSED / PHYSICAL_REALIZATION_NOT_YET_ENTERED`

Scope: canonical root semantics for the TIR primitive dependency chain. This surface distinguishes the pre-object relational zero from the later minimal support point and prevents a singleton carrier from being silently inserted into the zero layer.

## A0 — Relational existence principle

TIR does not take a self-standing object as primitive. An entity is admissible as an existent TIR object only through a realized distinction or relation that makes it identifiable relative to something else in the admitted relational presentation.

Write a relational presentation as

\[
\mathfrak R=(X,\mathcal D),
\]

where \(X\) is the support set and \(\mathcal D\) is the set of realized distinctions/relations carried by that presentation.

The relational zero is

\[
\boxed{
\mathfrak Z_{\rm rel}
=
(\varnothing,\varnothing).
}
\]

It is not an object, not a point, and not a singleton. It is the empty relational presentation: no support locus and no realized distinction.

Equivalently,

\[
X_0=\varnothing,
\qquad
\mathcal D_0=\varnothing.
\]

Therefore

\[
\boxed{
\nexists x\;(x\in X_0).
}
\]

### Logical status

The entry rule is definitional: TIR defines ontological admissibility relationally rather than by bare self-membership. Once that semantics is fixed, the absence of an existent object in \(\mathfrak Z_{\rm rel}\) is logically forced. This is not claimed to be a theorem of unrestricted first-order logic independent of definitions; it is an exact consequence of the TIR relational-existence definition.

This is the precise content of the phrase:

> nothing can exist at the zero layer because there is nothing to which it can stand in a realized relation.

Accordingly, zero is relational: \(0_{\rm rel}\) denotes zero realized relational structure, not a reified object called “nothing”.

## A1 — Minimal nonzero support

If the construction leaves \(\mathfrak Z_{\rm rel}\), the least nonempty support has one locus:

\[
\boxed{
\mathcal P=\{p\},
\qquad
|\mathcal P|=1.
}
\]

This is an ordinary minimal-cardinality statement. The point is the minimal nonzero support candidate.

Crucially,

\[
(\mathcal P,\varnothing)
\]

is still relationally unresolved. The point supplies support; it does not by itself satisfy the A0 relational-existence criterion. A nontrivial distinction must still be realized.

Thus the first two layers are not

\[
0\equiv\{p\},
\]

but rather

\[
\boxed{
\mathfrak Z_{\rm rel}
\prec_{\rm dep}
\mathcal P.
}
\]

## First nontrivial distinction

Let \(\Omega_{\mathcal P}\) be the state/aspect domain carried by the point support. A distinction is a partition \(\Pi\) of \(\Omega_{\mathcal P}\). It is nontrivial exactly when it has more than one nonempty block.

Hence every nontrivial distinction satisfies

\[
|\Pi|\ge 2.
\]

Minimality therefore fixes

\[
\boxed{
|\Pi_1|=2.
}
\]

Label the two blocks

\[
\boxed{
\Pi_1=\{N,S\}.
}
\]

The labels are relational poles/aspects of the minimal carrier. They need not be interpreted as two pre-existing spatial objects.

This establishes the dependency chain

\[
\boxed{
\mathfrak Z_{\rm rel}
\rightarrow
\mathcal P
\rightarrow
\{N,S\}.
}
\]

No exchange involution has been used to obtain the number of outcomes; binarity follows from the minimality of a nontrivial distinction.

## Exchange symmetry and the half

After the binary distinction exists, the primitive pole-exchange symmetry is

\[
J:N\leftrightarrow S,
\qquad
J^2=\mathrm{id}.
\]

For normalized nonnegative weights

\[
w_N+w_S=1,
\]

exchange invariance gives

\[
(w_N,w_S)=(w_S,w_N),
\]

and therefore

\[
\boxed{
w_N=w_S=\frac12.
}
\]

Equivalently, with \(u=w_S\),

\[
J(u)=1-u,
\qquad
\boxed{
\operatorname{Fix}(J)=\left\{\frac12\right\}.
}
\]

## First information value

For the binary Shannon carrier,

\[
H_2(u)=-(1-u)\ln(1-u)-u\ln u.
\]

At the exchange-fixed share,

\[
\boxed{
H_2(1/2)=\ln 2.
}
\]

Thus the exact scalar root is

\[
\boxed{
0_{\rm rel}
\rightarrow
\text{point support}
\rightarrow
\text{minimal binary distinction}
\rightarrow
\frac12
\rightarrow
\ln 2.
}
\]

## Quantum/projective lift boundary

The preceding chain does not yet assume quantum mechanics. If the TIR quantum-point postulate is then admitted, the two distinguished states have minimal complex span

\[
\mathcal H_2\cong\mathbb C^2.
\]

Projectivization gives the standard identity

\[
\mathbb{CP}^1\cong S^2,
\]

with the Fubini--Study metric on \(\mathbb{CP}^1\). This is downstream of the relational-zero and first-distinction theorem: the relational root does not silently assume the Bloch sphere, while the quantum lift does not alter the earlier zero semantics.

## Dependency certificate

\[
\boxed{
\text{A0 relational existence}
\rightarrow
0_{\rm rel}
\rightarrow
\text{A1 minimal support}
\rightarrow
\text{minimal nontrivial distinction}
\rightarrow
\{N,S\}
\rightarrow
\text{exchange symmetry}
\rightarrow
\frac12
\rightarrow
\ln2.
}
\]

Claim typing:

| Statement | Status |
|---|---|
| \(\mathfrak Z_{\rm rel}=(\varnothing,\varnothing)\) | DEFINITION |
| no object exists in \(\mathfrak Z_{\rm rel}\) | EXACT DEFINITIONAL CONSEQUENCE |
| minimal nonempty support is a singleton | EXACT SET-THEORETIC |
| a minimal nontrivial distinction has two outcomes | EXACT DEFINITIONAL / SET-THEORETIC |
| exchange-invariant normalized binary weights equal \((1/2,1/2)\) | EXACT |
| \(H_2(1/2)=\ln2\) | EXACT INFORMATION-THEORETIC |
| \(\mathbb C^2\) quantum lift | CONDITIONAL ON TIR QUANTUM-POINT POSTULATE |
| \(\mathbb{CP}^1\cong S^2\) with Fubini--Study geometry | STANDARD GEOMETRIC CONSEQUENCE OF THE COMPLEX TWO-STATE LIFT |

Firewall: the logical forcing claimed at A0 is internal to the explicitly declared relational semantics. No physical law, quantum structure, spacetime, or empirical statement is inferred from the empty presentation alone.
