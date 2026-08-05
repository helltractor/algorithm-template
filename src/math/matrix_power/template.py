#!/usr/bin/env python3
# @Link: https://github.com/981377660LMT/algorithm-study/blob/master/19_%E6%95%B0%E5%AD%A6/%E7%9F%A9%E9%98%B5%E8%BF%90%E7%AE%97/%E7%9F%A9%E9%98%B5%E5%BF%AB%E9%80%9F%E5%B9%82/matqpow.py

import numpy as np
from typing import List


class MatrixPower:

    @staticmethod
    def matrix_power(
        base: List[List[int]], n: int, f0: List[List[int]], mod: int = 1_000_000_007
    ) -> List[List[int]]:
        """Raise matrix base to the power of n under modulo, base ^ n @ f0."""

        def mul(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
            mat = [[0] * len(b[0]) for _ in range(len(a))]
            for i, a_row in enumerate(a):
                for k, v in enumerate(a_row):
                    if v == 0:
                        continue
                    for j in range(len(b[0])):
                        mat[i][j] = (mat[i][j] + a[i][k] * b[k][j]) % mod
            return mat

        res = f0
        while n:
            if n & 1:
                res = mul(base, res)
            base = mul(base, base)
            n >>= 1
        return res

    @staticmethod
    def matrix_multiply(
        a: List[List[int]], b: List[List[int]], mod: int = 1_000_000_007
    ) -> List[List[int]]:
        """Multiply two matrices a and b under modulo, a @ b."""
        return [
            [sum(x * y % mod for x, y in zip(a_row, b_col)) % mod for b_col in zip(*b)]
            for a_row in a
        ]

    @staticmethod
    def matrix_power_numpy_list(
        base: List[List[int]], n: int, f0: List[List[int]], mod: int = 1_000_000_007
    ) -> List[List[int]]:
        """Raise matrix base to the power of n under modulo using numpy, base ^ n @ f0."""
        base = np.array(base, dtype=object)
        res = np.array(f0, dtype=object)
        while n:
            if n & 1:
                res = base @ res % mod
            base = base @ base % mod
            n >>= 1
        return res.tolist()

