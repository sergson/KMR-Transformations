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

# 24. Curvature Generalization of the Continuous Phase Atom: The Persistent Unity
**Author**: Sergei Terikhov  
**Date**: 20.10.2026

## Abstract

The continuous phase atom of S_00023 possesses two degrees of freedom: the real phase $\(\alpha\)$ and the gauge scalar $\(D\)$. 
We demonstrate that a real phase is structurally confined to the elliptic and parabolic Möbius classes; 
the hyperbolic class is inaccessible without artificially inflating the gauge parameter or deforming the trigonometric structure itself. 
We therefore replace the flat trigonometric invariant with the generalized Pythagorean identity 

$$
\(\cos_k^2(\alpha) + k\sin_k^2(\alpha) = 1\)
$$

, where $\(k \in \mathbb{R}\)$ is the curvature parameter. 
Crucially, the unit $\(1\)$ is **not eliminated**: it remains explicitly in the denominator as a structural place, now deformed by curvature. 
The resulting **curvature atom** naturally produces all three Möbius classes: 
$\(k = 1\)$ (elliptic, oscillations), 
$\(k = 0\)$ (parabolic, monotonicity), 
and $\(k < 0\)$ (hyperbolic, exponential growth/decay). 
The classical atom remains a natural intermediate stage; its integrity is preserved, and it allows for recursive unfolding into a fractal hierarchy of curvatures.
---

## 24.1. The Inevitability of Curvature

In S_00023, the continuous phase atom was derived by deconstructing the rigid unit of the canonical KMR operator:

$$
F(A, B, D, \alpha) = \frac{A \cdot D}{(1 - \cos 2\alpha) + A \cdot \left(\frac{B}{D}\right)}.
$$

The Möbius matrix acting on the modulation parameter has the trace $\(\tau_B = 1 - \cos(2\alpha)\)$. 
Since $\(\alpha\)$ is real, $\(\cos(2\alpha) \in [-1, 1]\)$, which strictly limits the trace to the interval $\([0, 2]\)$. 
Consequently, the phase $\(\alpha\)$ can only interpolate between the **elliptic** class $(\(|\tau| < 2\)$, oscillations) and the **parabolic** boundary $(\(\tau = 2\)$, monotonic Abel flow). 

To reach the **hyperbolic** class $(\(|\tau| > 2\)$, exponential growth or decay), one must either artificially inflate the gauge scalar $\(D\)$ (which changes the scale of the state matrix $\(M_A\)$ but not the geometry of the phase) or **deform the trigonometric structure itself**. 
The latter is the natural path forward.

## 24.2. The Persistent Unit

A naive generalization might replace the flat unit with the curvature-dependent expression $\(2k\sin_k^2(\alpha)\)$. 
However, this obscures the structural foundation of the atom. 
We insist on preserving the unit explicitly:

$$
F_k(A, B, D, \alpha) = \frac{A \cdot D}{\bigl(1 - \cos_k(2\alpha)\bigr) + A \cdot \left(\frac{B}{D}\right)}.
$$

The unit $\(1\)$ remains in the denominator for three reasons:
1. **Structural place:** It can be recursively unfolded in future generalizations.
2. **Explicit Deformation:** The transition from flat geometry to curved geometry is a deformation of an entity, not its destruction.
3. **Recoverability:** At $\(k = 1\)$, we recover the exact formulation of S_00023.

## 24.3. Curvature Deformation and $\(k\)$ - Trigonometry

We replace the flat Pythagorean identity with its curvature-dependent counterpart:

$$
\cos_k^2(\alpha) + k \sin_k^2(\alpha) = 1,
$$

where the generalized sine and cosine functions depend on the curvature parameter $\(k \in \mathbb{R}\)$:
- $\(k > 0\)$ (Sphere): $\(\sin_k(\alpha) = \frac{\sin(\sqrt{k}\alpha)}{\sqrt{k}}, \quad \cos_k(\alpha) = \cos(\sqrt{k}\alpha)\)$.
- $\(k = 0\)$ (Plane): $\(\sin_k(\alpha) = \alpha, \quad \cos_k(\alpha) = 1\)$.
- $\(k < 0\)$ (Saddle): $\(\sin_k(\alpha) = \frac{\sinh(\sqrt{-k}\alpha)}{\sqrt{-k}}, \quad \cos_k(\alpha) = \cosh(\sqrt{-k}\alpha)\)$.

The generalized double-angle formula is:

$$
\cos_k(2\alpha) = \cos_k^2(\alpha) - k \sin_k^2(\alpha).
$$

Using the Pythagorean identity, the deformed unit can be written in two algebraically identical forms:

$$
1 - \cos_k(2\alpha) = 2k \sin_k^2(\alpha).
$$

The left-hand side is the canonical form used in the atom, as it preserves the unit.

## 24.4. The Curvature Atom

Substituting the deformed unit into the phase atom, we obtain the **curvature atom**:

$$
F_k(A, B, D, \alpha) = \frac{A \cdot D}{\bigl(1 - \cos_k(2\alpha)\bigr) + A \cdot \left(\frac{B}{D}\right)}.
$$

The denominator consists of two terms:
- **The deformed unit** $\(1 - \cos_k(2\alpha)\)$, which encodes the geometry of the computational space.
- **The interaction term** $\(A(B/D)\)$, which encodes the modulation.

## 24.5. Classification by Curvature

The curvature parameter $\(k\)$ determines the Möbius class of the modulation step:

| Curvature $\(k\)$ | Geometry | $\(\cos_k(2\alpha)\)$ | Möbius Class | Behavior |
| :--- | :--- | :--- | :--- | :--- |
| $\(k = 1\)$ | Sphere | $\(\cos(2\alpha)\)$ | Elliptic | Oscillations, return trajectories |
| $\(k = 0\)$ | Plane | $\(1\)$ | Parabolic | Monotonic, Abel flow |
| $\(k < 0\)$ | Saddle | $\(\cosh(\sqrt{-k} \cdot 2\alpha)\)$ | Hyperbolic | Exponential growth or decay |

For $\(k < 0\)$, the deformed unit $\(1 - \cos_k(2\alpha) = 1 - \cosh(\sqrt{-k} \cdot 2\alpha)\)$ becomes strictly negative and grows without bound, driving the trace to values less than $\(-2\)$. This is the natural geometric origin of the hyperbolic class.

## 24.6. The Classical Atom as a Topological Waypoint

In the elliptic regime $(\(k > 0\))$, as $\(\alpha\)$ varies monotonically, the deformed unit $\(1 - \cos_k(2\alpha)\)$ must pass through the value $\(1\)$. This occurs when $\(\cos_k(2\alpha) = 0\)$, which happens at $\(\alpha = \frac{\pi}{4\sqrt{k}}\)$. At this phase, the atom reduces to:

$$
F_k\left(A, B, D, \frac{\pi}{4\sqrt{k}}\right) = \frac{A \cdot D}{1 + A \cdot \left(\frac{B}{D}\right)},
$$

which is the classical KMR atom with gauge $\(D\)$. The classical atom is therefore a **forced waypoint** in any continuous transition within the elliptic regime. 
For $\(k \le 0\)$, the classical atom arises as a limiting boundary case as the geometry degenerates.

## 24.7. Recursive Unfolding and Fractal Curvatures

Because the unit $\(1\)$ is preserved, the curvature deformation can be applied **recursively**. 
The atom can be unfolded into a hierarchy of curvatures:

$$
1 \to 1 - \cos_{k_1}(2\alpha_1) \to 1 - \cos_{k_2}(2\alpha_2) - \cos_{k_1}(2\alpha_1) \to \cdots
$$

Each step adds a new curvature layer, generating a fractal hierarchy of interacting geometries. 
The unit is never eliminated; it is the base of the next unfolding. 
This provides a natural mechanism for modeling systems with multiple curvature scales or hierarchical phase transitions.

## 24.8. Conclusion

The rigid unit is not a constant to be eliminated, but a structural anchor to be deformed. The curvature atom 

$$
F_k(A, B, D, \alpha) = \frac{A \cdot D}{\bigl(1 - \cos_k(2\alpha)\bigr) + A \cdot (B/D)}
$$

preserves the unit explicitly, naturally produces all three Möbius classes, and admits recursive unfolding into a fractal hierarchy of curvatures. 
The phase $\(\alpha\)$ controls the geometry within a given $\(k\)$, the gauge $\(D\)$ balances the computational scale, and the curvature $\(k\)$ determines the fundamental conjugacy class of the space.

---

## 24.9. Appendix: Summary of Key Formulas

| Object | Formula |
| :--- | :--- |
| Generalized Pythagorean identity | $\(\cos_k^2(\alpha) + k\sin_k^2(\alpha) = 1\)$ |
| Generalized double angle | $\(\cos_k(2\alpha) = \cos_k^2(\alpha) - k\sin_k^2(\alpha)\)$ |
| Deformed unit | $\(1 - \cos_k(2\alpha) = 2k\sin_k^2(\alpha)\)$ |
| Curvature atom | $\(F_k(A, B, D, \alpha) = \dfrac{A \cdot D}{\bigl(1 - \cos_k(2\alpha)\bigr) + A(B/D)}\)$ |
| Elliptic regime | $\(k = 1\)$, $\(\tau_B = 1 - \cos(2\alpha) \in [0, 2]\)$ |
| Parabolic regime | $\(k = 0\)$, deformed unit $\(\to 0\)$ |
| Hyperbolic regime | $\(k < 0\)$, deformed unit $\(\to -\infty\)$ |
| Classical waypoint | $\(\alpha = \frac{\pi}{4\sqrt{k}}\)$, atom reduces to $\(A/(1 + A(B/D))\)$ |
