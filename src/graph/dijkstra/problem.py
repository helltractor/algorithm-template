#!/usr/bin/env python3

from math import inf

from graph.dijkstra.template import Dijkstra


class Solution:

    @staticmethod
    def lc743_network_delay_time():
        """
        link: https://leetcode.cn/problems/network-delay-time/
        tag: graph | dijkstra | shortest path
        """
        times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
        n, k = 4, 2
        dct = [[] for _ in range(n + 1)]
        for u, v, w in times:
            dct[u].append((v, w))
        dis = Dijkstra.get_shortest_path(dct, k, initial=0)
        ans = max(dis[1:])
        print(ans if ans < inf else -1)

    @staticmethod
    def lc1514_path_max_probability():
        """
        link: https://leetcode.cn/problems/path-with-maximum-probability/
        tag: graph | dijkstra | maximum product path
        """
        n = 3
        edges = [[0, 1], [1, 2], [0, 2]]
        succProb = [0.5, 0.5, 0.2]
        start, end = 0, 2
        dct = [{} for _ in range(n)]
        for (u, v), w in zip(edges, succProb):
            dct[u][v] = w
            dct[v][u] = w
        ans = Dijkstra.gen_maximum_product_path(dct, start, end)
        print(f"{ans:.5f}")

    @staticmethod
    def lc1976_number_of_ways():
        """
        link: https://leetcode.cn/problems/number-of-ways-to-arrive-at-destination/
        tag: graph | dijkstra | count shortest paths
        """
        n = 7
        roads = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3],
                 [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1],
                 [0, 4, 5], [4, 6, 2]]
        dct = [[] for _ in range(n)]
        for u, v, w in roads:
            dct[u].append((v, w))
            dct[v].append((u, w))
        mod = 10 ** 9 + 7
        cnt, _ = Dijkstra.get_cnt_of_shortest_path(dct, 0, mod)
        print(cnt[n - 1] % mod)
