# TIR First Distinction Theorem v0.2

Status: `EXACT_CONDITIONAL_PRIMITIVE_FOUNDATION_CANDIDATE`

Scope: TIR-only primitive derivation of the first relational distinction from the relational-zero definition, point-support minimality, information primacy, and exchange symmetry. This version keeps ordinary meta-mathematical cardinality separate from the later TIR claim about physical emergence of natural-number closure indices.

## 0. Relational-zero boundary

By A0, the pre-object relational presentation is

\[
\boxed{
\mathfrak Z_{\rm rel}=(\varnothing,\varnothing).
}
\]

No object is present at this layer:

\[
\boxed{
\nexists x\;(x\in X_0).
}
\]

This is an exact consequence of the TIR relational-existence definition. Relational zero is not identified with a singleton.

## 1. Primitive support

By A1, the least nonempty support candidate is

\[
\boxed{
\mathcal P=\{p\},
\qquad
|\mathcal P|=1.
}
\]

The unresolved presentation \((\mathcal P,\varnothing)\) supplies support but no realized relation. It is therefore upstream of, rather than identical with, the first admitted distinction.

## 2. Minimal nontrivial distinction and exchange orbit

Let \(\Omega_{\mathcal P}\) denote the state/aspect domain carried by the point support. A distinction is a partition \(\Pi\) of this domain. Nontriviality requires more than one nonempty block,

\[
|\Pi|>1.
\]

The least possible nontrivial partition therefore has exactly two blocks:

\[
\boxed{
|\Pi_1|=2.
}
\]

Rename them

\[
\boxed{
\Pi_1=\{N,S\}.
}
\]

### Theorem 1 — Minimal Binary Distinction

Every nontrivial partition has at least two nonempty blocks. Therefore the minimal nontrivial distinction is binary.

This result does not use exchange symmetry to obtain the number of outcomes.

After the binary distinction exists, A7 supplies the primitive exchange action

\[
\boxed{
J:N\leftrightarrow S,
\qquad
J^2=\mathrm{id}.
}
\]

Choosing \(x=N\),

\[
Jx=S\neq x,
\qquad
\mathcal O_J(x)=\{x,Jx\}=\{N,S\}.
\]

Thus the involution is the symmetry of the already established binary relation, not the premise from which binarity is inferred.

## 3. Unique symmetric normalized share

By A3 attach normalized relational weights

\[
w_N,w_S\ge0,
\qquad
w_N+w_S=1.
\]

By A7 the unresolved primitive distinction is invariant under pole exchange,

\[
J:(N,S)\mapsto(S,N).
\]

Weight invariance gives

\[
(w_N,w_S)=(w_S,w_N),
\]

hence

\[
w_N=w_S.
\]

Together with normalization,

\[
\boxed{w_N=w_S=\frac12}.
\]

### Theorem 2 — Unique Exchange-Invariant Share

The unique normalized nonnegative weight assignment invariant under exchange of the two primitive poles is

\[
\boxed{\left(\frac12,\frac12\right)}.
\]

## 4. Half-seam coordinate

Set

\[
u=w_S,
\qquad
w_N=1-u.
\]

Pole exchange acts as

\[
J(u)=1-u.
\]

Its fixed point satisfies

\[
u=1-u,
\]

therefore

\[
\boxed{u_\star=\frac12}.
\]

Thus the exchange-invariant probability vector and the relational half-seam are the same primitive object in two coordinate descriptions:

\[
\boxed{
(w_N,w_S)=\left(\frac12,\frac12\right)
\Longleftrightarrow
\operatorname{Fix}(u\mapsto1-u)=\left\{\frac12\right\}.
}
\]

## 5. First symmetric information value

Using the A3 binary Shannon carrier

\[
H_2(u)=-(1-u)\ln(1-u)-u\ln u,
\]

the primitive symmetric distinction gives

\[
\boxed{H_2(1/2)=\ln2}.
\]

The exact primitive chain is therefore

\[
\boxed{
\mathfrak Z_{\rm rel}
\rightarrow
\mathcal P
\rightarrow
\{N,S\}
\xrightarrow{\text{exchange invariance}}
\left(\frac12,\frac12\right)
\xrightarrow{H_2}
\ln2.
}
\]

## 6. Axiom dependency certificate

The minimal TIR parent set for the scalar chain is:

- `A0`: defines relational existence and the empty relational zero;
- `A1`: supplies the minimal nonempty support candidate;
- minimal nontrivial partition: supplies the binary distinction without assuming an involution;
- `A7`: supplies exchange symmetry and invariance;
- `A3`: supplies normalized informational weights and Shannon information.

`A2` enters only at the coherent quantum lift of the already established pole pair.

`A4`, `A5`, `A6`, and `A8` are separate converging or downstream branches at this stage.

## 7. Quantum lift after the scalar theorem

By A2 represent the two distinguished poles as an orthonormal quantum basis

\[
|N\rangle,\;|S\rangle.
\]

Their minimal complex span is

\[
\boxed{\mathcal H_{NS}\cong\mathbb C^2}.
\]

The half-balanced coherent family is

\[
\boxed{
|\psi_{1/2}(\varphi)\rangle
=
\frac{|N\rangle+e^{i\varphi}|S\rangle}{\sqrt2}.
}
\]

This quantum lift remains part of the primitive structural packet. Temporal parametrization of `\varphi` belongs to the Time branch.

## 8. Primitive theorem output

```text
relational_zero         = EMPTY_RELATIONAL_PRESENTATION
primitive_carrier       = POINT_SUPPORT
first_distinction       = MINIMAL_NONTRIVIAL_BINARY_PARTITION
primitive_relation      = EXCHANGE_INVOLUTION_ON_BINARY_DISTINCTION
first_orbit             = {N,S}
exchange_fixed_share    = (1/2,1/2)
half_seam               = 1/2
symmetric_information   = ln2
quantum_lift             = C^2
relative_phase_domain   = U(1)
```

This output feeds the common TIR causal core before the Standard Model, Time, and Space branches separate.
