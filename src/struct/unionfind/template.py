#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class UnionFind:
    def __init__(self, n: int) -> None:
        self.fa = list(range(n))
        self.rank = [1] * n
        self.size = [1] * n

    def find(self, x: int) -> int:
        while x != self.fa[x]:
            self.fa[x] = self.fa[self.fa[x]]
            x = self.fa[x]
        return x

    def union_by_size(self, x: int, y: int) -> None:
        x_root, y_root = self.find(x), self.find(y)
        if x_root != y_root:
            if self.size[y_root] <= self.size[x_root]:
                self.fa[y_root] = x_root
                self.size[x_root] += self.size[y_root]
            else:
                self.fa[x_root] = y_root
                self.size[y_root] += self.size[x_root]

    def union_rank(self, x: int, y: int) -> None:
        x_root, y_root = self.find(x), self.find(y)
        if x_root != y_root:
            if self.rank[y_root] <= self.rank[x_root]:
                self.fa[y_root] = x_root
            else:
                self.fa[x_root] = y_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


# @Author: 0x3f
# @Link: https://leetcode.cn/circle/discuss/mOr1u6/


class WeightedUnionFind:
    def __init__(self, n: int) -> None:
        self.fa = list(range(n))
        self.dis = [0] * n

    def find(self, x: int) -> int:
        root, tot = x, 0
        while self.fa[root] != root:
            tot += self.dis[root]
            root = self.fa[root]

        while self.fa[x] != root:
            fa, tmp = self.fa[x], self.dis[x]
            self.dis[x] = tot
            tot -= tmp
            self.fa[x] = root
            x = fa
        return root

    def union(self, x: int, y: int, v: int) -> bool:
        x_root, y_root = self.find(x), self.find(y)
        dis = self.dis
        if x_root == y_root:
            return dis[x] - dis[y] == v
        dis[x_root] = v + dis[y] - dis[x]
        self.fa[x_root] = y_root
        return True

    def get_dis(self, x: int, y: int) -> int:
        self.find(x)
        self.find(y)
        return self.dis[x] - self.dis[y]

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
