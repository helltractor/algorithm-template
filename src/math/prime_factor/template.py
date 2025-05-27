#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/8/2 下午2:56

from collections import Counter
from typing import List


class Primes:

    @staticmethod
    def fool_primes(n):
        """暴力枚举"""
        primes = []
        for i in range(2, n):
            if all(i % j != 0 for j in range(2, i)):
                primes.append(i)
        return primes

    @staticmethod
    def primes_enumeration(n: int) -> int:
        """枚举"""

        def is_prime(n):
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True if n > 1 else False

        primes = []
        for i in range(2, n):
            if is_prime(i):
                primes.append(i)
        return primes

    @staticmethod
    def primes_enumeration_plus(n: int) -> int:
        """枚举优化"""

        def is_prime(n):
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True if n > 1 else False

        primes = []
        for i in range(2, n):
            if is_prime(i):
                primes.append(i)
        return primes

    @staticmethod
    def primes_linear(n: int) -> int:
        """线性（欧拉）筛"""
        primes = []
        is_prime = [False] * 2 + [True] * (n - 2)
        for i in range(2, n):
            if is_prime[i]:
                primes.append(i)
            for p in primes:
                if i * p >= n:
                    break
                is_prime[i * p] = False
                if i % p == 0:
                    break
        primes.extend([n, n])  # 防止下标越界
        return primes

    @staticmethod
    def primes_ealich(n: int) -> int:
        """埃氏筛"""
        primes = []
        is_prime = [False] * 2 + [True] * (n - 2)
        for i in range(2, n):
            if is_prime[i]:
                primes.append(i)
                for j in range(i**2, n, i):
                    is_prime[j] = False
        primes.extend([n, n])  # 防止下标越界
        return primes

    @staticmethod
    def count_primes_factor(n: int) -> int:
        """统计每个数的质因子的个数"""
        cnt = [0] * n
        for i in range(2, n):
            if cnt[i] == 0:
                for j in range(i, n, i):
                    cnt[j] += 1
        return cnt

    @staticmethod
    def primes_factor(n: int) -> List[List[int]]:
        """统计每个数的质因子"""
        fac = [[] for _ in range(n)]
        for i in range(2, n):
            if not fac[i]:
                for j in range(i, n, i):
                    fac[j].append(i)
        return fac

    @staticmethod
    def prime_factor(n: int) -> Counter:
        """
        统计一个数的质因子个数
        a = p1 ^ e1 * p2 ^ e2 * p3 ^ e3
        """
        cnt = Counter()
        d = 2
        while d * d <= n:
            while n % d == 0:
                cnt[d] += 1
                n //= d
            d += 1
        if n > 1:
            cnt[n] += 1
        return cnt
