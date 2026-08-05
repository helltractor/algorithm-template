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


n, q = map(int, input().split())
a = list(map(int, input().split()))
qs = [list(map(int, input().split())) for _ in range(q)]

tree = FenwickTree(n + 1)
for i, x in enumerate(a):
    tree.update(i + 1, x)

for row in qs:
    if row[0] == 2:
        l, r = row[1:]
        print(tree.range_query(l, r))
    else:
        x = row[1] - 1
        delta = a[x + 1] - a[x]
        a[x], a[x + 1] = a[x + 1], a[x]
        tree.update(x + 1, delta)
        tree.update(x + 2, -delta)
