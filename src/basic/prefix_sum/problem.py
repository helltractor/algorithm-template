#!/usr/bin/env python3

from itertools import accumulate


class Solution:

    @staticmethod
    def lc303_range_sum_query():
        """
        link: https://leetcode.cn/problems/range-sum-query-immutable/
        tag: array | prefix sum
        """
        nums = [-2, 0, 3, -5, 2, -1]
        pre = list(accumulate(nums, initial=0))
        # query [2, 5): pre[5] - pre[2] = 0
        left, right = 2, 5
        print(pre[right] - pre[left])

    @staticmethod
    def lc560_subarray_sum_equals_k():
        """
        link: https://leetcode.cn/problems/subarray-sum-equals-k/
        tag: array | hash map | prefix sum
        """
        from collections import Counter

        nums, k = [1, 1, 1], 2
        cnt = Counter([0])
        pre = ans = 0
        for x in nums:
            pre += x
            ans += cnt[pre - k]
            cnt[pre] += 1
        print(ans)

    @staticmethod
    def lc238_product_of_array_except_self():
        """
        link: https://leetcode.cn/problems/product-of-array-except-self/
        tag: array | prefix product | suffix product
        """
        nums = [1, 2, 3, 4]
        n = len(nums)
        ans = [1] * n
        # prefix product from left
        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]
        # multiply suffix product from right
        suffix = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]
        print(ans)
