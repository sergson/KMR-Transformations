<!-- 
License: CC BY-SA 4.0 (see LICENSE-CC.md)
-->

# KMR Transformations: Properties and Formulas Reference
**Author**: Sergei Terikhov  
**Date**: 08.12.2025  

## Introduction
This document provides a comprehensive reference of all properties and formulas derived for KMR (K-modulated Möbius Reduction) operators. It serves as a centralized knowledge base for the algebraic structure of KMR transformations, facilitating both theoretical research and practical implementation.

## Notation
- $A, B, C, K, X, Y, Z$: Real numbers unless otherwise specified
- $⊙$: Direct KMR operator
- $⊘$: Inverse KMR operator
- $f^K$: K-fold composition of function $f$
- $\mathbb{R}$: Real numbers
- $\mathbb{Z}$: Integers
- $\mathbb{C}$: Complex numbers

## Complete Reference Table

| Formula | Property Description | Section Reference |
|---------|---------------------|-------------------|
| **1. Basic Definitions** | | |
| $A ⊙ K ≔ \frac{A}{1 + K \cdot A}$ | Direct KMR operator definition | 3.1 |
| $A ⊘ K ≔ \frac{A}{1 - K \cdot A}$ | Inverse KMR operator definition | 3.2 |
| $A ⊙ 1 = \frac{A}{1 + A}$ | Single application of direct operator | 2.1 |
| $A ⊘ 1 = \frac{A}{1 - A}$ | Single application of inverse operator | 2.2 |
| **2. Fundamental Algebraic Properties** | | |
| $A ⊙ 0 = A$ | Identity element for direct operator | 5.1 |
| $A ⊘ 0 = A$ | Identity element for inverse operator | 5.2 |
| $(A ⊘ K) ⊙ K = A$ | Inversion identity | 5.2 |
| $(A ⊙ K) ⊘ K = A$ | Inversion identity (dual form) | 10.2.2 |
| $A ⊙ K = A ⊘ (-K)$ | Duality between operators | 9.2 |
| $A ⊘ K = A ⊙ (-K)$ | Duality (symmetric form) | 9.2 |
| **3. Composition Laws** | | |
| $(A ⊙ K) ⊙ C = A ⊙ (K + C)$ | Group property for direct operator | 9.2 |
| $(A ⊘ K) ⊘ C = A ⊘ (K + C)$ | Group property for inverse operator | 9.5 |
| $A ⊙ K ⊙ C = \frac{A}{1 + AK + AC + AKC}$ | Sequential application formula | 5.3 |
| $A ⊙ (K ⊘ C) = \frac{A(1 - KC)}{1 + AK - AKC}$ | Mixed operation formula | 5.3 |
| $A ⊙ \underbrace{K ⊙ \dots ⊙ K}_{n} = A ⊙ (Kn)$ | Iterated direct operator | 5.3 |
| $A ⊘ \underbrace{K ⊘ \dots ⊘ K}_{n} = A ⊘ (Kn)$ | Iterated inverse operator | 5.3 |
| $(A ⊙ (K⋅C)) ⊘ (K⋅D) = A ⊙ (K⋅(C-D))$ | Composition with scaled parameters (difference) | 14.5 |
| $(A ⊙ (K⋅C)) ⊙ (K⋅D) = A ⊙ (K⋅(C+D))$ | Composition with scaled parameters (sum) | 14.5 |
| **4. Differential Properties** | | |
| $\frac{\partial}{\partial K}(A ⊙ K) = -(A ⊙ K)^2$ | Flow equation for direct operator | 9.3 |
| $\frac{\partial}{\partial K}(A ⊘ K) = (A ⊘ K)^2$ | Flow equation for inverse operator | 9.3 |
| $A ⊙ (-A^{-1} + \varepsilon) = \frac{1}{\varepsilon}$ | Laurent expansion at direct singularity | 9.4 |
| $A ⊘ (A^{-1} + \varepsilon) = -\frac{1}{\varepsilon}$ | Laurent expansion at inverse singularity | 9.4 |
| **5. Scaling and Symmetry** | | |
| $\lambda \cdot (A ⊙ K) = (\lambda A) ⊙ (K/\lambda)$ | Scaling property for direct operator | 10.2.2 |
| $\lambda \cdot (A ⊘ K) = (\lambda A) ⊘ (K/\lambda)$ | Scaling property for inverse operator | 10.2.2 |
| **6. Parameter Extraction** | | |
| $K = \frac{1}{X} - \frac{1}{A}$ from $A ⊙ K = X$ | Parameter extraction for direct operator | 10.2.2 |
| $K = \frac{1}{A} - \frac{1}{X}$ from $A ⊘ K = X$ | Parameter extraction for inverse operator | 10.2.2 |
| $K = (X ⊘ A^{-1})^{-1}$ from $A ⊙ K = X$ | KMR form of direct parameter extraction | 10.2.2 |
| $K = -(X ⊘ A^{-1})^{-1}$ from $A ⊘ K = X$ | KMR form of inverse parameter extraction | 10.2.2 |
| **7. Arithmetic via KMR** | | |
| $K + C = \left(((A ⊙ K) ⊙ C) ⊘ A^{-1}\right)^{-1}$ | Addition through KMR operators | 10.3.1 |
| $K - C = -\left(((A ⊘ K) ⊙ C) ⊘ A^{-1}\right)^{-1}$ | Subtraction through KMR operators | 10.4.1 |
| $K - C = \left(((-A ⊘ K) ⊙ C) ⊘ A^{-1}\right)^{-1}$ | Alternative subtraction form | 10.4.1 |
| $K \cdot C = \left( \left( A ⊙ (K \cdot C) \right) ⊘ A^{-1} \right)^{-1}$ | Multiplication (tunneling form) | 14.3 |
| $K \cdot C = \left( \left( A ⊙ \underbrace{K ⊙ K ⊙ \cdots ⊙ K}_{C \text{ times}} \right) ⊘ A^{-1} \right)^{-1}$ | Multiplication (iterative form for integer C) | 14.3 |
| $\frac{1}{C} = A ⊙ C ⊘ A^{-1}$ | Reciprocal operation | 14.4 |
| $\frac{K}{C} = K \cdot \frac{1}{C}$ | Division as multiplication by reciprocal | 14.4 |
| $\frac{K}{C} = -\left( \left( (A ⊘ K) ⊙ \frac{1}{C} \right) ⊘ A^{-1} \right)^{-1}$ | Division (tunneling form) | 14.4 |
| $\frac{K}{C} = \left( \left( A ⊙ \underbrace{\frac{1}{C} ⊙ \cdots ⊙ \frac{1}{C}}_{K \text{ times}} \right) ⊘ A^{-1} \right)^{-1}$ | Division (iterative form for integer K) | 14.4 |
| $\frac{K}{C} = \left( \left( (A ⊘ K) ⊙ C^{-1} \right) ⊘ A^{-1} \right)^{-1}$ | Division (alternative direct form) | 14.4 |
| **8. Decomposition and Iteration Properties** | | |
| $A ⊙ (K \cdot (D + F)) = \left( A ⊙ (K \cdot D) \right) ⊙ (K \cdot F)$ | Decomposition theorem | 14.3 |
| $A ⊙ (K \cdot C) = A ⊙ K ⊙ (K \cdot (C-1))$ | Recursive form | 14.3 |
| $A ⊙ (K \cdot C) = \underbrace{((A ⊙ K) ⊙ K) \dots ⊙ K}_{C \text{ times}}$ | Iteration decomposition | 14.5 |
| **9. Tunneling Properties** | | |
| $Y ⊙ X ⊘ Y^{-1} = X^{-1}$ | General tunneling property | 11.1 |
| $(A_1 ⊙ \dots ⊙ A_n) ⊙ X ⊘ (A_1 ⊙ \dots ⊙ A_n)^{-1} = X^{-1}$ | Chain tunneling property | 11.1 |
| **10. Element Extraction from Chains** | | |
| $A_1 = X ⊘ A_n ⊘ \dots ⊘ A_2$ | Extract first element from chain | 11.3.2 |
| $A_k = \frac{1}{X ⊘ A_n ⊘ A_{n-1} ⊘ \dots ⊘ A_{k+1}} - \frac{1}{A_1 ⊙ A_2 ⊙ \dots ⊙ A_{k-1}} $ | Extract intermediate element ($1 < k < n$) | 11.3.4 |
| $A_n = X^{-1} - Z^{-1}, Z = A_1 ⊙ ... ⊙ A_{n-1}$ | Extracting the Last Element| 11.3.1 |
| **11. Derived Identities from Composition** | | |
| $\left( \left( (A ⊙ K) ⊙ (A ⊙ C) \right) ⊘ A^{-1} \right)^{-1} = K + C + KAC$ | Composition identity for direct operators | 14.8.4.1 |
| $\left( \left( (A ⊙ K) ⊘ (A ⊙ C) \right) ⊘ A^{-1} \right)^{-1} = K - (A ⊙ C)$ | Composition identity for mixed operators | 14.8.4.2 |
| $\left( \left( (A ⊘ K) ⊙ (A ⊘ C) \right) ⊘ A^{-1} \right)^{-1} = (A ⊘ C) - K$ | Composition identity for inverse operators | 14.8.4.3 |
| **12. Special Cases and Limits** | | |
| $\lim_{K \to -1/A} A ⊙ K = \infty$ | Singularity of direct operator | 5.2 |
| $\lim_{K \to 1/A} A ⊘ K = \infty$ | Singularity of inverse operator | 5.2 |
| $A ⊙ X = X \implies X = 0$ | Fixed point property | 5.3 |
| **13. Computational Properties** | | |
| $A ⊙ K \in \mathbb{R}$ for $A, K \in \mathbb{R} \setminus \{-1/K\}$ | Closure property | 5.1 |
| $(A ⊙ K) ⊙ C \neq A ⊙ (K ⊙ C)$ | Non-associativity | 5.1 |
| $A ⊙ K \neq K ⊙ A$ | Non-commutativity | 5.1 |

## Domain Restrictions and Singularities

### Direct Operator ($⊙$)
- **Domain**: $A, K \in \mathbb{R}$ with $1 + K \cdot A \neq 0$
- **Singularity**: $K = -1/A$ (simple pole)
- **Special cases**: $A = 0 \Rightarrow A ⊙ K = 0$ for all $K$

### Inverse Operator ($⊘$)
- **Domain**: $A, K \in \mathbb{R}$ with $1 - K \cdot A \neq 0$
- **Singularity**: $K = 1/A$ (simple pole)
- **Special cases**: $A = 0 \Rightarrow A ⊘ K = 0$ for all $K$

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
\[
A ⊙ (K \cdot (D + F)) = \left( A ⊙ (K \cdot D) \right) ⊙ (K \cdot F)
\]
This theorem enables fractional iteration and efficient computation by decomposing operations into integer and fractional components. (Section 14.3)

### Theorem 5 (Arithmetic Realization through KMR)
All fundamental arithmetic operations (addition, subtraction, multiplication, division) can be expressed purely through KMR operators $⊙$ and $⊘$ using an auxiliary parameter $A \neq 0$, demonstrating that linear arithmetic emerges from nonlinear KMR transformations. (Section 14)
