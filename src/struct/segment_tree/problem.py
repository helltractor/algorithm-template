#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025-04-15 12:30:49

from typing import List, Tuple
from struct.segment_tree import SegmentTree


class Solution:

    @staticmethod
    def lc_3525(nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        """
        link: https://leetcode.cn/problems/find-x-value-of-array-ii/
        """
        n = len(nums)
        nums = [x % k for x in nums]

        def op(
            a: Tuple[int, List[int]], b: Tuple[int, List[int]]
        ) -> Tuple[int, List[int]]:
            cnt = a[1].copy()
            left_m = a[0]
            for m, c in enumerate(b[1]):
                cnt[left_m * m % k] += c
            return left_m * b[0] % k, cnt

        e = (1, [0] * k)
        v = []
        for x in nums:
            res = [0] * k
            res[x] += 1
            v.append((x, res))

        sg = SegmentTree(op, e, v)
        ans = []
        for i, v, s, x in queries:
            res = [0] * k
            res[v % k] += 1
            sg.set(i, (v % k, res))
            _, cnt = sg.prod(s, n)
            ans.append(cnt[x])
        return ans
