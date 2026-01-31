#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bisect import bisect_left
from itertools import pairwise
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

    def lc3454(self, squares: List[List[int]]) -> float:
        """
        link: https://leetcode.cn/problems/separate-squares-ii
        relike: https://leetcode.cn/problems/rectangle-area-ii
        """
        xs = []
        events = []
        for lx, y, l in squares:
            rx = lx + l
            xs.append(lx)
            xs.append(rx)
            events.append((y, lx, rx, 1))
            events.append((y + l, lx, rx, -1))

        xs = sorted(set(xs))
        events.sort()

        # sum_len, min_cnt
        v = [(xs[i + 1] - xs[i], 0) for i in range(len(xs) - 1)]

        def op(a, b):
            min_cnt = min(a[1], b[1])
            sum_len = 0
            if a[1] == min_cnt:
                sum_len += a[0]
            if b[1] == min_cnt:
                sum_len += b[0]
            return sum_len, min_cnt

        def mapping(f, x):
            return x[0], x[1] + f

        def composition(f, g):
            return f + g

        tree = LazySegmentTree(op, (0, 0), mapping, composition, 0, v)
        records = []
        tot_area = 0
        for (y, lx, rx, delta), e2 in pairwise(events):
            l = bisect_left(xs, lx)
            r = bisect_left(xs, rx)
            # [l, r)
            tree.apply(l, r, delta)
            sum_len, min_cnt = tree.all_prod()
            cov_len = xs[-1] - xs[0] - (0 if min_cnt else sum_len)
            records.append((tot_area, cov_len))
            tot_area += cov_len * (e2[0] - y)

        i = bisect_left(records, tot_area, key=lambda p: p[0] * 2) - 1
        area, sum_len = records[i]
        return events[i][0] + (tot_area - area * 2) / (sum_len * 2)

    def abc441g():
        n, q = MII()
        qs = [LII() for _ in range(q)]

        def op(a, b):
            return fmax(a[0], b[0]), a[1] + b[1], a[2] + b[2]

        def mapping(f, x):
            a, b, c = x
            if f[0] % 2:
                if c == 0:
                    return 0, c, b
                return f[1], c, b
            if b == 0:
                return 0, b, c
            if f[0] == 0:
                return a + f[1], b, c
            return f[1], b, c

        def composition(f, g):
            if f[0] == 0 and g[0] == 0:
                return 0, f[1] + g[1]
            if f[0] == 0 and g[0] > 0:
                return g[0], f[1] + g[1]
            if f[0] >= 0 and g[0] == 0:
                return f
            return f[0] + g[0], f[1]

        e = (-inf, 0, 0)
        id = (0, 0)  # 翻转次数，新增丸数
        v = [(0, 1, 0) for _ in range(n)]

        tree = LazySegmentTree(op, e, mapping, composition, id, v)

        for row in qs:
            l, r = row[1], row[2]
            if row[0] == 1:
                tree.apply(l - 1, r, (0, row[-1]))
            elif row[0] == 2:
                tree.apply(l - 1, r, (1, 0))
            else:
                print(tree.prod(l - 1, r)[0])
