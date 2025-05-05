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
        b = -2
        co = 0
        for i in range(0, n):
            if a[i] == 0:
                b = -2
            elif b == 0:
                if a[i] <= 2:
                    b = -2
                elif a[i] <= 4:
                    b = 2
                    co += 1
                else:
                    b = -2
                    co += 1
            elif a[i] <= 2 or (b == 2 and a[i] <= 4):
                b = 0
                co += 1
            else:
                b = -2
                co += 1
        return co
    
    def mysolve(self, n, a):
        
        ans = 0
        pre = 0
        for i, x in enumerate(a):
            if x == 0:
                pre = 0
            elif pre == 1:
                if x <= 2:
                    pre = 0
                elif x <= 4:
                    pre = 2
                    ans += 1
                else:
                    pre = 0
                    ans += 1
            elif x <= 2 or (pre == 2 and x <= 4):
                pre = 1
                ans += 1
            else:
                pre = 0
                ans += 1
        return ans
    
    def test(self):
        for _ in range(10 ** 5):
            n = randint(1, 10)
            a = [randint(1, n) for _ in range(n)]
            other = self.solve(n, a)
            mine = self.mysolve(n, a)
            if other != mine:
                print(n)
                print(a)
            assert other == mine, (other, mine)


# pre = 0 : no square
# pre = 1 : one square (0, 2)
# pre = 2 : one square (2, 4)
def D():
    for _ in range(II()):
        n = II()
        a = LII()
        
        ans = 0
        pre = 0
        for i, x in enumerate(a):
            if x == 0:
                pre = 0
            elif pre == 1:
                if x <= 2:
                    pre = 0
                elif x <= 4:
                    pre = 2
                    ans += 1
                else:
                    pre = 0
                    ans += 1
            elif x <= 2 or (pre == 2 and x <= 4):
                pre = 1
                ans += 1
            else:
                pre = 0
                ans += 1
        print(ans)


if __name__ == '__main__':
    D()
