#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from src.math.quick_power.template import FastPower, BlockFastPower


class TestGeneral(unittest.TestCase):

    def test_pow(self):
        pow = FastPower().pow
        self.assertEqual(pow(2, 10), 1024)
        self.assertEqual(pow(2, -2), 0.25)
        self.assertEqual(pow(2, 0), 1)
        self.assertEqual(pow(0, 0), 1)

    def test_pow_sum(self):
        pow_sum = FastPower().pow_sum
        self.assertEqual(pow_sum(2, 20), (1048576, 1048575))
        self.assertEqual(pow_sum(2, 10), (1024, 1023))
        self.assertEqual(pow_sum(2, 1), (2, 1))

    def test_block_pow(self):
        block_pow = BlockFastPower(2, 10)
        self.assertEqual(block_pow.pow(10), 1024)
        self.assertEqual(block_pow.pow(0), 1)


if __name__ == "__main__":
    unittest.main()
