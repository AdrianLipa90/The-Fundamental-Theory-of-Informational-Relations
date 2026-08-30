# XF-5 — Nonlocal transverse curvature of the Riemann Xi surface

## Status ledger

- `EXACT`: transverse-curvature identity
- `EXACT`: differentiated theta-kernel identity
- `STANDARD`: equivalence between XF-4 strict positivity and strict transverse convexity on the open critical-strip parameter range
- `STANDARD`: strict transverse convexity plus the outer-halfplane growth closure yields the classical Xi growth criterion
- `OPEN_RH_EQUIVALENT_CRITERION`: global strict positivity / strict transverse convexity
- `LITERATURE_NO_GO`: universal phase-aligned blockwise positivity in the Planat theta-kernel decomposition is obstructed by nonlocal cancellation

## 1. Coordinates

Use

\[
\Xi(z)=\xi\!\left(\frac12+i z\right),\qquad z=x+i y,
\]

with real `x,y`. The XF-4 scalar is

\[
Q_\Xi(x,y)
=|\Xi'(z)|^2
-\operatorname{Re}\!\left(\Xi(z)\overline{\Xi''(z)}\right).
\]

The RH-equivalent XF-4 domain is

\[
x\in\mathbb R,\qquad 0<|y|<\frac12.
\]

## 2. Exact transverse-curvature identity

Because `Xi` is a real-entire function,

\[
\overline{\Xi(x+i y)}=\Xi(x-i y).
\]

Define

\[
F_x(y)=|\Xi(x+i y)|^2
      =\Xi(x+i y)\Xi(x-i y).
\]

Differentiating twice in `y` gives

\[
F_x''(y)
=2|\Xi'(x+i y)|^2
-2\operatorname{Re}\!\left(
\Xi(x+i y)\overline{\Xi''(x+i y)}
\right).
\]

Therefore

\[
\boxed{
\frac12\,\partial_y^2|\Xi(x+i y)|^2
=Q_\Xi(x,y)
}
\]

exactly.

Hence the XF-4 condition

\[
Q_\Xi(x,y)>0
\]

is equivalent, on the same domain, to

\[
\partial_y^2|\Xi(x+i y)|^2>0.
\]

This is the XF-5 strict-transverse-convexity interface.

## 3. Growth bridge

`F_x(y)` is even in `y`, so

\[
F_x'(0)=0.
\]

If the OPEN XF-5 strict-convexity condition holds for

\[
0<y<\frac12,
\]

then

\[
F_x'(y)>0
\]

throughout that interval. The region `y>=1/2`, corresponding to
`Re(s)>=1`, is closed by the standard symmetric-Hadamard/logarithmic-
derivative positivity argument. Combining the two regions recovers the
classical Xi growth route associated with Hinkkanen and Lagarias.

The logical direction recorded by the solver is

```text
Q_Xi global strict positivity
    <=> strict transverse convexity in 0<|y|<1/2
    => positive vertical growth in 0<y<1/2
    + outer-halfplane growth closure
    => full Xi growth criterion
    => RH
```

The first premise in this chain retains `OPEN_RH_EQUIVALENT_CRITERION`.

## 4. TIR theta-kernel normalization

The verified repository normalization is

\[
\Xi(z)=2\int_0^\infty \Phi(u)\cos(zu)\,du.
\]

Set

\[
D(z)=\int_0^\infty \Phi(u)\cos(zu)\,du=\frac12\Xi(z).
\]

With

\[
u=a+b,\qquad v=a-b,\qquad a>|b|,
\]

and

\[
M(a,b)=\Phi(a+b)\Phi(a-b),
\]

the symmetrized first-growth kernel is

\[
K_{x,y}(a,b)
=\frac a2\cos(2xb)\sinh(2ya)
+\frac b2\cos(2xa)\sinh(2yb).
\]

Differentiation in `y` gives the local curvature kernel

\[
\boxed{
L_{x,y}(a,b)
:=\partial_yK_{x,y}(a,b)
=a^2\cos(2xb)\cosh(2ya)
+b^2\cos(2xa)\cosh(2yb)
}.
\]

Under the TIR normalization,

\[
\boxed{
Q_\Xi(x,y)
=4\iint_{a>|b|}M(a,b)L_{x,y}(a,b)\,da\,db
}.
\]

This is the XF-5 nonlocal-curvature representation.

## 5. Exact anchor at x=0

At `x=0`,

\[
L_{0,y}(a,b)
=a^2\cosh(2ya)+b^2\cosh(2yb)>0
\]

for every interior point `a>|b|` with `a>0`. Since

\[
M(a,b)>0,
\]

the curvature integrand is pointwise positive on this slice. This recovers
the origin-sign anchor used by the XF-4 Wiener argument through a direct
kernel statement.

## 6. Nonlocality firewall

Michel Planat's 2026 theta-kernel work gives an exact decomposition of the
first growth derivative into longitudinal and transverse oscillatory sectors.
The peer-reviewed communication records the phase-aligned block programme and
the companion result; the companion August 2026 preprint proves that the two
sectors cancel to all algebraic orders as `x -> infinity` and that universal
phase-aligned block positivity fails in that representation.

Repository consequence:

```text
GLOBAL CORRELATED SIGN CONTROL: admissible research route
UNIVERSAL INDEPENDENT PHASE-ALIGNED BLOCK POSITIVITY: literature no-go firewall
FINITE BLOCK SAMPLING: numerical diagnostic
```

The no-go scope is representation-specific. The active XF-5 frontier is
therefore a globally coupled identity, exact resummation, or another
correlation structure capable of controlling the sign of the complete
curvature integral.

## 7. Falsification targets

XF-5 exposes concrete targets:

1. an analytic global lower bound for the complete curvature integral;
2. an exact resummation preserving longitudinal/transverse cancellation;
3. a positive-definite representation of the fully coupled integral;
4. a counterexample `(x,y)` in the admissible strip with `Q_Xi(x,y)<=0`;
5. a proof that any proposed local partition loses the exponentially small
   remainder carrying the global sign.

Finite numerical positivity has `NUMERICAL_DIAGNOSTIC` status.

## References

- D. K. Dimitrov and Y. Xu, *Wronskians of Fourier and Laplace transforms*, arXiv:1606.05011 (2016).
- J. C. Lagarias, *On a positivity property of the Riemann xi-function*, Acta Arith. 89 (1999), 217–234.
- M. Planat, *A Theta-Kernel Reformulation of Riemann-Xi Growth and the Obstruction to Blockwise Positivity*, Symmetry 18 (2026), 1283, DOI: 10.3390/sym18081283.
- M. Planat, *Nonlocal Cancellation in a Theta-Kernel Decomposition of the Riemann Xi-Growth Derivative: An Obstruction to Phase-Aligned Blockwise Positivity*, Preprints.org, posted 25 August 2026.
