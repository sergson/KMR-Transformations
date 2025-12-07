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
├── kmr_operations.py                       # Reference Python implementation
├── LICENSE-СС                              # License for THEORY (CC BY-SA 4.0)
├── LICENSE                                 # License for CODE (GPL 3.0)
├── tests/                                  # Framework tests
└── examples/                               # Usage examples for the Python module 
```

## 🚀 Quick Start
```python
from kmr_operations import kmr_direct, kmr_inverse

print(kmr_direct(2, 3))  # 0.2857 = 2 ⊙ 3
print(kmr_inverse(2, 3)) # -0.4   = 2 ⊘ 3
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
