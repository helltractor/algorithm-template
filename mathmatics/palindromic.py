#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/12/17 12:25


class Palindromic:
    
    @staticmethod
    def convert_by_string():
        """生成所有回文数（字符串转换）"""
        pal = []
        MX = 10 ** 5
        for i in range(1, MX):
            s = str(i)
            pal.append(int(s + s[::-1]))
            pal.append(int(s + s[::-1][1:]))
        pal.sort()
        return pal
    
    @staticmethod
    def convert_by_number():
        """按顺序从小到大生成所有回文数（不用字符串转换）"""
        pal = []
        MX = 10 ** 4
        base = 1
        while base <= MX:
            for i in range(base, base * 10):
                x = i
                t = i // 10
                while t:
                    x = x * 10 + t % 10
                    t //= 10
                pal.append(x)
            if base <= MX // 10:
                for i in range(base, base * 10):
                    x = t = i
                    while t:
                        x = x * 10 + t % 10
                        t //= 10
                    pal.append(x)
            base *= 10
        pal.append(10 ** 8 + 1)  # 哨兵，防止下标越界
        return pal
