# Roadmap

## M0 - Foundations Governance
- freeze axioms registry
- freeze dependency graph
- create assumptions, decisions, interfaces, falsification, provenance, artifact tracking
- define status labels and review workflow

## M1 - Initial Conditions
- define potential/chaos/state mapping
- implement Bloch-sphere initial conditions
- symbolic and numeric tests
- write module whitepaper

## M2 - Dynamics and Closure
- define minimal Bloch/spinor dynamics
- implement Euler closure as active regulator
- define acceptance / rollback logic
- benchmark stability and sensitivity

## M3 - Holonomy Layer
- define connection, transport, white-thread primitives
- implement pairwise holonomy objects and tests
- formalize closure / winding interaction

## M4 - Tau from Coupling
- define operator built from coupling + closure
- derive tau_i as spectrum, not fitted inputs
- document failure modes and residual assumptions

## M5 - Genesis of Constants
- define generator of dimensionless constants
- define lifting to dimensional scales
- populate constants registry with explicit provenance

## M6 - Sector Realization
- neutrino sector first
- then charged leptons
- then quarks / hadrons / cosmology
- each sector must inherit constants and operators, not redefine them locally

## M7 - Integration Surface for Omega
- export only stabilized constants, operators, and constraints
- document import contract for Omega as downstream consumer
