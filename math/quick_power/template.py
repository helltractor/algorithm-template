#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/11/30 19:57


class QuickPow:
    
    def _quick_power(self, x: int, y: int, mod: int = 31) -> float:
        ans = 1.0
        while y:
            if y % 2:
                ans = ans * x % mod
            x = x * x % mod
            y //= 2
        return ans
    
    def quick_power(self, x: float, n: int) -> float:
        return self._quick_power(x, n) if n >= 0 else 1.0 / self._quick_power(x, -n)
    
    def quick_power_rec(self, x: int, y: int, mod: int = 31) -> float:
        if y == 0:
            return 1.0
        ans = self.quick_power_rec(x, y // 2) % mod
        return ans * ans % mod if y % 2 == 0 else ans * ans * x % mod
