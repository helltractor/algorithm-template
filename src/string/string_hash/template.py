#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/3/11 15:50


class StringHash:
    def __init__(self, s : str) -> None:
        """字符串哈希，用O(n)时间预处理，用O(1)时间获取段的哈希值"""
        self.n = n = len(s)
        self.BASE = BASE = 131313  # 进制 31,131,13131,13331,131313
        self.MOD = MOD = 10 ** 13 + 7  # 10**13+37 ,10**13+51 ,10**13+99 ,10**13+129 ,10**13+183
        self.h = h = [0] * (n + 1)
        self.p = p = [1] * (n + 1)
        for i in range(1, n + 1):
            p[i] = (p[i - 1] * BASE) % MOD
            h[i] = (h[i - 1] * BASE + ord(s[i - 1])) % MOD

    def get_hash(self, l: int, r: int) -> int:
        """用O(1)时间获取闭区间[l,r]（即s[l:r]）的哈希值，比切片要快"""
        return (self.h[r + 1] - self.h[l] * self.p[r - l + 1]) % self.MOD

    def get_addhash(self, l1: int, r1: int, l2: int, r2: int) -> int:
        """获取 s[l1:r1+1] 和 s[l2:r2+1] 拼接的哈希值，要求不能有重叠部分，且有先后顺序"""
        return (self.get_hash(l1, r1) * self.p[r2 - l2 + 1] + self.get_hash(l2, r2)) % self.MOD
