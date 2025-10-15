#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import gcd
from operator import add
from typing import List, Tuple
from struct.segment_tree import SegmentTree, LazySegmentTree
from util.io.fast_io import II, LI, LII, MII
from math import inf


class Solution:

    @staticmethod
    def lc3525(nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
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

    def lc3605(self, nums: List[int], maxC: int) -> int:
        """
        link: https://leetcode.cn/problems/minimum-stability-factor-of-array/
        """
        n = len(nums)
        seg = SegmentTree(gcd, 0, nums)
        l = 1
        r = n
        while l <= r:
            m = l + r >> 1
            i = 0
            cnt = 0
            while i + m <= n:
                g = seg.prod(i, i + m)
                if g > 1:
                    i += m - 1
                    cnt += 1
                i += 1
            if cnt > maxC:
                l = m + 1
            else:
                r = m - 1
        return r

    def abc426f():
        """
        link: https://atcoder.jp/contests/abc426/tasks/abc426_f
        """
        n = II()
        a = LII()
        q = II()
        qs = [LII() for _ in range(q)]
        op = mapping = composition = lambda x, y: x + y
        check = lambda x: x >= 0
        fmin = lambda x, y: x if x < y else y
        segtree = SegmentTree(op, 0, [1] * (n + 1))
        lazy_segtree = LazySegmentTree(fmin, inf, mapping, composition, 0, a)

        for l, r, k in qs:
            l -= 1
            lazy_segtree.apply(l, r, -k)
            ans = segtree.prod(l, r) * k
            while lazy_segtree.prod(l, r) < 0:
                right = lazy_segtree.max_right(l, check)
                ans += lazy_segtree.get(right)
                lazy_segtree.set(right, inf)
                segtree.set(right, 0)
            print(ans)

    def cf2145e():
        """
        link: https://codeforces.com/contest/2145/problem/E
        tag: mex
        """
        ac, dr = MII()
        n = II()
        a = LII()
        b = LII()
        m = II()
        c = [LII() for _ in range(m)]

        mx = 2 * 10**6 + 1
        fmax = lambda x, y: x if x > y else y
        fmin = lambda x, y: x if x < y else y
        f = lambda x, y: fmax(0, x - ac) + fmax(0, y - dr)
        p = [f(x, y) for x, y in zip(a, b)]
        cnt = [-i for i in range(mx)]
        sg = LazySegmentTree(fmin, 0, add, add, 0, cnt)
        for x in p:
            sg.apply(x + 1, mx, 1)

        pre = -1
        for k, x, y in c:
            ans = -1
            if f(x, y) != p[k - 1]:
                sg.apply(p[k - 1] + 1, mx, -1)
                p[k - 1] = f(x, y)
                sg.apply(p[k - 1] + 1, mx, 1)
            else:
                ans = pre
            if ans == -1:
                ans = sg.max_right(0, lambda v: v >= 0) - 1
            print(ans)
