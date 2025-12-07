"""
KMR Operator Algebra
Version: 1.0.0
License: GPL 3.0
"""
__author__ = "Sergei Terikhov"

import kmr_operations as kmr

"""
KMR Operations Demo

Examples:
    >>> kmr.kmr_direct(2, 3)
    0.2857142857142857
    >>> kmr.kmr_inverse(2, 3)
    -1.0
"""
if __name__ == "__main__":
    """
    KMR Transformations
    """
    print(f"2 ⊙ 3 = {kmr.kmr_direct(2, 3):.4f}")
    print(f"2 ⊘ 3 = {kmr.kmr_inverse(2, 3):.4f}")
    print(f"2 ⊙ 1 = {kmr.kmrd(2):.4f}")
    print(f"2 ⊘ 1 = {kmr.kmri(2):.4f}")
    print(f"2 ⊙ 3 = {kmr.kmr_dircly(2, 3):.4f}")
    print(f"2 ⊘ 3 = {kmr.kmr_invly(2, 3):.4f}")

    """
    KMR Arithmetic +/-
    """
    # Handle A = 1
    print(f"A=1,(3 + 2) = {kmr.kmr_add(1, 3, 2):.4f}")
    print(f"A=1,(3 - 2) = {kmr.kmr_sub(1, 3, 1):.4f}")
    print(f"A=1,(3.14 + 2.72) = {kmr.kmr_add(1, 3.14, 2.72):.4f}")
    print(f"A=1,(3.14 - 2.72) = {kmr.kmr_sub(1, 3.14, 2.72):.4f}")
    print(f"A=1,(-3.14 + 2.72) = {kmr.kmr_add(1, -3.14, 2.72):.4f}")
    print(f"A=1,(2.72 - 3.14)  = {kmr.kmr_sub(1, 2.72, 3.14):.4f}")

    # Handle precise if A = 1
    print(f"A=1,(3.14 + 3.14) = {kmr.kmr_add(1, 3.14, 3.14):.30f}")
    print(f"A=1,(2.72 - 2.72)  = {kmr.kmr_sub(1, 2.72, 2.72):.30f}")
    print(f"A=1,(3.14E12 + 3.14E12) = {kmr.kmr_add(1, 3.14E12, 3.14E12):.30f}")
    print(f"A=1,(3.14E12 - 2.72E12)  = {kmr.kmr_sub(1, 3.14E12, 2.72E12):.30f}")

    # Handle precise if A = 0 in case then return: A+B, A-B
    print(f"A=0,(3.14 + 3.14) = {kmr.kmr_add(0, 3.14, 3.14):.30f}")
    print(f"A=0,(2.72 - 2.72)  = {kmr.kmr_sub(0, 2.72, 2.72):.30f}")
    print(f"A=0,(3.14E12 + 3.14E12) = {kmr.kmr_add(0, 3.14E12, 3.14E12):.30f}")
    print(f"A=0,(3.14E12 - 2.72E12)  = {kmr.kmr_sub(0, 3.14E12, 2.72E12):.30f}")

    # Handle precise if A = 10E+/-12
    print(f"A=10E12,(3.14 + 3.14) = {kmr.kmr_add(10E12, 3.14, 3.14):.30f}")
    print(f"A=10E12,(2.72 - 2.72)  = {kmr.kmr_sub(10E12, 2.72, 2.72):.30f}")
    print(f"A=10E-12,(3.14 + 3.14) = {kmr.kmr_add(10E-12, 3.14, 3.14):.30f}")
    print(f"A=10E-12,(2.72 - 2.72)  = {kmr.kmr_sub(10E-12, 2.72, 2.72):.30f}")

    # Handle precise and big if A = 10E-12
    print(f"A=10E-12,(3.14E12 + 3.14E12) = {kmr.kmr_add(10E-12, 3.14E12, 3.14E12):.30f}")
    print(f"A=10E-12,(2.72E12 - 2.72E12)  = {kmr.kmr_sub(10E-12, 2.72E12, 2.72E12):.30f}")
