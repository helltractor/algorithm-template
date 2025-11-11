#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import defaultdict
from heapq import heappop, heappush, heappushpop


# link: https://leetcode.cn/circle/discuss/mOr1u6/
class LazyHeap:
    def __init__(self):
        self.heap = []  # 最小堆（最大堆可以把数字取反或重载 __lt__）
        self.remove_cnt = defaultdict(int)  # 每个元素剩余需要删除的次数
        self.size = 0  # 堆的实际大小
        self.sum = 0

    def remove(self, x: int) -> None:
        self.remove_cnt[x] += 1  # 懒删除
        self.size -= 1
        self.sum -= x

    def _apply_remove(self) -> None:
        while self.heap and self.remove_cnt[self.heap[0]] > 0:
            self.remove_cnt[self.heap[0]] -= 1
            heappop(self.heap)

    def top(self) -> int:
        self._apply_remove()
        return self.heap[0]  # 真正的堆顶

    def pop(self) -> int:
        self._apply_remove()
        self.size -= 1
        self.sum -= self.heap[0]
        return heappop(self.heap)

    def push(self, x: int) -> None:
        if self.remove_cnt[x] > 0:
            self.remove_cnt[x] -= 1  # 抵消之前的删除
        else:
            heappush(self.heap, x)
        self.size += 1
        self.sum += x

    def pushpop(self, x: int) -> int:
        self._apply_remove()
        if not self.heap or x <= self.heap[0]:
            return
        self.sum += x - self.heap[0]
        return heappushpop(self.heap, x)
