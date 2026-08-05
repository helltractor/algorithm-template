#!/usr/bin/env python3

import unittest

from src.struct.unionfind.template import UnionFind


class TestUnionFind(unittest.TestCase):
    def test_find(self):
        uf = UnionFind(5)
        uf.union_by_size(0, 1)
        uf.union_by_size(1, 2)
        self.assertEqual(uf.find(0), uf.find(2))
        self.assertNotEqual(uf.find(3), uf.find(0))

    def test_connected(self):
        uf = UnionFind(4)
        self.assertFalse(uf.connected(0, 1))
        uf.union_by_size(0, 1)
        self.assertTrue(uf.connected(0, 1))
        self.assertFalse(uf.connected(0, 2))

    def test_size_after_union(self):
        uf = UnionFind(5)
        uf.union_by_size(0, 1)
        uf.union_by_size(1, 2)
        root = uf.find(0)
        self.assertEqual(uf.size[root], 3)
        self.assertEqual(uf.size[uf.find(3)], 1)

    def test_union_rank(self):
        uf = UnionFind(5)
        uf.union_rank(0, 1)
        uf.union_rank(2, 3)
        self.assertTrue(uf.connected(0, 1))
        self.assertTrue(uf.connected(2, 3))
        self.assertFalse(uf.connected(1, 2))
        uf.union_rank(1, 2)
        self.assertTrue(uf.connected(0, 3))

    def test_single_element(self):
        uf = UnionFind(1)
        self.assertEqual(uf.find(0), 0)


if __name__ == "__main__":
    unittest.main()
