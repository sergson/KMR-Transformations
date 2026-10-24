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


# 27. Atomic Algebra: Questions and Answers on the Advantages of the Approach
**Author**: Sergei Terikhov  
**Date**: 24.10.2026

**Abstract.** A short collection of answers to frequently asked questions about the atomic algebra $A_u(x)=x/(u-x)$. The questions concern: the relation between the non-shift algebra and Boolean algebra; the meaning of the "pre-Boolean" status; why shift is secondary to division; how the distinguishability threshold works; why the unit is a parameter rather than an axiom; and what advantages this gives over the standard Boolean picture. The answers are formulated in a popular style but stay within the bounds of the proved core: external negation $\nu(S)\notin S$; the chain $C_{n+1}=C_n\cup\{\nu(C_n)\}$; the $\Sigma_0$-atomicity of $x/(1-x)$; its definability in $\Sigma_3^+$; uniqueness in the Möbius class.

---

## Q1. What is atomic algebra in one sentence?

**Answer.** Atomic algebra is the algebra whose basic object is the division atom $A_u(x)=x/(u-x)$, where $u$ is a distinguishable norm (unit) rather than a fixed axiom. Everything else—shift, Boolean complement, threshold—is derived or is a special case.

The name reflects the main claim: division is the atom, and shift is secondary.

---

## Q2. Why is $x/(1-x)$ called an atom and not just a function?

**Answer.** Because in the minimal signature $\Sigma_0=\{0^\ast,e,1,\nu\}$, it cannot be expressed as a nontrivial unary term. Any term of sort $E$ in $x$ is either $x$ itself or a constant. So $x/(1-x)$ is not built from simpler element operations—it appears only when division and duality $\partial$ are added. This is **relative atomicity**: it holds with respect to $\Sigma_0$ and disappears when the signature is extended.

In short: in the minimal language, there is nothing simpler from which to assemble $x/(1-x)$.

---

## Q3. Why is shift secondary to division?

**Answer.** Because division is available at level $C_3$ in the signature $\Sigma_3^+$, while successor $\sigma(x)=x+1$ is not in $\Sigma_3^+$ at all. Any expression with $\sigma$ requires an extended signature $\Sigma_3^\sigma$.

This is not a philosophical claim but a formal one: in the order of signatures, division precedes shift. Shift appears later, after the unit has been identified and the signature extended.

---

## Q4. Does this mean shift is unnecessary?

**Answer.** No. Shift is necessary as an arithmetic identification, but it is not a primitive of the triadic scheme. It arises after the level has been generated and the unit identified. The correct formulation: shift is **secondary**, not **eliminated**.

---

## Q5. What does "non-shift algebra" mean?

**Answer.** The non-shift algebra is the algebra $\mathcal A_n^G(u)=(C_n;\Sigma_3^+(u)\upharpoonright C_n)$, where $\Sigma_3^+(u)=\{0^\ast,e,u,\partial_u,/\}$ and $\partial_u(x)=u-x$. The symbol $\sigma$ is absent from it. The unit $u$ is a parameter, not an axiom.

The name emphasizes: this algebra does not contain shift as an operation. Shift appears only in an extension.

---

## Q6. Is the non-shift algebra "pre-Boolean"?

**Answer.** Yes, in a precise sense. Boolean algebra is the special case of the non-shift algebra with a fixed unit $u=1_R$ and a fixed threshold. In the non-shift algebra, the unit is a parameter $u$ and the threshold $\delta_n$ is an explicit term.

So:

- Boolean algebra = $A_1$ with a **frozen** unit.
- Non-shift algebra = $A_u$ with a **regulated** unit.

Boolean algebra can be obtained from the non-shift algebra by fixing $u=1_R$. The reverse is impossible: Boolean algebra has no parameter $u$, so it cannot "rise" to the non-shift algebra. This is the meaning of "pre-Boolean": containing Boolean algebra as a normalized limit, but not reducing to it.

---

## Q7. Does Boolean algebra have hysteresis? And what does that change?

**Answer.** Boolean algebra may have hysteresis—a dead band around the threshold, as in a Schmitt trigger. But this hysteresis is **fixed**: it is part of the "hardware," not part of the algebra. Boolean algebra cannot **change** its threshold or its unit; it can only have a fixed dead band around them.

In the non-shift algebra, the threshold $\delta_n$ is an explicit term that can be assigned at the meta-level. Hysteresis here is **regulated**, not fixed.

---

## Q8. Why is the unit a parameter and not an axiom?

**Answer.** Because the unit is a **distinguishable norm** assigned by the observer, not a property of the algebra itself. In the triadic scheme, each level exists only because a threshold distinguishes $x$ and $\mathrm{NOT}(x)$. If the threshold is not distinguished, the level collapses.

So the unit is not given "from below"—it descends "from above," from the meta-level. Making it a parameter is the formal expression of this: the algebra does not dictate its unit; the observer assigns it.

---

## Q9. What is the distinguishability threshold?

**Answer.** The threshold $\delta_n$ is the element that makes $x$ and $\mathrm{NOT}(x)$ distinguishable for all $x$ at level $n$. In the polymorphic algebra, it is given by the condition $x\neq u/2$: at $x=u/2$, we have $x=\mathrm{NOT}(x)$, and distinction is impossible.

Without a threshold, the level collapses: either $\nu$ is undefined, or $\nu(S)\in S$, which contradicts $\nu(S)\notin S$.

---

## Q10. Why is the top layer "one term larger"?

**Answer.** Because the top layer contains the governing term

$$
\Delta(x)=\mathrm{NOT}\!\left(\frac{x}{\mathrm{NOT}(x)}\right)=u-\frac{x}{u-x},
$$

which controls all thresholds. This term is the "distinction of distinction"—the control unit of the entire hierarchy.

By construction $C_{n+1}=C_n\cup\{\delta_n\}$, where $\delta_n$ is the threshold. At the top level, the threshold becomes an explicit term. Hence the top layer is one term larger.

---

## Q11. What advantage does this give over the standard Boolean picture?

**Answer.** Three advantages.

**First, the unit becomes adjustable.** Boolean algebra fixes the unit once and for all. The non-shift algebra allows the unit to be a parameter, which is necessary wherever the norm is not given in advance—fuzzy logic, curvature, non-standard analysis.

**Second, shift is no longer primitive.** In the standard picture, shift (successor, normalization) is often taken as basic. Here it is derived: division comes first, shift appears after the level has been generated. This clarifies the order of primitives.

**Third, the hierarchy is explained.** Boolean algebra appears as a normalized limit, not as the only possible algebra. The non-shift algebra explains **why** Boolean algebra is the way it is: because its unit is frozen.

---

## Q12. Does this have practical applications?

**Answer.** Potentially, in three areas.

**Fuzzy logic and control.** The unit $u$ can be adjusted continuously, which matches the behavior of fuzzy controllers better than a fixed Boolean threshold.

**Curvature and geometry.** The parametrization $u(k)=1-\cos_k(2\alpha)$ links the unit to curvature. This gives a curvature-generalized atom $A_{u(k)}$, which reduces to the classical atom at $k=1$.

**Computation.** The KMR-algebra with its atom $A/(1+KA)$ is a direct relative of $A_u$. The non-shift algebra provides a foundation for it: the atom is primary, the iterated shift is derived.

---

## Q13. What remains open?

**Answer.** Three questions.

**First, absolute primacy of $A_u$.** Relative atomicity is proved: $A_u$ is not definable in $\Sigma_0$. But absolute primacy requires a separate order of term complexity. This is not yet built.

**Second, the status of $e/e$.** In the standard syntax, $e/e$ is a term of $\Sigma_3^+$ and equals $1_R$. The claim that "$e/e$ is not primitive" requires linear or resource-sensitive terms. Without this, the claim is not proved.

**Third, the general classification of Möbius generators.** Uniqueness is proved in the class with $f(0)=0$, a pole at $u$, and a fixed value at $\varepsilon$. The full classification of all Möbius generators by the invariant $\operatorname{tr}^2/\det$ remains open.

---

## Q14. In one formula: what is the main thesis?

**Answer.**

$$
\boxed{
\begin{aligned}
&\text{Division is primary, shift is secondary.}\\
&\text{The unit is a parameter, not an axiom.}\\
&\text{Boolean algebra is the normalized special case with a frozen unit.}\\
&\text{The non-shift algebra is pre-Boolean: it contains Boolean algebra as a limit, but does not reduce to it.}
\end{aligned}}
$$

---

## Q15. Why "atomic algebra" and not "non-shift algebra" in the title?

**Answer.** Because the atom is the central object: $A_u(x)=x/(u-x)$. "Non-shift" is a negative characterization—it says what the algebra does not contain. "Atomic" is positive—it says what the algebra is built from.

The full title could be: **Atomic Algebra: Division as Primitive, Shift as Derived, Unit as Parameter.**

---

## Conclusion

The atomic algebra is an attempt to build algebra from below—from the division atom and the distinguishability threshold—rather than from above, from a fixed Boolean unit. Its main advantages are: adjustable unit, secondary shift, explained hierarchy. Its main open questions are: absolute primacy of the atom, the status of $e/e$, and the full classification of Möbius generators.

The approach does not replace Boolean algebra; it explains it as a normalized limit. This is its main value: Boolean algebra ceases to be the only possible algebra and becomes one case among many, distinguished by a frozen unit.