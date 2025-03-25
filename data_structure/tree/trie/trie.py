#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/12/10 21:42


class Node:
    __slots__ = ['son', 'cnt', 'is_end']

    def __init__(self):
        self.son = dict()
        self.cnt = 0
        self.is_end = False


class Trie:
    def __init__(self):
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
    
    def delete(self, word: str):
        def _delete(cur: Node, word: str, index: int) -> bool:
            if index == len(word):
                if cur.is_end:
                    cur.is_end = False
                    return len(cur.son) == 0  # 如果没有子节点，可以删除该节点
                return False
            
            char = word[index]
            if char not in cur.son:
                return False
            
            should_delete = _delete(cur.son[char], word, index + 1)
            
            if should_delete:
                del cur.son[char]
                
            cur.cnt -= 1
            return len(cur.son) == 0 and not cur.is_end
        
        _delete(self.root, word, 0)
        