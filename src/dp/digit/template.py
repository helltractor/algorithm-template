#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import lru_cache


class DigitDynamicProgramming:

    def count_numbers(self, num: int) -> int:
        nums = list(map(int, str(num)))

        @lru_cache(None)
        def dfs(i: int, mask: int, is_limit: bool, is_num: bool) -> int:
            if i == len(nums):
                return int(is_num)
            res = 0
            if not is_num:
                res = dfs(i + 1, mask, False, False)
            lo = 0 if is_num else 1
            hi = nums[i] if is_limit else 9
            for d in range(lo, hi + 1):
                if (mask >> d & 1) == 0:
                    res += dfs(i + 1, mask | (1 << d), is_limit and d == hi, True)
            return res

        ans = dfs(0, 0, True, False)
        dfs.cache_clear()
        return ans

    def count_numbers_in_range(self, low: int, high: int) -> int:
        n = len(str(high))
        diff = n - len(low)
        high = list(map(int, str(high)))
        low = list(map(int, str(low).zfill(n)))

        @lru_cache(None)
        def dfs(i: int, limit_low: bool, limit_high: bool, is_num: bool) -> int:
            if i == len(high):
                return int(is_num)
            res = 0

            if i < diff and not is_num:
                res += dfs(i + 1, True, False, False)

            lo = low[i] if limit_low else 0
            hi = high[i] if limit_high else 9

            for d in range(max(lo, 1 - is_num), hi + 1):
                res += dfs(i + 1, limit_low and d == lo, limit_high and d == hi, True)
            return res

        ans = dfs(0, True, True, False)
        dfs.cache_clear()
        return ans
