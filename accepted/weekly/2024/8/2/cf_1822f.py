from types import GeneratorType

ImportType = InputType = ConstType = 1
if ImportType:
    import os, sys, random, threading
    from random import randint, choice, shuffle
    from copy import deepcopy
    from functools import lru_cache, reduce
    from bisect import bisect_left, bisect_right
    from collections import Counter, defaultdict, deque
    from itertools import accumulate, combinations, permutations
    from heapq import heapify, heappop, heappush, heappushpop
    from typing import Generic, Iterable, Iterator, TypeVar, Union, List
    from string import ascii_lowercase, ascii_uppercase, digits
    from math import ceil, comb, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf
    from decimal import Decimal, getcontext
    from sys import stdin, stdout, setrecursionlimit

if InputType:
    input = lambda: sys.stdin.readline().rstrip("\r\n")
    I = lambda: input()
    II = lambda: int(input())
    MII = lambda: map(int, input().split())
    LI = lambda: list(input().split())
    LII = lambda: list(map(int, input().split()))
    GMI = lambda: map(lambda x: int(x) - 1, input().split())
    LGMI = lambda: list(map(lambda x: int(x) - 1, input().split()))

if ConstType:
    RD = random.randint(10 ** 9, 2 * 10 ** 9)
    MOD = 998244353
    inf = 10 ** 18
    Y = "Yes"
    N = "No"


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


def CF1822F():
    for _ in range(II()):
        n, k, c = MII()
        g = [[] for _ in range(n)]
        for _ in range(n - 1):
            u, v = GMI()
            g[u].append((v, k))
            g[v].append((u, k))
        
        nodes = [None] * n
        
        @bootstrap
        def dfs(x, fa):
            p = -1
            mx = 0
            mx2 = 0
            for y, w in g[x]:
                if y == fa:
                    continue
                tmp = yield dfs(y, x)
                tmp += w
                if tmp > mx:
                    mx2 = mx
                    mx = tmp
                    p = y
                elif tmp > mx2:
                    mx2 = tmp
            nodes[x] = (p, mx, mx2)
            yield mx
        
        dfs(0, -1)
        
        def reroot(x, fa, up, cost):
            nonlocal ans
            ans = max(ans, max(up, nodes[x][1]) - cost)
            for y, w in g[x]:
                if y == fa:
                    continue
                if y == nodes[x][0]:
                    tmp = max(up, nodes[x][2])
                else:
                    tmp = max(up, nodes[x][1])
                reroot(y, x, tmp + w, cost + c)
        
        ans = nodes[0][1]
        # reroot(0, -1, 0, 0)
        
        q = deque([(0, -1, 0, 0)])
        while q:
            for _ in range(len(q)):
                x, fa, up, cost = q.popleft()
                ans = max(ans, max(up, nodes[x][1]) - cost)
                for y, w in g[x]:
                    if y == fa:
                        continue
                    if y == nodes[x][0]:
                        tmp = max(up, nodes[x][2])
                    else:
                        tmp = max(up, nodes[x][1])
                    q.append([y, x, tmp + w, cost + c])
        print(ans)


if __name__ == '__main__':
    CF1822F()
