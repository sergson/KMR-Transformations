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

# KMR Transformations: Extension to Fractional Compositions  
**Author**: Sergei Terikhov  
**Date**: 16.07.2025  

## 9. Fractional Composition Extension  

### 9.1 Problem Statement  
The discrete KMR operators are [defined for integer compositions](./kmr_paper.md):  
$$A ⊙ K = \frac{A}{1 + K \cdot A}, \quad K \in \mathbb{Z}$$  
$$A ⊘ K = \frac{A}{1 - K \cdot A}, \quad K \in \mathbb{Z}$$  
We seek a mathematically consistent extension to fractional $K \in \mathbb{R}$ that:  
1. Preserves the algebraic structure  
2. Satisfies continuity conditions  
3. Maintains duality between direct and inverse operators  
4. Explicitly handles singularities at $K = -1/A$ (⊙) and $K = 1/A$ (⊘)

### 9.2 Analytic Continuation Approach  

**Theorem 1** (Canonical Extension).  
For $A \in \mathbb{R}$, the closed-form expressions  
$$A ⊙ K \coloneqq \frac{A}{1 + K \cdot A}, \quad 
A ⊘ K \coloneqq \frac{A}{1 - K \cdot A}$$  
provide unique analytic continuations to $K \in \mathbb{R}$ that satisfy:  
1. **Consistency**:  

$⊙\big|_{\mathbb{Z}} = ⊙$  

and  

$⊘\big|_{\mathbb{Z}} = ⊘$  

2. **Duality**: $A ⊙ K = A ⊘ (-K)$  
3. **Group Property**: $(A ⊙ K) ⊙ C = A ⊙ (K + C)$  

*Proof*.  
1. **Consistency for integers**:  
   For $K = n \in \mathbb{Z}_+$: $A ⊙ n = A/(1 + nA)$
   
   For $K = -n \in \mathbb{Z}_-$: $A ⊙ (-n) = \frac{A}{1 - n \cdot A} = A ⊘ n$
   
3. **Duality**:  
   $$A ⊘ (-K) = \frac{A}{1 - (-K)A} = \frac{A}{1 + KA} = A ⊙ K$$  
4. **Group Property**:  
   $$(A ⊙ K) ⊙ C = \frac{\frac{A}{1+KA}}{1 + C \cdot \frac{A}{1+KA}} = \frac{A}{1 + KA + CA} = A ⊙ (K+C)$$  
5. **Uniqueness**: By the identity theorem for meromorphic functions, since $A/(1+KA)$ is meromorphic in $\mathbb{C}$ with simple pole at $K=-1/A$, and agrees with the discrete operator on $\mathbb{Z}$ (which has accumulation points), it is the unique analytic continuation. ∎  

### 9.3 Flow Equation Derivation  

**Motivation for the Differential Equation Approach**  
To extend the discrete KMR operator 
$A ⊙ K = A/(1 + K·A)$
from integer $K$ to continuous $K ∈ ℝ$, we seek a natural continuous flow that interpolates between discrete iterations. Differential equations arise naturally as infinitesimal generators of such flows: if we view $K$ as a continuous "time" parameter, then the rate of change $\frac{∂}{∂K}(A ⊙ K)$ should be determined by the local behavior of the operator. This leads to a differential equation whose unique solution coincides with the explicit fractional formula, thereby providing a consistent analytic continuation.

**Theorem 2** (Dual Generators).  
For $A \neq 0$, the fractional compositions satisfy dual differential equations:  
1. **Direct operator**:  
   $$\frac{\partial}{\partial K}(A ⊙ K) = - (A ⊙ K)^2, \quad A ⊙ 0 = A$$  
2. **Inverse operator**:  
   $$\frac{\partial}{\partial K}(A ⊘ K) = (A ⊘ K)^2, \quad A ⊘ 0 = A$$  
Solutions are locally unique in neighborhoods where $A ⊙ K \neq 0$ and $A ⊘ K \neq 0$.

*Proof*.  

1. **Direct operator**:  
   Direct differentiation yields:
   $$\frac{d}{dK}\left(\frac{A}{1 + AK}\right) = \frac{-A^2}{(1 + AK)^2} = -(A ⊙ K)^2$$

2. **Inverse operator**:  
   Similarly:
   $$\frac{d}{dK}\left(\frac{A}{1 - AK}\right) = \frac{A^2}{(1 - AK)^2} = (A ⊘ K)^2$$

3. **Local uniqueness**:  

   For the direct operator, consider the initial value problem (IVP):

$$
\begin{cases}
\dfrac{dy}{dK} = -y^2, \\
y(0) = A \neq 0.
\end{cases}
$$

   Define $f(y) = -y^2$. The function $f$ is continuously differentiable (hence locally Lipschitz) on any open interval not containing $0$. Since $A \neq 0$, there exists a neighborhood of $A$ where $f$ is Lipschitz. By the Picard–Lindelöf theorem, the IVP has a unique local solution. The explicit formula $y(K) = A/(1 + AK)$ satisfies the ODE and the initial condition, and therefore it is the unique solution where $1 + AK \neq 0$.

   For the inverse operator, the corresponding IVP is:
   
$$
\begin{cases}
\dfrac{dy}{dK} = y^2, \\
y(0) = A \neq 0.
\end{cases}
$$

   Here $f(y) = y^2$ is likewise locally Lipschitz away from $0$. The unique local solution is $y(K) = A/(1 - AK)$, valid where $1 - AK \neq 0$.

   In both cases, the explicit fractional KMR formulas provide the unique solutions guaranteed by the Picard–Lindelöf theorem. ∎

*Explanation of the Picard–Lindelöf theorem application*:
- The theorem ensures existence and uniqueness of solutions to  
$y' = f(y)$ with $y(0)=y_0$  
when $f$ is Lipschitz continuous in a neighborhood of $y_0$.  
- For $f(y) = \pm y^2$, the derivative $f'(y) = \pm 2y$ is bounded on any bounded interval, which implies Lipschitz continuity on that interval.  
- Since $A \neq 0$, we can choose a neighborhood of $A$ that does not include $0$, guaranteeing that $f$ is Lipschitz there.  
- The solutions extend uniquely until they approach a singularity (where the denominator vanishes), which corresponds exactly to the conditions $1 + AK = 0$ for $⊙$ and $1 - AK = 0$ for $⊘$. 

### 9.4 Laurent Series at Singularities  

**Theorem 3** (Simple Poles).  
1. **Direct operator**: At $K_0 = -1/A$ ($A \neq 0$)  
   $$A ⊙ (-A^{-1} + \varepsilon) = \frac{1}{\varepsilon}$$  
2. **Inverse operator**: At $K_0 = 1/A$ ($A \neq 0$)  
   $$A ⊘ (A^{-1} + \varepsilon) = -\frac{1}{\varepsilon}$$  

*Proof*.  
1. **Direct operator singularity**:  
   
   $$A ⊙ (-A^{-1} + \varepsilon) = \frac{A}{1 + A(-A^{-1} + \varepsilon)} = \frac{A}{A\varepsilon} = \frac{1}{\varepsilon}$$
     
3. **Inverse operator singularity**:  
   
   $$A ⊘ (A^{-1} + \varepsilon) = \frac{A}{1 - A(A^{-1} + \varepsilon)} = \frac{A}{-A\varepsilon} = -\frac{1}{\varepsilon} \quad \square$$  
   
### 9.5 Composition Algebra  

**Corollary 1** (Fractional Rules). For $K, C \in \mathbb{R}$:  
1. **Additivity**:  
   $$(A ⊙ K) ⊙ C = A ⊙ (K + C)$$  
   $$(A ⊘ K) ⊘ C = A ⊘ (K + C)$$  
2. **Inversion Duality**:  
   $$(A ⊙ K) ⊘ K = A = (A ⊘ K) ⊙ K$$  
3. **Scaling Symmetry**:  
   $$\lambda \cdot (A ⊙ K) = (\lambda A) ⊙ (K/\lambda)$$  
   $$\lambda \cdot (A ⊘ K) = (\lambda A) ⊘ (K/\lambda)$$  

*Proof*.  
2. **Inversion Duality**:  
   $$(A ⊙ K) ⊘ K = \frac{\frac{A}{1+KA}}{1 - K \cdot \frac{A}{1+KA}} = \frac{A}{1+KA - KA} = A$$  
   Similarly: $(A ⊘ K) ⊙ K = A$.  
3. **Scaling**:  
   $$\lambda \cdot \left( \frac{A}{1 + KA} \right) = \frac{\lambda A}{1 + K A} = \frac{\lambda A}{1 + \frac{K}{\lambda} \cdot (\lambda A)} = (\lambda A) ⊙ (K/\lambda) \quad \square$$  

### 9.6 Computational Framework  

| Operation | Formula | Domain |  
|-----------|---------|--------|  
| $A ⊙ K$ | $\frac{A}{1 + K\cdot A}$ | $A \neq 0$ and $K \neq -1/A$ |  
| $A ⊘ K$ | $\frac{A}{1 - K\cdot A}$ | $A \neq 0$ and $K \neq 1/A$ |  
| $A ⊙ K ⊙ C$ | $A ⊙ (K + C)$ | Valid where compositions defined |  
| $(A ⊙ K) ⊘ K$ | $A$ | Fundamental inversion |  

**Note**: At pole locations ($K = -1/A$ for ⊙ and $K = 1/A$ for ⊘), the functions are undefined. Computational implementations should return NaN to explicitly indicate the singularity.

### 9.7 Implementation  
```python
def kmr_direct(A: float, K: float) -> float:
    """A ⊙ K = A/(1 + K·A) with singularity handling"""
    if A == 0:
        return 0.0
    denom = 1.0 + K * A
    if abs(denom) < 1e-15:
        # Undefined at pole - return NaN
        return float('nan')
    return A / denom

def kmr_inverse(A: float, K: float) -> float:
    """A ⊘ K = A/(1 - K·A) with singularity handling"""
    if A == 0:
        return 0.0
    denom = 1.0 - K * A
    if abs(denom) < 1e-15:
        # Undefined at pole - return NaN
        return float('nan')
    return A / denom
