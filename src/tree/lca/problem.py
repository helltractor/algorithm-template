#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2025年5月18日 15点19分

from typing import List
from src.tree.lca.template import LcaWithWeight

class Solution:

    def lc_3553(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        lca = LcaWithWeight(edges)
        return [(lca.get_dis(a, b) + lca.get_dis(b, c) + lca.get_dis(a, c)) // 2 for a, b, c in queries]
