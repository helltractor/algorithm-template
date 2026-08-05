#!/usr/bin/env python3

from string.kmp.template import KMP


class Solution:

    @staticmethod
    def lc28_str_str():
        """
        link: https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/
        tag: string | kmp | two pointers
        """
        haystack, needle = "sadbutsad", "sad"
        kmp = KMP(haystack, needle)
        print(kmp.matches[0] if kmp.matches else -1)

    @staticmethod
    def lc796_rotate_string():
        """
        link: https://leetcode.cn/problems/rotate-string/
        tag: string | kmp | string matching
        """
        s, goal = "abcde", "cdeab"
        kmp = KMP(s + s, goal)
        print(len(goal) == len(s) and bool(kmp.matches))

    @staticmethod
    def lc459_repeated_substring():
        """
        link: https://leetcode.cn/problems/repeated-substring-pattern/
        tag: string | kmp | next array
        """
        s = "abab"
        n = len(s)
        nxt = KMP("", "").computeNxt(s)
        # If s is composed of repeated substrings, the last nxt value gives the period
        period = n - nxt[-1]
        print(period > 0 and n % period == 0)
