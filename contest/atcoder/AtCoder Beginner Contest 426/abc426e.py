ImportType = InputType = ConstType = 1
from typing import Tuple
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


def distance_square(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def subtract(a: Tuple[float, float], b: Tuple[float, float]) -> Tuple[float, float]:
    return (a[0] - b[0], a[1] - b[1])


def distance(a: Tuple[float, float], b: Tuple[float, float]) -> float:
    d = subtract(a, b)
    return sqrt(d[0] ** 2 + d[1] ** 2)


def internal_division(
    a: Tuple[float, float], b: Tuple[float, float], p: float
) -> Tuple[float, float]:
    x = a[0] + (b[0] - a[0]) * p
    y = a[1] + (b[1] - a[1]) * p
    return (x, y)


NUM_ITERATION = 60


def dist_segment_and_origin(a: Tuple[float, float], b: Tuple[float, float]) -> float:
    def f(p: float) -> float:
        return distance(internal_division(a, b, p), (0, 0))

    l, r = 0.0, 1.0
    for _ in range(NUM_ITERATION):
        ml = (l * 2 + r) / 3
        mr = (l + r * 2) / 3
        if f(ml) < f(mr):
            r = mr
        else:
            l = ml
    return f(l)


def helltractor():
    for _ in range(II()):
        a = [None, None]
        b = [None, None]
        for i in range(2):
            ax, ay, bx, by = MII()
            a[i] = (ax, ay)
            b[i] = (bx, by)

        if distance_square(a[0], b[0]) < distance_square(a[1], b[1]):
            a[0], a[1] = a[1], a[0]
            b[0], b[1] = b[1], b[0]
        ta = (float(a[0][0]), float(a[0][1]))
        tb = (float(b[0][0]), float(b[0][1]))
        sa = (float(a[1][0]), float(a[1][1]))
        sb = (float(b[1][0]), float(b[1][1]))
        tm = internal_division(ta, tb, distance(sa, sb) / distance(ta, tb))
        d1 = dist_segment_and_origin(subtract(ta, sa), subtract(tm, sb))
        d2 = dist_segment_and_origin(subtract(tm, sb), subtract(tb, sb))
        print(f"{min(d1, d2):.10f}")


if __name__ == "__main__":
    helltractor()
