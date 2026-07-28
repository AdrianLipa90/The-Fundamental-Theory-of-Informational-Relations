# Up-sector common-baseline no-go audit v10.4

## Status

- **Technical status:** PASS
- **Methodological status:** retrospective mathematical audit
- **Substantive status:** common additive baseline is insufficient for the fixed v10.2 up-sector trace
- **Physical spectrum status:** OPEN / NOT CLOSED
- **Canonical promotion:** DENIED
- **New mass formula proposed:** no

This audit corrects the research direction frozen in v10.3. It does not search for a better coefficient. It proves that no single common additive baseline can simultaneously remove the `u` offset and retain the present absolute `c/t` scale while the v10.2 relative trace is held fixed.

## 1. Architecture being tested

The v10.3 preregistration proposed

\[
\ln\frac{m_{u_g}}{m_e}=B_{\rm up}+\Delta_{\rm up}(g),
\qquad g\in\{u,c,t\},
\]

where one common `B_up` acts on all three up-type generations and the relative trace `Delta_up(g)` remains fixed.

Let the v10.2 logarithmic validation residual be

\[
r_g=\ln\frac{m_g^{\rm pred}}{m_g^{\rm val}}.
\]

Adding a common baseline shift `B` produces

\[
r'_g=r_g+B.
\]

## 2. Translation-invariance theorem

For any pair of generations,

\[
r'_g-r'_h=(r_g+B)-(r_h+B)=r_g-r_h.
\]

Therefore a common baseline cannot alter the spread of the residual set. If all translated residuals are required to satisfy

\[
|r'_g|\leq\varepsilon,
\]

then the intervals

\[
[-r_g-\varepsilon,-r_g+\varepsilon]
\]

must have a common intersection. For points on the real line this occurs if and only if

\[
\max_g r_g-\min_g r_g\leq 2\varepsilon.
\]

Equivalently, the smallest possible uniform absolute log error under any common translation is

\[
\varepsilon_{\min}=\frac{\max r-\min r}{2}.
\]

This is an elementary no-go result; it does not depend on the physical interpretation of the baseline.

## 3. v10.2 residuals

The already inspected v10.2 residuals are

| Slot | Log residual |
|---|---:|
| `u` | 3.1857238256 |
| `c` | 0.0818052322 |
| `t` | 0.2293790515 |

Their invariant spread is

\[
\Delta r
=3.1857238256-0.0818052322
=3.1039185934.
\]

Hence

\[
\boxed{\varepsilon_{\min}=1.5519592967}
\]

and at least one of the three channels must retain a multiplicative error of at least

\[
\boxed{e^{\varepsilon_{\min}}=4.7207104}.
\]

The minimax common shift is

\[
B_*=-\frac{\max r+\min r}{2}=-1.6337645289,
\]

which leaves

\[
|r'_u|=|r'_c|=1.5519592967,
\qquad
|r'_t|=1.4043854774.
\]

Thus even the mathematically optimal common shift does not approach the v10.2 non-`u` envelope of approximately `0.254`.

## 4. Consequence for v10.3

The original v10.3 demand was internally too restrictive. A common `B_up` preserves all `u:c:t` ratios. It can shift the whole sector, but it cannot repair the first-generation `u` position while keeping the existing absolute `c/t` agreement.

Therefore the following statement is now closed:

\[
\boxed{
\text{common additive up-sector baseline}
\;\not\Rightarrow\;
\text{closure of the v10.2 up-sector residuals}
}
\]

This is a no-go for the **architecture**, not a no-go for Collatz quarter-power scaling or for a richer sector geometry.

## 5. Revised admissible direction

The repository already distinguishes two structural up-type regimes before v10.4:

- `u`: `light_quark_seed`, based on the light `(11,13)` orientation sector;
- `c,t`: `heavy_quark_resonance`, based on the `(101,103)` resonance sector and explicitly quarantined as an old-document bridge ansatz.

The next candidate may therefore investigate a structural decomposition

\[
\ln\frac{m_{u_g}}{m_e}
=
B_{s(g)}+\Delta_{s(g)}(g),
\]

where `s(g)` is a pre-existing sector label, not the particle name. This does **not** license a `u`-specific correction. Any split must be derived from the already declared seed, colour, chiral and Euler--Berry geometry, and the heavy-sector source quarantine must remain visible.

An alternative is to revise the up-sector relative release itself from structural inputs. Either path remains retrospective when checked only on the known charged-fermion table.

## 6. Integrity rules retained

- no use of the factor `24.18` as a design target;
- no residual-derived coefficient;
- no branch keyed directly by `u`, `c`, or `t`;
- no silent promotion of `old_doc_bridge_ansatz_quarantined` inputs;
- Ramanujan remains mandatory;
- the electron remains the only dimensional mass anchor in the current architecture;
- any result on the existing mass table is hypothesis-generating only;
- promotion requires an independently preregistered observable.

## 7. Execution

```bash
python TIR/validation/up_sector_common_baseline_no_go_v10_4.py
```

Output:

- `TIR/validation/results/up_sector_common_baseline_no_go_v10_4.json`
