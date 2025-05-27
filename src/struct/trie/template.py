#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/12/10 21:42


class Node:
    __slots__ = ["son", "cnt", "is_end"]

    def __init__(self) -> None:
        self.cnt = 0
        self.son = dict()
        self.is_end = False


class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.son:
                cur.son[char] = Node()
            cur = cur.son[char]
            cur.cnt += 1
        cur.is_end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            cur = cur.son.get(char)
            if cur is None:
                return False
        return cur.is_end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            cur = cur.son.get(char)
            if cur is None:
                return False
        return True

    def _delete(self, cur: Node, word: str, index: int) -> bool:
        if index == len(word):
            if cur.is_end:
                cur.is_end = False
                return len(cur.son) == 0  # 如果没有子节点，可以删除该节点
            return False

        char = word[index]
        if char not in cur.son:
            return False

        should_delete = self._delete(cur.son[char], word, index + 1)

        if should_delete:
            del cur.son[char]

        cur.cnt -= 1
        return len(cur.son) == 0 and not cur.is_end

    def delete(self, word: str):
        self._delete(self.root, word, 0)


class Node:
    __slots__ = ["son", "cnt"]

    def __init__(self) -> None:
        self.cnt = 0
        self.son = [None, None]


class ZeroOneTrie:
    HIGH_BIT = 32

    def __init__(self) -> None:
        self.root = Node()

    def insert(self, val: int) -> None:
        cur = self.root
        for i in range(Trie.HIGH_BIT, -1, -1):
            bit = val >> i & 1
            if cur.son[bit] is None:
                cur.son[bit] = Node()
            cur = cur.son[bit]
            cur.cnt += 1
        return cur

    def remove(self, val: int) -> None:
        cur = self.root
        for i in range(Trie.HIGH_BIT, -1, -1):
            bit = val >> i & 1
            cur = cur.son[bit]
            cur.cnt -= 1
        return cur

    def max_xor(self, val: int) -> int:
        cur = self.root
        ans = 0
        for i in range(Trie.HIGH_BIT, -1, -1):
            bit = val >> i & 1
            if cur.son[bit ^ 1] and cur.son[bit ^ 1].cnt:
                ans |= 1 << i
                bit ^= 1
            cur = cur.son[bit]
        return ans
