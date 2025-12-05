
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

# KMR Transformations: Novel Binary Operators  
**Author**: Sergei Terikhov  
**Date**: 04.05.2025


## 1. Introduction

### 1.1 KMR Acronym Interpretations  
- **K**-modulated Möbius Reduction  
- **K**-ordered Metric Rescaling 

### 1.2 Composition in Mathematics and Its Application to a Recurrent Formula

In mathematics, the composition of functions is typically denoted by the symbol ∘. For example, given two functions f and g, their composition is written as f∘g and defined as:  
`(f∘g)(x) = f(g(x))`

### 1.3 Problem Statement  
We are given a recurrent formula:  
`A_{n+1} = A_n/(1 + A_n)`  
where:  
- Initial value: `A_0 = A`  
- Operation is applied recursively K times  

This is equivalent to repeatedly applying:  
`f(x) = x/(1 + x)`

Thus, A(K) is:  
`A(K) = (f ∘ f ∘ ... ∘ f)(A) = f^K(A)`  
(where f^K means K applications of f)

### 1.4 Computation Examples:
1. **K=1**:  
   `A(1) = A/(1 + A)`
2. **K=2**:  
   `A(2) = [A/(1+A)]/[1 + A/(1+A)] = A/(1 + 2A)`
3. **K=3**:  
   `A(3) = [A/(1+2A)]/[1 + A/(1+2A)] = A/(1 + 3A)`

### 1.5 General Solution:
`A(K) = A/(1 + K A)`

### 1.6 Proof by Induction:
1. **Base case (K=1)**:  
   Matches the first iteration ✓
2. **Inductive step**:  
   If true for K=n: `A(n) = A/(1 + n A)`  
   Then for K=n+1:  
   `A(n+1) = [A/(1+nA)]/[1 + A/(1+nA)] = A/(1 + (n+1)A)` ✓

### 1.7 Final Answer:
The K-fold composition gives:  
`A(K) = A/(1 + K A)`


## 2. Mathematical Definitions of KMR 

### 2.1 Direct KMR Operator (⊙)  
$$ A ⊙ K ≔ \underbrace{(\frac{A}{1 + A} ∘ \frac{A}{1 + A} \dots ∘ \frac{A}{1 + A})}_{K \text{ times}} $$ 

### 2.2 Inverse KMR Operator (⊘)
$$ A ⊘ K ≔ \underbrace{(\frac{A}{1 - A} ∘ \frac{A}{1 - A} \dots ∘ \frac{A}{1 - A})}_{K \text{ times}} $$  


## 3. KMR General Solutions

### 3.1 Direct KMR General Solution
$$ A ⊙ K ≔ \frac{A}{1 + AK} $$ 

### 3.2 Inverse KMR General Solution
$$ A ⊘ K ≔ \frac{A}{1 - AK} $$


## 4. Handling Singularities in Stepwise Computations

When recursively applying the operator \( ⊙ 1 \), a singularity \( s = $\frac{1}{0}$ \, `float('inf')`in Python) may occur at step \( m \), interrupting the computation chain. To maintain consistency with the explicit KMR formula \( A ⊙ K = $\frac{A}{1 + AK}$ \), we implement:

1. **Singularity Regularization**  
   Replace the singular step \( s ⊙ 1 \) with the general solution value:  
   $$s ⊙ 1 \coloneqq \frac{A}{1 + K A}$$  
   $$s ⊘ 1 \coloneqq \frac{A}{1 - K A}$$  
   where:
   - \( A) = initial input value
   - \( K \) = total steps in computation

2. **Validity Conditions**  
   This substitution requires:  
   $$1 + K A \neq 0$$  
   Otherwise, the singularity is fundamental (e.g., when \( A = $-\frac{1}{K}$ \)).

**Example Calculation**  
For \( A = -0.5 \), \( K = 3 \):
Step 1: -0.5 ⊙ 1 = -1
Step 2: -1 ⊙ 1 = s (singularity)
Step 3: s ⊙ 1 → (-0.5)/(1 + 3*(-0.5)) = 1  (singularity passed, calculations can continue if K > 3, define K=4)
Step 4: 1 ⊙ 1 = 0.5 (for K = 4)

## 5. Core Algebraic Properties

### 5.1 Direct KMR Operator (⊙)
| Property               | Formula                               | Note                                                                  |
|------------------------|---------------------------------------|-----------------------------------------------------------------------|
| **Closure**            | \( A ⊙ K $\in \mathbb{R}$ \)            | Defined ∀ \( A,K $\in\mathbb{R}\setminus\{-\frac{1}{K}\}$ \)          |
| **Non-Associativity**  | \( (A ⊙ K) ⊙ C $\neq$ A ⊙ (K ⊙ C) \) | Example: \( (1 ⊙ 2) ⊙ 3 = 0.1666 $\neq$ 1 ⊙ (2 ⊙ 3) = 0.2222 \)     |
| **Identity Element**   | \( A ⊙ 0 = A \)                       | The zero element retains its value                                   |
| **Non-Commutativity**  | \( A ⊙ K $\neq$ K ⊙ A \)               | Example: \( 1 ⊙ 2 = 0.333 $\neq$ 2 ⊙ 1 = 0.666 \)                     |

### 5.2 Inverse KMR Operator (⊘)
| Property               | Formula                                  | Note                                      |
|------------------------|------------------------------------------|-------------------------------------------|
| **Inversion**          | \( (A ⊘ K) ⊙ K = A \)                  | Full restoration of the original value    |
| **Singularity**        | \( $\lim_{K \to 1/A} A ⊘ K = \infty$ \)   | Vertical asymptote at \( AK $\to$ 1 \)      |

### 5.3 Composition Laws
1. **Sequential Application**:  
   $$A ⊙ K ⊙ C ≔ \frac{A}{1 + AK + AC + AKC}$$

2. **Mixed Operations**:  
   $$A ⊙ (K ⊘ C) = \frac{A(1 - KC)}{1 + AK - AKC}$$

3. **Fixed Points**:  
  $$\exists X : A ⊙ X = X \implies X = 0$$

4. **Iterated Application**:   
   $$A ⊙ \underbrace{K ⊙ K ⊙ \dots ⊙ K}_{n \text{ times}} = A ⊙ Kn = \frac{A}{1 + A K n}$$

   $$A ⊘ \underbrace{K ⊘ \dots ⊘ K}_{n \text{ times}} = A ⊘ K n = \frac{A}{1 - A K n}$$
     
  **Special case of iterated application**: (when \( K = 1 \)):  
  $A ⊙ \underbrace{1 ⊙ \dots ⊙ 1}_{n \text{ times}} = A ⊙ n$  
  
  $A ⊘ \underbrace{1 ⊘ \dots ⊘ 1}_{n \text{ times}} = A ⊘ n$  


## 6. Python Implementation of mathematical definitions  
```python
# License: CC BY-SA 4.0 (see LICENSE-CC.md)
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
```

## 7. Iterative Properties of Operators

### 7.1 KMR Decomposition

Both operators represent fractions obtained by `K` multiple composition (iterations):

#### 7.1.1 Direct Operator (⊙)
**Definition**:  
For a given initial value `A` and `K` iterations:  
$$\mathrm{KMR}(n) = \frac{\mathrm{KMR}(n-1)}{1 + \mathrm{KMR}(n-1)},\quad \mathrm{KMR}(0) = A$$

**Example: Calculate 1 ⊙ 2**
1. Initial value: $\mathrm{KMR}(0) = 1$
2. First iteration ($n=1$):  
   $$\mathrm{KMR}(1) = \frac{1}{1+1} = \frac{1}{2}$$
3. Second iteration ($n=2$):  
   $$\mathrm{KMR}(2) = \frac{\frac{1}{2}}{1+\frac{1}{2}} = \frac{\frac{1}{2}}{\frac{3}{2}} = \frac{1}{3}$$
   
**Result**: $1 ⊙ 2 = \frac{1}{3}$

**Notation**:  
$A ⊙ K$ computes $\mathrm{KMR}(K)$ using the direct operator (positive denominator)

#### 7.1.2 Inverse Operator (⊘)
**Definition**:  
For a given initial value `A` and `K` iterations:
$$\mathrm{KMR}(n) = \frac{\mathrm{KMR}(n-1)}{1 - \mathrm{KMR}(n-1)},\quad \mathrm{KMR}(0) = A$$

**Example: Calculate 1/3 ⊘ 2**
1. Initial value: $\mathrm{KMR}(0) = \frac{1}{3}$
2. First iteration ($n=1$):
   $$\mathrm{KMR}(1) = \frac{\frac{1}{3}}{1-\frac{1}{3}} = \frac{\frac{1}{3}}{\frac{2}{3}} = \frac{1}{2}$$
3. Second iteration ($n=2$):
   $$\mathrm{KMR}(2) = \frac{\frac{1}{2}}{1-\frac{1}{2}} = \frac{\frac{1}{2}}{\frac{1}{2}} = 1$$
   
**Result**: $\frac{1}{3} ⊘ 2 = 1$

**Notation**:  
$A ⊘ K$ computes $\mathrm{KMR}(K)$ using the inverse operator (negative denominator)

### 7.2 Decomposition Components

The KMR decomposition can be represented both recursively and through direct formulas:

#### 7.2.1 Recursive Definition
- **Base case**:  
  $\mathrm{KMR}(0) = A$
  
- **Recursive step**:  
  $\mathrm{KMR}({n+1}) = \frac{\mathrm{KMR}(n)}{1 \pm \mathrm{KMR}(n)}$  
  (where `+` for ⊙, `-` for ⊘)

#### 7.2.2 Direct Formulas (Non-Recursive)
For $K$ iterations:

**Direct operator (⊙)**:
$$\mathrm{KMR}(K) = \frac{A}{1 + K \cdot A}\quad \text{(for } K \cdot A \neq -1\text{)}$$

**Inverse operator (⊘)**:
$$\mathrm{KMR}(K) = \frac{A}{1 - K \cdot A} \quad \text{(for } K \cdot A \neq 1\text{)}$$

#### 7.3 Composition Rules
The final value can be expressed as:
- **As fraction**:  
  $\mathrm{KMR}(K) = A ⊙ K = \underbrace{\frac{\frac{\frac{A\ddots}{1+A\ddots}}{1+\frac{A\ddots}{1+A\ddots}}}{1+\frac{\frac{A\ddots}{1+A\ddots}}{1+\frac{A\ddots}{1+A\ddots}}}}_{2^K \text{ levels}}$

#### 7.4 Numerical Example
Let's compute $2 ⊙ 3$ both recursively and directly:

**Direct formula**:
$$\mathrm{KMR}(3) = \frac{2}{1 + 3 \cdot 2} = \frac{2}{7} \approx 0.2857$$

**Recursive method**:  
1. $\mathrm{KMR}(0) = 2$
   
3. $\mathrm{KMR}(1) = \frac{2}{1+2} = \frac{2}{3} \approx 0.6667$
   
5. $\mathrm{KMR}(2) = \frac{\frac{2}{3}}{1+\frac{2}{3}} = \frac{2}{5} = 0.4$
   
7. $\mathrm{KMR}(3) = \frac{\frac{2}{5}}{1+\frac{2}{5}} = \frac{2}{7} \approx 0.2857$
   
As full fraction:  
$$2 ⊙ 3 = \frac{\frac{\frac{2}{1+2}}{1 + \frac{2}{1+2}}}{1 + \frac{\frac{2}{1+2}}{ 1 + \frac{2}{1+2}}} =  \frac{\displaystyle \frac{2}{3}}{\displaystyle 1 + \frac{2}{3}} \Bigg/ \left(1 + \frac{\displaystyle \frac{2}{3}}{\displaystyle 1 + \frac{2}{3}}\right) = \frac{2/5}{1+2/5} = \frac{2}{7}$$ 

$$2 ⊙ 3 = KMR(0) ⊙ 1⊙ 1 ⊙ 1  = KMR(1) ⊙ 1 ⊙ 1 = KMR(2) ⊙ 1 = KMR(3)$$

## 8. Iterative Python Implementation

```python
def kmr_iter_n(A: float, K: int) -> list[float]:
    """A ⊙ K or A ⊘ K via fraction (iterative approach).
    Iterative KMR(n) calculation for any K ∈ ℤ.
    Returns [KMR(0), KMR(1), ..., KMR(K)]"""
    if not isinstance(K, int):
        raise ValueError("K must be integer")
        
    result = [A]
    for _ in range(abs(K)):
        result.append(kmrd(result[-1]) if K >= 0 else kmri(result[-1]))
    return result
```

