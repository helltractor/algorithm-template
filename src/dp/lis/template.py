#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025/4/15 上午11:27

from bisect import bisect_left
from typing import List


class LongestIncreasingSubsequence:

    @staticmethod
    def lis(nums: List[int]) -> int:
        lis = []
        for i, x in enumerate(nums):
            idx = bisect_left(lis, x)
            if idx == len(lis):
                lis.append(x)
            else:
                lis[idx] = x
        return len(lis)
