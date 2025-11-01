#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import gcd, inf
from operator import add
from typing import List, Tuple
from struct.fenwick.template import FenwickTree
from struct.segment_tree.template import SegmentTree, LazySegmentTree
from util.io.fast_io import II, LII, MII

fmax = lambda x, y: x if x > y else y
fmin = lambda x, y: x if x < y else y


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

        tree = SegmentTree(op, e, v)
        ans = []
        for i, v, s, x in queries:
            res = [0] * k
            res[v % k] += 1
            tree.set(i, (v % k, res))
            _, cnt = tree.prod(s, n)
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
        f = lambda x, y: fmax(0, x - ac) + fmax(0, y - dr)
        p = [f(x, y) for x, y in zip(a, b)]
        cnt = [-i for i in range(mx)]
        tree = LazySegmentTree(fmin, 0, add, add, 0, cnt)
        for x in p:
            tree.apply(x + 1, mx, 1)

        pre = -1
        for k, x, y in c:
            ans = -1
            if f(x, y) != p[k - 1]:
                tree.apply(p[k - 1] + 1, mx, -1)
                p[k - 1] = f(x, y)
                tree.apply(p[k - 1] + 1, mx, 1)
            else:
                ans = pre
            if ans == -1:
                ans = tree.max_right(0, lambda v: v >= 0) - 1
            print(ans)

    def cf1701f():
        """
        link: https://codeforces.com/contest/1701/problem/F
        """
        n, d = MII()
        a = LII()
        mx = max(a) + 1
        vis = [0] * mx

        def op(a, b):
            return a[0] + b[0], a[1] + b[1], a[2] + b[2]

        e = 0, 0, 0

        def mapping(f, x):
            a, b, c = x
            c += b * f * 2 + a * f * f
            b += a * f
            return a, b, c

        tree = LazySegmentTree(op, e, mapping, add, 0, mx)
        fw = FenwickTree(mx)
        for v in a:
            if vis[v]:
                fw.update(v, -1)
                tree.set(v, (0, 0, 0))
                tree.apply(fmax(1, v - d), v, -1)
            else:
                k = fw.range_query(v, fmin(mx, v + d))
                fw.update(v, 1)
                tree.set(v, (1, k, k * k))
                tree.apply(fmax(1, v - d), v, 1)
            _, s1, s2 = tree.all_prod()
            print((s2 - s1) // 2)
            vis[v] = 1 - vis[v]

    def lc3721(self, nums: List[int]) -> int:
        """
        link: https://leetcode.cn/problems/longest-balanced-subarray-ii/
        """
        n = len(nums)
        ans = 0

        def op(a, b):
            return fmin(a[0], b[0]), fmax(a[1], b[1])

        def mapping(f, k):
            return k[0] + f, k[1] + f

        e = [inf, -inf]
        v = [e for _ in range(n + 1)]
        tree = LazySegmentTree(op, e, mapping, add, 0, v)
        last = [-1] * (max(nums) + 1)
        for i, x in enumerate(nums):
            y = -1 if x % 2 else 1
            tree.set(i, [y, y])
            tree.apply(last[x] + 1, i, y)
            last[x] = i
            j = tree.max_right(0, lambda p: not (p[0] <= 0 and p[1] >= 0))
            ans = fmax(ans, i - j + 1)
        return ans
