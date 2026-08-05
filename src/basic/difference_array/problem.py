#!/usr/bin/env python3

from itertools import accumulate


class Solution:

    @staticmethod
    def lc1094_car_pooling():
        """
        link: https://leetcode.cn/problems/car-pooling/
        tag: array | difference array | prefix sum

        Use 1D difference array — range-add then scan prefix sum.
        """
        trips = [[2, 1, 5], [3, 3, 7]]
        capacity = 4
        max_to = max(t[2] for t in trips)
        diff = [0] * (max_to + 1)
        for num, frm, to in trips:
            diff[frm] += num
            diff[to] -= num
        ok = all(s <= capacity for s in accumulate(diff))
        print(ok)

    @staticmethod
    def lc1109_corp_flight_bookings():
        """
        link: https://leetcode.cn/problems/corporate-flight-bookings/
        tag: array | difference array
        """
        bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
        n = 5
        diff = [0] * (n + 1)
        for frm, to, seats in bookings:
            diff[frm - 1] += seats
            diff[to] -= seats
        ans = list(accumulate(diff[:-1]))
        print(ans)  # [10, 55, 45, 25, 25]

    @staticmethod
    def lc2536_range_add_matrix():
        """
        link: https://leetcode.cn/problems/increment-submatrices-by-one/
        tag: array | 2D difference array | matrix

        2D difference array — range-add on submatrices.
        """
        n = 3
        queries = [[1, 1, 2, 2], [0, 0, 1, 1]]
        diff = [[0] * (n + 2) for _ in range(n + 2)]
        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c1] -= 1
            diff[r2 + 1][c2 + 1] += 1
        # 2D prefix sum to recover final matrix
        mat = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                mat[i][j] = diff[i][j]
                if i:
                    mat[i][j] += mat[i - 1][j]
                if j:
                    mat[i][j] += mat[i][j - 1]
                if i and j:
                    mat[i][j] -= mat[i - 1][j - 1]
        for row in mat:
            print(row)
