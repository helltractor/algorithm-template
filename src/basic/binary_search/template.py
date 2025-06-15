#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2024/8/7 上午1:46


class BinarySearch:

    @staticmethod
    def find_left(l: int, r: int, f: callable) -> int:
        while l <= r:
            mid = l + (r - l) // 2
            if f(mid):
                l = mid + 1
            else:
                r = mid - 1
        return l

    @staticmethod
    def find_right(l: int, r: int, f: callable) -> int:
        while l <= r:
            mid = l + (r - l) // 2
            if f(mid):
                r = mid - 1
            else:
                l = mid + 1
        return r
