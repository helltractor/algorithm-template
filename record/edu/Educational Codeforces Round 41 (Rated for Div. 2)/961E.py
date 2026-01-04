class FenwickTree:
    __slots__ = ["n", "c"]

    def __init__(self, n: int) -> None:
        self.n = n
        self.c = [0] * (n + 1)

    def update(self, x: int, delta: int) -> None:
        while x <= self.n:
            self.c[x] += delta
            x += x & -x

    def query(self, x: int) -> int:
        s = 0
        while x > 0:
            s += self.c[x]
            x -= x & -x
        return s

    def range_query(self, l: int, r: int) -> int:
        return self.query(r) - self.query(l - 1)


n = int(input())
a = list(map(int, input().split()))
b = sorted((x, i) for i, x in enumerate(a, 1))
ans = 0
j = n - 1
tree = FenwickTree(n + 1)
for i in range(n, 0, -1):
    while j >= 0 and b[j][0] >= i:
        tree.update(b[j][1], 1)
        j -= 1
    y = min(n, a[i - 1])
    if i + 1 <= y:
        ans += tree.range_query(i + 1, y)
print(ans)
