#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2023/12/10 21:42


class Trie:
    __slots__ = ["son", "cnt", "is_end"]

    def __init__(self) -> None:
        self.cnt = 0
        self.son = {}
        self.is_end = False

    def insert(self, word: str) -> None:
        cur = self
        for char in word:
            if char not in cur.son:
                cur.son[char] = Trie()
            cur = cur.son[char]
            cur.cnt += 1
        cur.is_end = True

    def search(self, word: str) -> bool:
        cur = self
        for char in word:
            cur = cur.son.get(char)
            if cur is None:
                return False
        return cur.is_end

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for char in prefix:
            cur = cur.son.get(char)
            if cur is None:
                return False
        return True

    def _delete(self, cur: "Trie", word: str, index: int) -> bool:
        if index == len(word):
            if not cur.is_end:
                return False
            cur.is_end = False
            return len(cur.son) == 0  # 如果没有子节点，可以删除该节点

        char = word[index]
        node = cur.son.get(char)
        if node is None:
            return False

        should_delete = self._delete(node, word, index + 1)
        node.cnt -= 1
        if should_delete:
            del cur.son[char]

        return node.cnt == 0 and not node.is_end

    def delete(self, word: str) -> None:
        self._delete(self, word, 0)


# %%
class ZeroOneTrie:
    __slots__ = ["son", "cnt"]
    HIGH_BIT = 30

    def __init__(self) -> None:
        self.son = [None, None]
        self.cnt = 0

    def insert(self, val: int) -> None:
        cur = self
        for i in range(ZeroOneTrie.HIGH_BIT, -1, -1):
            bit = val >> i & 1
            if cur.son[bit] is None:
                cur.son[bit] = ZeroOneTrie()
            cur = cur.son[bit]
            cur.cnt += 1

    def remove(self, val: int) -> None:
        cur = self
        for i in range(ZeroOneTrie.HIGH_BIT, -1, -1):
            bit = val >> i & 1
            cur = cur.son[bit]
            cur.cnt -= 1

    def max_xor(self, val: int) -> int:
        """返回字典树中与 val 异或结果最大的值"""
        cur = self
        ans = 0
        for i in range(ZeroOneTrie.HIGH_BIT, -1, -1):
            bit = val >> i & 1
            if cur.son[bit ^ 1] and cur.son[bit ^ 1].cnt:
                ans |= 1 << i
                bit ^= 1
            cur = cur.son[bit]
        return ans

    def search(self, val: int, limit: int) -> bool:
        """返回字典树中与 val 异或结果小于 limit 的个数"""
        cur = self
        ans = 0
        for i in range(ZeroOneTrie.HIGH_BIT, -1, -1):
            if cur is None:
                return ans
            bit = val >> i & 1
            if limit >> i & 1:
                if cur.son[bit]:
                    ans += cur.son[bit].cnt
                bit ^= 1
            cur = cur.son[bit]
        return ans
