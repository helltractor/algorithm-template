#!/usr/bin/env python3

import unittest

from src.graph.dijkstra.template import Dijkstra


class TestDijkstra(unittest.TestCase):
    _graph = [
        [(1, 2), (2, 5)],
        [(0, 2), (2, 3)],
        [(0, 5), (1, 3)],
    ]

    def test_shortest_path(self):
        dis = Dijkstra.get_shortest_path(self._graph, 0)
        self.assertEqual(dis[0], 0)
        self.assertEqual(dis[1], 2)
        self.assertEqual(dis[2], 5)

    def test_get_path_to_dst(self):
        path, dist = Dijkstra.get_shortest_path_from_src_to_dst(
            self._graph, 0, 2
        )
        self.assertEqual(dist, 5)
        self.assertEqual(path, [2, 0])

    def test_shortest_path_by_bfs(self):
        g = [{1}, {0, 2}, {1}]
        dis = Dijkstra.get_shortest_path_by_bfs(g, 0)
        self.assertEqual(dis, [0, 1, 2])

    def test_cnt_of_shortest_path(self):
        g = [
            [(1, 1), (2, 2)],
            [(0, 1), (2, 1)],
            [(0, 2), (1, 1)],
        ]
        cnt, dis = Dijkstra.get_cnt_of_shortest_path(g, 0)
        self.assertEqual(dis, [0, 1, 2])
        self.assertEqual(cnt[2], 2)


if __name__ == "__main__":
    unittest.main()
