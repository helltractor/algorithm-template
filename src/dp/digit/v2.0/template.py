#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/4/21 19:59

from functools import lru_cache


class DigitDynamicProgrammingTwo:

    def calculate(self, low: int, high: int) -> int:
        n = len(str(high))
        high = list(map(int, str(high)))
        low = list(map(int, str(low).zfill(n)))
        diff = n - len(low)

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
