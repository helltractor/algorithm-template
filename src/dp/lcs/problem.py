#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bisect import bisect_left
from typing import List


class Solution:

    @staticmethod
    def lc1713(target: List[int], arr: List[int]) -> int:
        """
        link: https://leetcode.cn/problems/minimum-operations-to-make-a-subsequence/
        desc: 无相同元素的LCS可以转化为LIS
        """

        d = {x: i for i, x in enumerate(target)}
        li = []
        s = set(target)
        for i, x in enumerate(arr):
            if x not in s:
                continue
            idx = bisect_left(li, d[x])
            if idx == len(li):
                li.append(d[x])
            else:
                li[idx] = d[x]
        return len(target) - len(li)
