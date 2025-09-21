#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @link: https://leetcode.cn/problems/find-minimum-diameter-after-merging-two-trees/solutions/2827577/xiang-jie-bo-yang-cong-da-fa-hao-by-l00-yp6l/

from typing import List


class TreeDiameter:

    @staticmethod
    def treeDiameterDFS(edges: List[List[int]]) -> int:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(x: int, fa: int) -> int:
            nonlocal diameter
            max_len = 0
            for y in g[x]:
                if y == fa:
                    continue
                sub_len = dfs(y, x) + 1
                diameter = max(diameter, max_len + sub_len)
                max_len = max(max_len, sub_len)
            return max_len

        diameter = 0
        dfs(0, -1)
        return diameter

    @staticmethod
    def treeDiameterTopologicalSort(edges: List[List[int]]) -> int:
        n = len(edges) + 1
        deg = [0] * (n + 1)
        mix = [0] * (n + 1)
        for u, v in edges:
            deg[u] += 1
            deg[v] += 1
            mix[u] ^= v
            mix[v] ^= u

        radius = 0
        q = [i for i, u in enumerate(deg) if u == 1]
        while len(q) > 1:
            nq = []
            for u in q:
                v = mix[u]  # deg[v]=1时，mix[v]指向唯一邻居u
                mix[v] ^= u
                deg[v] -= 1
                if deg[v] == 1:
                    nq.append(v)
            q = nq
            radius += 1
        return (radius << 1) - (len(q) ^ 1)
