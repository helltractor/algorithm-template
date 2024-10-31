# _*_ coding: utf-8 _*_
# @File : dict.py
# @Time : 2024/7/15 下午2:20


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = {}
        self.rank = [1] * n
        self.size = [1] * n

    def find(self, x):
        self.parent.setdefault(x, x)
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
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
    