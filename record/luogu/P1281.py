fmin = lambda x, y: x if x < y else y
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

m = n * 5
f = [0] * (2 * m + 1)
for i, (x, y) in enumerate(a):
    nf = [10**9] * (2 * m + 1)
    d = x - y
    for j in range(m - 5 * i, m + 5 * i + 1):
        nf[j + d] = fmin(nf[j + d], f[j])
        nf[j - d] = fmin(nf[j - d], f[j] + 1)
    f = nf[:]

ans = 10**9
for i in range(m + 1):
    ans = fmin(f[m - i], f[m + i])
    if ans < 10**9:
        print(ans)
        break
