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

class BinaryIndexedTree:
    __slots__ = ["n", "c"]
    
    def __init__(self, n):
        self.n = n
        self.c = [0] * (n + 1)  # 初始化树状数组，长度为 n+1，下标从 1 开始
    
    def update(self, x: int, delta: int):
        while x <= self.n:
            self.c[x] += delta  # 更新当前位置的值
            x += x & -x  # 利用 x 的二进制表示中的最低非零位，找到下一个需要更新的位置
    
    def query(self, x: int) -> int:
        s = 0
        while x > 0:
            s += self.c[x]  # 累加当前位置的值
            x -= x & -x  # 利用 x 的二进制表示中的最低非零位，找到下一个需要累加的位置
        return s

class Factorial:
    
    def __init__(self, l=10**6+5, mod=10**9+7):
        self.mod = mod
        self.l = l
        self.fact = fact = [1] * (l + 1)
        self.finv = finv = [1] * (l + 1)
        for i in range(1, l + 1):
            fact[i] = fact[i - 1] * i % mod
        finv[l] = pow(fact[l], mod - 2, mod)
        for i in range(l - 1, -1, -1):
            finv[i] = finv[i + 1] * (i + 1) % mod
    
    @staticmethod
    def build_inv(n, mod):
        inv = [0] * (n + 1)
        inv[0] = 1
        for i in range(2, n + 1):
            inv[i] = (mod - mod // i) * inv[mod % i] % mod
        return inv
    
    def comb(self, n, r):
        return self.fact[n] * self.finv[r] % self.mod * self.finv[n - r] % self.mod if n >= r >= 0 else 0
    
    def factorial(self, n):
        return self.fact[n]
    
    def fac_inv(self, n):
        return self.finv[n]
    
    def inverse(self, n):
        return self.fact[n - 1] * self.finv[n] % self.mod
    
    def perm(self, n, r):
        return self.fact[n] * self.finv[n - r] % self.mod if n >= r >= 0 else 0
    
    
def CF1648C():
    n, m = MII()
    a = LII()
    b = LII()
    bit = BinaryIndexedTree(2 * 10 ** 5 + 1)
    fact = Factorial(n, MOD9)
    cnt = Counter(a)
    cur = fact.factorial(n)
    for k, v in cnt.items():
        bit.update(k, v)
        cur = cur * fact.fac_inv(v) % MOD9
    
    ans = 0
    for i, x in enumerate(b):
        if i >= n:
            ans += 1
            ans %= MOD9
            break
        cur = cur * fact.inverse(n - i) % MOD9
        ans += cur * bit.query(x - 1)
        ans %= MOD9
        if cnt[x] == 0: break
        cur = cur * cnt[x] % MOD9
        cnt[x] -= 1
        bit.update(x, -1)
    print(ans)
    
if __name__ == "__main__":
    CF1648C()
