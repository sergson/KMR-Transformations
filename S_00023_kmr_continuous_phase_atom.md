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

# 23. Deconstruction of unity and gauge-balanced dualities of KMR operators (The Continuous Phase Atom)
**Author**: Sergei Terikhov  
**Date**: 20.10.2026

## Abstract
In the canonical KMR model (S_00020–S_00022), there is a choice between direct ($\odot$) and inverse ($\oslash$) operators, which is discrete and determined by a fixed value of $\pm 1$ in the denominator. In this work, this "unity" element is reinterpreted. A continuous trigonometric equivalent is derived by invoking an orthogonality condition ($\beta = \alpha + \pi/2$), which transforms the discrete sign into a smooth phase rotation of the form $1 - \cos(2\alpha)$. Furthermore, a scaling factor $D$ is introduced, acting as a "balancing element": it functions similarly to modulating the term that occupies the position of unity—linearly amplifying the input amplitude ($A \cdot D$) while simultaneously attenuating the modulation step ($B/D$) in inverse proportion. Crucially, their product, $A \cdot B$, remains constant, allowing for dynamic control of the atom's state. The resulting **"Continuous Phase Atom"** enables a smooth transition between elliptic, parabolic, and hyperbolic classes of Möbius transformations—achieved simply by varying the phase $\alpha$—thereby eliminating the need for conditional branching in numerical implementations.
---

## 23.1. The Genesis: Replacing the Unit

The foundational KMR atom is defined by two distinct operations:

$$
A \odot B = \frac{A}{1 + AB}, \qquad A \oslash B = \frac{A}{1 - AB}.
$$

Here, the unit ($1$) acts as a passive functional element. The choice between the direct (compression) and inverse (expansion) modes is made through the discrete selection of an operator.

Analyzing the meaning of this element, we posit the existence of a state of atomic destruction, in which the rigid element varies according to a metric scalar $\(D\)$:

$$
F(A, B, D) = \frac{A}{D \pm AB}.
$$

At first glance, $\(D\)$ is simply an arbitrary coefficient. However, let us perform an identity transformation by multiplying both the numerator and the denominator by $\(D\)$:

$$
F(A, B, D) = \frac{D \cdot A}{1 \pm A \cdot \left(\frac{B}{D}\right)}.
$$

Look closely at this result. We started by replacing the unit with $\(D\)$, but **a rigid unit has reappeared** in the denominator. 

What is this? This transformation reveals a **Balancing Co-Scaling** mechanism. The parameter $\(D\)$ operates as a lever:
- The input amplitude $\(A\)$ is scaled proportionally: $\(A \to (D \cdot A)\)$.
- The modulation parameter $\(B\)$ is scaled inversely: $\(B \to (B/D)\)$.
- Their internal product remains invariant: $\((D \cdot A) \cdot (B/D) = AB\)$.

We are left with a rigid $\(1\)$ in the denominator and a free parameter $\(D\)$ in the numerator. This creates a fundamental bifurcation in how we understand the atom. The structure is symmetric, offering two distinct but equivalent paths.

## 23.2. The Bifurcation: Two Symmetrical Paths

The reappearance of $\(1\)$ means that $\(D\)$ and $\(1\)$ are deeply connected. We can proceed along two symmetrical paths:

### Path A: Geometric Revelation (Trigonometry)
If we interpret the rigid $\(1\)$ as a collapsed trigonometric metric, we can deconstruct it using an orthogonal phase invariant (where the phase shift is $\(\beta = \alpha + \pi/2\))$:

$$
D = \sin^2(\alpha) + \cos^2(\alpha + \pi/2) = 2\sin^2(\alpha) = 1 - \cos(2\alpha).
$$

This path absorbs the discrete sign $\(\pm\)$ into a continuous rotation of the angle $\(\alpha\)$. It moves us along a single smooth Riemann surface.

### Path B: Dynamic Modulation (Co-Scaling)
If we treat $\(D\)$ as an independent, dynamic function $\(D(t)\)$ or $\(D(\alpha, \beta)\)$, it acts as a **balancing regulator**. 
In classical 2D cross-chains (S_00021), the Abel structure forces monotonic behavior: one coordinate grows while the other decays. But Path B introduces a dynamic lever:
- When the system approaches a singularity (the product $\(AB\)$ grows dangerously), the balance function $\(D\)$ can increase.
- This instantly dampens the effective modulation step $\(B/D\)$.
- Simultaneously, it transfers energy to the numerator $\(D \cdot A\)$, shifting the computation to a higher scale without breaking the chain.

Path B allows the space to "breathe," cyclically exchanging roles between $\(A\)$ and $\(B\)$, thus destroying the rigid Abelian monotonicity.

### 23.3. The Unified Continuous Phase Atom

Both paths are symmetrical and mathematically consistent. They converge when we recognize that the deconstructed unit itself is the phase wave. By substituting \(D = 1 - \cos(2\alpha)\) into our transformed atom, and by keeping a strictly positive sign in the denominator, we arrive at the **Continuous Phase Atom**:

$$
F(A, B, D, \alpha) = \frac{A \cdot D}{(1 - \cos 2\alpha) + A \cdot \left(\frac{B}{D}\right)}.
$$

**The New Role of B (Operator Type).**
Notice that the rigid $\(\pm\)$ operator is completely gone from the formula. In the canonical KMR model, the choice between direct $(\(\odot\))$ and inverse $(\(\oslash\))$ required an external switch. Here, this choice is naturally absorbed by the **sign of the modulation parameter $\(B\)$**:
- If $\(B > 0\)$, the term $\(A(B/D)\)$ is positive, yielding the direct-like (compression) behavior.
- If $\(B < 0\)$, the term $\(A(B/D)\)$ is negative, yielding the inverse-like (expansion) behavior.

Thus, $\(B\)$ is no longer just a magnitude of modulation; it is a **signed parameter that defines the operator's duality class**.

**Behavior at Critical Points:**
1. **At $\(\alpha = \pi/2\)$:** $\(D = 1 - \cos(\pi) = 2\)$. The denominator becomes $\(2 + A(B/D)\)$. We recover a scaled canonical KMR atom, where the sign of $\(B\)$ dictates direct vs. inverse.
2. **At $\(\alpha = 0\)$:** $\(D = 1 - \cos(0) = 0\)$. The constant metric completely annihilates. The nonlinear residue remains:

$$
F(A, B, 0) = \frac{A \cdot 0}{0 + A(B/0)} = \frac{D^2}{B}.
$$
The input impulse $\(A\)$ completely cancels out, and the system undergoes a phase transition into a "pure division" mode. The sign of $\(B\)$ determines whether this limit is positive or negative, acting as the stabilizing lever.

### 23.4. Dynamic Sign Calibration and Möbius Trace

The geometric implication becomes clear when we translate the continuous phase atom into its Möbius matrix representation. For a given state $\(A\)$ and a signed parameter $\(B\)$, the transformation operates on $\(K = B/D\)$. The matrix $\(M\)$ acting on the complex plane takes the form:

$$
M(\alpha) = \begin{pmatrix} 0 & A \cdot D \\ A/D & 1 - \cos(2\alpha) \end{pmatrix}.
$$

*(Note: The trace of a Möbius matrix is independent of the specific values of $\(A\)$ and $\(B\)$ in the numerator/denominator, as they are scaled out).*

The trace of this matrix is:

$$
\tau = 1 - \cos(2\alpha).
$$

This formula reveals the magic of the continuous phase:
- **Parabolic Class $(\(|\tau| = 2\))$:** Occurs when $\(\cos(2\alpha) = -1\)$, i.e., $\(\alpha = \pi/2\)$. This is the classical, monotonic KMR flow.
- **Elliptic Class $(\(|\tau| < 2\))$:** Occurs when $\(0 < \alpha < \pi/2\)$. The system oscillates (return trajectories, like in S_00022, but without needing complex numbers).
- **Hyperbolic Class $(\(|\tau| > 2\))$:** Not reachable with real \(\alpha\) in this specific normalization, but accessible if the phase is complexified.

By simply rotating the phase $\(\alpha\)$, the atom continuously changes its conjugacy class. The angle $\(\alpha\)$ controls the **geometry** (the trace), while the sign of $\(B\)$ controls the **duality direction** (compression vs. expansion).

## 23.5. Conclusion

We have deconstructed the KMR atom along two symmetric paths. The rigid unit $1$ is replaced by a dynamic phase wave $\(1 - \cos(2\alpha)\)$ (Path A) and a balancing scalar $\(D\)$ (Path B) that controls the computational lever. This "clean" atom removes the need for conditional operators in numerical implementations. The flow simply evolves according to the phase \(\alpha\). This closes the structure of the atom and opens the door to creating 2D cross-chains where the angles $\(\alpha_1, \alpha_2\)$ themselves generate auto-oscillations instead of monotonic escapes to infinity.

---

## 23.6. Appendix: Summary

| Object | Formula |
| :--- | :--- |
| Perturbed atom | $\(F(A,B,D) = \frac{A}{D \pm AB}\)$ |
| Co-scaling transformation | $\(F = \frac{D \cdot A}{1 \pm A(B/D)}\)$ |
| Orthogonal invariant (Path A) | $\(D = 1 - \cos(2\alpha)\)$ |
| Continuous phase atom | $\(F(A, B, D, \alpha) = \dfrac{A \cdot D}{(1 - \cos 2\alpha) \pm A(B/D)}\)$ |
| Phase transition ($\(\alpha=0\)$) | $\(F = D^2 / B\)$ |
| Möbius trace | $\(\tau = 1 - \cos(2\alpha)\)$ |