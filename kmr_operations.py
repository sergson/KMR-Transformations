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

import math

def kmr_direct(A, K):
    """version without error protection of A ⊙ K = A/(1 + AK)"""
    return A / (1 + A*K)

def kmr_direct_sh(A: float, K: float) -> float:
    """A ⊙ K = A/(1 + K·A) with singularity handling"""
    if A == 0:
        return 0.0
    denom = 1.0 + K * A
    if abs(denom) < 1e-15:
        # Undefined at pole - return NaN
        return float('nan')
    return A / denom


def kmr_inverse(A, K):
    """version without error protection of A ⊘ K = A/(1 - AK)"""
    return A / (1 - A*K)

def kmr_inverse_sh(A: float, K: float) -> float:
    """A ⊘ K = A/(1 - K·A) with singularity handling"""
    if A == 0:
        return 0.0
    denom = 1.0 - K * A
    if abs(denom) < 1e-15:
        # Undefined at pole - return NaN
        return float('nan')
    return A / denom

def kmrd(A):
    """A ⊙ 1 operation
       KMR direct operator: A/(1+A) (works for all A ≠ -1)"""
    return kmr_direct_sh(A, 1)

def kmri(A):
    """A ⊘ 1 operation
       KMR inverse operator: A/(1-A) (works for all A ≠ 1)"""
    return kmr_inverse_sh(A, 1)

def kmr_dircly(A: float, K: float) -> float:
    """Compute A ⊙ K (direct KMR operator): A/(1 + K*A).
    
    Args:
        A: Input value.
        K: Number of iterations.
        
    Returns:
        Result of A ⊙ K. Returns float('inf') if a singularity occurs (1 + K*A = 0).
    """
    return kmr_direct_sh(A, K)

def kmr_invly(A: float, K: float) -> float:
    """Compute A ⊘ K (inverse KMR operator): A/(1 - K*A).
    
    Args:
        A: Input value.
        K: Number of iterations.
        
    Returns:
        Result of A ⊘ K. Returns float('inf') if a singularity occurs (1 - K*A = 0).
    """
    return kmr_inverse_sh(A, K)


def kmr_add(A: float, K: float, C: float, eps: float = 1e-12) -> float:
    """Compute K + C using KMR operators without classical fallback.

    For |A| < eps, the parameter is adjusted to eps to maintain
    computation within the KMR operator framework.
    """
    # Maintain KMR purity: adjust A rather than fall back to classical arithmetic
    if abs(A) < eps:
        # Preserve sign for consistency, default to positive for A=0
        A = math.copysign(eps, A) if A != 0 else eps

    # Pure KMR composition without classical shortcuts
    X = kmr_dircly(A, K)
    Y = kmr_dircly(X, C)
    Z = kmr_invly(Y, 1 / A)
    return 1 / Z


def kmr_sub(A: float, K: float, C: float, eps: float = 1e-12) -> float:
    """Compute K - C using KMR operators without classical fallback.

    For |A| < eps, the parameter is adjusted to eps to maintain
    computation within the KMR operator framework.
    """
    # Maintain KMR purity: adjust A rather than fall back to classical arithmetic
    if abs(A) < eps:
        # Preserve sign for consistency, default to positive for A=0
        A = math.copysign(eps, A) if A != 0 else eps

    # Pure KMR composition using standard form
    X = kmr_invly(A, K)
    Y = kmr_dircly(X, C)
    Z = kmr_invly(Y, 1 / A)
    return -1 / Z
    
    # Alternative using symmetric form
    # X = kmr_invly(-A, K)
    # Y = kmr_dircly(X, C)
    # Z = kmr_invly(Y, 1/A)
    # return 1/Z

