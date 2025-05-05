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

# 1 | 4
# ------
# 2 | 3
def CF429B():
    n, m = MII()
    g = [LII() for _ in range(n)]
    f1 = [[0] * (m + 2) for _ in range(n + 2)]
    f2 = [[0] * (m + 2) for _ in range(n + 2)]
    f3 = [[0] * (m + 2) for _ in range(n + 2)]
    f4 = [[0] * (m + 2) for _ in range(n + 2)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            f1[i][j] = fmax(f1[i - 1][j], f1[i][j - 1]) + g[i - 1][j - 1]
        for j in range(m, 0, -1):
            f4[i][j] = fmax(f4[i - 1][j], f4[i][j + 1]) + g[i - 1][j - 1]
    for i in range(n, 0, -1):
        for j in range(1, m + 1):
            f2[i][j] = fmax(f2[i + 1][j], f2[i][j - 1]) + g[i - 1][j - 1]
        for j in range(m, 0, -1):
            f3[i][j] = fmax(f3[i + 1][j], f3[i][j + 1]) + g[i - 1][j - 1]

    ans = 0
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            ans = fmax(ans, f1[i][j + 1] + f4[i + 1][j + 2] + f2[i + 1][j] + f3[i + 2][j + 1])
            ans = fmax(ans, f1[i + 1][j] + f4[i][j + 1] + f2[i + 2][j + 1] + f3[i + 1][j + 2])
    print(ans)


if __name__ == "__main__":
    CF429B()
