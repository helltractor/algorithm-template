#!/usr/bin/env python3

import unittest

from src.struct.trie.template import Trie, ZeroOneTrie


class TestTrie(unittest.TestCase):
    def test_insert_search(self):
        trie = Trie()
        trie.insert("hello")
        self.assertTrue(trie.search("hello"))
        self.assertFalse(trie.search("hell"))
        self.assertFalse(trie.search("world"))

    def test_starts_with(self):
        trie = Trie()
        trie.insert("hello")
        trie.insert("helium")
        self.assertTrue(trie.startsWith("hel"))
        self.assertTrue(trie.startsWith("hello"))
        self.assertFalse(trie.startsWith("hex"))

    def test_delete(self):
        trie = Trie()
        trie.insert("abc")
        trie.insert("ab")
        self.assertTrue(trie.search("abc"))
        self.assertTrue(trie.search("ab"))
        trie.delete("abc")
        self.assertFalse(trie.search("abc"))
        self.assertTrue(trie.search("ab"))

    def test_empty(self):
        trie = Trie()
        self.assertFalse(trie.search(""))
        self.assertTrue(trie.startsWith(""))


class TestZeroOneTrie(unittest.TestCase):
    def test_insert_and_max_xor(self):
        trie = ZeroOneTrie()
        trie.insert(1)
        trie.insert(5)
        self.assertEqual(trie.max_xor(4), 5)

    def test_min_xor(self):
        trie = ZeroOneTrie()
        trie.insert(2)
        trie.insert(5)
        self.assertEqual(trie.min_xor(7), 2)

    def test_search_count(self):
        trie = ZeroOneTrie()
        for x in [1, 2, 3, 4, 5]:
            trie.insert(x)
        self.assertEqual(trie.search(0, 3), 2)

    def test_remove(self):
        trie = ZeroOneTrie()
        trie.insert(3)
        trie.insert(5)
        trie.insert(7)
        trie.remove(5)
        self.assertEqual(trie.max_xor(0), 7)


if __name__ == "__main__":
    unittest.main()
