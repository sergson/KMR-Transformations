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
    """version without error protection of A ⊙ K = A/(1 + AK)"""
    return A / (1 + A*K)

def kmr_inverse(A, K):
    """version without error protection of A ⊘ K = A/(1 - AK)"""
    return A / (1 - A*K)

def kmrd(A):
    """A ⊙ 1 operation
       KMR direct operator: A/(1+A) (works for all A ≠ -1)"""
    return A / (1 + A) if (1 + A) != 0 else float('inf')

def kmri(A):
    """A ⊘ 1 operation
       KMR inverse operator: A/(1-A) (works for all A ≠ 1)"""
    return A / (1 - A) if (1 - A) != 0 else float('inf')

def kmr_dircly(A: float, K: float) -> float:
    """Compute A ⊙ K (direct KMR operator): A/(1 + K*A).
    
    Args:
        A: Input value.
        K: Number of iterations.
        
    Returns:
        Result of A ⊙ K. Returns float('inf') if a singularity occurs (1 + K*A = 0).
    """
    return A / (1 + K * A) if (1 + K * A) != 0 else float('inf')

def kmr_invly(A: float, K: float) -> float:
    """Compute A ⊘ K (inverse KMR operator): A/(1 - K*A).
    
    Args:
        A: Input value.
        K: Number of iterations.
        
    Returns:
        Result of A ⊘ K. Returns float('inf') if a singularity occurs (1 - K*A = 0).
    """
    return A / (1 - K * A) if (1 - K * A) != 0 else float('inf')

def kmr_add(A: float, K: float, C: float) -> float:
    """Compute K + C using KMR operators."""
    if abs(A) < 1e-15:  # Handle A ≈ 0 case
        return K + C
    X = kmr_dircly(A, K)
    Y = kmr_dircly(X, C)
    Z = kmr_invly(Y, 1/A)
    return 1/Z

def kmr_sub(A: float, K: float, C: float) -> float:
    """Compute K - C using KMR operators."""
    if abs(A) < 1e-15:  # Handle A ≈ 0 case
        return K - C
    # Using the standard form
    X = kmr_invly(A, K)
    Y = kmr_dircly(X, C)
    Z = kmr_invly(Y, 1/A)
    return -1/Z
    
    # Alternative using symmetric form
    # X = kmr_invly(-A, K)
    # Y = kmr_dircly(X, C)
    # Z = kmr_invly(Y, 1/A)
    # return 1/Z

