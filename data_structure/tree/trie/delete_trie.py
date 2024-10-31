# _*_ coding: utf-8 _*_
# @File : delete_trie.py
# @Time : 2024/8/5 下午1:58


class Node:
    __slots__ = ['children', 'is_end_of_word']
    
    def __init__(self):
        self.children = {}  # 存储子节点的字典，键是字符，值是Node
        self.is_end_of_word = False  # 标记当前节点是否是一个单词的结尾


class Trie:
    __slots__ = ['root']
    
    def __init__(self):
        self.root = Node()  # 创建根节点
    
    def insert(self, word: str) -> None:
        cur = self.root  # 从根节点开始插入单词的字符
        for char in word:
            if char not in cur.children:
                cur.children[char] = Node()  # 如果字符不存在，创建一个新节点
            cur = cur.children[char]  # 移动到下一个节点
        cur.is_end_of_word = True  # 标记最后一个节点为单词的结尾
    
    def search(self, word: str) -> bool:
        cur = self.root  # 从根节点开始搜索单词
        for char in word:
            if char not in cur.children:
                return False  # 如果字符不存在，单词不存在
            cur = cur.children[char]  # 移动到下一个节点
        return cur.is_end_of_word  # 返回最后一个节点是否标记为单词的结尾
    
    def starts_with(self, prefix: str) -> bool:  # 检查是否存在以给定前缀开头的单词
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True
    
    def delete(self, word: str):
        def _delete(cur: Node, word: str, index: int) -> bool:
            if index == len(word):
                if cur.is_end_of_word:
                    cur.is_end_of_word = False
                    return not bool(cur.children)  # 如果没有子节点，可以删除该节点
                return False
            
            char = word[index]
            if char not in cur.children:
                return False
            
            should_delete = _delete(cur.children[char], word, index + 1)
            
            if should_delete:
                del cur.children[char]
                return not bool(cur.children)
            return False
        
        _delete(self.root, word, 0)
