#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/4/21 19:55

from functools import lru_cache

class DigitDynamicProgramming:
    def __init__(self):
       pass
    
    def calculate(self, num: int) -> int:
        nums = list(map(int, str(num)))

        @lru_cache(None)
        def dfs(i: int, mask: int, is_limit: bool, is_num: bool) -> int:
            if i == len(nums):
                return is_num
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
