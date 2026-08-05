from bisect import bisect_left

fmax = lambda x, y: x if x > y else y


class FenwickTree:
    __slots__ = ["n", "c"]

    def __init__(self, n: int) -> None:
        self.n = n
        self.c = [-(10**18)] * (n + 1)

    def update(self, x: int, v: int) -> None:
        while x <= self.n:
            self.c[x] = fmax(self.c[x], v)
            x += x & -x

    def pre(self, x: int) -> int:
        res = -(10**18)
        while x > 0:
            res = fmax(res, self.c[x])
            x -= x & -x
        return res


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    pre = [0] * (n + 1)
    for i in range(n):
        pre[i + 1] = pre[i] + a[i]
    b = sorted(set(pre))
    m = len(b)
    ans = 0
    ltree = FenwickTree(m)
    gtree = FenwickTree(m)
    mx = [-(10**18)] * m
    for r, v in enumerate(pre):
        idx = bisect_left(b, v)
        if r > 0:
            ans = fmax(fmax(ltree.pre(idx) + r, gtree.pre(m - idx - 1) - r), mx[idx])
        ltree.update(idx + 1, ans - r)
        gtree.update(m - idx, ans + r)
        mx[idx] = fmax(mx[idx], ans)
    print(ans)
