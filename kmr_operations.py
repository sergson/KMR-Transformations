"""
KMR Operator Algebra
Version: 1.0.0
License: GPL 3.0 (see LICENSE)
"""
__author__ = "Sergei Terikhov"

"""
KMR Operator Algebra v1.0

Defines direct (⊙) and inverse (⊘) KMR transformations:
A ⊙ K = A/(1 + AK)
A ⊘ K = A/(1 - AK)

Defines addition and subtraction by KMR operators:
K + C = ( ( ( A ⊙ K ) ⊙ C ) ⊘ 1 A ) − 1 
K − C = − ( ( ( A ⊘ K ) ⊙ C ) ⊘ 1 A ) − 1 
symmetric form:
K − C = ( ( ( − A ⊘ K ) ⊙ C ) ⊘ 1 A ) − 1 
"""

def kmr_direct(A, K):
    """A ⊙ K = A/(1 + AK)"""
    return A / (1 + A*K)

def kmr_inverse(A, K):
    """A ⊘ K = A/(1 - AK)"""
    return A / (1 - A*K)

def kmr_add(A: float, K: float, C: float) -> float:
    """Compute K + C using KMR operators."""
    if abs(A) < 1e-15:  # Handle A ≈ 0 case
        return K + C
    X = kmr_direct(A, K)
    Y = kmr_direct(X, C)
    Z = kmr_inverse(Y, 1/A)
    return 1/Z

def kmr_sub(A: float, K: float, C: float) -> float:
    """Compute K - C using KMR operators."""
    if abs(A) < 1e-15:  # Handle A ≈ 0 case
        return K - C
    # Using the standard form
    X = kmr_inverse(A, K)
    Y = kmr_direct(X, C)
    Z = kmr_inverse(Y, 1/A)
    return -1/Z
    
    # Alternative using symmetric form
    # X = kmr_inverse(-A, K)
    # Y = kmr_direct(X, C)
    # Z = kmr_inverse(Y, 1/A)
    # return 1/Z
