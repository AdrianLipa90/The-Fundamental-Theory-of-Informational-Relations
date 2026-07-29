#!/usr/bin/env python3
"""Normalize LaTeX references and line breaking before monograph compilation.

The transformations are deterministic and idempotent. They do not alter any
scientific formula or numerical result; they only repair cross-references,
bibliographic TeX, and non-breaking paths/tables that could prevent a clean PDF.
"""
from __future__ import annotations

import re
from pathlib import Path


def replace(path: str, old: str, new: str, count: int = -1) -> bool:
    """
    Replace occurrences of specified text in a UTF-8 text file.
    
    Parameters:
    	path (str): Path to the file to modify.
    	old (str): Text to replace.
    	new (str): Replacement text.
    	count (int): Maximum number of replacements, or -1 to replace all occurrences.
    
    Returns:
    	bool: True if the file was updated, False if the target text was absent.
    """
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    if old not in text:
        print(f"SKIP already normalized: {path}")
        return False
    p.write_text(text.replace(old, new, count), encoding="utf-8")
    print(f"UPDATED: {path}")
    return True


def normalize_root(path: str) -> None:
    """
    Normalize LaTeX package configuration and emergency-stretch settings in a source file.
    
    Parameters:
        path (str): Path to the LaTeX source file to normalize.
    """
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    original = text

    if "\\usepackage{xurl}" not in text:
        text = text.replace(
            "\\usepackage{graphicx}\n\\usepackage{hyperref}",
            "\\usepackage{graphicx}\n\\usepackage{xurl}\n"
            "\\usepackage[protrusion=true,expansion=false]{microtype}\n"
            "\\usepackage{hyperref}",
            1,
        )
    text = text.replace(
        "\\usepackage{microtype}",
        "\\usepackage[protrusion=true,expansion=false]{microtype}",
    )

    # Collapse any historical repeated insertions and ensure exactly one line.
    stretch = "\\setlength{\\emergencystretch}{3em}\n"
    text = re.sub(
        r"(?:\\setlength\{\\emergencystretch\}\{3em\}\n)+",
        lambda _match: stretch,
        text,
    )
    if stretch not in text:
        text = text.replace("]{geometry}\n", "]{geometry}\n" + stretch, 1)

    if text != original:
        p.write_text(text, encoding="utf-8")
        print(f"UPDATED: {path}")
    else:
        print(f"SKIP already normalized: {path}")


def normalize_app_m(path: str) -> None:
    """
    Normalize Appendix M labels and LaTeX path references in a source file.
    
    Parameters:
    	path (str): Path to the LaTeX source file to normalize.
    """
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    original = text
    alias = "\\label{app:prospective_observable_identifiability}\n"
    text = re.sub(
        r"(?:" + re.escape(alias) + r")+",
        lambda _match: alias,
        text,
    )
    if alias not in text:
        text = text.replace(
            "\\label{app:observable_identifiability}\n",
            "\\label{app:observable_identifiability}\n" + alias,
            1,
        )
    text = text.replace("\\texttt{heavy\\_quark\\_resonance}", "\\path{heavy_quark_resonance}")
    text = text.replace(
        "\\texttt{charged\\_lepton\\_small\\_seed}",
        "\\path{charged_lepton_small_seed}",
    )
    text = text.replace(
        "\\texttt{TIR/validation/up\\_sector\\_observable\\_identifiability\\_v10\\_6.py}",
        "\\path{TIR/validation/up_sector_observable_identifiability_v10_6.py}",
    )
    if text != original:
        p.write_text(text, encoding="utf-8")
        print(f"UPDATED: {path}")
    else:
        print(f"SKIP already normalized: {path}")


def main() -> None:
    """Normalize all targeted LaTeX source files used to build the monograph."""
    root = "TIR/monograph/metatime_monograph.tex"
    normalize_root(root)

    app_m = "TIR/monograph/appendices/appM_prospective_observable_identifiability.tex"
    normalize_app_m(app_m)

    app_n = "TIR/monograph/appendices/appN_separable_candidate_family.tex"
    replace(
        app_n,
        "Appendix~\\ref{app:prospective_observable_identifiability}",
        "Appendix~\\ref{app:observable_identifiability}",
    )
    replace(
        app_n,
        """\\[
\\boxed{
\\text{candidate family frozen}
\\;\\land\\;
\\text{no mass benchmark}
\\;\\land\\;
\\text{no candidate selected}
\\;\\land\\;
\\text{canonical promotion denied}
}
\\]""",
        """\\[
\\boxed{
\\begin{gathered}
\\text{candidate family frozen}
\\;\\land\\;
\\text{no mass benchmark}\\\\
\\text{no candidate selected}
\\;\\land\\;
\\text{canonical promotion denied}
\\end{gathered}
}
\\]""",
    )
    replace(
        app_n,
        "\\texttt{TIR/validation/separable\\_universal\\_candidate\\_family\\_v10\\_7.py}",
        "\\path{TIR/validation/separable_universal_candidate_family_v10_7.py}",
    )
    replace(
        app_n,
        "\\texttt{2bbf9985b6a4fc9d19d039e117b15eb446a51a3e8828a2894c8d797bb35f23f4}",
        "\\path{2bbf9985b6a4fc9d19d039e117b15eb446a51a3e8828a2894c8d797bb35f23f4}",
    )

    app_k = "TIR/monograph/appendices/appK_sector_holonomy_release.tex"
    replace(
        app_k,
        "\\chapter{Sector-Holonomy Release of the Collatz Quarter-Power Trace}",
        "\\chapter[Sector-Holonomy Release]{Sector-Holonomy Release of the Collatz Quarter-Power Trace}",
        1,
    )
    replace(
        app_k,
        "\\texttt{TIR/validation/collatz\\_sector\\_holonomy\\_mass\\_audit\\_v10\\_2.py}",
        "\\path{TIR/validation/collatz_sector_holonomy_mass_audit_v10_2.py}",
    )
    replace(
        app_k,
        "\\texttt{TIR/validation/collatz\\_sector\\_holonomy\\_mass\\_audit\\_v10\\_2r1.py}",
        "\\path{TIR/validation/collatz_sector_holonomy_mass_audit_v10_2r1.py}",
    )

    app_j = "TIR/monograph/appendices/appJ_collatz_quarter_power_scaling.tex"
    replace(
        app_j,
        "\\texttt{TIR/validation/collatz\\_quarter\\_power\\_mass\\_audit\\_v10\\_1.py}",
        "\\path{TIR/validation/collatz_quarter_power_mass_audit_v10_1.py}",
    )

    app_l = "TIR/monograph/appendices/appL_up_sector_common_baseline_no_go.tex"
    replace(app_l, "\\texttt{light\\_quark\\_seed}", "\\path{light_quark_seed}")
    replace(app_l, "\\texttt{heavy\\_quark\\_resonance}", "\\path{heavy_quark_resonance}")
    replace(
        app_l,
        "\\texttt{TIR/validation/up\\_sector\\_common\\_baseline\\_no\\_go\\_v10\\_4.py}",
        "\\path{TIR/validation/up_sector_common_baseline_no_go_v10_4.py}",
    )

    ch31 = "TIR/monograph/chapters/ch31_open_problems.tex"
    replace(
        ch31,
        "\\subsection{Sector-Holonomy Release (Retrospective Signal; Absolute Offset Open)}",
        "\\subsection{Sector-Holonomy Release (Retrospective; Offset Open)}",
        1,
    )

    app_f = "TIR/monograph/appendices/appF_baryon_calculations.tex"
    replace(
        app_f,
        """\\[
\\begin{array}{ccccccc}
\\text{Particle} & Y & I(I{+}1) & \\beta Y & \\gamma(I(I{+}1){-}Y^2/4) & \\text{Mass (MeV)} & \\text{PDG (MeV)} \\\\
\\hline
p,n & 1 & 0.75 & -185.90 & 38.73(0.75{-}0.25) = 19.37 & 925.95{+}189.77{-}185.90{+}19.37 = 949.19 & 938.92 \\\\
\\Lambda & 0 & 0 & 0 & 0 & 925.95{+}189.77 = 1115.72 & 1115.68 \\\\
\\Sigma & 0 & 2 & 0 & 38.73(2{-}0) = 77.46 & 925.95{+}189.77{+}77.46 = 1193.18 & 1193.15 \\\\
\\Xi & -1 & 0.75 & +185.90 & 38.73(0.75{-}0.25) = 19.37 & 925.95{+}189.77{+}185.90{+}19.37 = 1320.99 & 1318.29 \\\\
\\end{array}
\\]""",
        """\\begin{center}
\\resizebox{\\textwidth}{!}{$
\\begin{array}{ccccccc}
\\text{Particle} & Y & I(I{+}1) & \\beta Y & \\gamma(I(I{+}1){-}Y^2/4) & \\text{Mass (MeV)} & \\text{PDG (MeV)} \\\\
\\hline
p,n & 1 & 0.75 & -185.90 & 38.73(0.75{-}0.25) = 19.37 & 925.95{+}189.77{-}185.90{+}19.37 = 949.19 & 938.92 \\\\
\\Lambda & 0 & 0 & 0 & 0 & 925.95{+}189.77 = 1115.72 & 1115.68 \\\\
\\Sigma & 0 & 2 & 0 & 38.73(2{-}0) = 77.46 & 925.95{+}189.77{+}77.46 = 1193.18 & 1193.15 \\\\
\\Xi & -1 & 0.75 & +185.90 & 38.73(0.75{-}0.25) = 19.37 & 925.95{+}189.77{+}185.90{+}19.37 = 1320.99 & 1318.29 \\\\
\\end{array}
$}
\\end{center}""",
    )

    refs = "TIR/monograph/references_expanded_v10_8.tex"
    replace(refs, "K.~{\\dot Z}yczkowski", "K.~\\.{Z}yczkowski")
    replace(refs, "tensor product of semifinite W^*-algebras", "tensor product of semifinite $W^*$-algebras")


if __name__ == "__main__":
    main()
