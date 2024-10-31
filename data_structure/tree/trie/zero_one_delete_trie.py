#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File : zero_one_delete_trie.py
# @Time : 2024/8/24 下午1:13


class Node:
    __slots__ = ["children", "cnt"]
    
    def __init__(self):
        self.children = [None, None]
        self.cnt = 0


class Trie:
    HIGH_BIT = 32
    
    def __init__(self):
        self.root = Node()
    
    def insert(self, val: int) -> None:
        cur = self.root
        for i in range(Trie.HIGH_BIT, -1, -1):
            bit = val >> i & 1
            if cur.children[bit] is None:
                cur.children[bit] = Node()
            cur = cur.children[bit]
            cur.cnt += 1
        return cur
    
    def remove(self, val: int) -> None:
        cur = self.root
        for i in range(Trie.HIGH_BIT, -1, -1):
            bit = val >> i & 1
            cur = cur.children[bit]
            cur.cnt -= 1
        return cur
    
    def max_xor(self, val):
        cur = self.root
        ans = 0
        for i in range(Trie.HIGH_BIT, -1, -1):
            bit = val >> i & 1
            if cur.children[bit ^ 1] and cur.children[bit ^ 1].cnt:
                ans |= 1 << i
                bit ^= 1
            cur = cur.children[bit]
        return ans
