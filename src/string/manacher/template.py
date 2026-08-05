#!/usr/bin/env python3


class Manacher:
    def __init__(self, s: str) -> None:
        self.s = s
        self.half_len = self.manacher(s)

    @staticmethod
    def manacher(s: str) -> str:
        t = "#".join(f"^{s}$")
        n = len(t)
        half_len = [0] * n
        mid = r = 0
        for i in range(1, n - 1):
            if i < r:
                half_len[i] = min(r - i, half_len[2 * mid - i])
            while t[i + half_len[i] + 1] == t[i - half_len[i] - 1]:
                half_len[i] += 1
            if i + half_len[i] > r:
                mid, r = i, i + half_len[i]
        return half_len
