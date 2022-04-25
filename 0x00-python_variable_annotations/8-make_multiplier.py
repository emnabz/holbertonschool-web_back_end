#!/usr/bin/env python3
"""a type-annotated function"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by multiplier"""
    def f(x):
        return x * multiplier
    return f
