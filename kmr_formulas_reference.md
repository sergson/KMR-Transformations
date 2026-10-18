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

# KMR Transformations: Properties and Formulas Reference
**Author**: Sergei Terikhov  
**Date**: 2025-2026  

## Introduction
This document provides a comprehensive reference of all properties and formulas derived for KMR (K-modulated Möbius Reduction) operators. It serves as a centralized knowledge base for the algebraic structure of KMR transformations, facilitating both theoretical research and practical implementation.

## Notation
- $A, B, C, K, X, Y, Z$: Real numbers unless otherwise specified
- $⊙$: Direct KMR operator
- $⊘$: Inverse KMR operator
- $f^K$: K-fold composition of function $f$
- $u, v$: Inverse (Abel) coordinates, e.g., $u = 1/A$
- $\mathbb{R}$: Real numbers
- $\mathbb{Z}$: Integers
- $\mathbb{C}$: Complex numbers

---

## Complete Reference Table

### 1. Basic Definitions
| Formula | Property Description | Section Reference |
|---------|---------------------|-------------------|
| $A ⊙ K ≔ \frac{A}{1 + K \cdot A}$ | Direct KMR operator definition | 3.1 |
| $A ⊘ K ≔ \frac{A}{1 - K \cdot A}$ | Inverse KMR operator definition | 3.2 |
| $A ⊙ 1 = \frac{A}{1 + A}$ | Single application of direct operator | 2.1 |
| $A ⊘ 1 = \frac{A}{1 - A}$ | Single application of inverse operator | 2.2 |
| $A ⊙ K = A ⊘ (-K)$ | Duality between operators | 9.2 |
| $A ⊘ K = A ⊙ (-K)$ | Duality (symmetric form) | 9.2 |

### 2. Fundamental Algebraic Properties
| Formula | Property Description | Section Reference |
|---------|---------------------|-------------------|
| $A ⊙ 0 = A$ | Identity element for direct operator | 5.1 |
| $A ⊘ 0 = A$ | Identity element for inverse operator | 5.2 |
| $(A ⊘ K) ⊙ K = A$ | Inversion identity | 5.2 |
| $(A ⊙ K) ⊘ K = A$ | Inversion identity (dual form) | 10.2.2 |
| $\lambda \cdot (A ⊙ K) = (\lambda A) ⊙ (K/\lambda)$ | Scaling property for direct operator | 10.2.2 |
| $\lambda \cdot (A ⊘ K) = (\lambda A) ⊘ (K/\lambda)$ | Scaling property for inverse operator | 10.2.2 |

### 3. Composition Laws
| Formula | Property Description | Section Reference |
|---------|---------------------|-------------------|
| $(A ⊙ K) ⊙ C = A ⊙ (K + C)$ | Group property for direct operator (Homogeneous collapse) | 9.2, 20.3 |
| $(A ⊘ K) ⊘ C = A ⊘ (K + C)$ | Group property for inverse operator | 9.5 |
| $A ⊙ K ⊙ C = \frac{A}{1 + A(K + C)}$ | Sequential application formula | 5.3 |
| $A ⊙ (K ⊘ C) = \dfrac{A(1 - C K)}{1 + K(A - C)}$ | Mixed operation formula | 5.3 |
| $(A ⊙ K) ⊘ C \neq A ⊙ (K ⊘ C)$ | Non-commutativity of mixed chains | 20.4 |
| $A ⊙ \underbrace{K ⊙ \dots ⊙ K}_{n} = A ⊙ (Kn)$ | Iterated direct operator | 5.3 |

### 4. Differential and Integral Properties
| Formula | Property Description | Section Reference |
|---------|---------------------|-------------------|
| $\frac{\partial}{\partial K}(A ⊙ K) = -(A ⊙ K)^2$ | Flow equation for direct operator | 9.3, 13.2 |
| $\frac{\partial}{\partial K}(A ⊘ K) = (A ⊘ K)^2$ | Flow equation for inverse operator | 9.3, 13.2 |
| $A ⊙ (-A^{-1} + \varepsilon) = \frac{1}{\varepsilon}$ | Laurent expansion at direct singularity | 9.4 |
| $A ⊘ (A^{-1} + \varepsilon) = -\frac{1}{\varepsilon}$ | Laurent expansion at inverse singularity | 9.4 |
| $y'' = 2y^3$ | Differential equation solved by $y = A ⊘ K$ | 13.6.2 |

### 5. Parameter Extraction (Tunneling)
| Formula | Property Description | Section Reference |
|---------|---------------------|-------------------|
| $K = \frac{1}{X} - \frac{1}{A}$ from $A ⊙ K = X$ | Parameter extraction for direct operator | 10.2.2 |
| $K = \frac{1}{A} - \frac{1}{X}$ from $A ⊘ K = X$ | Parameter extraction for inverse operator | 10.2.2 |
| $\mathcal{E}_{A}(X) = \left( X ⊘ A^{-1} \right)^{-1} = \frac{1}{X} - \frac{1}{A}$ | Parameter extraction operator (General) | 17.1, 18.1 |
| $\mathcal{E}_{1}(X) = \frac{1}{X} - 1$ | Extraction operator with anchor $A=1$ | 17.1, 18.1 |
| $Y ⊙ X ⊘ Y^{-1} = X^{-1}$ | General tunneling property | 11.1 |
| $A_1 = X ⊘ A_n ⊘ \dots ⊘ A_2$ | Extract first element from chain | 11.3.2 |
| $A_n = X^{-1} - Z^{-1}, Z = A_1 ⊙ ... ⊙ A_{n-1}$ | Extracting the Last Element | 11.3.1 |

### 6. Arithmetic via KMR
| Formula | Property Description | Section Reference |
|---------|---------------------|-------------------|
| $K + C = \left(((A ⊙ K) ⊙ C) ⊘ A^{-1}\right)^{-1}$ | Addition through KMR operators | 10.3.1 |
| $t - c = (A ⊙ t)^{-1} - (A ⊙ c)^{-1}$ | Subtraction via affine deformation | 19.4.1 |
| $t = (A ⊙ t)^{-1} - (A ⊙ 0)^{-1}$ | Subtraction of zero (zero as $1/A$) | 19.2.1 |
| $t = (A ⊘ 0)^{-1} - (A ⊘ t)^{-1}$ | Subtraction of zero (inverse dual form) | 19.2.3 |
| $\frac{A}{t-c} = \Big( (A^2 \odot t/A)^{-1} - (A^2 \odot c/A)^{-1} \Big)^{-1}$ | Fractional-Linear Generalization | 19.4.3 |
| $K \cdot C = \left( \left( A ⊙ \underbrace{K ⊙ \cdots ⊙ K}_{C \text{ times}} \right) ⊘ A^{-1} \right)^{-1}$ | Multiplication (iterative form) | 14.3 |
| $\frac{1}{C} = A ⊙ C ⊘ A^{-1}$ | Reciprocal operation | 14.4 |

### 7. Power Functions and Exponential Chains
| Formula | Property Description | Section Reference |
|---------|---------------------|-------------------|
| $K^2 = \Bigl( \bigl( 1 \odot \underbrace{K \odot \cdots \odot K}_{K \text{ times}} \bigr) \oslash 1^{-1} \Bigr)^{-1}$ | Integer square chain (canonical) | 17.2, 18.1 |
| $K^2 = \Bigl( \bigl( 1 \odot \underbrace{\tfrac{K}{M} \odot \cdots \odot \tfrac{K}{M}}_{KM \text{ times}} \bigr) \oslash 1^{-1} \Bigr)^{-1}$ | Square chain for real $K$ (step $K/M$) | 18.1 |
| $K^n = \Bigl( \bigl( A \odot \underbrace{K \odot \cdots \odot K}_{K^{n-1} \text{ times}} \bigr) \oslash A^{-1} \Bigr)^{-1}$ | Higher power chain | 17.3 |

### 8. Iterators and Flows (Chain Paradigm)
| Formula | Property Description | Section Reference |
|---------|---------------------|-------------------|
| $\alpha(f(x)) = \alpha(x) + 1$ | Abel functional equation | 20.1 |
| $\alpha(x) = \frac{1}{x}, \quad \alpha^{-1}(u) = \frac{1}{u}$ | Abel function (linearization coordinate) | 20.2 |
| $f^t(x) = x \odot t = \frac{x}{1 + tx}$ | Continuous 1D KMR flow (homogeneous chain) | 20.3 |
| $x_{n+1} = x \odot x_n = \frac{x}{1 + x x_n}$ | Self-referential iteration (fixed parameter) | 20.6 |
| $x_\infty = \frac{\sqrt{1 + 4x^2} - 1}{2x}$ | Attractor of self-referential chain | 20.6 |

### 9. Dimensional Modulations (2D and 3D Cross-Chains)
| Formula | Property Description | Section Reference |
|---------|---------------------|-------------------|
| $u_1(t)\, u_2(t) = C$ | True invariant of real 2D cross-chain (hyperbolic) | 21.2.3 |
| $u_1(t) = u_1(0)\, e^{t/C}, \; u_2(t) = u_2(0)\, e^{-t/C}$ | Explicit 2D exponential solution | 21.2.3 |
| $v_+^2 - v_-^2 = 2C$ | 2D invariant in canonical (Minkowski) form | 21.2.3 |
| $u_1 + u_3 = C$ | True invariant of real 3D mediated cascade (linear) | 21.3.4 |
| $u_1^2 + u_2^2 + u_3^2 \neq \text{const}$ | Failed spherical invariant in 3D | 21.3.3 |

### 10. Complex Continuation and Trigonometry
| Formula | Property Description | Section Reference |
|---------|---------------------|-------------------|
| $z(t) = \frac{1}{u + it} = \frac{u - it}{u^2 + t^2}$ | Complex KMR flow (imaginary parameter $K=it$) | 22.1 |
| $\left( \mathop{\mathrm{Re}} z - \frac{1}{2u} \right)^2 + (\mathop{\mathrm{Im}} z)^2 = \left( \frac{1}{2u} \right)^2$ | Circle invariant in the complex plane | 22.2 |
| $R = \frac{1}{2u}$ | Radius of the complex circle | 22.2 |
| $\cos t = \frac{u}{\sqrt{u^2 + t^2}}, \quad \sin t = \frac{t}{\sqrt{u^2 + t^2}}$ | Sine and cosine as rational projections of the flow | 22.3 |
| $\frac{z(t)}{|z(t)|} = e^{-i\arctan(t/u)}$ | Euler's formula as polar form of the chain | 22.4 |

---

## Domain Restrictions and Singularities

### Direct Operator ($⊙$)
- **Domain**: $A, K \in \mathbb{R}$ with $1 + K \cdot A \neq 0$
- **Singularity**: $K = -1/A$ (simple pole)
- **Special cases**: $A = 0 \Rightarrow A ⊙ K = 0$ for all $K$

### Inverse Operator ($⊘$)
- **Domain**: $A, K \in \mathbb{R}$ with $1 - K \cdot A \neq 0$
- **Singularity**: $K = 1/A$ (simple pole)
- **Special cases**: $A = 0 \Rightarrow A ⊘ K = 0$ for all $K$

---

## Important Theorems

### Theorem 1 (Canonical Extension)
The expressions $A ⊙ K = A/(1 + K·A)$ and $A ⊘ K = A/(1 - K·A)$ provide unique continuous extensions from integer $K$ to real $K$ satisfying consistency, duality, and group properties. (Section 9.2)

### Theorem 2 (Dual Generators)
The fractional compositions satisfy the differential equations:
- $\frac{\partial}{\partial K}(A ⊙ K) = -(A ⊙ K)^2$, $A ⊙ 0 = A$
- $\frac{\partial}{\partial K}(A ⊘ K) = (A ⊘ K)^2$, $A ⊘ 0 = A$
with locally unique solutions. (Section 9.3)

### Theorem 3 (Arithmetic Realization and Zero Deformation)
All fundamental arithmetic operations can be expressed through KMR operators. Zero is not a neutral element in the classical sense, but is "remembered" as $1/A$. The identity $t - 0 = t$ is represented as $t = (A ⊙ t)^{-1} - (A ⊙ 0)^{-1}$. (Sections 14, 19.2.1)

### Theorem 4 (Iterator Paradigm)
The basis of the relational KMR algebra is not a set of points but an iterator. The continuous 1D KMR flow is a homogeneous chain $f^t(x) = x \odot t$. The self-referential chain $x_{n+1} = x \odot x_n$ converges to the attractor $x_\infty = (\sqrt{1+4x^2}-1)/(2x)$. (Sections 20.3, 20.6)

### Theorem 5 (Parabolic Abelian Constraints)
The atomic pair $\{f, f^{-1}\}$ consists of parabolic Möbius transformations (trace $\tau=2$) that share a fixed point. They generate an Abelian group isomorphic to $\mathbb{Z}$ or $\mathbb{R}$. Consequently, any sequential chain with constant parameters is strictly monotonic in the Abel coordinate $u=1/x$. (Section 21.4.1–21.4.2)

### Theorem 6 (Dimensional Modulation Invariants)
Real cross-modulation yields:
- Multiplicative invariant in 2D: $u_1 u_2 = C$ (hyperbolic).
- Linear invariant in 3D: $u_1 + u_3 = C$ (cascade cancellation).
- Spherical invariant $u_1^2+u_2^2+u_3^2=C$ is strictly impossible for real modulations. (Section 21.2, 21.3)

### Theorem 7 (Genesis of Trigonometry)
Complexification of the chain parameter ($K=it$) moves the atom into the elliptic class. The complex flow $z(t) = 1/(u+it)$ preserves a quadratic form of signature $(+,+)$, producing a circle of radius $R=1/(2u)$. Sine and cosine are rational projections of this complex chain. (Section 22)