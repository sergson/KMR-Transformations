"""
KMR Operator Algebra
Version: 1.0.0
License: GPL 3.0 (see LICENSE)
"""
__author__ = "Sergei Terikhov"

"""
KMR Operator Algebra v1.0

Defines direct (⊙) and inverse (⊘) KMR transformations:
- A ⊙ B = A/(1 + AB)
- A ⊘ B = A/(1 - AB)
"""

def kmr_direct(a, b):
    """A ⊙ B = A/(1 + AB)"""
    return a / (1 + a*b)

def kmr_inverse(a, b):
    """A ⊘ B = A/(1 - AB)"""
    return a / (1 - a*b)