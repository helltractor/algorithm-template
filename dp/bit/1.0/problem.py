# _*_ coding: utf-8 _*_
# @File : problem.py
# @Time : 2024/4/21 19:56
from functools import cache


class Solution:

    # https://leetcode.cn/problems/count-special-integers/
    @staticmethod
    def countSpecialNumbers(self, n: int) -> int:
        s = str(n)

        @cache  # 记忆化搜索
        def f(i, mask, is_limit, is_num):
            if i == len(s):
                return int(is_num)  # is_num 为 True 表示得到了一个合法数字
            ret = 0
            if not is_num:  # 可以跳过当前数位
                ret = f(i + 1, mask, False, False)
            # low = 1 - int(is_num)
            low = 0 if is_num else 1  # 如果前面没有填数字，必须从 1 开始（因为不能有前导零）
            up = int(s[i]) if is_limit else 9  # 如果前面填的数字都和 n 的一样，那么这一位至多填 s[i]（否则就超过 n 啦）
            for d in range(low, up + 1):  # 枚举要填入的数字 d
                if (mask >> d & 1) == 0:  # d 不在 mask 中
                    ret += f(i + 1, mask | (1 << d), is_limit and d == up, True)
            return ret

        return f(0, 0, True, False)
