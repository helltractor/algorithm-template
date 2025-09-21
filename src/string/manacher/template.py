#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Manacher:
    def __init__(self, s: str) -> None:
        self.s = s
        self.halfLen = self.manacher(s)

    @staticmethod
    def manacher(s: str) -> str:
        t = "#".join(f"^{s}$")
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
