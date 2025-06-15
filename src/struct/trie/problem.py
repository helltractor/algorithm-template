#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025年6月13日 17点29分

from functools import cache
from struct.trie.template import Trie, ZeroOneTrie
from typing import List


class Solution:

    def lc_472(self, words: List[str]) -> List[str]:
        """
        link: https://leetcode.cn/problems/concatenated-words/
        """
        words.sort(key=len)
        trie = Trie()
        ans = []

        @cache
        def dfs(idx: int, trie: "Trie", word: str) -> bool:
            if idx == len(word):
                return True
            cur = trie
            for i in range(idx, len(word)):
                c = word[i]
                if c not in cur.son:
                    return False
                cur = cur.son[c]
                if cur.is_end and dfs(i + 1, trie, word):
                    return True
            return False

        for word in words:
            if dfs(0, trie, word):
                ans.append(word)
            trie.insert(word)
        return ans

    def lc_1803(self, nums: List[int], low: int, high: int) -> int:
        """
        link: https://leetcode.cn/problems/count-pairs-with-xor-in-a-range/
        """
        ans = 0
        tree = ZeroOneTrie()
        for x in nums:
            ans += tree.search(x, high + 1) - tree.search(x, low)
            tree.insert(x)
        return ans
