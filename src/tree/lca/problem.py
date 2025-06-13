#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2025年5月18日 15点19分

from typing import List
from template.codeforces.template import II, LGMI, MOD1
from src.tree.lca.template import LcaWithWeight, LowestCommonAncestor


class Solution:

    def lc_3553(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        lca = LcaWithWeight(edges)
        return [
            (lca.get_dis(a, b) + lca.get_dis(b, c) + lca.get_dis(a, c)) // 2
            for a, b, c in queries
        ]

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
                lca = LowestCommonAncestor(e)
                x, y = leaf
                lca_xy = lca.get_lca(x, y)
                diff_x = lca.depth[x] - lca.depth[lca_xy]
                diff_y = lca.depth[y] - lca.depth[lca_xy]
                if diff_x == diff_y:
                    print(pow(2, lca.depth[lca_xy] + 2, MOD1))
                else:
                    print(3 * pow(2, lca.depth[lca_xy] + abs(diff_x - diff_y), MOD1) % MOD1)
        return
