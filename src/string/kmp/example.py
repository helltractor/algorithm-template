#!/usr/bin/env python3

import unittest

from src.string.kmp.template import KMP


class TestKMP(unittest.TestCase):
    def test_single_match(self):
        kmp = KMP("hello world", "world")
        self.assertEqual(kmp.matches, [6])

    def test_multiple_matches(self):
        kmp = KMP("abababa", "aba")
        self.assertEqual(kmp.matches, [0, 2, 4])

    def test_no_match(self):
        kmp = KMP("abcdef", "xyz")
        self.assertEqual(kmp.matches, [])

    def test_pattern_longer_than_text(self):
        kmp = KMP("ab", "abcdef")
        self.assertEqual(kmp.matches, [])

    def test_overlapping_pattern(self):
        kmp = KMP("aaaaa", "aa")
        self.assertEqual(kmp.matches, [0, 1, 2, 3])

    def test_single_character(self):
        kmp = KMP("abcabc", "a")
        self.assertEqual(kmp.matches, [0, 3])

    def test_compute_nxt(self):
        kmp = KMP("", "abcab")
        nxt = kmp.computeNxt("abcab")
        self.assertEqual(nxt, [0, 0, 0, 1, 2])


if __name__ == "__main__":
    unittest.main()
