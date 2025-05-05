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


def B_TLE():
    for _ in range(II()):
        n = II()
        a = LII()
        arr = [[0] * 20 for _ in range(n + 1)]
        for i in range(n):
            x = a[i]
            for j in range(20):
                if x >> j & 1:
                    arr[i + 1][j] += 1
                arr[i + 1][j] += arr[i][j]
        ans = n
        print(arr)
        for k in range(1, n):
            flag = True
            for i in range(1, n - k + 1):
                for j in range(20):
                    if arr[k][j]:
                        if arr[i + k][j] - arr[i][j] == 0:
                            flag = False
                            break
                    else:
                        if arr[i + k][j] - arr[i][j] != 0:
                            flag = False
                            break
                if not flag:
                    break
            if flag:
                ans = k
                break
        print(ans)


def check(arr, n, k):
    flag = True
    for i in range(1, n - k + 1):
        for j in range(20):
            if arr[k][j]:
                if arr[i + k][j] - arr[i][j] == 0:
                    flag = False
                    break
            else:
                if arr[i + k][j] - arr[i][j] != 0:
                    flag = False
                    break
        if not flag:
            return False
    return True


def B_BinarySearch():
    for _ in range(II()):
        n = II()
        a = LII()
        arr = [[0] * 20 for _ in range(n + 1)]
        for i in range(n):
            x = a[i]
            for j in range(20):
                if x >> j & 1:
                    arr[i + 1][j] += 1
                arr[i + 1][j] += arr[i][j]
        
        l = 1
        r = n
        while l <= r:
            m = l + r >> 1
            if check(arr, n, m):
                r = m - 1
            else:
                l = m + 1
        print(l)


def B():
    for _ in range(II()):
        n = II()
        a = LII()
        mx = max(a)
        arr = [[0] * mx.bit_length() for _ in range(n)]
        for i in range(n):
            for j in range(mx.bit_length()):
                if a[i] >> j & 1:
                    arr[i][j] += 1
        mat = list(zip(*arr))
        ans = 1
        for row in mat:
            cnt = 0
            tmp = 0
            for x in row:
                if x == 0:
                    tmp += 1
                else:
                    cnt = max(cnt, tmp)
                    tmp = 0
            if tmp == len(row):
                continue
            cnt = max(cnt, tmp)
            ans = max(cnt + 1, ans)
        print(ans)


if __name__ == '__main__':
    B_BinarySearch()
