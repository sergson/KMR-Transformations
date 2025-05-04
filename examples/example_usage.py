"""
KMR Operator Algebra
Version: 1.0.0
License: GPL 3.0
"""
__author__ = "Sergei Terikhov"

from kmr_operations import kmr_direct, kmr_inverse

"""
KMR Operations Demo

Examples:
    >>> kmr_direct(2, 3)
    0.2857142857142857
    >>> kmr_inverse(2, 3)
    -1.0
"""
if __name__ == "__main__":
    print(f"2 ⊙ 3 = {kmr_direct(2, 3):.4f}")  # 0.2857
    print(f"2 ⊘ 3 = {kmr_inverse(2, 3):.1f}")  # -1.0