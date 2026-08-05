fmax = lambda x, y: x if x > y else y
s, n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(s):
    a = list(map(int, input().split()))
    for j, v in enumerate(a):
        v = v << 1 | 1
        if v <= m:
            g[j].append(v)

f = [0] * (m + 1)
for i, row in enumerate(g):
    row.sort()
    t = []
    for j, w in enumerate(row):
        if j == len(row) - 1 or w != row[j + 1]:
            t.append(((i + 1) * (j + 1), w))
    for j in range(m, -1, -1):
        for v, w in t:
            if j < w:
                break
            f[j] = fmax(f[j], f[j - w] + v)
print(f[-1])
