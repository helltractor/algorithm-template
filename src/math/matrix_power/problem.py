#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter
from itertools import pairwise
from typing import List

from util.io import MII
from math.matrix_power.template import MatrixPower


class Solution:

    def lc3337(self, s: str, t: int, nums: List[int]) -> int:
        """
        link: https://leetcode.cn/problems/total-characters-in-string-after-transformations-ii/
        """
        mat = [[0] * 26 for _ in range(26)]
        f0 = [[1] for _ in range(26)]
        for i, x in enumerate(nums):
            for j in range(i + 1, i + x + 1):
                mat[i][j % 26] = 1
        mat = MatrixPower.matrix_power(mat, t, f0)
        # mat = MatrixPower.matrix_power_numpy_list(a, t, f0)
        ans = 0
        for k, v in Counter(s).items():
            ans += mat[ord(k) - 97][0] * v
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

        valid = []
        for c in range(3**m):
            c3 = convert(c)
            for x, y in pairwise(c3):
                if x == y:
                    break
            else:
                valid.append(c3)

        nv = len(valid)
        mat = [[0] * nv for _ in range(nv)]
        f0 = [1] * nv
        for i, c1 in enumerate(valid):
            for j, c2 in enumerate(valid):
                for x, y in zip(c1, c2):
                    if x == y:
                        break
                else:
                    mat[i][j] = 1

        ans = MatrixPower.matrix_power_numpy_list(mat, n - 1, f0)
        return sum(ans) % 1_000_000_007

    def lc3700_1(self, n: int, l: int, r: int) -> int:
        """
        link:https://leetcode.cn/problems/number-of-zigzag-arrays-ii/
        """
        m = r - l + 1
        mat = [[0] * (2 * m) for _ in range(2 * m)]
        f0 = [[1] for _ in range(2 * m)]
        for i in range(m):
            for j in range(m):
                if i == j:
                    continue
                if i > j:
                    mat[i][j + m] = 1
                else:
                    mat[i + m][j] = 1

        res = MatrixPower.matrix_power(mat, n - 1, f0)
        ans = sum(sum(row) for row in res)
        return ans % 1_000_000_007

    def lc3700_2(self, n: int, l: int, r: int) -> int:
        """
        link:https://leetcode.cn/problems/number-of-zigzag-arrays-ii/
        """
        m = r - l
        mat = [[0] * m for _ in range(m)]
        f0 = [[1] for _ in range(m)]
        for i in range(m):
            for j in range(m - i - 1, m):
                mat[i][j] = 1

        res = MatrixPower.matrix_power(mat, n - 1, f0)
        ans = sum(sum(row) for row in res)
        return 2 * ans % 1_000_000_007

    def cf93d(self):
        """
        link: https://codeforces.com/problemset/problem/93/D
        """
        L, R = MII()

        def f(n):
            if n == 0:
                return 0
            if n == 1:
                return 4
            mat = [[0] * 17 for _ in range(17)]
            f0 = [[0] for _ in range(17)]
            mat[16][16] = 1
            f0[16][0] = 4

            # wbry -> 0123
            # wr, rw, by, yb, bwr, rwb not allowed
            for i in range(4):
                for j in range(4):
                    if i == j or i + j == 3:
                        continue
                    for k in range(4):
                        if j == k or j + k == 3 or (j == 0 and i + k == 3):
                            continue
                        mat[i * 4 + j][j * 4 + k] = 1
                        mat[16][j * 4 + k] += 1
                    f0[i * 4 + j][0] = 1
                    f0[16][0] += 1
            return MatrixPower.matrix_power(mat, n - 2, f0)[16][0]

        def cal(n):
            inv2 = (1_000_000_007 + 1) // 2
            return (f(n) + f((n + 1) // 2)) * inv2

        ans = (cal(R) - cal(L - 1)) % 1_000_000_007
        print(ans)
