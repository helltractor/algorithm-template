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


class StringHash:
    def __init__(self, s: str) -> None:
        """字符串哈希，用O(n)时间预处理，用O(1)时间获取段的哈希值"""
        self.n = n = len(s)
        self.BASE = BASE = 131313  # 进制 31,131,13131
        self.MOD = MOD = 10**13 + 7  # 10**13+37 10**13+51,10**13+99
        self.h = h = [0] * (n + 1)
        self.p = p = [1] * (n + 1)
        for i in range(1, n + 1):
            p[i] = (p[i - 1] * BASE) % MOD
            h[i] = (h[i - 1] * BASE + ord(s[i - 1])) % MOD

    def get_hash(self, l: int, r: int) -> int:
        """用O(1)时间获取闭区间[l,r]（即s[l:r]）的哈希值，比切片要快"""
        return (self.h[r + 1] - self.h[l] * self.p[r - l + 1]) % self.MOD

    def get_addhash(self, l1: int, r1: int, l2: int, r2: int) -> int:
        """获取 s[l1:r1+1] 和 s[l2:r2+1] 拼接的哈希值，要求不能有重叠部分，且有先后顺序"""
        return (
            self.get_hash(l1, r1) * self.p[r2 - l2 + 1] + self.get_hash(l2, r2)
        ) % self.MOD


def helltractor():
    for _ in range(II()):
        s = I()
        t = I()
        if s == t:
            print(0)
            continue
        n = len(s)
        sh = StringHash(s)
        th = StringHash(t)
        ans = -1
        for i in range(n):
            # if sh.get_hash(0, i) == th.get_hash(n - i - 1, n - 1) and \
            # sh.get_hash(i + 1, n - 1) == th.get_hash(0, n - i - 2):
            #     ans = i + 1
            #     break
            if sh.get_addhash(i + 1, n - 1, 0, i) == th.get_hash(0, n - 1):
                ans = i + 1
                break
        print(ans)


if __name__ == "__main__":
    helltractor()
