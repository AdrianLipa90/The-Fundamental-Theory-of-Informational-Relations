# WP-MOD — White-Thread U(1) primitive

## Status
`defined`

## Scope
This whitepaper records the first canonical minimal constructor of the White-Thread object as a transported matrix element of a U(1) holonomy.

## 1. Theory chapter
### 1.1 U(1) transport
The minimal transport operator is
\[
U[\gamma_{ij}] = \mathcal P\exp\!\left(i\int_{\gamma_{ij}}A\right),
\]
which reduces to a simple exponential in the abelian U(1) toy sector.

### 1.2 White-Thread primitive
The primitive pairwise quantity is
\[
W_{ij}[\gamma] = \langle \Psi_i | U[\gamma_{ij}] | \Psi_j \rangle.
\]

### 1.3 Primitive bound
For normalized states and unitary transport, the primitive amplitude satisfies
\[
|W_{ij}|\le 1.
\]
This is a bound on the minimal primitive, not on later dressed effective pairwise quantities.

## 2. Source files
- `definitions/DEF-0010-white-thread-holonomy-primitive.md`
- `derivations/D-0009-white-thread-u1-primitive.md`
- `interfaces/IF-0008-white-thread-primitive.yaml`

## 3. Code bindings
- `src/ciel_foundations/solvers/white_thread_primitive_solver.py`
- `tests/test_white_thread_primitive.py`
- `Simulations/code/sim_white_thread_primitive.py`

## 4. Epistemic note
This module closes the minimal abelian White-Thread primitive only. It does not yet define the full dressed pairwise coupling or non-abelian extensions.
