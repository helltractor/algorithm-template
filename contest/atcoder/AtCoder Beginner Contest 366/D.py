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


class PrefixSum3D:
    __slots__ = ["m", "n", "o", "pre"]
    
    def __init__(self, mat: List[List[List[int]]]):
        self.m = m = len(mat)
        self.n = n = len(mat[0])
        self.o = o = len(mat[0][0])
        self.pre = pre = [[[0] * (o + 1) for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                for k in range(o):
                    pre[i + 1][j + 1][k + 1] = mat[i][j][k] + pre[i][j + 1][k + 1] + pre[i + 1][j][k + 1] + \
                                               pre[i + 1][j + 1][k] - pre[i][j][k + 1] - pre[i][j + 1][k] - \
                                               pre[i + 1][j][k] + pre[i][j][k]
    
    def find(self, x1: int, y1: int, z1: int, x2: int, y2: int, z2: int) -> int:
        pre = self.pre
        return pre[x2][y2][z2] - pre[x1][y2][z2] - pre[x2][y1][z2] - pre[x2][y2][z1] + pre[x1][y1][z2] + pre[x1][y2][
            z1] + pre[x2][y1][z1] - pre[x1][y1][z1]


def D():
    n = II()
    b = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            b[i][j] = LII()
    q = II()
    pre = PrefixSum3D(b)
    for _ in range(q):
        lx, rx, ly, ry, lz, rz = MII()
        print(pre.find(lx - 1, ly - 1, lz - 1, rx, ry, rz))


if __name__ == '__main__':
    D()
