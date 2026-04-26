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
- 
## Repository Structure
```text
.
├── kmr_paper.md                            # Core theory: primary exposition (Sections 1-8)
├── kmr_extension_to_fractional.md          # Extension to Fractional Compositions (Section 9)
├── kmr_arithmetic_addition_subtraction.md  # Extension to arithmetic: addition and subtraction (Section 10)
├── kmr_chain_notation_convention.md        # Chain Notation and Left-Associativity Convention (Section 12)
├── kmr_tunneling_extraction.md             # Tunneling Property and Element Extraction in KMR Chains (Section 11)
├── kmr_formulas_reference.md               # Properties and Formulas Reference (handbook)
├── kmr_operations.py                       # Core KMR operations implementation
├── kmr_chains.py                           # Abstract chain space implementation
├── kmr_chains_operations_by_id.py          # Chain space ID-based chain operations
├── kmr_chains_operations_func.py           # Chain space functional operations extension
├── kmr_chains_operations_init.py           # Chain space operations initialization
├── kmr_prilosophical_KMR-L.md	            # Relational Ontology of KMR-L: An Interim Synthesis (Section 16)
├── kmr_tunneling.py                        # Tunneling and Extraction implementation
├── LICENSE-СС                              # License for THEORY (CC BY-SA 4.0)
├── LICENSE                                 # License for CODE (GPL 3.0)
├── tests/                                  # Framework tests
└── examples/                               # Usage examples
	├── example_usage.py                    # Core KMR operations example
	├── example_quick_start.py              # Chain space functional example
    ├── example_operations_by_id.py         # Chain space ID as value operations example
	├── example_extended_operations_by_id.py# Chain space ID as value operations extended example
    ├── example_functional_operations.py    # Chain space function as value operations example
    └── example_kmr_algebraic_properties.py # Algebraic properties verification by using functional chains example
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
- Pure mathematical formulation
- Complete algebraic properties
- Ready-to-use Python implementation
- Extensible operator framework

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

💡 Future Directions
- Applications in mathematical physics
- Connection to Möbius transformations
