#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2025年5月13日 11点12分
# @Link : 

from typing import List

class MatrixPower:

    @staticmethod
    def matrix_multiply(a: List[List[int]], b: List[List[int]], mod: int = 1_000_000_007) -> List[List[int]]:
        """Multiply two matrices a and b under modulo, a @ b."""
        return [[sum(x * y % mod for x, y in zip(a_row, b_col)) % mod for b_col in zip(*b)] for a_row in a]
    
    @staticmethod
    def matrix_power(base: List[List[int]], n: int, f0: List[List[int]], mod: int = 1_000_000_007) -> List[List[int]]:
        """Raise matrix base to the power of n under modulo, base ^ n @ f0."""
        mul = lambda a, b: [[sum(x * y % mod for x, y in zip(a_row, b_col)) % mod for b_col in zip(*b)] for a_row in a]
        res = f0
        while n:
            if n & 1:
                res = mul(base, res)
            base = mul(base, base)
            n >>= 1
        return res
    
    @staticmethod
    def matrix_power_numpy(base: List[List[int]], n: int, f0: List[List[int]], mod: int = 1_000_000_007) -> List[List[int]]:
        """Raise matrix base to the power of n under modulo using numpy, base ^ n @ f0."""
        import numpy as np
        base = np.array(base, dtype=object)
        res = np.array(f0, dtype=object)
        while n:
            if n & 1:
                res = base @ res % mod
            base = base @ base % mod
            n >>= 1
        return res.tolist()
    