from math import comb


n, m = map(int, input().split())
a = [set() for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    a[x].add(y)
    a[y].add(x)
ans = []
for i in range(1, n + 1):
    x = n - 1 - len(a[i])
    ans.append(0 if x < 3 else comb(x, 3))
print(*ans)
