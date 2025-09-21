#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Factorial:
    def __init__(self, l: int = 10**6 + 5, mod: int = 10**9 + 7):
        self.mod = mod
        self.l = l
        self.fact = fact = [1] * (l + 1)
        self.finv = finv = [1] * (l + 1)
        for i in range(1, l + 1):
            fact[i] = fact[i - 1] * i % mod
        finv[l] = pow(fact[l], mod - 2, mod)
        for i in range(l - 1, -1, -1):
            finv[i] = finv[i + 1] * (i + 1) % mod

    @staticmethod
    def build_inv(n: int, mod: int) -> list:
        inv = [0] * (n + 1)
        inv[0] = 1
        for i in range(2, n + 1):
            inv[i] = (mod - mod // i) * inv[mod % i] % mod
        return inv

    def comb(self, n: int, r: int) -> int:
        return self.fact[n] * self.finv[r] % self.mod * self.finv[n - r] % self.mod if n >= r >= 0 else 0
    
    def factorial(self, n: int) -> int:
        return self.fact[n]

    def fac_inv(self, n: int) -> int:
        return self.finv[n]

    def inverse(self, n: int) -> int:
        return self.fact[n - 1] * self.finv[n] % self.mod

    def perm(self, n: int, r: int) -> int:
        return self.fact[n] * self.finv[n - r] % self.mod if n >= r >= 0 else 0
