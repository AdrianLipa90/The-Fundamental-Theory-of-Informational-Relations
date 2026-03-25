# Sectors Index

This index organizes the sector-realization layer.

## Role
Sectors are downstream realizations of the foundational theory.
They must inherit constants, operators, and constraints from upstream canonical layers and must not create local replacements for them.

## Current sectors
- neutrino
- lepton
- quark
- hadron
- cosmology

## Rule
Every sector entry must answer:
- which constants it consumes
- which operators it consumes
- which assumptions it adds
- what its falsification target is
- which whitepaper/derivation/code/tests instantiate it

## Current state
Sector folders exist but are still introductory placeholders.
This means sector boundaries are present, but inheritance wiring is not yet explicit.

## Immediate next step
For each sector, add:
1. import surface from foundations
2. minimal dependency map
3. falsification stub
4. linked whitepaper target

## Priority order
1. neutrino
2. lepton
3. quark
4. hadron
5. cosmology
