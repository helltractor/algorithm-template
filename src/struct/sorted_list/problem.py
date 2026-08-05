#!/usr/bin/env python3

from struct.sorted_list.template import SortedList


class Solution:

    @staticmethod
    def lc295_median_finder():
        """
        link: https://leetcode.cn/problems/find-median-from-data-stream/
        tag: data structure | sorted list | heap | two pointers

        Demonstrates how SortedList can replace two heaps for median queries.
        """
        sl = SortedList()
        stream = [1, 2, 3, 4, 5]
        for x in stream:
            sl.add(x)
            n = len(sl)
            if n & 1:
                print(f"median: {sl[n // 2]}")
            else:
                print(f"median: {(sl[n // 2 - 1] + sl[n // 2]) / 2}")

    @staticmethod
    def lc1825_mk_average():
        """
        link: https://leetcode.cn/problems/finding-mk-average/
        tag: data structure | sorted list | sliding window
        """
        m, k = 6, 1
        nums = [1, 3, 4, 5, 9, 2]
        sl = SortedList()
        for i, x in enumerate(nums):
            sl.add(x)
            if len(sl) > m:
                sl.discard(nums[i - m])
            if len(sl) == m:
                # Remove k smallest and k largest, average the rest
                trimmed = [sl[j] for j in range(k, m - k)]
                print(f"MK average: {sum(trimmed) // len(trimmed)}")

    @staticmethod
    def lc220_contains_duplicate_iii():
        """
        link: https://leetcode.cn/problems/contains-duplicate-iii/
        tag: sorted list | sliding window | bucket sort
        """
        nums, k, t = [1, 5, 9, 1, 5, 9], 2, 3
        sl = SortedList()
        for i, x in enumerate(nums):
            idx = sl.bisect_left(x - t)
            if idx < len(sl) and sl[idx] <= x + t:
                print(True)
                return
            sl.add(x)
            if len(sl) > k:
                sl.discard(nums[i - k])
        print(False)
