#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict

if __name__ == "__main__":
    trie = lambda: defaultdict(trie)  # 嵌套 defaultdict 来实现 Trie 树
    root = trie()

    word = ""
    cur = root  # 从根节点开始插入单词的字符
    for c in word:
        cur = cur[c]  # 移动到下一个节点
    cur[None] = True  # 标记最后一个节点为单词的结尾
