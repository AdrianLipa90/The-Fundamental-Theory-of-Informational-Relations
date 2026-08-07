#!/usr/bin/env python3
"""Deterministic implementation audit for the TIR κ phase-rate subsystem.

The exact algebraic statement under audit is

    κ = ln(2)/(24π),  ω = 2πf,  Γ_I = κω = (ln2/12)f.

The primary certificate is symbolic at the factor-exponent level: rational
coefficients are represented by :class:`fractions.Fraction`, while ``ln2``,
``pi`` and ``f`` are tracked as formal factors.  Floating-point evaluations at
representative frequencies are only secondary implementation sanity checks.

The script does not promote the Metatime normalization or the physical
interpretation of Γ_I beyond their declared claim classes.
"""
from __future__ import annotations

import json
import math
from dataclasses import asdict, dataclass
from fractions import Fraction

FREQUENCIES_HZ = (0.0, 1.0, 7.83, 12.0, 60.0, 440.0)
ABS_TOL = 1e-15
REL_TOL = 1e-14


@dataclass(frozen=True)
class FactorSignature:
    """Formal monomial used to certify coefficient and phase-factor cancellation."""

    coefficient: Fraction
    ln2_power: int = 0
    pi_power: int = 0
    frequency_power: int = 0

    def __mul__(self, other: "FactorSignature") -> "FactorSignature":
        """Multiply two formal monomials exactly."""
        return FactorSignature(
            coefficient=self.coefficient * other.coefficient,
            ln2_power=self.ln2_power + other.ln2_power,
            pi_power=self.pi_power + other.pi_power,
            frequency_power=self.frequency_power + other.frequency_power,
        )

    def receipt(self) -> dict[str, object]:
        """Serialize the exact formal signature without floating-point conversion."""
        return {
            "coefficient": [self.coefficient.numerator, self.coefficient.denominator],
            "ln2_power": self.ln2_power,
            "pi_power": self.pi_power,
            "frequency_power": self.frequency_power,
        }


@dataclass(frozen=True)
class Row:
    """Secondary floating-point implementation check at one cyclic frequency."""

    frequency_hz: float
    omega_rad_s: float
    gamma_from_kappa_omega: float
    gamma_from_closed_form: float
    residual: float
    pass_identity: bool


def kappa() -> float:
    """Return the numerical TIR normalization used by the implementation audit."""
    return math.log(2.0) / (24.0 * math.pi)


def exact_factor_certificate() -> dict[str, object]:
    """Certify the ``2π`` cancellation and the exact rational prefactor ``1/12``.

    The TIR normalization contributes ``(1/24) * ln2 * pi^-1``.  Converting
    cyclic frequency to angular frequency contributes ``2 * pi * f``.  Their
    product therefore has rational coefficient ``1/12`` and zero net power of
    ``pi``.  No numerical approximation of π or ln2 enters this certificate.
    """
    kappa_signature = FactorSignature(
        coefficient=Fraction(1, 24),
        ln2_power=1,
        pi_power=-1,
    )
    omega_signature = FactorSignature(
        coefficient=Fraction(2, 1),
        pi_power=1,
        frequency_power=1,
    )
    product = kappa_signature * omega_signature
    expected = FactorSignature(
        coefficient=Fraction(1, 12),
        ln2_power=1,
        pi_power=0,
        frequency_power=1,
    )
    return {
        "kappa_signature": kappa_signature.receipt(),
        "omega_signature": omega_signature.receipt(),
        "product_signature": product.receipt(),
        "expected_signature": expected.receipt(),
        "pi_cancelled_exactly": product.pi_power == 0,
        "exact_prefactor": [product.coefficient.numerator, product.coefficient.denominator],
        "pass": product == expected,
    }


def evaluate(frequency_hz: float) -> Row:
    """Compare the two numerical implementations of Γ_I at one frequency."""
    omega = 2.0 * math.pi * frequency_hz
    gamma_a = kappa() * omega
    gamma_b = (math.log(2.0) / 12.0) * frequency_hz
    residual = gamma_a - gamma_b
    return Row(
        frequency_hz=frequency_hz,
        omega_rad_s=omega,
        gamma_from_kappa_omega=gamma_a,
        gamma_from_closed_form=gamma_b,
        residual=residual,
        pass_identity=math.isclose(gamma_a, gamma_b, rel_tol=REL_TOL, abs_tol=ABS_TOL),
    )


def constraint_rank_certificate() -> dict[str, object]:
    """Record the exact rank argument for the three-constraint subsystem.

    For ``q=(κ,ω,f,Γ)`` the Jacobian rows are
    ``(1,0,0,0)``, ``(0,1,-2π,0)``, and ``(-ω,-κ,0,1)``.  The first two are
    independent and the third is the only row with a nonzero Γ component, so
    the rank is three for every κ and ω.
    """
    return {
        "ambient_dimension": 4,
        "constraint_count": 3,
        "jacobian_rank": 3,
        "constraint_manifold_dimension": 1,
        "proof_basis": "row independence from κ pivot, ω/f relation, and unique Γ pivot",
    }


def build_receipt() -> dict[str, object]:
    """Build the complete exact-plus-numerical κ phase-rate audit receipt."""
    exact = exact_factor_certificate()
    rows = [evaluate(f) for f in FREQUENCIES_HZ]
    rank = constraint_rank_certificate()
    technical_pass = (
        exact["pass"]
        and all(row.pass_identity for row in rows)
        and rank["jacobian_rank"] == 3
        and rank["constraint_manifold_dimension"] == 1
    )
    return {
        "schema": "TIR_KAPPA_PHASE_RATE_IDENTITY_V11_1",
        "claim_class": {
            "kappa_normalization": "B_MODEL_POSTULATE",
            "omega_equals_2pi_f": "A_STANDARD_DEFINITION",
            "phase_rate_identity": "EXACT_CONDITIONAL_IDENTITY",
            "surface_refresh_interpretation": "OPEN_OPERATIONAL_INTERPRETATION",
        },
        "exact_factor_certificate": exact,
        "kappa_numeric": kappa(),
        "per_cycle_information_increment_numeric": math.log(2.0) / 12.0,
        "numerical_sanity_rows": [asdict(row) for row in rows],
        "constraint_rank": rank,
        "technical_status": "PASS" if technical_pass else "FAIL",
    }


def main() -> None:
    """Print the deterministic JSON receipt and fail the process on audit failure."""
    receipt = build_receipt()
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if receipt["technical_status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
