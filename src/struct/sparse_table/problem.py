from heapq import heappop, heappush
from typing import List
from struct.sparse_table.template import SparseTable


class Solution:

    def lc_3691(self, nums: List[int], k: int) -> int:
        """
        link: https://leetcode.cn/problems/maximum-total-subarray-value-ii/
        """
        n = len(nums)
        h = []
        mxt = SparseTable(nums, max)
        mnt = SparseTable(nums, min)

        def query(l: int, r: int) -> int:
            return mxt.query(l, r) - mnt.query(l, r)

        for i in range(n):
            heappush(h, (-query(i, n - 1), i, n - 1))

        ans = 0
        while k:
            k -= 1
            x, l, r = heappop(h)
            ans -= x
            if l == r:
                continue
            s = query(l, r - 1)
            heappush(h, (-s, l, r - 1))
        return ans
