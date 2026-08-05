#!/usr/bin/env python3

import unittest

from src.struct.segment_tree.template import SegmentTree, LazySegmentTree


class TestSegmentTree(unittest.TestCase):
    def test_build_and_query(self):
        seg = SegmentTree(max, -10**9, [1, 3, 2, 5, 4])
        self.assertEqual(seg.prod(0, 3), 3)
        self.assertEqual(seg.prod(1, 4), 5)
        self.assertEqual(seg.all_prod(), 5)
        self.assertEqual(seg.get(2), 2)

    def test_point_update(self):
        seg = SegmentTree(min, 10**9, [1, 3, 2, 5, 4])
        seg.set(1, 0)
        self.assertEqual(seg.prod(0, 3), 0)
        self.assertEqual(seg.prod(1, 4), 0)

    def test_range_sum(self):
        seg = SegmentTree(lambda a, b: a + b, 0, [1, 2, 3, 4, 5])
        self.assertEqual(seg.prod(0, 3), 6)
        self.assertEqual(seg.prod(2, 5), 12)
        seg.set(2, 10)
        self.assertEqual(seg.prod(0, 5), 22)

    def test_size_constructor(self):
        seg = SegmentTree(lambda a, b: a + b, 0, 5)
        self.assertEqual(seg.all_prod(), 0)
        seg.set(3, 7)
        self.assertEqual(seg.get(3), 7)
        self.assertEqual(seg.prod(2, 5), 7)


class TestLazySegmentTree(unittest.TestCase):
    @staticmethod
    def _make_range_add_min_tree(arr):
        return LazySegmentTree(
            op=min,
            e=10**9,
            mapping=lambda f, x: f + x,
            composition=lambda f, g: f + g,
            idlazy=0,
            v=arr,
        )

    def test_range_add_min(self):
        seg = self._make_range_add_min_tree([3, 1, 4, 1, 5])
        seg.apply(0, 3, 10)
        self.assertEqual(seg.get(0), 13)
        self.assertEqual(seg.get(2), 14)
        self.assertEqual(seg.get(4), 5)
        self.assertEqual(seg.prod(0, 5), 1)

    def test_range_add_min_overlap(self):
        seg = self._make_range_add_min_tree([5, 5, 5, 5, 5])
        seg.apply(0, 3, -2)
        seg.apply(2, 5, -1)
        self.assertEqual(seg.get(0), 3)
        self.assertEqual(seg.get(2), 2)
        self.assertEqual(seg.get(4), 4)
        self.assertEqual(seg.prod(0, 5), 2)

    def test_point_apply(self):
        seg = self._make_range_add_min_tree([10, 20, 30])
        seg.apply(1, f=5)
        self.assertEqual(seg.get(1), 25)
        self.assertEqual(seg.get(0), 10)


if __name__ == "__main__":
    unittest.main()
