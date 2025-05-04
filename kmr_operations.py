"""
KMR Operator Algebra
Version: 1.0.0
License: GPL 3.0 (see LICENSE)
"""
__author__ = "Sergei Terikhov"

"""
KMR Operator Algebra v1.0

Defines direct (⊙) and inverse (⊘) KMR transformations:
- A ⊙ K = A/(1 + AK)
- A ⊘ K = A/(1 - AK)
"""

def kmr_direct(A, K):
    """A ⊙ K = A/(1 + AK)"""
    return A / (1 + A*K)

def kmr_inverse(A, K):
    """A ⊘ K = A/(1 - AK)"""
    return A / (1 - A*K)
