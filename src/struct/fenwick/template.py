#!/usr/bin/env python3


class FenwickTree:
    __slots__ = ["n", "c"]

    def __init__(self, n: int) -> None:
        self.n = n
        self.c = [0] * (n + 1)

    def update(self, x: int, delta: int) -> None:
        while x <= self.n:
            self.c[x] += delta
            x += x & -x

    def query(self, x: int) -> int:
        s = 0
        while x > 0:
            s += self.c[x]
            x -= x & -x
        return s

    def range_query(self, l: int, r: int) -> int:
        return self.query(r) - self.query(l - 1)


# @Author: liupengsay
# @Link: https://github.com/liupengsay/PyIsTheBestLang/blob/main/src/struct/tree_array/template.py
class FenwickTree2D:
    def __init__(self, m: int, n: int) -> None:
        self.m = m  # row
        self.n = n  # col
        self.t1 = [[0] * (n + 1) for _ in range(m + 1)]
        self.t2 = [[0] * (n + 1) for _ in range(m + 1)]
        self.t3 = [[0] * (n + 1) for _ in range(m + 1)]
        self.t4 = [[0] * (n + 1) for _ in range(m + 1)]
    
    def _add(self, x: int, y: int, val: int) -> None:
        # index start from 1 and single point add val and val cam be any integer
        i = x
        while i <= self.m:
            j = y
            while j <= self.n:
                self.t1[i][j] += val
                self.t2[i][j] += val * x
                self.t3[i][j] += val * y
                self.t4[i][j] += val * x * y
                j += j & -j
            i += i & -i
    
    def range_add(self, x1: int, y1: int, x2: int, y2: int, val: int) -> None:
        # index start from 1 and left up corner is (x1, y1) and right down corner is (x2, y2) and val can be any integer
        self._add(x1, y1, val)
        self._add(x1, y2 + 1, -val)
        self._add(x2 + 1, y1, -val)
        self._add(x2 + 1, y2 + 1, val)
    
    def _query(self, x: int, y: int) -> int:
        # index start from 1 and query the sum(sum(g[:y]) for g in grid[:x]) which is 0-index
        assert 0 <= x <= self.m and 0 <= y <= self.n
        res = 0
        i = x
        while i:
            j = y
            while j:
                res += (x + 1) * (y + 1) * self.t1[i][j] - (y + 1) * self.t2[i][j] - (x + 1) * self.t3[i][j] + \
                       self.t4[i][j]
                j -= j & -j
            i -= i & -i
        return res

    def range_query(self, x1: int, y1: int, x2: int, y2: int) -> int:
        # index start from 1 and left up corner is (x1, y1) and right down corner is (x2, y2)
        return self._query(x2, y2) - self._query(x2, y1 - 1) - self._query(x1 - 1, y2) + self._query(x1 - 1, y1 - 1)
