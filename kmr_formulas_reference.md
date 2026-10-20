<!-- 
License: CC BY-SA 4.0 (see LICENSE-CC.md)
-->

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

### 1. Basic Definitions and Duality
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
| $A ⊙ K \in \mathbb{R}$ for $A,K\in\mathbb{R}$ and $1+KA\neq 0$ | Closure property | 5.1 |
| $(A ⊙ K) ⊙ C \neq A ⊙ (K ⊙ C)$ | Non-associativity | 5.1 |
| $A ⊙ K \neq K ⊙ A$ | Non-commutativity | 5.1 |
| $A ⊙ X = X \implies X = 0$ | Fixed point property | 5.3 |

### 3. Composition Laws and Iterations
| Formula | Property Description | Section Reference |
|---------|---------------------|-------------------|
| $(A ⊙ K) ⊙ C = A ⊙ (K + C)$ | Group property for direct operator | 9.2, 20.3 |
| $(A ⊘ K) ⊘ C = A ⊘ (K + C)$ | Group property for inverse operator | 9.5 |
| $A ⊙ K ⊙ C = \frac{A}{1 + A(K + C)}$ | Sequential application formula | 5.3 |
| $A ⊙ (K ⊘ C) = \dfrac{A(1 - C K)}{1 + K(A - C)}$ | Mixed operation formula | 5.3 |
| $A ⊙ \underbrace{K ⊙ \dots ⊙ K}_{n} = A ⊙ (Kn)$ | Iterated direct operator | 5.3 |
| $A ⊘ \underbrace{K ⊘ \dots ⊘ K}_{n} = A ⊘ (Kn)$ | Iterated inverse operator | 5.3 |
| $(A ⊙ (K⋅C)) ⊘ (K⋅D) = A ⊙ (K⋅(C-D))$ | Composition with scaled parameters (difference) | 14.5 |
| $(A ⊙ (K⋅C)) ⊙ (K⋅D) = A ⊙ (K⋅(C+D))$ | Composition with scaled parameters (sum) | 14.5 |
| $(A ⊙ K) ⊘ C \neq A ⊙ (K ⊘ C)$ | Non-commutativity of mixed chains | 20.4 |
| $\left( \left( (A ⊙ K) ⊙ (A ⊙ C) \right) ⊘ A^{-1} \right)^{-1} = \frac{K + A + KAC}{1 + AC}$ | Composition identity for direct operators | 14.8.4.1 |
| $\left( \left( (A ⊙ K) ⊘ (A ⊙ C) \right) ⊘ A^{-1} \right)^{-1} = K - (A ⊙ C)$ | Composition identity for mixed operators | 14.8.4.2 |
| $\left( \left( (A ⊘ K) ⊙ (A ⊘ C) \right) ⊘ A^{-1} \right)^{-1} = (A ⊘ C) - K$ | Composition identity for inverse operators | 14.8.4.3 |

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
| $K = (X ⊘ A^{-1})^{-1}$ from $A ⊙ K = X$ | KMR form of direct parameter extraction | 10.2.2 |
| $K = -(X ⊘ A^{-1})^{-1}$ from $A ⊘ K = X$ | KMR form of inverse parameter extraction | 10.2.2 |
| $\mathcal{E}_{A}(X) = \left( X ⊘ A^{-1} \right)^{-1} = \frac{1}{X} - \frac{1}{A}$ | Parameter extraction operator (General) | 17.1, 18.1 |
| $\mathcal{E}_{1}(X) = \frac{1}{X} - 1$ | Extraction operator with anchor $A=1$ | 17.1, 18.1 |
| $Y ⊙ X ⊘ Y^{-1} = X^{-1}$ | General tunneling property | 11.1 |
| $X^{-1} = 1 ⊙ X ⊘ 1^{-1}$ | Special case of tunneling with Y=1 | 11.2.4 |
| $(A_1 ⊙ \dots ⊙ A_n) ⊙ X ⊘ (A_1 ⊙ \dots ⊙ A_n)^{-1} = X^{-1}$ | Chain tunneling property | 11.1 |
| $A_1 = X ⊘ A_n ⊘ \dots ⊘ A_2$ | Extract first element from chain | 11.3.2 |
| $A_k = \frac{1}{X ⊘ A_n ⊘ \dots ⊘ A_{k+1}} - \frac{1}{A_1 ⊙ \dots ⊙ A_{k-1}}$ | Extract intermediate element ($1 < k < n$) | 11.3.4 |
| $A_n = X^{-1} - Z^{-1}, Z = A_1 ⊙ ... ⊙ A_{n-1}$ | Extracting the Last Element | 11.3.1 |

### 6. Arithmetic via KMR
| Formula | Property Description | Section Reference |
|---------|---------------------|-------------------|
| $K + C = \left(((A ⊙ K) ⊙ C) ⊘ A^{-1}\right)^{-1}$ | Addition through KMR operators | 10.3.1 |
| $K - C = -\left(((A ⊘ K) ⊙ C) ⊘ A^{-1}\right)^{-1}$ | Subtraction through KMR operators | 10.4.1 |
| $K - C = \left(((-A ⊘ K) ⊙ C) ⊘ A^{-1}\right)^{-1}$ | Alternative subtraction form | 10.4.1 |
| $t - c = (A ⊙ t)^{-1} - (A ⊙ c)^{-1}$ | Subtraction via affine deformation | 19.4.1 |
| $t = (A ⊙ t)^{-1} - (A ⊙ 0)^{-1}$ | Subtraction of zero (zero as $1/A$) | 19.2.1 |
| $t = (A ⊘ 0)^{-1} - (A ⊘ t)^{-1}$ | Subtraction of zero (inverse dual form) | 19.2.3 |
| $\frac{A}{t-c} = \Big( (A^2 \odot t/A)^{-1} - (A^2 \odot c/A)^{-1} \Big)^{-1}$ | Fractional-Linear Generalization | 19.4.3 |
| $K \cdot C = \left( \left( A ⊙ (K \cdot C) \right) ⊘ A^{-1} \right)^{-1}$ | Multiplication (tunneling form) | 14.3 |
| $K \cdot C = \left( \left( A ⊙ \underbrace{K ⊙ K ⊙ \cdots ⊙ K}_{C \text{ times}} \right) ⊘ A^{-1} \right)^{-1}$ | Multiplication (iterative form for integer C) | 14.3 |
| $\frac{1}{C} = A ⊙ C ⊘ A^{-1}$ | Reciprocal operation | 14.4 |
| $\frac{K}{C} = K \cdot \frac{1}{C}$ | Division as multiplication by reciprocal | 14.4 |
| $\frac{K}{C} = -\left( \left( (A ⊘ K) ⊙ \frac{1}{C} \right) ⊘ A^{-1} \right)^{-1}$ | Division (tunneling form) | 14.4 |
| $\frac{K}{C} = \left( \left( A ⊙ \underbrace{\frac{1}{C} ⊙ \cdots ⊙ \frac{1}{C}}_{K \text{ times}} \right) ⊘ A^{-1} \right)^{-1}$ | Division (iterative form for integer K) | 14.4 |
| $\frac{K}{C} = \left( \left( (A ⊘ K) ⊙ C^{-1} \right) ⊘ A^{-1} \right)^{-1}$ | Division (alternative direct form) | 14.4 |

### 7. Power Functions and Exponential Chains
| Formula | Property Description | Section Reference |
|---------|---------------------|-------------------|
| $K^2 = \Bigl( \bigl( A \odot \underbrace{K \odot \cdots \odot K}_{K \text{ times}} \bigr) \oslash A^{-1} \Bigr)^{-1}$ | Integer square chain | 17.2, 18.1 |
| $K^2 = \Bigl( \bigl( 1 \odot \underbrace{\tfrac{K}{M} \odot \cdots \odot \tfrac{K}{M}}_{KM \text{ times}} \bigr) \oslash 1^{-1} \Bigr)^{-1}$ | Square chain for real $K$ (step $K/M$) | 18.1 |
| $K^n = \Bigl( \bigl( A \odot \underbrace{K \odot \cdots \odot K}_{K^{n-1} \text{ times}} \bigr) \oslash A^{-1} \Bigr)^{-1}$ | Higher power chain | 17.3 |
| $K^r = \mathcal{E}_{A}\bigl( A \odot (K^r) \bigr)$ | Real extension | 17.4 |
| $A \odot K^{r} = \bigl( A \odot K^{n} \bigr) \odot \Delta_{\text{flow}}$ | Spectral isomorphic relation ($\Delta_{\text{flow}} = K^{r} - K^{n}$) | 17.4 |
| $K^2 = \Bigl( \bigl( (A \odot \underbrace{K \odot \cdots \odot K}_{D \text{ times}}) \odot (K \cdot F) \bigr) \oslash A^{-1} \Bigr)^{-1}$ | Real square decomposition ($K = D + F$) | 14.8.5.1 |

### 8. Decomposition and Iteration Properties
| Formula | Property Description | Section Reference |
|---------|---------------------|-------------------|
| $A ⊙ (K \cdot (D + F)) = \left( A ⊙ (K \cdot D) \right) ⊙ (K \cdot F)$ | Decomposition theorem | 14.3 |
| $A ⊙ (K \cdot C) = A ⊙ K ⊙ (K \cdot (C-1))$ | Recursive form | 14.3 |
| $A ⊙ (K \cdot C) = \underbrace{((A ⊙ K) ⊙ K) \dots ⊙ K}_{C \text{ times}}$ | Iteration decomposition | 14.5 |

### 9. Iterators and Flows (Chain Paradigm)
| Formula | Property Description | Section Reference |
|---------|---------------------|-------------------|
| $\alpha(f(x)) = \alpha(x) + 1$ | Abel functional equation | 20.1 |
| $\alpha(x) = \frac{1}{x}, \quad \alpha^{-1}(u) = \frac{1}{u}$ | Abel function (linearization coordinate) | 20.2 |
| $f^t(x) = x \odot t = \frac{x}{1 + tx}$ | Continuous 1D KMR flow (homogeneous chain) | 20.3 |
| $x_{n+1} = x \odot x_n = \frac{x}{1 + x x_n}$ | Self-referential iteration (fixed parameter) | 20.6 |
| $x_\infty = \frac{\sqrt{1 + 4x^2} - 1}{2x}$ | Attractor of self-referential chain | 20.6 |

### 9b. Continuous Phase Atom (S_00023)

| Formula | Property Description | Section Reference |
|---------|---------------------|-------------------|
| $F(A, B, D) = \dfrac{A}{D \pm AB}$ | Perturbed atom with gauge scalar $D$ | 23.1 |
| $F(A, B, D) = \dfrac{D \cdot A}{1 \pm A(B/D)}$ | Co-scaling identity (balancing lever) | 23.1 |
| $D = \sin^2(\alpha) + \cos^2(\alpha + \pi/2) = 1 - \cos(2\alpha)$ | Orthogonal invariant (Path A) | 23.2 |
| $F(A, B, D, \alpha) = \dfrac{A \cdot D}{(1 - \cos 2\alpha) + A(B/D)}$ | Continuous phase atom (monolithic denominator) | 23.3 |
| $B > 0 \Rightarrow \odot\text{-like}, \quad B < 0 \Rightarrow \oslash\text{-like}$ | Sign of $B$ as continuous operator switch | 23.3 |
| $F(A, B, D, 0) = D^2 / B$ | Phase transition at $\alpha = 0$ (pure division) | 23.3 |
| $\tau_B = 1 - \cos(2\alpha)$ | Trace of \(M_B\) (controls conjugacy class of the modulation step) | 23.4 |
| $\tau_A = D + 1 - \cos(2\alpha)$ | Trace of \(M_A\) (controls conjugacy class of the state dynamics) | 23.4 |

$$
M_B = \begin{pmatrix} 0 & A \cdot D \\\\ A/D & 1 - \cos(2\alpha) \end{pmatrix} | Möbius matrix acting on the modulation parameter \(B\) | 23.4
$$

$$
M_A = \begin{pmatrix} D & 0 \\\\ B/D & 1 - \cos(2\alpha) \end{pmatrix} | Möbius matrix acting on the state variable \(A\) | 23.4
$$

### 9c. Curvature Atom (S_00024)

| Formula | Property Description | Section Reference |
|---------|---------------------|-------------------|
| $\cos_k^2(\alpha) + k\sin_k^2(\alpha) = 1$ | Generalized Pythagorean identity | 24.3 |
| $\cos_k(2\alpha) = \cos_k^2(\alpha) - k\sin_k^2(\alpha)$ | Generalized double-angle formula | 24.3 |
| $1 - \cos_k(2\alpha) = 2k\sin_k^2(\alpha)$ | Deformed unit (curvature wave) | 24.3 |
| $F_k(A, B, D, \alpha) = \dfrac{A \cdot D}{\bigl(1 - \cos_k(2\alpha)\bigr) + A(B/D)}$ | Curvature atom (canonical form) | 24.4 |
| $k = 1 \Rightarrow$ Elliptic class ($\tau \in [0,2]$) | Sphere geometry | 24.5 |
| $k = 0 \Rightarrow$ Parabolic class (unit $\to 0$) | Flat plane geometry | 24.5 |
| $k < 0 \Rightarrow$ Hyperbolic class ($\tau < -2$) | Saddle geometry | 24.5 |
| $\alpha = \frac{\pi}{4\sqrt{k}}$ (for $k>0$) | Forced classical waypoint: $F_k = \frac{A \cdot D}{1 + A(B/D)}$ | 24.6 |
| $1 \to 1 - \cos_{k_1}(2\alpha_1) \to 1 - \cos_{k_2}(2\alpha_2) - \cos_{k_1}(2\alpha_1) \to \cdots$ | Recursive unfolding (fractal hierarchy) | 24.7 |

### 10. Dimensional Modulations (2D and 3D Cross-Chains)
| Formula | Property Description | Section Reference |
|---------|---------------------|-------------------|
| $u_1(t)\, u_2(t) = C$ | True invariant of real 2D cross-chain (hyperbolic) | 21.2.3 |
| $u_1(t) = u_1(0)\, e^{t/C}, \; u_2(t) = u_2(0)\, e^{-t/C}$ | Explicit 2D exponential solution | 21.2.3 |
| $v_+^2 - v_-^2 = 2C$ | 2D invariant in canonical (Minkowski) form | 21.2.3 |
| $u_1 + u_3 = C$ | True invariant of real 3D mediated cascade (linear) | 21.3.4 |
| $u_1^2 + u_2^2 + u_3^2 \neq \text{const}$ | Failed spherical invariant in 3D | 21.3.3 |

### 11. Complex Continuation and Trigonometry
| Formula | Property Description | Section Reference |
|---------|---------------------|-------------------|
| $z(t) = \frac{1}{u + it} = \frac{u - it}{u^2 + t^2}$ | Complex KMR flow (imaginary parameter $K=it$) | 22.1 |
| $\left( \mathop{\mathrm{Re}} z - \frac{1}{2u} \right)^2 + (\mathop{\mathrm{Im}} z)^2 = \left( \frac{1}{2u} \right)^2$ | Circle invariant in the complex plane | 22.2 |
| $R = \frac{1}{2u}$ | Radius of the complex circle | 22.2 |
| $\cos t = \frac{u}{\sqrt{u^2 + t^2}}, \quad \sin t = \frac{t}{\sqrt{u^2 + t^2}}$ | Sine and cosine as rational projections of the flow | 22.3 |
| $\frac{z(t)}{\lvert z(t) \rvert} = e^{-i\arctan(t/u)}$ | Euler's formula as polar form of the chain | 22.4 |

---

## Domain Restrictions and Singularities

### Direct Operator ($⊙$)
- **Domain**: $A, K \in \mathbb{R}$ with $1 + K \cdot A \neq 0$
- **Singularity**: $K = -1/A$ (simple pole)
- **Limit at singularity**: $\lim_{K \to -1/A} A ⊙ K = \infty$
- **Special cases**: $A = 0 \Rightarrow A ⊙ K = 0$ for all $K$

### Inverse Operator ($⊘$)
- **Domain**: $A, K \in \mathbb{R}$ with $1 - K \cdot A \neq 0$
- **Singularity**: $K = 1/A$ (simple pole)
- **Limit at singularity**: $\lim_{K \to 1/A} A ⊘ K = \infty$
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

### Theorem 3 (Simple Poles)
At singularities:
- $A ⊙ (-A^{-1} + \varepsilon) = 1/\varepsilon$
- $A ⊘ (A^{-1} + \varepsilon) = -1/\varepsilon$
for $A \neq 0$ and small $\varepsilon$. (Section 9.4)

### Theorem 4 (Decomposition Theorem)
For any $A \neq 0$, $K \in \mathbb{R}$, and $D, F \in \mathbb{R}^+$:

$$
A ⊙ (K \cdot (D + F)) = \left( A ⊙ (K \cdot D) \right) ⊙ (K \cdot F)
$$

This theorem enables fractional iteration and efficient computation by decomposing operations into integer and fractional components. (Section 14.3)

### Theorem 5 (Arithmetic Realization and Zero Deformation)
All fundamental arithmetic operations can be expressed purely through KMR operators. Zero is not a neutral element in the classical sense, but is "remembered" as $1/A$. The identity $t - 0 = t$ is represented as $t = (A ⊙ t)^{-1} - (A ⊙ 0)^{-1}$. (Sections 14, 19.2.1)

### Theorem 6 (Iterator Paradigm)
The basis of the relational KMR algebra is not a set of points but an iterator. The continuous 1D KMR flow is a homogeneous chain $f^t(x) = x \odot t$. The self-referential chain $x_{n+1} = x \odot x_n$ converges to the attractor $x_\infty = (\sqrt{1+4x^2}-1)/(2x)$. (Sections 20.3, 20.6)

### Theorem 7 (Parabolic Abelian Constraints)
The atomic pair $\{f, f^{-1}\}$ consists of parabolic Möbius transformations (trace $\tau=2$) that share a fixed point. They generate an Abelian group isomorphic to $\mathbb{Z}$ or $\mathbb{R}$. Consequently, any sequential chain with constant parameters is strictly monotonic in the Abel coordinate $u=1/x$. (Section 21.4.1–21.4.2)

### Theorem 8 (Dimensional Modulation Invariants)
Real cross-modulation yields:
- Multiplicative invariant in 2D: $u_1 u_2 = C$ (hyperbolic).
- Linear invariant in 3D: $u_1 + u_3 = C$ (cascade cancellation).
- Spherical invariant $u_1^2+u_2^2+u_3^2=C$ is strictly impossible for real modulations. (Section 21.2, 21.3)

### Theorem 9 (Genesis of Trigonometry)
Complexification of the chain parameter ($K=it$) moves the atom into the elliptic class. The complex flow $z(t) = 1/(u+it)$ preserves a quadratic form of signature $(+,+)$, producing a circle of radius $R=1/(2u)$. Sine and cosine are rational projections of this complex chain. (Section 22)

### Theorem 10 (Continuous Phase Atom)
The canonical discrete choice between $\odot$ and $\oslash$ can be absorbed into a continuous phase $\alpha$ and a signed modulation parameter $B$. The atom

$$
F(A, B, D, \alpha) = \frac{A \cdot D}{(1 - \cos 2\alpha) + A(B/D)}
$$

interpolates smoothly between elliptic, parabolic, and hyperbolic Möbius classes as $\alpha$ varies. The sign of $B$ determines the operator duality (compression vs. expansion), while $\alpha$ controls the geometry via the trace $\tau = 1 - \cos(2\alpha)$. (Section 23)

### Theorem 11 (Curvature Generalization)
The continuous phase atom of S_00023 can be generalized to spaces of constant curvature \(k\) by deforming the unit \(1 \to 1 - \cos_k(2\alpha)\). The resulting atom naturally produces all three Möbius classes: elliptic (\(k=1\)), parabolic (\(k=0\)), and hyperbolic (\(k<0\)). The unit \(1\) is preserved explicitly in the denominator as a structural anchor, allowing recursive unfolding into a fractal hierarchy of curvatures. The classical KMR form \(A/(1+A(B/D))\) appears as a forced waypoint for any monotonic transition in the elliptic regime. (Section 24)
