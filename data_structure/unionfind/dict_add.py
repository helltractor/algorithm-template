# _*_ coding: utf-8 _*_
# @File : dict_add.py
# @Time : 2024/7/15 下午2:25


class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.size = {}
    
    def find(self, x):
        root = x
        while self.parent[root] is not None:
            root = self.parent[root]
        while x != root:
            original_parent = self.parent[x]
            self.parent[x] = root
            x = original_parent
        return root
    
    def union_by_size(self, x, y):
        x_root, y_root = self.find(x), self.find(y)
        if x_root != y_root:
            if self.size[y_root] <= self.size[x_root]:
                self.parent[y_root] = x_root
                self.size[x_root] += self.size[y_root]
            else:
                self.parent[x_root] = y_root
                self.size[y_root] += self.size[x_root]
    
    def union_rank(self, x: int, y: int):
        x_root, y_root = self.find(x), self.find(y)
        if x_root != y_root:
            if self.rank[y_root] <= self.rank[x_root]:
                self.parent[y_root] = x_root
            else:
                self.parent[x_root] = y_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1
    
    def connected(self, x: int, y: int):
        return self.find(x) == self.find(y)
    
    def add(self, x):
        self.parent[x] = None
        self.rank[x] = 1
        self.size[x] = 1
    