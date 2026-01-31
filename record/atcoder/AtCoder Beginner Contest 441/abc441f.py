fmax = lambda x, y: x if x > y else y
n, m = map(int, input().split())
p = [0] * n
v = [0] * n
for i in range(n):
    pi, vi = map(int, input().split())
    p[i] = pi
    v[i] = vi

f = [[0] * (m + 1) for _ in range(n + 1)]
f2 = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n):
    f[i + 1] = f[i][:]
    for j in range(m + 1):
        if j >= p[i]:
            f[i + 1][j] = fmax(f[i + 1][j], f[i][j - p[i]] + v[i])

for i in reversed(range(n)):
    f2[i] = f2[i + 1][:]
    for j in range(m + 1):
        if j >= p[i]:
            f2[i][j] = fmax(f2[i][j], f2[i + 1][j - p[i]] + v[i])

tar = f[n][m]
ans = []
for i in range(n):
    mx = 0
    for j in range(m + 1):
        x = f[i][j] + f2[i + 1][m - j]
        if x > mx:
            mx = x

    mx2 = 0
    limit = m - p[i]
    for j in range(limit + 1):
        x = f[i][j] + f2[i + 1][limit - j]
        if x > mx2:
            mx2 = x

    if mx < tar:
        ans.append("A")
    elif mx2 < tar - v[i]:
        ans.append("C")
    else:
        ans.append("B")

print("".join(ans))
