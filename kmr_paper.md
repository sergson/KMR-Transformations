<!-- 
License: CC BY-SA 4.0 (see LICENSE-CC.md)
-->

### For Theoretical Content
- All mathematical formulations and documentation must be licensed under **CC BY-SA 4.0**
- When adding new theoretical content, include the header:
```markdown
<!-- 
License: CC BY-SA 4.0 (see LICENSE-CC.md)
-->```

# KMR Transformations: Novel Binary Operators  
**Author**: Sergei Terikhov  
**Date**: 04.05.2025

## KMR Acronym Interpretations  
- **K**-modulated Möbius Reduction  
- **K**-ordered Metric Rescaling  

## Mathematical Definitions  

### Direct KMR Operator (⊙)  
$$ A ⊙ K ≔ \frac{A}{1 + AK} $$  

### Inverse KMR Operator (⊘)  
$$ A ⊘ K ≔ \frac{A}{1 - AK} $$  

## Core Algebraic Properties

### Direct KMR Operator (⊙)
| Property               | Formula                               | Note                                                                  |
|------------------------|---------------------------------------|-----------------------------------------------------------------------|
| **Closure**            | \( A ⊙ K \in \mathbb{R} \)            | Defined ∀ \( A,K \in \mathbb{R}\setminus\{-\frac{1}{K}\} \)          |
| **Non-Associativity**  | \( (A ⊙ K) ⊙ C \neq A ⊙ (K ⊙ C) \) | Example: \( (1 ⊙ 2) ⊙ 3 = 0.1666 \neq 1 ⊙ (2 ⊙ 3) = 0.2222 \)     |
| **Identity Element**   | \( A ⊙ 0 = A \)                       | The zero element retains its value                                   |
| **Non-Commutativity**  | \( A ⊙ K \neq K ⊙ A \)               | Example: \( 1 ⊙ 2 = 0.333 \neq 2 ⊙ 1 = 0.666 \)                     |

### Inverse KMR Operator (⊘)
| Property               | Formula                                  | Note                                      |
|------------------------|------------------------------------------|-------------------------------------------|
| **Inversion**          | \( (A ⊘ K) ⊙ K = A \)                  | Full restoration of the original value    |
| **Singularity**        | \( \lim_{K \to 1/A} A ⊘ K = \infty \)   | Vertical asymptote at \( AK \to 1 \)      |

### Composition Laws
1. **Sequential Application**:
   \[
   A ⊙ K ⊙ C ≔ \frac{A}{1 + AK + AC + AKC}
   \]
2. **Mixed Operations**:
   \[
   A ⊙ (K ⊘ C) = \frac{A(1 - KC)}{1 + AK - AKC}
   \]
3. **Fixed Points**:
   \[
   \exists X : A ⊙ X = X \implies X = 0
   \]

## Python Implementation of mathematical definitions  
```python
# License: CC BY-SA 4.0 (see LICENSE-CC.md)
def kmrd(A, K):
    """A ⊙ K operation
       KMR direct operator: A/(1+A) (works for all A ≠ -1)"""
    return A / (1 + A)

def kmri(A, K):
    """A ⊘ K operation
       KMR inverse operator: A/(1-A) (works for all A ≠ 1)"""
    return A / (1 - A) if (1 - A) != 0 else float('inf')

def kmr_dircly(A: float, K: float) -> float:
    """A ⊙ K OR A ⊘ K
       KMR calculation: A/(1+K*A) for K ∈ ℝ"""
    return A / (1 + K * A) if (1 + K * A) != 0 else float('inf')```

## Iterative Properties of Operators

### KMR Continued Fraction Decomposition
Both operators represent continued fractions with `K` iterations:

**Direct operator (⊙)**:
A ⊙ K = A/(1 + A/(1 + A/(... + A/(1 + A)))) (K iterations)

**Inverse operator (⊘)**:
A ⊘ K = A/(1 - A/(1 - A/(... - A/(1 - A)))) (K iterations)

### Decomposition Components
For KMR decomposition, we define:
- KMR₀ = A
- KMRₙ₊₁ = KMRₙ/(1 ± KMRₙK) (sign depends on operator)
Or
- A₀ = A
- Aₙ₊₁ = Aₙ/(1 ± AₙK) (sign depends on operator)

## Iterative Python Implementation

```python
def kmr_iter_n(A: float, K: int) -> list[float]:
  """A ⊘ K via continued fraction (iterative approach)
     Iterative KMR^n calculation for any K ∈ ℤ
     Returns [KMR_0, KMR_1, ..., KMR_K]"""
  if not isinstance(K, int):
      raise ValueError("K must be integer")
      
  result = [A]
  for _ in range(abs(K)):
      result.append(kmrp(result[-1]) if K >= 0 
                   else kmrm(result[-1]))
  return result
