#!/usr/bin/env python3

import unittest

from src.struct.fenwick.template import FenwickTree, FenwickTree2D


class TestFenwickTree(unittest.TestCase):
    def test_point_update_range_query(self):
        ft = FenwickTree(5)
        ft.update(1, 3)
        ft.update(3, 7)
        self.assertEqual(ft.query(1), 3)
        self.assertEqual(ft.query(3), 10)
        self.assertEqual(ft.query(5), 10)

    def test_range_query(self):
        ft = FenwickTree(10)
        for i in range(1, 11):
            ft.update(i, i)
        self.assertEqual(ft.range_query(1, 3), 6)
        self.assertEqual(ft.range_query(4, 6), 15)
        self.assertEqual(ft.range_query(1, 10), 55)

    def test_zero_updates(self):
        ft = FenwickTree(3)
        self.assertEqual(ft.query(3), 0)
        self.assertEqual(ft.range_query(1, 3), 0)


class TestFenwickTree2D(unittest.TestCase):
    def test_range_add_range_query(self):
        ft = FenwickTree2D(3, 3)
        ft.range_add(1, 1, 2, 2, 5)
        self.assertEqual(ft.range_query(1, 1, 1, 1), 5)
        self.assertEqual(ft.range_query(1, 1, 2, 2), 20)
        self.assertEqual(ft.range_query(3, 3, 3, 3), 0)

    def test_boundary(self):
        ft = FenwickTree2D(2, 2)
        ft.range_add(1, 1, 1, 1, 10)
        self.assertEqual(ft.range_query(1, 1, 1, 1), 10)
        ft.range_add(1, 2, 1, 2, 3)
        self.assertEqual(ft.range_query(1, 1, 1, 2), 13)


if __name__ == "__main__":
    unittest.main()
