#!/usr/bin/env python3

import unittest

from src.struct.sorted_list.template import SortedList


class TestSortedList(unittest.TestCase):
    def test_add_and_len(self):
        sl = SortedList()
        sl.add(5)
        sl.add(1)
        sl.add(3)
        self.assertEqual(len(sl), 3)

    def test_iteration_order(self):
        sl = SortedList([5, 1, 3, 1])
        self.assertEqual(list(sl), [1, 1, 3, 5])

    def test_contains(self):
        sl = SortedList([1, 3, 5])
        self.assertIn(3, sl)
        self.assertNotIn(2, sl)

    def test_getitem(self):
        sl = SortedList([5, 2, 8, 1])
        self.assertEqual(sl[0], 1)
        self.assertEqual(sl[2], 5)
        self.assertEqual(sl[-1], 8)

    def test_bisect(self):
        sl = SortedList([1, 3, 5])
        self.assertEqual(sl.bisect_left(3), 1)
        self.assertEqual(sl.bisect_right(3), 2)
        self.assertEqual(sl.bisect_left(0), 0)
        self.assertEqual(sl.bisect_right(6), 3)

    def test_count(self):
        sl = SortedList([1, 2, 2, 3, 2])
        self.assertEqual(sl.count(2), 3)
        self.assertEqual(sl.count(1), 1)
        self.assertEqual(sl.count(9), 0)

    def test_discard(self):
        sl = SortedList([1, 2, 3])
        sl.discard(2)
        self.assertEqual(list(sl), [1, 3])
        sl.discard(99)
        self.assertEqual(list(sl), [1, 3])

    def test_remove(self):
        sl = SortedList([1, 2, 3, 2])
        sl.remove(2)
        self.assertEqual(list(sl), [1, 2, 3])
        self.assertEqual(len(sl), 3)

    def test_pop(self):
        sl = SortedList([3, 1, 2])
        self.assertEqual(sl.pop(), 3)
        self.assertEqual(sl.pop(0), 1)
        self.assertEqual(list(sl), [2])

    def test_delitem(self):
        sl = SortedList([1, 2, 3, 4])
        del sl[1]
        self.assertEqual(list(sl), [1, 3, 4])

    def test_reversed(self):
        sl = SortedList([1, 3, 2])
        self.assertEqual(list(reversed(sl)), [3, 2, 1])

    def test_large_scale(self):
        sl = SortedList()
        for i in range(500):
            sl.add(i % 100)
        self.assertEqual(len(sl), 500)
        self.assertEqual(sl[0], 0)
        self.assertEqual(sl[-1], 99)
        self.assertEqual(sl[250], 50)


if __name__ == "__main__":
    unittest.main()
