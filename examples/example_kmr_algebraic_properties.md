
=== KMR Algebraic Properties Demonstration ===

=== Property 1: Group Property ===
Testing: (A ⊙ K) ⊙ C = A ⊙ (K + C)

Left side: (A ⊙ 2) ⊙ 3
Right side: A ⊙ (2 + 3) = A ⊙ 5

Verification:
A=1: (1 ⊙ 2) ⊙ 3 = 0.166667, 1 ⊙ 5 = 0.166667, Match: True
A=2: (2 ⊙ 2) ⊙ 3 = 0.181818, 2 ⊙ 5 = 0.181818, Match: True
A=3: (3 ⊙ 2) ⊙ 3 = 0.187500, 3 ⊙ 5 = 0.187500, Match: True
A=5: (5 ⊙ 2) ⊙ 3 = 0.192308, 5 ⊙ 5 = 0.192308, Match: True
A=10: (10 ⊙ 2) ⊙ 3 = 0.196078, 10 ⊙ 5 = 0.196078, Match: True


=== Property 2: Duality ===
Testing: A ⊙ K = A ⊘ (-K)

Left side: A ⊙ 2
Right side: A ⊘ (-2)

Verification:
A=1: 1 ⊙ 2 = 0.333333, 1 ⊘ -2 = 0.333333, Match: True
A=2: 2 ⊙ 2 = 0.400000, 2 ⊘ -2 = 0.400000, Match: True
A=3: 3 ⊙ 2 = 0.428571, 3 ⊘ -2 = 0.428571, Match: True
A=5: 5 ⊙ 2 = 0.454545, 5 ⊘ -2 = 0.454545, Match: True
A=10: 10 ⊙ 2 = 0.476190, 10 ⊘ -2 = 0.476190, Match: True


=== Property 3: Inversion Identity ===
Testing: (A ⊙ K) ⊘ K = A

Left side: (A ⊙ 2) ⊘ 2

Verification (should return original A):
A=1: (1 ⊙ 2) ⊘ 2 = 1.000000, Match with A: True
A=2: (2 ⊙ 2) ⊘ 2 = 2.000000, Match with A: True
A=3: (3 ⊙ 2) ⊘ 2 = 3.000000, Match with A: True
A=5: (5 ⊙ 2) ⊘ 2 = 5.000000, Match with A: True
A=10: (10 ⊙ 2) ⊘ 2 = 10.000000, Match with A: True


=== Property 4: Scaling Property ===
Testing: λ·(A ⊙ K) = (λA) ⊙ (K/λ)
Let λ=3, K=2

Verification:
A=1: 3*(1 ⊙ 2) = 1.000000, (3*1) ⊙ (2/3) = 1.000000, Match: True
A=2: 3*(2 ⊙ 2) = 1.200000, (3*2) ⊙ (2/3) = 1.200000, Match: True
A=3: 3*(3 ⊙ 2) = 1.285714, (3*3) ⊙ (2/3) = 1.285714, Match: True
A=5: 3*(5 ⊙ 2) = 1.363636, (3*5) ⊙ (2/3) = 1.363636, Match: True
A=10: 3*(10 ⊙ 2) = 1.428571, (3*10) ⊙ (2/3) = 1.428571, Match: True


=== Property 5: Correct Chain Composition ===
Testing: (A ⊙ K) ⊙ C = A / (1 + A*K + A*C)
This is the same as A ⊙ (K + C) by group property

This property was already verified in Property 1.


=== Property 6: Tunneling Property ===
Testing: Y ⊙ X ⊘ Y⁻¹ = X⁻¹

Left side: 2 ⊙ 3 ⊘ 2⁻¹

Result should be 1/3 ≈ 0.3333...
Result: 0.333333, Expected: 0.333333, Match: True


=== Property 7: Arithmetic via KMR (Addition) - Fixed ===
Testing: K + C = (((A ⊙ K) ⊙ C) ⊘ A⁻¹)⁻¹

For A=2, K=3, C=4, we should get K+C=7

Creating reciprocal function safely...

Computing step by step:
2 ⊙ 3 = 0.285714
(2 ⊙ 3) ⊙ 4 = 0.133333
((2 ⊙ 3) ⊙ 4) ⊘ 0.5 = 0.142857
Reciprocal of above = 7.000000
Expected K+C = 3+4 = 7, Match: True


=== Property 8: Decomposition Theorem ===
Testing: A ⊙ (K·(D + F)) = (A ⊙ (K·D)) ⊙ (K·F)
Let A=1, K=2, D=3, F=4

Verification:
Left: 1 ⊙ 14 = 0.066667
Right: (1 ⊙ 6) ⊙ 8 = 0.066667
Match: True

=== Summary ===
All properties verified successfully!
Total elements created: 33

Process finished with exit code 0