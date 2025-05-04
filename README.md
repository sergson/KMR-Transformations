<!-- 
Лицензия: CC BY-SA 4.0 (см. LICENSE-CC.md) 
-->
# KMR Transformations Framework
## Licensing
- **Code**: Licensed under [GPL 3.0](LICENSE)
- **Theoretical content**: Licensed under [CC BY-SA 4.0](LICENSE-CC.md)

⚠️ Note: GitHub may automatically detect GPL 3.0 as the primary license,
but this applies only to source code files. All theoretical materials
are explicitly licensed under CC BY-SA 4.0.

## Core Operators
- **Direct (⊙)**: `A ⊙ B ≔ A/(1 + AB)`
- **Inverse (⊘)**: `A ⊘ B ≔ A/(1 - AB)`

## Repository Structure
.
├── kmr_paper.md # Primary mathematical exposition
├── kmr_operations.py # Python implementation
├── LICENSE # CC BY-SA 4.0 license
└── examples/ # Usage examples

## 🚀 Quick Start
```python
from kmr_operations import kmr_direct, kmr_inverse

print(kmr_direct(2, 3))  # 0.2857 = 2 ⊙ 3
print(kmr_inverse(2, 3)) # -1.0   = 2 ⊘ 3
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
@software{Terikhov_KMR_2023,
  author = {Terikhov, Sergei},
  title = {KMR Transformations Framework},
  year = {2023},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/sergson/KMR-Transformations}}}```

💡 Future Directions
- Applications in mathematical physics
- Connection to Möbius transformations