#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2025-04-15 12:30:49


class TrinarySearch:

    @staticmethod
    def find_ceil_point_int(l: int, r: int, f: callable, error=1) -> int:
        ll, rr = l, r
        while l <= r - error:
            diff = (r - l) // 3
            ml = l + diff
            mr = r - diff
            fl = f(ml)
            fr = f(mr)
            if fl < fr:
                r = mr - 1
            elif fl > fr:
                l = ml + 1
            else:
                l = ml + 1
                r = mr - 1
        res = l
        for x in range(l - 5, r + 5):
            if ll <= x <= rr and f(x) > f(res):
                res = x
        return res
