#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter
from itertools import pairwise
from typing import List

from math.matrix_power.template import MatrixPower


class Solution:

    def lc3337(self, s: str, t: int, nums: List[int]) -> int:
        """
        link: https://leetcode.cn/problems/total-characters-in-string-after-transformations-ii/
        """
        f0 = [[1] for _ in range(26)]
        a = [[0] * 26 for _ in range(26)]
        for i, x in enumerate(nums):
            for j in range(i + 1, i + x + 1):
                a[i][j % 26] = 1
        mt = MatrixPower.matrix_power(a, t, f0)
        # mt = MatrixPower.matrix_power_numpy_list(a, t, f0)
        ans = 0
        for k, v in Counter(s).items():
            ans += mt[ord(k) - 97][0] * v
        return ans % 1_000_000_007

    def lc1931(self, m: int, n: int) -> int:
        """
        link: https://leetcode.cn/problems/painting-a-grid-with-three-different-colors/
        """

        def convert(base: int) -> str:
            res = [0] * m
            for i in range(m):
                res[i] = base % 3
                base //= 3
            return "".join(map(str, res[::-1]))

        vaild = []
        for c in range(3**m):
            c3 = convert(c)
            for x, y in pairwise(c3):
                if x == y:
                    break
            else:
                vaild.append(c3)

        nv = len(vaild)
        mat = [[0] * nv for _ in range(nv)]
        for i, c1 in enumerate(vaild):
            for j, c2 in enumerate(vaild):
                for x, y in zip(c1, c2):
                    if x == y:
                        break
                else:
                    mat[i][j] = 1

        ans = MatrixPower.matrix_power_numpy_list(mat, n - 1, [1] * nv)
        return sum(ans) % 1_000_000_007

    def lc3700_1(self, n: int, l: int, r: int) -> int:
        """
        link:https://leetcode.cn/problems/number-of-zigzag-arrays-ii/
        """
        m = r - l + 1
        mat = [[0] * (2 * m) for _ in range(2 * m)]
        for i in range(m):
            for j in range(m):
                if i == j:
                    continue
                if i > j:
                    mat[i][j + m] = 1
                else:
                    mat[i + m][j] = 1

        f0 = [[1] for _ in range(2 * m)]
        res = MatrixPower.matrix_power(mat, n - 1, f0)
        ans = sum(sum(row) for row in res)
        return ans % 1_000_000_007

    def lc3700_2(self, n: int, l: int, r: int) -> int:
        """
        link:https://leetcode.cn/problems/number-of-zigzag-arrays-ii/
        """
        m = r - l
        mat = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m - i - 1, m):
                mat[i][j] = 1

        f0 = [[1] for _ in range(m)]
        res = MatrixPower.matrix_power(mat, n - 1, f0)
        ans = sum(sum(row) for row in res)
        return 2 * ans % 1_000_000_007
