ImportType = InputType = ConstType = 1
DecoratorType = FunctinoType = 1
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


if FunctinoType:
    fmax = lambda x, y: x if x > y else y
    fmin = lambda x, y: x if x < y else y

if ConstType:
    MOD1, MOD9 = 1000000007, 998244353
    RD = random.randint(MOD1, MOD1 << 1)
    D4 = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    D8 = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    Y, N = "Yes", "No"
    A, B = "Alice", "Bob"


# def helltractor():
#     for _ in range(II()):
#         n = II()
#         g = [[] for _ in range(n)]
#         for _ in range(n - 1):
#             u, v = GMI()
#             g[u].append(v)
#             g[v].append(u)

#         if n <= 2:
#             print(0)
#             continue

#         # cs[i]: 以i为根的子树中深度>1的叶子数
#         # cs1[i]: 以i为根的子树中度数为1的子节点数
#         # cs2[i]: 以i为根的子树中深度>1的叶子数（不包括度数为1的直接子节点）
#         cs = [0] * n
#         cs1 = [0] * n
#         cs2 = [0] * n
#         ans = [0] * n

#         def dfs(x, fa):
#             c = c1 = c2 = 0
#             for y in g[x]:
#                 if y == fa:
#                     continue
#                 dfs(y, x)
#                 cc = cs[y]
#                 if cc == 0:
#                     c += 1
#                     c1 += 1
#                 else:
#                     c += cc
#                     c2 += cc

#             cs[x] = c
#             cs1[x] = c1
#             cs2[x] = c2

#         def dfs1(u, parent, up_c1, up_c2):
#             ans[u] = cs2[u] + up_c2

#             for v in g[u]:
#                 if v != parent:
#                     if len(g[u]) == 1:
#                         dfs1(v, u, 1, 0)
#                     else:
#                         new_c2 = up_c1 + up_c2 + cs[u] - cs[v]
#                         dfs1(v, u, 0, new_c2)

#         dfs(0, -1)
#         dfs1(0, -1, 0, 0)
#         print(min(ans))


def helltractor():
    for _ in range(II()):
        n = II()
        g = [[] for _ in range(n)]
        for _ in range(n - 1):
            u, v = GMI()
            g[u].append(v)
            g[v].append(u)

        if n <= 2:
            print(0)
            continue

        leaf = 0
        mx = 0

        for x in range(n):
            connected = 0
            if len(g[x]) == 1:
                leaf += 1
                connected += 1

            for y in g[x]:  # x的邻居中的叶子
                if len(g[y]) == 1:
                    connected += 1
            mx = max(mx, connected)

        print(leaf - mx)


if __name__ == "__main__":
    helltractor()
