======================================================================
                KMR ELEMENT EXTRACTION TEST SUITE v2.0                
             With CORRECTED formulas from updated theory              
======================================================================

======================================================================
       1. BASIC ELEMENT EXTRACTION FORMULAS (3-ELEMENT CHAINS)        
======================================================================

Description          A          B          C          Full Chain          
--------------------------------------------------------------------------------
Simple case          2.000      3.000      4.000      0.133333333333333   
Fractional elements  1.000      0.500      2.000      0.285714285714286   
Mixed fractions      0.500      2.000      0.250      0.235294117647059   
Negative element     10.000     -2.000     3.000      0.909090909090909   

Description          Extraction Method         Expected             Extracted            Diff            Status    
------------------------------------------------------------------------------------------------------------------------
Simple case          First (A)                 2.000000000000000    1.999999999999999    6.66e-16        PASS      
Simple case          Intermediate (B)          3.000000000000000    3.000000000000000    0.00e+00        PASS      
Simple case          Last (C)                  4.000000000000000    4.000000000000000    0.00e+00        PASS      
                     -                         -                    -                    -               -         
Fractional elements  First (A)                 1.000000000000000    1.000000000000000    4.44e-16        PASS      
Fractional elements  Intermediate (B)          0.500000000000000    0.500000000000000    4.44e-16        PASS      
Fractional elements  Last (C)                  2.000000000000000    2.000000000000000    4.44e-16        PASS      
                     -                         -                    -                    -               -         
Mixed fractions      First (A)                 0.500000000000000    0.500000000000000    0.00e+00        PASS      
Mixed fractions      Intermediate (B)          2.000000000000000    2.000000000000000    0.00e+00        PASS      
Mixed fractions      Last (C)                  0.250000000000000    0.250000000000000    0.00e+00        PASS      
                     -                         -                    -                    -               -         
Negative element     First (A)                 10.000000000000000   9.999999999999970    3.02e-14        PASS      
Negative element     Intermediate (B)          -2.000000000000000   -2.000000000000000   2.22e-16        PASS      
Negative element     Last (C)                  3.000000000000000    3.000000000000000    0.00e+00        PASS      
                     -                         -                    -                    -               -         

✅ Test 1 completed successfully

======================================================================
             2. LONG CHAIN EXTRACTION (4 AND 5 ELEMENTS)              
======================================================================

--- 4-Element Chain Test: 2 ⊙ 3 ⊙ 4 ⊙ 5 ---
Chain result X = 0.080000000000000

Element         Left Chain                Right Chain               Expected        Extracted       Status    
------------------------------------------------------------------------------------------------------------------------
A1              []                        [3.0, 4.0, 5.0]           2.000000        2.000000        ✓         
A2              [2.0]                     [4.0, 5.0]                3.000000        3.000000        ✓         
A3              [2.0, 3.0]                [5.0]                     4.000000        4.000000        ✓         
A4              [2.0, 3.0, 4.0]           []                        5.000000        5.000000        ✓         

--- 5-Element Chain Test: 2 ⊙ 3 ⊙ 4 ⊙ 5 ⊙ 6 ---
Chain result X = 0.054054054054054

Element         Extraction Method              Expected        Extracted       Diff            Status    
------------------------------------------------------------------------------------------------------------------------
A1              First element formula          2.000000        2.000000        6.66e-16        ✓         
A2              Intermediate: k=2              3.000000        3.000000        0.00e+00        ✓         
A3              Intermediate: k=3              4.000000        4.000000        0.00e+00        ✓         
A4              Intermediate: k=4              5.000000        5.000000        0.00e+00        ✓         
A5              Last element formula           6.000000        6.000000        0.00e+00        ✓         

✅ Test 2 completed successfully

======================================================================
              3. ARBITRARY ELEMENT EXTRACTION FROM CHAIN              
======================================================================

--- 5-Element Chain: 2 ⊙ 3 ⊙ 4 ⊙ 5 ⊙ 6 ---
Chain result X = 0.054054054054054

Element    Other Elements                           Expected        Extracted       Diff            Status    
------------------------------------------------------------------------------------------------------------------------
A1         [3.0, 4.0, 5.0, 6.0]                     2.000000        2.000000        6.66e-16        ✓         
A2         [2.0, 4.0, 5.0, 6.0]                     3.000000        3.000000        0.00e+00        ✓         
A3         [2.0, 3.0, 5.0, 6.0]                     4.000000        4.000000        0.00e+00        ✓         
A4         [2.0, 3.0, 4.0, 6.0]                     5.000000        5.000000        0.00e+00        ✓         
A5         [2.0, 3.0, 4.0, 5.0]                     6.000000        6.000000        0.00e+00        ✓         

✅ Test 3 completed successfully

======================================================================
                  4. EDGE CASES AND ERROR CONDITIONS                  
======================================================================

4.1 Zero and near-zero elements:

Zero element in middle: [2.0, 0.0, 3.0]
  X = 0.285714
  A1: expected=2.000000, extracted=2.000000, diff=6.66e-16, ✓
  A2: expected=0.000000, extracted=0.000000, diff=0.00e+00, ✓
  A3: expected=3.000000, extracted=3.000000, diff=0.00e+00, ✓

First element zero: [0.0, 3.0, 4.0]
  X = 0.000000
  A1: expected=0.000000, extracted=0.000000, diff=0.00e+00, ✓

First element zero: ERROR - Cannot compute 1/D: D=0.0 (too close to zero)

Last element zero: [2.0, 3.0, 0.0]
  X = 0.285714
  A1: expected=2.000000, extracted=2.000000, diff=6.66e-16, ✓
  A2: expected=3.000000, extracted=3.000000, diff=0.00e+00, ✓
  A3: expected=0.000000, extracted=0.000000, diff=0.00e+00, ✓

Small values: [0.1, 0.2, 0.3]
  X = 0.095238
  A1: expected=0.100000, extracted=0.100000, diff=1.39e-17, ✓
  A2: expected=0.200000, extracted=0.200000, diff=7.22e-16, ✓
  A3: expected=0.300000, extracted=0.300000, diff=1.05e-15, ✓

4.2 Division by zero/singularity cases:

A1 ⊙ A2 where 1 + A1*A2 = 0: [1.0, -1.0]
  X = nan

A1 ⊙ A2 where 1 + A1*A2 = 0: [1.0, -1.0]
  Expected error: ValueError: Cannot compute inverse at element -1.0

A1 ⊙ A2 where 1 + A1*A2 ≠ 0, but extraction might fail: [2.0, -0.5]
  X = nan

A1 ⊙ A2 where 1 + A1*A2 ≠ 0, but extraction might fail: [2.0, -0.5]
  Expected error: ValueError: Cannot compute inverse at element -0.5

✅ Test 4 completed successfully

======================================================================
                    5. VERIFICATION FUNCTION TEST                     
======================================================================

Standard 3-element chain: [2.0, 3.0, 4.0]
  A1_extraction: ✓ diff=6.66e-16
  A2_extraction: ✓ diff=0.00e+00
  A3_extraction: ✓ diff=0.00e+00
  A2_direct_extraction: ✓ diff=0.00e+00
  ✅ All extractions successful!

4-element chain: [2.0, 3.0, 4.0, 5.0]
  A1_extraction: ✓ diff=6.66e-16
  A2_extraction: ✓ diff=0.00e+00
  A3_extraction: ✓ diff=0.00e+00
  A4_extraction: ✓ diff=0.00e+00
  A2_direct_extraction: ✓ diff=0.00e+00
  A3_direct_extraction: ✓ diff=0.00e+00
  ✅ All extractions successful!

5-element chain: [2.0, 3.0, 4.0, 5.0, 6.0]
  A1_extraction: ✓ diff=6.66e-16
  A2_extraction: ✓ diff=0.00e+00
  A3_extraction: ✓ diff=0.00e+00
  A4_extraction: ✓ diff=0.00e+00
  A5_extraction: ✓ diff=0.00e+00
  A2_direct_extraction: ✓ diff=0.00e+00
  A3_direct_extraction: ✓ diff=0.00e+00
  A4_direct_extraction: ✓ diff=0.00e+00
  ✅ All extractions successful!

Fractional chain: [1.0, 0.5, 2.0, 0.25]
  A1_extraction: ✓ diff=4.44e-16
  A2_extraction: ✓ diff=4.44e-16
  A3_extraction: ✓ diff=4.44e-16
  A4_extraction: ✓ diff=4.44e-16
  A2_direct_extraction: ✓ diff=4.44e-16
  A3_direct_extraction: ✓ diff=4.44e-16
  ✅ All extractions successful!

✅ Test 5 completed successfully

======================================================================
               6. THEORETICAL CORRECTNESS VERIFICATION                
======================================================================

6.1 CORRECTED Formula for intermediate elements:
   A_k = 1/(X ⊘ A_n ⊘ A_{n-1} ⊘ ... ⊘ A_{k+1}) - 1/L
   where L = A1 ⊙ A2 ⊙ ... ⊙ A_{k-1} (computed sequentially)

6.2 Comparison with manual calculation:

Chain: [2.0, 3.0, 4.0, 5.0, 6.0]
X = 0.054054054054054

Extracting A3 = 4.0
  L = A1 ⊙ A2 = 2 ⊙ 3 = 0.285714285714286
  D = X ⊘ A5 ⊘ A4 = 0.054054 ⊘ 6 ⊘ 5 = 0.133333333333333
  A3_theoretical = 1/D - 1/L = 1/0.133333 - 1/0.285714
                 = 7.500000 - 3.500000
                 = 4.000000000000000

  Function result: 4.000000000000000
  Difference: 0.00e+00
  Match: True

✅ Test 6 completed successfully

======================================================================
                             TEST SUMMARY                             
======================================================================

✅ All extraction tests completed!

Key Findings (CORRECTED):
1. ✅ First element extraction: A1 = X ⊘ An ⊘ ... ⊘ A2
2. ✅ Last element extraction: An = 1/X - 1/Z where Z = A1 ⊙ ... ⊙ A_{n-1}
3. ✅ Intermediate element extraction (CORRECTED FORMULA):
   A_k = 1/(X ⊘ A_n ⊘ ... ⊘ A_{k+1}) - 1/(A1 ⊙ ... ⊙ A_{k-1})
4. ✅ Formula works for chains of ANY length (3, 4, 5, ...)
5. ✅ Non-associativity is handled by sequential computation

Important Note:
The old formula A_k = 1/(X ⊘ A_{k+1}) - 1/L only works when k = n-1
The corrected formula requires canceling ALL elements to the right.

Process finished with exit code 0