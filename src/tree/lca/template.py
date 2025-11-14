#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List


# @Link: https://leetcode.cn/problems/kth-ancestor-of-a-tree-x/solutions/2305895/mo-ban-jiang-jie-shu-shang-bei-zeng-suan-v3rw/
class LowestCommonAncestor:
    __slots__ = ["depth", "pa"]

    def __init__(self, edges: List[List[int]]) -> None:
        n = len(edges) + 1
        m = n.bit_length()
        g = [[] for _ in range(n)]
        self.depth = depth = [0] * n
        self.pa = pa = [[-1] * m for _ in range(n)]
        for x, y in edges:  # 节点编号从 0 开始
            g[x].append(y)
            g[y].append(x)

        q = [0]
        for u in q:
            for v in g[u]:
                if pa[u][0] == v:
                    continue
                pa[v][0] = u
                depth[v] = depth[u] + 1
                q.append(v)

        for i in range(m - 1):
            for x in range(n):
                if (p := pa[x][i]) != -1:
                    pa[x][i + 1] = pa[p][i]

    def get_kth_ancestor(self, x: int, k: int) -> int:
        """返回 x 的第 k 个祖先"""
        for i in range(k.bit_length()):
            if k >> i & 1:
                x = self.pa[x][i]
        return x

    def get_lca(self, x: int, y: int) -> int:
        """返回 x 和 y 的最近公共祖先（节点编号从 0 开始）"""
        if self.depth[x] > self.depth[y]:
            x, y = y, x
        y = self.get_kth_ancestor(
            y, self.depth[y] - self.depth[x]
        )  # 使 y 和 x 在同一深度
        if y == x:
            return x
        for i in range(len(self.pa[x]) - 1, -1, -1):
            px, py = self.pa[x][i], self.pa[y][i]
            if px != py:
                x, y = px, py  # 同时上跳 2**i 步
        return self.pa[x][0]


# @Link: https://leetcode.cn/problems/find-weighted-median-node-in-tree/solutions/3700556/mo-ban-zui-jin-gong-gong-zu-xian-lcapyth-6ekj/
class LcaWithWeight:
    __slots__ = ["depth", "dis", "pa", "m"]

    def __init__(self, edges: List[List[int]]) -> None:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        self.m = m = n.bit_length()
        self.depth = depth = [0] * n
        self.dis = dis = [0] * n
        self.pa = pa = [[-1] * m for _ in range(n)]

        for x, y, w in edges:
            g[x].append((y, w))
            g[y].append((x, w))

        q = [0]
        for u in q:
            for v, w in g[u]:
                if v == pa[u][0]:
                    continue
                pa[v][0] = u
                depth[v] = depth[u] + 1
                dis[v] = dis[u] + w
                q.append(v)

        for i in range(m - 1):
            for x in range(n):
                if (p := pa[x][i]) != -1:
                    pa[x][i + 1] = pa[p][i]

    def get_kth_ancestor(self, x: int, k: int) -> int:
        """返回 x 的第 k 个祖先"""
        for i in range(k.bit_length()):
            if k >> i & 1:
                x = self.pa[x][i]
                if x == -1:
                    break
        return x

    def get_lca(self, x: int, y: int) -> int:
        """返回 x 和 y 的最近公共祖先（节点编号从 0 开始）"""
        if self.depth[x] > self.depth[y]:
            x, y = y, x
        y = self.get_kth_ancestor(y, self.depth[y] - self.depth[x])
        if x == y:
            return x
        for i in reversed(range(len(self.pa[x]))):
            if self.pa[x][i] != self.pa[y][i]:
                x = self.pa[x][i]
                y = self.pa[y][i]
        return self.pa[x][0]

    def get_dis(self, x: int, y: int) -> int:
        """返回 x 和 y 之间的路径权值和（distance）"""
        return self.dis[x] + self.dis[y] - 2 * self.dis[self.get_lca(x, y)]

    def upto_dis(self, x: int, d: int) -> int:
        """返回 x 向上跳至多 d 距离能到达的最远节点"""
        dx = self.dis[x]
        for i in range(self.m - 1, -1, -1):
            p = self.pa[x][i]
            if p != -1 and dx - self.dis[p] <= d:
                x = p
        return x
