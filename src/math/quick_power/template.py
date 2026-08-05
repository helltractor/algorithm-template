#!/usr/bin/env python3

from math import log2, sqrt
from typing import Tuple


class FastPower:

    def _quick_power(self, x: int, y: int, mod: int = 1_000_000_007) -> float:
        ans = 1.0
        while y:
            if y % 2:
                ans = ans * x % mod
            x = x * x % mod
            y //= 2
        return ans

    def pow(self, x: float, n: int) -> float:
        return self._quick_power(x, n) if n >= 0 else 1.0 / self._quick_power(x, -n)

    def pow_rec(self, x: int, n: int, mod: int = 31) -> float:
        if n == 0:
            return 1.0
        ans = self.quick_power_rec(x, n // 2) % mod
        return ans * ans % mod if n % 2 == 0 else ans * ans * x % mod

    def pow_sum(self, x: int, n: int, mod: int = 1_000_000_007) -> Tuple[int, int]:
        """计算 x^n, x^(n-1) + ... + x^0 模 mod"""
        if mod == 1:
            return 0, 0
        sum_, p = 1, x
        start = int(log2(n)) - 1

        for d in range(start, -1, -1):
            sum_ = sum_ * (p + 1) % mod
            p = p * p % mod
            if (n >> d) & 1:
                sum_ = (sum_ + p) % mod
                p = p * x % mod
        return p, sum_


# @Link: https://github.com/981377660LMT/algorithm-study/blob/master/19_%E6%95%B0%E5%AD%A6/%E7%9F%A9%E9%98%B5%E8%BF%90%E7%AE%97/%E7%9F%A9%E9%98%B5%E5%BF%AB%E9%80%9F%E5%B9%82/%E5%85%89%E9%80%9F%E5%B9%82.py
class BlockFastPower:
    __slots__ = "_max", "_mod", "_div_pow", "_mod_pow"

    def __init__(self, base: int, n: int, mod: int = 1_000_000_007) -> None:
        self._max = max_ = int(sqrt(n)) + 1
        self._mod = mod
        self._div_pow = [0] * (max_ + 1)
        self._mod_pow = [0] * (max_ + 1)
        cur = 1
        for i in range(max_ + 1):
            self._div_pow[i] = cur
            cur = cur * base % mod
        cur = 1
        last = self._div_pow[max_]
        for i in range(max_ + 1):
            self._mod_pow[i] = cur
            cur = cur * last % mod

    def pow(self, n: int) -> int:
        assert n <= self._max * self._max

        return self._div_pow[n // self._max] * self._mod_pow[n % self._max] % self._mod
