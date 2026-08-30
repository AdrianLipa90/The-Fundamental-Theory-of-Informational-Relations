# The Fundamental Theory of Informational Relations

https://www.researchgate.net/publication/408131825_Metatime_A_Low-Parameter_Ansatz_for_Standard_Model_Parameters_from_Geometric_Phase_Information_Theory

**Author:** Adrian Lipa — Independent Researcher, Doncaster, United Kingdom  
**Current monograph:** TIR v12 content-migration candidate  
**Working branch:** `feat/tir-monograph-v12-structural-skeleton`  
**Publication status:** dependency-ordered content migration with exact/conditional/empirical gates tracked separately

## Overview

The **Fundamental Theory of Informational Relations (TIR)** is a research programme that develops a dependency-ordered relation between primitive informational structure, quantum/projective geometry, spatial transport, flavour structure, particle-sector relations and falsifiable empirical tests.

The current v12 monograph uses the causal spine

```text
0
-> POINT
-> FIRST DISTINCTION
-> {N,S}
-> 1/2
-> ln2
-> C^2
-> Herm_0(2) ~= R^3
-> Euclidean relational geometry
-> tetrahedral closure
-> connection / holonomy / SE(3) / solder / torsion
-> flavour carrier
-> kappa normalization
-> particle and gauge sectors
-> evidence and prospective tests
```

Historical v11 sources remain versioned provenance.

## Canonical kappa normalization

The current internal TIR normalization surface derives

\[
\boxed{
\kappa=\frac{\ln2}{24\pi}
}
\]

from the already established three-flavour mixing carrier:

\[
V_F\cong\mathbb C^3,
\qquad
U_F\in SU(3)_F,
\qquad
\dim_{\mathbb R}\mathfrak{su}(3)_F=8.
\]

The mixing-channel count is

\[
N_{\rm mix}
=
N_F(N_F^2-1)
=
3(3^2-1)
=
24.
\]

The primitive half coordinate supplies the half-turn phase

\[
\Delta\phi_{1/2}=\pi,
\]

so

\[
\Phi_{\rm mix}=24\pi,
\qquad
H_2(1/2)=\ln2,
\]

and therefore

\[
\boxed{
\kappa
=
\frac{H_2(1/2)}{\Phi_{\rm mix}}
=
\frac{\ln2}{24\pi}.
}
\]

Canonical source:

`TIR/foundations/TIR_KAPPA_FLAVOUR_MIXING_NORMALIZATION_V0_1.md`

Deterministic audit:

`TIR/validation/tir_kappa_flavour_mixing_normalization_v0_1.py`

The independent tetrahedral symmetry crosscheck is

\[
3\,\dim\mathfrak{su}(3)_F
=
24
=
|S_4|.
\]

## Exact phase-rate consequence

For

\[
d\mathcal I=\kappa\,d\phi,
\qquad
\omega=\frac{d\phi}{dt}=2\pi f,
\]

the exact conditional identity is

\[
\boxed{
\Gamma_{\mathcal I}
=
\frac{d\mathcal I}{dt}
=
\kappa\omega
=
\frac{\ln2}{12}f
},
\qquad
\boxed{
\Delta\mathcal I_{\rm cycle}
=
\frac{\ln2}{12}.
}
\]

The four quantities
\((\kappa,\omega,f,\Gamma_{\mathcal I})\)
obey three independent constraints and form a one-dimensional regular constraint manifold under the declared definitions. The physical observable binding of \(\Gamma_{\mathcal I}\) remains an `OPEN` operational gate.

## Emergent geometry

The binary quantum carrier gives the normalized state affine hull

\[
\mathcal A_2
=
\frac12I+\operatorname{Herm}_0(2),
\qquad
\operatorname{Herm}_0(2)\cong\mathbb R^3.
\]

The canonical ordered endpoint relation is

\[
\boxed{
\mathcal E_{xy}
=
2(\rho_y-\rho_x)
\in\operatorname{Herm}_0(2).
}
\]

It obeys

\[
\mathcal E_{yx}=-\mathcal E_{xy},
\qquad
\mathcal E_{xz}=\mathcal E_{xy}+\mathcal E_{yz}.
\]

The invariant local metric is

\[
\boxed{
\langle A,B\rangle
=
\frac12\operatorname{Tr}(AB),
}
\]

which becomes the Euclidean dot product in Pauli coefficients. Full local adjoint \(SO(3)\) isotropy stabilizes rank three.

Minimal finite full isotropy then forces the regular tetrahedral Gram class,

\[
\mathbf n_a\cdot\mathbf n_b=-\frac13
\qquad(a\neq b),
\]

with

\[
\hat a=\sqrt{\frac83},
\qquad
\hat V_{\Delta^3}=\frac{8}{9\sqrt3}.
\]

The minimal symmetric informationally complete qubit frame independently reaches the same tetrahedral congruence class.

## Connection, holonomy and torsion

The typed connection family is

\[
W_{ij}^{WT}\in U(1),
\qquad
W_{ij}^{X}\in SU(2),
\qquad
W_{ij}^{c}\in SU(3).
\]

For the spatial branch,

\[
R_{ij}
=
\operatorname{Ad}_{W_{ij}^{X}}
\in SO(3),
\]

and the affine connection lift is

\[
\boxed{
G_{ij}^{\nabla}
=
(R_{ij},\mathbf e_{ij})
\in SE(3).
}
\]

Pure affine-atlas transitions satisfy an exact \(SE(3)\) cocycle and give the zero-holonomy baseline. On a rotationally consistent connection triangle,

\[
R_C=I,
\]

and the translational loop source satisfies

\[
\boxed{
\mathbf t_C
=
-\mathbf c_{xyz}
=
\operatorname{vec}(\mathcal T_{xyz}).
}
\]

The next geometry theorem is controlled refinement of the discrete solder/torsion and rotational-holonomy data to Cartan torsion and curvature.

## Evidence architecture

Version 12 represents publication status by the ordered triple

```text
(Claim Class, Timing, Verdict)
```

defined in

`TIR/monograph/v12/STATUS_TAXONOMY.md`.

Sector chapters own formulas and provenance. Chapter 19, **Unified Evidence Matrix**, owns current observable-level verdicts.

Current retained evidence includes:

- CKM retrospective compatibility in the frozen PDG-2026 matrix;
- PMNS reactor-angle tension;
- charged-lepton precision failures;
- baryon and meson provenance/formula quarantines;
- electroweak precision failures plus the common scheme/scale closure gate;
- the retained neutron-EDM physical failure;
- exact Standard Model local anomaly cancellations and the even Witten doublet count;
- cosmological arithmetic and dimensionful-conversion quarantine.

A technical calculation and an empirical verdict remain separate axes throughout the repository.

## Electroweak closure gate

The current structural values

\[
g_0=\frac{24}{35},
\qquad
\sin^2\theta_W^{(0)}=\frac29+\kappa
\]

combined through \(e_0=g_0\sin\theta_W^{(0)}\) imply an electromagnetic coupling different from the separate TIR \(\alpha^{-1}\) relation. Version 12 therefore promotes the common binding target

\[
\boxed{
(g_0,\theta_W^{(0)},\alpha_0,v_0)
\xrightarrow{\mathcal R_{EW}(\mu,\mathrm{scheme})}
(g,e,\theta_W,\alpha,v)_{\mu,\mathrm{scheme}}.
}
\]

This common transport is upstream of renewed \(W\), \(Z\), Higgs and precision-electroweak evidence evaluation.

## Prospective programme

The active prospective family is the frozen v10.7 separable architecture

\[
\ln y_{f,g}=F(S_f)+D(G_g,R_g).
\]

Exactly three candidates are frozen. The two orthogonal primary observables are

- `y_c / y_mu`, isolating the sector functional;
- `y_c / y_t`, isolating the generation-release operator.

Frozen predictions:

| Candidate | `y_c / y_mu` | `y_c / y_t` |
|---|---:|---:|
| C1 | 4.850346751338371 | 0.16766796647328305 |
| C2 | 2.3521800134268784 | 0.17147213462587316 |
| C3 | 6.858021228826222 | 2.8101955040512466e-11 |

The no-refit rule and assigned likelihood gates are preserved in Chapter 20.

## Completion frontier

Chapter 21 maintains the remaining theorem programme as a directed acyclic dependency graph. The current receipt records 23 resolved nodes: eight closed root surfaces and fifteen open gates.

Principal open gates include:

1. discrete-to-continuum Cartan refinement;
2. zero-torsion spatial sector;
3. TIR–IDT ADM join and Einstein closure;
4. coefficient magnitude forcing;
5. continuum gauge normalization/running;
6. common electroweak scheme/scale transport;
7. Higgs scalar-action binding;
8. holonomic strong-CP source;
9. meson absolute-action baseline;
10. neutrino absolute-action repair;
11. cosmological dimensionful scale binding;
12. native Li/Weil positivity closure.

## Repository map

```text
TIR/
├── foundations/
├── integration/
├── interfaces/
├── standard_model/
├── validation/
├── subrepos/
│   └── the-space-of-geometry/
└── monograph/
    ├── tir_monograph_v12.tex
    ├── v12/
    │   ├── STATUS_TAXONOMY.md
    │   ├── MIGRATION_MANIFEST.yaml
    │   ├── chapters/
    │   └── appendices/
    └── metatime_monograph.tex
```

The v12 master is

`TIR/monograph/tir_monograph_v12.tex`.

The v11 master remains the historical publication line at

`TIR/monograph/metatime_monograph.tex`.

## Validation

The v12 branch includes dedicated deterministic validators for the migrated theorem/evidence surfaces, including:

```text
TIR/validation/tir_kappa_flavour_mixing_normalization_v0_1.py
TIR/validation/tir_v12_ch05_euclidean_spatial_gate_v0_1.py
TIR/validation/tir_v12_ch06_tetrahedral_closure_v0_1.py
TIR/validation/tir_v12_ch07_holonomy_se3_torsion_v0_1.py
TIR/validation/tir_v12_hypercharge_anomaly_audit_v0_1.py
TIR/validation/tir_v12_completion_frontier_dag_v0_1.py
```

Publication promotion requires an exact-head source-contract pass, LaTeX compilation, citation/reference integrity checks and PDF preflight.

## Research and publication policy

The repository preserves the following invariants:

1. formulas retain source provenance and version identity;
2. retrospective and prospective evidence remain separate;
3. failed gates remain visible in the evidence record;
4. scheme- and scale-dependent quantities use declared comparison conventions;
5. prospective candidate families remain frozen after their assigned evidence gate opens;
6. technical PASS and physical empirical verdicts remain separate;
7. GREMLIN supplies bounded candidate generation and adversarial audit, while theorem promotion requires deterministic proof/validation;
8. `main` changes only through an explicit promotion decision.

## Citation

Until a DOI-backed v12 release is deposited, cite the repository and the exact commit used:

```bibtex
@misc{Lipa2026TIR,
  author       = {Adrian Lipa},
  title        = {Theory of Informational Relations:
                  Foundations, Emergent Geometry, and Phenomenological Tests},
  year         = {2026},
  howpublished = {The Fundamental Theory of Informational Relations repository},
  url          = {https://github.com/AdrianLipa90/The-Fundamental-Theory-of-Informational-Relations},
  note         = {Version 12 content-migration candidate; cite the exact Git commit used}
}
```

## Author and contact

**Adrian Lipa**  
Independent Researcher  
Doncaster, United Kingdom

For scientific discussion, reproducibility reports or collaboration proposals, use the repository's GitHub issue or discussion channels where available.
