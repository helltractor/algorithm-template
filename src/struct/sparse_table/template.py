#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: liupengsay
# @Link: https://github.com/liupengsay/PyIsTheBestLang/src/struct/sparse_table/template.py


class SparseTable:
    def __init__(self, lst, fun):
        """static range queries can be performed as long as the range_merge_to_disjoint fun satisfies monotonicity"""
        self.n = n = len(lst)
        self.bit = bit = [0] * (n + 1)
        self.fun = fun
        for i in range(2, n + 1):
            bit[i] = bit[i >> 1] + 1
        for i in range(n + 1):
            assert bit[i] == (i.bit_length() - 1 if i else i.bit_length())
        self.st = st = [[0] * n for _ in range(bit[-1] + 1)]
        st[0] = lst
        for i in range(1, bit[-1] + 1):
            for j in range(n - (1 << i) + 1):
                st[i][j] = fun(st[i - 1][j], st[i - 1][j + (1 << (i - 1))])

    def query(self, left, right):
        """index start from 0"""
        assert 0 <= left <= right < self.n
        pos = self.bit[right - left + 1]
        return self.fun(self.st[pos][left], self.st[pos][right - (1 << pos) + 1])

    def bisect_right(self, left, val, initial):
        """index start from 0"""
        assert 0 <= left < self.n
        # find the max right such that st.query(left, right) >= val
        pos = left
        pre = initial  # 0 or (1<<32)-1
        for x in range(self.bit[-1], -1, -1):
            if (
                pos + (1 << x) - 1 < self.n and self.fun(self.st[x][pos], pre) >= val
            ):  # can by any of >= > <= <
                pre = self.fun(self.st[x][pos], pre)
                pos += 1 << x
        # may be pos=left and st.query(left, left) < val
        if pos > left:
            pos -= 1
        else:
            pre = self.st[0][left]
        assert left <= pos < self.n
        return pos, pre

    def bisect_right_length(self, left):
        """index start from 0"""
        assert 0 <= left < self.n
        # find the max right such that st.query(left, right) < right-left+1
        pos = left
        pre = 0
        for x in range(self.bit[-1], -1, -1):
            if (
                pos + (1 << x) - 1 < self.n
                and self.fun(self.st[x][pos], pre) > pos + (1 << x) - left
            ):
                pre = self.fun(self.st[x][pos], pre)
                pos += 1 << x
        if pos == left and self.st[0][pos] == 1:
            return True, pos
        if pos < self.n and self.fun(pre, self.st[0][pos]) == pos + 1 - left:
            return True, pos
        return False, pos
