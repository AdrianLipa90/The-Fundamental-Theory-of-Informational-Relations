# XF-2A — Constant Xi-Branch Mixing Class Audit

Status: `EXACT_MARGIN_IDENTITY / NUMERICAL_SIGN_CHANGE_PASS / CONSTANT_REAL_MIXING_CLASS_FAIL`

Let

\[
X(z):=\Xi(z)=A_+(z)+A_-(z),
\qquad
D(z):=A_-(z)-A_+(z).
\]

For the real Riemann kernel,

\[
X^{\#}=X,
\qquad
D^{\#}=-D.
\]

Consider the full constant real antisymmetric mixing family

\[
E_c(z):=X(z)+cD(z),
\qquad c\in\mathbb R.
\]

Then

\[
E_c^{\#}(z)=X(z)-cD(z),
\]

and every member preserves the symmetric Xi reconstruction:

\[
\boxed{
\Xi(z)=\frac12\left(E_c(z)+E_c^{\#}(z)\right).
}
\]

Its Hermite–Biehler margin is exactly

\[
\begin{aligned}
|E_c|^2-|E_c^{\#}|^2
&=4c\,\Re\!\left(X\overline D\right)\\
&=4c\left(|A_-|^2-|A_+|^2\right).
\end{aligned}
\]

Therefore a fixed nonzero real \(c\) can satisfy the Hermite–Biehler sign condition throughout the upper half-plane only if the raw branch margin

\[
\Delta(z)=|A_-(z)|^2-|A_+(z)|^2
\]

has one global sign there.

The XF-1 numerical evaluator gives two reproducible upper-half-plane witnesses at \(\Im z=0.1\):

\[
\Delta(10+0.1i)
\approx
+4.2545370906168767\times10^{-4},
\]

\[
\Delta(17+0.1i)
\approx
-2.5296379021628202\times10^{-6}.
\]

The sign change is pinned by `tests/test_xi_kernel.py`.

Hence the constant real antisymmetric branch-mixing family is classified

\[
\boxed{
\texttt{CONSTANT\_REAL\_BRANCH\_MIXING\_HB = FAIL}.
}
\]

This removes an entire one-parameter repair class, not only the raw choice \(E=2A_-\). The next de Branges candidate must contain genuinely \(z\)-dependent or operator-derived structure. A rigorous interval/error-bound certificate for the numerical sign witnesses remains an independent validation target.
