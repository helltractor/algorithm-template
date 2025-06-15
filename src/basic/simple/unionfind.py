#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2024/7/15 下午2:21

if __name__ == "__main__":
    n = int(input())
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
