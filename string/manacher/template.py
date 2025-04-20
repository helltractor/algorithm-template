#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/10/10 下午8:50

class Manacher:
    def __init__(self, s):
        self.s = s
        self.halfLen = self.manacher(s)
        
    @staticmethod
    def manacher(s: str) -> str:
        t = '#'.join(f'^{s}$')
        n = len(t)
        halfLen = [0] * n
        mid = r = 0
        for i in range(1, n - 1):
            if i < r:
                halfLen[i] = min(r - i, halfLen[2 * mid - i])
            while t[i + halfLen[i] + 1] == t[i - halfLen[i] - 1]:
                halfLen[i] += 1
            if i + halfLen[i] > r:
                mid, r = i, i + halfLen[i]
        return halfLen
    