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

Q13. What exactly is proven, and what lies beyond the proven core?

**Answer.** The proven core is complete for the main thesis. What remains open are stronger claims that the theory does not depend on. The distinction matters, so let us separate them.

**What is proven (the core):**

In the minimal signature $\Sigma_0=\{0^\ast,e,1,\nu\}$, no nontrivial unary term of sort $E$ in $x$ exists except $x$ itself. Hence $A_u(x)=x/(u-x)$ is not definable in $\Sigma_0$ for any $u$. This is relative atomicity—the atom cannot be assembled from the minimal language.

In $\Sigma_3^+=\{0^\ast,e,1,\partial,/\}$, the atom is a term, and its value at $x=e$ is $\varepsilon/(u-\varepsilon)$.

Successor $\sigma(x)=x+1$ is not in $\Sigma_3^+$. In the order of signatures, division precedes shift.

In the Möbius class with $f(0)=0$, a pole at $u$, and $f(\varepsilon)=\varepsilon/(u-\varepsilon)$, the atom is unique.

These four statements are theorems. They do not depend on anything below.

**What is open, and why it does not undermine the core:**

**(a) "Absolute" primacy of the atom.** Relative atomicity says: the atom cannot be built from $\Sigma_0$. "Absolute" primacy would say: no extension of any kind can express the atom more simply than the atom itself. This is a much stronger claim, and it requires a separate theory of term complexity—a way to compare terms across different signatures. That theory is not yet built. But the main thesis does not need it. The claim "division is primary" is a claim about $\Sigma_0$ and $\Sigma_3^+$, and it is fully proven. "Absolute" primacy is a bonus question, not a foundation.

**(b) The status of $e/e$.** In standard syntax, $e/e$ is a term of $\Sigma_3^+$ and equals $1$. So in standard syntax, " $1$ can be obtained by division" is true. The claim that " $e/e$ is not primitive" requires a different syntax—linear terms, in which each constant is used at most once. In linear syntax, $e/e$ is not a term, and $1$ is introduced only through $\nu(C_2)$. Which syntax is "right" is a modelling choice, not a mathematical gap. The theorem "division precedes shift in the order of signatures" holds in either syntax; only the finer claim about $e/e$ depends on the choice.

**(c) Full classification of Möbius generators.** The theorem proves uniqueness in the class with $f(0)=0$, a pole at $u$, and $f(\varepsilon)=\varepsilon/(u-\varepsilon)$. The full classification of all Möbius generators by the invariant $\mathrm{tr}^2/\det$ is a completeness question: which other generators exist, and how they relate. It does not affect the proven result: within the relevant class, the atom is unique. The open question is "what lies outside the class", not "is the class correct".

**Why this is not a weakness.** A theory is not weak because it states what it does not cover. It is weak if it claims more than it proves. Here the core claims—relative atomicity, primacy of division in the order of signatures, uniqueness in the Möbius class—are fully proven. The open items are extensions: stronger primacy, a finer syntax, a full classification. Each is a separate project, and each can be pursued without touching the core.

**In one sentence:** the foundation is proven; what is open are stronger claims that the foundation does not need.

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

## Q16. Can this be shown on a numerical example?

**Answer.** Yes. Take four levels with units $u=8,4,2,1$. The atom at each level is

$$
A_u(x)=\frac{x}{u-x},\qquad \delta=\frac{u}{2}.
$$

| Level | $u$ | Threshold $\delta=u/2$ | Atom |
|---|---|---|---|
| 1 | 8 | 4 | $x/(8-x)$ |
| 2 | 4 | 2 | $x/(4-x)$ |
| 3 | 2 | 1 | $x/(2-x)$ |
| 4 | 1 | 0.5 | $x/(1-x)$ |

At level 1, as $x\to4$, we have $A_8(x)\to1$, and at $x=4$: $\mathrm{NOT}(4)=8-4=4$, i.e. $x=\mathrm{NOT}(x)$—the distinction vanishes. This is the hint of shift. The observer passes downward:

$$
\nu_1=4,\quad u_2=4,\quad \delta_2=2.
$$

Then at level 2, as $x\to2$, a new split occurs, and $u_3=2$, $\delta_3=1$ are passed down. At level 3, as $x\to1$: $u_4=1$, $\delta_4=0.5$. At level 4 the governing term

$$
\Delta(x)=u-\frac{x}{u-x}
$$

at the threshold gives

$$
\Delta_1(0.5)=1-\frac{0.5}{0.5}=0.
$$

The sequence of the governing term along the chain:

$$
\Delta_8(4)=7,\quad \Delta_4(2)=3,\quad \Delta_2(1)=1,\quad \Delta_1(0.5)=0.
$$

That is, $7\to3\to1\to0$: the signal from the tip to the head decreases until it vanishes at the Boolean normalization point $u=1$. Below $u=1$ it becomes negative: $\Delta_{0.5}(0.25)=-0.5$—the algebra enters the anti-Boolean regime.

**Short formula:**

$$
\boxed{
\text{Downward: threshold becomes an element, the unit is halved.}
\quad
\text{Upward: }\Delta(\delta)=u-1\text{ decreases }7\to3\to1\to0\to-0.5.
}
$$

---

## Q17. Is there an intuitive analogy?

**Answer.** Yes—an octopus. The head sets the scale, the tentacles stretch downward to different depths, the suckers are the elements of the levels, and $\Delta(x)$ is the nerve signal from tip to head.

**Head.** The top unit $u_{\mathrm{top}}$—the scale from which all lengths are measured.

**Tentacle.** The chain

$$
C_1\subsetneq C_2\subsetneq\dots\subsetneq C_N,
$$

where the length is given by halving:

$$
N=\log_2\!\left(\frac{u_{\mathrm{top}}}{\delta_{\min}}\right).
$$

That is, **the length of a tentacle is a solution**: how many times the unit must be halved to reach the minimal distinguishable threshold.

**Suckers.** The elements of the levels: $0^\ast,e,1,\dots$. The farther from the head, the smaller: $u_n=u_{\mathrm{top}}/2^{n-1}$.

**Thinner means more sensitive.** The derivative of the atom at the threshold point:

$$
\left.\frac{dA_u}{dx}\right|_{x=u/2}=\frac{4}{u}.
$$

The product of thickness and sensitivity:

$$
u\cdot\frac{4}{u}=4=\text{const}.
$$

Law of conservation: the thinner the tentacle, the more sensitive it is, and the product is constant along its length. This is the formal analogue of the octopus tentacle tip containing more receptors per unit area.

**The governing term is the nervous system.** $\Delta(x)$ is the signal from tip to head: "the limit has been reached here." It decreases along the tentacle: $7\to3\to1\to0\to-0.5$. Positive—the tentacle is alive; zero—it has reached Boolean normalization; negative—it has entered the anti-Boolean regime.

**Collapse—the tentacle hits the bottom.** As $u\to\ell_P$, further halving is impossible: the threshold falls below distinguishability. The threshold returns to the head as $\Delta_{\mathrm{top}}$, and the head reassigns the norm.

**Summary:**

$$
\boxed{
\begin{aligned}
&\text{Head: }u_{\mathrm{top}}\text{ --- the scale.}\\
&\text{Tentacles: chains }C_1\subsetneq\dots\subsetneq C_N\text{ per number of independent thresholds.}\\
&\text{Length: }N=\log_2(u_{\mathrm{top}}/\delta_{\min})\text{ --- the solution of the distinction problem.}\\
&\text{Suckers: elements of the levels; thinner --- more sensitive }(u\cdot4/u=4).\\
&\text{Bottom: }\delta_{\min}\text{ (e.g. }\ell_P\text{); collapse and return of }\Delta(x)\text{ to the head.}
\end{aligned}}
$$

---

## Q18. How can a second dimension be added if extensions of the lower levels are forbidden?

**Answer.** Through **modulation of the distinguishability threshold** by the information coming from the lower layers. This is the minimal variant consistent with the triadic construction.

**The prohibition.** In the triadic scheme, an extension of a lower level is impossible: $C_{n+1}=C_n\cup\{\nu_n(C_n)\}$ is a transition upward, not an addition of terms downward. Hence a second dimension cannot be obtained by a flat extension $C_n\to C_n\cup\{\text{new terms}\}$.

**The resolution.** The threshold $\delta_n$ is not fixed: it is **modulated** by the signal $\Delta_{n+1}$ coming from above. That is,

$$
\delta_n\;\longmapsto\;\delta_n(\Delta_{n+1}).
$$

This is the second dimension: not a new element, but a **dependence of the threshold on information from above**.

**Formally.** Introduce a modulation parameter $m$:

$$
\delta_n(m)=\frac{u_n}{2}\bigl(1+m\,\Delta_{n+1}\bigr),
$$

where $m\in[0,1]$ is the coupling strength. For $m=0$—the original threshold; for $m>0$—the threshold shifts depending on the signal $\Delta_{n+1}$ from the upper level.

**Triadic interpretation.** This is exactly what $\mathcal O_n$ means in the triad $\mathcal L_n=(\mathcal O_n\mid C_n\mid\nu_n(C_n))$: the observer does not add elements to $C_n$ but **modulates the condition of distinction** at level $n$. The second dimension is the axis $\mathcal O_n$, orthogonal to the axis $C_n$.

**Scheme:**

$$
\underbrace{\mathcal A_n^G(u_n)}_{\text{datum}}
\;\xrightarrow{\ \Delta_{n+1}\ }\;
\underbrace{\delta_n(m)}_{\text{modulated threshold}}
\;\xrightarrow{\ m\ }\;
\underbrace{\mathcal A_{n+1}^G}_{\text{next level}}.
$$

**Properties:**
1. The lower level is not extended: $C_n$ remains the same.
2. The threshold becomes a function: $\delta_n=\delta_n(m)$.
3. The second dimension is the axis $m$, not a new sort of elements.
4. As $m\to0$ the original algebra is restored; as $m\to1$—maximal coupling.

**Corollary.** A second dimension does not require extending the lower levels. It requires only a modulation of the threshold—that is, a dependence of $\delta_n$ on $\Delta_{n+1}$. This is the minimal variant consistent with the triad: the observer modulates the distinction without adding data.

---

## Q19. What does this give for the "animation" of the algebra?

**Answer.** This is precisely the mechanism of "animation": the algebra ceases to be static, because its thresholds depend on signals coming from above.

First, let us recall two notions.

**Interface.** The interface between layers $k$ and $k+1$ is the space of admissible maps

$$
\mathcal M^{(k)}=\{\,\varphi:C^{(k+1)}\to C^{(k)}\mid \varphi\text{ is consistent with the norm, threshold and signature}\,\}.
$$

The elements of the interface are not numbers and not coefficients, but **maps**. This is the sort $E\to E$, not the sort $E$.

**Tower.** The tower is the alternation of algebras and interfaces:

$$
\mathcal A^{(1)}\;\xrightarrow{\ \mathcal M^{(1)}\ }\;\mathcal A^{(2)}\;\xrightarrow{\ \mathcal M^{(2)}\ }\;\mathcal A^{(3)}\;\to\;\dots
$$

where each $\mathcal A^{(k)}$ is an atomic algebra of type $x/(u-x)$, and each $\mathcal M^{(k)}$ is the interface between adjacent algebras. The depth of the tower $L$ is the number of levels up to the first trivial interface.

Now—static and modulated algebras.

**Static algebra:** one level, one threshold, one distinction. It does not change—it simply is.

**Modulated algebra:** the threshold $\delta_n$ depends on $\Delta_{n+1}$, which depends on $\Delta_{n+2}$, and so on. Each level modulates the next through a signal. The algebra becomes a **process**, not a structure.

**Relation to flat extension.** A flat extension adds terms within a single level—the dimension does not change. Modulation of the threshold adds an **axis of dependence**—the dimension grows. This is vertical growth: not more of the same, but **something else**.

**Criterion of "life".** The tower is "alive" as long as the interfaces are nontrivial: $c_k\neq0$, where $c_k$ is the "curvature" of the interface $\mathcal M^{(k)}$ (a measure of its inhomogeneity). When the interface is trivial ($c_k=0$), the tower terminates—the algebra "freezes" at that level. Modulation of the threshold is precisely the nontriviality of the interface: $\delta_n$ depends on $\Delta_{n+1}$, hence $c_n\neq0$. That is why "life" = nontriviality of the interface: as long as the signal from above changes the threshold below, the tower works as a process; when the signal ceases to influence, the tower becomes a static structure.

**The shift-free atom is universal.** The atom $x/(u-x)$ contains no shift. Shift arises as a transition between levels, not as a term. That is why the tower is "alive": it contains no shift, yet generates it as an act at every step. Modulation of the threshold is the way in which the act of transition influences the lower level without adding terms to it.

**Summary:**

$$
\boxed{
\begin{aligned}
&\text{Interface: space of maps between layers; tower: alternation of algebras and interfaces.}\\
&\text{Flat extension: more terms, same dimension, statics.}\\
&\text{Threshold modulation: }\delta_n=\delta_n(\Delta_{n+1})\text{ --- a second dimension without extension.}\\
&\text{"Animation" = modulation: each level influences the threshold of the lower one via }\Delta.\\
&\text{Criterion of "life": the interface is nontrivial }(c_k\neq0)\text{; otherwise the tower "freezes".}
\end{aligned}}
$$

The algebra "comes alive" not because new elements were added to it, but because its thresholds have become **dependent on signals from above**. This is the minimal change consistent with the triad: the observer modulates the distinction without adding data. And this is precisely what turns the tower into a process rather than a structure.

---

## Q20. How can such algebras be used already today?

**Answer.** Such algebras can be used as **objects in the shift algebra**. That is, define an object by an atomic algebra, and measure its external parameters in the shift algebra. A combination is born—a hybrid structure in which the atomic algebra provides the internal constitution of the object, and the shift algebra provides its behaviour in the external space of parameters.

**Scheme.** Let $\mathcal A_u$ be the atomic algebra with parameter $u$, and $\mathcal S_\sigma$ the shift algebra with operation $\sigma(x)=x+1$. Then the object

$$
\mathcal O=(\mathcal A_u;\ \mathcal S_\sigma)
$$

is defined as follows:
- **internal constitution** is given by $\mathcal A_u$: atom $x/(u-x)$, threshold $u/2$, governing term $\Delta(x)=u-x/(u-x)$;
- **external parameters** are measured in $\mathcal S_\sigma$: shift $\sigma$, normalization, iterations.

**What this gives.** The atomic algebra answers the question "how is the object constituted"; the shift algebra—"how does the object behave under a transition to the next". Together they give a **two-layer description**: internal (atomic) and external (shift).

**Example: the KMR atom.** In the KMR framework, the atom $A/(1+KA)$ is an object whose internal constitution is given by the atomic algebra $\mathcal A_u$ with $u=1$, and whose external behaviour is given by the iterations $\odot$ and $\oslash$, i.e. by the shift algebra. The combination

$$
\mathcal O_{\mathrm{KMR}}=(\mathcal A_1;\ \mathcal S_{\odot,\oslash})
$$

gives a complete description: atom $x/(1-x)$ inside, iterations outside.

**Example: the curvature atom.** In $S_{00024}$, the object is given by the atomic algebra $A_{u(k)}$ with $u(k)=1-\cos_k(2\alpha)$, and its external behaviour is given by shift in the curvature space $k$. The combination

$$
\mathcal O_{\mathrm{curv}}=(\mathcal A_{u(k)};\ \mathcal S_k)
$$

gives the curvature generalization: atom with parameter $u(k)$ inside, shift in $k$ outside.

**Why this works.** The atomic algebra is **shift-free**: it contains no $\sigma$. The shift algebra is **division-free**: it contains no atom $x/(u-x)$. The combination supplies what is missing in each taken separately:

$$
\mathcal A_u\ \text{gives division and threshold},\qquad
\mathcal S_\sigma\ \text{gives shift and iteration}.
$$

Together—a complete structure.

**Formally.** The combination is a fibration

$$
\pi:\ \mathcal S_\sigma\;\longrightarrow\;\mathcal A_u,
$$

where the fibre over a point $a\in\mathcal A_u$ is the orbit of $a$ under the action of $\sigma$. The internal constitution is the base; the external behaviour is the fibre. This is precisely the fibred tower discussed in Q19, but with two levels: $\mathcal A_u$ and $\mathcal S_\sigma$.

**Properties of the combination:**
1. The internal parameters of the object (atom, threshold, $\Delta$) are given by $\mathcal A_u$.
2. The external parameters (shift, iteration, normalization) are given by $\mathcal S_\sigma$.
3. The object $\mathcal O=(\mathcal A_u;\mathcal S_\sigma)$ is a fibration, not a product: the fibre depends on the point of the base.
4. For $u=1$ the object reduces to the KMR atom; for $u=u(k)$—to the curvature atom.

**Summary:**

$$
\boxed{
\begin{aligned}
&\text{Object = (atomic algebra inside; shift algebra outside).}\\
&\mathcal O=(\mathcal A_u;\ \mathcal S_\sigma):\quad
\mathcal A_u\text{ gives constitution, }\mathcal S_\sigma\text{ gives behaviour.}\\
&\text{Combination --- fibration }\pi:\mathcal S_\sigma\to\mathcal A_u;\text{ fibre = orbit under }\sigma.\\
&\text{Examples: KMR atom }(\mathcal A_1;\mathcal S_{\odot,\oslash}),\ \text{curvature }(\mathcal A_{u(k)};\mathcal S_k).\\
&\text{For }u=1\text{ --- KMR; for }u=u(k)\text{ --- curvature atom.}
\end{aligned}}
$$

Such algebras can be used already today: define an object by an atomic algebra, and measure its external parameters in the shift algebra. A **combination** is born—a two-layer description in which the atomic algebra is responsible for the internal constitution (division, threshold, governing term), and the shift algebra for the external behaviour (shift, iteration, normalization). This is not a replacement of one algebra by another, but their **conjugation**: base and fibre, internal and external, constitution and behaviour.

## Q21. Does atomic algebra compete with Łukasiewicz, Post, intuitionistic, or quantum logic?

**Answer.** No. These are different types of objects solving different problems. The comparison is not "apples to apples", and the honest way to state the relation is: atomic algebra **adds an axis** that these logics do not have, rather than replacing them.

**Łukasiewicz and Post: flat extensions.**

Łukasiewicz logic $\mathbf{L}_n$ has truth values $\{0,\tfrac{1}{n-1},\dots,1\}$ and negation $\neg x=1-x$. Post logic $\mathbf{P}_m$ has values $\{0,1,\dots,m-1\}$ and cyclic negation $\neg x=x+1\pmod m$.

Both are **flat extensions** in a precise sense: they add truth values to the carrier, but the unit and the negation are **fixed**. There is no mechanism that changes the unit in response to information from above. In the notation of atomic algebra, Łukasiewicz is the case $u=1$ with a **frozen** unit and **no modulation**. Post is even further: its cyclic negation is an iteration of shift, not a duality $u-x$.

So the relation is:

- Łukasiewicz negation $\neg x=1-x$ is the **duality component** $\partial_u(x)=u-x$ of the atomic algebra at $u=1$;
- atomic algebra **uses** this duality, but adds what Łukasiewicz does not have: a regulated unit and generated levels;
- Post's cyclic negation is closer to shift than to division; it is a different construction altogether.

The word "flat" is exact: these logics extend the carrier without generating new levels. The levels are **given**, not produced by a threshold.

**Intuitionistic logic: levels, but given.**

Intuitionistic logic does have a level structure—Kripke models, partial order of worlds, the Brouwer–Heyting–Kolmogorov reading. But these levels are **given** by the model, not **generated** by a threshold of distinguishability. There is no operation $C_{n+1}=C_n\cup\{\nu(C_n)\}$ that produces the next level; the levels are part of the semantics from the start.

So intuitionistic logic is not "flat" in the same sense as Łukasiewicz, but it is also not "tower-like" in the sense of atomic algebra: it has levels, but they are data, not products.

**Quantum logic: a different axis.**

Quantum logic (orthomodular lattices, the logic of quantum propositions) addresses **non-commutativity**—the failure of distributivity in the lattice of projections. This is orthogonal to the axis "unit–threshold–modulation". Quantum logic does not ask "how is the unit assigned?" or "how does the threshold distinguish $x$ from $\mathrm{NOT}(x)$?" It asks "what is the lattice of propositions when observables do not commute?"

Atomic algebra and quantum logic do not compete because they address different questions. One could imagine a combination—non-commutative atomic algebra—but that is a separate project, not a competition.

**What atomic algebra actually adds.**

The axis that Łukasiewicz, Post, and intuitionistic logic do not have is **modulation of the unit**:

- in Łukasiewicz and Post, $u$ is fixed;
- in intuitionistic logic, the level structure is fixed by the model;
- in atomic algebra, $u$ is a **parameter** that can be modulated by a signal from above: $\delta_n=\delta_n(\Delta_{n+1})$.

This is the second dimension discussed in Q18: not a new truth value, but a **dependence of the threshold on information from above**. None of the competing logics has this axis.

**Honest limitations.**

Atomic algebra does **not** replace these logics in their own domains:

- it does not solve Łukasiewicz's problem (many-valued semantics with a fixed t-norm);
- it does not solve the intuitionistic problem (constructivity, BHK semantics);
- it does not solve the quantum-logic problem (non-commutativity, orthomodularity).

It adds an axis—modulation of the unit—that these logics do not have. This is not a competition; it is a **complement**. The skeptical objection "there are already powerful non-Boolean logics" is correct as a statement about those logics, but it does not apply to atomic algebra, because atomic algebra is not trying to be a non-Boolean logic in their sense. It is trying to be a **generated** algebra with a modulated unit.

**In one sentence:** Łukasiewicz and Post are flat extensions with a frozen unit; intuitionistic logic has given levels; quantum logic addresses an orthogonal axis; atomic algebra adds a modulated unit and generated levels—an axis none of them has.

## Conclusion

The atomic algebra is an attempt to build algebra from below—from the division atom and the distinguishability threshold—rather than from above, from a fixed Boolean unit. Its main advantages are: an adjustable unit, a secondary shift, and an explained hierarchy. Boolean algebra appears as the normalized limit with a frozen unit, not as the only possible algebra.

The **proven core** is complete for the main thesis:

- relative atomicity: $A_u$ is not definable in $\Sigma_0$ for any $u$;
- definability in $\Sigma_3^+$, with the value $\varepsilon/(u-\varepsilon)$ at $x=e$;
- primacy of division in the order of signatures: $\sigma\notin\Sigma_3^+$;
- uniqueness in the Möbius class with $f(0)=0$, a pole at $u$, and $f(\varepsilon)=\varepsilon/(u-\varepsilon)$.

Beyond the core lie **extensions**, not gaps:

- *absolute* primacy of the atom requires a separate theory of term complexity; the main thesis does not need it;
- the status of $e/e$ depends on the choice of syntax—standard or linear; the order-of-signatures theorem holds in either;
- the full classification of Möbius generators is a completeness question, not a correctness question; uniqueness in the relevant class is already proved.

In short: the foundation is proven; what remains open are stronger claims that the foundation does not depend on. The approach does not replace Boolean algebra—it explains it as a normalized limit distinguished by a frozen unit.
