#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class UnionFind:
    def __init__(self, n: int) -> None:
        self.n = n
        self.parent = list(range(n))
        self.rank = [1] * n
        self.size = [1] * n

    def find(self, x: int) -> int:
        root = x
        while root != self.parent[root]:
            root = self.parent[root]
        while x != root:
            x, self.parent[x] = self.parent[x], root
        return root

    def union_by_size(self, x: int, y: int) -> None:
        x_root, y_root = self.find(x), self.find(y)
        if x_root != y_root:
            if self.size[y_root] <= self.size[x_root]:
                self.parent[y_root] = x_root
                self.size[x_root] += self.size[y_root]
            else:
                self.parent[x_root] = y_root
                self.size[y_root] += self.size[x_root]

    def union_rank(self, x: int, y: int) -> None:
        x_root, y_root = self.find(x), self.find(y)
        if x_root != y_root:
            if self.rank[y_root] <= self.rank[x_root]:
                self.parent[y_root] = x_root
            else:
                self.parent[x_root] = y_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
