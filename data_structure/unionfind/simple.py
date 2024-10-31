# _*_ coding: utf-8 _*_
# @File : simple.py
# @Time : 2024/7/15 下午2:21


parent = list(range(n))

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    parent[find(y)] = find(x)


def connected(x, y):
    return find(x) == find(y)
