"""Typed XF-6 solver extension for the transverse mass-envelope programme.

The extension is isolated from DEFAULT_SOLVER while the branch is under audit.
It records exact conditional consequences of Xi-kernel strict log-concavity and
keeps the global positive-core / oscillatory-tail domination as an OPEN gate.
"""

from __future__ import annotations

from .solver import ClaimSolver, ClaimStatus, HALF_AXIS_RULES, Rule


XF6_RULES = (
    Rule(
        ("xi_fourier_kernel",),
        "xi_kernel_strict_log_concavity_tp2",
        ClaimStatus.OPEN,
        "XF-6 external preprint claim: Gershon v2 global strict log-concavity / TP2",
    ),
    Rule(
        ("xi_kernel_strict_log_concavity_tp2",),
        "xf6_transverse_mass_center_dominance",
        ClaimStatus.EXACT,
        "midpoint Jensen inequality for log M(a,b)=f(a+b)+f(a-b)",
    ),
    Rule(
        ("xi_kernel_strict_log_concavity_tp2",),
        "xf6_transverse_mass_strict_abs_b_decay",
        ClaimStatus.EXACT,
        "d_b log M=f'(a+b)-f'(a-b)<0 for b>0 when f' is strictly decreasing",
    ),
    Rule(
        ("xi_kernel_strict_log_concavity_tp2",),
        "xf6_slice_gaussian_mass_envelope_exists",
        ClaimStatus.STANDARD,
        "continuous strict negative log-curvature has a positive minimum on each compact symmetric slice",
    ),
    Rule(
        ("xi_fourier_kernel",),
        "xf6_exact_positive_curvature_corridor",
        ClaimStatus.EXACT,
        "|b|<=min(a/2,pi/(8|x|)) gives an explicit positive lower bound for the XF-5 curvature kernel; x=0 is positive on the full interior cone",
    ),
    Rule(
        (
            "xf6_exact_positive_curvature_corridor",
            "xf6_slice_gaussian_mass_envelope_exists",
        ),
        "xf6_global_core_tail_domination",
        ClaimStatus.OPEN,
        "uniform positive-core lower bound must dominate the correlated oscillatory tail for all real x and 0<|y|<1/2",
    ),
    Rule(
        ("xf6_global_core_tail_domination",),
        "xi_wiener_laguerre_strict_positivity",
        ClaimStatus.STANDARD,
        "XF-6 core-tail inequality is precisely a sufficient global sign bound for the XF-5 integral representation",
    ),
)


XF6_SOLVER = ClaimSolver((*HALF_AXIS_RULES, *XF6_RULES))
