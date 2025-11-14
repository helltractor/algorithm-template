#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


class PrefixSum2D:
    __slots__ = ["m", "n", "pre"]

    def __init__(self, mat: List[List[int]]):
        self.m = m = len(mat)
        self.n = n = len(mat[0])
        self.pre = pre = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(mat):
            for j, v in enumerate(row):
                pre[i + 1][j + 1] = pre[i][j + 1] + pre[i + 1][j] - pre[i][j] + v

    def find(self, r1: int, c1: int, r2: int, c2: int) -> int:
        """查询以(r1,c1)为左上角，(r2,c2)为右下角的矩形区间内所有值的和"""
        return self.pre[r2 + 1][c2 + 1] - self.pre[r2 + 1][c1] - self.pre[r1][c2 + 1] + self.pre[r1][c1]


class PrefixSum3D:
    __slots__ = ["m", "n", "o", "pre"]

    def __init__(self, mat: List[List[List[int]]]):
        self.m = m = len(mat)
        self.n = n = len(mat[0])
        self.o = o = len(mat[0][0])
        self.pre = pre = [[[0] * (o + 1) for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                for k in range(o):
                    pre[i + 1][j + 1][k + 1] = mat[i][j][k] + pre[i][j + 1][k + 1] + pre[i + 1][j][k + 1] + pre[i + 1][j + 1][k] - pre[i][j][k + 1] - pre[i][j + 1][k] - pre[i + 1][j][k] + pre[i][j][k]

    def find(self, x1: int, y1: int, z1: int, x2: int, y2: int, z2: int) -> int:
        pre = self.pre
        return pre[x2][y2][z2] - pre[x1][y2][z2] - pre[x2][y1][z2] - pre[x2][y2][z1] + pre[x1][y1][z2] + pre[x1][y2][z1] + pre[x2][y1][z1] - pre[x1][y1][z1]
