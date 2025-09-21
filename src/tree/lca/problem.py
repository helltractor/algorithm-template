#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List
from util.io.fast_io import II, LGMI, MOD1
from src.tree.lca.template import LcaWithWeight, LowestCommonAncestor


class Solution:

    def lc_3553(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        g = LcaWithWeight(edges)
        return [
            (g.get_dis(a, b) + g.get_dis(b, c) + g.get_dis(a, c)) // 2
            for a, b, c in queries
        ]

    def lc_3585(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        g = LcaWithWeight(edges)
        ans = [0] * len(queries)
        for i, (u, v) in enumerate(queries):
            if u == v:
                ans[i] = u
                continue
            lca = g.get_lca(u, v)
            dis_uv = g.dis[u] + g.dis[v] - 2 * g.dis[lca]
            half = (dis_uv + 1) // 2
            if g.dis[u] - g.dis[lca] < half:
                ans[i] = g.upto_dis(v, dis_uv - half)
            else:
                to = g.upto_dis(u, half - 1)
                ans[i] = g.pa[to][0]
        return ans

    def cf_2117f():
        for _ in range(II()):
            n = II()
            leaf = []
            degreee = [0] * n
            e = [LGMI() for _ in range(n - 1)]
            for u, v in e:
                degreee[u] += 1
                degreee[v] += 1
            for i in range(1, n):
                if degreee[i] == 1:
                    leaf.append(i)
            if len(leaf) > 2:
                print(0)
            elif len(leaf) == 1:
                print(pow(2, n, MOD1))
            else:
                g = LowestCommonAncestor(e)
                x, y = leaf
                lca_xy = g.get_lca(x, y)
                diff_x = g.depth[x] - g.depth[lca_xy]
                diff_y = g.depth[y] - g.depth[lca_xy]
                if diff_x == diff_y:
                    print(pow(2, g.depth[lca_xy] + 2, MOD1))
                else:
                    print(
                        3 * pow(2, g.depth[lca_xy] + abs(diff_x - diff_y), MOD1) % MOD1
                    )
        return
