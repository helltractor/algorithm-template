from typing import List


class PrefixSum2D:
    __slots__ = ["pre"]

    def __init__(self, mat: List[List[int]]):
        n, m = len(mat), len(mat[0])
        self.pre = pre = [[0] * (m + 1) for _ in range(n + 1)]
        for i, row in enumerate(mat):
            for j, v in enumerate(row):
                pre[i + 1][j + 1] = pre[i][j + 1] + pre[i + 1][j] - pre[i][j] + v

    def find(self, r1: int, c1: int, r2: int, c2: int) -> int:
        """查询以(r1,c1)为左上角，(r2,c2)为右下角的矩形区间内所有值的和"""
        return (
            self.pre[r2 + 1][c2 + 1]
            - self.pre[r2 + 1][c1]
            - self.pre[r1][c2 + 1]
            + self.pre[r1][c1]
        )


class Difference2D:
    __slots__ = ["m", "n", "diff"]

    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.diff = [[0] * (n + 2) for _ in range(m + 2)]

    def add(self, r1, c1, r2, c2, delta):
        """下标从0开始，区间变化delta"""
        diff = self.diff
        diff[r1 + 1][c1 + 1] += delta
        diff[r1 + 1][c2 + 2] -= delta
        diff[r2 + 2][c1 + 1] -= delta
        diff[r2 + 2][c2 + 2] += delta

    def get(self):
        diff = self.diff
        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                diff[i][j] += diff[i][j - 1] + diff[i - 1][j] - diff[i - 1][j - 1]
        diff = diff[1:-1]
        for i, row in enumerate(diff):
            diff[i] = row[1:-1]
        return diff


m = 2000
base = m * m
diff = Difference2D(m, m)
a = []
n = int(input())
for _ in range(n):
    u, d, l, r = map(int, input().split())
    a.append((u, d, l, r))
    diff.add(u - 1, l - 1, d - 1, r - 1, 1)

cnt = diff.get()
for i, row in enumerate(cnt):
    for j, v in enumerate(row):
        if v:
            base -= 1
        if v != 1:
            cnt[i][j] = 0

pre = PrefixSum2D(cnt)
ans = []
for u, d, l, r in a:
    ans.append(base + pre.find(u - 1, l - 1, d - 1, r - 1))
print("\n".join(map(str, ans)))
