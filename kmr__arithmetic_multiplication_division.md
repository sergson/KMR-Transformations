<!-- 
License: CC BY-SA 4.0 (see LICENSE-CC.md)
-->

### For Theoretical Content
- All mathematical formulations and documentation must be licensed under **CC BY-SA 4.0**
- When adding new theoretical content, include the header:
```markdown
<!-- 
License: CC BY-SA 4.0 (see LICENSE-CC.md)
-->
```

# 14. Arithmetic Operations via KMR Transformations: Complete Framework for Multiplication and Division
**Author**: Sergei Terikhov  
**Date**: 12.12.2025

## 14.1 Introduction

Building upon the established framework for addition and subtraction through KMR operators, this section extends the algebraic system to include complete expressions for multiplication and division. The KMR framework, which has been extended to real numbers through the canonical extension theorem, allows all parameters ($A$, $K$, $C$) to be real numbers. We present both iterative and closed-form expressions for multiplication and division, leveraging the decomposition property to handle both integer and fractional components.

## 14.2 Foundational Properties

### 14.2.1 Basic Operator Definitions
- **Direct KMR operator**: $A ⊙ K = \frac{A}{1 + K \cdot A}$ (for $K \in \mathbb{R}$)
- **Inverse KMR operator**: $A ⊘ K = \frac{A}{1 - K \cdot A}$ (for $K \in \mathbb{R}$)

### 14.2.2 Canonical Extension to Real Numbers
By Theorem 1 (Canonical Extension), these expressions provide unique continuous extensions from integer $K$ to real $K$ satisfying consistency, duality, and group properties.

### 14.2.3 Core Algebraic Properties for Real Parameters
1. **Group Property**: $(A ⊙ K) ⊙ C = A ⊙ (K + C)$ for $K, C \in \mathbb{R}$
2. **Inversion Identity**: $(A ⊙ K) ⊘ K = A = (A ⊘ K) ⊙ K$
3. **Scaling Property**: $λ \cdot (A ⊙ K) = (λ A) ⊙ (K/λ)$ for $λ \in \mathbb{R}$
4. **Parameter Extraction**: If $A ⊙ K = X$, then $K = \frac{1}{X} - \frac{1}{A}$

### 14.2.4 Tunneling Property
For any $Y \neq 0$ and $X$ where operations are defined:

$$
Y ⊙ X ⊘ Y^{-1} = X^{-1}
$$

## 14.3 Multiplication Through KMR Operators

### 14.3.1 Fundamental Multiplication Theorem

For any $A \neq 0$ and real $K, C$, the product $K \cdot C$ can be expressed in multiple equivalent forms:

#### 14.3.1.1 Tunneling Form

$$
K \cdot C = \left( \left( A ⊙ (K \cdot C) \right) ⊘ A^{-1} \right)^{-1}
$$

#### 14.3.1.2 Iterative Form (for integer C)
For $C \in \mathbb{Z}^+$:

$$
K \cdot C = \left( \left( A ⊙ \underbrace{K ⊙ K ⊙ \cdots ⊙ K}_{C \text{ times}} \right) ⊘ A^{-1} \right)^{-1}
$$

#### 14.3.1.3 Decomposition Form (for real C)
For $C \in \mathbb{R}^+$, let $C = D + F$ where $D \in \mathbb{Z}^+$ and $F \in [0,1)$:

$$
K \cdot C = \left( \left( (A ⊙ \underbrace{K ⊙ \cdots ⊙ K}_{D \text{ times}}) ⊙ (K \cdot F) \right) ⊘ A^{-1} \right)^{-1}
$$

### 14.3.2 Decomposition Property and Its Significance

#### 14.3.2.1 General Decomposition Theorem
For any $A \neq 0$, $K \in \mathbb{R}$, and $D, F \in \mathbb{R}^+$:

$$
A ⊙ (K \cdot (D + F)) = \left( A ⊙ (K \cdot D) \right) ⊙ (K \cdot F)
$$

#### 14.3.2.2 Proof
Using the group property:

$$
A ⊙ (K \cdot (D + F)) = A ⊙ (K \cdot D + K \cdot F) = \left( A ⊙ (K \cdot D) \right) ⊙ (K \cdot F)
$$

#### 14.3.2.3 Applications
This property enables:
1. **Fractional iteration**: Combining integer iterations with fractional adjustments
2. **Computational optimization**: Pre-computing integer portions
3. **Analytical simplification**: Breaking complex expressions into manageable parts

### 14.3.3 Special Cases

#### 14.3.3.1 Recursive Form

$$
A ⊙ (K \cdot C) = A ⊙ K ⊙ (K \cdot (C-1))
$$

for $C > 0$.

#### 14.3.3.2 Symmetric Form

$$
K \cdot C = \left( \left( A ⊙ \underbrace{C ⊙ \cdots ⊙ C}_{K \text{ times}} \right) ⊘ A^{-1} \right)^{-1}
$$

demonstrating emergent commutativity.

### 14.3.4 Complete Algorithm for Real Multiplication

Given $K, C \in \mathbb{R}^+$:
1. **Decompose**: $C = \lfloor C \rfloor + \{C\}$, where $\{C\} = C - \lfloor C \rfloor \in [0,1)$
2. **Integer component**: Compute $A ⊙ (K \cdot \lfloor C \rfloor)$ iteratively
3. **Fractional component**: Compute $A ⊙ (K \cdot \{C\})$ using direct formula
4. **Combine**: $A ⊙ (K \cdot C) = \left( A ⊙ (K \cdot \lfloor C \rfloor) \right) ⊙ (K \cdot \{C\})$
5. **Extract**: $K \cdot C = \left( (A ⊙ (K \cdot C)) ⊘ A^{-1} \right)^{-1}$

## 14.4 Division Through KMR Operators

### 14.4.1 Reciprocal Operation
$$
\frac{1}{C} = A ⊙ C ⊘ A^{-1}
$$

### 14.4.2 Division as Multiplication by Reciprocal

$$
\frac{K}{C} = K \cdot \frac{1}{C}
$$

### 14.4.3 Direct Division Formulas

#### 14.4.3.1 Tunneling Form

$$
\frac{K}{C} = -\left( \left( (A ⊘ K) ⊙ \frac{1}{C} \right) ⊘ A^{-1} \right)^{-1}
$$

#### 14.4.3.2 Iterative Form (for integer K)
For $K \in \mathbb{Z}^+$:

$$
\frac{K}{C} = \left( \left( A ⊙ \underbrace{\frac{1}{C} ⊙ \cdots ⊙ \frac{1}{C}}_{K \text{ times}} \right) ⊘ A^{-1} \right)^{-1}
$$

#### 14.4.3.3 Alternative Direct Form

$$
\frac{K}{C} = \left( \left( (A ⊘ K) ⊙ C^{-1} \right) ⊘ A^{-1} \right)^{-1}
$$

where $C^{-1} = \frac{1}{C}$.

### 14.4.4 Complete Algorithm for Real Division

Given $K, C \in \mathbb{R}^+$:
1. **Compute reciprocal**: $C^{-1} = A ⊙ C ⊘ A^{-1}$
2. **Decompose**: $K = \lfloor K \rfloor + \{K\}$
3. **Integer component**: Compute $A ⊙ (C^{-1} \cdot \lfloor K \rfloor)$ iteratively
4. **Fractional component**: Compute $A ⊙ (C^{-1} \cdot \{K\})$ using direct formula
5. **Combine**: $A ⊙ \left( \frac{K}{C} \right) = \left( A ⊙ (C^{-1} \cdot \lfloor K \rfloor) \right) ⊙ (C^{-1} \cdot \{K\})$
6. **Extract**: $\frac{K}{C} = \left( \left( A ⊙ \frac{K}{C} \right) ⊘ A^{-1} \right)^{-1}$

## 14.5 Pattern Recognition and Simplification Rules

### 14.5.1 Basic Patterns

1. **Iteration decomposition**:   

$$
A ⊙ (K \cdot C) = \underbrace{((A ⊙ K) ⊙ K) \dots ⊙ K}_{C \text{ times}}
$$

2. **Partial computation**:   

$$
A ⊙ (K \cdot (D+F)) = (A ⊙ (K \cdot D)) ⊙ (K \cdot F)
$$

3. **Recursive form**:   

$$
A ⊙ (K \cdot C) = A ⊙ K ⊙ (K \cdot (C-1))
$$

### 14.5.2 Advanced Transformation Rules

4. **Parameter interchange**:

$$
\left( \left( A ⊙ \underbrace{K ⊙ \cdots ⊙ K}_{C} \right) ⊘ A^{-1} \right)^{-1} = \left( \left( A ⊙ \underbrace{C ⊙ \cdots ⊙ C}_{K} \right) ⊘ A^{-1} \right)^{-1}
$$

5. **Mixed operations**:

$$
(A ⊙ (K \cdot C)) ⊘ (K \cdot D) = A ⊙ (K \cdot (C-D))
$$

6. **Chain simplification**:

$$
(A ⊙ (K \cdot C)) ⊙ (K \cdot D) = A ⊙ (K \cdot (C+D))
$$

## 14.6 Python Implementation

```python
import math
from kmr_operations import kmr_dircly, kmr_invly

def kmr_multiply_iterative(A: float, K: float, C: int, eps: float = 1e-12) -> float:
    """
    Compute K * C using iterative KMR operations for integer C.
    
    Uses decomposition property for integer iterations.
    
    Args:
        A: Base parameter (A ≠ 0)
        K: Multiplicand (K ∈ ℝ)
        C: Integer multiplier (C ≥ 1)
        eps: Tolerance for near-zero A
        
    Returns:
        K * C computed through iterative KMR operations
    """
    if abs(A) < eps:
        A = math.copysign(eps, A) if A != 0 else eps
    
    if C == 0:
        return 0.0
    
    # Start with A ⊙ K
    result = kmr_dircly(A, K)
    if math.isnan(result):
        return float('nan')
    
    # Apply ⊙ K (C-1) more times
    for _ in range(C - 1):
        result = kmr_dircly(result, K)
        if math.isnan(result):
            return float('nan')
    
    # Apply ⊘ A^{-1} and invert
    A_inv = 1 / A
    result = kmr_invly(result, A_inv)
    if math.isnan(result) or result == 0:
        return float('nan') if math.isnan(result) else float('inf')
    
    return 1 / result

def kmr_multiply_general(A: float, K: float, C: float, eps: float = 1e-12) -> float:
    """
    Compute K * C for real C using KMR operators with decomposition.
    
    Uses decomposition: C = floor(C) + frac(C)
    
    Args:
        A: Base parameter (A ≠ 0)
        K: Multiplicand (K ∈ ℝ)
        C: Real multiplier (C ≥ 0)
        eps: Tolerance for near-zero A
        
    Returns:
        K * C computed through KMR operations with decomposition
    """
    if abs(A) < eps:
        A = math.copysign(eps, A) if A != 0 else eps
    
    if C == 0:
        return 0.0
    
    # Decompose C into integer and fractional parts
    C_int = int(math.floor(C))
    C_frac = C - C_int
    
    # Handle integer part iteratively
    if C_int > 0:
        # Compute A ⊙ (K * C_int) iteratively
        int_part = A
        for _ in range(C_int):
            int_part = kmr_dircly(int_part, K)
            if math.isnan(int_part):
                return float('nan')
    else:
        int_part = A
    
    # Handle fractional part using direct formula
    if C_frac > 0:
        # Compute K * C_frac using tunneling
        # First compute A ⊙ (K * C_frac)
        K_times_frac = K * C_frac
        frac_part = kmr_dircly(A, K_times_frac)
        if math.isnan(frac_part):
            return float('nan')
        
        # Apply decomposition property
        if C_int > 0:
            # A ⊙ (K*C) = (A ⊙ (K*C_int)) ⊙ (K*C_frac)
            combined = kmr_dircly(int_part, K_times_frac)
        else:
            combined = frac_part
    else:
        combined = int_part
    
    # Extract K*C using tunneling
    A_inv = 1 / A
    extracted = kmr_invly(combined, A_inv)
    if math.isnan(extracted) or extracted == 0:
        return float('nan') if math.isnan(extracted) else float('inf')
    
    return 1 / extracted

def kmr_reciprocal(A: float, C: float, eps: float = 1e-12) -> float:
    """
    Compute 1/C using KMR tunneling property.
    
    Args:
        A: Base parameter (A ≠ 0)
        C: Value to invert (C ≠ 0)
        eps: Tolerance for near-zero A
        
    Returns:
        1/C computed through KMR operations
    """
    if abs(A) < eps:
        A = math.copysign(eps, A) if A != 0 else eps
    
    # 1/C = A ⊙ C ⊘ A^{-1}
    X = kmr_dircly(A, C)
    if math.isnan(X):
        return float('nan')
    
    A_inv = 1 / A
    result = kmr_invly(X, A_inv)
    if math.isnan(result):
        return float('nan')
    
    return result

def kmr_divide_iterative(A: float, K: float, C: float, eps: float = 1e-12) -> float:
    """
    Compute K/C for integer K using iterative KMR operations.
    
    Uses reciprocal and iterative multiplication.
    
    Args:
        A: Base parameter (A ≠ 0)
        K: Numerator (integer, K ≥ 1)
        C: Denominator (C ≠ 0)
        eps: Tolerance for near-zero A
        
    Returns:
        K/C computed through iterative KMR operations
    """
    if abs(A) < eps:
        A = math.copysign(eps, A) if A != 0 else eps
    
    if K == 0:
        return 0.0
    
    # Compute reciprocal of C
    C_inv = kmr_reciprocal(A, C, eps)
    if math.isnan(C_inv):
        return float('nan')
    
    # Multiply K by C_inv iteratively
    return kmr_multiply_iterative(A, C_inv, int(K), eps)

def kmr_divide_general(A: float, K: float, C: float, eps: float = 1e-12) -> float:
    """
    Compute K/C for real K using KMR operations with decomposition.
    
    Args:
        A: Base parameter (A ≠ 0)
        K: Numerator (K ≥ 0, real)
        C: Denominator (C ≠ 0)
        eps: Tolerance for near-zero A
        
    Returns:
        K/C computed through KMR operations
    """
    if abs(A) < eps:
        A = math.copysign(eps, A) if A != 0 else eps
    
    if K == 0:
        return 0.0
    
    # Compute reciprocal of C
    C_inv = kmr_reciprocal(A, C, eps)
    if math.isnan(C_inv):
        return float('nan')
    
    # Multiply K by C_inv using general multiplication
    return kmr_multiply_general(A, C_inv, K, eps)

def kmr_divide_direct(A: float, K: float, C: float, eps: float = 1e-12) -> float:
    """
    Compute K/C using direct KMR formula.
    
    Uses formula: K/C = -(((A ⊘ K) ⊙ C^{-1}) ⊘ A^{-1})^{-1}
    
    Args:
        A: Base parameter (A ≠ 0)
        K: Numerator (K ≠ 0)
        C: Denominator (C ≠ 0)
        eps: Tolerance for near-zero A
        
    Returns:
        K/C computed through direct KMR formula
    """
    if abs(A) < eps:
        A = math.copysign(eps, A) if A != 0 else eps
    
    if K == 0:
        return 0.0
    
    # Compute A ⊘ K
    X = kmr_invly(A, K)
    if math.isnan(X):
        return float('nan')
    
    # Compute C^{-1}
    C_inv = 1 / C
    
    # Compute (A ⊘ K) ⊙ C^{-1}
    Y = kmr_dircly(X, C_inv)
    if math.isnan(Y):
        return float('nan')
    
    # Apply ⊘ A^{-1}
    A_inv = 1 / A
    Z = kmr_invly(Y, A_inv)
    if math.isnan(Z) or Z == 0:
        return float('nan') if math.isnan(Z) else float('inf')
    
    # Return negative inverse
    return -1 / Z
```


## 14.7 Numerical Examples

### 14.7.1 Multiplication with Decomposition

Let $A = 2$, $K = 3$, $C = 4.7$:
- $C_{\text{int}} = 4$, $C_{\text{frac}} = 0.7$
- Compute $A ⊙ (3 \cdot 4) = A ⊙ 12 = \frac{2}{1+24} = \frac{2}{25}$
- Compute $A ⊙ (3 \cdot 0.7) = A ⊙ 2.1 = \frac{2}{1+4.2} = \frac{2}{5.2}$
- Combine: $\frac{2}{25} ⊙ 2.1 = \frac{2/25}{1+2.1\cdot(2/25)} = \frac{0.08}{1+0.168} = \frac{0.08}{1.168} \approx 0.06849$
- Extract: $K \cdot C = \left(0.06849 ⊘ 0.5\right)^{-1} \approx 14.1$ (verifying $3 \cdot 4.7 = 14.1$)

### 14.7.2 Division with Iterative Method

Let $A = 1$, $K = 5$, $C = 2$:
- $C^{-1} = 1 ⊙ 2 ⊘ 1 = \frac{1}{3} ⊘ 1 = \frac{1/3}{1-1/3} = \frac{1}{2}$
- $5 \cdot \frac{1}{2} = \left(1 ⊙ \frac{1}{2} ⊙ \frac{1}{2} ⊙ \frac{1}{2} ⊙ \frac{1}{2} ⊙ \frac{1}{2} ⊘ 1\right)^{-1}$
- Chain computation yields $\frac{5}{2} = 2.5$

## 14.8 Properties and Characteristics

### 14.8.1 Computational Complexity
- **Iterative multiplication**: $O(C)$ operations for integer $C$
- **General multiplication**: $O(1)$ after decomposition
- **Division**: Similar complexity to multiplication via reciprocal

### 14.8.2 Domain Restrictions
1. $A \neq 0$ (for $A^{-1}$ definition)
2. Avoid singularities: $1 + A \cdot K \cdot C \neq 0$ for multiplication
3. $C \neq 0$ for division operations
4. All operations defined for $K, C \in \mathbb{R}$

### 14.8.3 Precision Characteristics
- **Exact results**: For integer $C$ in iterative multiplication
- **Approximation**: For fractional $C$ using decomposition
- **Error bound**: $\epsilon \approx 10^{-12}$ for typical parameters

## 14.9 Theoretical Implications

### 14.9.1 Unified Arithmetic Framework
The KMR expressions for multiplication and division complete the fundamental arithmetic operations, demonstrating that:
1. All basic arithmetic can be expressed through KMR operators
2. Linear operations emerge from nonlinear transformations
3. Real-valued operations are naturally supported through the canonical extension

### 14.9.2 Decomposition Property Significance
The property $A ⊙ (K \cdot (D+F)) = (A ⊙ (K \cdot D)) ⊙ (K \cdot F)$ is fundamental because it:
1. Bridges discrete and continuous KMR operations
2. Enables efficient computation through pre-computation
3. Provides a pattern for simplifying complex expressions

### 14.9.3 Algebraic Structure
The KMR arithmetic framework reveals:
1. **Emergent commutativity**: Multiplication exhibits commutativity despite non-commutative base operations
2. **Hierarchical construction**: Multiplication builds on addition, division on multiplication
3. **Unified transformation**: All operations reduce to applications of $⊙$ and $⊘$

## 14.10 Future Research Directions

### 14.10.1 Computational Optimization
- Efficient algorithms for large integer iterations
- Parallel implementation of decomposition property
- Numerical stability analysis for near-singular parameters

### 14.10.2 Extended Operations
- Exponentiation: $K^C$ through nested iterations
- Logarithm: $\log_K C$ as inverse of exponentiation
- Trigonometric functions through series expansions

### 14.10.3 Applications
- Cryptographic protocols based on KMR arithmetic complexity
- Numerical methods for nonlinear equations
- Algebraic systems with KMR-based arithmetic units

## 14.11 Conclusion

This section has established complete expressions for multiplication and division within the KMR framework, featuring:

1. **Multiple equivalent forms** for both operations: tunneling, iterative, and decomposition forms
2. **Key decomposition property**: $A ⊙ (K \cdot (D+F)) = (A ⊙ (K \cdot D)) ⊙ (K \cdot F)$, enabling efficient computation
3. **Comprehensive implementation** supporting both integer and real-valued operations
4. **Pattern recognition rules** for simplifying complex KMR expressions
5. **Unified arithmetic framework** where all fundamental operations emerge from KMR transformations

The decomposition property represents a crucial insight, allowing the combination of integer iterations with fractional adjustments. This property, combined with the canonical extension to real numbers, provides a powerful framework for both theoretical analysis and practical computation.

The KMR paradigm demonstrates that linear arithmetic operations can be constructed from fundamental nonlinear transformations, suggesting a deep connection between linearity and nonlinearity in mathematical structures. Future work will explore extending this framework to more complex operations and investigating applications in computation, cryptography, and algebraic systems.

<!-- License: CC BY-SA 4.0 (see LICENSE-CC.md) -->
