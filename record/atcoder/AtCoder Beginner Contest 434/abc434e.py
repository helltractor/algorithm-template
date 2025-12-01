ImportType = InputType = ConstType = 1
DecoratorType = FunctionType = 1
if ImportType:
    import os, sys, random
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


class UnionFind:
    def __init__(self, n: int) -> None:
        self.n = n
        self.parent = list(range(n))
        self.edge = [0] * n
        self.size = [1] * n

    def find(self, x: int) -> int:
        root = x
        while root != self.parent[root]:
            root = self.parent[root]
        while x != root:
            x, self.parent[x] = self.parent[x], root
        return root

    def union(self, x: int, y: int) -> None:
        x_root, y_root = self.find(x), self.find(y)
        if x_root != y_root:
            self.parent[y_root] = x_root
            self.size[x_root] += self.size[y_root]
            self.edge[x_root] += self.edge[y_root] + 1
        else:
            self.edge[x_root] += 1

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


# https://atcoder.jp/contests/abc434/editorial/14690
def helltractor():
    n = II()
    a = [LII() for _ in range(n)]
    st = set()
    for x, r in a:
        st.add(x + r)
        st.add(x - r)

    m = len(st)
    b = sorted(st)
    rd = {x: i for i, x in enumerate(b)}
    uf = UnionFind(m)
    for x, r in a:
        uf.union(rd[x + r], rd[x - r])

    ans = 0
    for i in range(m):
        if uf.parent[i] == i:
            ans += fmin(uf.edge[i], uf.size[i])
    print(ans)


if __name__ == "__main__":
    helltractor()
