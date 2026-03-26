<!-- 
License: CC BY-SA 4.0 (see LICENSE-CC.md)
-->

# 15. Ergodicity of the Continuous KMR Flow in Compact Spaces
**Author**: Sergei Terikhov  
**Date**: 27.03.2026  

## 15.1 Abstract
This section establishes the formal conditions for ergodicity within a modified KMR framework. While the original discrete KMR mapping on $\mathbb{R}$ is dissipative and parabolic, we demonstrate that the continuous flow derived from the fractional extension (Section 9) becomes ergodic when the state space is configured as a compact manifold with periodic boundaries.

## 15.2 The KMR-L Model: Postulating the Period $L$

### 15.2.1 Extension of the Original Theory
The original KMR algebraic axioms do not inherently imply a periodic structure. To achieve ergodicity, we introduce an additional structure: **The KMR-L Model**. 
We postulate the existence of a **fundamental constant of the environment $L > 0$** (System Capacity), which defines the periodic boundary conditions for the inversion coordinate $u = 1/y$.

### 15.2.2 Compactification via Factorization
Unlike the standard real projective line $\mathbb{RP}^1$ (where the shift $u \mapsto u+K$ remains parabolic and non-ergodic), our model utilizes the factorization of the $u$-axis:
$$\mathcal{M} = \mathbb{R} / L\mathbb{Z} \cong S^1_L$$
This transformation turns the inversion space into a circle of length $L$. This specific choice of compactification is critical: it converts the dissipative Euclidean "leak" at $y=0$ into a conservative periodic rotation.

## 15.3 Invariant Measure and Normalization

### 15.3.1 Transformation of the Volume Form
In the inversion space $u$, the flow is a pure translation $u \mapsto u+K$. The Haar measure $du$ is invariant under this action. Pulling this measure back to the original $y$-space, we obtain the invariant measure:
$$\mu(dy) = \frac{dy}{y^2}$$

### 15.3.2 Normalization on the Compact Manifold
The measure $dy/y^2$ is infinite on the open ray $\mathbb{R}^+$. However, it becomes finite upon the introduced compactification ($u \pmod L$). We define the **normalized invariant measure** $\bar{\mu}$ on the manifold $\mathcal{M}$ as:
$$d\bar{\mu} = \frac{1}{L} du = \frac{1}{L} \frac{dy}{y^2}$$
This ensures that $\int_{\mathcal{M}} d\bar{\mu} = 1$, satisfying the requirements for the application of the Birkhoff Ergodic Theorem.

## 15.4 Ergodicity of the Continuous Flow

### 15.4.1 Dynamics in Fractional Extension
We consider the **continuous KMR flow** $\phi^K: \mathcal{M} \to \mathcal{M}$ defined for $K \in \mathbb{R}$ using the fractional composition formula (Section 9):
$$\phi^K(u) = (u + K) \pmod L$$

### 15.4.2 Proof of Ergodicity
**Theorem**: The continuous KMR flow $\phi^K$ on the compactified manifold $S^1_L$ is ergodic with respect to the normalized measure $d\bar{\mu}$ for any $L > 0$.

*Proof*:
1. **Spectral Property**: A continuous translation flow on a circle $S^1_L$ with constant velocity $v=1$ is strictly ergodic for any $K \in \mathbb{R}$.
2. **Minimality**: For any $L$, the orbit of any point $u_0$ covers the entire manifold $\mathcal{M}$.
3. **Convergence**: By the Birkhoff Ergodic Theorem, for any integrable function $f \in L^1(\bar{\mu})$:
   $$\lim_{T \to \infty} \frac{1}{T} \int_0^T f(\phi^K u) dK = \int_{\mathcal{M}} f \, d\bar{\mu}$$
4. **Distinction from Discrete Case**: For discrete iterations ($K \in \mathbb{Z}$), ergodicity would require the irrationality of $1/L$. In this continuous model ($K \in \mathbb{R}$), ergodicity is an intrinsic property of the flow. $\square$

## 15.5 Physical and Philosophical Interpretation
The "collapse to zero" ($y \to 0$) observed in Euclidean coordinates is an artifact of a non-compact projection. Within the KMR-L model:
1. **Transit Point**: The point $y=0$ (corresponding to $u \to \infty$) is a point of maximal flow velocity, acting as an instantaneous bridge back to the observable state.
2. **Dynamic Equilibrium**: The system state does not "age" in a dissipative sense; it undergoes a steady-state rotation where all phases (injection, circulation, and absorption) are statistically equivalent over time.

**Conclusion**: 
Ergodicity is proven for the **KMR-L continuous flow model**. This transformation of the dissipative KMR dynamics into a conservative ergodic process is enabled by the postulation of the period $L$ and the resulting compactification of the inversion space.
