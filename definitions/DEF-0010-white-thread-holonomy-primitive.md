# DEF-0010 — White-Thread holonomy primitive

## Status
`defined`

## Depends on
- `DEF-0002`

## Objects defined here
1. `OBJ-WHITE-THREAD-PRIMITIVE-0001`
2. `OBJ-U1-HOLONOMY-0001`
3. `OBJ-WHITE-THREAD-MATRIX-ELEMENT-0001`

## U(1) holonomy primitive
For a path \(\gamma_{ij}\) between cycle-associated states \(|\Psi_i\rangle\) and \(|\Psi_j\rangle\), define the minimal U(1) holonomy
\[
U[\gamma_{ij}] = \mathcal P\exp\!\left(i\int_{\gamma_{ij}} A\right).
\]
In the abelian U(1) toy sector this reduces to
\[
U[\gamma_{ij}] = \exp\!\left(i\int_{\gamma_{ij}} A\right).
\]

## White-Thread primitive
Define the White-Thread primitive between \(i\) and \(j\) by the transported matrix element
\[
W_{ij}[\gamma] = \langle \Psi_i | U[\gamma_{ij}] | \Psi_j \rangle.
\]

## Canonical role
This object is the minimal canonical upstream constructor of White-Thread transport. It isolates the pure transport primitive before later dressing, calibration, or effective amplification is introduced.

## Immediate bound
For normalized states in the abelian toy sector,
\[
|W_{ij}[\gamma]| \le 1.
\]
This follows from unitary transport and the Cauchy--Schwarz inequality.

## Registered numeric trace
Toy registered values:
\[
\phi = 0.2 + 0.3 - 0.1 = 0.4,
\qquad
\langle \Psi_i|\Psi_j\rangle = 0.6.
\]
Hence
\[
W_{ij} = 0.6 e^{0.4 i}
\]
and numerically
\[
W_{ij} \approx 0.5526365964 + 0.2336510054 i,
\qquad
|W_{ij}| = 0.6.
\]

## Executable bindings
- solver: `src/ciel_foundations/solvers/white_thread_primitive_solver.py`
- simulation: `Simulations/code/sim_white_thread_primitive.py`
- appendix: `LaTeX/appendices/APP-0006-white-thread-primitive-numerical-derivations.tex`

## Artifact bindings
- result: `Simulations/results/ART-0005-white-thread-primitive-demo.csv`
- provenance: `provenance/ART-0005-provenance.yaml`
- falsification: `falsification/FM-0005-white-thread-primitive.yaml`

## Scope restriction
This primitive is intentionally minimal. Later effective pairwise quantities may include additional dressing, calibration, or non-abelian structure. Those are not part of this definition.
