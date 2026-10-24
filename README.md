<!-- 
License: CC BY-SA 4.0 (см. LICENSE-CC.md) 
-->
# KMR Transformations Framework
## Licensing
- **Code**: Licensed under [GPL 3.0](LICENSE)
- **Theoretical content**: Licensed under [CC BY-SA 4.0](LICENSE-CC.md)

⚠️ Note: GitHub may automatically detect GPL 3.0 as the primary license,
but this applies only to source code files. All theoretical materials
are explicitly licensed under CC BY-SA 4.0.

## Core Operators
- **Direct (⊙)**: ` A ⊙ K ≔ (A/(1 + A) ∘ A/(1 + A) ... A/(1 + A)) K times ` 
- **Inverse (⊘)**: ` A ⊘ K ≔ (A/(1 - A) ∘ A/(1 - A) ... A/(1 - A)) K times `
- Structural universality is demonstrated as a further generalization to spaces of constant curvature, achieved through the decomposition of an "additional unit"—expressed analytically in such a way as to preclude any violation of this "additional unit."
- The expression $\(A \odot K = \frac{A}{1 + K A}\)$ is shown to represent a fundamental **computational atom**—an algebraic "building block" upon which various systems can be constructed, ranging from one-dimensional continuous flows to phase-dependent modulations and geometries defined by curvature. The KMR atom is presented as a structural invariant that maintains its stability.

## Repository Structure
```text
.
├── S_00001_00008_kmr_paper.md             			# Core theory: primary exposition (Sections 1-8)
├── S_00009_kmr_extension_to_fractional.md    		# Extension to Fractional Compositions (Section 9)
├── S_00010_kmr_arithmetic_addition_subtraction.md  # Extension to arithmetic: addition and subtraction (Section 10)
├── S_00011_kmr_tunneling_extraction.md	   		    # Tunneling Property and Element Extraction in KMR Chains (Section 11)
├── S_00012_kmr_chain_notation_convention.md   		# Chain Notation and Left-Associativity Convention (Section 12)
├── S_00014_kmr__arithmetic_multiplication_...md    # Multiplication and Division (Section 14)
├── S_00015_KRM_Ergodicity Proof.md		   		    # Ergodicity of the Continuous KMR Flow in Compact Spaces (Section 15)
├── S_00016_kmr_philosophical_KMR-L.md	            # Relational Ontology of KMR-L: An Interim Synthesis (Section 16)
├── S_00017_kmr_exponential_functions.md            # KMR Chains of Power Functions (Section 17)
├── S_00019_kmr_representation_of_zero.md           # KMR Representation of Zero and Subtraction
├── S_00018_kmr_squaring_examples_z_r.md            # Practical Examples of KMR Applications for Natural and Real Numbers (Section 18)
├── S_00019_kmr_representation_of_zero.md           # KMR Representation of Zero and Subtraction (Section 19)
├── S_00020_Relational_KMR_Basis.md                 # Relational KMR Basis: Chain Algebra and the Iterator Paradigm (Section 20)
├── S_00021_KMR_modulations.md                      # KMR Modulations: Cross-Chain Dynamics in 2D and 3D (Section 21)
├── S_00022_KMR_trigonometry.md                     # Complex KMR Continuation: The Genesis of Trigonometry (Section 22)
├── S_00023_kmr_continuous_phase_atom.md            # Continuous Phase Atom: Deconstruction of Unity and Gauge-Balanced Dualities (Section 23)
├── S_00024_kmr_curvature_atom.md                   # Curvature Generalization of the Continuous Phase Atom: The Persistent Unity (Section 24)
├── S_00025_primacy_of_division.md                  # Primacy of Division (Section 25)
├── S_00026_atomic_algebra.md                       # Atomic Algebra (Section 26)
├── S_00027_Atomic_Algebra_FAQ.md                   # Atomic Algebra: Questions and Answers on the Advantages of the Approach (Section 26)
├── kmr_formulas_reference.md       		        # Properties and Formulas Reference (handbook)
├── LICENSE-СС                  		            # License for THEORY (CC BY-SA 4.0)
├── LICENSE                      		            # License for CODE (GPL 3.0)
├── src/											# Source code for KMR
│	├── kmr_operations.py               		    # Core KMR operations implementation
│	├── kmr_chains.py                    	  	    # Abstract chain space implementation
│	├── kmr_chains_operations_by_id.py    			# Chain space ID-based chain operations
│	├── kmr_chains_operations_func.py   			# Chain space functional operations extension
│	├── kmr_chains_operations_init.py    			# Chain space operations initialization
│	├── kmr_tunneling.py                  			# Tunneling and Extraction implementation
├── tests/                              		    # Framework tests
│	├──algebra_test_suite.py						# Demonstrating KMR operator algebra and comparing it with classical
│	├──algebra_test_suite.md						# Results of test KMR operator algebra and comparing it with classical
│	├──extraction_test_suite.py						# Comprehensive test suite for KMR element extraction functions
│	├──extraction_test_suite.md						# Results of comprehensive test suite for KMR element extraction functions
│	├──tunneling_test_suite.py						# Test suite for KMR tunneling operations through KMRChainSpace
│	├──tunneling_tests_suite.md						# Results of test suite for KMR tunneling operations through KMRChainSpace
└── examples/                           		    # Usage examples
	├── example_usage.py                		    # Core KMR operations example
	├── example_quick_start.py          		    # Chain space functional example
    ├── example_operations_by_id.py     		    # Chain space ID as value operations example
	├── example_extended_operations_by_id.py		# Chain space ID as value operations extended example
    ├── example_functional_operations.py    		# Chain space function as value operations example
    └── example_kmr_algebraic_properties.py 		# Algebraic properties verification by using functional chains example
```


## 🚀 Quick Start

### Basic Operations   
```python
from kmr_operations import kmr_direct, kmr_inverse

print(kmr_direct(2, 3))  # 0.2857 = 2 ⊙ 3
print(kmr_inverse(2, 3)) # -0.4   = 2 ⊘ 3
```


### Chain Space Operations   
```python
from kmr_chains import get_default_space, add_element
from kmr_chains_operations_init import initialize_all_operations

# Initialize all operations
space = get_default_space()
initialize_all_operations(space)

# Create a functional chain
start_id = add_element('identity', lambda x: x)
f_id = add_element('⊙f', 2, parent_id=start_id)

# Evaluate at different points
from kmr_chains_operations_func import evaluate_function_chain
print(f"f(1) = {evaluate_function_chain(f_id, space, 1):.3f}")  # 0.333
```


## Key Features
- Iterator Paradigm: The basis elements are not points, but scale-sensitive operators (chain steps).
- Exact Closed Forms: Nonlinear 1D flows and power functions collapse into exact rational expressions via Abel's isomorphism.
- Algebraic Rigor: Full classification of parabolic Abelian dynamics (2D/3D modulations) and their boundaries.
- Ready-to-use Python Implementation: Pure mathematical formulation with extensible operator framework.
- **Continuous Phase Atom**: The discrete switch $\odot/\oslash$ is replaced by a smooth phase rotation, where the sign-based modulation parameter $B$ governs duality, and the scaling scalar $D$ regulates the computations.
- **Curvature Atom**: Generalization to spaces of constant curvature $\(k\)$, where the unit $\(1\)$ is deformed as $\(1 - \cos_k(2\alpha)\)$, naturally producing elliptic $(\(k=1\))$, parabolic $(\(k=0\))$, and hyperbolic $(\(k<0\))$ regimes while preserving recursive unfolding.
- **Primacy of Division**: Confirming the atomicity of KMR operations by proving that division takes precedence over shifting
- **Atimic algebra**: Introduction to the polymorphic atom and non-shift algebra.

## Acronym Interpretations
KMR may represent:
- **K**-cascaded Möbius Reduction
- **K**-ordered Metric Rescaling  
- **K**-modulated Relational operator

## License
This work is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).

## Citing This Work
```bibtex
@software{KMR-Transformations,
  author = {Terikhov, Sergei},
  title = {KMR Transformations Framework},
  year = {2025},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/sergson/KMR-Transformations}}}```
