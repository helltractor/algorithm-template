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
LI = lambda: list(input().split())
LII = lambda: list(map(int, input().split()))
GMI = lambda: map(lambda x: int(x) - 1, input().split())
LGMI = lambda: list(map(lambda x: int(x) - 1, input().split()))
fmin = lambda x, y: x if x < y else y
fmax = lambda x, y: x if x > y else y
MOD1, MOD9 = 10 ** 9 + 7, 998244353
RD = random.randint(MOD1, MOD1 << 1)
D4 = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # ->, <-, v, ^
D8 = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]  # ->, <-, v, ^, ↘, ↙, ↗, ↖
Y, N, A, B = "YES", "NO", "Alice", "Bob"

class Comb:
    __slots__ = ["mod", "l", "fact", "inv"]
    
    def __init__(self):
        self.mod = mod = pow(10, 9) + 7
        self.l = l = 3 * pow(10, 5) + 5
        self.fact = fact = [1] * (l + 1)
        self.inv = inv = [1] * (l + 1)
        for i in range(1, l + 1):
            fact[i] = fact[i - 1] * i % mod
        inv[l] = pow(fact[l], mod - 2, mod)
        for i in range(l - 1, -1, -1):
            inv[i] = inv[i + 1] * (i + 1) % mod
    
    def comb(self, n, r):
        return self.fact[n] * self.inv[r] % self.mod * self.inv[n - r] % self.mod if n >= r >= 0 else 0

def CF559C():
    h, w, n = MII()
    c = Comb().comb
    a = [LII() for _ in range(n)]
    a.sort()
    a.append([h, w])
    ans = []
    for i in range(n + 1):
        ans.append(c(a[i][0]+a[i][1]-2, a[i][0]-1))
        for j in range(i):
            if a[i][1] >= a[j][1]:
                ans[i] = (ans[i]+MOD1-(ans[j] * c(a[i][0]+a[i][1]-a[j][0]-a[j][1], a[i][0]-a[j][0]))%MOD1)%MOD1
    print(ans[-1])


if __name__ == "__main__":
    CF559C()
