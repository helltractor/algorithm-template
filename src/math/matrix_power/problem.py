#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2025年5月13日 11点39分

from collections import Counter
from typing import List

from math.matrix_power.template import MatrixPower

class Solution:

    def lc_3337(self, s: str, t: int, nums: List[int]) -> int:
        """
        link: https://leetcode.cn/problems/total-characters-in-string-after-transformations-ii/
        """
        f0 = [[1] for _ in range(26)]
        a = [[0] * 26 for _ in range(26)]
        for i, x in enumerate(nums):
            for j in range(i + 1, i + x + 1):
                a[i][j % 26] = 1
        mt = MatrixPower.matrix_power(a, t, f0)
        # mt = MatrixPower.matrix_power_numpy(a, t, f0)
        ans = 0
        for k, v in Counter(s).items():
            ans += mt[ord(k) - 97][0] * v
        return ans % 1_000_000_007
