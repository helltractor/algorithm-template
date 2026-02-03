n, m, x = map(int, input().split())
a = list(map(int, input().split()))
qs = [list(map(int, input().split())) for _ in range(m)]
d = {}
L = [-1] * (n + 1)
for i, v in enumerate(a):
    y = x ^ v
    L[i + 1] = L[i]
    if y in d:
        L[i + 1] = max(L[i + 1], d[y])
    d[v] = i

for l, r in qs:
    print("yes" if L[r] >= l - 1 else "no")
