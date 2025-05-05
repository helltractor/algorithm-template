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


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.Time = 0
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def bridgeUtil(self, u, visited, parent, low, disc, bridges):
        visited[u] = True
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1
        
        for v in self.graph[u]:
            if not visited[v]:
                parent[v] = u
                self.bridgeUtil(v, visited, parent, low, disc, bridges)
                low[u] = min(low[u], low[v])
                
                if low[v] > disc[u]:
                    bridges.append((u, v))
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])
    
    def findBridges(self):
        visited = [False] * (self.V + 1)
        disc = [float('Inf')] * (self.V + 1)
        low = [float('Inf')] * (self.V + 1)
        parent = [-1] * (self.V + 1)
        bridges = []
        
        for i in range(1, self.V + 1):
            if not visited[i]:
                self.bridgeUtil(i, visited, parent, low, disc, bridges)
        
        return bridges
    
    def dfsCount(self, v, visited):
        count = 1
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                count += self.dfsCount(i, visited)
        return count
    
    def minRemoveEdge(self):
        bridges = self.findBridges()
        min_pairs = float('Inf')
        
        for u, v in bridges:
            self.graph[u].remove(v)
            self.graph[v].remove(u)
            
            visited = [False] * (self.V + 1)
            size1 = self.dfsCount(u, visited)
            size2 = self.V - size1
            
            min_pairs = min(min_pairs, size1 * (size1 - 1) // 2 + size2 * (size2 - 1) // 2)
            
            self.graph[u].append(v)
            self.graph[v].append(u)
        
        return min_pairs


def F():
    for _ in range(II()):
        n, m = MII()
        g = Graph(n)
        for _ in range(m):
            u, v = GMI()
            g.addEdge(u, v)
        print(g.minRemoveEdge())


if __name__ == '__main__':
    F()
