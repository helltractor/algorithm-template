#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/09/18 上午11:31
# @Link : https://leetcode.cn/problems/find-minimum-diameter-after-merging-two-trees/solutions/2827577/xiang-jie-bo-yang-cong-da-fa-hao-by-l00-yp6l/

from typing import List


class TreeDiameter:
    
    @staticmethod
    def treeDiameterTopologicalSort(edges: List[List[int]]) -> int:
        n = len(edges) + 1
        if n == 1: return 0
        deg = [0] * (n + 1)
        mix = [0] * (n + 1)
        for u, v in edges:
            deg[u] += 1
            deg[v] += 1
            mix[u] ^= v
            mix[v] ^= u
        
        queue = [i for i, u in enumerate(deg) if u == 1]
        radius = 0
        while len(queue) > 1:
            nextQueue = []
            for u in queue:
                v = mix[u]
                mix[v] ^= u  # deg[v]=1时，mix[v]指向唯一邻居u
                deg[v] -= 1
                if deg[v] == 1: nextQueue.append(v)
            radius += 1
            queue = nextQueue
        return (radius << 1) - (len(queue) ^ 1)
