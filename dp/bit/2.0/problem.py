# _*_ coding: utf-8 _*_
# @File : problem.py
# @Time : 2024/4/21 19:59
from functools import cache


class Solution:
    
    # https://leetcode.cn/problems/count-the-number-of-powerful-integers/
    @staticmethod
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        low = str(start)
        high = str(finish)
        n = len(high)
        low = '0' * (n - len(low)) + low  # 补前导零，和 high 对齐
        diff = n - len(s)

        @cache
        def dfs(i: int, limit_low: bool, limit_high: bool) -> int:
            if i == n:
                return 1

            # 第 i 个数位可以从 lo 枚举到 hi
            # 如果对数位还有其它约束，应当只在下面的 for 循环做限制，不应修改 lo 或 hi
            lo = int(low[i]) if limit_low else 0
            hi = int(high[i]) if limit_high else 9

            res = 0
            if i < diff:  # 枚举这个数位填什么
                for d in range(lo, min(hi, limit) + 1):
                    res += dfs(i + 1, limit_low and d == lo, limit_high and d == hi)
            else:  # 这个数位只能填 s[i-diff]
                x = int(s[i - diff])
                if lo <= x <= min(hi, limit):
                    res = dfs(i + 1, limit_low and x == lo, limit_high and x == hi)
            return res

        return dfs(0, True, True)

    # https://leetcode.cn/problems/number-of-beautiful-integers-in-the-range/
    @staticmethod
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        low, high = str(low), str(high)
        n = len(high)
        diff = n - len(low)
        low = '0' * diff + low

        @cache
        def dfs(i: int, cnt: int, mod: int, limit_low: bool, limit_high: bool, is_num: bool) -> int:
            if i == n:
                return cnt == mod == 0
            res = 0

            if i < diff and not is_num:  # 可以跳过当前数位
                res += dfs(i + 1, 0, 0, True, False, False)

            # 第 i 个数位可以从 lo 枚举到 hi
            # 如果对数位还有其它约束，应当只在下面的 for 循环做限制，不应修改 lo 或 hi
            lo = int(low[i]) if limit_low else 0
            hi = int(high[i]) if limit_high else 9

            for d in range(max(lo, 1 - is_num), hi + 1):  # 如果前面没有填数字，必须从 1 开始（因为不能有前导零）
                res += dfs(i + 1, cnt + 1 - (d & 1) * 2, (mod * 10 + d) % k,
                           limit_low and d == lo, limit_high and d == hi, True)
            return res

        return dfs(0, 0, 0, True, True, False)
