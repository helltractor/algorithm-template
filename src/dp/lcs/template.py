#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2025/4/15 上午11:03

class LongestCommonSequence:

    @staticmethod
    def lcs(s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        max = lambda x, y: x if x > y else y
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[n][m]
    
    @staticmethod
    def get_lcs(s1: str, s2: str) -> str:
        n, m = len(s1), len(s2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        max = lambda x, y: x if x > y else y
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
        i, j = n, m
        lcs_str = []
        while i > 0 and j > 0:
            if s1[i - 1] == s2[j - 1]:
                lcs_str.append(s1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] >= dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
        
        return ''.join(reversed(lcs_str))
    