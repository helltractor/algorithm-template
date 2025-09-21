#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


class Difference2D:
    __slots__ = ["m", "n", "diff"]

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.diff = [[0] * (n + 2) for _ in range(m + 2)]

    def add(self, r1: int, c1: int, r2: int, c2: int, delta: int):
        """下标从0开始，区间变化delta"""
        diff = self.diff
        diff[r1 + 1][c1 + 1] += delta
        diff[r1 + 1][c2 + 2] -= delta
        diff[r2 + 2][c1 + 1] -= delta
        diff[r2 + 2][c2 + 2] += delta

    def get(self) -> List[List[int]]:
        diff = self.diff
        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                diff[i][j] += diff[i][j - 1] + diff[i - 1][j] - diff[i - 1][j - 1]
        diff = diff[1:-1]
        for i, row in enumerate(diff):
            diff[i] = row[1:-1]
        return diff
