#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/9/23 下午4:02

class Factorial:
    
    def __init__(self, l=10**6+5, mod=10**9+7):
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
    def build_inv(n, mod):
        inv = [0] * (n + 1)
        inv[0] = 1
        for i in range(2, n + 1):
            inv[i] = (mod - mod // i) * inv[mod % i] % mod
        return inv
    
    def comb(self, n, r):
        return self.fact[n] * self.finv[r] % self.mod * self.finv[n - r] % self.mod if n >= r >= 0 else 0
    
    def factorial(self, n):
        return self.fact[n]
    
    def fac_inv(self, n):
        return self.finv[n]
    
    def inverse(self, n):
        return self.fact[n - 1] * self.finv[n] % self.mod
    
    def perm(self, n, r):
        return self.fact[n] * self.finv[n - r] % self.mod if n >= r >= 0 else 0
