#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/8/29 下午12:38

import time
import unittest

from src.math.prime_factor.template import Primes


class TestGeneral(unittest.TestCase):
    n = 2 * pow(10, 4)

    def test_primes_linear(self):
        start_time = time.time()
        primes = Primes.primes_linear(self.n)
        end_time = time.time()
        print("primes_linear:", end_time - start_time)

    def test_primes_ealich(self):
        start_time = time.time()
        primes = Primes.primes_ealich(self.n)
        end_time = time.time()
        print("primes_ealich:", end_time - start_time)

    def test_primes_enumeration(self):
        start_time = time.time()
        Primes.primes_enumeration(self.n)
        end_time = time.time()
        print("primes_enumeration:", end_time - start_time)

    def test_primes_enumeration_plus(self):
        start_time = time.time()
        Primes.primes_enumeration_plus(self.n)
        end_time = time.time()
        print("primes_enumeration_plus:", end_time - start_time)


if __name__ == "__main__":
    unittest.main()
