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

# 21. KMR Modulations: Cross-Chain Dynamics in 2D and 3D
**Author**: Sergei Terikhov  
**Date**: 18.10.2026

## Abstract

We explore two **cross-modulated** extensions of the KMR chain algebra of S_00020: a real 2D cross-chain and a real 3D mediated cascade. The design principle of each is stated explicitly: signs are chosen so that a **linear relation in inverse coordinates** closes the chain. In 2D the relation is multiplicative ($u_1u_2=C$), in 3D additive ($u_1+u_3=C$). We record the failed attempt at a spherical invariant in 3D and explain why it failed. **No practical application is claimed.** The paper is an algebraic exploration of what cross-modulation can and cannot do; the hypothesis on ensemble–time-series symmetry is stated and left open.

---

## 21.1. Design Principle

Two questions governed the construction of the systems below.

**Why 2D, and why these signs?** The 2D system is the **minimal symmetric cross-chain**: two variables, each serving as the parameter for the other. The signs are chosen so that the product $u_1u_2$ is conserved — the first equation uses $\odot$, the second uses $\oslash$, precisely so that $u_2\dot u_1+u_1\dot u_2=0$. This choice is **not motivated by trigonometry**: as §21.2.3 proves, real 2D modulation cannot produce circular rotation; the associated quadratic form has signature $(+,-)$, not $(+,+)$.

**Why 3D, and why these signs?** The 3D system is the **minimal mediated chain**: two end variables $u_1,u_3$ coupled through a mediator $u_2$, with no direct coupling between the ends. The original motivation was a Kolmogorov–Arnold-style hope of reducing $n$-D flows to a single 1D KMR function, which suggested a spherical invariant $u_1^2+u_2^2+u_3^2=C$. That hope failed (§21.3.3). The correct design principle, discovered after the failure, is: choose signs so that the end variables cancel — $u_1\odot\kappa$ and $u_3\oslash\kappa$ with the same $\kappa=1/u_2$ — yielding the linear invariant $u_1+u_3=C$.

**General statement.** In both cases the design principle is the same: **choose signs so that a linear relation in inverse coordinates closes the chain.** In 2D the relation is multiplicative; in 3D it is additive. Neither is spherical, and neither yields rotation without complexification (see S_00022).

---

## 21.2. Real 2D Cross-Chain

### 21.2.1. Discrete System

Consider the discrete system with cross-modulation:

$$
x_1(n+1) = \frac{x_1(n)}{1 + x_1(n) x_2(n)}, \qquad
x_2(n+1) = \frac{x_2(n)}{1 - x_1(n) x_2(n)}.
$$

In inverse coordinates $u_i = 1/x_i$:

$$
u_1(n+1) = u_1(n) + \frac{1}{u_2(n)}, \qquad
u_2(n+1) = u_2(n) - \frac{1}{u_1(n)}.
$$

### 21.2.2. Chain Representation

The 2D system is naturally read as a **pair of chains of length 1**, in which the parameter of each chain is the current value of the other coordinate:

$$
x_1(n+1) = x_1(n) \odot x_2(n),
\qquad
x_2(n+1) = x_2(n) \oslash x_1(n).
$$

This is the **minimal mixed chain**: one direct step and one inverse step, interleaved across coordinates. The pair is **ordered**, because $\odot$ and $\oslash$ do not commute (S_00020, §4). Swapping the order of the two coordinates changes the trajectory.

**Vector form.** Let $X = (x_1, x_2)$ and define the componentwise chain map $\Phi(X) = (x_1\odot x_2,\; x_2\oslash x_1)$. The discrete dynamics is the iterate $X(n) = \Phi^{\circ n}(X(0))$, confirming the central thesis of S_00020: the basis is the iterator, and the iterator here is a cross-chain.

**Linearization.** Passing to $u_i = 1/x_i$ makes the cross-chain additive:

$$
u_1(n+1) = u_1(n) + u_2^{-1}(n), \qquad
u_2(n+1) = u_2(n) - u_1^{-1}(n).
$$

The chain is no longer written with $\odot$ and $\oslash$; it has been **linearized** by the Abel isomorphism. This is the sense in which $u$-coordinates are the natural chain coordinates.

### 21.2.3. Continuous Limit and True Invariant

In the infinitesimal limit:

$$
\frac{du_1}{dt} = \frac{1}{u_2}, \qquad
\frac{du_2}{dt} = -\frac{1}{u_1}.
$$

**Derivation of the invariant.** Multiplying the first by $u_2$, the second by $u_1$, and adding:

$$
u_2 \dot u_1 + u_1 \dot u_2 = 1 - 1 = 0
\implies \frac{d}{dt}(u_1 u_2) = 0.
$$

**Exact invariant:**

$$
u_1(t)\, u_2(t) = u_1(0)\, u_2(0) = C = \text{const}.
$$

**Explicit solution.** Substituting $u_2 = C/u_1$ into the first equation:

$$
u_1(t) = u_1(0)\, e^{t/C},
\qquad
u_2(t) = u_2(0)\, e^{-t/C}.
$$

In original coordinates $x_i = 1/u_i$: $x_1(t) = x_1(0)e^{-t/C}$, $x_2(t) = x_2(0)e^{t/C}$. One coordinate decays exponentially while the other grows; there is no oscillation, because both solutions are real exponentials.

**Geometric meaning.** In the $(u_1,u_2)$-plane the trajectory lies on the level set $u_1u_2=C$, a hyperbola. Rotating the axes by $45^\circ$ ($v_\pm = (u_1\pm u_2)/\sqrt 2$) gives $u_1u_2 = (v_+^2-v_-^2)/2$, so the invariant becomes

$$
v_+^2 - v_-^2 = 2C.
$$

The preserved quadratic form $Q(v_+,v_-)=v_+^2-v_-^2$ has signature $(+,-)$ — this is the precise sense of a **pseudo-Euclidean (Minkowski-like) metric**. The asymptotes $v_+=\pm v_-$ (i.e. $u_1u_2=0$) play the role of a light cone.

**Why not a circle.** A circle would require a preserved form of signature $(+,+)$, i.e. an invariant $u_1^2+u_2^2=\text{const}$. No real linear change of coordinates maps a $(+,-)$ form to a $(+,+)$ form. This is the algebraic content of the statement that **circular trigonometry cannot arise from purely real 2D modulation**. Circles require the complex continuation of S_00022.

---

## 21.3. Real 3D Mediated Cascade

### 21.3.1. ODE System

Consider the 3D cascade in original coordinates:

$$
\dot x_1 = -x_1^2 x_2, \qquad
\dot x_2 = -x_2^2 x_3 + x_2^2 x_1, \qquad
\dot x_3 = x_3^2 x_2.
$$

In inverse coordinates $u_i = 1/x_i$:

$$
\dot u_1 = \frac{1}{u_2}, \qquad
\dot u_2 = \frac{1}{u_3} - \frac{1}{u_1}, \qquad
\dot u_3 = -\frac{1}{u_2}.
$$

Note the signs: $\dot u_1$ is positive (direct step with $\kappa = 1/u_2$), $\dot u_3$ is negative (inverse step with the same $\kappa$). The 3D system is therefore also a **mixed chain**, though the mixing only becomes visible in $u$-coordinates.

### 21.3.2. Chain Representation

In $u$-coordinates the 3D cascade is a **homogeneous linear chain** with signed parameters. The first and third equations are chains of length 1:

$$
u_1(t) = u_1(0) \odot \kappa(t),
\qquad
u_3(t) = u_3(0) \oslash \kappa(t),
\qquad
\kappa(t) = \int_0^t \frac{ds}{u_2(s)},
$$

while the second is a chain of length 2 with alternating signs:

$$
u_2(t) = u_2(0) \odot \Bigl(\int_0^t \frac{ds}{u_3(s)}\Bigr) \oslash \Bigl(\int_0^t \frac{ds}{u_1(s)}\Bigr).
$$

### 21.3.3. Failed Spherical Invariant

$$
\frac{d}{dt}(u_1^2 + u_2^2 + u_3^2) = 2 \left( \frac{u_1}{u_2} + \frac{u_2}{u_3} - \frac{u_2}{u_1} - \frac{u_3}{u_2} \right) \neq 0.
$$

The claim of a spherical invariant $u_1^2+u_2^2+u_3^2=\text{const}$ is **false**. This failure is what motivated the reformulation of the design principle in §21.1.

### 21.3.4. True Linear Invariant

Adding the first and third equations:

$$
\dot u_1 + \dot u_3 = \frac{1}{u_2} - \frac{1}{u_2} = 0 \implies u_1 + u_3 = C = \text{const}.
$$

**Chain reading.** The 3D invariant is the **closure of a mixed chain with opposite parameters**: $u_1\odot\kappa$ and $u_3\oslash\kappa$ with the same $\kappa$. Adding them, the integrals cancel. The invariant is linear precisely because the chain is evaluated in $u$-coordinates.

---

## 21.4. Algebraic Structure and Expectations

The modulations of §21.2 and §21.3 are built from the atomic pair

$$
f(x) = \frac{x}{1+x}, \qquad g(x) = \frac{x}{1-x},
$$

which are the two primitive chain operations of S_00020. Before stating what these modulations can and cannot produce, it is useful to recall the algebraic structure of this pair.

### 21.4.1. The Abelian Atom and Its Linearization

Both $f$ and $g$ are fractional-linear transformations, represented by the matrices

$$
f \sim \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix},
\qquad
g \sim \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix}.
$$

Their trace is $\tau = 2$ in both cases. In the classification of Möbius transformations by trace, a transformation is **parabolic** if $|\tau| = 2$, **elliptic** if $|\tau| < 2$, and **hyperbolic** if $|\tau| > 2$. The atomic pair is therefore strictly parabolic.

Parabolic elements that share a common fixed point (here $x = 0$) commute and generate an Abelian subgroup isomorphic to $\mathbb{Z}$ (discrete parameters) or $\mathbb{R}$ (continuous parameters). The Abel function

$$
\alpha(x) = \frac{1}{x}, \qquad \alpha^{-1}(u) = \frac{1}{u},
$$

makes this isomorphism explicit: in the coordinate $u = 1/x$, the nonlinear steps become ordinary translations,

$$
\alpha(f(x)) = \alpha(x) + 1,
\qquad
\alpha(g(x)) = \alpha(x) - 1.
$$

A finite chain with constant parameters therefore collapses to a single translation

$$
u \mapsto u + \sum_i \pm K_i,
$$

and the group operation is plain addition in $\mathbb{R}$.

### 21.4.2. Consequence: Monotonic Sequences

The Abelian structure has a direct dynamical consequence. Any sequential chain built from $f$ and $g$ with **constant parameters** produces a trajectory that is **monotonic in the Abel coordinate $u$**, and therefore monotonic in $x$ except at the pole $u = 0$ (i.e. $x = \infty$).

This is exactly what the 2D and 3D systems of §21.2 and §21.3 exhibit. In 2D, the invariant $u_1u_2 = C$ and the explicit exponential solutions

$$
u_1(t) = u_1(0)\, e^{t/C},
\qquad
u_2(t) = u_2(0)\, e^{-t/C}
$$

are the image, under the Abel isomorphism, of two opposite translations on a single Abelian orbit. In 3D, the linear invariant $u_1 + u_3 = C$ is the direct consequence of the cancellation of two opposite parabolic translations: $u_1$ and $u_3$ move in opposite directions with the same parameter $\kappa = 1/u_2$, and their sum is conserved.

**Expectations.** The current modulation is therefore **monotonic by construction**. It produces:

- exact closed forms (because the chain collapses to a translation);
- linear or multiplicative invariants (because the group is Abelian);
- monotonic trajectories in $u$-coordinates, with poles at $u=0$.

It does **not** produce oscillations, chaos, or non-monotonic invariants. This is not a shortcoming of the specific equations chosen: it is a structural consequence of the parabolic, Abelian nature of the atomic pair. Any sequential chain of $f$ and $g$ with constant parameters will share this behavior.

### 21.4.3. Toward Richer Dynamics

The monotonicity above is the boundary of the current construction, not the boundary of the framework. Three routes lead beyond it, and each corresponds to a controlled modification of the atom or of its evaluation:

1. **Dynamic parameters.** If the parameter $K_n$ depends on the state $x_n$ (as in the cross-modulated systems of §21.2–§21.3) or on the index $n$, the chain no longer collapses to a single translation. The Abel coordinate then satisfies $u_{n+1} = u_n + K_n$, whose solution is the partial sum $\sum K_n$ — still additive, but no longer a single shift. Periodic or polynomial $K_n$ produce non-monotonic trajectories in $x$ without leaving the real line.

2. **A second generator from a different conjugacy class.** If one adds an elliptic generator ($|\tau| < 2$) or a hyperbolic one ($|\tau| > 2$) with a different fixed point, the generated group ceases to be Abelian. For generic choices, the group $\langle f, h \rangle$ is free of rank 2, with a fractal limit set — a genuinely non-monotonic, non-commutative structure. This is the route to new invariants that are neither linear nor multiplicative.

3. **Complexification.** Replacing the real parameter $K$ by $K = it$ moves the atom into the elliptic class. The orbit becomes a circle, and classical trigonometry emerges (see S_00022). This is the route already explored in the companion paper.

### 21.4.4. Open Search

The modulations of §21.2 and §21.3 are therefore the **first rigorous step**, not the final word. They establish a baseline: a parabolic Abelian atom, evaluated sequentially with constant or state-dependent parameters, yields monotonic or piecewise-monotonic dynamics with linear or multiplicative invariants. Richer behavior requires one of the three modifications above, and the choice among them is a matter of design, not of necessity. The search for modulations that produce genuinely new invariants — spherical, spiral, or fractal — is open, and the algebraic framework of S_00020 provides the language in which that search can be carried out.

---

## 21.5. What the Modulation Does and Does Not Buy

| Gain | Where it appears | Concrete form |
| :--- | :--- | :--- |
| Exact closed forms | 2D on invariant, 3D components | $u_1u_2=C$, $u_1+u_3=C$ |
| Conservation law | 3D cascade | $u_1+u_3=C$ reduces effective dimension from 3 to 2 |
| Structural role assignment | 3D cascade | $u_2$ is the mediator; $u_1,u_3$ are symmetric ends |
| Path dependence | Mixed chains | $(A\odot K)\oslash C \neq A\odot(K\oslash C)$ |

What the modulation does **not** buy:

- no universal Kolmogorov–Arnold reduction of $n$-D flows to 1D; that claim failed in 3D (§21.3.3);
- no elimination of nonlinearity — it is **relocated** from the coupling in $x$-coordinates to individual chain steps in $u$-coordinates;
- no spherical invariant in 3D;
- no classification of which $n$-D systems admit exact chain representations — that remains open.

**Honest status of applications.** No practical application is claimed in this paper. The candidates one might explore — modeling of cross-modulated systems, control respecting the linear invariant, feature decomposition by dynamic role — remain **open questions**, not results. This honesty is deliberate: the framework is algebraic, and applications require domain-specific validation not attempted here.

---

## 21.6. Hypothesis on Symmetry of Ensemble and Time Series

### 21.6.1. Formulation

Two limiting constructions are considered:

1. **Spatial ensemble (dimensionality):** cascade $M \to \infty$ of conjugate inverse axes $u_1,\dots,u_M$ — a chain in dimension index.
2. **Time series (iterations):** infinite iteration of a single operator $t \to \infty$ — a chain in time index.

### 21.6.2. Observed Symmetry

Both constructions are described by the same class of rational chain operators; both possess invariants of the form $\sum_i u_i = \text{const}$ (3D) or $u_1u_2=\text{const}$ (2D); both yield stable attractors in the macroscopic limit.

### 21.6.3. Status

**This is a hypothesis, not a theorem.** To elevate it to a rigorous result, one must (i) define an invariant measure on the phase space of KMR-M, (ii) prove metric transitivity of the flow on the invariant manifold, (iii) numerically confirm coincidence of temporal and spatial averages. Until then it remains a scientifically motivated heuristic.

---

## 21.7. Conclusion

The paper explores two cross-modulated KMR chains. What is rigorous:

- the 2D invariant $u_1u_2=C$ and the explicit exponential solution;
- the 3D linear invariant $u_1+u_3=C$;
- the algebraic explanation of why real 2D cannot produce a circle.

What is **not** claimed:

- universal reduction of $n$-D flows to 1D;
- practical applications;
- the ensemble–time-series symmetry (hypothesis only).

The design principle is explicit: **choose signs so that a linear relation in inverse coordinates closes the chain.** Multiplicative in 2D, additive in 3D. Neither is spherical. Rotation requires complexification, treated in S_00022.

---

## 21.8. Appendix: Summary

| Object | Formula |
| :--- | :--- |
| 2D cross-chain | $x_1\odot x_2,\; x_2\oslash x_1$ |
| 2D invariant | $u_1 u_2 = C$ |
| 2D explicit solution | $u_1(t)=u_1(0)e^{t/C},\; u_2(t)=u_2(0)e^{-t/C}$ |
| 3D mediated chain | $u_1\odot\kappa,\; u_3\oslash\kappa,\; \kappa=1/u_2$ |
| 3D linear invariant | $u_1 + u_3 = C$ |
| Failed spherical invariant | $u_1^2+u_2^2+u_3^2 \neq \text{const}$ |

## 21.9. Python Reference

```python
"""
KMR Modulations: Reference Implementation
License: GPL 3.0 (see LICENSE)
"""

from __future__ import annotations
from typing import Tuple


def cross_step_2d(x1: float, x2: float) -> Tuple[float, float]:
    """One 2D cross-chain step."""
    d1 = 1.0 + x1 * x2
    d2 = 1.0 - x1 * x2
    if abs(d1) < 1e-15 or abs(d2) < 1e-15:
        return (float("nan"), float("nan"))
    return (x1 / d1, x2 / d2)


def invariant_2d(u1: float, u2: float) -> float:
    """Real 2D invariant u1 * u2 = const."""
    return u1 * u2


def cascade_step_3d(x1: float, x2: float, x3: float, dt: float) -> Tuple[float, float, float]:
    """One explicit Euler step of the 3D cascade (dt small)."""
    dx1 = -x1 * x1 * x2
    dx2 = -x2 * x2 * x3 + x2 * x2 * x1
    dx3 = x3 * x3 * x2
    return (x1 + dt * dx1, x2 + dt * dx2, x3 + dt * dx3)


def invariant_3d(u1: float, u3: float) -> float:
    """Real 3D coupling invariant u1 + u3 = const."""
    return u1 + u3