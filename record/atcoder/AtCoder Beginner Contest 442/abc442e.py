ImportType = InputType = ConstType = 1
DecoratorType = FunctionType = 1
if ImportType:
    import os, sys, random, typing
    from random import randint, choice, shuffle
    from copy import deepcopy
    from io import BytesIO, IOBase
    from types import GeneratorType
    from functools import lru_cache, reduce, cmp_to_key
    from bisect import bisect_left, bisect_right
    from collections import Counter, defaultdict, deque
    from itertools import accumulate, combinations, permutations
    from heapq import heapify, heappop, heappush
    from typing import Generic, Iterable, Iterator, TypeVar, Union, List
    from string import ascii_lowercase, ascii_uppercase, digits
    from math import ceil, floor, sqrt, isqrt, factorial, gcd, log, log10, log2, inf, pi
    from decimal import Decimal, getcontext

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
    RD = randint(MOD1, MOD1 << 1)
    D4 = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    D8 = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    Y, N = "Yes", "No"
    A, B = "Alice", "Bob"


def helltractor():
    def half(p):
        return p[1] < 0 or (p[1] == 0 and p[0] < 0)

    def cross(a, b):
        return a[0] * b[1] - a[1] * b[0]

    def check(a, b):
        ah, bh = half(a), half(b)
        if ah != bh:
            return -1 if ah < bh else 1
        val = cross(a, b)
        if val > 0:
            return -1
        elif val < 0:
            return 1
        return 0

    n, m = MII()
    a = [LII() for _ in range(n)]
    qs = [LGMI() for _ in range(m)]
    order = list(range(n))
    order.sort(key=cmp_to_key(lambda i, j: check(a[i], a[j])))
    order.reverse()
    rev = [0] * n
    for i, idx in enumerate(order):
        rev[idx] = i

    l = list(range(n))
    r = list(range(1, n + 1))
    for i in range(1, n):
        if check(a[order[i]], a[order[i - 1]]) == 0:
            l[i] = l[i - 1]
    for i in reversed(range(n - 1)):
        if check(a[order[i]], a[order[i + 1]]) == 0:
            r[i] = r[i + 1]

    for x, y in qs:
        nx, ny = rev[x], rev[y]
        mn, mx = l[nx], r[ny]
        if mn < mx:
            print(mx - mn)
        else:
            print(n - mn + mx)


if __name__ == "__main__":
    helltractor()
