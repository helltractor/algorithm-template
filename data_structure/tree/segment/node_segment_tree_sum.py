#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2025/1/6 下午5:00


class Node:
    __slots__ = ['ls', 'rs', 'sum', 'add']
    
    def __init__(self) -> None:
        self.ls = self.rs = None
        self.sum = 0
        self.add = 0


class SegmentTree:
    __slots__ = 'root'
    
    def __init__(self):
        self.root = Node()
    
    @staticmethod
    def update(node: Node, lc: int, rc: int, l: int, r: int, v: int) -> None:
        if l <= lc and rc <= r:
            node.sum += (rc - lc + 1) * v
            node.add += v
            return
        SegmentTree.pushdown(node, lc, rc)
        mid = (lc + rc) >> 1
        if l <= mid:
            SegmentTree.update(node.ls, lc, mid, l, r, v)
        if r > mid:
            SegmentTree.update(node.rs, mid + 1, rc, l, r, v)
        SegmentTree.pushup(node)
    
    @staticmethod
    def query(node: Node, lc: int, rc: int, l: int, r: int) -> int:
        if l <= lc and rc <= r:
            return node.sum
        SegmentTree.pushdown(node, lc, rc)
        mid, total = (lc + rc) >> 1, 0
        if l <= mid:
            total += SegmentTree.query(node.ls, lc, mid, l, r)
        if r > mid:
            total += SegmentTree.query(node.rs, mid + 1, rc, l, r)
        return total
    
    @staticmethod
    def pushdown(node: Node, lc: int, rc: int) -> None:
        if node.ls is None:
            node.ls = Node()
        if node.rs is None:
            node.rs = Node()
        if node.add != 0:
            mid = (lc + rc) >> 1
            node.ls.sum += node.add * (mid - lc + 1)
            node.rs.sum += node.add * (rc - mid)
            node.ls.add += node.add
            node.rs.add += node.add
            node.add = 0
    
    @staticmethod
    def pushup(node: Node) -> None:
        node.sum = (node.ls.sum if node.ls else 0) + (node.rs.sum if node.rs else 0)
