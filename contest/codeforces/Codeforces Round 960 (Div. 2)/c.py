import unittest

import os, sys, random
from io import IOBase, BytesIO
from copy import deepcopy
from decimal import Decimal, getcontext
from types import GeneratorType
from functools import lru_cache, reduce
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from itertools import accumulate, combinations, permutations
from heapq import heapify, heappop, heappush, heappushpop
from typing import Generic, Iterable, Iterator, TypeVar, Union, List
from math import ceil, floor, sqrt, pi, factorial, gcd, lcm, log, log10, log2, inf
from sys import stdin, stdout, setrecursionlimit


class FastIO(IOBase):
    newlines = 0
    
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
    
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b: break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
    
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
    
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


BUFSIZE = 1 << 12
sys.stdin = IOWrapper(sys.stdin)
sys.stdout = IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LI = lambda: list(input())
LII = lambda: list(map(int, input().split()))
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LGMI = lambda: list(map(lambda x: int(x) - 1, input().split()))
MOD1, MOD9 = 10 ** 9 + 7, 998244353
RD = random.randint(MOD1, MOD1 << 1)
D4 = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # ->, <-, v, ^
D8 = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]  # ->, <-, v, ^, ↘, ↙, ↗, ↖
Y, N, A, B = "Yes", "No", "Alice", "Bob"


class UnitTest(unittest.TestCase):
    
    def solve(self, n, a):
        def f(n, a):
            sm = sum(a)
            b = [0] * n
            cnt = [0] * (n + 1)
            mad = 0
            for i in range(n):
                cnt[a[i]] += 1
                if cnt[a[i]] >= 2:
                    mad = max(mad, a[i])
                b[i] = mad
            return sm, b
        
        ans = 0
        sm, b = f(n, a)
        ans += sm
        sm, b = f(n, b)
        ans += sm
        tmp = 0
        for i in range(n):
            diff = b[i] - tmp
            c = (n - i)
            ans += diff * c * (c + 1) // 2
            tmp = b[i]
        return ans
    
    def solve1(self, n, a):
        def f(a):
            s = sum(a)
            cnt = [0] * (n + 1)
            mad = 0
            for i in range(n):
                cnt[a[i]] += 1
                if cnt[a[i]] >= 2:
                    mad = max(mad, a[i])
                a[i] = mad
            return s, a
        
        s1, b = f(a)
        s2, b = f(b)
        pre = 0
        ans = s1 + s2
        cnt = Counter(b)
        for x in sorted(cnt, reverse=True):
            v = cnt[x]
            ans += (v * pre + (v + 1) * v // 2) * x
            pre += v
        return ans
    
    def test(self):
        for i in range(1, 100):
            n = random.randint(1, 10000)
            a = [random.randint(1, n) for _ in range(n)]
            other = self.solve(n, a)
            my = self.solve1(n, a)
            assert other == my


def C():
    for _ in range(II()):
        n = II()
        a = LII()
        
        def f(a):
            s = sum(a)
            cnt = [0] * (n + 1)
            mad = 0
            for i in range(n):
                cnt[a[i]] += 1
                if cnt[a[i]] >= 2:
                    mad = max(mad, a[i])
                a[i] = mad
            return s, a
        
        s1, b = f(a)
        s2, b = f(b)
        pre = 0
        ans = s1 + s2
        cnt = Counter(b)
        for x in sorted(cnt, reverse=True):
            v = cnt[x]
            ans += (v * pre + (v + 1) * v // 2) * x
            pre += v
        print(ans)


if __name__ == '__main__':
    C()
