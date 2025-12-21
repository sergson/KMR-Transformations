🚀 INITIALIZING KMR CHAIN SPACE WITH ID OPERATIONS
------------------------------------------------------------
✓ Default space created: KMRChainSpace(elements=0)
✓ ID operations registered
  - Handlers: ['⊙id', '⊘id', '+id', '-id', '*id', '/id']
  - Aliases: 20 entries

🔗 CREATING CHAIN A: A1 ⊙ 2 ⊙ 3 ⊙ 4
----------------------------------------
  Created A1: ID=d2beef37..., value=2, operation=⊙
  Created A2: ID=df006af0..., value=3, operation=⊙, parent=d2beef37...
  Created A3: ID=2a035a9b..., value=4, operation=⊙, parent=df006af0...
  Chain A complete: d2beef37... → df006af0... → 2a035a9b...

🔗 CREATING CHAIN B: B1 ⊙ 1.5 ⊙ 2 ⊙ 3
----------------------------------------
  Created B1: ID=7f3875c7..., value=1.5, operation=⊙
  Created B2: ID=5abe7494..., value=2, operation=⊙, parent=7f3875c7...
  Created B3: ID=e88d1bfb..., value=3, operation=⊙, parent=5abe7494...
  Chain B complete: 7f3875c7... → 5abe7494... → e88d1bfb...

➕ CREATING ID OPERATIONS (COMBINING CHAINS)
----------------------------------------
  Created SUM: ID=e9ccd60b..., value=ref:e88d1bfb..., operation=+id, parent=2a035a9b...
    Operation: Chain A result + Chain B result (via reference)
  Created MUL: ID=6e887a03..., value=ref:e88d1bfb..., operation=*id, parent=2a035a9b...
    Operation: Chain A result × Chain B result (via reference)
  Created KMR: ID=15598258..., value=ref:e88d1bfb..., operation=⊙id, parent=2a035a9b...
    Operation: Chain A result ⊙ Chain B result (via reference)

🎯 ENHANCED CHAIN GRAPH WITH VALUES:
================================================================================
└── d2beef37... [⊙ 2]
        Before: 1.000000 → After: 0.333333
    └── df006af0... [⊙ 3]
            Before: 0.333333 → After: 0.166667
        └── 2a035a9b... [⊙ 4]
                Before: 0.166667 → After: 0.100000
            ├── e9ccd60b... [+id ref:e88d1bfb...]
                    Before: 0.100000 → After: 0.233333
            ├── 6e887a03... [*id ref:e88d1bfb...]
                    Before: 0.100000 → After: 0.013333
            └── 15598258... [⊙id ref:e88d1bfb...]
                    Before: 0.100000 → After: 0.098684

└── 7f3875c7... [⊙ 1.500000]
        Before: 1.000000 → After: 0.400000
    └── 5abe7494... [⊙ 2]
            Before: 0.400000 → After: 0.222222
        └── e88d1bfb... [⊙ 3]
                Before: 0.222222 → After: 0.133333

🔗 CHAIN CONNECTIONS (with branching):
--------------------------------------------------
Chain 1: [ROOT:d2beef37...] → [df006af0...] → [2a035a9b...] 
       [BRANCH 1/3] → [e9ccd60b...]
Chain 2: [ROOT:d2beef37...] → [df006af0...] → [2a035a9b...] 
       [BRANCH 2/3] → [6e887a03...]
Chain 3: [ROOT:d2beef37...] → [df006af0...] → [2a035a9b...] 
       [BRANCH 3/3] → [15598258...]
Chain 4: [ROOT:7f3875c7...] → [5abe7494...] → [e88d1bfb...]

📊 BRANCHING ANALYSIS:
--------------------------------------------------
  Branching at 2a035a9b...:
    Number of branches: 3
    Branch 1: → e9ccd60b... (operation: +id)
    Branch 2: → 6e887a03... (operation: *id)
    Branch 3: → 15598258... (operation: ⊙id)

🔄 CONVERGENCE POINTS (if any):
--------------------------------------------------
  No convergence points (tree structure)

📊 FINAL RESULTS
============================================================
🔗 Chain A (A1⊙2⊙3⊙4): 0.100000
   A1 = 2
   A2 = 3 (A1⊙2 = 0.333333 ⊙ 3)
   A3 = 4 (A2⊙3 = 0.166667 ⊙ 4)

🔗 Chain B (B1⊙1.5⊙2⊙3): 0.133333
   B1 = 1.5
   B2 = 2 (B1⊙1.5 = 0.400000 ⊙ 2)
   B3 = 3 (B2⊙2 = 0.222222 ⊙ 3)

➕ Sum (A+B via +id): 0.233333
   = 0.100000 + 0.133333
   Verification: 0.233333

✖️ Product (A×B via *id): 0.013333
   = 0.100000 × 0.133333
   Verification: 0.013333

⊙ KMR(A,B via ⊙id): 0.098684
   = 0.100000 ⊙ 0.133333
   = 0.100000 / (1 + 0.133333 * 0.100000)

✅ OPERATION VERIFICATION
----------------------------------------
Chain A consistency check:
  [d2beef37...]: ✗ Inconsistent
  [df006af0...]: ✓ Consistent
  [2a035a9b...]: ✓ Consistent

Chain B consistency check:
  [7f3875c7...]: ✗ Inconsistent
  [5abe7494...]: ✓ Consistent
  [e88d1bfb...]: ✓ Consistent

ID operations consistency check:
  SUM [e9ccd60b...]: ✓ Consistent
  MUL [6e887a03...]: ✓ Consistent
  KMR [15598258...]: ✓ Consistent

============================================================
🎉 EXAMPLE COMPLETED SUCCESSFULLY!
============================================================