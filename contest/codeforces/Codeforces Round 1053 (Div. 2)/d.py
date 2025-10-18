from math import comb


ImportType = InputType = ConstType = 1
DecoratorType = FunctionType = 1
if ImportType:
    import os, sys, random, threading
    from random import randint, choice, shuffle
    from copy import deepcopy
    from io import BytesIO, IOBase
    from types import GeneratorType
    from functools import lru_cache, reduce
    from bisect import bisect_left, bisect_right
    from collections import Counter, defaultdict, deque
    from itertools import accumulate, combinations, permutations
    from heapq import heapify, heappop, heappush
    from typing import Generic, Iterable, Iterator, TypeVar, Union, List
    from string import ascii_lowercase, ascii_uppercase, digits
    from math import ceil, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf
    from decimal import Decimal, getcontext
    from sys import stdin, stdout, setrecursionlimit

if InputType:

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
                if not b:
                    break
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

if DecoratorType:

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


if FunctionType:
    fmax = lambda x, y: x if x > y else y
    fmin = lambda x, y: x if x < y else y

if ConstType:
    MOD1, MOD9 = 1000000007, 998244353
    RD = random.randint(MOD1, MOD1 << 1)
    D4 = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    D8 = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    Y, N = "Yes", "No"
    A, B = "Alice", "Bob"


class Factorial:
    def __init__(self, l: int = 10**6 + 5, mod: int = 10**9 + 7):
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
    def build_inv(n: int, mod: int) -> list:
        inv = [0] * (n + 1)
        inv[0] = 1
        for i in range(2, n + 1):
            inv[i] = (mod - mod // i) * inv[mod % i] % mod
        return inv

    def comb(self, n: int, r: int) -> int:
        return (
            self.fact[n] * self.finv[r] % self.mod * self.finv[n - r] % self.mod
            if n >= r >= 0
            else 0
        )

    def factorial(self, n: int) -> int:
        return self.fact[n]

    def fac_inv(self, n: int) -> int:
        return self.finv[n]

    def inverse(self, n: int) -> int:
        return self.fact[n - 1] * self.finv[n] % self.mod

    def perm(self, n: int, r: int) -> int:
        return self.fact[n] * self.finv[n - r] % self.mod if n >= r >= 0 else 0


def helltractor():
    comb = Factorial(l=2 * 10**5 + 5, mod=MOD9).comb
    for _ in range(II()):
        n = II()
        a = LII()
        ans = 1
        pre = 0
        for i in range(n // 2, -1, -1):
            x = a[i]
            if i <= n // 2:
                ans = ans * comb(n - 2 * i - pre, x) % MOD9
                pre += x
                if n - 2 * i < x or pre > n - 2 * i:
                    ans = 0
                    break
            elif x:
                ans = 0
                break
        if pre != n:
            ans = 0
        print(ans)


if __name__ == "__main__":
    helltractor()
