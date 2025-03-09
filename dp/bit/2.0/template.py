#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/4/21 19:59

"""
    上下边界数位dp模板
    limitHigh 表示当前是否受到了 finish 的约束（我们要构造的数字不能超过 finish。若为真，则第 iii 位填入的数字至多为 finish[i]，否则至多为 9，
    这个数记作 hi。如果在受到约束的情况下填了 finish[i]，那么后续填入的数字仍会受到 finish 的约束。例如 finish=123，那么 i=0 填的是 1 的话，i=1 的这一位至多填 2。

    limitLow 表示当前是否受到了 start 的约束（我们要构造的数字不能低于 start。若为真，则第 i 位填入的数字至少为 start[i]，否则至少为 0，这个数记作 lo。
    如果在受到约束的情况下填了 start[i]，那么后续填入的数字仍会受到 start 的约束。
    
    @Author : 灵茶山艾府
    @link : https://leetcode.cn/problems/count-the-number-of-powerful-integers/solutions/2595149/shu-wei-dp-shang-xia-jie-mo-ban-fu-ti-da-h6ci
"""

from functools import lru_cache

low = int(input())
high = int(input())

low, high = str(low), str(high)
n = len(high)
diff = n - len(low)
low = '0' * diff + low

@lru_cache(None)
def dfs(i: int, limit_low: bool, limit_high: bool, is_num: bool) -> int:
    if i == len(high):
        return int(is_num)
    res = 0

    if i < diff and not is_num:  # 可以跳过当前数位
        res += dfs(i + 1, True, False, False)

    # 第 i 个数位可以从 lo 枚举到 hi
    # 如果对数位还有其它约束，应当只在下面的 for 循环做限制，不应修改 lo 或 hi
    lo = int(low[i]) if limit_low else 0
    hi = int(high[i]) if limit_high else 9

    for d in range(max(lo, 1 - is_num), hi + 1):  # 如果前面没有填数字，必须从 1 开始（因为不能有前导零）
        res += dfs(i + 1, limit_low and d == lo, limit_high and d == hi, True)
    return res
