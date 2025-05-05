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


def CF1725M():
    # n, m = MII()
    # g = [[] for _ in range(n)]
    # for _ in range(m):
    #     u, v, w = MII()
    #     u -= 1
    #     v -= 1
    #     g[u].append((v, w, 0))
    #     g[v].append((u, w, 1))
    # dis = [[inf] * 2 for _ in range(n)]
    # dis[0] = [0, 0]
    # h = [(0, 0, 0)]
    # while h:
    #     d, u, uInv = heappop(h)
    #     if d > dis[u][uInv]:
    #         continue
    #     for v, w, vInv in g[u]:
    #         nd = d + w
    #         if (vInv or uInv == 0) and dis[v][vInv] > nd:
    #             dis[v][vInv] = nd
    #             heappush(h, (nd, v, vInv))
    # ans = [-1] * (n - 1)
    # for i, row in enumerate(dis[1:]):
    #     tmp = min(row)
    #     if tmp < inf:
    #         ans[i] = tmp
    # print(*ans)
    
    n, m = MII()
    # 状态转移，选择反向边
    g = [[(u + n, 0)] if u <= n else [] for u in range(n << 1 | 1)]
    for _ in range(m):
        u, v, w = MII()
        g[u].append((v, w))
        g[v + n].append((u + n, w))
    dis = [inf] * (n << 1 | 1)
    dis[1], mask, h = 0, (1 << 20) - 1, [1]
    while h:
        s = heappop(h)
        d, u = s >> 20, s & mask
        if d > dis[u]:
            continue
        for v, w in g[u]:
            new_d = w + d
            if new_d < dis[v]:
                dis[v] = new_d
                heappush(h, new_d << 20 | v)
    print(' '.join(map(lambda x: str(x) if x < inf else '-1', dis[n + 2:])))


if __name__ == '__main__':
    CF1725M()
