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

$L = A_1 ⊙ A_2 ⊙ \dots ⊙ A_{k-1} \quad \text{(left part)}$ 
$R = A_{k+1} ⊙ \dots ⊙ A_n \quad \text{(right part)}$
Then:
$X = L ⊙ A_k ⊙ R$

**Step 1**: Compute $L ⊙ A_k = X ⊘ R$ (if $R$ is non-empty, otherwise $L ⊙ A_k = X$)

**Step 2**: From $L ⊙ A_k = D$, extract $A_k$: 

$D = \frac{L}{1 + L A_k} \implies A_k = \frac{L - D}{L D} = \frac{1}{D} - \frac{1}{L}$

**Final formula**: 

$$
A_k = \frac{1}{X ⊘ R} - \frac{1}{L} = ({X ⊘ R})^{-1} - {L}^{-1}
$$  

where:
- $L$ is computed from known $A_1, \dots, A_{k-1}$
- $R$ is computed from known $A_{k+1}, \dots, A_n$

### 11.3.5 Special Case: Extracting $A_k$ Without Neighbors

If only the full chain $X$ and all elements except $A_k$ are known, then $A_k$ can be found by solving:  

$X = A_1 ⊙ \dots ⊙ A_{k-1} ⊙ A_k ⊙ A_{k+1} ⊙ \dots ⊙ A_n$  

which gives:  

$A_k = \frac{1}{X ⊘ (A_{k+1} ⊙ \dots ⊙ A_n)} - \frac{1}{A_1 ⊙ \dots ⊙ A_{k-1}}$

## 11.4 Examples

### Example 1: Three-Element Chain
Let $X = A ⊙ B ⊙ C$, where $A = 2$, $B = 3$, $C = 4$.

1. **Extracting $A$**:  

$A = X ⊘ C ⊘ B = (2 ⊙ 3 ⊙ 4) ⊘ 4 ⊘ 3 = 2$

3. **Extracting $B$ given $A$ and $C$**:

$L = A = 2, \quad R = C = 4$

$D = X ⊘ R = (2 ⊙ 3 ⊙ 4) ⊘ 4 = 2 ⊙ 3 = \frac{2}{7}$
$B = \frac{1}{D} - \frac{1}{L} = \frac{7}{2} - \frac{1}{2} = 3$

4. **Extracting $C$ given $A$ and $B$**: 

$Z = A ⊙ B = \frac{2}{7}$
$X = 2 ⊙ 3 ⊙ 4 = \frac{2}{15}$
$C = X^{-1} - Z^{-1} = \frac{15}{2} - \frac{7}{2} = 4$

### Example 2: Tunneling Application
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
def kmr_tunnel(Y: float, X: float) -> float:
    """
    Compute Y ⊙ X ⊘ Y^{-1} = X^{-1} (tunneling property)
    
    Args:
        Y: Tunneling parameter (Y ≠ 0)
        X: Input value
        
    Returns:
        X^{-1} (inverse of X)
    """
    if Y == 0:
        raise ValueError("Y must not be zero")
    
    # Y ⊙ X
    Y_odot_X = Y / (1 + Y * X) if (1 + Y * X) != 0 else float('nan')
    
    # Y^{-1}
    Y_inv = 1 / Y
    
    # (Y ⊙ X) ⊘ Y^{-1}
    result = Y_odot_X / (1 - Y_inv * Y_odot_X) if (1 - Y_inv * Y_odot_X) != 0 else float('nan')
    
    return result

def extract_first_element(X: float, *chain) -> float:
    """
    Extract the first element from a KMR chain.
    
    Args:
        X: Final result of the chain
        *chain: The known elements A2, A3, ..., An
        
    Returns:
        The first element A1
    """
    result = X
    for element in reversed(chain):
        result = result / (1 - element * result) if (1 - element * result) != 0 else float('nan')
    return result

def extract_element(X: float, left_part: float, right_part: float) -> float:
    """
    Extract an intermediate element from a KMR chain.
    
    Args:
        X: Full chain result
        left_part: Value of L = A1 ⊙ ... ⊙ A_{k-1}
        right_part: Value of R = A_{k+1} ⊙ ... ⊙ An
        
    Returns:
        The element A_k
    """
    if right_part == 0:
        D = X
    else:
        # Compute X ⊘ R
        D = X / (1 - right_part * X) if (1 - right_part * X) != 0 else float('nan')
    
    # Compute A_k = 1/D - 1/L
    if D == 0 or left_part == 0:
        return float('nan')
    return 1/D - 1/left_part
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
