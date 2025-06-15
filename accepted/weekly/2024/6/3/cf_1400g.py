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


class Comb:
    
    def __init__(self):
        self.mod = MOD1
        self.l = 3 * pow(10, 5) + 5
        self.fact = [1] * (self.l + 1)
        self.inv = [1] * (self.l + 1)
        for i in range(1, self.l + 1):
            self.fact[i] = self.fact[i - 1] * i % self.mod
        self.inv[self.l] = pow(self.fact[self.l], self.mod - 2, self.mod)
        for i in range(self.l - 1, -1, -1):
            self.inv[i] = self.inv[i + 1] * (i + 1) % self.mod
    
    def comb(self, n, r):
        return self.fact[n] * self.inv[r] % self.mod * self.inv[n - r] % self.mod if n >= r >= 0 else 0


# https://codeforces.com/problemset/problem/1400/G
#
# 输入 n(1≤n≤3e5) 和 m(0≤m≤min(20,n*(n-1)/2))。
# 解释：有 n 个雇佣兵，从中选择一些人（至少一个人），组成一支部队。m 的含义见下。
#
# 然后输入 n 个闭区间的左右端点 [Li,Ri]，范围 [1,n]。
# 解释：如果选了第 i 位雇佣兵，那么部队的人数必须在闭区间 [Li,Ri] 中。
#
# 最后输入 m 对数字 (ai, bi)，满足 1≤ai<bi≤n。
# 解释：这 m 对雇佣兵相互憎恨，如果选了第 ai 位雇佣兵，那么不能选第 bi 位雇佣兵，反之亦然。
#
# 输出有多少种选法，模 998244353。

def CF1400G():
    cb = Comb()
    n, m = MII()
    a = [LII() for _ in range(n)]
    b = [LII() for _ in range(m)]
    diff = [0] * (n + 2)
    sum = [[0] * 41 for _ in range(n + 1)]
    for l, r in a:
        diff[l] += 1
        diff[r + 1] -= 1
    cnt = 0
    for i in range(1, n + 1):
        cnt += diff[i]
        for j in range(41):
            sum[i][j] = (sum[i - 1][j] + cb.comb(cnt - j, i - j)) % MOD1
    ans = sum[n][0]
    has = [0] * (n + 1)
    for i in range(1, 1 << m):
        l, r, k = 1, n, 0
        for j in range(m):
            if i >> j & 1:
                # 计算区间交集
                p = b[j]
                l = max(l, a[p[0] - 1][0], a[p[1] - 1][0])
                r = min(r, a[p[0] - 1][1], a[p[1] - 1][1])
                # 时间戳，记录是否已经访问过
                if has[p[0]] != i:
                    has[p[0]] = i
                    k += 1
                if has[p[1]] != i:
                    has[p[1]] = i
                    k += 1
        if r < l:
            continue
        res = sum[r][k] - sum[l - 1][k]
        if bin(i).count('1') & 1:
            res = -res
        ans += res
    print((ans % MOD1 + MOD1) % MOD1)


if __name__ == '__main__':
    CF1400G()
