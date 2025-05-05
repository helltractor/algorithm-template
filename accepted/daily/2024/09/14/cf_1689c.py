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

def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    
    return wrappedfunc

# choose the node by depth
def CF1689C():
    for _ in range(II()):
        n = II()
        g = [[] for _ in range(n + 1)]
        g[1].append(0)
        for _ in range(n - 1):
            u, v = MII()
            g[u].append(v)
            g[v].append(u)
        cnt = [1] * (n + 1)
        @bootstrap
        def dfs(u, f):
            for v in g[u]:
                if v == f:
                    continue
                cnt[u] += yield dfs(v, u)
            yield cnt[u]
        dfs(1, 0)
        ans = 0
        q = deque([[1, 0, 0]])
        while q:
            x, fa, s = q.popleft()
            tmp = s
            if len(g[x]) == 2:
                for y in g[x]:
                    if y != fa:
                        s += cnt[y] - 1
                        tmp = fmax(tmp, s)
            elif len(g[x]) == 3:
                y1 = y2 = 0
                for y in g[x]:
                    if y != fa:
                        if y1 == 0:
                            y1 = y
                        else:
                            y2 = y
                tmp = fmax(tmp, s + cnt[y1] - 1)
                q.append([y2, x, s + cnt[y1] - 1])
                tmp = fmax(tmp, s + cnt[y2] - 1)
                q.append([y1, x, s + cnt[y2] - 1])
            ans = fmax(ans, tmp)
        print(ans)

def CF1689C2():
    for _ in range(II()):
        n = II()
        g = [[] for _ in range(n + 1)]
        g[1].append(0)
        for _ in range(n - 1):
            u, v = MII()
            g[u].append(v)
            g[v].append(u)
            
        @bootstrap
        def dfs(u, f):
            if len(g[u]) <= 2:
                yield len(g[u])
            res = MOD9
            for v in g[u]:
                if v == f:
                    continue
                tmp = yield dfs(v, u)
                res = fmin(res, 2 + tmp)
            yield res
        print(n - dfs(1, 0))
    
if __name__ == "__main__":
    CF1689C2()
