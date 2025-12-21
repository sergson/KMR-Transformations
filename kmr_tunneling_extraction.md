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

# 11. Tunneling Property and Element Extraction in KMR Chains
**Author**: Sergei Terikhov  
**Date**: 08.12.2025  

## 11.1 Introduction

This section introduces two fundamental properties of KMR operators that enable powerful algebraic manipulations:

1. **Tunneling (Shielding) Property**: The ability to "tunnel through" arbitrary KMR chains to extract the inverse of a value
2. **Element Extraction**: Methods to isolate individual elements from multi-step KMR compositions

These properties demonstrate the deep algebraic structure of KMR operators and provide computational tools for analyzing complex KMR expressions.

**Chain Notation Convention**: Throughout this document, chains of KMR operators are interpreted as left-associative. For example, \( A ⊙ K ⊙ C ⊙ D \) means \( ((A ⊙ K) ⊙ C) ⊙ D \). This notation convention is discussed in detail in Section 12 (Chain Notation and Left-Associativity Convention).

## 11.2 Tunneling (Shielding) Property

### 11.2.1 Fundamental Tunneling Identity

For any valid values $Y \neq 0$ and $X$ (where all operations are defined), the following identity holds:  
$Y ⊙ X ⊘ Y^{-1} = X^{-1}$

*Proof*:  
$Y ⊙ X = \frac{Y}{1 + Y X}$   

$$
(Y ⊙ X) ⊘ Y^{-1} = \frac{\frac{Y}{1 + Y X}}{1 - Y^{-1} \cdot \frac{Y}{1 + Y X}} 
= \frac{\frac{Y}{1 + Y X}}{1 - \frac{1}{1 + Y X}} 
= \frac{\frac{Y}{1 + Y X}}{\frac{Y X}{1 + Y X}} 
= \frac{Y}{Y X} = \frac{1}{X} = X^{-1}
\quad \square
$$

### 11.2.2 Generalization to Arbitrary Chains

For any KMR chain $Y = A_1 ⊙ A_2 ⊙ \dots ⊙ A_n$, the tunneling property extends to:  

$(A_1 ⊙ A_2 ⊙ \dots ⊙ A_n) ⊙ X ⊘ (A_1 ⊙ A_2 ⊙ \dots ⊙ A_n)^{-1} = X^{-1}$

### 11.2.3 Interpretation

The tunneling property shows that:
1. Any KMR chain $Y$ can serve as a "container" that transforms $X$ to $X^{-1}$
2. The result $X^{-1}$ is independent of the specific content of $Y$ (provided $Y \neq 0$)
3. This represents a form of algebraic "shielding" where the chain $Y$ becomes transparent to the extraction of $X^{-1}$  

### 11.2.4 Special Case: Y = 1

A particularly elegant and simple case of the tunneling property occurs when \(Y = 1\):   

$$
1 ⊙ X ⊘ 1 = X^{-1}
$$

*Proof*:  
From the general tunneling identity $(Y ⊙ X ⊘ Y^{-1} = X^{-1})$, substitute $(Y = 1)$. Since $(1^{-1} = 1)$, we obtain:  

$$
1 ⊙ X ⊘ 1 = X^{-1} \quad \square
$$

*Numerical Example*:  
Let \(X = 5\). Then:   
$1 ⊙ 5 = \frac{1}{1 + 1 \cdot 5} = \frac{1}{6} \approx 0.1667$  
$\frac{1}{6} ⊘ 1 = \frac{1/6}{1 - 1 \cdot (1/6)} = \frac{1/6}{5/6} = \frac{1}{5} = 5^{-1}$

*Interpretation*:  
This special case demonstrates that the simplest possible chain—a single element equal to 1—can already serve as a complete “tunnel” to extract the inverse of any \(X\). It underscores the fundamental nature of the tunneling property and provides a minimal computational recipe for obtaining $(X^{-1})$ using only the basic KMR operators.


## 11.3 Element Extraction from KMR Chains

### 11.3.1 Notation

Consider a chain of $n$ elements:  
$X = A_1 ⊙ A_2 ⊙ \dots ⊙ A_n$

### 11.3.2 Extracting the First Element

$A_1 = X ⊘ A_n ⊘ A_{n-1} ⊘ \dots ⊘ A_2$

*Explanation*: Sequential application of the inverse operator cancels the corresponding direct operations from right to left.

### 11.3.3 Extracting the Last Element

Let $Z = A_1 ⊙ A_2 ⊙ \dots ⊙ A_{n-1}$. Then:  

$X = Z ⊙ A_n \implies A_n = \frac{1}{X} - \frac{1}{Z} = X^{-1} - Z^{-1}$

where $Z$ can be computed if $A_1, \dots, A_{n-1}$ are known.

### 11.3.4 Extracting an Intermediate Element $A_k$

Let:
- $L = A_1 ⊙ A_2 ⊙ \dots ⊙ A_{k-1}$ (left part, computed sequentially)
- Right elements: $A_{k+1}, A_{k+2}, \dots, A_n$ (known, but not composed due to non-associativity)

**Step 1**: Compute $D$ by sequentially canceling all elements to the right of $A_k$:

$$
D = X ⊘ A_n ⊘ A_{n-1} ⊘ \dots ⊘ A_{k+1}
$$

This yields $D = L ⊙ A_k$.

**Step 2**: Extract $A_k$ from $D$ and $L$ using the basic inverse formula:

$$
D = L ⊙ A_k = \frac{L}{1 + L \cdot A_k} \implies A_k = \frac{1}{D} - \frac{1}{L}
$$

**Final working formula**:

$$
A_k = \frac{1}{X ⊘ A_n ⊘ A_{n-1} ⊘ \dots ⊘ A_{k+1}} - \frac{1}{A_1 ⊙ A_2 ⊙ \dots ⊙ A_{k-1}}
$$

where:
- $A_1 ⊙ A_2 ⊙ \dots ⊙ A_{k-1}$ is computed sequentially from left to right
- $X ⊘ A_n ⊘ A_{n-1} ⊘ \dots ⊘ A_{k+1}$ is computed sequentially from right to left

### 11.3.5 Complete Recovery: Finding A_k When All Other Elements Are Known

If only the full chain $X$ and all elements except $A_k$ are known, then $A_k$ can be found by:

1. Compute the left accumulation $L = A_1 ⊙ A_2 ⊙ \dots ⊙ A_{k-1}$ sequentially
2. Compute $D$ by sequentially applying inverse operators to cancel all elements to the right of $A_k$:

$$
D = X ⊘ A_n ⊘ A_{n-1} ⊘ \dots ⊘ A_{k+1}
$$

3. Extract $A_k$ using:

$$
A_k = \frac{1}{D} - \frac{1}{L}
$$

This formula works for any position $k$ in the chain ($1 < k < n$).

## 11.4 Examples

### Example 1: Three-Element Chain
Let $X = A ⊙ B ⊙ C$, where $A = 2$, $B = 3$, $C = 4$.

1. **Extracting $A$**:  
$A = X ⊘ C ⊘ B = (2 ⊙ 3 ⊙ 4) ⊘ 4 ⊘ 3 = 2$

2. **Extracting $B$ given $A$ and $C$**:
$L = A = 2$  
$D = X ⊘ C = (2 ⊙ 3 ⊙ 4) ⊘ 4 = 2 ⊙ 3 = \frac{2}{7}$  
$B = \frac{1}{D} - \frac{1}{L} = \frac{7}{2} - \frac{1}{2} = 3$

3. **Extracting $C$ given $A$ and $B$**:  
$Z = A ⊙ B = \frac{2}{7}$  
$X = 2 ⊙ 3 ⊙ 4 = \frac{2}{15}$  
$C = \frac{1}{X} - \frac{1}{Z} = \frac{15}{2} - \frac{7}{2} = 4$

### Example 2: Four-Element Chain
Let $X = 2 ⊙ 3 ⊙ 4 ⊙ 5$

Compute $X$:
$2 ⊙ 3 = \frac{2}{7} \approx 0.2857$  
$0.2857 ⊙ 4 = \frac{0.2857}{1 + 0.2857 \cdot 4} = \frac{0.2857}{2.1428} \approx 0.1333$  
$0.1333 ⊙ 5 = \frac{0.1333}{1 + 0.1333 \cdot 5} = \frac{0.1333}{1.6665} \approx 0.08$

**Extracting $A_2 = 3$ (k=2)**:
- $L = A_1 = 2$
- $D = X ⊘ A_4 ⊘ A_3 = 0.08 ⊘ 5 ⊘ 4$  
  $D_1 = 0.08 ⊘ 5 = \frac{0.08}{1 - 0.08 \cdot 5} = \frac{0.08}{0.6} \approx 0.1333$  
  $D = 0.1333 ⊘ 4 = \frac{0.1333}{1 - 0.1333 \cdot 4} = \frac{0.1333}{0.4668} \approx 0.2857$
- $A_2 = \frac{1}{0.2857} - \frac{1}{2} \approx 3.5 - 0.5 = 3$ ✓

**Extracting $A_3 = 4$ (k=3)**:
- $L = A_1 ⊙ A_2 = 2 ⊙ 3 = \frac{2}{7} \approx 0.2857$
- $D = X ⊘ A_4 = 0.08 ⊘ 5 \approx 0.1333$
- $A_3 = \frac{1}{0.1333} - \frac{1}{0.2857} \approx 7.5 - 3.5 = 4$ ✓


### Example 3: Tunneling Application
Let $Y = 1 ⊙ 2 = \frac{1}{3}$, $X = 5$.

Applying the tunneling property:

$Y ⊙ X ⊘ Y^{-1} = \frac{1}{3} ⊙ 5 ⊘ 3 = \frac{1/3}{1+(5/3)} ⊘ 3 = \frac{1/3}{8/3} ⊘ 3 = \frac{1}{8} ⊘ 3$
$= \frac{1/8}{1-3/8} = \frac{1/8}{5/8} = \frac{1}{5} = 5^{-1}$

## 11.5 Applications

### 11.5.1 State Recovery in Transformation Chains
If $A_1, A_2, \dots, A_n$ represent successive transformations applied to a system, and $X$ is the final state, then:
- Initial state: $A_1 = X ⊘ A_n ⊘ \dots ⊘ A_2$
- Any intermediate state: $S_k = A_1 ⊙ \dots ⊙ A_k$

### 11.5.2 Cryptographic Applications
The tunneling property enables the creation of one-way functions:
1. **Forward transformation**: $F(Y, X) = Y ⊙ X ⊘ Y^{-1} = X^{-1}$
2. **Reverse transformation**: Requires knowledge of $Y$ to recover $X$ from $X^{-1}$
3. **Key generation**: Long KMR chains can serve as private keys

### 11.5.3 Computational Optimization
Element extraction properties allow:
- Parallel computation of chain segments
- Integrity verification in distributed computations
- Recovery of lost elements in transformation sequences

## 11.6 Python Implementation

```python
def extract_intermediate_element(X: float, left_chain: list, right_chain: list) -> float:
    """
    Extract intermediate element A_k from KMR chain.
    
    Args:
        X: Final result of the chain A₁ ⊙ ... ⊙ Aₙ
        left_chain: List [A₁, ..., A_{k-1}] in original order
        right_chain: List [A_{k+1}, ..., Aₙ] in original order
        
    Returns:
        The element A_k
    """
    # Compute L = A₁ ⊙ ... ⊙ A_{k-1} (left accumulation)
    L = left_chain[0] if left_chain else 0
    for element in left_chain[1:]:
        denom = 1 + L * element
        if abs(denom) < 1e-12:  # Numerical stability check
            return float('nan')
        L = L / denom
    
    # Compute D = X ⊘ Aₙ ⊘ ... ⊘ A_{k+1} (right cancellation)
    D = X
    for element in reversed(right_chain):
        denom = 1 - element * D
        if abs(denom) < 1e-12:  # Numerical stability check
            return float('nan')
        D = D / denom
    
    # Compute A_k = 1/D - 1/L
    if abs(D) < 1e-12 or abs(L) < 1e-12:
        return float('nan')
    
    return 1/D - 1/L

# Example usage for 4-element chain
X = 2 ⊙ 3 ⊙ 4 ⊙ 5  # ≈ 0.08

# Extract A₂ = 3
A2 = extract_intermediate_element(
    X=0.08,
    left_chain=[2],      # A₁
    right_chain=[4, 5]   # A₃, A₄
)
# Result: A2 ≈ 3

# Extract A₃ = 4
A3 = extract_intermediate_element(
    X=0.08,
    left_chain=[2, 3],   # A₁, A₂
    right_chain=[5]      # A₄
)
# Result: A3 ≈ 4
```

## 11.7 Theoretical Implications

The discovered properties reveal deep algebraic structure in KMR operators:

1.  **Tunneling Property**: Demonstrates that arbitrary KMR chains can be used to transform $X$ to $X^{-1}$ independently of the chain's content, showing a form of algebraic invariance.
    
2.  **Element Extraction**: Shows that KMR chains behave similarly to non-commutative groups with special inversion properties, allowing recovery of individual elements from composite expressions.
    
3.  **Practical Significance**: Enables new algorithms for sequence processing, cryptographic protocol design, and computational optimization with KMR transformations.
    

## 11.8 Conclusion

The tunneling and element extraction properties provide powerful tools for analyzing and manipulating KMR expressions. These results:

-   Uncover fundamental algebraic structures in KMR operators
    
-   Enable practical applications in computation and cryptography
    
-   Open new research directions in nonlinear algebraic systems
    

These properties, combined with previously established KMR identities, form a comprehensive algebraic framework for working with KMR transformations in both theoretical and applied contexts.
