=== Example 1: Creating simple functional chains ===
Created chain for f(A) = A ⊙ 2
Element ID: dee96dcefd3a6d32...
f(1) = 0.333
f(2) = 0.400
f(5) = 0.455

=== Example 2: Using predefined functions ===
Created square function
Created chain for g(A) = A^2 ⊙ 3
g(1) = 0.250
g(2) = 0.308
g(3) = 0.321

=== Example 3: Chain of KMR transformations ===
Created chain for h(A) = A ⊙ 2 ⊙ 3 ⊙ 4
h(1) = 0.100
h(2) = 0.105

=== Example 4: Using string expressions ===
Created chain for p(A) = A^2 + 2A + 1
p(0) = 1.000
p(1) = 4.000
p(2) = 9.000

=== Example 5: Function composition ===
Created chain for r(A) = sin(A^2)
r(0) = 0.000
r(π/2) = 1.000

=== Example 6: Arithmetic with functions ===
Created sum function: f(x) = x^2 + x
sum(2) = 6.000
Created product function: f(x) = x^2 * x = x^3
product(2) = 8.000

=== Example 7: Extracting and using functions ===
Type of f_func: <class 'function'>
Is callable: True
Direct call f_func(3): 0.429
Direct call f_func(10): 0.476

Helper kmr_func(3): 0.429
Helper kmr_func(10): 0.476

=== Example 8: Complex KMR chain (Fixed - avoiding singularity) ===
Created chain for f(A) = (A ⊙ 2) ⊘ 1.5
f(1) = 0.667
f(2) = 1.000
f(0.5) = 0.400

=== Example 9: Mixed operations ===
Created chain for f(A) = ((A ⊙ 2) + 1) * 3
f(1) = 4.000
f(2) = 4.200

=== Example 10: Using reciprocal function ===
Created reciprocal function: f(x) = 1/x
recip(1) = 1.000
recip(2) = 0.500
recip(4) = 0.250

=== Example 11: Demonstrating singularities ===

Demonstrating singularity in inverse KMR operator:
For f(x) = x ⊘ K, singularity occurs when x * K = 1

Values approaching singularity for f(x) = x ⊘ 3:
f(0.2) = 0.5000000000000001
f(0.3) = 2.9999999999999973
f(0.33) = 32.99999999999997
f(0.333) = 333.0000000000367
f(0.35) = -7.000000000000025
f(0.4) = -1.9999999999999984

=== Example 12: Safe chain with no singularities ===
Created safe chain: f(x) = ((x ⊙ 0.5) + 2) ⊙ 1.5
f(0) = 0.500
f(1) = 0.533
f(2) = 0.545
f(5) = 0.558
f(10) = 0.564

=== Summary ===
Total elements in space: 30
All operations completed successfully!

Process finished with exit code 0
