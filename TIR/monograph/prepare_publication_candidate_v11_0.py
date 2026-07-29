#!/usr/bin/env python3
from __future__ import annotations

import re
import runpy
from pathlib import Path

_original_sub = re.sub

def _literal_hyperref_sub(pattern, repl, string, count=0, flags=0):
    """Apply substitutions involving hyperref patterns with literal string replacements.
    
    Parameters:
        pattern: The regular-expression pattern to search for.
        repl: The replacement string or callable.
        string: The text in which to perform the substitution.
        count: The maximum number of substitutions to make.
        flags: Regular-expression compilation flags.
    
    Returns:
        The string resulting from the substitutions.
    """
    if isinstance(repl, str) and "hyperref" in str(pattern):
        return _original_sub(
            pattern,
            lambda _match: repl,
            string,
            count=count,
            flags=flags,
        )
    return _original_sub(pattern, repl, string, count=count, flags=flags)

re.sub = _literal_hyperref_sub
runpy.run_path(
    str(Path(__file__).with_name("prepare_publication_candidate_v11_0_impl.py")),
    run_name="__main__",
)
