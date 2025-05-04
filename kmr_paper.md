<!-- 
License: CC BY-SA 4.0 (see LICENSE-CC.md)
-->

### For Theoretical Content
- All mathematical formulations and documentation must be licensed under **CC BY-SA 4.0**
- When adding new theoretical content, include the header:
<!-- 
License: CC BY-SA 4.0 (see LICENSE-CC.md)
-->

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
   $$ A ⊙ K ⊙ C ≔ \frac{A}{1 + AK + AC + AKC} $$

2. **Mixed Operations**:
   $$ A ⊙ (K ⊘ C) = \frac{A(1 - KC)}{1 + AK - AKC} $$

3. **Fixed Points**:
  $$ \exists X : A ⊙ X = X \implies X = 0 $$

4. **Iterated Application**:
  $$ A ⊙ \underbrace{K ⊙ K ⊙ \dots ⊙ K}_{n \text{ times}} = A ⊙ K n = \frac{A}{1 + A K n} $$
  $$ A ⊘ \underbrace{K ⊘ \dots ⊘ K}_{n \text{ times}} = A ⊘ K n = \frac{A}{1 - A K n} $$
  **Special case of iterated application**: (when \( K = 1 \)):
  $$ A ⊙ \underbrace{1 ⊙ \dots ⊙ 1}_{n \text{ times}} = A ⊙ n $$
  $$ A ⊘ \underbrace{1 ⊘ \dots ⊘ 1}_{n \text{ times}} = A ⊘ n $$

## Python Implementation of mathematical definitions  
```python
# License: CC BY-SA 4.0 (see LICENSE-CC.md)
def kmrd(A):
    """A ⊙ 1 operation
       KMR direct operator: A/(1+A) (works for all A ≠ -1)"""
    return A / (1 + A)

def kmri(A):
    """A ⊘ 1 operation
       KMR inverse operator: A/(1-A) (works for all A ≠ 1)"""
    return A / (1 - A) if (1 - A) != 0 else float('inf')

def kmr_dircly(A: float, K: float) -> float:
    """A ⊙ K OR A ⊘ K
       KMR calculation: A/(1+K*A) for K ∈ ℝ"""
    return A / (1 + K * A) if (1 + K * A) != 0 else float('inf')```

## Iterative Properties of Operators

### KMR Decomposition

Both operators represent fractions obtained by `K` multiple composition (iterations):

#### Direct Operator (⊙)
**Definition**:  
For a given initial value `A` and `K` iterations:
$$
\mathrm{KMR}(n) = \frac{\mathrm{KMR}(n-1)}{1 + \mathrm{KMR}(n-1)},\quad \mathrm{KMR}(0) = A
$$

**Example: Calculate 1 ⊙ 2**
1. Initial value: $\mathrm{KMR}(0) = 1$
2. First iteration ($n=1$):
   $$\mathrm{KMR}(1) = \frac{1}{1+1} = \frac{1}{2}$$
3. Second iteration ($n=2$):
   $$\mathrm{KMR}(2) = \frac{\frac{1}{2}}{1+\frac{1}{2}} = \frac{\frac{1}{2}}{\frac{3}{2}} = \frac{1}{3}$$
   
**Result**: $1 ⊙ 2 = \frac{1}{3}$

**Notation**:  
$A ⊙ K$ computes $\mathrm{KMR}(K)$ using the direct operator (positive denominator)

#### Inverse Operator (⊘)
**Definition**:  
For a given initial value `A` and `K` iterations:
$$
\mathrm{KMR}(n) = \frac{\mathrm{KMR}(n-1)}{1 - \mathrm{KMR}(n-1)},\quad \mathrm{KMR}(0) = A
$$

**Example: Calculate 1/3 ⊘ 2**
1. Initial value: $\mathrm{KMR}(0) = \frac{1}{3}$
2. First iteration ($n=1$):
   $$\mathrm{KMR}(1) = \frac{\frac{1}{3}}{1-\frac{1}{3}} = \frac{\frac{1}{3}}{\frac{2}{3}} = \frac{1}{2}$$
3. Second iteration ($n=2$):
   $$\mathrm{KMR}(2) = \frac{\frac{1}{2}}{1-\frac{1}{2}} = \frac{\frac{1}{2}}{\frac{1}{2}} = 1$$
   
**Result**: $\frac{1}{3} ⊘ 2 = 1$

**Notation**:  
$A ⊘ K$ computes $\mathrm{KMR}(K)$ using the inverse operator (negative denominator)

### Decomposition Components

The KMR decomposition can be represented both recursively and through direct formulas:

#### 1. Recursive Definition
- **Base case**:  
  $\mathrm{KMR}(0) = A$
  
- **Recursive step**:  
  $\mathrm{KMR}({n+1}) = \frac{\mathrm{KMR}(n)}{1 \pm \mathrm{KMR}(n)}$  
  (where `+` for ⊙, `-` for ⊘)

#### 2. Direct Formulas (Non-Recursive)
For $K$ iterations:

**Direct operator (⊙)**:
$$
\mathrm{KMR}(K) = \frac{A}{1 + K \cdot A}
$$

**Inverse operator (⊘)**:
$$
\mathrm{KMR}(K) = \frac{A}{1 - K \cdot A} \quad \text{(for } K \cdot A < 1\text{)}
$$

#### 3. Composition Rules
The final value can be expressed as:
- **As continued fraction**:  
  $\mathrm{KMR}(K) = \cfrac{A}{1 \pm \cfrac{A}{1 \pm \cfrac{A}{\ddots \pm A}}}$ (K levels)

- **As product expansion**:  
  $\mathrm{KMR}(K) = A \prod_{i=1}^{K} \frac{1}{1 \pm (i \cdot A)}$

#### 4. Numerical Example
Let's compute $2 ⊙ 3$ both recursively and directly:

**Recursive method**:
1. $\mathrm{KMR}(0) = 2$
2. $\mathrm{KMR}(1) = \frac{2}{1+2} = \frac{2}{3} \approx 0.6667$
3. $\mathrm{KMR}(2) = \frac{\frac{2}{3}}{1+\frac{2}{3}} = \frac{2}{5} = 0.4$
4. $\mathrm{KMR}(3) = \frac{\frac{2}{5}}{1+\frac{2}{5}} = \frac{2}{7} \approx 0.2857$
As full fraction:
$$ 
2 ⊙ 3 = \frac{2}{1 + \frac{2}{1 + \frac{2}{1 + \underbrace{2}_{K=1}}}}
$$ 
**Direct formula**:
$$
\mathrm{KMR}(3) = \frac{2}{1 + 3 \cdot 2} = \frac{2}{7} \approx 0.2857
$$

#### 5. Component Interpretation
Each component $\mathrm{KMR}(n)$ represents:
- Partial evaluation after $n$ steps
- Intermediate convergence rate (⊙) or divergence factor (⊘)
- Building blocks for the final composition:  
  $\mathrm{KMR}(K) = \mathrm{COMPOSE}(\mathrm{KMR}(0), \mathrm{KMR}(1), ..., \mathrm{KMR}(K)$

#### 6. Validity Conditions
- For ⊙: Always converges for $A > 0$
- For ⊘: Only valid when $K \cdot A < 1$ (avoid division by zero)

## Iterative Python Implementation

```python
def kmr_iter_n(A: float, K: int) -> list[float]:
  """A ⊘ K via continued fraction (iterative approach)
     Iterative KMR(n) calculation for any K ∈ ℤ
     Returns [KMR(0), KMR(1), ..., KMR(K)]"""
  if not isinstance(K, int):
      raise ValueError("K must be integer")
      
  result = [A]
  for _ in range(abs(K)):
      result.append(kmrp(result[-1]) if K >= 0 
                   else kmrm(result[-1]))
  return result
