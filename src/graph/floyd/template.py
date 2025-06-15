#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025年6月15日 01点00分

from typing import List, Tuple


class WeightedGraphForFloyd:

    def __init__(self, n: int) -> None:
        self.n = n
        self.edges = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            self.edges[i][i] = 0

    def add_edge(self, u: int, v: int, weight: int) -> None:
        assert 0 <= u < self.n and 0 <= v < self.n, "Vertex index out of bounds"

        self.edges[u][v] = min(self.edges[u][v], weight)

    def floyd_warshall(self) -> List[List[int]]:
        dst = [row[:] for row in self.edges]
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if dst[i][j] > dst[i][k] + dst[k][j]:
                        dst[i][j] = dst[i][k] + dst[k][j]
        return dst
