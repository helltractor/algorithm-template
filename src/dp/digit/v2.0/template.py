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

            if i < diff and not is_num:  # 可以跳过当前数位
                res += dfs(i + 1, True, False, False)

            # 第 i 个数位可以从 lo 枚举到 hi
            # 如果对数位还有其它约束，应当只在下面的 for 循环做限制，不应修改 lo 或 hi
            lo = low[i] if limit_low else 0
            hi = high[i] if limit_high else 9

            for d in range(max(lo, 1 - is_num), hi + 1):  # 如果前面没有填数字，必须从 1 开始（因为不能有前导零）
                res += dfs(i + 1, limit_low and d == lo, limit_high and d == hi, True)
            return res
        
        ans = dfs(0, True, True, False)
        dfs.cache_clear()
        return ans
    