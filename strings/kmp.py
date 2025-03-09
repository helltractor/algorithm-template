#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/1/14 12:12


class KMP:
    def __init__(self, s, t):
        self.s = s
        self.t = t
        self.matches = self.kmp(s, t)
        
    def computeNxt(self, t):
        n = len(t)
        j = 0
        nxt = [0] * n
        
        for i in range(1, n):
            while j > 0 and t[i] != t[j]:
                j = nxt[j - 1]
            if t[i] == t[j]:
                j += 1
            nxt[i] = j
        
        return nxt
    
    def kmp(self, s, t):
        m, n = len(s), len(t)
        j = 0
        matches = []
        nxt = self.computeNxt(t)
        
        for i in range(m):
            while j > 0 and s[i] != t[j]:
                j = nxt[j - 1]
            if s[i] == t[j]:
                j += 1
            if j == n:
                matches.append(i - n + 1)
                j = nxt[j - 1]
        
        return matches
    