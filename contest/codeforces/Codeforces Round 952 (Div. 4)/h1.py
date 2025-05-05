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


class UnionFind:
    def __init__(self, n):
        self.parent = {}
        self.rank = [1] * n
        self.size = [1] * n
        self.n = n
    
    def find(self, x):
        self.parent.setdefault(x, x)
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union_by_size(self, x, y):
        x_root, y_root = self.find(x), self.find(y)
        if x_root != y_root:
            if self.size[y_root] <= self.size[x_root]:
                self.parent[y_root] = x_root
                self.size[x_root] += self.size[y_root]
            else:
                self.parent[x_root] = y_root
                self.size[y_root] += self.size[x_root]
    
    def union_rank(self, x: int, y: int):
        x_root, y_root = self.find(x), self.find(y)
        if x_root != y_root:
            if self.rank[y_root] <= self.rank[x_root]:
                self.parent[y_root] = x_root
            else:
                self.parent[x_root] = y_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1
    
    def connected(self, x: int, y: int):
        return self.find(x) == self.find(y)


def H1():
    for _ in range(II()):
        n, m = MII()
        a = [I() for _ in range(n)]
        uf = UnionFind(n * m)
        for i in range(n):
            for j in range(m):
                if a[i][j] == '#':
                    if i and a[i - 1][j] == '#':
                        uf.union_by_size(i * m + j, (i - 1) * m + j)
                    if j and a[i][j - 1] == '#':
                        uf.union_by_size(i * m + j, i * m + j - 1)
        
        ans = 0
        for i in range(n):
            d = dict()
            d[-1] = 0
            cnt = 0
            for j in range(m):
                if a[i][j] == '.':
                    cnt += 1
                else:
                    tmp = uf.find(i * m + j)
                    d[tmp] = uf.size[tmp]
                if i and a[i - 1][j] == '#':
                    tmp = uf.find((i - 1) * m + j)
                    d[tmp] = uf.size[tmp]
                if i < n - 1 and a[i + 1][j] == '#':
                    tmp = uf.find((i + 1) * m + j)
                    d[tmp] = uf.size[tmp]
            ans = max(ans, sum(d.values()) + cnt)
        for j in range(m):
            d = dict()
            d[-1] = 0
            cnt = 0
            for i in range(n):
                if a[i][j] == '*':
                    cnt += 1
                else:
                    tmp = uf.find(i * m + j)
                    d[tmp] = uf.size[tmp]
                if j and a[i][j - 1] == '#':
                    tmp = uf.find(i * m + j - 1)
                    d[tmp] = uf.size[tmp]
                if j < m - 1 and a[i][j + 1] == '#':
                    tmp = uf.find(i * m + j + 1)
                    d[tmp] = uf.size[tmp]
            ans = max(ans, sum(d.values()) + cnt)
        print(ans)


if __name__ == "__main__":
    H1()
